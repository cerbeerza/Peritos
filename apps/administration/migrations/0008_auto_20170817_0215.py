# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20170817_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telefono_cel',
            field=models.IntegerField(default='0'),
        ),
    ]