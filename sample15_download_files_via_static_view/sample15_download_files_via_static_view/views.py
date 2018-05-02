from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.jinja2', request_method='GET')
def home_view_via_get(request):
    return {}

@view_config(route_name='home', request_method='POST')
def home_view_via_post(request):
    import os
    from pyramid.httpexceptions import HTTPFound

    filename = request.POST['myfile'].filename
    input_file = request.POST['myfile'].file

    with open(os.path.join(request.registry.settings['files_path'], filename), 'wb') as output_file:
        output_file.write(input_file.read())

    return HTTPFound(location=request.route_path('list'))

@view_config(route_name='list', renderer='templates/list.jinja2')
def list_view(request):
    import os
    from glob import glob

    files = glob(os.path.join(request.registry.settings['files_path'], '*'))
    return {'files': files}
