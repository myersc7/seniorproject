import os

class Config(object):
    # change it as needed
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Ytiliga2018**@ec2-54-157-47-97.compute-1.amazonaws.com/senior_project2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
