import os
from datetime import timedelta


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:veg101sh@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_URL_RULE = "/auth/login"
    JWT_EXPIRATION_DELTA = timedelta(days=14)
    JWT_AUTH_USERNAME_KEY = "email"


class ProdConf(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = "prodsecretkey"


class DevConf(Config):
    DEBUG = True
    SECRET_KEY = "secretkey"


class TestConf(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:veg101sh@localhost:5432/test"
    SECRET_KEY = "testsecretkey"
