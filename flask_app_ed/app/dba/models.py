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