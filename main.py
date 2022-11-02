from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

class P(BaseModel):
    message: str
    currentdate: str

app = FastAPI()

@app.get("/multiply")


async def root(number : int = 1):

    return {"result": number*2}

@app.get("/hello")
async def root2():
    d = date.today()
    return {"message": "Hello you", "current date": d}


