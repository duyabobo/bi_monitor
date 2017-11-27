# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.


class ApiAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_name', 'indicator', 'indicator_name', 'is_method', 'sub_indicator', 'sub_indicator_name', 'target_id', 'target_name', 'target_indicator', 'target_indicator_name', 'is_delete', 'is_complicate')  # list
    search_fields = ('t_id', 't_name', 'indicator', 'indicator_name')


class ApiMsgAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_name', 'search_time', 'search_type', 'indicator_name', 'indicator_id', 'bi_value', 'compute_value', 'compute_source')  # list
    search_fields = ('t_id', 't_name', 'indicator_name', 'indicator_id')


class CacheAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_name', 't_type', 'is_day', 'is_month', 'is_delete')  # list
    search_fields = ('t_id', 't_name')


class DataAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_name', 't_type', 'is_personnel', 'is_delete')  # list
    search_fields = ('t_id', 't_name')


class SourceGrouobyAdmin(admin.ModelAdmin):
    list_display = ('field_name', 'bi_job_id', 'origin_field', 'origin_db', 'origin_sel', 'origin_sql', 'origin_time_type', 'origin_field', 'target_db', 'target_sel', 'target_sql', 'target_time_type', 'middle_first_db', 'middle_first_sel', 'middle_first_sql', 'middle_first_time_type', 'middle_second_db', 'middle_second_sel', 'middle_second_sql', 'middle_second_time_type', 'is_complicate', 'is_delete')  # list
    search_fields = ('field_name', 'origin_field', 'target_field')


class TablesAdmin(admin.ModelAdmin):
    list_display = ('db_name', 't_id', 't_name', 't_column', 'time_type', 'is_delete')  # list
    search_fields = ('db_name', 't_id', 't_name')


class EnumerationAdmin(admin.ModelAdmin):
    list_display = ('db_name', 't_name', 't_up_col', 'col_name', 'col_value', 'time_type', 'is_delete')  # list
    search_fields = ('db_name', 't_name')


class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_name', 't_type', 'history_error', 'continuous_error', 'is_delete')  # list
    search_fields = ('t_id', 't_name')


class UvPvAdmin(admin.ModelAdmin):
    list_display = ('cubes_source', 'cubes_name', 'ignore_user_email', 'is_delete')  # list
    search_fields = ('cubes_source', 'cubes_name')


class ColumnTableAdmin(admin.ModelAdmin):
    list_display = ('cubes_source', 'cubes_name', 'column_source_params', 'table_source_params', 'column_url', 'table_url', 'cookies_url', 'is_delete')  # list
    search_fields = ('cubes_source', 'cubes_name')


admin.site.register(MonitorBiApi, ApiAdmin)
admin.site.register(MonitorBiCache, CacheAdmin)
admin.site.register(MonitorBiData, DataAdmin)
admin.site.register(MonitorBiSourceGroupby, SourceGrouobyAdmin)
admin.site.register(MonitorBiTables, TablesAdmin)
admin.site.register(MonitorBiEnumeration, EnumerationAdmin)
admin.site.register(MonitorBiInterface, InterfaceAdmin)
admin.site.register(MonitorBiUvPv, UvPvAdmin)
admin.site.register(MonitorBiColumnTable, ColumnTableAdmin)
