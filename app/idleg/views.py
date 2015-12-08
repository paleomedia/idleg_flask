from flask import render_template, request, Blueprint, jsonify, flash, redirect, url_for, session
from flask import g, session
from werkzeug import abort
from app import app, db
from app import login_manager, facebook
from flask.ext.login import current_user, login_user, logout_user, login_required
from app.idleg.models import User, RegistrationForm, LoginForm, Bill, Comment, CommentForm

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
  return render_template('login.html',form=form)
  
      
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
  comment_form = CommentForm(request.form)
  id_bills = Bill.query.all()
  return render_template('home.html', user=current_user, id_bills=id_bills, form=form, comment_form=comment_form)

@idleg.route('/about')
def about():
  form = RegistrationForm(request.form)
  return render_template('about.html', user=current_user, form=form)

@idleg.route('/lawmakers')
def lawmakers():
  form = RegistrationForm(request.form)
  return render_template('lawmakers.html', user=current_user, form=form)

@idleg.route('/topics')
def topics():
  form = RegistrationForm(request.form)
  return render_template('topics.html', user=current_user, form=form)

@idleg.route('/bills/<path:bill_deet>')
def bills(bill_deet):
#  bill_deets = Bill.query.bill_id.get_or_404(bill_name)
#  Get bills from Sunlight and add to database Bills table
  import sunlight
  import json
  from sunlight import openstates
  id_bill_json = openstates.bill_detail(
    state = 'id',
    session = '2015',
    bill_id = '%s' % bill_deet
    )
  return render_template('bills.html', bill_deet = bill_deet, user=current_user, id_bill_json=id_bill_json)

@app.route('/comment', methods=['GET', 'POST'])
@login_required
def add_comment():
  form = CommentForm(request.form)
  if request.method == 'POST' and form.validate():
    comment = request.form.get('comment')
    print comment
    author = current_user.id
    position = request.form.get('position')
    bill_num = request.form.get('bill_num')
    new_comment = Comment(comment, author, position, bill_num)
    db.session.add(comment)
    db.session.commit()
    return jsonify(new_comment)
  flash(form.errors, 'danger')
  return ""


"""
@app.route('/search', methods=['POST'])
def search():
  if not g.search_form.validate_on_submit():
    return redirect(url_for('home'))
  return redirect(url_for('search_results', query=g.search_form.search.data))

@app.route('/search_results/<query>')
def search_results(query):
  results = Bill.query.whoosh_search(query).all()
  return render_template('search_results.html', query=query, results=results)
"""

@idleg.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404
