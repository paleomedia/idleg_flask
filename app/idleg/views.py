from flask import render_template, request, Blueprint, jsonify, flash, redirect, url_for, session
from werkzeug import abort
from app import app, db
from app.auth.models import User, RegistrationForm, LoginForm

idleg = Blueprint('idleg', __name__)
auth = Blueprint('auth', __name__)

@idleg.route('/')
@idleg.route('/index')
def home():
  return render_template('index.html')

'''
@idleg.route('/users')
def users():
  users = USer.query.all()
  res = {}
  for user in users:
    res[user.id] = {
      'name' : user.name,
      'email' : user.email
    }
  return jsonify(res)
  
@idleg.route('/product-create', methods=['POST',])
def create_user():
  name = request.form.get('name')
  email = request.form.get('email')
  db.session.add(email)
  db.session.commit()
  return 'User created.'
'''

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404
