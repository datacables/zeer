def zeer_config(flask_app, key):
    # Helper function to get configuration values
    return flask_app.config.get(f"ZEER_{key}", None)

# Default store type (choose from database, redis, file, etc.)
ZEER_DEFAULT_STORE = 'memcached'

# Configuration for each supported store type
ZEER_STORE_CONFIG = {
    'database': {
        # Database connection details as supported by SQLAlchemy
        'engine': 'sqlite:///data.db',  # Replace with your connection string
    },
    'redis': {
        # Redis connection details (host, port, db)
        'host': 'localhost',
        'port': 6379,
        'db': 0,
    },
    'file': {
        # File path for storing data (optional, default provided in stores/file.py)
        'file_path': '../logs/data.log',  # Update with your desired path
    },
    's3': {
        # AWS S3 connection details (access key, secret key, bucket name)
        'aws_access_key_id': 'YOUR_ACCESS', 
        'aws_secret_access_key': 'SECRET_KEY', 
        'bucket_name': 'mybucket',
        'region_name': 'us-east-1',  # Optional: Add region name
    },
    'mongodb': {
        # MongoDB connection details (URI, database name, collection name)
        'mongo_uri': 'mongodb://localhost:27017/',  # Replace with your MongoDB URI
        'database_name': 'mydatabase',
        'collection_name': 'mycollection',
    },
    'memcached': {
        # Memcached connection details (host, port)
        'host': 'localhost',
        'port': 11211,
    },
    'custom': {
        'params': {},
        'provider_class': 'path.to.custom.Store',  # Replace with your custom store class
    }
}
