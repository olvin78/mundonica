# Generated by Django 5.1.3 on 2024-12-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_empresa_imagen_nosotros'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='video_nosotros',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='video_nosotros'),
        ),
    ]
