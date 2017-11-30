// {# 点击选项卡时，表格列表请求 #}
$(document).on("click", ".click-on", function () {
    $('.list-group a').removeClass('active');
    $(this).addClass('active');
    $.get(
        '/list/?api_id=' + $(this).attr('api_id'),
        function(data, status) {
            $('#leftCol').html(data);
        }
    );
    $.get(
        '/get_pager/?api_id=' + $(this).attr('api_id'),
        function (data, ststus) {
            $('.bottomCol').html(data);
        }
    );
    $('.bottomCol').show()
});
// {# 表格详情请求 #}
$(document).on("click", ".my_list_item", function () {
    $.get(
        '/content/?api_id=' + $(this).attr('api_id') + '&item_id=' + $(this).attr('item_id'),
        function(data, status) {
            $('#leftCol').html(data);
            $('.bottomCol').hide();
        }
    )
});
// {# 分页列表请求 #}
$(document).on("click", "#pageSelect li", function () {
    $.get(
        '/list/?api_id=' + $('.list-group .active').attr('api_id') + '&page=' + $("#pageSelect .sel-page").text(),
        function(data, status) {
            $('#leftCol').html(data);
        }
    );
    if ($('#pageSelect > li.sel-page').text() === '1')
    {
        $('#prePage').attr('disabled', 'disabled');
        $('#firstPage').attr('disabled', 'disabled');
    }
    else
    {
        $('#prePage').removeAttr('disabled');
        $('#firstPage').removeAttr('disabled');
    };
    if ($('#pageSelect > li.sel-page').text() === $('#page_num').text())
    {
        $('#nextPage').attr('disabled', 'disabled');
        $('#lastPage').attr('disabled', 'disabled');
    }
    else
    {
        $('#nextPage').removeAttr('disabled');
        $('#lastPage').removeAttr('disabled');
    };
});
$(document).on("click", "#box button", function () {
    $.get(
        '/list/?api_id=' + $('.list-group .active').attr('api_id') + '&page=' + $("#pageSelect .sel-page").text(),
        function(data, status) {
            $('#leftCol').html(data);
        }
    );
    if ($('#pageSelect > li.sel-page').text() === '1')
    {
        $('#prePage').attr('disabled', 'disabled');
        $('#firstPage').attr('disabled', 'disabled');
    }
    else
    {
        $('#prePage').removeAttr('disabled');
        $('#firstPage').removeAttr('disabled');
    };
    if ($('#pageSelect > li.sel-page').text() === $('#page_num').text())
    {
        $('#nextPage').attr('disabled', 'disabled');
        $('#lastPage').attr('disabled', 'disabled');
    }
    else
    {
        $('#nextPage').removeAttr('disabled');
        $('#lastPage').removeAttr('disabled');
    };
});
// {# 返回的时候分页列表请求 #}
$(document).on("click", "#back_to_list", function () {
    $.get(
        '/list/?api_id=' + $('.list-group .active').attr('api_id') + '&page=' + $("#pageSelect .sel-page").text(),
        function(data, status) {
            $('#leftCol').html(data);
            $('.bottomCol').show()
        }
    );
    if ($('#pageSelect > li.sel-page').text() === '1')
    {
        $('#prePage').attr('disabled', 'disabled');
        $('#firstPage').attr('disabled', 'disabled');
    }
    else
    {
        $('#prePage').removeAttr('disabled');
        $('#firstPage').removeAttr('disabled');
    };
    if ($('#pageSelect > li.sel-page').text() === $('#page_num').text())
    {
        $('#nextPage').attr('disabled', 'disabled');
        $('#lastPage').attr('disabled', 'disabled');
    }
    else
    {
        $('#nextPage').removeAttr('disabled');
        $('#lastPage').removeAttr('disabled');
    };
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
