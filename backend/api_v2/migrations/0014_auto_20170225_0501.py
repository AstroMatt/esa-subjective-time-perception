# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0013_auto_20170225_0458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trial',
            old_name='time_mean_all',
            new_name='interval_all',
        ),
        migrations.RenameField(
            model_name='trial',
            old_name='time_mean_blue',
            new_name='interval_blue',
        ),
        migrations.RenameField(
            model_name='trial',
            old_name='time_mean_red',
            new_name='interval_red',
        ),
        migrations.RenameField(
            model_name='trial',
            old_name='time_mean_white',
            new_name='interval_white',
        ),
    ]
