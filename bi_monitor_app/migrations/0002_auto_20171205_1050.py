# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 02:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bi_monitor_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorBiApiCompareMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_recorder_id', models.IntegerField(default=0)),
                ('t_id', models.CharField(max_length=255)),
                ('t_name', models.CharField(max_length=255)),
                ('indicator_name', models.CharField(max_length=255)),
                ('indicator_id', models.CharField(max_length=255)),
                ('search_type', models.CharField(max_length=100)),
                ('today_value', models.CharField(default='', max_length=20)),
                ('compare_result', models.CharField(default='', max_length=20)),
                ('compare_value', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'monitor_bi_api_compare_msg',
            },
        ),
        migrations.RenameField(
            model_name='monitorbiaccessanalysis',
            old_name='source',
            new_name='access_source',
        ),
        migrations.RenameField(
            model_name='monitorbilogweekreport',
            old_name='source',
            new_name='access_source',
        ),
        migrations.RenameField(
            model_name='monitorbinoteworthylog',
            old_name='source',
            new_name='access_source',
        ),
        migrations.AddField(
            model_name='emailrecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 5, 10, 50, 22, 791000)),
        ),
    ]