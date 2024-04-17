from flask import Blueprint, request
from stores import BaseStore

blueprint = Blueprint("webhook", __name__)


@blueprint.route("/", methods=["POST"])
def main():
    # Get data from request
    data = request.get_json()  # Assumes JSON payload

    # Check if data is present
    if not data:
        return "No data received", 400

    # Get store instance
    store = BaseStore.get_provider()

    # Store data
    if not store.store(data):
        return "Error storing data", 500

    return "Data stored successfully!", 201
