#!/usr/bin/python3
'''
    Render all cities by states
'''
from flask import Flask
from models import storage, DBStorage
from flask import render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    '''
        list states
    '''
    states = (storage.all('State')).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def city_by_states(id):
    '''
        list states
    '''
    cities = []
    states = (storage.all('State')).values()
    for state in states:
        if state.id == id:
            state_name = state.name
            if isinstance(storage, DBStorage):
                cities = (state.cities)
                break
            else:
                cities = (state.cities())
                break
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
