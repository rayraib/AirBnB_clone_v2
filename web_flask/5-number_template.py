#!/usr/bin/python3
'''
    Starts a Flask web application
'''
from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return('HBNB!')


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return ('C %s') % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def python_text(text='is cool'):
    return ('python %s') % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return ("%d is a number") % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
