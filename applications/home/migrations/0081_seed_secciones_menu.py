from django.db import migrations


SECCIONES_INICIALES = [
    # (clave, nombre visible, activo, orden)
    ('inicio', 'Inicio', True, 0),
    ('blog', 'Blog', True, 10),
    ('mapa', 'Mapa', True, 20),
    ('galeria', 'Galería', True, 30),
    ('recetas', 'Recetas', False, 40),  # oculta hoy: la portada se enfoca en el marketplace
    ('servicios', 'Servicios (Preguntas y Moneda)', True, 50),
    ('donativos', 'Donativos', True, 60),
    ('empresas', 'Empresas (Explorar negocios)', True, 70),
    ('extranjeros', 'Extranjeros (Consulados, Embajadas, Abogados)', True, 80),
    ('contacto', 'Contacto', True, 90),
]


def seed_secciones(apps, schema_editor):
    SeccionMenu = apps.get_model('home', 'SeccionMenu')
    for clave, nombre, activo, orden in SECCIONES_INICIALES:
        SeccionMenu.objects.get_or_create(
            clave=clave,
            defaults={'nombre': nombre, 'activo': activo, 'orden': orden},
        )


def eliminar_secciones(apps, schema_editor):
    SeccionMenu = apps.get_model('home', 'SeccionMenu')
    claves = [c for c, *_ in SECCIONES_INICIALES]
    SeccionMenu.objects.filter(clave__in=claves).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0080_seccionmenu'),
    ]

    operations = [
        migrations.RunPython(seed_secciones, eliminar_secciones),
    ]
