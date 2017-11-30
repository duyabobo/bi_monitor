# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class EmailRecord(models.Model):
    """邮件记录表，每条数据记录了一个报警邮件的一些基本属性（不包括邮件的body内容）"""
    msg_table_name = models.CharField(max_length=100)  # 每一种监控类型都有一个邮件类别
    from_datetime = models.CharField(max_length=50)  # 开始统计时间
    end_datetime = models.CharField(max_length=50)  # 结束统计时间
    content_count = models.IntegerField(default=0)  # 本次邮件发送的报警信息条数
    created_at = models.DateTimeField(default=datetime.now())  # 记录创建时间

    class Meta:
        db_table = 'monitor_bi_record'  # 自定义表名称

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
        return cls.objects.filter(msg_table_name=email_key).order_by('-id')[10 * page: 10 * (page + 1)]

    @classmethod
    def get_total(cls, email_key):
        """
        获取某一类邮件的邮件总数
        :param email_key:  邮件类别
        :return:
        """
        return cls.objects.filter(msg_table_name=email_key).count()


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


class MonitorBiNginxLogWeekReport(BaseModel):
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
        db_table = 'monitor_bi_nginx_log_week_report'  # 自定义表名称


class MonitorBiLogWeekReport(BaseModel):
    """
    访问BI日志统计报表，从monitor_bi数据库分析统计的结果
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    access_source = models.IntegerField(default=0)  # 所属类型：api还是web访问，0 web，1 api
    delay_time_key = models.CharField(max_length=20, default='')  # 可能是 200/300/404/502，也可能是 0~1s
    api_count = models.IntegerField(default=0)  # api 数目统计
    percent = models.CharField(max_length=20, default='')  # 百分比数，80.3 就代表 80.3%
    average_delay_microseconds = models.CharField(max_length=20, default='')  # 接口平均响应时间，单位是毫秒

    class Meta:
        db_table = 'monitor_bi_log_week_report'  # 自定义表名称


class MonitorBiAccessAnalysis(BaseModel):
    """
    通过网页/API访问BI的日志统计数据，
    从数据库 guazi_bi 分析 bi_permission_logs(web)/ bi_permission_api_log(api) 数据表获得的统计信息
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    access_source = models.IntegerField(default=0)  # 访问来源：0 WEB, 1 API
    table_content = models.CharField(max_length=5000, default='')  # 报表的内容，json存储

    class Meta:
        db_table = 'monitor_bi_access_analysis'  # 自定义表名称


class MonitorBiNoteWorthyLog(BaseModel):
    """
    从数据库中查询的值得注意的访问日志记录，
    从数据库 guazi_bi 分析 bi_permission_logs(web)/ bi_permission_api_log(api) 数据表获得的日志信息
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    access_source = models.IntegerField(default=0)  # 访问来源：0 WEB, 1 API
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
        db_table = 'monitor_bi_noteworthy_log'  # 自定义表名称


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


class MonitorBiDataMsg(BaseModel):
    """
    BI数据快照监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    t_id = models.CharField(max_length=255)  # 报表ID
    t_name = models.CharField(max_length=255)  # 报表名称
    indicator_name = models.CharField(max_length=255)  # 指标名称
    search_time = models.CharField(max_length=100)  # 查询时间
    search_type = models.CharField(max_length=100)  # 分组类型
    old_value = models.CharField(max_length=255)  # 上次查询值
    new_value = models.CharField(max_length=100)  # 此次查询值
    deviation = models.CharField(max_length=100)  # 偏差值

    class Meta:
        db_table = 'monitor_bi_data_msg'  # 自定义表名称


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


