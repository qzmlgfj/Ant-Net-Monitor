import os

SECRET_KEY = "dev"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    os.getcwd(), "instance/backend.sqlite"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
