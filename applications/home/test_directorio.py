import csv
import io
import tempfile
from pathlib import Path

from django.contrib.auth.models import Permission, User
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from django.conf import settings
from django.urls import reverse

from .management.commands.importar_perfiles import EXPECTED_HEADERS
from .models import Empresa, ImportacionPerfil, TipoEmpresa


class DirectorioBase(TestCase):
    def setUp(self):
        self.categoria = TipoEmpresa.objects.create(nombre='Comercio', plantilla_perfil='comercio')

    def empresa(self, **kwargs):
        defaults = {
            'nombre_de_la_empresa': 'Perfil de prueba', 'nombreUrl': 'perfil-prueba',
            'tipo_empresa': self.categoria, 'estado_publicacion': 'published',
            'tipo_perfil': 'business',
        }
        defaults.update(kwargs)
        return Empresa.objects.create(**defaults)


class DirectorioPublicoTests(DirectorioBase):
    def test_listado_y_detalle_excluyen_borradores_y_archivados(self):
        publicada = self.empresa()
        self.empresa(nombre_de_la_empresa='Borrador', nombreUrl='borrador', estado_publicacion='draft')
        self.empresa(nombre_de_la_empresa='Archivado', nombreUrl='archivado', estado_publicacion='archived')
        response = self.client.get(reverse('home_app:explorar_negocios'))
        self.assertContains(response, publicada.nombre_de_la_empresa)
        self.assertNotContains(response, 'Borrador')
        self.assertNotContains(response, 'Archivado')
        self.assertEqual(self.client.get('/borrador/').status_code, 404)
        self.assertEqual(self.client.get('/archivado/').status_code, 404)

    def test_busqueda_y_filtros_ampliados(self):
        self.empresa(tipo_perfil='organization', region='Euskadi', provincia='Gipuzkoa',
                     ciudad='Donostia', relacion_nicaragua='Cultura nicaragüense')
        response = self.client.get(reverse('home_app:explorar_negocios'), {
            'q': 'Cultura', 'tipo_perfil': 'organization', 'region': 'Euskadi',
            'provincia': 'Gipuzkoa', 'ciudad': 'Donostia',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_obj'].paginator.count, 1)

    def test_perfil_generico_no_muestra_datos_internos_ni_mapa_ficticio(self):
        categoria = TipoEmpresa.objects.create(nombre='Asociación cultural')
        perfil = self.empresa(tipo_empresa=categoria, tipo_perfil='organization',
                              nombreUrl='asociacion', identificador_externo='CULT-TEST', relacion_nicaragua='Vínculo público')
        ImportacionPerfil.objects.create(
            empresa=perfil, identificador_externo='CULT-TEST', notas_internas='SECRETO',
            tipo_direccion='registry_not_for_visit', precision_localizacion='unknown',
        )
        response = self.client.get('/asociacion/')
        self.assertTemplateUsed(response, 'perfil_generico.html')
        self.assertContains(response, 'Vínculo público')
        self.assertNotContains(response, 'SECRETO')
        self.assertNotContains(response, '12.136389')
        self.assertNotContains(response, 'id="perfil-map"')

    def test_api_es_lista_blanca_y_solo_publicados(self):
        publicada = self.empresa(identificador_externo='MUN-API')
        ImportacionPerfil.objects.create(empresa=publicada, identificador_externo='MUN-API', notas_internas='SECRETO')
        self.empresa(nombre_de_la_empresa='Oculta', nombreUrl='oculta', estado_publicacion='draft')
        response = self.client.get('/api/v1/empresas/')
        self.assertEqual(response.status_code, 200)
        payload = response.json()['results']
        self.assertEqual(len(payload), 1)
        self.assertNotIn('identificador_externo', payload[0])
        self.assertNotIn('estado_reclamacion', payload[0])
        self.assertNotIn('notas_internas', str(payload))

    def test_mapa_no_inventa_coordenadas_ni_marca_perfiles_sin_posicion(self):
        self.empresa(nombre_de_la_empresa="Sin coordenadas", latitud="", longitud="")
        response = self.client.get(reverse("home_app:mapa"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "12.136389")
        self.assertNotContains(response, "Sin coordenadas")

    def test_sitemap_solo_incluye_publicados(self):
        self.empresa()
        self.empresa(nombre_de_la_empresa='Oculta', nombreUrl='oculta', estado_publicacion='draft')
        response = self.client.get('/sitemap.xml')
        self.assertContains(response, '/perfil-prueba/')
        self.assertNotContains(response, '/oculta/')


class PermisosEmpresaTests(DirectorioBase):
    def test_usuario_no_puede_editar_empresa_ajena(self):
        propietario = User.objects.create_user('propietario', password='x')
        intruso = User.objects.create_user('intruso', password='x')
        empresa = self.empresa(propietario_sitio_web=propietario)
        self.client.force_login(intruso)
        self.assertEqual(self.client.get(reverse('home_app:actualizar_empresa', kwargs={'pk': empresa.pk})).status_code, 404)

    def test_propietario_puede_abrir_edicion_sin_campos_administrativos(self):
        propietario = User.objects.create_user('propietario', password='x')
        empresa = self.empresa(propietario_sitio_web=propietario)
        self.client.force_login(propietario)
        response = self.client.get(reverse('home_app:actualizar_empresa', kwargs={'pk': empresa.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('estado_publicacion', response.context['form'].fields)
        self.assertNotIn('identificador_externo', response.context['form'].fields)


class ImportadorTests(DirectorioBase):
    def row(self, **changes):
        row = dict.fromkeys(EXPECTED_HEADERS, '')
        row.update({
            'external_id': 'MUN-TEST', 'profile_type': 'business', 'name': 'Ñandutí Café',
            'category': 'Restaurante', 'country': 'España', 'region': 'Euskadi',
            'province': 'Gipuzkoa', 'city': 'Donostia', 'postal_code': '20001',
            'public_email': 'hola@example.com', 'website': 'example.com',
            'nicaragua_connection': 'Gastronomía nicaragüense',
            'source_url': 'https://example.com/fuente', 'notes': 'Nota interna',
            'contact_channel': 'email', 'contact_readiness': 'pending_validation',
            'address_kind': 'business_or_public', 'location_precision': 'municipality_only',
            'verification_status': 'Datos públicos contrastados',
            'publication_status': 'draft_review', 'claim_status': 'unclaimed',
            'source_sheet': 'Negocios',
        })
        row.update(changes)
        return row

    def csv_file(self, rows):
        handle = tempfile.NamedTemporaryFile('w', encoding='utf-8-sig', newline='', suffix='.csv', delete=False)
        writer = csv.DictWriter(handle, fieldnames=EXPECTED_HEADERS)
        writer.writeheader()
        writer.writerows(rows)
        handle.close()
        self.addCleanup(Path(handle.name).unlink, missing_ok=True)
        return handle.name

    def test_csv_real_dry_run_procesa_100_y_rechaza_4(self):
        output = io.StringIO()
        errors = io.StringIO()
        call_command("importar_perfiles", Path(settings.BASE_DIR) / "mundonica_perfiles.csv", dry_run=True, stdout=output, stderr=errors)
        self.assertIn("creados=100", output.getvalue())
        self.assertIn("inválidos=4", output.getvalue())
        for external_id in ("CULT-0008", "CULT-0013", "CULT-0016", "CULT-0019"):
            self.assertIn(external_id, errors.getvalue())
        self.assertEqual(Empresa.objects.count(), 0)

    def test_importacion_crea_borrador_es_idempotente_y_actualiza(self):
        path = self.csv_file([self.row()])
        call_command('importar_perfiles', path)
        empresa = Empresa.objects.get(identificador_externo='MUN-TEST')
        self.assertEqual(empresa.estado_publicacion, 'draft')
        self.assertEqual(empresa.nombre_de_la_empresa, 'Ñandutí Café')
        self.assertEqual(ImportacionPerfil.objects.count(), 1)
        call_command('importar_perfiles', path)
        self.assertEqual(Empresa.objects.count(), 1)
        path2 = self.csv_file([self.row(public_phone='+34 600 000 000')])
        call_command('importar_perfiles', path2)
        empresa.refresh_from_db()
        self.assertEqual(empresa.telefono, '+34 600 000 000')

    def test_dry_run_no_escribe(self):
        path = self.csv_file([self.row()])
        call_command('importar_perfiles', path, dry_run=True)
        self.assertFalse(Empresa.objects.filter(identificador_externo='MUN-TEST').exists())

    def test_strict_cancela_csv_invalido_y_detecta_desplazamiento(self):
        path = self.csv_file([self.row(public_phone='persona@example.com', public_email='https://example.com')])
        with self.assertRaises(CommandError):
            call_command('importar_perfiles', path, strict=True)
        self.assertFalse(Empresa.objects.filter(identificador_externo='MUN-TEST').exists())

    def test_coincidencia_ambigua_no_crea(self):
        self.empresa(nombre_de_la_empresa='Ñandutí Café')
        path = self.csv_file([self.row()])
        call_command('importar_perfiles', path)
        self.assertFalse(Empresa.objects.filter(identificador_externo='MUN-TEST').exists())

    def test_perfil_con_propietario_conserva_datos_y_registra_conflicto(self):
        propietario = User.objects.create_user('duena', password='x')
        empresa = self.empresa(nombre_de_la_empresa='Nombre propietario', identificador_externo='MUN-TEST', propietario_sitio_web=propietario)
        ImportacionPerfil.objects.create(empresa=empresa, identificador_externo='MUN-TEST', datos_ultima_importacion=self.row(name='Nombre anterior'))
        path = self.csv_file([self.row(name='Nombre nuevo')])
        call_command('importar_perfiles', path)
        empresa.refresh_from_db()
        empresa.importacion_perfil.refresh_from_db()
        self.assertEqual(empresa.nombre_de_la_empresa, 'Nombre propietario')
        self.assertIn('name', empresa.importacion_perfil.campos_en_conflicto)

    def test_registro_nuevo_duplicados_vacios_y_texto_se_conservan(self):
        path = self.csv_file([
            self.row(external_id='MUN-NUEVO', postal_code='01234', public_phone='00123'),
            self.row(external_id='MUN-DUP', name='Primero'),
            self.row(external_id='MUN-DUP', name='Segundo'),
            self.row(external_id='MUN-VACIO', public_email='', website='', postal_code=''),
        ])
        output, errors = io.StringIO(), io.StringIO()
        call_command('importar_perfiles', path, stdout=output, stderr=errors)
        nuevo = Empresa.objects.get(identificador_externo='MUN-NUEVO')
        self.assertEqual(nuevo.codigo_postal, '01234')
        self.assertEqual(nuevo.telefono, '00123')
        self.assertTrue(Empresa.objects.filter(identificador_externo='MUN-VACIO').exists())
        self.assertFalse(Empresa.objects.filter(identificador_externo='MUN-DUP').exists())
        self.assertIn('inválidos=2', output.getvalue())
        self.assertEqual(ImportacionPerfil.objects.filter(identificador_externo='MUN-DUP', resultado_validacion='error').count(), 1)

    def test_dry_run_revierte_tambien_errores_auxiliares(self):
        path = self.csv_file([self.row(public_email='correo-invalido')])
        call_command('importar_perfiles', path, dry_run=True)
        self.assertEqual(Empresa.objects.count(), 0)
        self.assertEqual(ImportacionPerfil.objects.count(), 0)

    def test_strict_csv_real_no_escribe_nada(self):
        with self.assertRaises(CommandError):
            call_command('importar_perfiles', Path(settings.BASE_DIR) / 'mundonica_perfiles.csv', strict=True)
        self.assertEqual(Empresa.objects.count(), 0)
        self.assertEqual(ImportacionPerfil.objects.count(), 0)

    def test_importado_usa_ficha_generica_y_slug_unico(self):
        self.empresa(nombre_de_la_empresa='Ñandutí Café histórico', nombreUrl='nanduti-cafe')
        path = self.csv_file([self.row(external_id='MUN-ESPECIAL', name='Ñandutí Café')])
        call_command('importar_perfiles', path)
        empresa = Empresa.objects.get(identificador_externo='MUN-ESPECIAL')
        empresa.estado_publicacion = 'published'
        empresa.save()
        self.assertNotEqual(empresa.nombreUrl, 'nanduti-cafe')
        response = self.client.get(f'/{empresa.nombreUrl}/')
        self.assertTemplateUsed(response, 'perfil_generico.html')
        self.assertContains(response, f'<link rel="canonical" href="http://testserver/{empresa.nombreUrl}/">', html=True)


class SeguridadAdminYMapaTests(DirectorioBase):
    def test_anonimo_no_edita_y_usuario_normal_no_accede_importaciones(self):
        empresa = self.empresa()
        response = self.client.get(reverse('home_app:actualizar_empresa', kwargs={'pk': empresa.pk}))
        self.assertEqual(response.status_code, 302)
        usuario = User.objects.create_user('normal', password='x', is_staff=True)
        self.client.force_login(usuario)
        self.assertEqual(self.client.get(reverse('admin:home_importacionperfil_changelist')).status_code, 403)

    def test_admin_no_publica_perfil_con_errores(self):
        admin_user = User.objects.create_superuser('adminfase1', 'admin@example.com', 'x')
        valido = self.empresa(nombre_de_la_empresa='Válido', nombreUrl='valido', estado_publicacion='draft', identificador_externo='VALIDO')
        invalido = self.empresa(nombre_de_la_empresa='Inválido', nombreUrl='invalido', estado_publicacion='draft', identificador_externo='INVALIDO')
        ImportacionPerfil.objects.create(empresa=valido, identificador_externo='VALIDO', resultado_validacion='valid')
        ImportacionPerfil.objects.create(empresa=invalido, identificador_externo='INVALIDO', resultado_validacion='error', errores_validacion='error de prueba')
        self.client.force_login(admin_user)
        response = self.client.post(reverse('admin:home_empresa_changelist'), {
            'action': 'publicar_perfiles', '_selected_action': [valido.pk, invalido.pk], 'index': 0,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        valido.refresh_from_db(); invalido.refresh_from_db()
        self.assertEqual(valido.estado_publicacion, 'published')
        self.assertEqual(invalido.estado_publicacion, 'draft')

    def test_mapa_excluye_coordenadas_no_publicables_y_fuera_de_rango(self):
        privada = self.empresa(nombre_de_la_empresa='Privada', nombreUrl='privada', latitud='43.1', longitud='-2.1', identificador_externo='PRIVADA')
        ImportacionPerfil.objects.create(empresa=privada, identificador_externo='PRIVADA', tipo_direccion='registry_not_for_visit', precision_localizacion='address_unverified')
        self.empresa(nombre_de_la_empresa='Fuera', nombreUrl='fuera', latitud='91', longitud='181')
        response = self.client.get(reverse('home_app:mapa'))
        self.assertNotContains(response, 'Privada')
        self.assertNotContains(response, 'Fuera')

    def test_directorio_pagina_conserva_filtros(self):
        for numero in range(13):
            self.empresa(nombre_de_la_empresa=f'Perfil {numero}', nombreUrl=f'perfil-{numero}', region='Euskadi', ciudad='Donostia')
        response = self.client.get(reverse('home_app:explorar_negocios'), {'region': 'Euskadi', 'ciudad': 'Donostia'})
        self.assertTrue(response.context['is_paginated'])
        self.assertContains(response, 'region=Euskadi')
        self.assertContains(response, 'ciudad=Donostia')

    def test_api_oculta_direccion_y_coordenadas_no_publicables(self):
        privada = self.empresa(nombre_de_la_empresa='API privada', nombreUrl='api-privada', latitud='43.1', longitud='-2.1', direccion='Dato privado', identificador_externo='API-PRIVADA')
        ImportacionPerfil.objects.create(empresa=privada, identificador_externo='API-PRIVADA', tipo_direccion='registry_not_for_visit', precision_localizacion='address_unverified')
        payload = self.client.get('/api/v1/empresas/').json()['results'][0]
        self.assertIsNone(payload['direccion'])
        self.assertIsNone(payload['latitud'])
        self.assertIsNone(payload['longitud'])

    def test_plantillas_historicas_renderizan_seo_dinamico(self):
        restaurante = TipoEmpresa.objects.create(nombre='Restaurante', plantilla_perfil='restaurante')
        peluqueria = TipoEmpresa.objects.create(nombre='Peluquería', plantilla_perfil='peluqueria')
        perfiles = [
            self.empresa(nombre_de_la_empresa='Histórico comercio', nombreUrl='historico-comercio'),
            self.empresa(nombre_de_la_empresa='Histórico restaurante', nombreUrl='historico-restaurante', tipo_empresa=restaurante),
            self.empresa(nombre_de_la_empresa='Histórico peluquería', nombreUrl='historico-peluqueria', tipo_empresa=peluqueria),
        ]
        for perfil in perfiles:
            response = self.client.get(f'/{perfil.nombreUrl}/')
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, f'<title>{perfil.nombre_de_la_empresa} |')
            self.assertContains(response, f'<link rel="canonical" href="http://testserver/{perfil.nombreUrl}/">', html=True)
            self.assertNotContains(response, 'google.com/maps/embed')
