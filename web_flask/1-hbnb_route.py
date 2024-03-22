#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
       Displays 'Hello HBNB!'
       Returns:
           str: "Hello HBNB"
       """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def again():
    """
       Displays 'Hello HBNB!'
       Returns:
           str: "HBNB"
       """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
