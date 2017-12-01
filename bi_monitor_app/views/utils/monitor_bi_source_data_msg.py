# coding=utf-8
# author='duyabo'
# date='2017/11/28'
from bi_monitor_app.models import MonitorBiSourceDataMsg


def get_detail(email_recorder_id):
    """
    BI数据清洗脚本监控错误信息邮件
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiSourceDataMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["BI数据与业务源数据监控"],
            ['指标名', '查询时间', '业务库值', 'BI库值', '偏差值', '最新数据时间', '脚本捕获时间', '偏差原因'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.indicator_name, item.search_time, item.source_value,
            item.bi_value, item.deviation, item.new_data_time, item.script_time, item.devi_reason
        ])
    return {'table_datas': table_datas}


def get_warning_dict(email_record_ids):
    """
    根据 email_record_ids 查询每一个 email_record_id 对应的邮件内容中有多少条告警信息
    :param email_record_ids:
    :return:
    """
    return MonitorBiSourceDataMsg.get_warning_dict(email_record_ids)
