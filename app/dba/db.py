from flask_sqlalchemy import SQLAlchemy
from dba.models import db

import sqlite3

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext

def add(book):
    db.session.add(book)
    db.session.commit()