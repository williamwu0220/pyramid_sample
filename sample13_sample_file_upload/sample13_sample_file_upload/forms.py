from pyramid_wtf import FileField, MultiFilesField, SubmitField, Form
from pyramid_wtf import validators

class MyForm(Form):
    file = FileField("單檔")
    files = MultiFilesField("多檔", [validators.FileAllowed(['jpg', 'png'])])
    submit = SubmitField("上傳檔案")
