from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    edition = db.Column(db.String(120), nullable=True)
    author = db.Column(db.String(120), nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, title, author, edition, date, description):
        self.title = title
        self.edition = edition
        self.author = author
        self.date = date
        self.description = description

    def __repr__(self):
        return '<Book %r>' % self.title

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
    date = db.Column(db.DateTime)

    def __init__(self, public_id, name, password, date, admin):
        self.public_id = public_id
        self.name = name
        self.password = password
        self.date = date
        self.admin = admin

    def __repr__(self):
        return '<User %r>' % self.name