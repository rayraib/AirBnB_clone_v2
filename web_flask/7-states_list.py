#!/usr/bin/python3
'''
'''
from flask import Flask
from models import storage
from flask import render_template 


app = Flask(__name__)

storage.reload()
data = storage.all()
print(data)

@app.route('/states_list', strict_slashes=False)
def list_states():
   return render_template('7-states_list.html', data=data)

@app.teardown_appcontext
def tear_down(storage):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
