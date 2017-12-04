// 请求邮件列表
function email_item_list() {
    $.get(
        '/list/?api_id=' + $('#sidebar > div a.active').attr('api_id'),
        function(data, status) {
            $('#rightCol').html(data);
        }
    );
}

// {# 点击选项卡时，表格列表请求 #}
function reloadRight() {
    email_item_list();
    var api_id = $('#sidebar > div a.active').attr('api_id');
    if (api_id !== 'collect_real_time') {
        $.get(
            '/get_pager/?api_id=' + api_id,
            function (data, ststus) {
                $('.bottomCol').html(data);
            }
        );
        $('.bottomCol').show();
    }
    else {
        $('.bottomCol').html('');
    }
}

// 只有处于首页时，才会自动刷新监控实时汇总信息
function reloadCollectAuto() {
    if ($('.bottomCol').attr('style')==="display: block;" && $('#sidebar > div > a:nth-child(1)').hasClass('active')){
        email_item_list();
    }
}

$(document).on("click", ".click-on", function () {
    $('.list-group a').removeClass('active');
    $(this).addClass('active');
    reloadRight();
});
// {# 表格详情请求 #}
$(document).on("click", ".my_list_item", function () {
    $.get(
        '/content/?api_id=' + $(this).attr('api_id') + '&item_id=' + $(this).attr('item_id') + '&analysiss_time=' + $(this).attr('analysiss_time'),
        function(data, status) {
            $('#rightCol').html(data);
            $('.bottomCol').hide();
        }
    )
});

// 分页器对首页（末页）时，上一页（下一页）不能点击的逻辑实现
function disableButtonLogic() {
    if ($('#pageSelect > li.sel-page').text() === '1')
    {
        $('#prePage').attr('disabled', 'disabled');
        $('#firstPage').attr('disabled', 'disabled');
    }
    else
    {
        $('#prePage').removeAttr('disabled');
        $('#firstPage').removeAttr('disabled');
    }
    if ($('#pageSelect > li.sel-page').text() === $('#page_num').text())
    {
        $('#nextPage').attr('disabled', 'disabled');
        $('#lastPage').attr('disabled', 'disabled');
    }
    else
    {
        $('#nextPage').removeAttr('disabled');
        $('#lastPage').removeAttr('disabled');
    }
}

// {# 分页列表请求 #}
$(document).on("click", "#pageSelect li", function () {
    $.get(
        '/list/?api_id=' + $('.list-group .active').attr('api_id') + '&page=' + $("#pageSelect .sel-page").text(),
        function(data, status) {
            $('#rightCol').html(data);
        }
    );
    disableButtonLogic();
});
$(document).on("click", "#box button", function () {
    $.get(
        '/list/?api_id=' + $('.list-group .active').attr('api_id') + '&page=' + $("#pageSelect .sel-page").text(),
        function(data, status) {
            $('#rightCol').html(data);
        }
    );
    disableButtonLogic();
});
// {# 返回的时候分页列表请求 #}
$(document).on("click", "#back_to_list", function () {
    $.get(
        '/list/?api_id=' + $('.list-group .active').attr('api_id') + '&page=' + $("#pageSelect .sel-page").text(),
        function(data, status) {
            $('#rightCol').html(data);
            $('.bottomCol').show()
        }
    );
    disableButtonLogic();
});

// {# 左侧表格展开或折叠 #}
$(document).on("click", "a.father", function () {
    next = $(this).next();
    if (next.attr('class') === 'hidden')
    {
        $('#sidebar > div > li').attr('class', 'hidden');
        next.removeAttr('class');
    }
    else
    {
        next.attr('class', 'hidden');
    }
});
