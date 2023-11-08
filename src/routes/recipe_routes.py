from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from ..database import async_db, Base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
from databases import Database

router = APIRouter(tags=["recipes"], prefix="/recipe")


# Define the Recipe ORM model (if you haven't done it elsewhere)
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    image = Column(String)
    prep_time = Column(Integer)
    cook_time = Column(Integer)
    servings = Column(Integer)
    description = Column(String)
    ingredients = Column(String)
    instructions = Column(String)

# Define the Pydantic model for Recipe output
class RecipeOut(BaseModel):
    id: int
    title: str
    image: str
    description: str
    prep_time: int
    cook_time: int
    servings: int
    instructions: str

@router.get("/assets", response_model=List[RecipeOut])
async def get_recipe_list():
    query = Recipe.__table__.select()
    recipes = await async_db.fetch_all(query)
    return recipes