from pyramid.view import view_config
from pyramid.response import FileResponse

@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    return {}

@view_config(route_name='xlsx')
def xlsx_view(request):
    'use FileResponse to response.'
    from os.path import abspath, dirname
    from urllib.parse import quote
    where_am_i = dirname(abspath(__file__))
    uploads_path = '{}/uploads'.format(where_am_i)
    response = FileResponse('{}/sample.xlsx'.format(uploads_path), request=request, )
    
    # rfc 6266 standards say that we need to url quote our utf-8 filename in this way.
    response.content_disposition = "attachment; filename*=UTF-8''{}".format(quote('試算表.xlsx'))

    return response


