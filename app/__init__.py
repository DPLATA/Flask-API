from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:password@localhost/flask_challenge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

database = SQLAlchemy(app)
marshmallow = Marshmallow(app)

from app import routes