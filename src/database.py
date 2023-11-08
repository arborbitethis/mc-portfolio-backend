import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

from .config import Config

config = Config()

print(config.database_url)
# Synchronous engine for migrations and other synchronous operations
engine = create_engine(config.database_url)

# Asynchronous database for async CRUD operations
async_db = Database(config.database_url)

# Base class for ORM models
Base = declarative_base()

# Connect and disconnect functions
async def connect_db():
    await async_db.connect()

async def disconnect_db():
    await async_db.disconnect()