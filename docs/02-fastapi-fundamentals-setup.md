# FastAPI Fundamentals and Setup

## 1. What Is FastAPI?

**FastAPI** is a Python web framework used to build APIs. It helps developers create endpoints, validate request data, and return structured responses.

### Why do we use FastAPI?

- To build REST APIs using Python.
- To validate incoming data using Pydantic.
- To generate interactive API documentation automatically.
- To build APIs with asynchronous support when needed.

## 2. How FastAPI Works

FastAPI follows a request-to-response flow:

1. The client sends an HTTP request.
2. Uvicorn receives the request and passes it to FastAPI.
3. FastAPI identifies the matching endpoint.
4. Request data is validated when applicable.
5. The endpoint executes its logic.
6. FastAPI prepares the response.
7. The client receives the response and status code.

## 3. Project Setup

### Step 1: Create a project folder

```bash
mkdir "FASTAPI PRACTICE"
cd "FASTAPI PRACTICE"
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

A virtual environment keeps the project's Python packages separate from other projects.

### Step 3: Install dependencies

```bash
pip install fastapi uvicorn
```

- `fastapi`: Provides the framework for creating APIs.
- `uvicorn`: Runs the FastAPI application as an ASGI server.

Save the installed dependencies:

```bash
pip freeze > requirements.txt
```

## 4. Create the FastAPI Application

Create a file named `main.py`.

```python
from fastapi import FastAPI

app = FastAPI()
```

**Explanation:**

- `FastAPI` is the class imported from the framework.
- `app = FastAPI()` creates the application instance.
- `app` is used to register endpoints and configure the application.

## 5. Create Your First Endpoint

Add the following code to `main.py`:

```python
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

**Explanation:**

- `@app.get("/")` registers a GET endpoint at the root path.
- `home()` executes when a matching GET request arrives.
- The returned Python dictionary is serialized into a JSON response.

## 6. Run the Application

Execute this command in the terminal:

```bash
uvicorn main:app --reload
```

Meaning:

- `uvicorn`: Starts the server.
- `main`: Refers to `main.py`, without the `.py` extension.
- `app`: Refers to the FastAPI application instance.
- `--reload`: Restarts the development server when code changes.

Open these URLs in your browser:

- Application: `http://127.0.0.1:8000/`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Expected response at `/`:

```json
{
  "message": "Welcome to FastAPI"
}
```

## 7. Pydantic Fundamentals

**Pydantic** validates data against Python type annotations and model definitions.

Example:

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
```

This model defines the expected structure of a product.

Example valid request body:

```json
{
  "name": "Laptop",
  "price": 50000
}
```

FastAPI uses the model to validate incoming request data when it is declared as an endpoint parameter.

If required data is missing or invalid, FastAPI normally returns a `422 Unprocessable Entity` response for request validation errors.

## 8. Important Concepts

| Concept | Purpose |
|---|---|
| FastAPI | Defines the API application and endpoints |
| Uvicorn | Runs the application server |
| Endpoint | Handles a particular request path and method |
| HTTP method | Specifies the operation, such as GET or POST |
| Pydantic model | Defines and validates data structures |
| Virtual environment | Isolates project dependencies |
| Swagger UI | Allows interactive API exploration and testing |

## 9. Key Takeaway

FastAPI defines the API, Uvicorn runs it, and Pydantic validates structured data. Together, they provide the foundation for building REST APIs in Python.
