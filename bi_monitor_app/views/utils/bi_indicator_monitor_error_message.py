# coding=utf-8
# author='duyabo'
# date='2017/11/23'
from bi_monitor_app.models import MonitorBiApiMsg


def get_detail(email_recorder_id):
    """
    根据 item_id 获取BI指标监控告警邮件数据
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiApiMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["BI监控指标异常"],
            [
                '报表ID', '报表名称', '查询时间', '查询类型',
                '指标名称', '指标Indicator', 'BI显示指标值',
                '计算所得指标值', '计算数据来源'
            ],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.t_id, item.t_name, item.search_time,
            item.search_type, item.indicator_name, item.indicator_id,
            item.bi_value, item.compute_value, item.compute_source
        ])
    return {'table_datas': table_datas}
