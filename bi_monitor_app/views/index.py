# coding=utf-8
# author='duyabo'
# date='2017/11/15'
from datetime import datetime
from django.shortcuts import render

from bi_monitor_app.models import EmailRecord
from bi_monitor_app.views import email_name_dict, children_email_name_dict
from bi_monitor_app.views import email_table_head, sorted_email_name
from bi_monitor_app.views.utils import monitor_bi_cache_msg
from bi_monitor_app.views.utils import monitor_bi_api_msg
from bi_monitor_app.views.utils import monitor_bi_data_msg
from bi_monitor_app.views.utils import monitor_bi_enumeration_msg
from bi_monitor_app.views.utils import monitor_bi_interface_msg
from bi_monitor_app.views.utils import monitor_bi_scripts_msg
from bi_monitor_app.views.utils import monitor_bi_access_hour_report
from bi_monitor_app.views.utils import monitor_bi_nginx_log_week_report
from bi_monitor_app.views.utils import monitor_bi_source_data_msg
from bi_monitor_app.views.utils import monitor_bi_source_groupby_msg
from bi_monitor_app.views.utils import monitor_cubes_column_msg
from bi_monitor_app.views.utils import monitor_cubes_table_msg
from bi_monitor_app.views.utils import monitor_bi_log_week_report


def index(request):
    email_name_items = map(lambda x: [x, email_name_dict[x]], sorted_email_name)
    return render(
        request,
        'index.html',
        context={'email_name_items': email_name_items}
    )


def email_detail(request):
    """
    根据request中的api_id实现各种业务逻辑，查询各种类型的监控数据图表详情
    :param request:
    :return:
    """
    api_id = request.GET['api_id']  # 指定哪一类监控数据
    analysiss_time = request.GET['analysiss_time']  # 汇总生成的时间
    email_recorder_id = request.GET['item_id']  # 指定某一条监控数据
    if api_id in email_name_dict or api_id in children_email_name_dict:
        context = eval(api_id).get_detail(email_recorder_id)
    else:
        context = {'table_datas': []}
    context['analysiss_time'] = analysiss_time
    return render(request, 'email_detail.html', context=context)


def email_list(request):
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
    if api_id in email_name_dict:
        name = email_name_dict[api_id]['title']
    elif api_id in children_email_name_dict:
        name = children_email_name_dict[api_id]['title']
    else:
        name = ''
    email_records = EmailRecord.get_list(page, api_id)
    warning_num_dict = eval(api_id).get_warning_dict(map(lambda x: x.id, email_records))
    body = map(
        lambda (i, x):
        [[x.id, x.created_at.strftime('%Y-%m-%d %H:%M'), warning_num_dict.get(x.id, 0)], [0, 0, 0]], enumerate(email_records[:10])
    )
    for i, x in enumerate(email_records[10:]):
        body[i][1] = [x.id, x.created_at.strftime('%Y-%m-%d %H:%M'), warning_num_dict.get(x.id, 0)]
    return render(request, 'email_list.html', context={
        'api_id': api_id,
        'name': name,
        'head': email_table_head,
        'body': body,
        })


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
        'total_page': int(total/20) + 1 if total % 20 else int(total/20)
    })
