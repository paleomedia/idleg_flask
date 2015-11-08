from flask import request, render_template, flash, redirect,  url_for 
from flask import session, Blueprint, g
from flask.ext.login import current_user, login_user, logout_user, login_required
from app import app, db
from app import login_manager
from app import facebook
from app.auth.models import User, RegistrationForm, LoginForm
#from flask_wtf import Form

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))
  
@auth.before_request
def get_current_user():
  g.user = current_user

@auth.route('/')
@auth.route('/home')
def home():
  return render_template('home.html', user=current_user)
  
@auth.route('/register', methods=['GET', 'POST'])
def register():
  if session.get('username'):
    flash('Your are already logged in.', 'info')
    return redirect(url_for('auth.home'))

  form = RegistrationForm(request.form)
      
  if request.method == 'POST' and form.validate():
    username = request.form.get('username')
    password = request.form.get('password')
    existing_username = User.query.filter_by(username=username).first()
    if existing_username:
      flash('This username has been already taken. Try another  one.','warning')
      return render_template('register.html', form=form)
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash('You are now registered and logged in.', 'success')
    return redirect(url_for('auth.home'))
  if form.errors:
      flash(form.errors, 'danger')
  return render_template('register.html', form=form)
  
@auth.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    flash('You are already logged in.')
    return redirect(url_for('auth.home'))

  form = LoginForm(request.form)
    
  if request.method == 'POST' and form.validate():
    username = request.form.get('username')
    password = request.form.get('password')
    existing_user =  User.query.filter_by(username=username).first()
    
    if not (existing_user and existing_user.check_password(password)):
      flash('Invalid username or password. Please try  again.', 'danger')
      return render_template('login.html', form=form)

    login_user(existing_user)    
    flash('You have successfully logged in.', 'success')
    return redirect(url_for('auth.home'))
    
  if form.errors:
    flash(form.errors, 'danger')
    
  return render_template('login.html', form=form)

@auth.route('/facebook-login')
def facebook_login():
 return facebook.authorize(callback=url_for('auth.facebook_authorized', next=request.args.get('next') or request.referrer or None, _external=True))

@auth.route('/facebook-login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
  if resp is None:
    return 'Access denied: reason=%s error=%s' % (request.args['error_reason'], request.args['error_description'])
  session['facebook_oauth_token'] = (resp['access_token'], '')
  me = facebook.get('/me')
  user = User.query.filter_by(username=me.data['email']).first()
  if not user:
    user = User(me.data['email'], '')
    db.session.add(user)
    db.session.commit()
  
  login_user(user)
  flash('Logged in as id=%s name=%s' % (me.data['id'], me.data['name']),'success')
  return redirect(request.args.get('next'))

@facebook.tokengetter
def get_facebook_oauth_token():
  return session.get('facebook_oauth_token')
 
@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.home'))
