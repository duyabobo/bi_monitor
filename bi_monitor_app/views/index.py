# coding=utf-8
# author='duyabo'
# date='2017/11/15'
from django.shortcuts import render

from utils import get_detail_example
from utils import get_list_example
from bi_monitor_app.views.utils import week_report
from bi_monitor_app.views import title_dict


def index(request):
    return render(request, 'index.html')


def content_detail(request):
    """
    根据request中的api_id实现各种业务逻辑，查询各种类型的监控数据图表详情
    :param request:
    :return:
    """
    api_id = request.GET['api_id']  # 指定哪一类监控数据
    item_id = request.GET['item_id']  # 指定某一条监控数据
    if api_id == 'example':
        context = get_detail_example(item_id)
    elif api_id == 'bi_api_week_report':  # bi访问日志周报报表
        context = week_report.get_detail(item_id)
    else:
        context = {'table_datas': []}
    return render(request, 'report_detail_2_dime.html', context=context)


def content_list(request):
    """
    查询各种类型的监控数据列表
    :param request:
    :return:
    """
    api_id = request.GET['api_id']  # 指定哪一类监控数据
    page = request.GET.get('page', 0)
    if api_id == 'example':
        datas = get_list_example()
    elif api_id == 'bi_api_week_report':  # bi访问日志周报报表
        datas = week_report.get_list(page)
    else:
        datas = []
    return render(request, 'report_list.html', context={
        'api_id': api_id,
        'title': title_dict[api_id],
        'datas': datas
        }
    )
