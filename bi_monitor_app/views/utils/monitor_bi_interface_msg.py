# coding=utf-8
# author='duyabo'
# date='2017/11/27'
from bi_monitor_app.models import MonitorBiInterfaceMsg


def get_detail(email_recorder_id):
    """
    BI接口监控告警邮件邮件
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiInterfaceMsg.get_items(email_recorder_id)
    table_datas = [
        [
            ["BI监控接口异常"],
            ['报表名称', '报表ID', 'HTTP状态', '查询类型', '监控类型', '历史错误次数', '连续错误次数'],
            []
        ]
    ]
    for item in report_items:
        table_datas[0][2].append([
            item.t_name, item.t_id, item.http_status, item.search_type, item.monitor_type, item.history_error, item.continuous_error
        ])
    return {'table_datas': table_datas}
