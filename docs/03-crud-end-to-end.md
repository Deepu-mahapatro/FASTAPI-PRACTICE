# CRUD Operations — End-to-End

## 1. What Is CRUD?

CRUD represents the four basic operations performed on a resource.

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | POST | Add a new product |
| Read | GET | Retrieve product data |
| Update | PUT | Replace a product's data |
| Partial Update | PATCH | Modify selected fields |
| Delete | DELETE | Remove a product |

In this project, a product is the resource, and a Python list stores the product data temporarily.

## 2. Initial Product Data

The application starts with three products:

```python
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 1000},
    {"id": 3, "name": "KeyBoard", "price": 2000}
]
```

Each product contains an ID, name, and price.

## 3. GET — Retrieve All Products

**Endpoint:** `GET /products`

```python
@app.get("/products", response_model=ProductListResponse)
def get_products():
    return {"products": products}
```

**How it works:**

1. The client sends a GET request.
2. FastAPI executes `get_products()`.
3. The function returns the product list.
4. FastAPI validates and structures the response using `ProductListResponse`.
5. The client receives the product data with status code `200 OK`.

## 4. POST — Create a Product

**Endpoint:** `POST /products`

Request body:

```json
{
  "name": "Monitor",
  "price": 12000
}
```

Implementation:

```python
@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }

    products.append(new_product)

    return {
        "message": "Product created successfully",
        "product": new_product
    }
```

**How it works:**

1. The client sends product data.
2. FastAPI validates it using the `Product` model.
3. The function creates a product dictionary and assigns an ID.
4. The new product is appended to the list.
5. The API returns the created product with status code `201 Created`.

**Important:** The current ID-generation logic, `len(products) + 1`, can produce duplicate IDs after deletions. A database or a safer ID-generation strategy should be used when improving this project.

## 5. GET — Retrieve a Product by ID

**Endpoint:** `GET /products/{product_id}`

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

**How it works:**

1. The client provides an ID in the URL.
2. FastAPI converts and validates the path parameter as an integer.
3. The function searches the list for a matching ID.
4. If found, the product is returned with `200 OK`.
5. If not found, the API raises an HTTP exception and returns `404 Not Found`.

Example: `GET /products/2` retrieves the product whose ID is `2`.

## 6. PUT — Update a Complete Product

**Endpoint:** `PUT /products/{product_id}`

Request body:

```json
{
  "name": "Gaming Laptop",
  "price": 75000
}
```

Implementation:

```python
@app.put(
    "/products/{product_id}",
    response_model=ProductUpdateResponse
)
def update_product(product_id: int, product: Product):
    for existing_product in products:
        if existing_product["id"] == product_id:
            existing_product["name"] = product.name
            existing_product["price"] = product.price

            return {
                "message": "Product updated successfully",
                "product": existing_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
```

**How it works:**

1. The client provides the product ID and complete product data.
2. FastAPI validates the request body using `Product`.
3. The function searches for the product.
4. Both the name and price are updated.
5. The updated product is returned with `200 OK`, or `404 Not Found` if the ID does not exist.

**Key point:** PUT is used here to replace the product's editable fields. The request must include both `name` and `price`.

## 7. PATCH — Update Selected Fields

**Endpoint:** `PATCH /products/{product_id}`

Request body:

```json
{
  "price": 65000
}
```

Implementation:

```
