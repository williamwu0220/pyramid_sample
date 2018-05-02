from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    config.add_static_view('static', 'static', cache_max_age=3600)
    # for example:
    # 
    # 1.
    # If set config.add_static_view('abc', 'def'), then
    # request.static_route('def/xyz.jpg) will produce /abc/xyz.jpb
    # 
    # 2.
    # If set config.add_static_view('http://img.frontmobi.com', 'myimages'), then
    # request.static_route('myimages/myfile.jpg') will produce http://img.frontmobi.com/myfile.jpg
    config.add_static_view('files_path', settings['files_path'], cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('list', '/list')

    config.scan()
    return config.make_wsgi_app()
