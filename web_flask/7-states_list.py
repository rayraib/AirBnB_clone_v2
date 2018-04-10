#!/usr/bin/python3
'''
'''
from flask import Flask
from models import storage
from flask import render_template 


app = Flask(__name__)


@app.route('states_list', strict_slashes=False)
def list_states():
    storage.reload()
    data = storage.all()
    return render_template('7-states_list.html', value=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
