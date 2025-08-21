from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="Mi API FastAPI",
    description="Una API mínima con FastAPI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "¡Hola Mundo! Mi API FastAPI está funcionando"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}")
async def read_user(user_id: int, name: Optional[str] = None):
    return {"user_id": user_id, "name": name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
