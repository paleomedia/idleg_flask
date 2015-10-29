from flask import render_template, request, Blueprint
#from werkzeug import abort

homepage = Blueprint('homepage', __name__)

@homepage.route('/')
@homepage.route('/index')
def homepage_view():
  return render_template('index.html')
