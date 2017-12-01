# coding=utf-8
# author='duyabo'
# date='2017/11/28'
from bi_monitor_app.models import MonitorBiSourceGroupByMsg


def get_detail(email_recorder_id):
    """
    BI与业务源字段监控错误信息记录邮件
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiSourceGroupByMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["BI数据与业务源字段值数量监控"],
            ['指标名称', '业务源表', '目标表', '查询时间段', '字段值', '业务库数量', 'BI库数量', '偏差值'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.indicator_name, item.source_name, item.target_name,
            item.search_time, item.col_value, item.source_number, item.target_number, item.deviation
        ])
    return {'table_datas': table_datas}


def get_warning_dict(email_record_ids):
    """
    根据 email_record_ids 查询每一个 email_record_id 对应的邮件内容中有多少条告警信息
    :param email_record_ids:
    :return:
    """
    return MonitorBiSourceGroupByMsg.get_warning_dict(email_record_ids)
