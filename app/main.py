from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.security.api_key import APIKeyHeader
from app.router import router
from app.utils import validate_secret_key


# Create the FastAPI app instance with metadata
app = FastAPI(
    title="AI Agent for Website Scraping",
    description="A FastAPI application to scrape homepage details and provide industry, company size, and location information.",
    version="1.0.0",
)

# Define the API key header for security
API_KEY_NAME = "Authorization"  # The header name for the Authorization token
api_key_header = APIKeyHeader(name=API_KEY_NAME)

# Custom OpenAPI schema for adding the "Authorize" button in Swagger UI
def custom_openapi():
    """
    Customize the OpenAPI schema to include an APIKey security scheme.
    This enables the "Authorize" button in the Swagger UI.
    """
    if app.openapi_schema:  # Return cached schema if already created
        return app.openapi_schema

    # Generate the OpenAPI schema
    openapi_schema = get_openapi(
        title="AI Agent for Website Scraping",
        version="1.0.0",
        description="A FastAPI application to scrape homepage details and provide industry, company size, and location information.",
        routes=app.routes,
    )

    # Add security schemes to the schema
    openapi_schema["components"]["securitySchemes"] = {
        "APIKeyAuth": {
            "type": "apiKey",
            "name": API_KEY_NAME,  # Matches the header name
            "in": "header",        # Indicates the header usage
        }
    }

    # Apply the security scheme globally
    openapi_schema["security"] = [{"APIKeyAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Apply the custom OpenAPI schema to the app
app.openapi = custom_openapi

# Include the router with a global dependency for authorization
app.include_router(
    router,
    dependencies=[Depends(validate_secret_key)],  # Enforces validation for all routes in the router
    tags=["Scrape Homepage"]                      # Tag for categorizing routes in Swagger UI
)

# Root endpoint for health check
@app.get("/", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify if the API is running.
    """
    return {"message": "API is running successfully"}
