# coding=utf-8
# author='duyabo'
# date='2017/11/27'
from bi_monitor_app.models import MonitorBiDataMsg


def get_detail(email_recorder_id):
    """
    获取BI强制缓存监控错误信息数据
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiDataMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["BI监控数据异常"],
            ['报表名称', '报表ID', '指标名称', '查询时间', '分组类型', '上次查询值', '此次查询值', '偏差值'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.t_name, item.t_id, item.indicator_name, item.search_time, item.search_type, item.old_value, item.new_value, item.deviation
        ])
    return {'table_datas': table_datas}


def get_warning_dict(email_record_ids):
    """
    根据 email_record_ids 查询每一个 email_record_id 对应的邮件内容中有多少条告警信息
    :param email_record_ids:
    :return:
    """
    return MonitorBiDataMsg.get_warning_dict(email_record_ids)
