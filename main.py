from fastapi import FastAPI

app = FastAPI()

@app.get("/multiply")

async def root(number : int = 1):

    return {"result": number*2}