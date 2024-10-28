from typing import Optional
from sqlmodel import Field, Relationship
from .base import Base

class Product(Base, table=True):
    __tablename__ = "products"

    name: str
    price: str
    quality: str
    summary: str
    image: Optional[str] = None

    category_id: Optional[int] = Field(default=None, foreign_key="categories.id")
    