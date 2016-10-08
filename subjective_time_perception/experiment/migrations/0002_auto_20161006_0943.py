# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='click',
            options={'ordering': ['datetime'], 'verbose_name': 'Click event', 'verbose_name_plural': 'Click events'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['datetime'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AddField(
            model_name='experiment',
            name='device',
            field=models.CharField(default='computer 1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experiment',
            name='polarization',
            field=models.CharField(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical'), ('cross', 'Cross'), ('mixed', 'Mixed')], default='horizontal', max_length=15),
            preserve_default=False,
        ),
    ]
