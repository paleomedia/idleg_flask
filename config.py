import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  WTF_CSRF_ENABLED = True
  SECRET_KEY = 'aG45!geB8593423)fkFrd4C'
  DEBUG= False
  TESTING = False

class ProductionConfig(Config):
  'Production specific config'
  DEBUG = False

class DevelopmentConfig(Config):
  'Development environment specific config'
  DEVELOPMENT = True
  DEBUG = True
  TESTING = True
