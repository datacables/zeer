import os

class Store:
    def __init__(self, config):
        # Get file path from config or define a default
        self.file_path = config.get('file_path', 'data.log')  # Default to 'data.log'

    def store(self, data):
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)  # Create directory if needed

        # Open file in append mode
        with open(self.file_path, 'a') as f:
            # Write data to the file
            f.write(f"{data}\n")  # Add newline character after each entry

        return True