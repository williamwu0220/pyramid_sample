from pyramid.view import view_config
from . import forms
from deform import Form
from deform.exception import ValidationFailure
from pyramid.httpexceptions import HTTPFound
import sqlite3


@view_config(route_name='form', renderer='templates/form.jinja2')
def form_view(request):
    form = Form(forms.Schema())
    if 'submit' in request.POST:
        try:
            params = form.validate(request.POST.items())
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()
            cursor.execute('insert into info values (?, ?)', (params['name'], params['age']))
            conn.commit()
            conn.close()
            return HTTPFound(location=request.route_url('list'))
        except ValidationFailure as e:
            return {'form': form}
    else:
        return {'form': form}

@view_config(route_name='list', renderer='templates/list.jinja2')
def list_view(request):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('select name, age from info')
    result = []
    for each_record in cursor:
        result.append({'name': each_record[0], 'age': each_record[1]})
    return {'result': result}
