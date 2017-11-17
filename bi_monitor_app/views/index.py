# coding=utf-8
# author='duyabo'
# date='2017/11/15'
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def content_detail(request):
    """
    根据request中的api_id实现各种业务逻辑，查询各种类型的监控数据图表详情
    :param request:
    :return:
    """
    return render(request, 'report_detail.html')


def content_list(request):
    """
    查询各种类型的监控数据列表
    :param request:
    :return:
    """
    return render(request, 'report_list.html')
