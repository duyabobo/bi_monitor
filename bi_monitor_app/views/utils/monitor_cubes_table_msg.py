# coding=utf-8
# author='duyabo'
# date='2017/11/28'
from bi_monitor_app.models import MonitorCubesTablesMsg


def get_detail(email_recorder_id):
    """
    CUBES接口监控告警邮件-table监控
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorCubesTablesMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["CUBES监控-table异常"],
            ['报表名称', 'source名称', 'HTTP状态'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.t_name, item.source_name, item.http_status
        ])
    return {'table_datas': table_datas}


def get_warning_dict(email_record_ids):
    """
    根据 email_record_ids 查询每一个 email_record_id 对应的邮件内容中有多少条告警信息
    :param email_record_ids:
    :return:
    """
    return MonitorCubesTablesMsg.get_warning_dict(email_record_ids)
