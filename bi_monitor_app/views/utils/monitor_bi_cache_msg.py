# coding=utf-8
# author='duyabo'
# date='2017/11/23'
from bi_monitor_app.models import MonitorBiCacheMsg


def get_detail(email_recorder_id):
    """
    获取BI强制缓存监控错误信息数据
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiCacheMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["BI强制缓存-并行"],
            ['报表名称', '报表ID', 'HTTP状态', '查询类型', '报错时间'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.t_name, item.t_id, item.http_status, item.search_type, item.error_time
        ])
    return {'table_datas': table_datas}


def get_warning_dict(email_record_ids):
    """
    根据 email_record_ids 查询每一个 email_record_id 对应的邮件内容中有多少条告警信息
    :param email_record_ids:
    :return:
    """
    return MonitorBiCacheMsg.get_warning_dict(email_record_ids)
