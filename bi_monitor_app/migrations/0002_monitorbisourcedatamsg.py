# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bi_monitor_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorBiSourceDataMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_recorder_id', models.IntegerField(default=0)),
                ('indicator_name', models.CharField(max_length=255)),
                ('search_time', models.CharField(max_length=100)),
                ('source_value', models.CharField(max_length=50)),
                ('bi_value', models.CharField(max_length=50)),
                ('deviation', models.CharField(max_length=50)),
                ('new_data_time', models.CharField(max_length=50)),
                ('script_time', models.CharField(max_length=50)),
                ('devi_reason', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'monitor_bi_source_data_msg',
            },
        ),
    ]
