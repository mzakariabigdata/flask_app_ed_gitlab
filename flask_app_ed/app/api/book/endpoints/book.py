from flask_restplus import Resource, Namespace
from flask import request, jsonify
import requests
from app.api.restplus import api_v1
from app.dba.models import Book
from app.api.book.api_definition import book_def
from app.api.book.domain_logic import create_book
from app.dba.models import db
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import OperationalError

ns_books = Namespace('books', description = "Books operations")

@ns_books.route('/')
class BooksList(Resource):
    
    @api_v1.marshal_with(book_def)
    def get(self):
        """
        returns a list of books
        """
        try:
            res = Book.query.all()
        except NoResultFound as e:
            return None, 404
        return res
    
    @api_v1.expect(book_def)
    def post(self):
        """
        Add a new book to the list
        """
        try:
            print("________zaal___________________________________")
            print(requests)
            f = Book.query.filter(Book.title == request.json.get('title')).one()
        except NoResultFound as e:
            res = create_book(request.json)
        return True, 201

    def put(self):
        """
        Update/Replace a selected book
        """
        return True, 405
    
    # def patch(self):
    #     """
    #     Update/Modify a selected book
    #     """
    #     return True, 405

    def delete(self):
        """
        delete a selected book
        """
        
        try:
            Book.query.delete()
            db.session.commit()
        except OperationalError as e:
            return False, 500
        return True, 200

@ns_books.route('/<string:title>')
class BookItem(Resource):
    
    @api_v1.marshal_with(book_def)
    def get(self, title):
        """
        returns a list of books
        """
        try:
            res = Book.query.filter(Book.title == title).one()
        except NoResultFound as e:
            return False, 404
        return res, 200
    
    @api_v1.expect(book_def)
    def post(self, title):
        """
        Add a new book to the list
        """
        try:
            f = Book.query.filter(Book.title == request.json.get('title')).one()
        except NoResultFound as e:
            res = create_book(request.json)
        return True, 201

    @api_v1.expect(book_def)
    def put(self, title):
        """
        Update/Replace a selected book
        """
        try:
            f = Book.query.filter(Book.title == title).one()
            num_rows_updated = Book.query.filter_by(title=title).update(dict(author=request.json.get('author')))
            print(num_rows_updated)
            db.session.commit()
            # res = update_book(request.json)
        except NoResultFound as e:
            return False, 404
        except OperationalError as e:
            return False, 500
        return True, 200
    
    # def patch(self):
    #     """
    #     Update/Modify a selected book
    #     """
    #     return True, 405

    # @api_v1.expect(book_def)
    def delete(self, title):
        """
        delete a selected book
        """
        try:
            f = Book.query.filter(Book.title == title).one()
            num_rows_updated = Book.query.filter_by(title=title).delete()
            print(num_rows_updated)
            db.session.commit()
            # res = update_book(request.json)
        except NoResultFound as e:
            return False, 404
        return True, 202


# @ns_movies.route('/')
# class HelloWorld(Resource):
    
#     def get(self):
#         return {'hello': 'world'}
    
#     def post(self):
#         return True, 201

#     def put(self):
#         return True, 405
    
#     def patch(self):
#         return True, 405

#     def delete(self):
#         return True, 205

