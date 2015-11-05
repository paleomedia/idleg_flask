class BaseConfig(object):
  'Base config class'
  WTF_CSRF_ENABLED = False
  SECRET_KEY = 'aG45!geB8593423)fkFrd4C'
  DEBUG= True
  TESTING = False
  SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

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
