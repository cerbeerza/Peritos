# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-02 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20180302_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='archivo_ci',
            field=models.FileField(null=True, upload_to='Archivo/'),
        ),
    ]
