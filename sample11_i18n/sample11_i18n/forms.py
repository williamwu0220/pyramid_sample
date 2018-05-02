from pyramid_wtf import Form, StringField
from pyramid_i18n_wrapper.wtforms import wtforms_translation_string_factory

_ = wtforms_translation_string_factory('sample11_i18n')

class TestForm(Form):
    email = StringField(_('email'))
    quantity = StringField(_('quantity: (max ${max_quantity})', mapping={'max_quantity': 30}))
