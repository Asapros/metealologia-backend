import importlib.metadata

import uvicorn
from fastapi import FastAPI

app = FastAPI()  
@app.get("/")
async def main_route():
  return "MeteALOlogia API v{}".format(importlib.metadata.version("metealologia_api"))

def start():
    uvicorn.run("metealologia_api.main:app", host="localhost", port=8000, reload=True)
