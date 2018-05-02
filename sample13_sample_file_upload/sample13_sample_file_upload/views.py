from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from .forms import MyForm

@view_config(route_name='home', renderer='templates/home.jinja2', request_method='GET')
def home_view_via_get(request):
    form = MyForm()
    return {'form': form}

@view_config(route_name='home', renderer='templates/home.jinja2', request_method='POST')
def home_view_via_post(request):
    form = MyForm(request.POST)
    if form.validate():
        # handling one file upload, and saving the file to current directory
        if form.file.data is not None:
            single_file = form.file.data
            with open(single_file.filename, 'wb') as output_file:
                output_file.write(single_file.file.read())

        # handling multi files uploads, and saving files to current directory
        if form.files.data is not None:
            for each_file in form.files.data:
                with open(each_file.filename, 'wb') as output_file:
                    output_file.write(each_file.file.read())
        # redirect to kimo after completing file upload process
        return HTTPFound(location='http://www.kimo.com.tw')
    else:
        return {'form': form}
