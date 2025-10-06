from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool
    

app = FastAPI()

@app.post("/items/")
def create_item(item: Item):
    print(item)
