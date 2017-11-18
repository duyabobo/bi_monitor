# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import WeekReport
from models import WeekReportItem

# Register your models here.
admin.site.register(WeekReport)
admin.site.register(WeekReportItem)
