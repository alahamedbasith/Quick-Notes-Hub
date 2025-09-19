from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/")
def read_root():
    return {"message": "This is Local Address route! "}