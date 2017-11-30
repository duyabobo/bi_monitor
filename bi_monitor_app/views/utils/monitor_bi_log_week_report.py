# coding=utf-8
# author='duyabo'
# date='2017/11/29'
from bi_monitor_app.models import MonitorBiLogWeekReport, EmailRecord


def get_detail(email_recorder_id):
    """
    BI接口监控告警邮件邮件
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiLogWeekReport.get_items(email_recorder_id)
    email_record = EmailRecord.get_one(email_recorder_id)
    interval_date = "日期: {0} ——> {1}".format(email_record.from_datetime, email_record.end_datetime)
    table_datas = [
        [
            ["WEB访问BI日志按照 delay time 统计", interval_date],
            ['delay_time', '数量统计', '占比', '平均响应时间(ms)'],
            []
        ], [
            ["API访问BI日志按照 delay time 统计", interval_date],
            ['delay_time', '数量统计', '占比', '平均响应时间(ms)'],
            []
        ]
    ]
    for item in report_items:
        table_datas[item.source][2].append([
            item.delay_time_key, item.api_count, item.percent, item.average_delay_microseconds
        ])
    return {'table_datas': table_datas}
