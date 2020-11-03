import os

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:veg101sh@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConf(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = 'prodsecretkey'

class DevConf(Config):
    DEBUG = True
    SECRET_KEY = 'secretkey'

