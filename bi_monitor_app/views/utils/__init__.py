# coding=utf-8
# author='duyabo'
# date='2017/11/18'


def get_detail_example(api_id, item_id):
    """
    获取某一类监控，指定item_id的监控数据
    :param api_id:
    :param item_id:
    :return:
    {
        'table_datas': [
            [
                'test_title_of_table',
                [
                    ['时间', '接口名', '统计数目'],
                    ['2017-11-01 11:01:20', '/api/dashboard?', '20233']
                ]
            ]
        ]
    }
    """
    return {
        'table_datas': [
            [
                'test_title_of_table',
                [
                    ['时间', '接口名', '统计数目'],
                    ['2017-11-01 11:01:20', '/api/dashboard?', '20233']
                ]
            ]
        ]
    }


def get_list_example(api_id):
    """
    获取某一类监控数据的列表，分页显示
    :param api_id:
    :return:
    [
        [1, '2017-11-01'],
        [2, '2017-11-08'],
        [3, '2017-11-15']
    ]
    """
    return [
        [1, '2017-11-01'],
        [2, '2017-11-08'],
        [3, '2017-11-15']
    ]
