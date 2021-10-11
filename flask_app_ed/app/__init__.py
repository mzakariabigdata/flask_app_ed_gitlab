from flask import Flask, Blueprint, blueprints, request
from app.api.restplus import api_v1, api_v2
from app.api.book.endpoints.book import ns_books
from app.api.user.endpoints.user import ns_users
from app.dba.models import db
from app import config_app
import os

# Extention
from flask_session import Session
from flask_migrate import Migrate
import redis
from app.ext.cache_ext import cache

migrate = Migrate()
session = Session()

def initialize_app(flask_app):
    
    blueprint_api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
    blueprint_api_v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

    api_v1.init_app(blueprint_api_v1)
    api_v1.add_namespace(ns_books)
    api_v1.add_namespace(ns_users)
    flask_app.register_blueprint(blueprint_api_v1)

    api_v2.init_app(blueprint_api_v2)
    api_v2.add_namespace(ns_users)
    api_v2.add_namespace(ns_books)
    flask_app.register_blueprint(blueprint_api_v2)
    # ns_movies = api.namespace('movies', description = "Movies operations")
    

    db.init_app(flask_app)
    session.init_app(flask_app)
    cache.init_app(flask_app)
    migrate.init_app(flask_app, db)

    @flask_app.route('/')
    def hello_world_1():
        return 'Hello, Zakaria MORCHID!'

    @flask_app.route('/login')
    def login():
        return 'Login'

    @flask_app.route('/mor')
    def hello_world_mor9():
        return 'Hello, Zakaria!'

def configure_app(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
    app.config['DATABASE'] = "app.sqlite"
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    # app.config['SESSION_REDIS'] = '127.0.0.1:6379'
    app.config['SESSION_REDIS'] = redis.Redis("127.0.0.1")
    app.config['SESSION_TYPE'] = 'redis'
    app.config['CACHE_TYPE'] = 'RedisCache'
    app.config['CACHE_REDIS_URL'] = 'redis://127.0.0.1:6379/2'

def create_app(debug=False, config_env='development'):
    """ Create an application """
    flask_app = Flask(__name__)
    
    # flask_app.config.from_object("config_app.{}config".format(config_env.capitalize()))

    configure_app(flask_app)
    initialize_app(flask_app)

    return flask_app
    
if __name__ == '__main__':
    app = create_app()

    app.run(debug=True)