# coding=utf-8
# author='duyabo'
# date='2017/11/15'
# api_id 为 key，对应监控的名称为 value

# 邮件的 email_key 和 邮件名称的对应关系
email_name_dict = {
    'monitor_bi_log_report': {
        'title': 'BI访问日志统计',
        'children': {
            'monitor_bi_access_hour_report': {'title': 'BI访问PHP日志统计时报'},
            'monitor_bi_log_week_report': {'title': 'BI访问PHP日志统计周报'},
            'monitor_bi_nginx_log_week_report': {'title': 'BI访问Nginx日志统计周报'},
        }
    },
    'monitor_bi_api_msg': {'title': 'BI指标接洽监控'},
    'monitor_bi_cache_msg': {'title': 'BI强制缓存监控'},
    'monitor_bi_data_msg': {'title': 'BI数据快照监控'},
    'monitor_bi_enumeration_msg': {'title': 'BI枚举值监控'},
    'monitor_bi_interface_msg': {'title': 'BI接口监控'},
    'monitor_bi_scripts_msg': {'title': 'BI清洗脚本监控'},
    'monitor_bi_source_data_msg': {'title': 'BI数据与业务源数据监控'},
    'monitor_bi_source_groupby_msg': {'title': 'BI数据与业务源数据字段监控'},
    'monitor_cubes_msg': {
        'title': 'CUBES接口监控',
        'children': {
            'monitor_cubes_column_msg': {'title': 'CUBES接口column监控'},
            'monitor_cubes_table_msg': {'title': 'CUBES接口table监控'}
        }
    }
}

# 邮件数据表的表头
email_table_head = ['#', '邮件生成时间', '#', '邮件生成时间']


def get_children_email_name_dict():
    """获取 email_name_dict 中的 children dict"""
    children_name_dict = {}
    for k in email_name_dict:
        children_name_dict.update(email_name_dict[k].get('children', {}))
    return children_name_dict


children_email_name_dict = get_children_email_name_dict()
