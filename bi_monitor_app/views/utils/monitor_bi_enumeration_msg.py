# coding=utf-8
# author='duyabo'
# date='2017/11/27'
from bi_monitor_app.models import MonitorBiEnumerationMsg


def get_detail(email_recorder_id):
    """
    BI业务源库枚举值监控错误信息邮件
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiEnumerationMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["库表监控枚举值异常"],
            ['数据库', '表', '字段', '枚举值', '异常值'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.db_mname, item.t_name, item.t_col, item.t_value, item.error_value
        ])
    return {'table_datas': table_datas}


def get_warning_dict(email_record_ids):
    """
    根据 email_record_ids 查询每一个 email_record_id 对应的邮件内容中有多少条告警信息
    :param email_record_ids:
    :return:
    """
    return MonitorBiEnumerationMsg.get_warning_dict(email_record_ids)
