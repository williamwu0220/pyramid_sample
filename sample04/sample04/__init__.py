from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = session_factory_from_settings(settings)
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_beaker')
    config.set_session_factory(session_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('login', '/login')
    config.add_route('home', '/')
    config.add_route('auth', '/auth')
    config.scan()
    return config.make_wsgi_app()
