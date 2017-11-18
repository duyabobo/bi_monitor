# coding=utf-8
# author='duyabo'
# date='2017/11/18'
from datetime import timedelta

from bi_monitor_app.models import WeekReport
from bi_monitor_app.models import WeekReportItem


def get_detail(report_id):
    """
    根据 item_id 获取周报报表监控数据
    :param report_id:
    :return:
    """
    report = WeekReport.objects.get(id=report_id)
    analysis_date = report.analysis_date
    report_items = WeekReportItem.objects.filter(week_report_id=report_id)
    interval_date = "日期: {0} ——> {1}".format(analysis_date, analysis_date - timedelta(days=7))
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
            table_datas[1][2].append([item.analysis_key, item.api_count, item.percent, item.average_delay_time])
    return {'table_datas': table_datas}


def get_list():
    """
    获取周报监控报表的列表，分页显示
    :return:
    """
    week_reports = WeekReport.objects.all()  # todo 待优化
    return map(lambda x: [x.id, str(x.analysis_date)], week_reports)
