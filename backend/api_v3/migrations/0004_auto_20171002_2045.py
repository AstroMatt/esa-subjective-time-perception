# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v3', '0003_auto_20170928_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='is_valid',
            field=models.NullBooleanField(db_index=True, default=None, verbose_name='Valid?'),
        ),
    ]
