from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)




app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///bco.sqlite3"
app.config['SECRET_KEY'] = 'sucodeuva'


db = SQLAlchemy(app)