class MonitorBiEnumerationMsg(BaseModel):
    """
    BI业务源库枚举值监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    db_mname = models.CharField(max_length=100)  # 数据库
    t_name = models.CharField(max_length=255)  # 表名称
    t_col = models.CharField(max_length=100)  # 字段
    t_value = models.CharField(max_length=1000)  # 枚举值
    error_value = models.CharField(max_length=100)  # 异常值

    class Meta:
        db_table = 'monitor_bi_enumeration_msg'  # 自定义表名称


class MonitorBiInterfaceMsg(BaseModel):
    """
    BI接口监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    t_name = models.CharField(max_length=255)  # 报表名称
    t_id = models.CharField(max_length=100)  # 报表ID
    http_status = models.CharField(max_length=50)  # HTTP状态
    search_type = models.CharField(max_length=50)  # 查询类型
    monitor_type = models.CharField(max_length=50)  # 监控类型
    history_error = models.CharField(max_length=50)  # 历史错误次数
    continuous_error = models.CharField(max_length=50)  # 连续错误次数

    class Meta:
        db_table = 'monitor_bi_interface_msg'  # 自定义表名称


class MonitorBiScriptsMsg(BaseModel):
    """
    BI数据清洗脚本监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    alert_msg = models.CharField(max_length=255)  # 警报信息
    script_name = models.CharField(max_length=255)  # 脚本名称
    script_status = models.CharField(max_length=50)  # 脚本状态
    start_time = models.CharField(max_length=50)  # 脚本开始时间
    monitor_time = models.CharField(max_length=50)  # 监控查询时间

    class Meta:
        db_table = 'monitor_bi_scripts_msg'  # 自定义表名称


class MonitorBiSourceDataMsg(BaseModel):
    """
    BI与业务源指标监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    indicator_name = models.CharField(max_length=255)  # 指标名称
    search_time = models.CharField(max_length=100)  # 查询时间
    source_value = models.CharField(max_length=50)  # 业务库值
    bi_value = models.CharField(max_length=50)  # BI库值
    deviation = models.CharField(max_length=50)  # 偏差值
    new_data_time = models.CharField(max_length=50)  # 最新数据时间
    script_time = models.CharField(max_length=50)  # 脚本捕获时间
    devi_reason = models.CharField(max_length=200)  # 偏差原因

    class Meta:
        db_table = 'monitor_bi_source_data_msg'  # 自定义表名称


class MonitorBiSourceGroupByMsg(BaseModel):
    """
    BI与业务源字段监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    indicator_name = models.CharField(max_length=255)  # 指标名称
    source_name = models.CharField(max_length=100)  # 业务源表
    target_name = models.CharField(max_length=50)  # 目标表
    search_time = models.CharField(max_length=50)  # 查询时间段
    col_value = models.CharField(max_length=50)  # 字段值
    source_number = models.CharField(max_length=50)  # 业务库数量
    target_number = models.CharField(max_length=50)  # BI库数量
    deviation = models.CharField(max_length=200)  # 偏差原因

    class Meta:
        db_table = 'monitor_bi_source_groupby_msg'  # 自定义表名称


class MonitorCubesTablesMsg(BaseModel):
    """
    CUBES接口table监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    t_name = models.CharField(max_length=100)  # 表名称
    source_name = models.CharField(max_length=100)  # source名称
    http_status = models.CharField(max_length=50)  # HTTP状态

    class Meta:
        db_table = 'monitor_cubes_table_msg'  # 自定义表名称


