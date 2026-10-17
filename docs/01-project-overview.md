# FastAPI Practice — Project Overview

## 1. About the Project

**FASTAPI PRACTICE** is a beginner-level project created to understand FastAPI and build REST APIs using Python.

The project focuses on CRUD operations, request and response models, HTTP status codes, and error handling.

## 2. Project Objectives

- Understand how FastAPI applications work.
- Create REST API endpoints using HTTP methods.
- Perform CRUD operations on product data.
- Validate incoming data using Pydantic models.
- Structure API responses using response models.
- Handle errors using `HTTPException`.
- Test endpoints using Swagger UI and Postman.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Build REST APIs |
| Pydantic | Validate request data and structure responses |
| Uvicorn | Run the FastAPI application |
| Swagger UI | Explore and test API endpoints |
| Postman | Send requests and verify responses |

## 4. Features Implemented

| HTTP Method | Endpoint | Purpose |
|---|---|---|
| GET | `/products` | Retrieve all products |
| POST | `/products` | Create a product |
| GET | `/products/{product_id}` | Retrieve a product by ID |
| PUT | `/products/{product_id}` | Replace a product's data |
| PATCH | `/products/{product_id}` | Update selected fields |
| DELETE | `/products/{product_id}` | Delete a product |

## 5. Important Concepts Covered

- **FastAPI application:** Created using `FastAPI()`.
- **Path parameters:** Pass values through the URL, such as `product_id`.
- **Pydantic models:** Define and validate the structure of incoming data.
- **Request models:** Specify the data accepted by an endpoint.
- **Response models:** Define and validate the structure of API responses.
- **HTTP status codes:** Communicate the result of a request, such as `200`, `201`, and `404`.
- **HTTPException:** Return appropriate errors when a requested product does not exist.
- **CRUD:** Create, Read, Update, and Delete resources.

## 6. How the Project Works

1. A client sends an HTTP request using Swagger UI or Postman.
2. FastAPI matches the request to the appropriate endpoint.
3. Pydantic validates the incoming data when a request model is used.
4. The endpoint executes the required operation on the product list.
5. FastAPI validates and serializes the response when a response model is configured.
6. The client receives the response data and HTTP status code.

## 7. Data Storage

This project currently uses a Python list to store product data in memory.

**Limitation:** Data is temporary. Changes are lost when the application restarts. The project does not yet use a database for product storage.

## 8. API Documentation and Testing

When the application is running, open:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

Swagger UI allows you to explore endpoints and send requests directly. Postman can also be used to test requests, response bodies, status codes, and error cases.

## 9. Project Scope

This project establishes the fundamentals of building REST APIs with FastAPI. It focuses on understanding the request-to-response flow and implementing CRUD operations.

**Key takeaway:** This is a learning project using in-memory data, not a complete production application with persistent database storage.