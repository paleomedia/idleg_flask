from flask import render_template, request, Blueprint, jsonify, flash, redirect, url_for, session
from flask import g, session
from werkzeug import abort
from app import app, db
from app import login_manager, facebook
from flask.ext.login import current_user, login_user, logout_user, login_required
from app.idleg.models import User, RegistrationForm, LoginForm, Bills

idleg = Blueprint('idleg', __name__)

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))
    
@idleg.before_request
def get_current_user():
  g.user = current_user

def byteify(input):
  if isinstance(input, dict):
    return {byteify(key):byteify(value) for key,value in input.iteritems()}
  elif isinstance(input, list):
    return [byteify(element) for element in input]
  elif isinstance(input, unicode):
    return input.encode('utf-8')
  else:
    return input

@idleg.route('/register', methods=['GET', 'POST'])
def register():
  if session.get('username'):
    flash('Your are already logged in.', 'info')
    return redirect(url_for('idleg.home'))

  form = RegistrationForm(request.form)

  if request.method == 'POST' and form.validate():
    username = request.form.get('username')
    password = request.form.get('password')
    email= request.form.get('email')
    existing_username = User.query.filter_by(username=username).first()
    if existing_username:
      flash('This username has been already taken. Try another  one.','warning')
      return render_template('register.html', form=form)
    user = User(username, password, email)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash('You are now registered and logged in.', 'success')
    return redirect(url_for('idleg.home'))
  if form.errors:
    flash(form.errors, 'danger')
  return render_template('register.html', form=form)

@idleg.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    flash('You are already logged in.')
    return redirect(url_for('idleg.home'))

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
    return redirect(url_for('idleg.home'))
        
    if form.errors:
      flash(form.errors, 'danger')                 

    return render_template('login.html', form=form)
      
@idleg.route('/facebook-login')
def facebook_login():
  return facebook.authorize(callback=url_for('idleg.facebook_authorized', next=request.args.get('next') or request.referrer or None, _external=True))

@idleg.route('/facebook-login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
  if resp is None:
    return 'Access denied: reason=%s error=%s' % (request.args['error_reason'], request.args['error_description'])
  session['facebook_oauth_token'] = (resp['access_token'], '')
  me = facebook.get('/me?fields=id,name,email')
  user = User.query.filter_by(email=me.data['email']).first()
  if not user:
    user = User(username=me.data['name'], email=me.data['email'], password=me.data['id'])
    db.session.add(user)
    db.session.commit()
                     
  login_user(user)
  flash('Logged in as id=%s name=%s' % (me.data['id'], me.data['name']),'success')
  return redirect(request.args.get('next'))
                         
@facebook.tokengetter
def get_facebook_oauth_token():
 return session.get('facebook_oauth_token')

@idleg.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('idleg.home'))

@idleg.route('/')
@idleg.route('/index')
@idleg.route('/home')
def home():
  form = RegistrationForm(request.form)
  id_bills = Bills.query.all()
  return render_template('home.html', user=current_user, id_bills=id_bills, form=form)

@idleg.route('/about')
def about():
  return render_template('about.html')

@idleg.route('/legislators')
def legislators():
  import sunlight
  from sunlight import openstates
  id_bills = openstates.bills(
    state = 'id',
    search_window = 'session')
  
  return render_template('lawmakers.html')

@idleg.route('/topics')
def topics():
  return render_template('topics.html')

@idleg.route('/bills')
def bills():
#  Get bills from Sunlight and add to database Bills table
#  import sunlight
#  import json
#  from sunlight import openstates
#  id_bills_json = openstates.bills(
#    state = 'id',
#    search_window = 'session')  
#  id_bills = byteify(json.dumps(id_bills_json))
#  for bill in id_bills_json:
#    bill_adder = Bills(bill["bill_id"], bill["session"], bill["title"], bill["id"], bill["updated_at"])
#    db.session.add(bill_adder)
#    db.session.commit()
  
  id_bills = Bills.query.all() 
  return render_template('bills.html', id_bills = id_bills)

@idleg.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404
