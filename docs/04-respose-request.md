# Request, Response, Status Codes and Error Handling

## 1. What Is an HTTP Request?

An HTTP request is a message sent by a client to an API to perform an operation or retrieve data.

A request commonly contains:

- **HTTP method:** Specifies the operation, such as GET or POST.
- **URL:** Identifies the endpoint.
- **Path parameters:** Values included in the URL, such as `product_id`.
- **Request body:** Data sent to the API, usually as JSON.
- **Headers:** Additional information, such as the content type.

Example request body:

```json
{
  "name": "Laptop",
  "price": 50000
}
```

## 2. Pydantic Request Models

A request model defines the structure and types of data an endpoint accepts.

Example from this project:

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
```

Used in an endpoint:

```python
@app.post("/products")
def create_product(product: Product):
    return {
        "name": product.name,
        "price": product.price
    }
```

**How it works:**

1. The client sends JSON data.
2. FastAPI reads the request body.
3. Pydantic validates the data against `Product`.
4. If valid, the endpoint receives a `Product` object.
5. If invalid, FastAPI returns a request validation error, normally with status code `422`.

Because `name` and `price` are required, both must be provided.

## 3. PUT vs PATCH Request Models

This project uses separate models for complete and partial updates.

```python
class Product(BaseModel):
    name: str
    price: float

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
```

| Model | Purpose |
|---|---|
| `Product` | Requires both name and price |
| `ProductUpdate` | Allows either field to be omitted |

For PUT, the client sends the complete editable product data:

```json
{
  "name": "Laptop",
  "price": 55000
}
```

For PATCH, the client can send only the field it wants to update:

```json
{
  "price": 55000
}
```

**Important:** In this project, the PATCH endpoint updates a field only when its value is not `None`. The model allows omitted fields, but the endpoint does not distinguish an omitted field from an explicitly supplied `null` value.

## 4. What Is an HTTP Response?

An HTTP response is the message the server sends back to the client after processing a request.

It commonly contains:

- **Status code:** Indicates the result of the request.
- **Response body:** Contains returned data or an error message.
- **Headers:** Provide additional response information.

Example successful response:

```json
{
  "message": "Product created successfully",
  "product": {
    "id": 4,
    "name": "Laptop",
    "price": 50000
  }
}
```

The status code `201 Created` indicates that the product was created successfully.

## 5. Response Models

A response model defines the expected structure of the data returned by an endpoint.

Example from this project:

```python
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class SingleProductResponse(BaseModel):
    product: ProductResponse
```

Used in an endpoint:

```python
@app.get(
    "/products/{product_id}",
    response_model=SingleProductResponse
)
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"product": product}

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
```

**Purpose of `response_model`:**

- Defines the expected response structure.
- Validates returned data.
- Serializes the response into JSON.
- Helps generate accurate API documentation.

The response model does not replace request validation. Request models validate incoming data, while response models define and validate outgoing data.

## 6. Important HTTP Status Codes

| Status code | Meaning | Usage in this project |
|---|---|---|
| `200 OK` | Request succeeded | GET, PUT, PATCH and DELETE |
| `201 Created` | Resource created | POST |
| `400 Bad Request` | Request cannot be processed due to a client error | General client errors |
| `404 Not Found` | Requested resource does not exist | Product ID not found |
| `422 Unprocessable Entity` | Request data failed validation | Missing or invalid request fields |
| `500 Internal Server Error` | Unexpected server-side error | Unhandled application errors |

The exact status code depends on the endpoint and the error being handled.

## 7. HTTPException — Error Handling

`HTTPException` allows an endpoint to stop normal processing and return an HTTP error response.

Syntax:

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Product not found"
)
```

Example error response:

```json
{
  "detail": "Product not found"
}
```

The response uses status code `404 Not Found`.

**How it works:**

1. The endpoint searches for the requested product.
2. The product is not found.
3. The endpoint raises `HTTPException`.
4. FastAPI stops normal processing for that request.
5. FastAPI returns the specified status code and error details.

In this project, the GET-by-ID, PUT, PATCH, and DELETE endpoints use this pattern when the product does not exist.

## 8. Complete Request-to-Response Flow

1. The client sends an HTTP request.
2. FastAPI matches the method and URL to an endpoint.
3. FastAPI validates the path parameters and request body when applicable.
4. The endpoint performs its operation.
5. If an expected error occurs, the endpoint may raise `HTTPException`.
6. FastAPI processes the returned data using the configured response model and serializes it.
7. The client receives the response body and HTTP status code.

## 9. Final Revision Notes

1. **Request model:** Defines and validates the data accepted by an endpoint.
2. **Response model:** Defines and validates the structure of returned data.
3. **Status codes and HTTPException:** Communicate success or failure clearly, such as `201` for creation and `404` when a product is not found.
