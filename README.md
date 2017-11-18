项目介绍：
    本项目实现bi监控任务的配置和展现，
    首先需要脚本定时跑的结果存储到数据库中，
    其次要完成对定时脚本的配置功能，
    最后要提供一个server来查询和展现监控结果。

开发环境：
    python    2.7
    django >= 1.11.6

开发过程：
    如果展示的监控数据表格都是二维表格，不存在表中有表的情况：
        1. 编辑 /bi_monitor_app/templates/index.html
            增加 <body><div><div><ul>下面的<li>，可以拷贝已有的<li>，只需要修改 api_id 属性以及 <a>.text
        2. 编辑 /bi_monitor_app/views/__init__.py
            为字典变量增加一个键值对，其中 key 为第一步的 api_id，value 为第一步的 <a>.text
        3. 不需要新增 view 函数，只需要编辑 /bi_monitor_app/views/index.py 下的 content_detail 和 content_list 函数
            根据 api_id/ item_id 以及自己定义的 model 进行逻辑实现，详细可参考已有例子
    如果展示的表格不是二维表格，比较复杂的表格，上面的第三步骤就需要增加 view 函数，还需要增加 ajax 方法。
