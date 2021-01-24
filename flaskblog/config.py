import os


class Config:
    # Secret key required to make GET and POST methods
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # configuring the location of the database. '///' is a relative path from current file
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # configure mail server
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
