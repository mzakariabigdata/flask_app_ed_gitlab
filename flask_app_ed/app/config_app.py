import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# class DevelopmentConfig(Config):
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.sqlite")
#     DATABASE = "app.sqlite"

# class TestingConfig(Config):
#     TESTING = True
#     DATABASE = "testing_db.sqlite"
#     FLASK_PORT = 5001
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "testing_db.sqlite")

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("FLASK_DB_URI") or \
#                             "sqlite:///" + os.path.join(basedir, "globomantics.sqlite")
#     IMAGE_UPLOADS = os.environ.get("FLASK_UPLOADS_FOLDER_URL") or \
#                             os.path.join(basedir, "uploads")