from pyramid.view import view_config
from pyramid.security import remember, forget, unauthenticated_userid
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='home', renderer='templates/home.jinja2', permission='abc')
def home_view(request):
    return {'project': unauthenticated_userid(request)}

@view_config(route_name='login')
def login_view(request):
    username = request.GET['username']
    headers = remember(request, username)
    return HTTPFound(location=request.route_path('home'), headers=headers)

@view_config(route_name='logout')
def logout_view(request):
    headers = forget(request)
    return HTTPFound(location=request.route_path('home'), headers=headers)
