from flask import render_template, request, Blueprint, jsonify, json, flash, redirect, url_for, session, send_from_directory
from flask import g, session
from werkzeug import abort
from app import app, db
from app import login_manager, facebook
from app.cache import cache
from flask_login import current_user, login_user, logout_user, login_required
from app.idleg.models import User, RegistrationForm, LoginForm, SearchForm, Bill, Comment, CommentForm, Lawmaker
from sqlalchemy import cast, Integer, desc
#from flask_restful import Resource, Api
#from flask.ext.restful import reqparse
from json import dumps


idleg = Blueprint('idleg', __name__)
#apiModule = Blueprint('api', __name__)

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))
    
@idleg.before_request
def get_current_user():
  g.user = current_user
  
# function to convert json for sqlite database
def byteify(input):
  if isinstance(input, dict):
    return {byteify(key):byteify(value) for key,value in input.iteritems()}
  elif isinstance(input, list):
    return [byteify(element) for element in input]
  elif isinstance(input, unicode):
    return input.encode('utf-8')
  else:
    return input
    
# routes for login and registrations --------------
@idleg.route('/register', methods=['GET', 'POST'])
def register():
  if session.get('username'):
    flash('Your are already logged in.', 'info')
    return redirect(url_for('idleg.home'))

  r_form = RegistrationForm(request.form, prefix="register-form")

  if request.method == 'POST' and r_form.validate():
    username = request.form.get('username')
    password = request.form.get('password')
    email= request.form.get('email')
    confirm = request.form.get('confirm')
    existing_username = User.query.filter_by(username=username).first()
    if existing_username:
      flash('This username has been already taken. Try another  one.','warning')
      return render_template('register.html', rform=r_form, lform=LoginForm(), )
    user = User(username, password, email)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash('You are now registered and logged in.', 'success')
    return redirect(url_for('idleg.home'))
  if r_form.errors:
    flash(r_form.errors, 'danger')
  return render_template('register.html', lform=LoginForm(), rform=r_form)


@idleg.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    flash('You are already logged in.')
    return redirect(url_for('idleg.home'))

  l_form = LoginForm(request.form, prefix="login-form")

  if request.method == 'POST' and l_form.validate():
    username = request.form.get('username')
    password = request.form.get('password')
    existing_user =  User.query.filter_by(username=username).first()
    if not (existing_user and existing_user.check_password(password)):
      popup = True
      flash('Invalid username or password. Please try  again.', 'danger')
      return render_template('login.html', lform=l_form, rform=RegistrationForm(), popup=popup)
    login_user(existing_user)
    flash('You have successfully logged in.', 'success')
    return redirect(url_for('idleg.home'))
  if l_form.errors:
    popup = True
    flash(l_form.errors, 'danger')
  return render_template('login.html',lform=l_form, rform=RegistrationForm(), popup=popup)
  
@idleg.route('/facebook-login')
def facebook_login():
  return facebook.authorize(callback=url_for('idleg.facebook_authorized', next=request.args.get('next') or request.referrer or None, _external=True))

@idleg.route('/facebook-login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
  if resp is None:
    return 'Access denied: reason=%s error=%s' % (request.args['error_reason'], request.args['error_description'])
  session['facebook_oauth_token'] = (resp['access_token'], '')
  me = facebook.get('/me?fields=id,name,email')
  user = User.query.filter_by(email=me.data['email']).first()
  if not user:
    user = User(username=me.data['name'], email=me.data['email'], password=me.data['id'])
    db.session.add(user)
    db.session.commit()
                     
  login_user(user)
  flash('Logged in as id=%s name=%s' % (me.data['id'], me.data['name']),'success')
  return redirect(request.args.get('next'))
                         
@facebook.tokengetter
def get_facebook_oauth_token():
 return session.get('facebook_oauth_token')

@idleg.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('idleg.home'))
  
@app.route('/favicon.ico')
def favicon():
    import os
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'favicon.ico', mimetype='image/png')

# routes to download data from Sunlight <---- to be automated later
@idleg.route('/populateBills')
def populateBills():
  import sunlight
  import json
  from sunlight import openstates
  id_bill_json = openstates.bills(
    state = 'id'
#    search_window = 'session',
#    updated_since = '2016-03-08'
    )
  print id_bill_json
  id_bills = byteify(json.dumps(id_bill_json))
#  db.session.query(Bill).update({Bill.bill_id:id_bills["bill_id"], Bill.session: id_bills["session"], Bill.title: id_bills["title"], Bill.id: id_bills["id"], Bill.updated_at: id_bills["updated_at"]})
  for bill in id_bill_json:
    bill_adder = Bill(bill["bill_id"], bill["session"], bill["title"], bill["id"], bill["updated_at"])
    db.session.add(bill_adder)
    db.session.commit()
  return id_bills
  
@idleg.route('/populateLawmakers')
def populateLawmakers():
  import sunlight
  import json
  from sunlight import openstates
  id_lm_json = openstates.legislators(
    state = 'id',
    active = 'true'
    )
  print id_lm_json
  id_lm = byteify(json.dumps(id_lm_json))
  for lm in id_lm_json:
    lm_adder = Lawmaker(lm["leg_id"], lm["first_name"], lm["last_name"], lm["middle_name"], lm["district"], lm["chamber"], lm["url"], lm["email"], lm["party"], lm["photo_url"])
    db.session.add(lm_adder)
    db.session.commit()
  return id_lm
  
