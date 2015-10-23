from flask.ext.sqlalchemy import SQLAlchemy

PRODUCTS = {
  'iphone': {
    'name': 'iphone 5s',
    'category': 'Phones',
    'price': 699,
  },
  'galaxy': {
    'name': 'Samsung Galaxy 5',
    'category': 'Phones',
    'price': 649,
  },
  'ipad-air': {
    'name': 'iPad Air',
    'category': 'Tablets',
    'price': 649,
  }
}

# class User(UserMixin, db.Model):
#    __tablename__ = 'users'
#   id = db.Column(db.Integer, primary_key=True)
#    social_id = db.Column(db.String(64), nullable=False, unique=True)
#    nickname = db.Column(db.String(64), nullable=False)
#    email = db.Column(db.String(64), nullable=True)
#    party = db.Column(db.String(12))
#    website = db.Column(db.String(64))
#    district_cong = db.Column(db.Integer)
#    district_leg = db.Column(db.Integer)
