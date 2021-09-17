from flask import Flask, Blueprint, blueprints
from api.restplus import api_v1, api_v2
from api.book.endpoints.book import ns_books
from flask_migrate import Migrate
from dba.models import db
import config
import os

migrate = Migrate()

def initialize_app(flask_app):
    
    blueprint_api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
    blueprint_api_v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

    api_v1.init_app(blueprint_api_v1)
    api_v1.add_namespace(ns_books)
    flask_app.register_blueprint(blueprint_api_v1)

    api_v2.init_app(blueprint_api_v2)
    api_v2.add_namespace(ns_books)
    flask_app.register_blueprint(blueprint_api_v2)
    # ns_movies = api.namespace('movies', description = "Movies operations")
    

    db.init_app(flask_app)

    migrate.init_app(flask_app, db)

    @flask_app.route('/')
    def hello_world_1():
        return 'Hello, Zakaria MORCHID!'

    @flask_app.route('/zak')
    def hello_world_zak9():
        return 'Hello, Zakaria!'

    @flask_app.route('/mor')
    def hello_world_mor9():
        return 'Hello, Zakaria!'
    
def create_app(debug=False, config_env='development'):
    """ Create an application """
    app = Flask(__name__)
    
    app.config.from_object("config.{}Config".format(config_env.capitalize()))
    initialize_app(app)

    return app
    
if __name__ == '__main__':
    app = create_app()

    app.run(debug=True)