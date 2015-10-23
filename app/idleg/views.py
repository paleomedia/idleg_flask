from werkzeug import abort
from flask import render_template, request, Blueprint
from app.idleg.models import PRODUCTS

idleg_blueprint = Blueprint('idleg', __name__)

@idleg_blueprint.route('/')
@idleg_blueprint.route('/home')
def home():
  return render_template('home.html', products=PRODUCTS)

@idleg_blueprint.route('/product/<key>')
def product(key):
  product = PRODUCTS.get(key)
  if not product:
    abort(404)
  return render_template('product.html', product=product)
