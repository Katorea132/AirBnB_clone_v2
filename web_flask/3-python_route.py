#!/usr/bin/python3
"""
Experimenting with flask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def initial():
    """Initial
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """Returns the letter c plus the ext
    """
    return "C %s" % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ptext(text):
    """Python text
    """
    return "Python %s" % text.replace('_', ' ')

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
