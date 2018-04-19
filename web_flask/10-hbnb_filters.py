#!/usr/bin/python3
'''
'''
import os
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


states = (storage.all('State')).values()
cities = storage.all('City').values()
amenities = storage.all('Amenity').values()

@app.teardown_appcontext
def teardown(exception):
    '''
        close session
    '''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filtered_index():
    '''
        Display a page
    '''
    return render_template('10-hbnb_filters.html',
                           states=states, cities=cities, amenities=amenities) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
