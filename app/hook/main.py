from flask import Flask, request
from importlib import import_module

# Flask app
app = Flask(__name__)


def get_store():
    store_type = app.config.get('STORE_TYPE', DEFAULT_STORE)
    store_module = import_module(f'stores.{store_type}')
    return store_module.Store(app.config.get(f'{store_type.upper()}_CONFIG'))


@app.route('/', methods=['POST'])
def receive_data():
    # Get data from request
    data = request.get_json()  # Assumes JSON payload

    # Check if data is present
    if not data:
        return 'No data received', 400

    # Get store instance
    store = get_store()

    # Store data
    if not store.store(data):
        return 'Error storing data', 500

    return 'Data stored successfully!', 201


if __name__ == '__main__':
    app.config.from_object(__name__)  # Load config from current module
    app.run(debug=True)
