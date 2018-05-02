from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from .forms import LocaleForm
from pyramid_i18n_wrapper import LazyTranslationString

@view_config(route_name='home', renderer='templates/home.jinja2', request_method='GET')
def home_view_get(request):
    lts = LazyTranslationString('i18n')
    _ = lts.translate
    author = _('William Wu')
    author2 = _('Bug Chang')

    # 預設語系為 zh_TW
    response = request.response
    response.set_cookie('_LOCALE_', 'zh_TW')

    return dict(author=author, author2=author2, form=LocaleForm())

@view_config(route_name='home', renderer='templates/home.jinja2', request_method='POST')
def home_view_post(request):
    form = LocaleForm(request.POST)
    
    if form.validate():
        response = request.response
        response.set_cookie('_LOCALE_', form.locale.data)

    # 要將 response.headers 傳入 HTTPFound，否則 http headers 會沒有 cookie 欄位，會視作要清除 cookie
    return HTTPFound(location='/', headers=response.headers)
