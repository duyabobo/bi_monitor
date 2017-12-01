# coding=utf-8
# author='duyabo'
# date='2017/11/18'
from bi_monitor_app.models import MonitorBiNginxLogWeekReport, EmailRecord


def get_detail(email_recorder_id):
    """
    根据 item_id 获取周报报表监控数据
    :param email_recorder_id:
    :return:
    """
    report_items = MonitorBiNginxLogWeekReport.get_items(email_recorder_id)
    email_record = EmailRecord.get_one(email_recorder_id)
    interval_date = "日期: {0} ——> {1}".format(email_record.from_datetime, email_record.end_datetime)
    table_datas = [
        [
            [
                "BI访问日志按照 http code 统计",
                interval_date,
                "分析接口：'/api/dashboard?'"
            ],
            ['http code', '数量统计', '占比'],
            []
        ], [
            [
                "BI访问日志按照 delay time 统计",
                interval_date,
                "分析接口：'/api/dashboard?'"
            ],
            ['delay_time', '数量统计', '占比', '平均响应时间(ms)'],
            []
        ]
    ]
    for item in report_items:
        if item.analysis_type == 0:
            table_datas[0][2].append([item.analysis_key, item.api_count, item.percent])
        if item.analysis_type == 1:
            table_datas[1][2].append([item.analysis_key, item.api_count, item.percent, item.average_delay_microseconds])
    return {'table_datas': table_datas}


def get_warning_dict(email_record_ids):
    """
    根据 email_record_ids 查询每一个 email_record_id 对应的邮件内容中有多少条告警信息
    :param email_record_ids:
    :return:
    """
    return MonitorBiNginxLogWeekReport.get_warning_dict_empty(email_record_ids)
