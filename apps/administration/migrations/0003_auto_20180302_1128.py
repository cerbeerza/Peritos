# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-02 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_auto_20180212_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='archivo_ant',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='archivo_ci',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='archivo_titulo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
