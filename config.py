WTF_CSRF_ENABLED = False

class BaseConfig(object):
  'Base config class'
  SECRET_KEY = 'aG45!geB8593423)fkFrd4C'
  DEBUG= True
  TESTING = False

import os
basedir = os.path.abspath(os.path.dirname(__file__))
