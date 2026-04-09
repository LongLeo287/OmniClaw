import os
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
SECRET_KEY = os.urandom(32)
FLASK_ENV = 'development'
DEBUG = True
