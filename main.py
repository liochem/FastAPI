from fastapi import FastAPI

app = FastAPI()

@app.get("/{path}")

async def root(path : str):
    if path == "hello":
        return "Hello you"