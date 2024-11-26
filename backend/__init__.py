import os
from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY', default='your-secret-key-here')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='sqlite:///urban_planning.db')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)