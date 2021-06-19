# Generated by Django 3.0.6 on 2020-06-27 01:04

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreZion', '0021_diretoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='diretoria',
            name='imagem',
            field=models.ImageField(default=1, storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='', verbose_name='Foto'),
            preserve_default=False,
        ),
    ]
