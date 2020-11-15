from flask import Blueprint, jsonify, render_template, request
from flask_jwt import JWT, jwt_required, current_identity
from datetime import datetime
from server.models import db
from server.models import Food, FoodSchema


foods_bp = Blueprint("foods", __name__, url_prefix="/foods")


def get_foods():
    all_foods = Food.query.all()
    return jsonify(FoodSchema(many=True).dump(all_foods))


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
        return {"code": "404"}


def update_food(id, data):
    this_food = Food.query.get(id)
    if this_food:
        for key, value in data.items():
            setattr(this_food, key, value)
        db.session.commit()
        return jsonify(FoodSchema().dump(this_food))
    else:
        return {"code": "404"}


def delete_food(id):
    this_food = Food.query.get(id)
    if this_food:
        db.session.delete(this_food)
        db.session.commit()
        return {"code": "204"}
    else:
        return {"code": "404"}


@foods_bp.route("/", methods=["GET", "POST"])
@jwt_required()
def list_foods():
    if request.method == "GET":
        print("this is {}'s foods!".format(current_identity.username))
        return get_foods()
    elif request.method == "POST":
        data = request.get_json()
        return new_food(data)


@foods_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def food(id):
    if request.method == "GET":
        return get_food(id)
    elif request.method == "PUT":
        data = request.get_json()
        return update_food(id, data)
    elif request.method == "DELETE":
        return delete_food(id)
