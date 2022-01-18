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
            print("header")
        print(f"token_required {token} {type(token)}")
        if not token:
            print("token_required 54", token)
            print("a valid token is missing")
            return jsonify({'message': 'a valid token is missing'}), 401
        
        try: 
            print(f"token_required decode {token} {type(token)}")

            data = jwt.decode(token, 'SECRET_KEY', algorithms="HS256")
            print(f"data: {data}")

            current_user = User.query.filter_by(public_id=data['public_id']).first()
            print(f"data: {data['public_id']}")
            print(f"data public_id: {data}")
            print(f"current_user: {current_user}")
        except jwt.exceptions.ExpiredSignatureError:
            return jsonify({'message' : 'Signature has expired !'}), 498
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorator


def deco_test(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        deco = "test deco zak"

        return f(deco, *args, **kwargs)

    return decorator