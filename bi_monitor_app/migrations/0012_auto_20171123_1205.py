# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bi_monitor_app', '0011_monitorbiapimsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='houranalysis',
            name='api_delay_bg_10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='houranalysis',
            name='web_delay_bg_10',
            field=models.IntegerField(default=0),
        ),
    ]
