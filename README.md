# ⚡ FastAPI Practice — REST API Fundamentals

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">

  <img src="https://img.shields.io/badge/FastAPI-REST_API-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">

  <img src="https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge" alt="Pydantic">

  <img src="https://img.shields.io/badge/Uvicorn-ASGI_Server-4051B5?style=for-the-badge" alt="Uvicorn">

  <img src="https://img.shields.io/badge/Postman-API_Testing-FF6C37?style=for-the-badge&logo=postman&logoColor=white" alt="Postman">

</p>

<p align="center">

  **A practical FastAPI project focused on REST API fundamentals, CRUD operations, request validation, response models, and error handling.**

</p>

---

## 📌 About the Project

**FASTAPI PRACTICE** is a Python project built to understand how REST APIs work using FastAPI.

The project implements a Product API that supports creating, retrieving, updating, partially updating, and deleting products.

The primary goal is to understand the complete API request-to-response flow rather than simply writing endpoint code.

The learning process follows:

```text
Understand the Concept
        ↓
Create the FastAPI Application
        ↓
Define Pydantic Models
        ↓
Implement CRUD Endpoints
        ↓
Handle Status Codes and Errors
        ↓
Explore Swagger UI
        ↓
Test APIs Using Postman
        ↓
Understand the Complete Flow
```

## 🎯 Project Objectives

- Understand FastAPI and its application structure.
- Learn how HTTP methods work in REST APIs.
- Implement complete CRUD operations.
- Understand path parameters and request bodies.
- Validate incoming data using Pydantic.
- Define response structures using response models.
- Handle missing resources using `HTTPException`.
- Use appropriate HTTP status codes.
- Explore automatically generated OpenAPI documentation.
- Test API endpoints using Swagger UI and Postman.
- Understand how a request becomes a response.

---

## 🏗️ Architecture

The project uses a simple architecture with in-memory product storage.

```text
              ┌─────────────────────┐
              │   Client / Postman  │
              └──────────┬──────────┘
                         │
                         │ HTTP Request
                         ▼
              ┌─────────────────────┐
              │       Uvicorn        │
              │    ASGI Server       │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │       FastAPI        │
              │    Route Matching    │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Pydantic Validation  │
              │  Request / Response  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Endpoint Logic     │
              │   CRUD Operations    │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Python List        │
              │  Product Data        │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   JSON Response      │
              │ Status Code + Body   │
              └─────────────────────┘
```

### Core Principle

> **FastAPI handles API routing and request processing, Pydantic validates structured data, and the endpoint logic performs operations on the product list.**

The project currently uses an in-memory Python list rather than a database.

---

## 🚀 Features Implemented

The project implements six API endpoints covering all the main CRUD operations.

| Operation | HTTP Method | Endpoint | Purpose |
|---|---|---|---|
| Read all | GET | `/products` | Retrieve all products |
| Create | POST | `/products` | Create a new product |
| Read one | GET | `/products/{product_id}` | Retrieve a product by ID |
| Update | PUT | `/products/{product_id}` | Update the complete product data |
| Partial update | PATCH | `/products/{product_id}` | Update selected product fields |
| Delete | DELETE | `/products/{product_id}` | Delete a product |

---

## 📦 Product Data Model

