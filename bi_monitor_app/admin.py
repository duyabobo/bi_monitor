# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import IntervalReport

# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    fields = ['from_timestamp', 'end_timestamp']
    list_display = ('from_timestamp', 'end_timestamp', 'analysis_type', 'analysis_key')
    search_fields = ['analysis_api']


admin.site.register(IntervalReport, ReportAdmin)
