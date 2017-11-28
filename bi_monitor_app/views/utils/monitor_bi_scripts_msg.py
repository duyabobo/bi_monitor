# coding=utf-8
# author='duyabo'
# date='2017/11/28'
from bi_monitor_app.models import MonitorBiScriptsMsg


def get_detail(email_recorder_id):
    """
    BI数据清洗脚本监控错误信息邮件
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiScriptsMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["数据清洗脚本运行状态 "],
            ['警报信息', '脚本名称', '脚本状态', '脚本开始时间', '监控查询时间'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.alert_msg, item.script_name, item.script_status, item.start_time, item.monitor_time
        ])
    return {'table_datas': table_datas}
