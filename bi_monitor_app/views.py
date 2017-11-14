# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from models import IntervalReport


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, report_id):
    """
    查询某个id对应的汇总详情，测试用的接口
    :param request:
    :param report_id:
    :return:
    """
    interval_report = IntervalReport.get_one_interval_report_by_id(report_id)
    content = {
        'start_date': interval_report.start_date,
        'end_date': interval_report.end_date,
        'analysis_type': interval_report.analysis_type,
        'analysis_key': interval_report.analysis_key,
        'analysis_api': interval_report.analysis_api
    }
    return render(request, 'bi_monitor_app/detail.html', content)
