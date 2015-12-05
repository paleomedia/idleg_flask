import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

#class BaseConfig(object):
#  'Base config class'
WTF_CSRF_ENABLED = False
SECRET_KEY = 'aG45!geB8593423)fkFrd4C'
DEBUG= True
TESTING = False

# SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

'''
class ProductionConfig(BaseConfig):
  'Production specific config'
  DEBUG = False
  SECRET_KEY = open('/path/to/secret/file').read()

class DevelopmentConfig(BaseConfig):
  'Development environment specific config'
  DEBUG = True
  TESTING = True
  SECRET_KEY = 'Anotherrandomsecretkey'
'''
