from os import environ, path
import os

class Config:
    """Set Flask config variables."""

    #Configuracao geral
    SECRET_KEY = os.urandom(32)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    #Db
    MONGO_URI = 'mongodb://mongo/sensdb'
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    
