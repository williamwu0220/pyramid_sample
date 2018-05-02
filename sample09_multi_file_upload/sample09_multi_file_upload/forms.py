from pyramid_wtf import Form, FileField, StringField
from pyramid_wtf.validators import FileAllowed, FileRequired

class UploadForm(Form):
    name = StringField('名稱')
    # 檔案只能上傳 jpg 和 png
    file1 = FileField('可選多檔', [FileRequired(), FileAllowed(['jpg', 'png'], '只接受 jpg 和 png')])
    file2 = FileField('單一檔案', [FileAllowed(['jpg', 'png'], '只接受 jpg 和 png')])
    file3 = FileField('單一檔案', [FileAllowed(['jpg', 'png'], '只接受 jpg 和 png')])
