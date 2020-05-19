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
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

CORS(app, resources={r"/*": {"origins": "*"}})


def get_foods():
    foods = Food.query.all()
    return jsonify(FoodSchema(many=True).dump(foods).data)


def new_food(data):
    print(data)
    new_food = Food(
        name=data["name"],
        quantity=data["quantity"],
        date=datetime.fromtimestamp(float(data["date"]) / 1000),
        reason=data["reason"],
    )
    db.session.add(new_food)
    db.session.commit()
    validate_new_food = (
        db.session.query(Food)
        .filter_by(
            name=data["name"], date=datetime.fromtimestamp(float(data["date"]) / 1000)
        )
        .first()
    )
    return jsonify(FoodSchema().dump(validate_new_food).data)

def get_food(id):
    this_food = Food.query.get(id)
    if this_food:
        return jsonify(FoodSchema().dump(this_food).data)
    else:
        return {'code': '404'}

def update_food(id, data):
    this_food = Food.query.get(id)
    if this_food:
        for key, value in data.items():
            setattr(this_food, key, value)
        db.session.commit()
        this_food = Food.query.get(id)
        return jsonify(FoodSchema().dump(this_food).data)
    else:
        return {'code': '404'}

def delete_food(id):
    this_food = Food.query.get(id)
    if this_food:
        db.session.delete(this_food)
        db.session.commit()
        return {'code': '204'}
    else:
        return {'code': '404'}

@app.route("/", methods=["GET"])
def home():
    return jsonify("Hello\n")


@app.route("/foods", methods=["GET", "POST"])
def foods():
    if request.method == "GET":
        return get_foods()
    elif request.method == "POST":
        data = request.get_json()
        return new_food(data)


@app.route('/food/<id>', methods=['GET', 'PUT', 'DELETE'])
def food(id):
    if request.method == 'GET':
        return get_food(id)
    elif request.method == 'PUT':
        data = request.get_json()
        return update_food(id, data)
    elif request.method == 'DELETE':
        return delete_food(id)


if __name__ == "__main__":
    app.run()
