from pyramid.view import view_config
import colander
from deform.widget import FileUploadWidget
from deform import Form
from deform.exception import ValidationFailure
from deform.schema import FileData
from pyramid.httpexceptions import HTTPFound

class Store(dict):
    def preview_url(self, name):
        return ""

store = Store()

class Schema(colander.MappingSchema):
    file = colander.SchemaNode(FileData(), widget=FileUploadWidget(store))

@view_config(route_name='form', renderer='templates/form.jinja2')
def form_view(request):
    form = Form(Schema())
    if 'submit' in request.POST:
        print('a')
        try:
            params = form.validate(request.POST.items())
            # 把檔案存到 tmp
            f = open('/tmp/out.txt', 'wb')
            f.write(params['file']['fp'].read())
            f.close()
            # 導向 /result 顯示已上傳
            return HTTPFound(location=request.route_url('result'))
        except ValidationFailure:
            return {'form': form}

    return {'form': form}

@view_config(route_name='result', renderer='templates/result.jinja2')
def result_view(request):
    return {}
