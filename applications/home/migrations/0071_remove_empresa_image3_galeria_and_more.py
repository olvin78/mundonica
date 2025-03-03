# Generated by Django 5.1.3 on 2025-01-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0070_empresa_imagen1_comentario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='image3_galeria',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='image4_galeria',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='image5_galeria',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='image6_galeria',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='image7_galeria',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='image8_galeria',
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen10_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 10 de la galería'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen11_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 11 de la galería'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen1_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 1 de la galería'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen3_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 3 de la galería'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen4_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 4 de la galería'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen5_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 5 de la galería'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen6_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 6 de la galería'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen7_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 7 de la galería'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen8_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 8 de la galería'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='galeria_activo',
            field=models.BooleanField(blank=True, default=1, verbose_name='Agregar sección Galería'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='imagen2_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 2 de la galería'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='imagen9_galeria',
            field=models.ImageField(blank=True, null=True, upload_to='empresas/imagenes/galeria', verbose_name='Imagen 9 de la galería'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='titulo1_galeria',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Título de la galería'),
        ),
    ]
