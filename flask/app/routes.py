from app import app
import os
from controllers.names_controller import get_all_names
from flask import Response
import json


@app.route("/")
def index():
    app_name = os.environ["APP_NAME"]

    return f"It's working. This is {app_name}"


@app.route("/test")
def test():
    return "This is working too"


@app.route("/names")
def names():
    names = get_all_names()
    return Response(json.dumps(names), mimetype='application/json')