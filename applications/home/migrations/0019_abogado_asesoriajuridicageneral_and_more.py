# Generated by Django 5.1.3 on 2024-12-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_abogado_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='abogado',
            name='asesoriajuridicageneral',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='abogado',
            name='mediacionyarbitraje',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='abogado',
            name='redaccionyrevisiondedocuemntos',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='abogado',
            name='representacionlegal',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
