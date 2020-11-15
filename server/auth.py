from flask import Blueprint, render_template, request
from flask_jwt import JWT, jwt_required, current_identity
from server.models import db
from server.models import User, UserSchema


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/protected")
@jwt_required()
def protected():
    return "%s" % current_identity

@auth_bp.route("/user")
@jwt_required()
def user():
    return current_identity.username

@auth_bp.route('/signup', methods=["POST"])
def signup():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return {}
