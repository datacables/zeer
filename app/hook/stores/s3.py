import boto3

class Store:
    def __init__(self, config):
        # Get S3 credentials and bucket name from config
        self.client = boto3.client(
            's3',
            aws_access_key_id=config['aws_access_key_id'],
            aws_secret_access_key=config['aws_secret_access_key'],
        )
        self.bucket_name = config['bucket_name']

    def store(self, data):
        # Implement logic to upload data to S3 bucket
        # ... (e.g., using put_object method)
        # ... (consider error handling)
        return True  # Return success or failure
