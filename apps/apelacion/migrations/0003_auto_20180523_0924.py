# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apelacion', '0002_auto_20180511_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apelacion',
            name='desc_apelacion',
            field=models.TextField(),
        ),
    ]
