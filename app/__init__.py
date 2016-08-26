import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.login import LoginManager
from flask.ext.wtf import Form
from flask_wtf.csrf import CsrfProtect
from flask_oauth import OAuth
from config import basedir
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
csrf = CsrfProtect(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'idleg.login'

oauth = OAuth()

twitter = oauth.remote_app('twitter', \
    base_url='https://api.twitter.com/1/', \
    request_token_url='https://api.twitter.com/oauth/request_token', \
    access_token_url='https://api.twitter.com/oauth/access_token', \
    authorize_url='https://api.twitter.com/oauth/authenticate', \
    consumer_key='nZRuF6tkYBLbhUvrHfauHK88a', \
    consumer_secret='n15RO8Xh0XgnB5ia1779cb9xKCF7pn5JKie161vSzd3lXzxh9W' \
)

facebook = oauth.remote_app('facebook', \
    base_url='https://graph.facebook.com/', \
    request_token_url=None, \
    access_token_url='/oauth/access_token', \
    authorize_url='https://www.facebook.com/dialog/oauth', \
    consumer_key='1172176769479154', \
    consumer_secret='789db0a5084f84ca460f66a9b44d2666', \
    request_token_params={'scope': 'email'})

from app.idleg import views, models
from app.idleg.views import idleg
from app.idleg import views
from app.api.views import apiModule

app.register_blueprint(apiModule)
app.register_blueprint(idleg)


csrf.exempt(apiModule)


# from app.auth.views import auth
# app.register_blueprint(auth)

db.create_all()



