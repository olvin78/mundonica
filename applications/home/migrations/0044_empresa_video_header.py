# Generated by Django 5.1.3 on 2024-12-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_alter_empresa_imagen_alter_empresa_imagen_header_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='video_header',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='video_header'),
        ),
    ]
