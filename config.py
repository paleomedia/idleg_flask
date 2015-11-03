class BaseConfig(object):
  WTF_CSRF_ENABLED = False
  SECRET_KEY = 'aG45!geB8593423)fkFrd4C'
  DEBUG= True
  TESTING = False
  SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

import os
basedir = os.path.abspath(os.path.dirname(__file__))
