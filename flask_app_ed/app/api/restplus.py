from flask_restplus import Api
from functools import wraps
from flask import request, jsonify
import jwt
from app.dba.models import User

authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'x-access-token'
    }
}

# authorizations = {
#     'Bearer Auth': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'x-access-token'
#     },
# }

api_v1 = Api(version='1.10', title='Book API 1', description='Book management API 1', authorizations=authorizations)

api_v2 = Api(version='2.10', title='Book API 2', description='Book management API 2', authorizations=authorizations)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'a valid token is missing'}), 401
        
        try: 
            data = jwt.decode(token, 'SECRET_KEY', algorithms="HS256")
            current_user = User.query.filter_by(public_id=data['public_id']).first()
            print(f"data: {data['public_id']}")
            print(f"current_user: {current_user}")

        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorator