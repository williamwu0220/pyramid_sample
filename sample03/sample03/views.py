from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view(request):
    return {'result_url': request.route_path('result')}

@view_config(route_name='result', renderer='templates/result.jinja2')
def result_view(request):
    # 取得所有的 POST num 的值；若名字不重複(比方 num1 和 num2)可以直接用 request.POST['num1']
    # 和 request.POST['num2'] 取得
    all_num = request.POST.getall('num')
    total = 0
    for each_num in all_num:
        total += int(each_num)
    return {'total': total}
