from flask_restplus import fields
from app.api.restplus import api_v1, api_v2

book_def = api_v1.model('Book', {
    'title' : fields.String(required = True, description='The title of the book'),
    # 'edition' : fields.String(description='The edition of the book'),
    'author' : fields.String(description='The author of the book'),
    # 'description' : fields.String(description='The description of the book'),
    # 'date' : fields.Date(description='The date of the book'),
})
