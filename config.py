WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

class BaseConfig(object) :
  'Base config class'
  SECRET_KEY = 'A random secret key'
  DEBUG= True
  TESTING = False

import os
basedir = os.path.abspath(os.path.dirname(__file__))
