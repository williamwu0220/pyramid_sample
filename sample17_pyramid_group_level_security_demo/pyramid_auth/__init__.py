from pyramid.config import Configurator
from pyramid.security import Allow, Deny, Everyone, Authenticated, DENY_ALL
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

def group_finder(userid, request):
    if userid == 'willie':
        return ['group:admin']

class RootFactory:
    __acl__ = [
        (Allow, 'williamwu0220', 'abc'),
        (Allow, 'group:admin', 'abc'),
        DENY_ALL
    ]

    def __init__(self, request):
        pass

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy('mysecret', timeout=30000, callback=group_finder)
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                          root_factory = RootFactory,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy)

    config.include('pyramid_jinja2')


    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    config.scan()
    return config.make_wsgi_app()
