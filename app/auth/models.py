from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, EqualTo
from app import db


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100))
  pwdhash= db.Column(db.String())

  #New instance instantiation
  def __init__(self, username, password):
    self.username = username
    self.pwdhash = generate_password_hash(password)
    
  #  social_id = db.Column(db.String(64), nullable=False, unique=True)
  #  email = db.Column(db.String(64), nullable=True)
  #  party = db.Column(db.String(12))
  #  website = db.Column(db.String(64))
  #  district_cong = db.Column(db.Integer)
  #  district_leg = db.Column(db.Integer)
  #  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  #  verified = db.Column(db.Boolean)
                
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
