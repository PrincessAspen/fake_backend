import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select
from db import get_session
from models.product import Product
from models.category import Category
from typing import List

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:3000',
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

@app.get("/")
def root():
    return {"message": "Hello World"}

app.mount("/images", StaticFiles(directory="images"), name="images")

# Endpoint to list all products
@app.get("/products")
def list_products(session: Session = Depends(get_session)):
    statement = select(Product)
    results = session.exec(statement)
    return results.all()

# Endpoint to retrieve a single product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Endpoint to list all categories
@app.get("/categories")
def list_categories(session: Session = Depends(get_session)):
    statement = select(Category)
    results = session.exec(statement)
    return results.all()

# Endpoint to retrieve a single category by ID
@app.get("/categories/{category_id}")
def get_category(category_id: int, session: Session = Depends(get_session)):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.get("/category-products/{category_name}", response_model=List[Product])
def get_category_products(category_name: str, session: Session = Depends(get_session)):
    # Query to join products with the specified category
    statement = (
        select(Product)
        .join(Category)
        .where(Category.name == category_name)
    )
    results = session.exec(statement).all()
    if not results:
        raise HTTPException(status_code=404, detail="Category not found or no products in this category")
    return results

# Endpoint to create a new product
@app.post("/create/product")
def create_product(name: str, price: str, quality: str, summary: str, image: str = None, session: Session = Depends(get_session)):
    product = Product(name=name, price=price, quality=quality, summary=summary, image=image)
    session.add(product)
    session.commit()
    session.refresh(product)
    return {"product": product}

# Endpoint to create a new category
@app.post("/create/category")
def create_category(name: str, session: Session = Depends(get_session)):
    category = Category(name=name)
    session.add(category)
    session.commit()
    session.refresh(category)
    return {"category": category}

# Endpoint to update an existing product
@app.put("/update/product/{id}")
def update_product(id: int, name: str, price: str, quality: str, summary: str, image: str, session: Session = Depends(get_session)):
    product = session.get(Product, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = name
    product.price = price
    product.quality = quality
    product.summary = summary
    product.image = image
    session.commit()
    session.refresh(product)
    return {"product": product}

# Endpoint to delete a product
@app.delete("/delete/product/{id}")
def delete_product(id: int, session: Session = Depends(get_session)):
    product = session.get(Product, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    session.delete(product)
    session.commit()
    return {"detail": "Product deleted"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)