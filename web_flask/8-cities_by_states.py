#!/usr/bin/python3
'''
    Render all cities by states
'''
from flask import Flask
from models import storage, State
from flask import render_template
import os



app = Flask(__name__)
states = (storage.all('State')).values()
cities = []
for state in states:
    if (os.environ.get('HBNB_TYPE_STORAGE')) == 'db':
        cities.append(state.cities)
    else:
        cities.append(state.cities())


@app.route('/cities_by_states', strict_slashes=False)
def list_city_by_states():
    '''
        list cities by states
    '''
    return render_template('8-cities_by_states.html',
                           cities=cities, states=states)


@app.teardown_appcontext
def tear_down(exception):
    '''
        teardown
    '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
