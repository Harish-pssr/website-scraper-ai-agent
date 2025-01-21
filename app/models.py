from pydantic import BaseModel, HttpUrl

class ScrapingRequest(BaseModel):
    """
    Represents the input data for the scraping API.
    Ensures the URL is a valid and properly formatted HTTP/HTTPS URL.
    """
    url: HttpUrl  # Validates that the input is a proper URL


class ScrapingResponse(BaseModel):
    """
    Represents the structured output returned by the scraping API.
    Includes fields extracted from the website's homepage.
    """
    industry: str  # The industry of the website
    company_size: str  # The size of the company (e.g., small, medium, large)
    location: str  # The location of the company (if available)


class LLMContext(BaseModel):
    """
    Context passed to the LLM for interpretation and extraction.
    Contains the scraped text from the website's homepage.
    """
    scraped_text: str  # Text content extracted from the homepage
