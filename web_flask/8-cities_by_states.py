#!/usr/bin/python3
"""
Experimenting with flask
"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def ripandtear(_):
    """Rips and tears
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def lists():
    """State list
    """
    lili = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=lili)

if __name__ == '__main__':
    storage.reload()
    app.run('0.0.0.0', 5000)
