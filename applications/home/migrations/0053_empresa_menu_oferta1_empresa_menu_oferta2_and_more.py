# Generated by Django 5.1.3 on 2024-12-23 11:50

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_empresa_menu_regalo1_empresa_menu_regalo2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='menu_oferta1',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='menu_oferta2',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='menu_oferta3',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
