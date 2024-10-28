from typing import List
from sqlmodel import Field, Relationship
from .base import Base

class Category(Base, table=True):
    __tablename__ = "categories"

    name: str
    