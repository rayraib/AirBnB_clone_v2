#!/usr/bin/python3
'''
    Render state and its cities based on state id
'''
from flask import Flask
from models import storage
from flask import render_template
import os


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    '''
        list all states
    '''
    states = (storage.all('State')).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def city_by_states(id):
    '''
        list cities belonging to state with id
    '''
    cities = []
    flag = 0
    states = (storage.all('State')).values()
    for state in states:
        if state.id == id:
            flag = 1
            state_name = state.name
            if (os.environ.get('HBNB_TYPE_STORAGE')) == 'db':
                cities = (state.cities)
                break
            else:
                cities = (state.cities())
                break
    if flag == 0:
        state_name = ''
    return render_template('9-states.html',
                           cities=cities, state_name=state_name)


@app.teardown_appcontext
def tear_down(exception):
    '''
        teardown
    '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
