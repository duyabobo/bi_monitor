# coding=utf-8
# author='duyabo'
# date='2017/11/15'
# api_id 为 key，对应监控的名称为 value

# 邮件的 email_key 和 邮件名称的对应关系
email_name_dict = {
    'bi_access_hour_report': 'bi接口访问统计时报',
    'bi_api_week_report': 'bi访问日志统计周报',
    'bi_indicator_monitor_error_message': 'BI指标监控告警邮件',
    'bi_cache_force_warning_message': 'BI强制缓存告警邮件',
}

# 邮件的 email_key 和 邮件数据表的表头的对应关系

head_dict = {
    'bi_access_hour_report': ['#', '统计的起始时间', '统计的结束时间', '响应时间大于10s次数'],
    'bi_api_week_report': ['#', '统计的起始时间', '统计的结束时间', '响应时间大于20s的次数'],
    'bi_indicator_monitor_error_message': ['#', '统计的起始时间', '统计的结束时间', 'BI指标监控告警次数'],
    'bi_cache_force_warning_message': ['#', '统计的起始时间', '统计的结束时间', 'BI强制缓存告警次数']
}
