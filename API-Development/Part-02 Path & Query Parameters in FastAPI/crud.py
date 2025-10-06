from fastapi import FastAPI
from request_body import Item
from typing import Optional

app = FastAPI()

fake_db = {}

# Create
@app.post("/items/")
def create_item(item_id: int, item: Item):
    fake_db[item_id] = item
    return {"msg": "Item created", "item": item}

# Read
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return fake_db.get(item_id, {"error": "Item not found"})

# Update (PUT = replace entire object)
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    fake_db[item_id] = item
    return {"msg": "Item updated", "item": item}

# Partial Update (PATCH = update some fields)
@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, name: Optional[str] = None, price: Optional[float] = None):
    if item_id not in fake_db:
        return {"error": "Item not found"}
    if name:
        fake_db[item_id].name = name
    if price:
        fake_db[item_id].price = price
    return {"msg": "Item partially updated", "item": fake_db[item_id]}

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in fake_db:
        del fake_db[item_id]
        return {"msg": "Item deleted"}
    return {"error": "Item not found"}
