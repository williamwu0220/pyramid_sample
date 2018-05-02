from pyramid_wtf import Form, StringField, SelectField
from pyramid.threadlocal import get_current_request
from pyramid_i18n_wrapper.wtforms import wtforms_translation_string_factory

_ = wtforms_translation_string_factory('i18n')

class LocaleForm(Form):
    locale = SelectField(_('locale'),
                         choices=[('en', 'en'), ('zh_TW', 'zh_TW')])
