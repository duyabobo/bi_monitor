# coding=utf-8
# author='duyabo'
# date='2017/11/22'
# 创建测试数据：
## python manage.py shell
## from create_test_data import *
## create_test_data()
import json
import random
from datetime import timedelta

from bi_monitor_app.models import *


def f0():
    """删除邮件记录"""
    EmailRecord.objects.all().delete()


def f1(msg_table_name):
    """创建邮件记录"""
    record_ids = []
    for i in range(50):
        now = datetime.now()
        record = EmailRecord(
            msg_table_name=msg_table_name,
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
                access_source=source,
                table_content=json.dumps(table_content)
            ).save()


def f3(record_ids):
    """创建值得关注的访问记录信息"""
    for i in record_ids:
        for source in [0, 1]:
            for num in range(random.randint(1, 8)):
                MonitorBiNoteWorthyLog(
                    email_recorder_id=i,
                    access_source=source,
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


def f11(record_ids):
    """创建BI与业务源指标监控错误信息记录表数据"""
    for i in record_ids:
        MonitorBiSourceDataMsg(
            email_recorder_id=i,
            indicator_name='C端的实际带看数（不包括保卖）',
            search_time='2017-11-26 00:00:00 - 2017-11-27 16:04:57',
            source_value='7462',
            bi_value='7450',
            deviation='-12',
            new_data_time='2017-11-27 16:04:57',
            script_time='2017-11-27 16:08:09',
            devi_reason='无新数据，清洗脚本update_appoint_task_middle_table已执行完毕，异常'
        ).save()


def f12(record_ids):
    """BI与业务源字段监控错误信息记录数据"""
    for i in record_ids:
        MonitorBiSourceGroupByMsg(
            email_recorder_id=i,
            indicator_name='C端的实际带看数（不包括保卖）',
            source_name='source_name',
            target_name='target_name',
            search_time='2017-11-26 00:00:00 - 2017-11-27 16:04:57',
            col_value='7462',
            source_number='7450',
            target_number='1234',
            deviation='-12'
        ).save()


def f13(record_ids):
    """CUBES接口column监控错误信息记录表数据"""
    for i in record_ids:
        MonitorCubesColumnMsg(
            email_recorder_id=i,
            t_name='C端售车（不包括保卖）',
            source_name='cube_dw_c_sales',
            http_status='500'
        ).save()


def f14(record_ids):
    """CUBES接口table监控错误信息记录表"""
    for i in record_ids:
        MonitorCubesTablesMsg(
            email_recorder_id=i,
            t_name='C端售车（不包括保卖）',
            source_name='cube_dw_c_sales',
            http_status='400'
        ).save()


def f15(record_ids):
    """访问BI日志统计记录表"""
    for i in record_ids:
        MonitorBiLogWeekReport(
            email_recorder_id=i,
            access_source=random.randint(0,1),
            delay_time_key='1~2s',
            api_count=400,
            percent='23.22',
            average_delay_microseconds='1233.1'
        ).save()


def f16(record_ids):
    """创建测试数据：BI监控指标异常-同比及环比监控错误信息"""
    for i in record_ids:
        MonitorBiApiCompareMsg(
            email_recorder_id=i,
            t_name='运营指标-二手车业绩',
            t_id='used_car_achievement',
            indicator_name='保卖放款',
            indicator_id='finance_give_consigned',
            search_type='环比查询',
            today_value='1',
            compare_value='222',
            compare_result='-100.00%'
        ).save()



def create_test_data():
    import django
    django.setup()
    f0()
    msg_table_name = 'monitor_bi_access_hour_report'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f2(record_ids)
    msg_table_name = 'monitor_bi_access_hour_report'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f3(record_ids)
    msg_table_name = 'monitor_bi_nginx_log_week_report'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f4(record_ids)
    msg_table_name = 'monitor_bi_api_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f5(record_ids)
    msg_table_name = 'monitor_bi_cache_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f6(record_ids)
    msg_table_name = 'monitor_bi_data_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f7(record_ids)
    msg_table_name = 'monitor_bi_enumeration_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f8(record_ids)
    msg_table_name = 'monitor_bi_interface_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f9(record_ids)
    msg_table_name = 'monitor_bi_scripts_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f10(record_ids)
    msg_table_name = 'monitor_bi_source_data_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f11(record_ids)
    msg_table_name = 'monitor_bi_source_groupby_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f12(record_ids)
    msg_table_name = 'monitor_cubes_column_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f13(record_ids)
    msg_table_name = 'monitor_cubes_table_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f14(record_ids)
    msg_table_name = 'monitor_bi_log_week_report'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f15(record_ids)
    msg_table_name = 'monitor_bi_api_compare_msg'
    record_ids = f1(msg_table_name)
    print msg_table_name, record_ids
    f16(record_ids)
