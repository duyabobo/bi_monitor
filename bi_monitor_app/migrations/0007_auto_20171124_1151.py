# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 03:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bi_monitor_app', '0006_auto_20171118_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiNginxLogWeekReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_recorder_id', models.IntegerField(default=0)),
                ('analysis_type', models.IntegerField(default=0)),
                ('analysis_key', models.CharField(default='', max_length=20)),
                ('analysis_api', models.CharField(default='/api/dashboard?', max_length=200)),
                ('api_count', models.IntegerField(default=0)),
                ('percent', models.FloatField()),
                ('average_delay_microseconds', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'bi_nginx_log_week_report',
            },
        ),
        migrations.CreateModel(
            name='EmailRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_key', models.CharField(max_length=100)),
                ('analysis_datetime', models.CharField(max_length=50)),
                ('from_datetime', models.CharField(max_length=50)),
                ('end_datetime', models.CharField(max_length=50)),
                ('content_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'email_record',
            },
        ),
        migrations.CreateModel(
            name='MonitorBiApiMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_recorder_id', models.IntegerField(default=0)),
                ('t_id', models.CharField(max_length=255)),
                ('t_name', models.CharField(max_length=255)),
                ('search_time', models.CharField(max_length=100)),
                ('search_type', models.CharField(max_length=100)),
                ('indicator_name', models.CharField(max_length=255)),
                ('indicator_id', models.CharField(max_length=255)),
                ('bi_value', models.CharField(max_length=100)),
                ('compute_value', models.CharField(max_length=100)),
                ('compute_source', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'monitor_bi_api_msg',
            },
        ),
        migrations.CreateModel(
            name='MonitorBiCacheMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_recorder_id', models.IntegerField(default=0)),
                ('t_id', models.CharField(max_length=255)),
                ('t_name', models.CharField(max_length=255)),
                ('http_status', models.CharField(max_length=100)),
                ('search_type', models.CharField(max_length=100)),
                ('error_time', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2017, 11, 24, 11, 51, 17, 109000))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2017, 11, 24, 11, 51, 17, 109000))),
            ],
            options={
                'db_table': 'monitor_bi_cache_msg',
            },
        ),
        migrations.DeleteModel(
            name='WeekReport',
        ),
        migrations.DeleteModel(
            name='WeekReportItem',
        ),
        migrations.RenameField(
            model_name='biaccessanalysis',
            old_name='end_timestamp',
            new_name='email_recorder_id',
        ),
        migrations.RenameField(
            model_name='noteworthylog',
            old_name='access_timestamp',
            new_name='email_recorder_id',
        ),
        migrations.RemoveField(
            model_name='biaccessanalysis',
            name='average',
        ),
        migrations.RemoveField(
            model_name='biaccessanalysis',
            name='from_timestamp',
        ),
        migrations.RemoveField(
            model_name='biaccessanalysis',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='biaccessanalysis',
            name='num',
        ),
        migrations.RemoveField(
            model_name='biaccessanalysis',
            name='percent',
        ),
        migrations.AddField(
            model_name='biaccessanalysis',
            name='table_content',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='noteworthylog',
            name='access_datetime',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='noteworthylog',
            name='source',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='biaccessanalysis',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='noteworthylog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='biaccessanalysis',
            table='bi_access_analysis',
        ),
        migrations.AlterModelTable(
            name='noteworthylog',
            table='noteworthy_log',
        ),
    ]