The project uses Pydantic models to define product data.

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
```

A product contains:

- `name`: Product name as a string.
- `price`: Product price as a floating-point number.

The application initially stores three products:

```python
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 1000},
    {"id": 3, "name": "KeyBoard", "price": 2000}
]
```

Additional Pydantic models define response structures and support partial updates.

---

## 📋 CRUD Operations

### 1. GET — Retrieve All Products

```http
GET /products
```

Returns the list of products.

Expected status code: `200 OK`

### 2. POST — Create a Product

```http
POST /products
```

Example request body:

```json
{
  "name": "Monitor",
  "price": 12000
}
```

Creates a product and returns its details.

Expected status code: `201 Created`

### 3. GET — Retrieve a Product by ID

```http
GET /products/1
```

Returns the product whose ID matches the path parameter.

Expected status code: `200 OK`

If the product does not exist, the API returns `404 Not Found`.

### 4. PUT — Update a Complete Product

```http
PUT /products/1
```

Example request body:

```json
{
  "name": "Gaming Laptop",
  "price": 75000
}
```

Updates both the name and price.

Expected status code: `200 OK`

### 5. PATCH — Update Selected Fields

```http
PATCH /products/1
```

Example request body:

```json
{
  "price": 65000
}
```

Updates only the supplied, non-null field in the current implementation.

Expected status code: `200 OK`

### 6. DELETE — Delete a Product

```http
DELETE /products/1
```

Removes the product and returns the deleted product details.

Expected status code: `200 OK`

---

## 🔄 Complete Request-to-Response Flow

Every API request follows this general process:

```text
1. Client Sends HTTP Request
             ↓
2. Uvicorn Receives the Request
             ↓
3. FastAPI Matches the Route
             ↓
4. Path Parameters / Request Body Validated
             ↓
5. Endpoint Executes Business Logic
             ↓
6. Product List Is Read or Modified
             ↓
7. Response Model Processes Output
   (When Configured)
             ↓
8. FastAPI Serializes the Response
             ↓
9. Client Receives JSON + Status Code
```

If the requested product does not exist, the endpoint raises `HTTPException` and FastAPI returns the corresponding error response.

This flow is the central concept behind the project.

---

## 🧠 Important Concepts Learned

### FastAPI Fundamentals

- Creating a FastAPI application using `FastAPI()`.
- Registering endpoints with decorators.
- Running the application using Uvicorn.
- Understanding the role of the ASGI server.

### Request Handling

- HTTP methods and endpoints.
- Path parameters.
- JSON request bodies.
- Pydantic request models.
- Required and optional fields.

### Response Handling

- Response models.
- JSON serialization.
- HTTP status codes.
- `HTTPException`.
- Request validation errors.
- `404 Not Found` handling.

### API Testing

- Swagger UI.
- OpenAPI documentation.
- Postman requests.
- Testing successful responses.
- Testing invalid inputs and missing resources.

---

## 🌐 API Documentation

FastAPI automatically generates interactive API documentation.

| URL | Purpose |
|---|---|
| `http://127.0.0.1:8000/docs` | Swagger UI |
| `http://127.0.0.1:8000/redoc` | ReDoc documentation |
| `http://127.0.0.1:8000/openapi.json` | OpenAPI schema |

Swagger UI allows you to inspect endpoints, enter request data, execute requests, and examine the responses.

Postman provides another way to send HTTP requests and verify status codes and response bodies.

---

## 🛠️ Technology Stack

### Backend

- **Python** — Programming language.
- **FastAPI** — API framework.
- **Pydantic** — Data validation and response schemas.
- **Uvicorn** — ASGI server.

### Testing and Documentation

- **Swagger UI** — Interactive API testing.
- **OpenAPI** — API description standard.
- **Postman** — Manual API testing.

### Development Tools

- **VS Code** — Code editor.
- **Git** — Version control.
- **GitHub** — Source code hosting.

---

## ⚙️ Setup and Installation

### 1. Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone <your-repository-url>
cd "FASTAPI PRACTICE"
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, install the required packages:

```bash
pip install fastapi uvicorn
```

### 4. Start the Application

```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI

Visit:

```text
http://127.0.0.1:8000/docs
```

You can now test the implemented endpoints.

---

## 📁 Project Structure

```text
FASTAPI PRACTICE/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── docs/
    ├── 01-project-overview.md
    ├── 02-fastapi-fundamentals-setup.md
    ├── 03-crud-end-to-end.md
    ├── 04-response-request.md
    └── 05-swagger-postman-testing.md
