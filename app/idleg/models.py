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
