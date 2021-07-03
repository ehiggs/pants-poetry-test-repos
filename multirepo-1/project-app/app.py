#!/usr/bin/env python3

from flask import Flask
from project_models.models import Greeting

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    greeting = Greeting(greet='hello', name=name)
    return f"{greeting.greet}, {greeting.name}"

if __name__ == '__main__':
    app.run()
