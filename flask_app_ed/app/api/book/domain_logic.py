from app.dba import db
from app.dba.models import Book
import datetime

def create_book(data):
    title = data.get('title')
    author = data.get('author')
    date = datetime.datetime.now()
    # def __init__(self, title, edition, auther, date, description):

    book = Book(title, author, '', date, '')

    # f = Book.find_one({"title": title})

    db.add(book)

