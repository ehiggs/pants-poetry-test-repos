#!/usr/bin/env python3

from fastapi import FastAPI
import uvicorn
from project_models.models import Greeting

# Because python is interpreted and each package is built from the same top 
# level venv, we can do things we wouldn't really want, like import packages 
# we don't depend on in this subproject.
from flask import Flask

app = FastAPI()


@app.get("/")
async def root():
    return f"Hello, try using /hello/<name>"

@app.get("/hello/{name}")
async def hello(name):
    greeting = Greeting(greet='hello', name=name)
    return f"{greeting.greet}, {greeting.name}"

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5001)
