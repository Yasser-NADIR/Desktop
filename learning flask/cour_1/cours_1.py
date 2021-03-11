from flask import Flask, request, redirect, abort
from flask_script import Manager
import sys

app = Flask(__name__)

@app.route('/')
def index():
	abort(500)
"""
@app.route('/<str:name>')
def salut(name):
	return "salut %s, bienveunue dans mon localhost"%name

manage = Manager(app)
"""
if __name__ == "__main__":
	#manage.run()
	app.run(debug=True)