from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    try:
        if request.session['is_auth'] is True:
            return {'msg': '已驗證'}
    except:
        pass
    return {'msg': '未認証'}


@view_config(route_name='login', renderer='templates/login.jinja2')
def login_view(request):
    return {'auth_url': request.route_path('auth')}

@view_config(route_name='auth', renderer='templates/auth.jinja2')
def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'william' and password == '1234':
        request.session['is_auth'] = True
        return {'msg': '已認証'}
    else:
        return {'msg': '錯誤'}
