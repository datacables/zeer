from pymongo import MongoClient

class Store:
    def __init__(self, config):
        # Get MongoDB connection details from config
        self.client = MongoClient(config['mongo_uri'])
        self.db = self.client[config['database_name']]
        self.collection = self.db[config['collection_name']]

    def store(self, data):
        # Insert data into MongoDB collection
        self.collection.insert_one({'data': data})
        return True  # Return success or failure (consider error handling)
