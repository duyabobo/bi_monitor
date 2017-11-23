# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class WeekReport(models.Model):
    """
    某周的bi访问日志汇总信息
    """
    analysis_date = models.DateField()  # 统计的日期


class WeekReportItem(models.Model):
    """
    某个时间段内，bi接口日志分析结果，从nginx日志分析统计的结果
    """
    week_report_id = models.IntegerField()  # 周报id
    analysis_type = models.IntegerField(default=0)  # 统计类别： 0 按照 http_code, 1 按照 delay_time
    analysis_key = models.CharField(max_length=20, default='')  # 可能是 200/300/404/502，也可能是 0~1s
    analysis_api = models.CharField(max_length=200, default='/api/dashboard?')  # 分析的接口： 默认是 '/api/dashboard?'
    api_count = models.IntegerField(default=0)  # api 数目统计
    percent = models.FloatField()  # 百分比数，80.3 就代表 80.3%
    average_delay_time = models.FloatField(default=0)  # 接口平均响应时间，单位是毫秒

    class Meta:
        db_table = 't_week_report_item'  # 自定义表名称

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_items(week_report_id):
        """
        查询某一个周的所有统计数据
        :param week_report_id:
        :return:
        """
        return WeekReportItem.objects.filter(week_report_id=week_report_id)


class HourAnalysis(models.Model):
    """
    按小时统计的日志基本信息，具体统计结果存储在 BiAccessAnalysis 和 NoteWorthyLog
    """
    from_timestamp = models.IntegerField(default=0)  # 开始统计的时间戳，单位毫秒
    end_timestamp = models.IntegerField(default=0)  # 结束统计的时间戳，单位毫秒
    web_delay_bg_10 = models.IntegerField(default=0)  # 从web访问的接口响应时间大于10s的次数
    api_delay_bg_10 = models.IntegerField(default=0)  # 从api访问的接口响应时间大于10s的次数

    class Meta:
        db_table = 't_hour_analysis'  # 自定义表名称

    @staticmethod
    def get_list(page):
        """
        查询某一个周的所有统计数据
        :param week_report_id:
        :return:
        """
        return HourAnalysis.objects.all()[10*page: 10*(page+1)]


class BiAccessAnalysis(models.Model):
    """
    通过网页/api访问BI的日志统计数据，从数据库访问记录log中搜集的统计信息
    """
    hour_analysis_id = models.IntegerField(default=0)
    source = models.IntegerField(default=0)  # 访问来源：0 WEB, 1 API
    table_content = models.CharField(max_length=5000, default='')  # 报表的内容，json存储

    class Meta:
        db_table = 't_bi_access_analysis'  # 自定义表名称

    @staticmethod
    def get_items(hour_analysis_id):
        """
        通过开始统计时间、结束统计时间查询统计数据
        :param hour_analysis_id:
        :return:
        """
        return BiAccessAnalysis.objects.filter(hour_analysis_id=hour_analysis_id)


class NoteWorthyLog(models.Model):
    """
    从数据库中查询的值得注意的访问日志记录
    """
    hour_analysis_id = models.IntegerField(default=0)
    source = models.IntegerField(default=0)  # 访问来源：0 WEB, 1 API
    access_timestamp = models.IntegerField(default=0)  # 接口访问的时间戳
    method = models.IntegerField(default=0)  # 接口访问的http方法：0 get，1 post，2 put，3 delete
    report_name = models.CharField(max_length=60)  # 报表名称
    report_id = models.CharField(max_length=200)  # 报表id
    user_name = models.CharField(max_length=50)  # 发出访问的用户名
    delay_microseconds = models.FloatField(default=0)  # 访问接口的响应的时长，单位是毫秒
    parameters = models.CharField(max_length=500)  # 参数JSON
    # 下面这俩是api访问时特有的
    department_name = models.CharField(max_length=20)  # 部门名
    api_key = models.CharField(max_length=50)  # 用户(原来表是这么注释的）

    class Meta:
        db_table = 't_noteworthy_log'  # 自定义表名称

    @staticmethod
    def get_items(hour_analysis_id):
        """
        查询某个时间区间内值得关注的访问日志记录
        :param hour_analysis_id:
        :return:
        """
        return NoteWorthyLog.objects.filter(hour_analysis_id=hour_analysis_id)


class MonitorBiApiMsg(models.Model):
    """
    BI指标监控告警邮件
    """
    t_id = models.CharField(max_length=255)  # 报表ID
    t_name = models.CharField(max_length=255)  # 报表名称
    search_time = models.CharField(max_length=100)  # 查询时间
    search_type = models.CharField(max_length=100)  # 查询类型
    indicator_name = models.CharField(max_length=255)  # 指标名称
    indicator_id = models.CharField(max_length=255)  # 指标Indicator
    bi_value = models.CharField(max_length=100)  # BI显示指标值
    compute_value = models.CharField(max_length=100)  # 计算所得指标值
    compute_source = models.CharField(max_length=1000)  # 计算数据来源

    class Meta:
        db_table = 'monitor_bi_api_msg'  # 自定义表名称

    @staticmethod
    def get_list(page):
        """
        查询某一个周的所有统计数据
        :param page:
        :return:
        """
        return MonitorBiApiMsg.objects.all().order_by('-search_time')[10 * page: 10 * (page + 1)]
