# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0023_trial_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='time',
            field=models.CharField(blank=True, choices=[('morning', 'Morning'), ('evening', 'Evening'), ('other', 'Other')], default=None, max_length=50, null=True, verbose_name='Time'),
        ),
    ]
