import os
import json
import unittest
from unittest import mock
# from config import basedir
from app import create_app
from app.dba.models import db
import requests
from unittest.mock import patch

import click

from app.dba.models import Book


# class TestAPI_v1(unittest.TestCase):

#     def setUp(self):
#         self.expected = []
#         # Happens before each test
#         app = create_app(config_env="testing")
#         self.app_ctx = app.app_context()
#         self.app_ctx.push()
#         self.app_test_client = app.test_client()
#         db.create_all()

#     def tearDown(self):
#         # Happens after each test
#         db.session.remove()
#         db.drop_all()

#     def test_get_status_v1(self):
#         res = self.app_test_client.get('/api/v1/books/')
#         self.assertEqual(res.status_code, 200)
    
    # def test_get_type_v1(self):
    #     res = self.app_test_client.get('/api/v1/books/')
    #     self.assertEqual(res.content_type, 'text/html')
    
    # def test_get_data_v1(self):
    #     res = self.app_test_client.get('/api/v1/books/')
    #     self.assertListEqual(self.expected, [])

class TestAPI(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Happens before each test
        app = create_app(config_env="testing")
        cls.app_ctx = app.app_context()
        cls.app_ctx.push()
        cls.app_test_client = app.test_client()
        db.create_all()

    @classmethod
    def tearDown(cls):
        # Happens after each test
        db.session.remove()
        db.drop_all()
        cls.app_ctx.pop()

    def test_get_status(self):
        resp = self.app_test_client.get("/api/v1/books/")
        self.assertEqual(resp.status_code, 200)
    
    # def test_get_data(self):
    #     resp = self.app_test_client.get("/api/v1/books/")
    #     self.assertEqual(resp.content_type, 'application/json')

    # @patch('requests.post')
    # def test_post_book(self, mock_post):
    #     info = {"title": "unittest", "author": "test hello"}
    #     resp = requests.post("/api/v1/books/", data=json.dumps(info), headers={'Content-Type': 'application/json'})
    #     mock_post.assert_called_with("/api/v1/books/", data=json.dumps(info), headers={'Content-Type': 'application/json'})
        # resp = self.app_test_client.get("/api/v1/books/unittest")
        # print(resp.data)
        # self.assertEqual(resp, info)
        # mock_post.assert_called_with("/api/v1/books/flask", data=json.dumps(info), headers={'Content-Type': 'application/json'})


class TestFront(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Happens before each test
        app = create_app(config_env="testing")
        cls.app_ctx = app.app_context()
        cls.app_ctx.push()
        cls.app_test_client = app.test_client()
        db.create_all()

    @classmethod
    def tearDown(cls):
        # Happens after each test
        db.session.remove()
        db.drop_all()
        cls.app_ctx.pop()

    # def test_home_route(self):
    #     resp = self.app_test_client.get("/")
    #     self.assertEqual(resp.status_code, 200)

    # def test_zak_route(self):
    #     resp = self.app_test_client.get("/zak")
    #     self.assertEqual(resp.status_code, 200)

    # def test_mor_route(self):
    #     resp = self.app_test_client.get("/mor")
    #     self.assertEqual(resp.status_code, 200)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(click.__version__ < '9',
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

#     # def test_user_creation(self):
#     #     u = User(username="test", email="test@mail.com")
#     #     u.set_password("password123")
#     #     db.session.add(u)
#     #     db.session.commit()
#     #     u = User.query.filter_by(username="test").first()
#     #     assert u.username == "test"
#     #     assert u.check_password("password123")


if __name__ == "__main__":
    unittest.main()