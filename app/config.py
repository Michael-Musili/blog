
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:access@localhost/dbblogapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mike'
    
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:access@localhost/dbblogapp'
    DEBUG = True


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}






