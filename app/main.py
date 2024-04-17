from flask import Flask, request, Blueprint, jsonify
from stores import get_store

from apis.browse import blueprint as browse_blueprint
from apis.search import blueprint as search_blueprint
from apis.webhook import blueprint as webhook_blueprint

# Flask app
app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive_data():
    # Get data from request
    data = request.get_json()  # Assumes JSON payload

    # Check if data is present
    if not data:
        return "No data received", 400

    # Get store instance
    store = get_store(flask_app=app)

    # Store data
    if not store.store(data):
        return "Error storing data", 500

    return "Data stored successfully!", 201


if __name__ == "__main__":
    import config as app_config

    app.config.from_object(app_config)  # Load config from current module
    app.run(debug=True)
