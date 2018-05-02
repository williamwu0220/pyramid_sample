from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    return {}

@view_config(route_name='google_login')
def google_login_view(request):
    from pyramid.response import Response
    from authomatic.providers import oauth2
    from authomatic.adapters import WebObAdapter
    from authomatic import Authomatic

    CONFIG = {
        'gl': {
            'class_': oauth2.Google,
            'consumer_key': request.registry.settings['google.key'],
            'consumer_secret': request.registry.settings['google.secret'],
            'scope': ['openid', 'profile', 'email']
        }
    }

    authomatic = Authomatic(config=CONFIG, secret='mysecret')
    response = Response()
    result = authomatic.login(WebObAdapter(request, response), 'gl')
    if result:
        if result.error:
            response.write(result.error.message)
        elif result.user:
            if result.user.credentials:
                # 參考資源 ----------------------------------
                # 套件官方範例程式：
                #   http://peterhudec.github.io/authomatic/examples/pyramid-simple.html

                # 有關 https://www.googleapis.com/plus/v1/people/me
                #   https://developers.google.com/identity/protocols/OpenIDConnect   

                # 使用新舊 API 的 url
                #   https://github.com/omab/python-social-auth/blob/master/social/backends/google.py       
                #   請看 def user_data(self, access_token, *args, **kwargs): (應於 65行)

                # for attr in dir(result.user):
                #     response.write(attr + '<br />')

                # result.user.update() 會使用新的 API，但執行會失敗!!!
                # 即 https://www.googleapis.com/plus/v1/people/me
                result.user.update()
                response.write('<p style="color:red;">')
                response.write('google id: ' + str(result.user.id) + '<br />')
                response.write('google name: ' + str(result.user.name) + '<br />')
                response.write('google email: ' + str(result.user.email) + '<br />')
                response.write('</p>')

                # 使用舊 API url，才可成功取得 userinfo
                url = 'https://www.googleapis.com/oauth2/v1/userinfo'
                gl_response = result.provider.access(url)

                # for attr in dir(gl_response):
                #     response.write(attr + '<br />')

                if gl_response.status == 200:
                    data = gl_response.data
                    response.write('<p style="color:blue;">')
                    response.write('google id: {} <br />'.format(data['id']))
                    response.write('google name: {} <br />'.format(data['name']))
                    response.write('google email: {} <br />'.format(data['email']))
                    response.write('</p>')
                else:
                    response.write('HTTP Status = ' + str(gl_response.status))
    return response

@view_config(route_name='facebook_login')
def facebook_login_view(request):
    from pyramid.response import Response
    from authomatic.providers import oauth2
    from authomatic.adapters import WebObAdapter
    from authomatic import Authomatic

    CONFIG = {
        'fb': {
            'class_': oauth2.Facebook,
            'consumer_key': request.registry.settings['facebook.key'],
            'consumer_secret': request.registry.settings['facebook.secret'],
            'scope': ['public_profile', 'email']
        }
    }

    authomatic = Authomatic(config=CONFIG, secret='mysecret')
    response = Response()
    result = authomatic.login(WebObAdapter(request, response), 'fb')
    if result:
        if result.error:
            response.write(result.error.message)
        elif result.user:
            if result.user.credentials:
                url = 'https://graph.facebook.com/me?fields=id,name,email,first_name,last_name'
                fb_response = result.provider.access(url)
                if fb_response.status == 200:
                    data = fb_response.data
                    response.write('facebook id: {} <br />'.format(data['id']))
                    response.write('facebook name: {} <br />'.format(data['name']))
                    response.write('facebook first name: {} <br />'.format(data['first_name']))
                    response.write('facebook last name: {} <br />'.format(data['last_name']))
                    response.write('facebook email: {} <br />'.format(data['email']))
    return response
