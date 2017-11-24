# coding=utf-8
# author='duyabo'
# date='2017/11/22'
import json

from bi_monitor_app.models import BiAccessAnalysis, NoteWorthyLog


def get_detail(email_recorder_id):
    """
    根据 item_id 获取周报报表监控数据
    :param email_recorder_id:
    :return:
    """
    table_datas = [
        [
            ['通过网页访问BI的日志统计', '(12点到13点)'],
            [' ', '全部', '0~1s', '1~2s', '2~3s', '3~5s', '5~10s', '10~20s', '20s +']
        ],
        [
            ['通过网页访问BI的日志报表', '(12点到13点, 响应时间大于10s)'],
            ['访问时刻', '报表名称', '报表ID', '用户名', '执行时间(ms)', '参数'],
            []
        ],
        [
            ['通过API访问BI的日志统计', '(12点到13点)'],
            [' ', '全部', '0~1s', '1~2s', '2~3s', '3~5s', '5~10s', '10~20s', '20s +']
        ],
        [
            ['通过API访问BI的日志报表', '(12点到13点, 响应时间大于10s) '],
            ['访问时刻', '部门', 'method', 'api_key', '执行时间(ms)', '参数'],
            []
        ]
    ]
    bi_analysises = BiAccessAnalysis.get_items(email_recorder_id)
    for b_a in bi_analysises:
        table_content = json.loads(b_a.table_content)
        if b_a.source == 0:
            table_datas[0].append(table_content)
        if b_a.source == 1:
            table_datas[2].append(table_content)
    note_worthies = NoteWorthyLog.get_items(email_recorder_id)
    for n_w in note_worthies:
        content = [
            n_w.access_datetime,
            n_w.department_name,
            n_w.method,
            n_w.api_key,
            n_w.delay_microseconds,
            n_w.parameters
        ]
        if n_w.source == 0:
            table_datas[1][2].append(content)
        if n_w.source == 1:
            table_datas[3][2].append(content)
    return {'table_datas': table_datas}
