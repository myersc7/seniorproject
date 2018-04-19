import os

class Config(object):
    # change it as needed
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Ytiliga2018**@localhost/senior_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
