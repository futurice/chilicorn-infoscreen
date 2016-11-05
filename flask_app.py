from flask import Flask
from flask import render_template
import errorutils

app = Flask(__name__)

@app.route('/')
def mainpage():
    return 'Hello from Flask!'

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.errorhandler(500)
def print_traceback(ex):
    return errorutils.render_traceback(ex)
