# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellido_p', models.CharField(max_length=50)),
                ('apellido_m', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('genero', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=80)),
                ('region', models.CharField(max_length=30)),
                ('comuna', models.CharField(max_length=50)),
                ('estado_civil', models.CharField(choices=[('SOLTERO', 'SOLTERO(A)'), ('CASADO', 'CASADO(A)'), ('VIUDO', 'VIUDO(A)')], max_length=20)),
                ('telefono_casa', models.IntegerField()),
                ('telefono_cel', models.IntegerField()),
                ('profesion', models.CharField(max_length=40)),
                ('universidad', models.CharField(max_length=50)),
                ('archivo_titulo', models.CharField(max_length=300)),
                ('archivo_ci', models.CharField(max_length=300)),
                ('archivo_ant', models.CharField(max_length=300)),
                ('year_titulo', models.IntegerField()),
                ('empresa', models.CharField(max_length=50)),
                ('telefono_empresa', models.IntegerField()),
                ('direccion_empresa', models.CharField(max_length=80)),
            ],
        ),
    ]
