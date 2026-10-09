# Mundonica 2.0 — Fase 1

## Alcance y estado

La fase 1 amplía `Empresa` como entidad canónica para negocios, organizaciones, personas y proyectos. Conserva IDs, slugs, propietarios, imágenes, favoritos, valoraciones y URLs históricas. Los datos internos del CSV se guardan en `ImportacionPerfil` y no se exponen por vistas públicas ni por la API.

La auditoría previa al despliegue encontró y corrigió localmente: reversión insegura de estados históricos, dependencia implícita de `TipoEmpresa(id=1)`, falta de registro administrativo de filas rechazadas, mapas/datos de contacto ficticios en plantillas, mapas para direcciones no publicables, duplicación de metadatos SEO y pérdida de filtros al cambiar de categoría.

## Migraciones

- `0087_directorio_perfiles_fase1`: añade campos opcionales, estados, selector de plantilla e `ImportacionPerfil`.
- `0088_publicar_perfiles_historicos`: publica los perfiles preexistentes (identificados porque aún no tienen `identificador_externo`) y asigna las plantillas históricas conocidas. Su reversión es deliberadamente un `noop`: no oculta perfiles ni borra datos.
- `0089_actualizar_fecha_perfil`: activa la actualización automática de `fecha_actualizacion`.
- `0090_auditar_importaciones_fase1`: elimina el supuesto histórico `TipoEmpresa(id=1)` y permite conservar, sin crear una `Empresa`, la validación y el motivo de una fila CSV rechazada.

Todas son compatibles con SQLite. No cambian PK, slugs ni relaciones de favoritos/valoraciones. Los perfiles históricos quedan publicados; los perfiles creados posteriormente conservan el valor predeterminado `draft`.

## Importación

```bash
python manage.py importar_perfiles mundonica_perfiles.csv --dry-run
python manage.py importar_perfiles mundonica_perfiles.csv
python manage.py importar_perfiles mundonica_perfiles.csv --strict
```

El importador comprueba exactamente los 26 encabezados, usa UTF-8/UTF-8 BOM, conserva códigos postales y teléfonos como texto, valida email, URL, coordenadas, estados, `address_kind` y `location_precision`, y usa `external_id` como única clave estable. No fusiona por nombre: las coincidencias históricas ambiguas quedan pendientes de revisión. Los perfiles con propietario o reclamados no se sobrescriben.

`--dry-run` revierte también categorías y registros auxiliares de error. `--strict` valida todo antes de abrir la transacción y no escribe si encuentra una fila inválida. En modo no estricto, los errores se conservan en `ImportacionPerfil` sin empresa asociada para su revisión en Admin.

El CSV actual produce 100 filas válidas y 4 inválidas: `CULT-0008`, `CULT-0013`, `CULT-0016` y `CULT-0019`. No se corrigen automáticamente.

## Seguridad y publicación

Las consultas públicas, API, favoritos, valoraciones, mapa, detalle y sitemap filtran por `published`. Un borrador o archivado no es público. Los usuarios propietarios solo acceden a sus empresas y sus formularios no incluyen estados administrativos ni `identificador_externo`. `ImportacionPerfil` exige permisos de Admin, es de solo lectura y muestra errores y conflictos.

Publicar requiere una acción explícita en Admin. La acción omite perfiles importados cuyo resultado no sea `valid`. Los perfiles importados usan la ficha genérica segura hasta recibir curación editorial; las plantillas especializadas y URLs históricas permanecen disponibles para los negocios anteriores.

Los mapas solo muestran coordenadas numéricas dentro de rango, con dirección publicable y precisión compatible. No existe una coordenada alternativa ficticia.

## Verificación local

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate --plan
python manage.py test
```

La prueba de migración parte de `0086` en una base temporal y comprueba PK, slug, propietario, favorito, valoración, publicación y `identificador_externo`. Las pruebas del importador cubren primera/segunda importación, actualización, alta, duplicados, ambigüedad, propietario, inválidos, vacíos, caracteres especiales, ceros iniciales, teléfono textual, `dry-run` y `strict`.

## Despliegue futuro con Docker

No ejecutar `docker compose up` antes del respaldo y ensayo: `docker-compose.yml` ejecuta `migrate --noinput` y `collectstatic --noinput` automáticamente al arrancar `web`.

1. Abrir una ventana de mantenimiento y detener escrituras.
2. Crear un respaldo consistente de SQLite con `sqlite3 db.sqlite3 ".backup 'backups/db-AAAAmmdd-HHMM.sqlite3'"`; no copiar el fichero mientras haya escrituras.
3. Identificar el volumen real de medios con `docker compose config --volumes`/`docker volume ls` y respaldar `media_data`. Los estáticos son regenerables con `collectstatic`.
4. Verificar que la copia SQLite abre y restaurar base y medios en un entorno de ensayo.
5. En ensayo, ejecutar el plan, las migraciones, las pruebas y el dry-run del CSV; comprobar conteos, PK, slugs, propietarios, favoritos, valoraciones, URLs, Admin, API, mapa y sitemap.
6. Verificar propietario y permisos de `./db.sqlite3`: el contenedor monta el fichero en `/app/db.sqlite3` y actualmente ejecuta como `root`, lo que puede dejar el fichero del host con propietario/permisos inesperados.
7. Desplegar de forma controlada. Importar el CSV solo tras revisar el dry-run; los nuevos perfiles quedan en borrador y se publican explícitamente desde Admin.

`compose.dev.yaml` monta el repositorio completo y usa `runserver`; es únicamente para desarrollo. `.env.docker` debe existir fuera de Git con secretos reales; `.env.docker.example` contiene solo marcadores.

## Reversión

1. Retirar tráfico y detener escrituras.
2. Restaurar la copia completa de `db.sqlite3` y el volumen de medios tomada antes del despliegue.
3. Restaurar la versión anterior del código y reiniciar los servicios.
4. Verificar URLs y conteos.

No se recomienda confiar en una migración inversa para una reversión de producción: `0088` no despublica perfiles al revertir, por seguridad, y la recuperación íntegra es la restauración del respaldo validado.

## Pendiente editorial

- Corregir en la fuente las cuatro filas desplazadas.
- Revisar y publicar explícitamente los perfiles importados.
- Normalizar manualmente categorías y territorios cuando proceda.
- Las reclamaciones avanzadas e invitaciones pertenecen a fases posteriores.

## Resultado de la auditoría local

- `check`: sin incidencias.
- `makemigrations --check --dry-run`: sin cambios pendientes.
- Plan sobre la SQLite local: únicamente `0090`; no se aplicó.
- Suite explícita completa: 33 pruebas ejecutadas, 33 correctas, 0 fallidas.
- El descubrimiento automático `python manage.py test` devuelve 0 pruebas por la disposición actual de los módulos; por eso se ejecutaron explícitamente los cuatro módulos existentes.
- CSV real en SQLite temporal: 104 filas, 100 válidas, 4 inválidas; `--dry-run` dejó 0 empresas y 0 auxiliares.
- CSV real en modo estricto: cancelado por 4 inválidas; dejó 0 empresas y 0 auxiliares.
