import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate
from datetime import datetime


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def home():
    return jsonify("Hello\n")

@app.route('/doitems', methods=['GET'])
def dos():
    dos = DoDontItems.query.filter_by(category='do')
    return jsonify(DoDontItemsSchema(many=True).dump(dos))

@app.route('/dontitems', methods=['GET'])
def donts():
    donts = DoDontItems.query.filter_by(category='dont')
    return jsonify(DoDontItemsSchema(many=True).dump(donts))

@app.route('/do', methods=['GET', 'POST'])
def do():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data = request.get_json()
        do_item = db.session.query(Dos).filter_by(parent_name=data['name'], end_at=None)
        if do_item.first():
            do_item.update({'end_at': datetime.fromtimestamp(data['datetime']/1000)})
            print('updated doitem')
        else:
            new_do_item = Dos(
                paent_name=data['name'],
                begin_at=datetime.fromtimestamp(data['datetime']/1000),
                end_at=None
                )
            db.session.add(new_do_item)
            print('created doitem')
        db.session.commit()
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
