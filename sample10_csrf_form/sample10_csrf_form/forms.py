from pyramid_wtf import SecureForm, StringField, FileField, MultiFilesField
from pyramid_wtf.validators import InputRequired, FileRequired, FileAllowed

class CSRFForm(SecureForm):
    file = FileField('單檔', [FileRequired(), FileAllowed(['docx'], message='只接受docx')])
    files = MultiFilesField('多檔', [FileRequired(), FileAllowed(['jpg', 'png'], message='只接受圖檔')])
