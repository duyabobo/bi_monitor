# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class EmailRecord(models.Model):
    """邮件记录表，每条数据记录了一个报警邮件的一些基本属性（不包括邮件的body内容）"""
    email_key = models.CharField(max_length=100)  # 邮件类别，每一种监控类型都有一个邮件类别
    analysis_datetime = models.CharField(max_length=50)  # 统计结果生成的时间，或者发送邮件的时间
    from_datetime = models.CharField(max_length=50)  # 开始统计时间
    end_datetime = models.CharField(max_length=50)  # 结束统计时间
    content_count = models.IntegerField(default=0)  # 本次邮件发送的报警信息条数

    class Meta:
        db_table = 'email_record'  # 自定义表名称

    @classmethod
    def get_one(cls, email_recorder_id):
        """
        获取一个邮件记录的信息
        :param email_recorder_id:
        :return:
        """
        return cls.objects.get(id=email_recorder_id)

    @classmethod
    def get_list(cls, page, email_key):
        """
        分页查询某一类邮件的邮件列表
        :param page:
        :param email_key:  邮件类别
        :return:
        """
        return cls.objects.filter(email_key=email_key).order_by('-id')[10 * page: 10 * (page + 1)]

    @classmethod
    def get_total(cls, email_key):
        """
        获取某一类邮件的邮件总数
        :param email_key:  邮件类别
        :return:
        """
        return cls.objects.filter(email_key=email_key).count()


class BaseModel(models.Model):
    """基础扩展类"""

    class Meta:
        abstract = True

    @classmethod
    def get_items(cls, email_recorder_id):
        """
        查询某个邮件id对应的内容
        :param email_recorder_id:
        :return:
        """
        return cls.objects.filter(email_recorder_id=int(email_recorder_id))


class BiNginxLogWeekReport(BaseModel):
    """
    bi接口日志分析周报，从nginx日志分析统计的结果
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    analysis_type = models.IntegerField(default=0)  # 统计类别： 0 按照 http_code, 1 按照 delay_time
    analysis_key = models.CharField(max_length=20, default='')  # 可能是 200/300/404/502，也可能是 0~1s
    analysis_api = models.CharField(max_length=200, default='/api/dashboard?')  # 分析的接口： 默认是 '/api/dashboard?'
    api_count = models.IntegerField(default=0)  # api 数目统计
    percent = models.FloatField()  # 百分比数，80.3 就代表 80.3%
    average_delay_microseconds = models.FloatField(default=0)  # 接口平均响应时间，单位是毫秒

    class Meta:
        db_table = 'bi_nginx_log_week_report'  # 自定义表名称


class BiAccessAnalysis(BaseModel):
    """
    通过网页/API访问BI的日志统计数据，
    从数据库 guazi_bi 分析 bi_permission_logs(web)/ bi_permission_api_log(api) 数据表获得的统计信息
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    source = models.IntegerField(default=0)  # 访问来源：0 WEB, 1 API
    table_content = models.CharField(max_length=5000, default='')  # 报表的内容，json存储

    class Meta:
        db_table = 'bi_access_analysis'  # 自定义表名称


class NoteWorthyLog(BaseModel):
    """
    从数据库中查询的值得注意的访问日志记录，
    从数据库 guazi_bi 分析 bi_permission_logs(web)/ bi_permission_api_log(api) 数据表获得的日志信息
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    source = models.IntegerField(default=0)  # 访问来源：0 WEB, 1 API
    access_datetime = models.CharField(max_length=50, default='')  # 接口访问的时间
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
        db_table = 'noteworthy_log'  # 自定义表名称


class MonitorBiApiMsg(BaseModel):
    """
    BI指标监控告警邮件
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
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


class MonitorBiCacheMsg(BaseModel):
    """
    BI强制缓存监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    t_id = models.CharField(max_length=255)  # 报表ID
    t_name = models.CharField(max_length=255)  # 报表名称
    http_status = models.CharField(max_length=100)  # HTTP状态
    search_type = models.CharField(max_length=100)  # 查询类型
    error_time = models.CharField(max_length=50)  # 报错时间

    class Meta:
        db_table = 'monitor_bi_cache_msg'  # 自定义表名称
