# coding=utf-8
# author='duyabo'
# date='2017/11/22'
import json
import random
from datetime import datetime, timedelta
from bi_monitor_app.models import *


def f0():
    """删除邮件记录"""
    EmailRecord.objects.all().delete()


def f1():
    """创建邮件记录"""
    record_ids = []
    for i in range(20):
        now = datetime.now()
        record = EmailRecord(
            email_key='monitor_bi_data_msg',
            analysis_datetime=str(now)[:-10],
            from_datetime=str(now - timedelta(hours=random.randint(0, 24)))[:-10],
            end_datetime=str(now - timedelta(hours=random.randint(0, 24)))[:-10],
        )
        record.save()
        record_ids.append(record.id)
    return record_ids


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
                email_recorder_id=i,
                source=source,
                table_content=json.dumps(table_content)
            ).save()


def f3():
    """创建值得关注的访问记录信息"""
    for i in range(500):
        for source in [0, 1]:
            for num in range(random.randint(1, 8)):
                NoteWorthyLog(
                    email_recorder_id=i,
                    source=source,
                    access_datetime=str(datetime.now())[:-10],
                    report_name='report_name',
                    report_id='report_id',
                    user_name='user_name',
                    delay_microseconds=random.random()*1000,
                    parameters='parameters',
                    department_name='department_name',
                    api_key='api_key'
                ).save()


def f4():
    """创建周报测试数据"""
    for i in range(500):
        analysis_type = random.randint(0,1)
        BiNginxLogWeekReport(
            email_recorder_id=i,
            analysis_type=analysis_type,
            analysis_key=[200, 300, 400, 404, 499, 500][random.randint(0, 5)]
            if analysis_type==0
            else ['0~1s', '1~2s', '2~3s', '3~5s', '5~10s', '10~20s', '20s+'][random.randint(0,6)],
            api_count=random.randint(100, 1000),
            percent=random.randint(0, 100),
            average_delay_microseconds=random.randint(0, 20000)
        ).save()


def f5():
    """创建BI指标监控告警数据记录"""
    for i in range(500):
        MonitorBiApiMsg(
            email_recorder_id=i,
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


def f6():
    """创建bi强制缓存报警信息数据"""
    for i in range(500):
        MonitorBiCacheMsg(
            email_recorder_id=i,
            t_id='c2c_recheck_without_consign',
            t_name='c2c_recheck_without_consign',
            http_status=500,
            search_type=['今日','当月'][random.randint(0,1)],
            error_time='2017-11-23 16:20:48'
        ).save()


def f7(record_ids):
    """BI强制缓存监控错误信息数据测试数据创建"""
    MonitorBiDataMsg.objects.all().delete()
    for i in record_ids:
        MonitorBiDataMsg(
            email_recorder_id=i,
            t_id='c2c_recheck_without_consign',
            t_name='运营指标-C2C业绩',
            indicator_name='for_sale_car_source_c2c',
            search_time='17/11/25',
            search_type='南区',
            old_value='50681',
            new_value='49428',
            deviation='-12312'
        ).save()


def create_test_data():
    record_ids = f1()
    print record_ids
    f7(record_ids)
