from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#breakpoint()
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sqlite.db'
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from app import views
from app import models
with app.app_context():
    db.init_app(app)
    db.create_all() 

