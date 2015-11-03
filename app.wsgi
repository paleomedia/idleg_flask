activate_this = '<Path to virtualenv>/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from my_app import app as application
import sys, 
logginglogging.basicConfig(stream = sys.stderr)
