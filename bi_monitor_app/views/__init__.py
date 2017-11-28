# coding=utf-8
# author='duyabo'
# date='2017/11/15'
# api_id 为 key，对应监控的名称为 value

# 邮件的 email_key 和 邮件名称的对应关系
email_name_dict = {
    'monitor_bi_access_hour_report': 'BI接口访问统计时报',
    'monitor_bi_nginx_log_week_report': 'BI访问日志统计周报',
    'monitor_bi_api_msg': 'BI指标监控告警邮件',
    'monitor_bi_cache_msg': 'BI强制缓存告警邮件',
    'monitor_bi_data_msg': 'BI数据快照监控错误信息邮件',
    'monitor_bi_enumeration_msg': 'BI业务源库枚举值监控错误信息邮件',
    'monitor_bi_interface_msg': 'BI接口监控告警邮件',
    'monitor_bi_scripts_msg': 'BI数据清洗脚本运行状态监控告警邮件',
    'monitor_bi_source_data_msg': 'BI数据与业务源数据监控告警邮件',
    'monitor_bi_source_groupby_msg': 'BI数据与业务源数据字段监控告警邮件',
    'monitor_cubes_column_msg': 'CUBES接口监控告警邮件-column监控',
}

# 邮件的 email_key 和 邮件数据表的表头的对应关系

head_dict = {
    'monitor_bi_access_hour_report': ['#', '统计的起始时间', '统计的结束时间', '响应时间大于10s次数'],
    'monitor_bi_nginx_log_week_report': ['#', '统计的起始时间', '统计的结束时间', '响应时间大于20s的次数'],
    'monitor_bi_api_msg': ['#', '统计的起始时间', '统计的结束时间', 'BI指标监控告警次数'],
    'monitor_bi_cache_msg': ['#', '统计的起始时间', '统计的结束时间', 'BI强制缓存告警次数'],
    'monitor_bi_data_msg': ['#', '统计的起始时间', '统计的结束时间', 'BI监控数据异常次数'],
    'monitor_bi_enumeration_msg': ['#', '统计的起始时间', '统计的结束时间', '库表监控枚举值异常次数'],
    'monitor_bi_interface_msg': ['#', '统计的起始时间', '统计的结束时间', 'BI接口监控告警次数'],
    'monitor_bi_scripts_msg': ['#', '监控开始时间', '监控结束时间', '数据清洗脚本告警次数'],
    'monitor_bi_source_data_msg': ['#', '监控开始时间', '监控结束时间', '监控告警次数'],
    'monitor_bi_source_groupby_msg': ['#', '监控开始时间', '监控结束时间', '监控告警次数'],
    'monitor_cubes_column_msg': ['#', '监控开始时间', '监控结束时间', '监控告警次数'],
}
