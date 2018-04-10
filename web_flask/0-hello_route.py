#!/usr/bin/python3
'''
	Starts a Flask web application
'''
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
	return('This is the index page \n Hello world!')
