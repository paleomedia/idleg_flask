from app import db

class User(db.Model):
   __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  social_id = db.Column(db.String(64), nullable=False, unique=True)
  nickname = db.Column(db.String(64), nullable=False)
  email = db.Column(db.String(64), nullable=True)
  party = db.Column(db.String(12))
  website = db.Column(db.String(64))
  district_cong = db.Column(db.Integer)
  district_leg = db.Column(db.Integer)
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  verified = db.Column(db.bool)
);

# New instance instantiation
def __init__(nickname, email):
    
                self.nickname     = name
                self.email    = email
                self.password = password
                             
def __repr__(self):
  return '<User %r>' % (self.nickname)   

class Comment(db.Model)
  __tablename__ = 'comments'
  
  comment_id = db.Column(db.Integer, primary_key=True)
  nickname = db.Column(db.String(64)
  comment MEDIUMBLOB,
  comment_link VARCHAR(200),
  comment_type VARCHAR(9),
  votes_for TINYINT,
  votes_against TINYINT,
  flags TINYINT,
  bill_id VARCHAR(20),
  comment_ip VARCHAR(100),
  comment TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  comment_parent BIGINT(20),
  approved BOOL
  );
  
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





import sunlight

