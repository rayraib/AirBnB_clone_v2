#!/usr/bin/python3
'''
'''
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)

storage.reload()
all_states = storage.all('State')
states = all_states.values()


@app.route('/states_list', strict_slashes=False)
def list_states():
    return render_template('7-states_list.html', states=states)


'''
@app.teardown_appcontext
def tear_down(storage):
    storage.close()
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
