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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
        display “C ” followed by the value of the text variable
            (replace underscore '_' symbols with a space ' ')
        Returns:
            str: "C <text>"
        """
    return "C{}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text="iscool"):
    """
            display “python ” followed by the value of the text variable
                (replace underscore '_' symbols with a space ' ')
            Returns:
                str: "python <text>"
            """
    return 'python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    """
       display “n is a number” only if n is an integer
       Returns:
           int: the value of n
       """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
