from flask import render_template, request, Blueprint, jsonify, flash, redirect, url_for, session
from flask import g, session
from werkzeug import abort
from app import app, db
from app import login_manager
from app.auth.models import User, RegistrationForm, LoginForm
from flask.ext.login import current_user
#from app.auth.views import form

idleg = Blueprint('idleg', __name__)
#auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))
    
@idleg.before_request
def get_current_user():
  g.user = current_user

@idleg.route('/')
@idleg.route('/index')
@idleg.route('/home')
def home():
  import sunlight
  from sunlight import openstates
  id_bills = openstates.bills(
      state = 'id',
      search_window = 'session') 
  return render_template('home.html', user=current_user, id_bills=id_bills)

@idleg.route('/about')
def about():
  return render_template('about.html')

@idleg.route('/legislators')
def legislators():
  return render_template('lawmakers.html')

@idleg.route('/topics')
def topics():
  return render_template('topics.html')

@idleg.route('/bills')
def bills():
  import sunlight
  from sunlight import openstates
  id_bills = openstates.bills(
    state = 'id',
    search_window = 'session')  
  return render_template('bills.html', id_bills = id_bills)


@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404
