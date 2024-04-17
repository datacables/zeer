from flask import Blueprint, request
from stores import BaseStore

from flask import request, jsonify

blueprint = Blueprint("webhook", __name__)

from models.webhook import Webhook


@blueprint.route("/<oid>/<token>/", methods=["POST"])
def main(oid, token):

    # quickly verify the access using oid and token
    # if not valid, return 401
    Webhook.query.filter_by(oid=oid, token=token).first()

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


@blueprint.route("/register/", methods=["POST"])
def register():
    # Get email and target_bucket from request
    data = request.get_json()
    email = data.get("email").strip()

    def is_valid_email(email):
        if email is None or email == "" or len(email) > 100:
            return False
        if "@" not in email:
            return False
        return True

    # Validate email format (basic check)
    # TODO Email validation
    if not is_valid_email(email):
        return jsonify({"message": "Invalid email format"}), 400

    hook_bucket = Webhook.create(email=email)
    hook_url = f"http://localhost:5000/webhook/{hook_bucket.oid}/{hook_bucket.token}"

    # Set cache for target_bucket with unique_url
    #     cache.set(target_bucket, unique_url)

    # Return success response with unique URL
    return jsonify(
        {
            "hook_url": hook_url,
            "hook_bucket": hook_bucket.oid,
            "hook_token": hook_bucket.token,
            "hook_email": email,
            "message": "Webhook registered successfully!",
        }
    )
