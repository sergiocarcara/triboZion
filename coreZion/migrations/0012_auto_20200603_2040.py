# Generated by Django 3.0.6 on 2020-06-04 00:40

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coreZion', '0011_auto_20200531_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha_Atleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('nome', models.CharField(max_length=11, verbose_name='Nome')),
                ('nomesobre', models.CharField(max_length=100, verbose_name='Nome Copleto')),
                ('texto', models.TextField(max_length=500, verbose_name='Obsevações')),
                ('imagem', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='', verbose_name='Foto')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da criação')),
                ('faixas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreZion.Faixa')),
            ],
            options={
                'verbose_name_plural': 'Alunos',
            },
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
    ]
