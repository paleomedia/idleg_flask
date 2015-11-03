from flask import request, render_template, flash, redirect,  url_for 
from flask import session, Blueprint
from app import app, db
from app.auth.models import User, RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)

# @auth.route('/')
# @auth.route('/home')
# def home():
#  return render_template('home.html')
  
@auth.route('/register', methods=['GET', 'POST'])
def register():
  if session.get('username'):
    flash('Your are already logged in.', 'info')
    return redirect(url_for('idleg.index'))

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
    flash('You are now registered. Please login.', 'success')
    return redirect(url_for('idleg.index'))
  if form.errors:
      flash(form.errors, 'danger')
      
  return render_template('register.html', form=form)
  
@auth.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm(request.form)
    
  if request.method == 'POST' and form.validate():
    username = request.form.get('username')
    password = request.form.get('password')
    existing_user =  User.query.filter_by(username=username).first()
    
    if not (existing_user and existing_user.check_password (password)):
      flash('Invalid username or password. Please try  again.', 'danger')
      return render_template('login.html', form=form)
    
    session['username'] = username
    flash('You have successfully logged in.', 'success')
    return redirect(url_for('idleg.index'))
    
  if form.errors:
    flash(form.errors, 'danger')
    
  return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
  if 'username' in session:
    session.pop('username')
    flash('You have successfully logged out.', 'success')
  return redirect(url_for('idelg.index'))

