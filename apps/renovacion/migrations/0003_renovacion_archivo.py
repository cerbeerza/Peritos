# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-10 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renovacion', '0002_auto_20180410_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='renovacion',
            name='archivo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]