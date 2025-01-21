from fastapi import APIRouter
from app.models import ScrapingRequest, ScrapingResponse
from app.services import fetch_homepage_content, parse_homepage_content_with_ai

# Initialize the API router
router = APIRouter()

@router.post("/scrape", response_model=ScrapingResponse)
async def scrape_website(request: ScrapingRequest):
    """
    Scrapes the homepage of the given website URL and extracts relevant details.
    Args:
        request (ScrapingRequest): The input request containing the website URL.
    Returns:
        ScrapingResponse: A structured response with extracted information.
    """
    # Fetch the homepage content
    html_content = fetch_homepage_content(request.url)
    
    # Parse the content using AI to extract structured details
    extracted_data = await parse_homepage_content_with_ai(html_content)
    
    # Return the extracted data as a response
    return extracted_data
