项目介绍：
    本项目实现bi监控任务的配置和展现，
    首先需要脚本定时跑的结果存储到数据库中，
    其次要完成对定时脚本的配置功能，
    最后要提供一个server来查询和展现监控结果。

部署过程：
    1. 运行环境
        mac/linux/windows均可，python 版本为 2.7。
    2. py包
        项目依赖的py包都记录在 bi_monitor/requirements.txt 中。
    3. db配置
        数据库使用自带的 sqlite3。
    4. 数据表table结构
        数据表的结构可以参考 bi_monitor/sql.bac 文件中的 create table 语句。
    5. 部署步骤(首先进入bi_data_monitor工作目录)
        cd bi_monitor
        pip install -f requirements.txt
        python manage.py runserver &

开发过程：
    如果有新增的监控数据展示到本系统中，依照下面步骤开发即可
    1. 编辑 /bi_monitor_app/views/__init__.py
        为字典变量 email_name_dict 增加一个键值对
        其中 key 为新增监控的数据表名称 db_table_name，value 为 邮件名称 email_name
    2. 不需要新增或编辑 view 函数
        在 views/utils 下新增一个以 db_table_name 为名字的 py 文件， 实现自己定义的 model 进行逻辑实现
        在 views/index.py 增加 import 语句，把新增的 views/utils/db_table_name 模块导入进来
        详细可参考已有例子

后续开发者可以参考下面的 `文件目录说明` 和 `项目实现逻辑说明`，进行项目维护或者项目扩展。
文件目录说明：
    bi_monitor
        |____bi_monitor    # project 基本文件
        |    |____settings.py   # 配置文件
        |    |____urls.py    # 路由规则最顶层配置
        |    |____wsgi.py
        |
        |____bi_monitor_app   # 监控展示的app项目
        |    |____migrations   # django orm 维护 db 结构的文件，不用管
        |    |____static    # css 和 js 文件，其中 base.css 和 base.js 是我自己写的
        |    |____templates    # html 文件
        |    |    |____base.html    # 基本 html 文件，包括 js、css 导入，还有页面中各个 block 的定义
        |    |    |____email_detail.html    # 用来渲染邮件详情数据的 html 文档
        |    |    |____email_list.html    # 用来渲染邮件列表的 html 文档
        |    |    |____index.html    # extend 了 base.html，实现了 left_list 这个 block
        |    |    |____pager_info.html    # 分页器的实现
        |    |
        |    |____views    # 视图逻辑实现的文件
        |    |    |____utils    # email_detail 这个路由规则的真正实现代码在这里
        |    |    |______init__.py    # 维护邮件数据表名和邮件名称的对应关系
        |    |    |____index.py    # 视图实现部分，总共有四个视图
        |    |
        |    |____admin.py    # admin 配置
        |    |____apps.py
        |    |____models.py   # ORM 数据表的 model 实现
        |    |____urls.py    # app 的 路由规则
        |
        |____.gitignore    # git 忽略规则
        |____create_test_data.py    # 创造测试数据的脚本，运行规则见脚本文档
        |____manage.py
        |____README.md
        |____requirements.txt    # 需要安装的py包
        |____sql.bac    # mysql 数据表的创建语句维护在这里

项目实现逻辑说明：
    1. 这个项目就一个页面就是 templates/index.html
    2. 包括四个接口:
        '/' 接口用来获取项目页面元素，使用到 index.html 模板
        '/list/' 接口用来获取某一类别邮件列表数据，使用到 email_list.html 模板
        '/content/' 接口用来获取某一个邮件的具体邮件内容，使用到 email_detail.html 模板
        '/get_pager/' 接口会返回分页器的 html 代码，使用到 pager_info.html 模板
    3. 后面三个接口的返回结果都是 html 格式的数据，都是服务于第一个接口 '/'
       实现方式是使用 ajax 响应对应的点击操作，对 '/list/'、'content'、'get_pager' 这三个对应接口发出请求
       然后把这三个接口的 response 使用 jquery 填充到 index.html 文件的对应标签中
    4. 其中 '/content/' 视图的实现需要对每一种邮件进行区别的去逻辑处理
       为了避免 '/content/' 视图过于臃肿，email_detail 视图函数只实现对邮件类别的分类处理
       具体某种邮件的详情数据获取逻辑都是在 views/utils 下面去实现的
