# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('renovacion', '0004_auto_20180511_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renovacion',
            name='archivo',
        ),
        migrations.RemoveField(
            model_name='renovacion',
            name='doc_ant',
        ),
        migrations.RemoveField(
            model_name='renovacion',
            name='doc_ci',
        ),
        migrations.RemoveField(
            model_name='renovacion',
            name='doc_tit',
        ),
    ]
