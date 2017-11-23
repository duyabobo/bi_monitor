# coding=utf-8
# author='duyabo'
# date='2017/11/23'
from bi_monitor_app.models import MonitorBiApiMsg


def get_list(page):
    """
    分页获取BI指标监控告警数据记录
    :param page:
    :return:
    """
    monitor_msgs = MonitorBiApiMsg.get_list(page)
    body = map(
        lambda x:
        [
            x.id, x.t_id, x.t_name, x.search_time,
            x.search_type, x.indicator_name,
            x.indicator_id, x.bi_value,
            x.compute_value, x.compute_source
        ],
        monitor_msgs
    )
    head = [
        'id', '报表ID', '报表名称', '查询时间', '查询类型',
        '指标名称', '指标Indicator', 'BI显示指标值',
        '计算所得指标值', '计算数据来源'
    ]
    return head, body


def get_total():
    """获取总数"""
    return MonitorBiApiMsg.get_total()
