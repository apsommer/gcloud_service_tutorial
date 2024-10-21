import os
from flask import Flask

"""
This code responds to requests with our "Hello World" greeting. HTTP handling is done by a Gunicorn web server in the 
container. When directly invoked for local use, this code creates a basic web server that listens on the port defined 
by the PORT environment variable.
"""
app = Flask(__name__)

@app.route("/")
def hello_world():

    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(
        debug = True,
        host = "0.0.0.0",
        port = int(os.environ.get("PORT", 8080)))