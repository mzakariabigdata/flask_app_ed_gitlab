from flask_restplus import fields
from app.api.restplus import api_v1, api_v2

user_post_def = api_v1.model('User', {
    'name' : fields.String(required = True, description='The name of the user'),
    'password' : fields.String(description='The password of the user'),
    # 'author' : fields.String(description='The author of the book'),
    # 'description' : fields.String(description='The description of the book'),
    # 'date' : fields.Date(description='The date of the book'),  
})

user_get_def = api_v1.model('User', {
    'name' : fields.String(required = True, description='The name of the user'),
    'password' : fields.String(description='The password of the user'),
    'public_id' : fields.String(description='The public_id of the user'),
    'admin' : fields.String(description='The admin of the user'),
    'date' : fields.DateTime(description='The date of the user'),  
})
