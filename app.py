from fastapi import FastAPI
from mangum import Mangum
from typing import Any, Dict

app = FastAPI()

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello from FastAPI on Lambda!"}

lambda_handler = Mangum(app, lifespan="off")
