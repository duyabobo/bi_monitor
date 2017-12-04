# coding=utf-8
# author='duyabo'
# date='2017/11/15'
# api_id 为 key，对应监控的名称为 value

# 邮件类型列表有序 email_key，这里控制了左侧导航栏的显示顺序

sorted_email_name = [
    'collect_real_time',  # 实时汇总显示最新的报警信息
    'monitor_bi_api_compare_msg',
    'monitor_bi_source_data_msg',
    'monitor_bi_interface_msg',
    'monitor_bi_api_msg',
    'monitor_bi_enumeration_msg',
    'monitor_bi_scripts_msg',
    'monitor_bi_data_msg',
    'monitor_bi_log_report',
    # 'monitor_bi_source_groupby_msg',
    'monitor_bi_cache_msg',
    # 'monitor_cubes_msg'
]

# 邮件的 email_key 和 邮件名称的对应关系
email_name_dict = {
    'collect_real_time': {'title': '最新的前20条报警信息(不包括时报)'},
    'monitor_bi_api_compare_msg': {'title': 'BI指标同比环比监控'},
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
    # 'monitor_bi_source_groupby_msg': {'title': 'BI数据与业务源数据字段监控'},
    # 'monitor_cubes_msg': {
    #     'title': 'CUBES接口监控',
    #     'children': {
    #         'monitor_cubes_column_msg': {'title': 'CUBES接口column监控'},
    #         'monitor_cubes_table_msg': {'title': 'CUBES接口table监控'}
    #     }
    # }
}

# 邮件数据表的表头
email_table_head = ['告警时间', '异常数据量', '告警时间', '异常数据量']

collect_item = 'collect_real_time'

# 汇总实时表头
collect_head = ['告警时间', '告警类型', '告警时间', '告警类型']


def get_flat_email_name_dict():
    """获取 email_name_dict 中的 flat_email_name_dict"""
    flat_email_name_dict = {}
    for k in email_name_dict:
        children = email_name_dict[k].get('children', {})
        if not children:  # 非折叠导航条
            flat_email_name_dict[k] = email_name_dict[k]['title']
        else:  # 折叠内的导航条
            for c_k in children:
                flat_email_name_dict[c_k] = children[c_k]['title']
    return flat_email_name_dict


flat_email_name_dict = get_flat_email_name_dict()
