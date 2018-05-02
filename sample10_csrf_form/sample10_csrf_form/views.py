from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from .forms import CSRFForm


@view_config(route_name='home', renderer='templates/home.jinja2', request_method='GET')
def home_get_view(request):
    form = CSRFForm(meta={'csrf_context': request.session})
    return {'form': form}

@view_config(route_name='home', renderer='templates/home.jinja2', request_method='POST')
def home_post_view(request):
    form = CSRFForm(request.POST, meta={'csrf_context': request.session})
    if form.validate():
        file = form.file.data # file 可以直接讀取
        files = form.files.data
        for each_file in files:
            pass
            # 依序儲存多個檔案
        return HTTPFound('http://www.kimo.com.tw')
    else:
        return {'form': form}
