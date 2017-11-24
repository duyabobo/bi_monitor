# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bi_monitor_app', '0006_auto_20171118_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='HourAnalysis',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('from_timestamp', models.IntegerField(default=0)),
                ('end_timestamp', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 't_hour_analysis',
            },
        ),
        migrations.RenameField(
            model_name='biaccessanalysis',
            old_name='end_timestamp',
            new_name='hour_analysis_id',
        ),
        migrations.RemoveField(
            model_name='biaccessanalysis',
            name='from_timestamp',
        ),
        migrations.AddField(
            model_name='noteworthylog',
            name='hour_analysis_id',
            field=models.IntegerField(default=0),
        ),
    ]