from urllib.parse import urlparse

from flask import Blueprint, current_app, jsonify, request, url_for
from flask_swagger import swagger, _parse_docstring, _sanitize

from ..__meta__ import __api_name__, __version__

swagger_bp = Blueprint("swagger", __name__)


@swagger_bp.route("/spec")
def spec():
    swag = swagger(current_app)

    swag["info"]["version"] = __version__
    swag["info"]["title"] = __api_name__
    swag["host"] = request.host
    swag["basePath"] = url_for("main.index").rstrip("/")

    o = urlparse(url_for("main.index", _external=True))

    swag["schemes"] = [o.scheme]
    swag["securityDefinitions"] = {
        "USER_ID": {
            "type": "apiKey",
            "name": "USER-ID",
            "in": "header",
            "description": "HTTP Header 에 USER-ID 지정",
        }
    }

    swag["definitions"] = _swagger_definition

    return jsonify(swag)


_swagger_definition = {}


def swagger_definition(class_):
    name, _, adict = _parse_docstring(class_, _sanitize, None)
    _swagger_definition[name] = adict

    return class_


from app.serializers import *  # noqa
from app.request_objects.comment import *  # noqa
from app.request_objects.post import *  # noqa
