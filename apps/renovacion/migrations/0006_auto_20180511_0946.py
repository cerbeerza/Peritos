# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renovacion', '0005_auto_20180511_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='renovacion',
            name='archivo_ant',
            field=models.FileField(null=True, upload_to='ant/'),
        ),
        migrations.AddField(
            model_name='renovacion',
            name='archivo_ci',
            field=models.FileField(null=True, upload_to='ci/'),
        ),
        migrations.AddField(
            model_name='renovacion',
            name='archivo_tit',
            field=models.FileField(null=True, upload_to='tit/'),
        ),
    ]