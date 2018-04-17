#!/usr/bin/python3
'''
    Starts a Flask web application
'''
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    return('HBNB!')


@app.route('/c/<text>')
def c_text(text):
    return ('C %s') %text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def python_text(text='is cool'):
        return ('python %s') % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
