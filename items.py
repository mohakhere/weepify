from fastapi import APIRouter, HTTPException, Depends
from models import Item
from typing import Optional

router = APIRouter()

def get_db():
    # database connection logic
    db = get_database_connection()
    try:
        yield db
    finally:
        db.close()
