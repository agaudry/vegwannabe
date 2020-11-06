from flask import Blueprint, render_template, request
from flask_jwt import JWT, jwt_required, current_identity
from server.models import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/protected")
@jwt_required()
def protected():
    return "%s" % current_identity


# @auth_bp.route('/login')
# @jwt_required()
# def protected():
#     return '%s' % current_identity