```

---

## 📚 Documentation

The project documentation is divided into five focused files.

| Document | Description |
|---|---|
| [Project Overview](docs/01-project-overview.md) | Project purpose, objectives, features, and scope |
| [FastAPI Fundamentals and Setup](docs/02-fastapi-fundamentals-setup.md) | FastAPI basics, installation, Uvicorn, and Pydantic |
| [CRUD End-to-End](docs/03-crud-end-to-end.md) | GET, POST, PUT, PATCH, DELETE, and execution flow |
| [Request, Response and Status Codes](docs/04-response-request.md) | Request models, response models, validation, and errors |
| [Swagger, Postman and Testing](docs/05-swagger-postman-testing.md) | API documentation, endpoint testing, and expected results |

### Documentation Flow

```text
01. Project Overview
          ↓
02. Fundamentals and Setup
          ↓
03. CRUD Implementation
          ↓
04. Request / Response / Errors
          ↓
05. Swagger and Postman Testing
```

---

## ⚠️ Current Limitations

This project focuses on learning FastAPI fundamentals, so it has some limitations:

- **In-memory storage:** Product data is lost when the application restarts.
- **ID generation:** `len(products) + 1` can produce duplicate IDs after deletions.
- **No database integration:** Products are not stored persistently in PostgreSQL or MySQL.
- **Basic error handling:** The project handles missing products, but does not implement a comprehensive application-wide error-handling strategy.
- **Manual testing:** Swagger UI and Postman are used for testing; automated tests are not included in this project's current scope.

These limitations are documented so the current learning scope is clear.

---

## 🎓 Learning Outcomes

After completing this project, the main concepts covered include:

- Understanding how a FastAPI application receives and processes requests.
- Creating REST API endpoints using HTTP methods.
- Implementing CRUD operations.
- Defining request and response models using Pydantic.
- Understanding path parameters and JSON request bodies.
- Handling validation failures and missing resources.
- Choosing appropriate HTTP status codes.
- Exploring automatically generated OpenAPI documentation.
- Testing APIs through Swagger UI and Postman.
- Tracing the complete request-to-response flow.

---

## 🧠 Final Mental Model

The main lesson from this project is understanding how the different components work together.

```text
                  CLIENT
                    │
                    ▼
                  UVICORN
                    │
                    ▼
                  FASTAPI
                    │
                    ▼
             REQUEST VALIDATION
                    │
                    ▼
              ENDPOINT LOGIC
                    │
                    ▼
             PRODUCT LIST (RAM)
                    │
                    ▼
            RESPONSE PROCESSING
                    │
                    ▼
               JSON RESPONSE
                    │
                    ▼
                  CLIENT
```

- **Uvicorn** runs the application.
- **FastAPI** routes and processes requests.
- **Pydantic** validates data and defines response structures.
- **Endpoint functions** execute the CRUD logic.
- **The Python list** stores product data temporarily.
- **HTTP status codes and JSON responses** communicate the result to the client.

---

## ⭐ Final Conclusion

**FASTAPI PRACTICE** establishes the foundation for building REST APIs using Python.

The project moves from understanding FastAPI fundamentals to implementing complete CRUD operations, validating requests, structuring responses, handling errors, and testing endpoints through Swagger UI and Postman.

The most important outcome is understanding the complete request-to-response flow: how a client sends a request, how FastAPI routes and validates it, how endpoint logic processes the data, and how the client receives the final response.

The current implementation uses in-memory storage, making it suitable for learning API fundamentals. Database integration and further application improvements can be introduced when the project requires them.

> **Key takeaway:** The goal was not just to create six API endpoints, but to understand how a REST API works from the incoming HTTP request to the final JSON response.

---

## 🔗 Related Documentation

- [Project Overview](docs/01-project-overview.md)
- [Fundamentals and Setup](docs/02-fastapi-fundamentals-setup.md)
- [CRUD End-to-End](docs/03-crud-end-to-end.md)
- [Request, Response and Status Codes](docs/04-response-request.md)
- [Swagger, Postman and Testing](docs/05-swagger-postman-testing.md)