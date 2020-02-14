import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

CORS(app, resources={r'/*': {'origins': '*'}})

class Do(db.Model):
    __tablename__ = 'do'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    begin_at = db.Column(db.Datetime)
    end_at = db.Column(db.Datetime)

@app.route('/', methods=['GET'])
def home():
    return jsonify("Hello\n")

@app.route('/do', methods=['GET'])
def dos():
    return jsonify("Do's")

@app.route('/dont', methods=['GET'])
def donts():
    return jsonify("Dont's")


if __name__ == '__main__':
    app.run()
