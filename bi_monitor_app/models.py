# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.http import Http404


class IntervalReport(models.Model):
    """
    某个时间段内，bi接口日志分析结果
    """
    id = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    analysis_type = models.IntegerField(default=0)  # 统计类别： 0 按照 http_code, 1 按照 delay_time
    analysis_key = models.CharField(max_length=20, default='')  # 可能是 200/300/404/502，也可能是 0~1s
    analysis_api = models.CharField(max_length=200, default='/api/dashboard?')  # 分析的接口： 默认是 '/api/dashboard?'
    api_count = models.IntegerField(default=0)  # api 数目统计
    percent = models.FloatField()  # 百分比数，80.3 就代表 80.3%
    average_delay_time = models.FloatField(default=0)  # 接口平均响应时间，单位是毫秒

    class Meta:
        db_table = 't_interval_report'  # 自定义表名称为 my_table

    def __str__(self):
        return self.id

    @staticmethod
    def select_interval_report(start_date, end_date):
        """
        查询某个时间段内的所有日志分析结果
        :param start_date: 起始日期
        :param end_date: 结束日期
        :return:
        """
        return IntervalReport.objects.filter(start_date=start_date, end_date=end_date)

    @staticmethod
    def get_one_interval_report_by_id(report_id):
        """
        通过id查询一个interval_report
        :param report_id:
        :return:
        """
        try:
            return IntervalReport.objects.get(id=report_id)
        except IntervalReport.DoesNotExist:
            raise Http404('interval report not found!')
