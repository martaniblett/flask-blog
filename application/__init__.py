# import Flask class from the flask module
from flask import Flask
#import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from os import getenv




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)
# import the ./application/routes.py file
from application import routes


