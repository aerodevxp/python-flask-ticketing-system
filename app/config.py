import os

class Config:
    SECRET_KEY = os.environ.get("superdupersecretkey")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.dirname(__file__), '..', 'instance', 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#This is what I would do in a real app, but we will always use the DevelopmentConfig since this is not a real website

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}