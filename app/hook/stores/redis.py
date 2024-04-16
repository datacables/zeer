import redis

class Store:
    def __init__(self, config):
        # Connect to Redis using config
        self.client = redis.Redis(**config)

    def store(self, data):
        # Store data in Redis (using SET command)
        try:
            self.client.set('data', data)  # Replace 'data' with a desired key name
            return True
        except Exception as e:
            print(f"Error storing data in Redis: {e}")
            return False
