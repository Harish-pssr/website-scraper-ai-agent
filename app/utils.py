import logging
from fastapi import HTTPException, Header
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.gemini import GeminiModel
from app.models import ScrapingResponse, LLMContext
from app.config import AUTHORIZATION_TOKEN


def validate_secret_key(authorization: str = Header(None)):
    """
    Validates the Authorization header with a predefined secret key.
    """
    if not authorization:
        logging.warning("Authorization header is missing in the request.")
        raise HTTPException(status_code=401, detail="Authorization header is missing.")
    if authorization != f"Bearer {AUTHORIZATION_TOKEN}":
        logging.error("Invalid authorization token provided.")
        raise HTTPException(status_code=401, detail="Invalid secret key.")

def create_ai_agent(model_name: str, api_key: str) -> Agent:
    """
    Creates an AI Agent for analyzing website homepage content.
    Args:
        model_name (str): The name of the AI model to use.
        api_key (str): The API key for authenticating with the AI model provider.
    Returns:
        Agent: An initialized Agent instance ready to process website scraping tasks.
    """
    # Initialize the AI Agent with the specified model and API key
    agent = Agent(
        model=GeminiModel(model_name=model_name, api_key=api_key),
        result_type=ScrapingResponse,  # Expected structured output
        deps_type=LLMContext,         # Input context structure
        system_prompt=(
            "You are an intelligent website analysis and scraping agent. "
            "Analyze the provided homepage content carefully and extract structured information such as "
            "industry, company size, and location of the company."
        ),
    )

    # Adds the context dependency to the agent's system prompt
    @agent.system_prompt
    async def add_scraped_text(ctx: RunContext[LLMContext]) -> str:
        """
        Modifies the system prompt by including the scraped text context.
        """
        return f"Company details: {ctx.deps}"

    return agent
