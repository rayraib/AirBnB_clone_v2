#!/usr/bin/python3
'''
    Starts a Flask web application
'''
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    '''
        Return the index page
    '''
    return ('Hello HBNB!')


if __name__ == '__main__':
    app.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
