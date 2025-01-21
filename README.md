# **AI Agent for Website Scraping**

## **Overview**
This is a FastAPI application that uses an AI-based agent to scrape website homepage content and extract structured information such as:
- **Industry**: The industry the company belongs to.
- **Company Size**: The size of the company (e.g., small, medium, large).
- **Location**: The company's location (if available).

The project uses modern tools like **Pydantic AI**, **BeautifulSoup**, and FastAPI's built-in features for robust and scalable web scraping.

---

## **Features**
- Secure API endpoints with token-based authentication via the `Authorization` header.
- AI-based content analysis using a predefined AI model.
- Automatic handling of errors such as invalid URLs, unsupported media types, or missing information.
- OpenAPI documentation available at `/docs` with an "Authorize" button for easy token authentication.
- Modular and maintainable code structure.

---

## **Setup**

### **Prerequisites**
- A valid AI model API key
- A valid authorization token for securing the API

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Harish-pssr/website-scraper-ai-agent.git
   cd website-scraper-ai-agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in a `.env` file (optional but recommended):
   ```
   MODEL_NAME=<your_AI_model_name>
   MODEL_API_KEY=<your-model-api-key>
   AUTHORIZATION_TOKEN=<your-authorization-token>
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## **Project Structure**
```plaintext
website-scraper-ai-agent/
├── app/
│   ├── __init__.py           # Initializes the app package
│   ├── main.py               # Entry point for the FastAPI application
│   ├── router.py             # Defines API endpoints
│   ├── utils.py              # Helper functions (e.g., validation, agent creation)
│   ├── models.py             # Pydantic models for request/response validation
│   ├── services.py           # Business logic (e.g., scraping and AI analysis)
│   ├── initializer.py        # Initializes shared resources like the AI agent
│   └── config.py             # Configuration and environment variable handling
├── requirements.txt          # List of dependencies
└── README.md                 # Documentation
```

---

## **Endpoints**
### **1. Health Check**
- **URL**: `GET /`
- **Description**: Verifies if the API is running.
- **Response**:
  ```json
  {
      "message": "API is running successfully"
  }
  ```

### **2. Scrape Website**
- **URL**: `POST /scrape`
- **Description**: Scrapes the homepage content of the given URL and extracts structured information.
- **Request Body**:
  ```json
  {
      "url": "https://example.com"
  }
  ```
- **Response**:
  ```json
  {
      "industry": "Technology",
      "company_size": "Medium",
      "location": "San Francisco, CA"
  }
  ```
- **Authentication**:
  - Requires the `Authorization` header with the format: `Bearer <your-token>`.

---

## Model Information:
This project uses the **Gemini Flash 1.5** model (`gemini-flash-1.5`) for AI-based website content analysis.

---

## Environment Variables:
The application relies on the following environment variables, which should be set up in your deployment environment:

1. **`MODEL_NAME`**:
   - **Purpose**: Specifies the AI model to be used.
   - **Example Value**: `gemini-flash-1.5`

2. **`MODEL_API_KEY`**:
   - **Purpose**: API key for authenticating with the model provider.
   - **Example Value**: `your-model-api-key`

3. **`AUTHORIZATION_TOKEN`**:
   - **Purpose**: Token used for securing API access. It is required in the `Authorization` header for all secure endpoints.
   - **Example Format**:
     ```
     Bearer your-authorization-token
     ```

---

## **Logging**
- The application uses Python's `logging` module for structured logs.
- Logs are printed to the console and include details about errors, status codes, and agent execution.

---

## **Error Handling**
- **400 Bad Request**: Invalid URLs or request errors.
- **401 Unauthorized**: Missing or invalid `Authorization` token.
- **415 Unsupported Media Type**: URL does not point to an HTML page.
- **500 Internal Server Error**: Issues during HTML parsing or AI analysis.

---

## **Testing**
To test the API:
1. Use **Postman** or **Swagger UI** (`/docs`).
2. Include the `Authorization` header for secure endpoints.
3. Send a `POST` request to `/scrape` with the website URL.

---

Thank you for using the **AI Agent for Website Scraping**! We hope it meets your needs and simplifies your workflow. Feel free to reach out with any feedback or suggestions!
