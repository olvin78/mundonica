import csv
from collections import Counter
import hashlib
import json
from pathlib import Path

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.core.validators import EmailValidator, URLValidator
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from django.utils.text import slugify

from applications.home.models import Empresa, ImportacionPerfil, TipoEmpresa


EXPECTED_HEADERS = [
    'external_id', 'profile_type', 'name', 'category', 'country', 'region',
    'province', 'city', 'public_address', 'postal_code', 'latitude',
    'longitude', 'public_phone', 'public_email', 'website',
    'nicaragua_connection', 'source_url', 'notes', 'contact_channel',
    'contact_readiness', 'address_kind', 'location_precision',
    'verification_status', 'publication_status', 'claim_status', 'source_sheet',
]
PROFILE_TYPES = {value for value, _ in Empresa.TIPOS_PERFIL}
ADDRESS_KINDS = {value for value, _ in ImportacionPerfil.TIPOS_DIRECCION}
LOCATION_PRECISIONS = {value for value, _ in ImportacionPerfil.PRECISIONES}
CONTACT_READINESS = {'pending_validation', 'indirect_only'}
PUBLICATION_STATUSES = {'draft_review'}
CLAIM_STATUSES = {'unclaimed'}
PUBLIC_FIELD_MAP = {
    'name': 'nombre_de_la_empresa',
    'profile_type': 'tipo_perfil',
    'country': 'pais',
    'region': 'region',
    'province': 'provincia',
    'city': 'ciudad',
    'public_address': 'direccion',
    'postal_code': 'codigo_postal',
    'latitude': 'latitud',
    'longitude': 'longitud',
    'public_phone': 'telefono',
    'public_email': 'email',
    'website': 'sitio_web',
    'nicaragua_connection': 'relacion_nicaragua',
}


def normalized_url(value):
    value = value.strip()
    if value and '://' not in value:
        return f'https://{value}'
    return value


def row_hash(row):
    payload = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


