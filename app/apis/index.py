from flask import Blueprint, jsonify, request

blueprint = Blueprint("default", __name__)


@blueprint.route("/", methods=["GET"])
def index():
    return jsonify(
        {
            "message": "The Webhook Service is running. Please refer to docs for more information."
        }
    )
