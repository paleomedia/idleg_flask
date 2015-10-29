from flask import Flask
from app.idleg.views import homepage
from flask.ext.sqlalchemy import SQLAlchemy
#from flask_oauth import OAuth
# from config import basedir

app = Flask(__name__)
app.register_blueprint(homepage)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db= SQLAlchemy(App)

db.create_all()

''' 
oauth = OAuth()

twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key='nZRuF6tkYBLbhUvrHfauHK88a',
    consumer_secret='n15RO8Xh0XgnB5ia1779cb9xKCF7pn5JKie161vSzd3lXzxh9W'
)

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='1172176769479154',
    consumer_secret='789db0a5084f84ca460f66a9b44d2666',
    request_token_params={'scope': 'email'}
)
'''
