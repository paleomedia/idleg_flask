from flask import Flask, Blueprint, jsonify, g, session
from app import app,api, db, csrf
from app.idleg.models import User, Bill, Comment
from flask_restful import Resource, Api, reqparse, fields
from app.cache import cache


from flask.views import MethodView

apiModule = Blueprint('apiModule', __name__)
api = Api(app, decorators=[csrf.exempt])

parser = reqparse.RequestParser()
parser.add_argument('comment', type=str)
parser.add_argument('author', type=int)
parser.add_argument('position', type=str)
parser.add_argument('bill', type=str)

class commentApi(Resource):
#@login_required
  def get(self, id):
    if not id:
      abort(404)
    comment = [Comment.query.get(id)]
    result = []
    for c in comment:
      result.append({
      'comment': c.body,
      'timestamp': c.timestamp,
      'author': c.commenter.username,
      'position': c.comment_type,
      'bill': c.bill_num
    })
    return jsonify(results=result)
    
  def post(self):
    args = parser.parse_args()
    comment = args['comment']
    #author = args['current_user.id'] - need to authenticate API caller
    author = args['author']
    position = args['position']
    bill = args['bill']
    newComment = Comment(comment, author, position, bill)
    db.session.add(newComment)
    db.session.commit()
    cache.clear()
    
    return jsonify({'comment': comment, 'author': author, 'position' : position, 'bill': bill})
    
api.add_resource(commentApi, '/api/comment','/api/comment/<int:id>')


#add optional position parameter
class commentsApi(Resource):
  def get(self, bill_deet, position=None):
    if not bill_deet:
      abort(404)
    else:
     #query for comments on current bill
     billComments = [Bill.query.get(bill_deet)]
    if not billComments:
      billComments = 'No comments yet'

    #return json sting of comment for current bill
    result = []
    for billComment in billComments:
      for comment in billComment.comments:
        result.append({
          "commentId": comment.id,
          "commentBody": comment.body,
          "timeStamp": comment.timestamp,
          "author": comment.author,
          "commentType": comment.comment_type,
          "bill": comment.bill_num,
          "bill_id": bill_deet
        })
    if not position:
      return jsonify(results=result)
    else:
      filtered_result = []
      for i in result:
        if i['commentType'] == position:
          filtered_result.append(i)
          print i['commentType']
          print position
    return jsonify(results=filtered_result)
    
api.add_resource(commentsApi, '/api/comments/<string:bill_deet>', '/api/comments/<string:bill_deet>/<string:position>')