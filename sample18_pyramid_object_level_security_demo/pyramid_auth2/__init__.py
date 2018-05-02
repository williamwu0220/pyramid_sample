from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Everyone, DENY_ALL

class MyTest:
    @property
    def __acl__(self):
        return [DENY_ALL]

class MyPolicy:
    
    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        print(key)
        return MyTest()

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy('mysecret', timeout=30000)
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy)

    config.include('pyramid_jinja2')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('test', '/test', factory=MyPolicy)

    config.scan()
    return config.make_wsgi_app()
