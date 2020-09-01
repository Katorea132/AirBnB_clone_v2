#!/usr/bin/python3
"""
Experimenting with flask
"""
from flask import Flask, render_template
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


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def ptext(text):
    """Python text
    """
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Numbers
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def temnumb(n):
    """Returns a template with a number
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddeven(n):
    """Returns like the previous one but with odd or even
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
