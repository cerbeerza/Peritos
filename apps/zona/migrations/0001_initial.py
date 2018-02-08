# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-08 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=80)),
                ('cod_comuna', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=80)),
                ('cod_provincia', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=80)),
                ('cod_region', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='provincia',
            name='id_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zona.Region'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='id_provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zona.Provincia'),
        ),
    ]
