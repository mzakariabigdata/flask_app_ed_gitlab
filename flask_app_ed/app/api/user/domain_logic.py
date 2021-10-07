from app.dba import db
from app.dba.models import User
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime

def create_user(data):
    hash_password = generate_password_hash(data['password'], method='sha256')
    date_new_user = datetime.datetime.now()
    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hash_password, admin=False, date=date_new_user)

    db.add(new_user)
