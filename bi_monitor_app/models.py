# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.http import Http404


class IntervalReport(models.Model):
    """
    某个时间段内，bi接口日志分析结果
    """
    id = models.IntegerField(primary_key=True)
    from_timestamp = models.DateField()  # 开始统计的时间戳，单位毫秒
    end_timestamp = models.DateField()
    analysis_type = models.IntegerField(default=0)  # 统计类别： 0 按照 http_code, 1 按照 delay_time
    analysis_key = models.CharField(max_length=20, default='')  # 可能是 200/300/404/502，也可能是 0~1s
    analysis_api = models.CharField(max_length=200, default='/api/dashboard?')  # 分析的接口： 默认是 '/api/dashboard?'
    api_count = models.IntegerField(default=0)  # api 数目统计
    percent = models.FloatField()  # 百分比数，80.3 就代表 80.3%
    average_delay_time = models.FloatField(default=0)  # 接口平均响应时间，单位是毫秒

    class Meta:
        db_table = 't_interval_report'  # 自定义表名称

    def __str__(self):
        return self.id

    @staticmethod
    def select_interval_report(from_timestamp, end_timestamp):
        """
        查询某个时间段内的所有日志分析结果
        :param from_timestamp: 起始日期
        :param end_timestamp: 结束日期
        :return:
        """
        return IntervalReport.objects.filter(from_timestamp=from_timestamp, end_timestamp=end_timestamp)


class BiAccessAnalysis(models.Model):
    """
    通过网页/api访问BI的日志统计数据
    """
    id = models.IntegerField(primary_key=True)
    from_timestamp = models.IntegerField(default=0)  # 开始统计的时间戳，单位毫秒
    end_timestamp = models.IntegerField(default=0)  # 结束统计的时间戳，单位毫秒
    source = models.IntegerField(default=0)  # 访问来源：0 WEB, 1 API
    # 统计类别：0 全部，1 0~1s，2 1~2s，3 2~3s，4 3~5s， 5 5~10s，6 10~20s，7 20s+
    kind = models.IntegerField(default=0)
    num = models.IntegerField(default=0)  # 访问次数统计
    percent = models.FloatField(default=0)  # 次数占百分比，80代表80%
    average = models.FloatField(default=0)  # api响应的平均时间

    class Meta:
        db_table = 't_bi_access_analysis'  # 自定义表名称

    @staticmethod
    def get_access_analysis(from_timestamp, end_timestamp):
        """
        通过开始统计时间、结束统计时间查询统计数据
        :param from_timestamp:
        :param end_timestamp:
        :return:
        """
        return BiAccessAnalysis.objects.filter(from_timestamp=from_timestamp, end_timestamp=end_timestamp)
