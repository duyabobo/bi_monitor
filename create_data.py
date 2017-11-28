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


def f1(email_key):
    """创建邮件记录"""
    record_ids = []
    for i in range(20):
        now = datetime.now()
        record = EmailRecord(
            email_key=email_key,
            analysis_datetime=str(now)[:-10],
            from_datetime=str(now - timedelta(hours=random.randint(0, 24)))[:-10],
            end_datetime=str(now - timedelta(hours=random.randint(0, 24)))[:-10],
        )
        record.save()
        record_ids.append(record.id)
    return record_ids


def f2(record_ids):
    """创建时报统计信息数据"""
    for i in record_ids:
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
            MonitorBiAccessAnalysis(
                email_recorder_id=i,
                source=source,
                table_content=json.dumps(table_content)
            ).save()


def f3(record_ids):
    """创建值得关注的访问记录信息"""
    for i in record_ids:
        for source in [0, 1]:
            for num in range(random.randint(1, 8)):
                MonitorBiNoteWorthyLog(
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


def f4(record_ids):
    """创建周报测试数据"""
    for i in record_ids:
        analysis_type = random.randint(0,1)
        MonitorBiNginxLogWeekReport(
            email_recorder_id=i,
            analysis_type=analysis_type,
            analysis_key=[200, 300, 400, 404, 499, 500][random.randint(0, 5)]
            if analysis_type==0
            else ['0~1s', '1~2s', '2~3s', '3~5s', '5~10s', '10~20s', '20s+'][random.randint(0,6)],
            api_count=random.randint(100, 1000),
            percent=random.randint(0, 100),
            average_delay_microseconds=random.randint(0, 20000)
        ).save()


def f5(record_ids):
    """创建BI指标监控告警数据记录"""
    for i in record_ids:
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


def f6(record_ids):
    """创建bi强制缓存报警信息数据"""
    for i in record_ids:
        MonitorBiCacheMsg(
            email_recorder_id=i,
            t_id='c2c_recheck_without_consign',
            t_name='c2c_recheck_without_consign',
            http_status=500,
            search_type=['今日','当月'][random.randint(0,1)],
            error_time='2017-11-23 16:20:48'
        ).save()


def f7(record_ids):
    """BI数据快照监控错误信息邮件"""
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


def f8(record_ids):
    """BI业务源库枚举值监控错误信息邮件"""
    for i in record_ids:
        MonitorBiEnumerationMsg(
            email_recorder_id=i,
            db_mname='ctob',
            t_name='vehicle_auction_appoint',
            t_col='receive_result',
            t_value='(4, 1, 7, 11, 5, 6, 2, 3, 12, 0, 8, 25, 19, 28, 9, 14, 22, 13, 15, 18, 17, 24, 20, 16, 33, 26, 21, 32, 23, 27, 31, 30, 29, 39, 35, 36, 37, 34, 40, 38, 41, 42, 43, 44, 47)',
            error_value='12'
        ).save()


def f9(record_ids):
    """创建BI接口监控错误信息记录表测试数据"""
    for i in record_ids:
        MonitorBiInterfaceMsg(
            email_recorder_id=i,
            t_name='vehicle_auction_appoint',
            t_id='receive_result',
            http_status='500',
            search_type='当日',
            monitor_type='报表',
            history_error='25',
            continuous_error='1',
        ).save()


def f10(record_ids):
    """创建BI数据清洗脚本监控错误信息记录测试数据"""
    for i in record_ids:
        MonitorBiScriptsMsg(
            email_recorder_id=i,
            alert_msg='执行超时-30分钟',
            script_name='update_appoint_task_middle_table',
            script_status='1',
            start_time='2017-11-28 04:04:28',
            monitor_time='2017-11-28 04:45:01',
        ).save()


def create_test_data():
    f0()
    email_key = 'monitor_bi_access_hour_report'
    record_ids = f1(email_key)
    print email_key, record_ids
    f2(record_ids)
    email_key = 'monitor_bi_access_hour_report'
    record_ids = f1(email_key)
    print email_key, record_ids
    f3(record_ids)
    email_key = 'monitor_bi_nginx_log_week_report'
    record_ids = f1(email_key)
    print email_key, record_ids
    f4(record_ids)
    email_key = 'monitor_bi_api_msg'
    record_ids = f1(email_key)
    print email_key, record_ids
    f5(record_ids)
    email_key = 'monitor_bi_cache_msg'
    record_ids = f1(email_key)
    print email_key, record_ids
    f6(record_ids)
    email_key = 'monitor_bi_data_msg'
    record_ids = f1(email_key)
    print email_key, record_ids
    f7(record_ids)
    email_key = 'monitor_bi_enumeration_msg'
    record_ids = f1(email_key)
    print email_key, record_ids
    f8(record_ids)
    email_key = 'monitor_bi_interface_msg'
    record_ids = f1(email_key)
    print email_key, record_ids
    f9(record_ids)
    email_key = 'monitor_bi_scripts_msg'
    record_ids = f1(email_key)
    print email_key, record_ids
    f10(record_ids)
