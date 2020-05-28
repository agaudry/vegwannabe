import os
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__, template_folder="../client/dist", static_folder="../client/dist/static")
app.config.from_object('config.' + os.environ['SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

CORS(app, resources={r"/*": {"origins": "*"}})


def get_foods():
    foods = Food.query.all()
    return jsonify(FoodSchema(many=True).dump(foods))


def new_food(data):
    new_food = Food(
        name=data["name"],
        quantity=data["quantity"],
        date=datetime.fromtimestamp(float(data["date"]) / 1000),
        reason=data["reason"],
    )
    db.session.add(new_food)
    db.session.commit()
    return jsonify(FoodSchema().dump(new_food))

def get_food(id):
    this_food = Food.query.get(id)
    if this_food:
        return jsonify(FoodSchema().dump(this_food))
    else:
        return {'code': '404'}

def update_food(id, data):
    this_food = Food.query.get(id)
    if this_food:
        for key, value in data.items():
            setattr(this_food, key, value)
        db.session.commit()
        return jsonify(FoodSchema().dump(this_food))
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

@app.route('/', defaults={'path': ''}, methods=["GET"])
@app.route("/<path>", methods=["GET"])
def home(path):
    return render_template("index.html")


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
