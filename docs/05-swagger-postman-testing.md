# Swagger UI, Postman and API Testing

## 1. What Is API Testing?

API testing verifies whether an API behaves as expected by checking its responses, status codes, request validation, and error handling.

In this project, we use two tools:

- **Swagger UI:** Tests endpoints directly through the browser.
- **Postman:** Sends API requests and checks responses using a dedicated API testing tool.

## 2. Run the FastAPI Application

Activate the virtual environment and start the server:

```bash
.venv\Scripts\activate
uvicorn main:app --reload
```

The application runs at:

`http://127.0.0.1:8000`

Keep the terminal running while testing.

## 3. Swagger UI and OpenAPI

FastAPI automatically generates API documentation from the application's routes, parameters, models, and response configuration.

| URL | Purpose |
|---|---|
| `http://127.0.0.1:8000/docs` | Interactive Swagger UI |
| `http://127.0.0.1:8000/redoc` | Alternative API documentation |
| `http://127.0.0.1:8000/openapi.json` | OpenAPI schema in JSON format |

**OpenAPI** is a standard format for describing an API. Swagger UI uses this schema to display endpoints, request bodies, parameters, and responses.

### How to test in Swagger UI

1. Open `/docs` in your browser.
2. Select an endpoint.
3. Click **Try it out**.
4. Enter any required path parameters or JSON request body.
5. Click **Execute**.
6. Inspect the response status code and response body.

## 4. Postman Setup

1. Open Postman.
2. Create a new HTTP request.
3. Select the HTTP method.
4. Enter the endpoint URL.
5. For POST, PUT, and PATCH, select **Body → raw → JSON** and enter the request data.
6. Click **Send**.
7. Check the status code and response body.

For example:

- Method: `GET`
- URL: `http://127.0.0.1:8000/products`

No request body is required for this GET request.

## 5. Test All CRUD Endpoints

Use the following test cases in Swagger UI or Postman.

### Test 1: Retrieve All Products

**Method:** GET

**URL:** `/products`

Expected status: `200 OK`

Expected response structure:

```json
{
  "products": [
    {
      "id": 1,
      "name": "Laptop",
      "price": 50000
    }
  ]
}
```

The actual response contains all products currently in the list. The example shows only one product for brevity.

### Test 2: Create a Product

**Method:** POST

**URL:** `/products`

Request body:

```json
{
  "name": "Monitor",
  "price": 12000
}
```

Expected status: `201 Created`

Expected response structure:

```json
{
  "message": "Product created successfully",
  "product": {
    "id": 4,
    "name": "Monitor",
    "price": 12000
  }
}
```

The example assumes the initial three products are still present and no products have been added or deleted.

### Test 3: Retrieve a Product by ID

**Method:** GET

**URL:** `/products/1`

Expected status: `200 OK`

Expected response:

```json
{
  "product": {
    "id": 1,
    "name": "Laptop",
    "price": 50000
  }
}
```

### Test 4: Update a Complete Product

**Method:** PUT

**URL:** `/products/1`

Request body:

```json
{
  "name": "Gaming Laptop",
  "price": 75000
}
```

Expected status: `200 OK`

Expected response structure:

```json
{
  "message": "Product updated successfully",
  "product": {
    "id": 1,
    "name": "Gaming Laptop",
    "price": 75000
  }
}
```

Both editable fields are updated.

### Test 5: Partially Update a Product

**Method:** PATCH

**URL:** `/products/1`

Request body:

```json
{
  "price": 65000
}
```

Expected status: `200 OK`

Expected response structure:

```json
{
  "message": "Product partially updated successfully",
  "product": {
    "id": 1,
    "name": "Gaming Laptop",
    "price": 65000
  }
}
```

Only the price is changed; the name remains unchanged.

### Test 6: Delete a Product

**Method:** DELETE

**URL:** `/products/1`

Expected status: `200 OK`

Expected response structure:

```json
{
  "message": "Product deleted successfully",
  "product": {
    "id": 1,
    "name": "Gaming Laptop",
    "price": 65000
  }
}
```

The returned product represents the deleted data. A subsequent GET request for that ID should return `404 Not Found`.

## 6. Test Error Cases

| Test | Example request | Expected status |
|---|---|---|
| Product does not exist | `GET /products/999` | `404 Not Found` |
| PUT with missing required field | `PUT /products/1` with only `name` | `422 Unprocessable Entity` |
| POST with missing required field | `POST /products` with only `name` | `422 Unprocessable Entity` |
| Invalid integer path parameter | `GET /products/abc` | `422 Unprocessable Entity` |

For a missing product, the response body is:

```json
{
  "detail": "Product not found"
}
```

Validation error responses may contain additional information about the invalid field.

## 7. Important Testing Notes

- Test POST before testing the newly created product.
- Test PUT and PATCH using an existing product ID.
- Test DELETE last if you still need that product for other tests.
- A request can succeed with the wrong result, so inspect both the status code and response body.
- Since the project uses an in-memory list, restarting the server resets the initial data.
- Product IDs generated using `len(products) + 1` can become duplicated after certain deletion and creation sequences.

## 8. Final Revision Notes

1. **Swagger UI (`/docs`)** lets you explore and execute API requests in a browser.
2. **Postman** lets you send requests and inspect status codes, response bodies, and validation errors.
3. Test successful operations and failure cases to verify that the API behaves as expected.