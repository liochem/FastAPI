from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

class P(BaseModel):
    message: str
    currentdate: str

app = FastAPI()

@app.get("/{path}")

async def root(path : str):
    if path == "hello":
        d = date.today()
        return {"message": "Hello you", "current date": d}

