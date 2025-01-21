import requests
import json
import logging
from fastapi import HTTPException
from bs4 import BeautifulSoup
from app.models import LLMContext, ScrapingResponse
from app.initializer import agent

def fetch_homepage_content(url: str) -> str:
    """
    Fetches the HTML content of the homepage from the given URL.
    Args:
        url (str): The website URL to fetch content from.
    Returns:
        str: The HTML content of the homepage.
    """
    try:
        response = requests.get(url, timeout=10)

        # Check for no content
        if response.status_code == 204:
            logging.warning(f"Received 204 No Content response for URL: {url}")
            raise HTTPException(status_code=204, detail="No content available at the URL.")

        # Validate the Content-Type header
        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            logging.error(f"Unsupported media type: {content_type} for URL: {url}. Expected 'text/html'.")
            raise HTTPException(
                status_code=415,
                detail=f"Unsupported media type: {content_type}. The URL must point to an HTML page."
            )

        # Raise exceptions for HTTP errors
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"RequestException occurred while fetching URL: {url}. Error details: {e}")
        raise HTTPException(status_code=400, detail=f"Error fetching URL.")


def process_response_object(response_object):
    """
    Processes the response object to ensure all fields are present and properly formatted.
    Args:
        response_object: The response object containing extracted fields.
    Returns:
        The updated response object with validated and processed fields.
    """
    fields_to_check = ["industry", "company_size", "location"]

    for field in fields_to_check:
        value = getattr(response_object, field, None)
        if not value:  # Replace missing or empty fields
            setattr(response_object, field, "Not Mentioned")
        elif isinstance(value, str):
            # Escape non-ASCII characters
            setattr(response_object, field, json.loads(json.dumps(value, ensure_ascii=True)))

    return response_object


async def parse_homepage_content_with_ai(html_content: str) -> ScrapingResponse:
    """
    Parses the homepage content using an AI agent to extract structured information.
    Args:
        html_content (str): The raw HTML content of the homepage.
    Returns:
        ScrapingResponse: Extracted information including industry, company size, and location.
    """
    try:
        # Extract visible text from the HTML content
        soup = BeautifulSoup(html_content, "html.parser")
        scraped_text = soup.get_text(separator="\n", strip=True)
    except Exception as e:
        logging.error(f"Parsing failed for the provided HTML content. Error details: {e}")
        raise HTTPException(status_code=500, detail=f"HTML parsing failed")

    # Use the AI agent to analyze the scraped text
    try:
        response = await agent.run(
            user_prompt=(
                "Extract industry (type of), company size (small, medium or large) if mentioned, "
                "location where the company exists if mentioned"
            ),
            deps=LLMContext(scraped_text=scraped_text),
        )
        response_data = process_response_object(response.data)
        return response_data
    except Exception as e:
        logging.error(f"Agent execution failed during content processing. Error details: {e}")
        raise HTTPException(status_code=500, detail=f"AI extraction failed")