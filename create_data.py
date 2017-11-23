# coding=utf-8
# author='duyabo'
# date='2017/11/22'
import json
import random
import time
from bi_monitor_app.models import *


def f1():
    """创建时报记录"""
    for i in range(500):
        now = time.time()*1000
        delta1 = random.randint(1, 1000) * 1000
        HourAnalysis(from_timestamp=now - delta1,
                     end_timestamp=now - delta1 - 3600000).save()


def f4():
    """删除统计信息时报"""
    BiAccessAnalysis.objects.all().delete()


def f2():
    """创建时报统计信息数据"""
    for i in range(500):
        for source in [0, 1]:
            table_content = [
                ['访问次数', 32563, 31288, 560, 404, 238, 64, 9, 0],
                ['占比', 100, 96.08, 1.72, 1.24, 0.73, 0.2, 0.03, 0.0],
                ['平均响应时间(ms)', 384.0, 298.0, 1376.0, 2559.0, 3548.0, 6588.0, 12144.0, 0]
            ] if source == 0 else [
                ['访问次数', 1786, 1382, 144, 204, 34, 19, 3, 0],
                ['占比', 100, 77.08, 8.72, 11.24, 9.73, 1.2, 1.03, 0.0],
                ['平均响应时间(ms)', 846.0, 298.0, 1376.0, 2559.0, 3548.0, 6588.0, 12144.0, 0]
            ]
            BiAccessAnalysis(
                hour_analysis_id=i,
                source=source,
                table_content=json.dumps(table_content)
            ).save()


def f3():
    """创建值得关注的访问记录信息"""
    for i in range(500):
        timestramp = time.time() - random.randint(1, 1000)*1000
        for source in [0, 1]:
            for num in range(random.randint(1, 8)):
                NoteWorthyLog(
                    hour_analysis_id=i,
                    source=source,
                    access_timestamp=timestramp,
                    report_name='report_name',
                    report_id='report_id',
                    user_name='user_name',
                    delay_microseconds=random.random()*1000,
                    parameters='parameters',
                    department_name='department_name',
                    api_key='api_key'
                ).save()


def f5():
    """创建BI指标监控告警数据记录"""
    for i in range(500):
        MonitorBiApiMsg(
            t_id=['operation_both', 'operation_buyer', 'process_index'][random.randint(0, 2)],
            t_name=['运营指标-双约', '运营指标-售车(核心)', '业务概览-C2C绩效考核-C2销售绩效考核过程指标'][random.randint(0, 2)],
            search_time='17/11/23',
            search_type='汇总',
            indicator_name='新增带看工单 和 实际带看',
            indicator_id='evaluation_sign_time and appoint_task_success_consigned',
            bi_value='0小于10',
            compute_value='不小于',
            compute_source='业务概览-C2C绩效考核-C2销售绩效考核过程指标'
        ).save()
