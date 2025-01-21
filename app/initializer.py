import logging
from app.utils import create_ai_agent
from app.config import MODEL_NAME, MODEL_API_KEY


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

try:
    # Attempt to initialize the AI agent
    agent = create_ai_agent(model_name=MODEL_NAME, api_key=MODEL_API_KEY)
    logging.info("AI Agent initialized successfully")
except Exception as e:
    # Log the error and raise it to prevent the application from starting
    logging.critical(f"Failed to initialize AI Agent: {e}", exc_info=True)
    raise RuntimeError("AI Agent initialization failed. Check the logs for more details.") from e
