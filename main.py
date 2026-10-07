from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException
#CREATE FAST API APPLICATION
app=FastAPI()

class Product(BaseModel):
    name:str
    price:float

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    
class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None

class SingleProductResponse(BaseModel):
    product: ProductResponse
    
class ProductCreateResponse(BaseModel):
    message: str
    product: ProductResponse
    
class ProductUpdateResponse(BaseModel):
    message: str
    product: ProductResponse
    
class ProductPartialUpdateResponse(BaseModel):
    message: str
    product: ProductResponse
    
class ProductDeleteResponse(BaseModel):
    message: str
    product: ProductResponse
    
#TEMPORARY STORAGE FOR PRODUCTS
products=[
    {
        "id":1,
        "name":"Laptop",
        "price":50000
    },
    {
        "id":2,
        "name":"Mouse",
        "price":1000
    },
    {
        "id":3,
        "name":"KeyBoard",
        "price":2000
    }
]
#GET METHOD (TO RETRIEVE DATA FORM THE SERVER)
@app.get(
    "/products",
    response_model=ProductListResponse,
    status_code=status.HTTP_200_OK)
def get_products():
    return {
        "products": products
    }
#POST METHOD(TO SEND DATA TO THE SERVER )
@app.post("/products",status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    new_product={
        "id":len(products)+1,
        "name": product.name,
        "price": product.price
    }
    products.append(new_product)
    return {
        "message": "Product created successfully",
        "product": new_product
    }
    
#GET METHOD (TO SEND DATA OF SELECTED SPECIFIC PRODUCT)
@app.get(
    "/products/{product_id}",
    response_model=SingleProductResponse,
    status_code=status.HTTP_200_OK)
def get_product(product_id:int):
    for product in products:
        if product["id"]==product_id:
            return {
                "product":product
            }
    #PRODUCT WAS NOT FOUND 
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )
            
#PUT METHOD (TO UPDATE DATA OF SELECTED ONE'S)
@app.put("/products/{product_id}",response_model=ProductUpdateResponse,status_code=status.HTTP_200_OK)
def update_product(product_id:int,product:Product):
    for item in products:
        if item["id"]==product_id:
            item["name"]=product.name
            item["price"]=product.price
            return {
                "message":"Product updated successfully",
                "product":item
            }
    #PRODUCT WAS NOT FOUND 
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )

# PATCH METHOD (TO PARTIALLY UPDATE A PRODUCT)
@app.patch("/products/{product_id}", response_model=ProductPartialUpdateResponse,status_code=status.HTTP_200_OK)
def update_product_partially(
    product_id: int,
    product: ProductUpdate
):
    for item in products:

        # Find the product
        if item["id"] == product_id:

            # Update name only if it was provided
            if product.name is not None:
                item["name"] = product.name

            # Update price only if it was provided
            if product.price is not None:
                item["price"] = product.price

            return {
                "message": "Product partially updated successfully",
                "product": item
            }

    # Product not found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )
    
      
#DELETE METHOD (TO DELETE DATA OF SELECTED ONES'S)
@app.delete("/products/{product_id}", response_model=ProductDeleteResponse,status_code=status.HTTP_200_OK)
def delete_product(product_id:int):
    for item in products:
        if item["id"]==product_id:
            products.remove(item)
            return {
                "message":"Product deleted successfully",
                "product":item
            }
    #PRODUCT NOT FOUND
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )