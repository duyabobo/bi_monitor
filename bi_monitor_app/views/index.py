# coding=utf-8
# author='duyabo'
# date='2017/11/15'
from django.shortcuts import render

from bi_monitor_app.views.utils import bi_indicator_monitor_error_message
from bi_monitor_app.views.utils import week_report
from bi_monitor_app.views.utils import hour_report
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
    if api_id == 'bi_access_hour_report':  # bi访问汇总时报
        context = hour_report.get_detail(item_id)
    elif api_id == 'bi_api_week_report':  # bi访问日志周报报表
        context = week_report.get_detail(item_id)
    else:
        context = {'table_datas': []}
    return render(request, 'report_detail_2_dime.html', context=context)


def content_list(request):
    """
    查询各种类型的监控数据列表，
    列表在前端显示的时候是使用 table 展现的，
    需要从数据库中获取 table 的 head 和 body 内容,
    注意：body 的 item 第一个字段都是 id
    :param request:
    :return:
    """
    api_id = request.GET['api_id']  # 指定哪一类监控数据
    page = request.GET.get('page', 1)
    page = 0 if page == 'undefined' else int(page) - 1  # 分页控件页码从1开始
    detail_url_is_needed = True  # 监控数据列表是否需要链接到数据详情页，False 的话是指，统计数据直接在列表页就展示了
    if api_id == 'bi_access_hour_report':  # bi 访问汇总时报
        head, body = hour_report.get_list(page)
    elif api_id == 'bi_api_week_report':  # bi访问日志周报报表
        head, body = week_report.get_list(page)
    elif api_id == 'bi_indicator_monitor_error_message':  # BI指标监控告警邮件
        detail_url_is_needed = False  # 统计数据直接在列表页就展示了
        head, body = bi_indicator_monitor_error_message.get_list(page)
    else:
        head, body = [], [[], []]
    return render(request, 'report_list.html', context={
        'api_id': api_id,
        'detail_url_is_needed': detail_url_is_needed,
        'title': title_dict[api_id],
        'head': head,
        'body': body
        }
    )


def get_pager(request):
    """
    获取分页数据
    :param request:
    :return:
    """
    api_id = request.GET['api_id']  # 指定哪一类监控数据
    if api_id == 'bi_access_hour_report':  # bi访问汇总时报
        total = hour_report.get_total()
    elif api_id == 'bi_api_week_report':  # bi访问日志周报报表
        total = week_report.get_total()
    elif api_id == 'bi_indicator_monitor_error_message':  # BI指标监控告警邮件
        total = bi_indicator_monitor_error_message.get_total()
    else:
        total = 0
    return render(request, 'pager_info.html', context={
        'api_id': api_id,
        'total': total,
        'total_page': int(total/10)
    })
