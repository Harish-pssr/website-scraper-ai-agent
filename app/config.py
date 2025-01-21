import os

# Load environment variables with default fallback values
MODEL_NAME = os.getenv("MODEL_NAME", "")  # model name
MODEL_API_KEY = os.getenv("MODEL_API_KEY", "")  # API key
AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN", "")  # authorization token
