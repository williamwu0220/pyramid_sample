from pyramid.view import view_config
from pyramid_i18n_wrapper import LazyTranslationString
from .forms import TestForm


@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    lts = LazyTranslationString('sample11_i18n')
    _ = lts.translate
    request.__LOCALE__ = 'zh_TW'
    form = TestForm()
    return dict(username=_('username'), form=form, myname=_('myname: ${name}', mapping={'name': '許功蓋'}))
