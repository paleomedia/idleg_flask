from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin

db = SQLAlchemy(app)
lm = LoginManager(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    party = db.Column(db.String(12))
    website = db.Column(db.String(64))
    district_cong = db.Column(db.Integer)
    district_leg = db.Column(db.Integer)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@property
  def is_authenticated(self):
    return True

@property
  def is_active(self):
    return True

@property
  def is_anonymous(self):
    return False

def get_id(self):
  try:
    return unicode(self.id)  # python 2
      except NameError:
        return str(self.id)  # python 3

def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