class MonitorCubesColumnMsg(BaseModel):
    """
    CUBES接口column监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    t_name = models.CharField(max_length=255)  # 报表名称
    source_name = models.CharField(max_length=100)  # source名称
    http_status = models.CharField(max_length=50)  # HTTP状态

    class Meta:
        db_table = 'monitor_cubes_column_msg'  # 自定义表名称


class MonitorCubesUvPvMsg(BaseModel):
    """
    CUBES用户行为监控错误信息记录表
    """
    email_recorder_id = models.IntegerField(default=0)  # 所属的邮件id
    cubes_date = models.CharField(max_length=255)  # 日期
    cubes_name = models.CharField(max_length=100)  # CUBE名称
    usr_name = models.CharField(max_length=50)  # 用户
    usr_email = models.CharField(max_length=50)  # 邮箱
    total_uv = models.CharField(max_length=50)  # UV数量
    total_pv = models.CharField(max_length=50)  # PV数量

    class Meta:
        db_table = 'monitor_cubes_uv_pv_msg'  # 自定义表名称


# monitor_bi下的表名
class MonitorBiApi(models.Model):
    t_id = models.CharField(max_length=255, verbose_name='报表ID')
    t_name = models.CharField(max_length=255, blank=True, default='', verbose_name='报表名称')
    indicator = models.CharField(max_length=255, verbose_name='指标indicator')
    indicator_name = models.CharField(max_length=255, blank=True, default='', verbose_name='指标名称')
    is_method = models.IntegerField(default=0, verbose_name='方法类型')
    sub_indicator = models.CharField(max_length=1000, blank=True, default='', verbose_name='子指标indicator')
    sub_indicator_name = models.CharField(max_length=1000, blank=True, default='', verbose_name='子指标名称')
    target_id = models.CharField(max_length=255, blank=True, default='', verbose_name='重叠报表ID')
    target_name = models.CharField(max_length=255, blank=True, default='', verbose_name='重叠报表名称')
    target_indicator = models.CharField(max_length=1000, blank=True, default='', verbose_name='重叠指标indicator')
    target_indicator_name = models.CharField(max_length=1000, blank=True, default='', verbose_name='重叠指标名称')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')
    is_complicate = models.IntegerField(default=0, verbose_name='是否重叠指标')

    def __unicode__(self):
        return self.t_id

    class Meta:
        db_table = 'monitor_bi_api'  # 自定义表名称


class MonitorBiCache(models.Model):
    t_id = models.CharField(max_length=255, verbose_name='报表ID')
    t_name = models.CharField(max_length=255, blank=True, default='', verbose_name='报表名称')
    t_type = models.CharField(max_length=255, blank=True, default='', verbose_name='报表类型')
    is_day = models.IntegerField(default=1, verbose_name='是否按天缓存')
    is_month = models.IntegerField(default=1, verbose_name='是否按月缓存')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')

    def __unicode__(self):
        return self.t_id

    class Meta:
        db_table = 'monitor_bi_cache'  # 自定义表名称


class MonitorBiData(models.Model):
    t_id = models.CharField(max_length=255, verbose_name='报表ID')
    t_name = models.CharField(max_length=255, blank=True, default='', verbose_name='报表名称')
    t_type = models.CharField(max_length=255, blank=True, default='', verbose_name='报表类型')
    is_personnel = models.IntegerField(default=0, verbose_name='是否人效报表')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')

    def __unicode__(self):
        return self.t_id

    class Meta:
        db_table = 'monitor_bi_data'  # 自定义表名称


class MonitorBiSourceGroupby(models.Model):
    field_name = models.CharField(max_length=255, verbose_name='指标ID')
    bi_job_id = models.CharField(max_length=100, verbose_name='清洗脚本名称')
    origin_field = models.CharField(max_length=100, blank=True, verbose_name='源字段')
    origin_db = models.CharField(max_length=50, blank=True, verbose_name='源数据库')
    origin_sel = models.CharField(max_length=100, blank=True, verbose_name='源数据字段')
    origin_sql = models.CharField(max_length=3000, blank=True, verbose_name='源数据SQL')
    origin_time_type = models.IntegerField(default=0, verbose_name='源表时间类型')
    target_field = models.CharField(max_length=100, blank=True, verbose_name='目标字段')
    target_db = models.CharField(max_length=50, blank=True, verbose_name='目标数据库')
    target_sel = models.CharField(max_length=100, blank=True, verbose_name='目标数据字段')
    target_sql = models.CharField(max_length=3000, blank=True, verbose_name='目标数据SQL')
    target_time_type = models.IntegerField(default=0, verbose_name='目标表时间类型')
    middle_first_db = models.CharField(max_length=50, blank=True, verbose_name='中间表一数据库')
    middle_first_sel = models.CharField(max_length=100, blank=True, verbose_name='中间表一数据字段')
    middle_first_sql = models.CharField(max_length=3000, blank=True, verbose_name='中间表一数据SQL')
    middle_first_time_type = models.IntegerField(default=0, verbose_name='中间表一时间类型')
    middle_second_db = models.CharField(max_length=50, blank=True, verbose_name='中间表二数据库')
    middle_second_sel = models.CharField(max_length=100, blank=True, verbose_name='中间表二数据字段')
    middle_second_sql = models.CharField(max_length=3000, blank=True, verbose_name='中间表二数据SQL')
    middle_second_time_type = models.IntegerField(default=0, verbose_name='中间表二时间类型')
    is_complicate = models.IntegerField(default=0, verbose_name='是否跨库')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')

    def __unicode__(self):
        return self.field_name

    class Meta:
        db_table = 'monitor_bi_source_groupby'  # 自定义表名称


class MonitorBiTables(models.Model):
    db_name = models.CharField(max_length=50, verbose_name='数据库名称')
    t_id = models.CharField(max_length=50, verbose_name='库表')
    t_name = models.CharField(max_length=200, blank=True, default='', verbose_name='库表名称')
    t_column = models.CharField(max_length=50, blank=True, default='', verbose_name='时间字段')
    time_type = models.IntegerField(default=1, verbose_name='时间类型')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')

    def __unicode__(self):
        return self.t_id

    class Meta:
        db_table = 'monitor_bi_tables'  # 自定义表名称


class MonitorBiEnumeration(models.Model):
    db_name = models.CharField(max_length=50, verbose_name='数据库名称')
    t_name = models.CharField(max_length=200, blank=True, default='', verbose_name='库表名称')
    t_up_col = models.CharField(max_length=50, blank=True, default='', verbose_name='时间字段')
    col_name = models.CharField(max_length=50, blank=True, default='', verbose_name='枚举字段名称')
    col_value = models.CharField(max_length=1000, blank=True, default='', verbose_name='枚举字段列表')
    time_type = models.IntegerField(default=1, verbose_name='时间类型')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')

    def __unicode__(self):
        return self.t_name

    class Meta:
        db_table = 'monitor_bi_enumeration'  # 自定义表名称


class MonitorBiInterface(models.Model):
    t_id = models.CharField(max_length=100, verbose_name='报表ID')
    t_name = models.CharField(max_length=100, blank=True, default='', verbose_name='报表名称')
    t_type = models.CharField(max_length=100, blank=True, default='', verbose_name='报表类型')
    history_error = models.IntegerField(default=0, verbose_name='历史错误')
    continuous_error = models.IntegerField(default=0, verbose_name='连续错误')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')

    def __unicode__(self):
        return self.t_id

    class Meta:
        db_table = 'monitor_bi_interface'  # 自定义表名称


# monitor_cubes下的表名
class MonitorBiUvPv(models.Model):
    cubes_source = models.CharField(max_length=255, verbose_name='CUBES')
    cubes_name = models.CharField(max_length=255, blank=True, verbose_name='CUBES名称')
    ignore_user_email = models.CharField(max_length=1000, blank=True, default='', verbose_name='不监控用户email')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')

    def __unicode__(self):
        return self.cubes_source

    class Meta:
        db_table = 'monitor_bi_uv_pv'  # 自定义表名称


class MonitorBiColumnTable(models.Model):
    cubes_source = models.CharField(max_length=255, verbose_name='CUBES')
    cubes_name = models.CharField(max_length=255, blank=True, verbose_name='CUBES名称')
    column_source_params = models.CharField(max_length=2000, blank=True, verbose_name='column请求参数')
    table_source_params = models.CharField(max_length=2000, blank=True, verbose_name='table请求参数')
    column_url = models.CharField(max_length=255, blank=True, verbose_name='column请求url')
    table_url = models.CharField(max_length=255, blank=True, verbose_name='table请求url')
    cookies_url = models.CharField(max_length=255, blank=True, verbose_name='cookies请求url')
    login_params = models.CharField(max_length=50, blank=True, verbose_name='login参数')
    cookies = models.CharField(max_length=50, blank=True, verbose_name='cookies')
    is_login = models.IntegerField(default=0, verbose_name='是否login')
    is_cookies = models.IntegerField(default=0, verbose_name='是否cookies')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')

    def __unicode__(self):
        return self.cubes_source

    class Meta:
        db_table = 'monitor_bi_column_table'  # 自定义表名称
