# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import IntervalReport

# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    fields = ['start_date', 'end_date']
    list_display = ('start_date', 'end_date', 'analysis_type', 'analysis_key')


admin.site.register(IntervalReport, ReportAdmin)
