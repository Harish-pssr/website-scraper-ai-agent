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
- Python 3.8 or higher
- A valid AI model API key
- A valid authorization token for securing the API

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
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
   MODEL_NAME=ni-1.5-flash
   MODEL_API_KEY=your-model-api-key
   AUTHORIZATION_TOKEN=your-authorization-token
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## **Project Structure**
```plaintext
project/
├── app/
│   ├── __init__.py           # Initializes the app package
│   ├── main.py               # Entry point for the FastAPI application
│   ├── router.py             # Defines API endpoints
│   ├── utils.py              # Helper functions (e.g., validation, agent creation)
│   ├── models.py             # Pydantic models for request/response validation
│   ├── services.py           # Business logic (e.g., scraping and AI analysis)
│   ├── initializer.py        # Initializes shared resources like the AI agent
│   └── config.py             # Configuration and environment variable handling
├── .env                      # Environment variables (not committed to version control)
├── requirements.txt          # List of dependencies
└── README.md                 # Documentation
```

---

## **Usage**

### **Endpoints**
#### **1. Health Check**
- **URL**: `GET /`
- **Description**: Verifies if the API is running.
- **Response**:
  ```json
  {
      "message": "API is running successfully"
  }
  ```

#### **2. Scrape Website**
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

## **Authentication**
The application uses token-based authentication. Set the `Authorization` header as follows:
```plaintext
Authorization: Bearer <your-token>
```
Tokens are validated against the `AUTHORIZATION_TOKEN` environment variable.

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

Thank you for using the **AI Agent for Website Scraping**! We hope it meets your needs and simplifies your workflow. Feel free to reach out with any feedback or suggestions!
