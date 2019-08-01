from flask import jsonify, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return jsonify({})
