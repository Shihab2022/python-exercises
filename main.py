from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    website :HttpUrl

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World from FastAPI!"}

@app.post("/items")
def create_item(item: Item):
    return item



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}