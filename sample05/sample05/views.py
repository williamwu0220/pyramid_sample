from pyramid.view import view_config
import colander
from deform import Form
from deform.exception import ValidationFailure

class Schema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age  = colander.SchemaNode(colander.Integer(), validator=colander.Range(1, 120))


@view_config(route_name='form', renderer='templates/form.jinja2')
def form_view(request):
    schema = Schema()
    form = Form(schema)
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
        except ValidationFailure as e:
            return {'form': form}
    return {'form': form}
