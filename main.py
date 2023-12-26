from fastapi import FastAPI
from routers import items

app = FastAPI()

app.include_router(items.router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