class Command(BaseCommand):
    help = 'Importa perfiles de Mundonica desde el CSV maestro de forma idempotente.'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=Path)
        parser.add_argument('--dry-run', action='store_true', help='Simula la importación y revierte todos los cambios.')
        parser.add_argument('--strict', action='store_true', help='Cancela toda la importación si alguna fila es inválida.')

    def handle(self, *args, **options):
        path = options['csv_path']
        if not path.exists() or not path.is_file():
            raise CommandError(f'No existe el archivo: {path}')

        try:
            with path.open(encoding='utf-8-sig', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                if reader.fieldnames != EXPECTED_HEADERS:
                    raise CommandError(
                        'Encabezados incorrectos.\n'
                        f'Esperados: {EXPECTED_HEADERS}\n'
                        f'Recibidos: {reader.fieldnames}'
                    )
                rows = [(line, {key: (value or '').strip() for key, value in row.items()})
                        for line, row in enumerate(reader, start=2)]
        except UnicodeDecodeError as exc:
            raise CommandError('El CSV debe estar codificado como UTF-8 o UTF-8 con BOM.') from exc

        id_counts = Counter(row['external_id'] for _, row in rows if row['external_id'])
        repeated_ids = {external_id for external_id, count in id_counts.items() if count > 1}
        validated = []
        errors = []
        for line, row in rows:
            row_errors = self.validate_row(row, repeated_ids)
            if row_errors:
                errors.append((line, row.get('external_id') or '(sin ID)', row_errors))
            else:
                row['website'] = normalized_url(row['website'])
                row['source_url'] = normalized_url(row['source_url'])
                validated.append((line, row))

        for line, external_id, row_errors in errors:
            self.stderr.write(self.style.ERROR(
                f'Fila {line} [{external_id}] rechazada: {"; ".join(row_errors)}'
            ))

        if errors and options['strict']:
            raise CommandError(
                f'Modo estricto: se cancela la importación por {len(errors)} fila(s) inválida(s).'
            )

        summary = {'creados': 0, 'actualizados': 0, 'sin_cambios': 0, 'ambiguos': 0,
                   'protegidos': 0, 'invalidos': len(errors)}
        with transaction.atomic():
            for line, external_id, row_errors in errors:
                self.record_validation_error(line, external_id, row_errors, rows)
            for line, row in validated:
                result, detail = self.import_row(row)
                summary[result] += 1
                if detail:
                    stream = self.stderr if result in {'ambiguos', 'protegidos'} else self.stdout
                    stream.write(f'Fila {line} [{row["external_id"]}]: {detail}')
            if options['dry_run']:
                transaction.set_rollback(True)

        prefix = 'SIMULACIÓN' if options['dry_run'] else 'IMPORTACIÓN'
        self.stdout.write(self.style.SUCCESS(
            f'{prefix}: creados={summary["creados"]}, actualizados={summary["actualizados"]}, '
            f'sin_cambios={summary["sin_cambios"]}, ambiguos={summary["ambiguos"]}, '
            f'protegidos={summary["protegidos"]}, inválidos={summary["invalidos"]}.'
        ))
        if options['dry_run']:
            self.stdout.write('No se ha modificado la base de datos.')

    def validate_row(self, row, repeated_ids):
        errors = []
        for field in ('external_id', 'profile_type', 'name', 'category', 'country'):
            if not row[field]:
                errors.append(f'{field} es obligatorio')
        if len(row['external_id']) > 50:
            errors.append('external_id supera 50 caracteres')
        if row['external_id'] in repeated_ids:
            errors.append('external_id está repetido en el CSV')
        if row['profile_type'] and row['profile_type'] not in PROFILE_TYPES:
            errors.append('profile_type no reconocido')
        if row['publication_status'] not in PUBLICATION_STATUSES:
            errors.append('publication_status no reconocido')
        if row['claim_status'] not in CLAIM_STATUSES:
            errors.append('claim_status no reconocido')
        if row['address_kind'] not in ADDRESS_KINDS:
            errors.append('address_kind no reconocido')
        if row['location_precision'] not in LOCATION_PRECISIONS:
            errors.append('location_precision no reconocido')
        if row['contact_readiness'] not in CONTACT_READINESS:
            errors.append('contact_readiness no reconocido')

        if row['public_phone'] and ('@' in row['public_phone'] or '://' in row['public_phone']):
            errors.append('public_phone contiene un correo o una URL')
        if row['public_email']:
            try:
                EmailValidator()(row['public_email'])
            except ValidationError:
                errors.append('public_email no es un correo válido')
        for field in ('website', 'source_url'):
            if row[field]:
                try:
                    URLValidator()(normalized_url(row[field]))
                except ValidationError:
                    errors.append(f'{field} no es una URL válida')

        coordinates = []
        for field, lower, upper in (('latitude', -90, 90), ('longitude', -180, 180)):
            if row[field]:
                try:
                    number = float(row[field].replace(',', '.'))
                    if not lower <= number <= upper:
                        raise ValueError
                    coordinates.append(number)
                except ValueError:
                    errors.append(f'{field} no es una coordenada válida')
        if bool(row['latitude']) != bool(row['longitude']):
            errors.append('latitude y longitude deben aparecer juntas')
        if len(row['postal_code']) > 20:
            errors.append('postal_code supera 20 caracteres')
        return errors

    def record_validation_error(self, line, external_id, row_errors, rows):
        row = next(item for item_line, item in rows if item_line == line)
        stable_id = row.get('external_id', '')
        if not stable_id or len(stable_id) > 50:
            stable_id = f'ERROR-FILA-{line}-{row_hash(row)[:12]}'
        ImportacionPerfil.objects.update_or_create(
            identificador_externo=stable_id,
            defaults={
                'empresa': None,
                'fuente_informacion': 'mundonica_perfiles.csv',
                'hoja_origen': row.get('source_sheet', '')[:100],
                'hash_fila': row_hash(row),
                'resultado_validacion': 'error',
                'datos_ultima_importacion': row,
                'campos_en_conflicto': {},
                'errores_validacion': '; '.join(row_errors),
            },
        )

    def import_row(self, row):
        external_id = row['external_id']
        empresa = Empresa.objects.filter(identificador_externo=external_id).first()
        if not empresa:
            ambiguous = self.find_ambiguous(row)
            if ambiguous:
                ids = ', '.join(str(pk) for pk in ambiguous)
                return 'ambiguos', f'coincidencia con empresa(s) histórica(s) ID {ids}; requiere revisión.'
            empresa = self.create_empresa(row)
            self.update_import_metadata(empresa, row, {}, 'valid')
            return 'creados', ''

        metadata = ImportacionPerfil.objects.filter(identificador_externo=external_id).first()
        previous = metadata.datos_ultima_importacion if metadata else {}
        changed = {field: {'anterior': previous.get(field, ''), 'nuevo': row[field]}
                   for field in PUBLIC_FIELD_MAP if previous and previous.get(field, '') != row[field]}
        protected = bool(empresa.propietario_sitio_web_id or empresa.estado_reclamacion == 'claimed')
        current_hash = row_hash(row)
        if metadata and metadata.hash_fila == current_hash:
            return 'sin_cambios', ''
        if protected:
            self.update_import_metadata(empresa, row, changed, 'warnings' if changed else 'valid')
            return 'protegidos', f'{len(changed)} cambio(s) público(s) reservado(s) para revisión.'

        self.apply_public_fields(empresa, row)
        empresa.tipo_empresa = self.category_for(row["category"])
        empresa.fecha_actualizacion = timezone.now()
        empresa.save()
        self.update_import_metadata(empresa, row, {}, 'valid')
        return 'actualizados', ''

    def find_ambiguous(self, row):
        query = Q(nombre_de_la_empresa__iexact=row['name'])
        for field, model_field in (
            ('public_email', 'email'), ('public_phone', 'telefono'),
            ('website', 'sitio_web'), ('public_address', 'direccion'),
        ):
            if row[field]:
                query |= Q(**{f'{model_field}__iexact': normalized_url(row[field]) if field == 'website' else row[field]})
        return list(Empresa.objects.filter(identificador_externo__isnull=True).filter(query).values_list('pk', flat=True))

    def category_for(self, name):
        plantilla = {"Restaurante": "restaurante", "Peluquería": "peluqueria", "Comercio": "comercio"}.get(name, "generica")
        category, created = TipoEmpresa.objects.get_or_create(nombre=name, defaults={"plantilla_perfil": plantilla})
        return category

    def unique_slug(self, name):
        base = slugify(name)[:130] or 'perfil'
        candidate = base
        suffix = 2
        while Empresa.objects.filter(nombreUrl=candidate).exists():
            candidate = f'{base[:140-len(str(suffix))]}-{suffix}'
            suffix += 1
        return candidate

    def create_empresa(self, row):
        category = self.category_for(row["category"])
        empresa = Empresa(
            identificador_externo=row['external_id'], tipo_empresa=category,
            nombreUrl=self.unique_slug(row['name']), estado_publicacion='draft',
            estado_verificacion='pending', estado_reclamacion='unclaimed',
        )
        self.apply_public_fields(empresa, row)
        empresa.save()
        return empresa

    def apply_public_fields(self, empresa, row):
        for csv_field, model_field in PUBLIC_FIELD_MAP.items():
            value = row[csv_field]
            if csv_field == 'website':
                value = normalized_url(value)
            if csv_field == 'public_address' and row['address_kind'] != 'business_or_public':
                value = ''
            setattr(empresa, model_field, value)

    def update_import_metadata(self, empresa, row, conflicts, result):
        defaults = {
            'identificador_externo': row['external_id'],
            'fuente_informacion': 'mundonica_perfiles.csv',
            'url_origen': row['source_url'], 'hoja_origen': row['source_sheet'],
            'notas_internas': row['notes'], 'canal_contacto': row['contact_channel'],
            'disponibilidad_contacto': row['contact_readiness'],
            'tipo_direccion': row['address_kind'],
            'precision_localizacion': row['location_precision'],
            'verificacion_original': row['verification_status'],
            'hash_fila': row_hash(row), 'resultado_validacion': result,
            'datos_ultima_importacion': row, 'campos_en_conflicto': conflicts,
            'errores_validacion': '', 'empresa': empresa,
        }
        ImportacionPerfil.objects.update_or_create(identificador_externo=row['external_id'], defaults=defaults)
