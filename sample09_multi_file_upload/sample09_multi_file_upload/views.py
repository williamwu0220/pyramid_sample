from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from .forms import UploadForm
from . import utils

@view_config(route_name='home', renderer='templates/home.jinja2', request_method='GET')
def home_view_via_get(request):
    form = UploadForm()
    return {'form': form}

@view_config(route_name='home', renderer='templates/home.jinja2', request_method='POST')
def home_view_via_post(request):
    
    form = UploadForm(request.POST)
    if form.validate():
        print(type(form.name.data))
        # 處理上傳檔案
        objFU = utils.ImageFileUpload()

        list_file1_files = objFU.upload_files(form.file1.data, 0, '', 160)
        str_test_2_file = objFU.upload_files(form.file2.data, 1, 'file2', 72)
        str_test_3_file = objFU.upload_files(form.file3.data, 1, 'file3', 16)

        str_test_1 = ''
        str_test_2 = ''
        str_test_3 = ''

        if len(list_file1_files) > 0:
            str_test_1 = '多檔上傳 OK'
        if str_test_2_file != '':
            str_test_2 = '單檔上傳 OK'
        if str_test_3_file != '':
            str_test_3 = '單檔上傳 OK'

        return {'form': form, 'str_message': 'success', 
                'str_test_1': str_test_1, 
                'str_test_2': str_test_2, 'str_test_2_file':str_test_2_file,
                'str_test_3': str_test_3, 'str_test_3_file':str_test_3_file}
        #return HTTPFound(request.route_path('success'))
    else:
        return {'form': form, 'str_message': 'error'}

@view_config(route_name='success', renderer='templates/success.jinja2')
def success_view(request):
    return {}
