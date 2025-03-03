# Generated by Django 5.1.3 on 2025-01-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0073_remove_empresa_propietario_sitio_web_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='plato_menu1',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='plato_menu2',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='plato_menu3',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='plato_menu4',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='plato_menu5',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='plato_menu6',
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion10_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 10'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion1_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 1'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion2_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 2'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion3_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 3'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion4_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 4'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion5_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 5'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion6_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 6'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion7_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 7'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion8_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 8'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descriptcion9_plato_menu',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción Plato 9'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen10_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 10'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen1_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 1'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen2_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 2'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen3_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 3'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen4_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 4'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen5_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 5'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen6_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 6'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen7_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 7'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen8_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 8'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen9_plato_menu',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/platos/', verbose_name='Imagen Plato 9'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre10_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 10'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre1_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 1'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre2_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 2'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre3_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 3'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre4_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 4'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre5_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 5'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre6_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 6'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre7_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 7'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre8_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 8'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='nombre9_plato_menu',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Plato 9'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio10_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 10'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio1_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 1'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio2_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 2'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio3_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 3'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio4_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 4'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio5_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 5'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio6_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 6'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio7_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 7'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio8_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 8'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='precio9_plato_menu',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Plato 9'),
        ),
    ]
