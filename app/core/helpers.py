from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request


def get_request_data():
    # Helper function to get request data
    if request.is_json:
        return request.get_json()
    else:
        return request.form.to_dict()
