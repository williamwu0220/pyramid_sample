from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/hello.jinja2')
def my_view(request):
    return {'hello_name': request.matchdict['hello_name']}
