# Generated by Django 5.1.3 on 2024-12-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_rename_empresas_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/empresa/principal'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='imagen_portada',
            field=models.ImageField(blank=True, null=True, upload_to='images/empresa/portada'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre de la Empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='pais',
            field=models.CharField(max_length=100, verbose_name='Pais de la Empresa'),
        ),
    ]
