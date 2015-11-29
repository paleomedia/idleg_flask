from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, EqualTo
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True)
  pwdhash= db.Column(db.String())
#  social_id = db.Column(db.String(64), unique=True)
#  email = db.Column(db.String(64), nullable=True)
#  party = db.Column(db.String(12))
#  website = db.Column(db.String(64))
#  district_cong = db.Column(db.Integer)
#  district_leg = db.Column(db.Integer)
#  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
#  verified = db.Column(db.Boolean)


  #New instance instantiation
  def __init__(self, username, password):
    self.username = username
    self.pwdhash = generate_password_hash(password)
    
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)
  
  def is_authenticated(self):
    return True
    
  def is_active(self):
    return True
    
  def is_anonymous(self):
    return False
    
  def get_id(self):
    return unicode(self.id)
  
#  def __repr__(self):
#   return '<User %r>' % (self.username)   
  
class RegistrationForm(Form):
  username = TextField('Username', [InputRequired()])
  password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
  confirm = PasswordField('Confirm Password', [InputRequired()])
  
class LoginForm(Form):
  username = TextField('Username', [InputRequired()])
  password = PasswordField('Password', [InputRequired()])

class Bills(db.Model):
  bill_id = db.Column(db.Integer, primary_key=True)
  year = db.Column(db.Integer),
  title = db.Column(db.Text)
  bill_name = db.Column(db.String(6))
  last_updated = db.Column(db.Text)
  votes_for = db.Column(db.Integer)
  votes_against = db.Column(db.Integer)

  def __init__(self, bill_id, year, title, bill_name, last_updated, votes_for=0, votes_against=0):
    self.bill_id = bill_id
    self.year = year
    self.title = title
    self.bill_name = bill_name
    self.last_updated = last_updated
    self.votes_for = votes_for
    self.votes_against = votes_against
  
  def __repr__(self):
    return '<Bill %d>' % (self.bill_id)
