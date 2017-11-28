# coding=utf-8
# author='duyabo'
# date='2017/11/15'
from django.shortcuts import render

from bi_monitor_app.models import EmailRecord
from bi_monitor_app.views import email_name_dict
from bi_monitor_app.views import head_dict
from bi_monitor_app.views.utils import monitor_bi_cache_msg
from bi_monitor_app.views.utils import monitor_bi_api_msg
from bi_monitor_app.views.utils import monitor_bi_data_msg
from bi_monitor_app.views.utils import monitor_bi_enumeration_msg
from bi_monitor_app.views.utils import monitor_bi_interface_msg
from bi_monitor_app.views.utils import monitor_bi_scripts_msg
from bi_monitor_app.views.utils import monitor_bi_access_hour_report
from bi_monitor_app.views.utils import monitor_bi_nginx_log_week_report
from bi_monitor_app.views.utils import monitor_bi_source_data_msg


def index(request):
    return render(request, 'index.html', context={'email_name_dict': email_name_dict})


def content_detail(request):
    """
    根据request中的api_id实现各种业务逻辑，查询各种类型的监控数据图表详情
    :param request:
    :return:
    """
    api_id = request.GET['api_id']  # 指定哪一类监控数据
    email_recorder_id = request.GET['item_id']  # 指定某一条监控数据
    if api_id in email_name_dict:
        context = eval(api_id).get_detail(email_recorder_id)
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
    email_records = EmailRecord.get_list(page, api_id)
    body = map(
        lambda (i, x):
        [x.id, i+page*10, x.from_datetime, x.end_datetime, x.content_count], enumerate(email_records)
    )
    return render(request, 'report_list.html', context={
        'api_id': api_id,
        'name': email_name_dict[api_id],
        'head': head_dict[api_id],
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
    total = EmailRecord.get_total(api_id)
    return render(request, 'pager_info.html', context={
        'api_id': api_id,
        'total': total,
        'total_page': int(total/10)
    })
