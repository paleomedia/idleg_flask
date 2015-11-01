from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, EqualTo
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  social_id = db.Column(db.String(64), nullable=False, unique=True)
  username = db.Column(db.String(64), nullable=False)
  pwdhash= db.Column(db.String(100))
  email = db.Column(db.String(64), nullable=True)
  party = db.Column(db.String(12))
  website = db.Column(db.String(64))
  district_cong = db.Column(db.Integer)
  district_leg = db.Column(db.Integer)
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  verified = db.Column(db.Boolean)

#New instance instantiation
def __init__(self, username, password):
                self.username = username
                self.pwdhash = generate_password_hash(password)
                             
def __repr__(self):
  return '<User %r>' % (self.username)   

import sunlight

class RegistrationForm(Form):
  username = TextField('Username', [InputRequired()])
  password = PasswordField(
    'Password', [
      InputRequired(), EqualTo('confirm', message='Passwords must match')
    ]
  )
  confirm = PasswordField('Confirm Password', [InputRequired()])
  
class LoginForm(Form):
  username = TextField('Username', [InputRequired()])
  password = PasswordField('Password', [InputRequired()])
  
'''
class Comment(db.Model):
  __tablename__ = 'comments'
comment_id = db.Column(db.Integer, primary_key=True)
nickname = db.Column(db.String(64))
comment = db.Column(db.String(256))
comment_link = db.Column(db.String(200))
comment_type = db.Column(db.String(9))
votes_for = db.Column(db.Integer)
votes_against = db.Column(db.Integer)
flags = db.Column(db.Integer)
bill_id = db.Column(db.String(20))
comment_ip = db.Column(db.String(100))
comment TIMESTAMP DEFAULT CURRENT_TIMESTAMP
comment_parent = db.Column(db.String(20))
approved = db.Column(db.Bool)
  
CREATE TABLE IF NOT EXISTS topics (
topic_id BIGINT(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
topic VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS bills_topics (
bill_id BIGINT(20),
topic_id BIGINT(20)
);

CREATE TABLE IF NOT EXISTS bills (
bill_id VARCHAR(15) NOT NULL PRIMARY KEY,
year YEAR(4),
title MEDIUMBLOB,
bill_name VARCHAR(6),
votes_for BIGINT(20),
votes_against BIGINT(20)
);

CREATE TABLE IF NOT EXISTS lawmakers (
leg_id VARCHAR(9) NOT NULL PRIMARY KEY,
first_name VARCHAR(32) NOT NULL,
last_name VARCHAR(32) NOT NULL,
middle_name VARCHAR(32),
suffix VARCHAR(8),
nickname VARCHAR(32),
district INT(2),
twitter VARCHAR(64),
facebook VARCHAR(64),
website VARCHAR(64),
party VARCHAR(24),
active BOOL,
chamber VARCHAR(12),
photo_url VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS leg_geo (
district INT(2) PRIMARY KEY,
polygon POLYGON NOT NULL
);

CREATE TABLE IF NOT EXISTS user_bills (
bill_id BIGINT(20),
user_id VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS user_friends (
user_id VARCHAR(64),
friend_id VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS user_topics (
user_id VARCHAR(64),
topic_id BIGINT(20)
);

CREATE TABLE IF NOT EXISTS user_lawmakers (
user_id VARCHAR(64),
lawmaker VARCHAR(9)
);

'''
