// {# 点击选项卡时，表格列表请求 #}
$(document).on("click", ".list-group-item", function () {
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
$(document).on("click", ".pagination li", function () {
    $.get(
        '/list/?api_id=' + $('.list-group .active').attr('api_id') + '&page=' + $('.pagination .active').attr('page'),
        function(data, status) {
            $('#leftCol').html(data);
        }
    )
});
// {# 返回的时候分页列表请求 #}
$(document).on("click", "#back_to_list", function () {
    $.get(
        '/list/?api_id=' + $('.list-group .active').attr('api_id') + '&page=' + $('.pagination .active').attr('page'),
        function(data, status) {
            $('#leftCol').html(data);
            $('.bottomCol').show()
        }
    )
});