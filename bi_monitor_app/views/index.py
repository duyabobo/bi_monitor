# coding=utf-8
# author='duyabo'
# date='2017/11/15'
import logging
from django.shortcuts import render

from bi_monitor.settings import LOGGING
from bi_monitor_app.models import EmailRecord
from bi_monitor_app.views import flat_email_name_dict, collect_item, email_name_dict
from bi_monitor_app.views import email_table_head, sorted_email_name, collect_head
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
from bi_monitor_app.views.utils import monitor_bi_api_compare_msg

logger = logging.getLogger("django")  # 为loggers中定义的名称


def api_logger(func):
    """
    接口打日志的装饰器
    :param func:
    :return:
    """
    def inner_func(request):
        try:
            result = func(request)
        except Exception as e:
            logger.exception(str(e))
            result = render(request, '500.html', context={'log_path': LOGGING['handlers']['file_handler']['filename']})
        return result
    return inner_func


@api_logger
def index(request):
    email_name_items = map(lambda x: [x, email_name_dict[x]], sorted_email_name)
    return render(
        request,
        'index.html',
        context={'email_name_items': email_name_items}
    )


@api_logger
def email_detail(request):
    """
    根据request中的api_id实现各种业务逻辑，查询各种类型的监控数据图表详情
    :param request:
    :return:
    """
    api_id = request.GET['api_id']  # 指定哪一类监控数据
    analysiss_time = request.GET['analysiss_time']  # 汇总生成的时间
    email_recorder_id = request.GET['item_id']  # 指定某一条监控数据
    if api_id in flat_email_name_dict:
        context = eval(api_id).get_detail(email_recorder_id)
    else:
        context = {'table_datas': []}
    context['analysiss_time'] = analysiss_time
    return render(request, 'email_detail.html', context=context)


@api_logger
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
    if api_id in flat_email_name_dict:
        name = flat_email_name_dict[api_id]
    else:
        name = ''
    if api_id == collect_item:  # 实时汇总的最新报警信息
        email_records = EmailRecord.get_latest_20()
        head = collect_head
        body = map(  # 前十条
            lambda (i, x):
            [[x.id, x.created_at.strftime('%Y-%m-%d %H:%M'), flat_email_name_dict.get(x.msg_table_name, ''), x.msg_table_name],
             [0, 0, 0, 0]],
            enumerate(email_records[:10])
        )
        for i, x in enumerate(email_records[10:]):  # 后十条
            body[i][1] = [x.id, x.created_at.strftime('%Y-%m-%d %H:%M'), flat_email_name_dict.get(x.msg_table_name, ''),
                          x.msg_table_name]
    else:  # 历史的某一种类型的报警信息
        page = request.GET.get('page', 1)
        page = 0 if page == 'undefined' else int(page) - 1  # 分页控件页码从1开始
        email_records = EmailRecord.get_list(page, api_id)
        warning_num_dict = eval(api_id).get_warning_dict(map(lambda x: x.id, email_records))
        head = email_table_head
        body = map(  # 前十条
            lambda (i, x):
            [[x.id, x.created_at.strftime('%Y-%m-%d %H:%M'), warning_num_dict.get(x.id, 0), x.msg_table_name], [0, 0, 0, 0]],
            enumerate(email_records[:10])
        )
        for i, x in enumerate(email_records[10:]):  # 后十条
            body[i][1] = [x.id, x.created_at.strftime('%Y-%m-%d %H:%M'), warning_num_dict.get(x.id, 0), x.msg_table_name]
    return render(request, 'email_list.html', context={
        'name': name,
        'head': head,
        'body': body,
        })


@api_logger
def get_pager(request):
    """
    获取分页数据
    :param request:
    :return:
    """
    api_id = request.GET['api_id']  # 指定哪一类监控数据
    total = 0
    if api_id != collect_item:  # 实时汇总最新报警
        total = EmailRecord.get_total(api_id)
    return render(request, 'pager_info.html', context={
        'api_id': api_id,
        'total': total,
        'total_page': int(total/20) + 1 if total % 20 else int(total/20)
    })
