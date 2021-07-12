#!/usr/bin/env python3

from fastapi import Flask
import uvicorn
from project_models.models import Greeting

app = FastAPI()

@app.get("/hello/<name>")
def hello(name):
    greeting = Greeting(greet='hello', name=name)
    return f"{greeting.greet}, {greeting.name}"

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5001)
