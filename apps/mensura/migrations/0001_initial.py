# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-21 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MensuraGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=4)),
                ('num_mensura', models.IntegerField()),
                ('promedio', models.FloatField()),
                ('empresa', models.CharField(max_length=40)),
                ('situacion', models.CharField(max_length=20)),
                ('usuario_id', models.CharField(max_length=10)),
            ],
        ),
    ]
