from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Create instance of flask app
app = Flask(__name__)

# Secret key required to make GET and POST methods
app.config['SECRET_KEY'] = '620c6e14822d650dce105f9d684af954'

# configuring the location of the database. '///' is a relative path from current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create instance of db
db = SQLAlchemy(app)

#
bcrypt = Bcrypt(app)

from flaskblog import routes
