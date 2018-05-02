from pyramid.view import view_config
from pyramid_mailer.mailer import Mailer
from pyramid_mailer.message import Message

@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    mailer = Mailer()
    message = Message(subject="測試信件",
        sender="notify@frontmobi.com",
        recipients=['willie.tw@gmail.com'],
        body="這是測試信")
    mailer.send(message)
    return {}
