# Generated by Django 5.1.3 on 2024-12-07 17:00

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_abogado_imagen_alter_blog_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='abogado',
            name='resumen',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
