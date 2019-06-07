from flask import Flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#
# from hrms.auth.views import auth
# from hrms.home.views import home
#
#
# app.register_blueprint(auth.auth)
# app.register_blueprint(auth.home)

# import a blueprint that we will create
from .auth.views import auth
app.register_blueprint(auth)
# url_prefix='/register'

from .home.views import home
app.register_blueprint(home, url_prefix='/homesite')
