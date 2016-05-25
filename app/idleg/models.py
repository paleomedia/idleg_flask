from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, RadioField
from wtforms.validators import InputRequired, EqualTo
import datetime
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True)
  pwdhash= db.Column(db.String())
  email = db.Column(db.String(64), nullable=True)
  comments = db.relationship('Comment', backref='username', lazy='dynamic')
  
#  socialid = db.Column(db.String(64), unique=True)
#  party = db.Column(db.String(12))
#  website = db.Column(db.String(64))
#  district_cong = db.Column(db.Integer)
#  district_leg = db.Column(db.Integer)
#  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
#  verified = db.Column(db.Boolean)


  #New instance instantiation
  def __init__(self, username, password, email):
    self.username = username
    self.pwdhash = generate_password_hash(password)
    self.email = email
    
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
    
  def get_comments(self):
    return Comment.query.filter_by(user_id = user.id).order_by(Coment.timestamp.desc())
  
#  def __repr__(self):
#   return '<User %r>' % (self.username)
  
class RegistrationForm(Form):
  username = TextField('Username', [InputRequired()])
# email = TextField('Email Address', [InputRequired()])
  password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
  confirm = PasswordField('Confirm Password', [InputRequired()])
  
class LoginForm(Form):
  username = TextField('Username', [InputRequired()])
  password = PasswordField('Password', [InputRequired()])

class Bill(db.Model):
  __searchable__ = ['bill_name']

  bill_id = db.Column(db.String(6))
  year = db.Column(db.String(4))
  title = db.Column(db.Text)
  bill_name = db.Column(db.String(9), primary_key=True)
  last_updated = db.Column(db.Text)
  votes_for = db.Column(db.Integer)
  votes_against = db.Column(db.Integer)
  comments = db.relationship('Comment', backref='bill_id', lazy='dynamic')

  def __init__(self, bill_id, year, title, bill_name, last_updated, votes_for=0, votes_against=0):
    self.bill_id = bill_id
    self.year = year
    self.title = title
    self.bill_name = bill_name
    self.last_updated = last_updated
    self.votes_for = votes_for
    self.votes_against = votes_against
  
  def __repr__(self):
    return '<Bill %s>' % (self.bill_id)
    
  def get_comments(self):
    return Comment.query.filter_by(bill_id = bill.id).order_by(Coment.timestamp.desc())
  
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    author = db.Column(db.String, db.ForeignKey('user.id'))
    comment_type = db.Column(db.String(8))
    bill_num = db.Column(db.String(8), db.ForeignKey('bill.bill_id'))
    
    def __init__(self, comment, author, position, bill_num, timestamp=datetime.datetime.utcnow()):
      self.body = comment
      self.author = author
      self.comment_type = position
      self.bill_num = bill_num
      self.timestamp = timestamp

class CommentForm(Form):
  comment = TextAreaField('comment')
  position = RadioField('Yea, Neutral or Nay?', choices=[('yea','Yea'),('neutral','Neutral'),('nay','Nay')])
  
  
  
#  def from_json(self, source):
#    if 'bill_id' in source:
#      self.bill_id = source['bill_id']
#    if 'session' in source:
#      self.year = source['session']
#    if 'title' in source:
#      self.completed = source['title']
#    if 'bill_name' in source:
#      self.bill_name = source['bill_name']
#    if 'last_updated' in source:
#      self.last_updated = source['last_updated']
      

