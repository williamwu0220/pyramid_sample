from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config, view_defaults

class ChildResource:
    
    def __getitem__(self, key):
        raise KeyError

class MyView:

    def __init__(self, request):
        self.request = request
    
    def home(self):
        return Response('c: {}'.format(self.request.context))

    def foo(self):
        return Response('c okla {}'.format(self.request.context))

def get_root(request):
    return ChildResource()

if __name__ == '__main__':
    config = Configurator(root_factory=get_root)
    # /
    config.add_view(MyView, attr='home', context=ChildResource)
    # /foo/bar
    config.add_view(MyView, attr='foo', name='bar', context=ChildResource)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
