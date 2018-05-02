from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    return {'project': 'pyramid_auth2'}

@view_config(route_name='test', permission='aaa')
def test_view(request):
    return Response('hello test')
