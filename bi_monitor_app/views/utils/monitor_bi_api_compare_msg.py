# coding=utf-8
# author='duyabo'
# date='2017/11/23'
from bi_monitor_app.models import MonitorBiApiCompareMsg


def get_detail(email_recorder_id):
    """
    根据 item_id 获取BI监控指标异常-同比及环比监控错误信息
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiApiCompareMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["BI监控指标异常-同比及环比"],  # 查询某一类邮件中的某一个邮件详情时，展示的表格名称
            [  # 邮件详情表格的表头信息
                '报表名称', '报表ID', '指标名称', '指标Indicator',
                '查询类型', '今日指标值', '对比指标值',
                '比较结果'
            ],
            []  # 用来装载具体的监控数据
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.t_name, item.t_id, item.indicator_name,
            item.indicator_id, item.search_type, item.today_value,
            item.compare_value, item.compare_result
        ])
    return {'table_datas': table_datas}


def get_warning_dict(email_record_ids):
    """
    根据 email_record_ids 查询每一个 email_record_id 对应的邮件内容中有多少条告警信息
    :param email_record_ids:
    :return:
    """
    return MonitorBiApiCompareMsg.get_warning_dict(email_record_ids)
