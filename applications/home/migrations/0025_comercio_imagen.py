# Generated by Django 5.1.3 on 2024-12-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_abogado_verificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/comercio'),
        ),
    ]
