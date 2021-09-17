import os
import psutil 
import sqlite3
import tempfile
import requests
import pytest
import sqlite3 as mdb
from flask import current_app
from dba.models import Book

from app import create_app
from dba.models import db


url = 'http://127.0.0.1:5000/api/v1/books/'
url_unittest = 'http://127.0.0.1:5000/api/v1/books/unittest'
app_json = 'application/json'
headers = {'Content-Type': app_json, 'accept': app_json}

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(config_env="testing")
    
    with app.app_context():
        with app.test_client() as client:
            # Book.query.delete()
            # db.session.commit()
            db.create_all()
            # if "db" not in g:
            
            # db = sqlite3.connect(app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
            # db.row_factory = sqlite3.Row
            # with app.open_resource("schema.sql") as f:
            #     db.executescript(f.read().decode('utf8'))
            yield client

    os.close(db_fd)
    os.unlink(db_path)

# def test_empty_from_db(client):
#     res = Book.query.all()
#     assert 200 == res

# def test_get_book(client):
#     # Make a tes call to /books/1
#     response = client.get("/api/v1/books")

#     # Validate the response
#     assert response.status_code == 200
#     # assert response.json == {
#     #     "id": 1, 
#     #     "title": "Python for Dummies"
#     # }




def chk_conn(conn):
     try:
        conn.cursor()
        return True
     except Exception as ex:
        return False

def test_is_open():
    myconn = mdb.connect('app.sqlite')
    res = chk_conn(myconn)
    assert True == res

def test_root_front(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b'Hello, Zakaria MORCHID!' in rv.data

def test_root_front(client):
    """Start with a blank database."""
    rv = client.get('/zak')
    assert b'Hello, Zakaria!' in rv.data

# def test_empty_db_status_pytest(client):
#     """Start with a blank database."""
#     resp = client.get('http://127.0.0.1:5001/api/v1/books/')
#     assert 200 == resp.status_code

def test_empty_db_status(client):
    """Start with a blank database."""
    resp = requests.get(url)
    assert 200 == resp.status_code

def test_empty_db_type(client):
    """Start with a blank database."""
    # rv = client.get('/api/v1/books/')
    resp = requests.get(url)
    assert resp.headers['content-type'] == 'application/json'


# def test_empty_db_data(client):
#     """Start with a blank database."""
#     # rv = client.get('/api/v1/books/')
#     url = 'http://127.0.0.1:5000/api/v1/books/'
#     resp = requests.get(url)
#     assert [] == resp.json()

def test_post_book_status(client):
    book = {'title': 'unittest', 'author': 'test hello word'}
    response = requests.post(url, json=book, headers=headers)
    assert 201 == response.status_code

def test_get_book_response_status(client):
    resp = requests.get(url_unittest)
    assert 200 == resp.status_code

def test_get_book_response_data(client):
    book = {'title': 'unittest', 'author': 'test hello word'}
    resp = requests.get(url_unittest)
    assert resp.json() == book

def test_put_book_response_status(client):
    book = {'author': 'unittest zak 54'}
    resp = requests.put(url_unittest, json=book, headers=headers)
    assert 200 == resp.status_code

# def test_patch_book_response_status(client):
#     url = 'http://127.0.0.1:5000/api/v1/books/unittest'
#     book = {'author': 'unittest zak 54'}
#     headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
#     resp = requests.patch(url, json=book, headers=headers)
#     assert 200 == resp.status_code

def test_put_book_response_data(client):
    book = {'title': 'unittest', 'author': 'unittest zak 54'}
    resp = requests.get(url_unittest)
    assert book == resp.json()

def test_delete_book_response_status(client):
    resp = requests.delete(url_unittest)
    assert resp.status_code == 202

def test_delete_book_response_data(client):
    resp = requests.get(url_unittest)
    assert 404 == resp.status_code

@pytest.mark.parametrize("num, result", [(1, 11), (2, 22), (3,44)])
def test_calculate(num, result):
    assert 11 * num == result