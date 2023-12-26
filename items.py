# routers/items.py
from fastapi import APIRouter, HTTPException
from models import Item

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

@router.post("/items/")
def create_item(item: Item):
    # Process the item and return a response
    return {"item_name": item.name, "item_description": item.description}
