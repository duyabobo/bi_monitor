# coding=utf-8
# author='duyabo'
# date='2017/11/23'
from bi_monitor_app.models import MonitorBiCacheMsg


def get_list(page):
    """
    分页获取BI强制缓存监控错误信息记录表数据
    :param page:
    :return:
    """
    cache_msgs = MonitorBiCacheMsg.get_list(page)
    body = map(
        lambda x:
        [
            x.id, x.t_name, x.t_id, x.http_status,
            x.search_type, x.error_time
        ],
        cache_msgs
    )
    head = [
        'id', '报表名称', '报表ID', 'HTTP状态', '查询类型', '报错时间'
    ]
    return head, body


def get_total():
    """获取总数"""
    return MonitorBiCacheMsg.objects.count()
