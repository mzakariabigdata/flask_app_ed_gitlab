from logging import fatal
from flask_restplus import Resource, Namespace
from flask import request, jsonify, make_response
import requests
from app.api.restplus import api_v1
from app.api.restplus import token_required
from app.dba.models import User
from app.api.user.api_definition import user_post_def, user_get_def
from app.api.user.domain_logic import create_user
from app.dba.models import db
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import OperationalError
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt

ns_users = Namespace('users', description = "users operations")

@ns_users.route('/login')
class UserLogin(Resource):
    def get(self):
        return True, 200
    
    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        user = User.query.filter_by(name=auth.username).first()

        if not user:
            return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'SECRET_KEY', algorithm="HS256")
            return jsonify({'token' : token})

        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

@ns_users.route('/')
@ns_users.doc(security='apikey')
class UsersList(Resource):
    
    @api_v1.marshal_with(user_get_def)
    @token_required
    def get(current_user, self):
        """
        returns a list of users
        """
        if not current_user.admin:
            print(current_user)
            return jsonify({'message' : 'Cannot perform that function!'})


        try:
            res = User.query.all()
        except NoResultFound as e:
            return None, 404
        return res
    
    @api_v1.expect(user_post_def)
    def post(self):
        print("________zaal___________________________________")
        # data = request.get_json()
        
        res = create_user(request.get_json())
        return 'New user created !', 201

    def put(self):
        return True, 405
    
    def patch(self):
        return True, 405

    def delete(self):
        return True, 205

@ns_users.doc(params={'user_id': 'An ID'})
@ns_users.route('/<string:user_id>')
class UserItem(Resource):
    
    @api_v1.marshal_with(user_get_def)
    def get(self, user_id):
        """
        returns a list of User
        """
        try:
            res = User.query.filter(User.id == user_id).one()
        except NoResultFound as e:
            return False, 404
        return res, 200

    @api_v1.expect(user_post_def)
    @api_v1.response(204, 'User update')
    @api_v1.response(404, 'User not found')
    def patch(self, user_id):
        try:
            res = User.query.filter(User.id == user_id).one()
            res.admin = True
            db.session.commit()
        except NoResultFound as e:
            return False, 404
        return {'message': 'User update'}, 204
    
    @api_v1.response(205, 'User deleted')
    def delete(self, user_id):
        try:
            res = User.query.filter(User.id == user_id).one()
            db.session.delete(res)
            db.session.commit()
        except NoResultFound as e:
            return False, 404
        return {'message': 'User deleted'}, 205