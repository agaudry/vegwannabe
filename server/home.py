from flask import Blueprint, render_template, request

home_bp = Blueprint("home", __name__, url_prefix="/")


@home_bp.route("/", defaults={"path": ""}, methods=["GET"])
@home_bp.route("/<path>", methods=["GET"])
def home(path):
    return render_template("index.html")
