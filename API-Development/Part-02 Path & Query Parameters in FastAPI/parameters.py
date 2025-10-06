
# 1. Path Parameters
# Path parameters are part of the URL path. Used to identify a specific resource.

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/10")
def read_item():
    return {"item_id 10"}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

# 2. Query Parameters
# Query params come after ? in the URL. They are optional by default.

# @app.get("/search/")
# def search_items(q, limit):
#     return {"query": q, "limit": limit}

@app.get("/search/")
def search_items(q = None, limit = 10):
    return {"query": q, "limit": limit}

# from typing import Optional

# @app.get("/users/")
# def get_users(age: Optional[int] = None, limit: int = 10):
#     return {"age": age, "limit": limit}


# 3. Type Hints for Automatic Validation

@app.get("/category/{category_id}/")
def read_item(category_id:int):
    return {"category_id": category_id}