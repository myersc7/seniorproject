import os


class Config(object):
    # change it as needed
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Ytiliga2018**@ec2-54-157-47-97.compute-1.amazonaws.com/senior_project'
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/senior_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
