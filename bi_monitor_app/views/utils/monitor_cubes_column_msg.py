# coding=utf-8
# author='duyabo'
# date='2017/11/28'
from bi_monitor_app.models import MonitorCubesColumnMsg


def get_detail(email_recorder_id):
    """
    CUBES接口column监控错误信息记录表邮件
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorCubesColumnMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["CUBES监控-column异常"],
            ['报表名称', 'source名称', 'HTTP状态'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.t_name, item.source_name, item.http_status
        ])
    return {'table_datas': table_datas}
