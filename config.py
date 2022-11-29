import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'non_secret_key')

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///test.db')
