import os
import sys

# enforce working path
# TODO : see this
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

from core.init import flask_app


# Flask app
if __name__ == "__main__":
    flask_app.run(debug=True)