# main app routes --------------
@idleg.route('/', methods=['GET','POST'])
@idleg.route('/index', methods=['GET','POST'])
@idleg.route('/home', methods=['GET','POST'])
@idleg.route('/index/<int:page>', methods=['GET','POST'])
@cache.cached(timeout=60)
def home(page=1):
  rform = RegistrationForm(request.form)
  lform = LoginForm(request.form)
  comment_form = CommentForm(request.form)
  search_form = SearchForm(request.form)
      
  id_bills = Bill.query.order_by(desc(Bill.last_updated)).paginate(page, 10, False)

  return render_template('home.html', user=current_user, id_bills=id_bills, lform=lform, comment_form=comment_form, search_form=search_form, rform=rform)

# route gets more bills by year by AJAX
'''
@idleg.route('/loadBills', methods=['POST'])
@cache.cached(timeout=5000)
def loadBills():
  # year="2016"
  if request.method == 'POST':
    billyear=request.json['billyear']
    print type(billyear)
  moreBills = Bill.query.order_by(desc(Bill.last_updated)).filter_by(year=billyear)
  return moreBills
'''

@idleg.route('/search', methods=['POST', 'GET'])
def search(page=1):
  import sunlight
  import json
  from sunlight import openstates
  form=SearchForm(request.form)
  
  if request.method == 'POST' and form.validate():
    searchTerm = request.form.get('search')
    
#    if len(year)==1:
#      year = 'session:'+year
#    else:
#      year = 'session:'+year[-1]+'-'+year[0]
    
    house = request.form.get('house')
    if house == 'all':
      house = ''
    
    year = form.year.data
    print year
    if year == []:
      year = [2017]
   
    searchResults = []
    for session in year:
  
      searchResult_json = openstates.bills(
        state = 'id',
        active = 'true',
        chamber = '%s' % house,
        search_window = 'session:%s' % session,
        q = '%s' % searchTerm,
        fields='bill_id'
        )
      searchResults.extend(searchResult_json)
    
    idList = []
    for bill in searchResults:
      idList.append(bill['id'])
    #idList = json.dumps(idList)
    
    rform = RegistrationForm(request.form)
    lform = LoginForm(request.form)
    comment_form = CommentForm(request.form)
    search_form = SearchForm(request.form)
        
    id_bills = Bill.query.filter(Bill.bill_name.in_(idList)).order_by(desc(Bill.last_updated)).paginate(page, 10, False)

    return render_template('home.html', user=current_user, id_bills=id_bills, lform=lform, rform=rform, comment_form=comment_form, search_form=search_form)

@idleg.route('/about')
def about():
  form = RegistrationForm(request.form)
  return render_template('about.html', user=current_user, form=form)

@idleg.route('/lawmakers')
def lawmakers():
  rform = RegistrationForm(request.form)
  lform = LoginForm(request.form)
  lawmakers = Lawmaker.query.order_by(cast(Lawmaker.district, Integer)).all()
  return render_template('lawmakers.html', user=current_user, lform=lform, rform=rform, lawmakers=lawmakers)
  
@idleg.route('/lawmaker/<path:legid>')
def lawmaker(legid):
  rform = RegistrationForm(request.form)
  lform = LoginForm(request.form)
# Get lawmaker detail from Sunlight
  import sunlight
  import json
  from sunlight import openstates
  id_lm_json = openstates.legislator_detail(legid)
  lawmakers = Lawmaker.query.filter_by(leg_id=legid).first()

  return render_template('leg_detail.html', legid=legid, lawmakers=lawmakers, id_lm_json=id_lm_json, user=current_user, lform=lform, rform=rform)

@idleg.route('/topics')
def topics():
  rform = RegistrationForm(request.form)
  lform = LoginForm(request.form)
  return render_template('topics.html', user=current_user, lform=lform, rform=rform)

@idleg.route('/bills/<path:bill_deet>')
def bills(bill_deet):
  rform = RegistrationForm(request.form)
  lform = LoginForm(request.form)
  bill_deets = Bill.query.filter_by(bill_name=bill_deet).first_or_404()
  
# Get bill detail from Sunlight
  import sunlight
  import json
  from sunlight import openstates
  id_bill_json = openstates.bill_detail(
    state = 'id',
    session = '%s' % bill_deets.year,
    bill_id = '%s' % bill_deets.bill_id
    )

#  vote_chart = {}
#  for vote in id_bill_json:
#    for yes_vote in vote.votes:

#      vote_chart_json = json.dumps(vote_chart)
  
  lawmakers = Lawmaker.query.order_by(cast(Lawmaker.district, Integer)).all()
  return render_template('bills.html', bill_deet = bill_deet, user=current_user, id_bill_json=id_bill_json, lawmakers=lawmakers, lform=lform, rform=rform)
  
@idleg.route('/billyear/<path:year>')
@cache.cached(timeout=5000)
def billyear(year):
  rform = RegistrationForm(request.form)
  lform = LoginForm(request.form)
  comment_form = CommentForm(request.form)
  id_bills = Bill.query.order_by(desc(Bill.last_updated)).filter_by(year=year)
  return render_template('home.html', user=current_user, id_bills=id_bills, lform=lform, rform=rform, comment_form=comment_form)
      

@app.route('/comment', methods=['POST'])
@login_required
def add_comment():
  rform = RegistrationForm(request.form)
  lform = LoginForm(request.form)
  if request.method == 'POST' and form.validate():
    comment = request.form.get('comment')
    author = current_user.id
    position = request.form.get('position')
    bill_num = request.form.get('bill_num')
    newComment = Comment(comment, author, position, bill_num)
    db.session.add(newComment)
    db.session.commit()
    cache.clear()
    return jsonify({'comment': comment, 'author': author, 'position' : position, 'bill_num': bill_num})
  flash(form.errors, 'danger')
  return ""

@idleg.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404
