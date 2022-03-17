
import os

class Config:
    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mike'
    
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG = True


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG = False
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}







