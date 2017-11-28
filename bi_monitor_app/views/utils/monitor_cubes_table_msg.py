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
