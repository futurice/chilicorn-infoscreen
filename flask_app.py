from flask import Flask
from flask import render_template
import errorutils

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/friend')
def my_friend():
    return render_template('friendpage.html')

@app.route('/friend/<friend_name>')
def my_friend_dynamic(friend_name):

    # The friend_name is a variable. It's value can be modified by
    # changing the last part of the address on the browser address bar.
    
    friend_age = 99
    friend_hair_color = '???'
    friend_hobbies = '???'

    # Set values based on friend's name like this:
    if friend_name == 'Niko-Petteri':
        friend_age = 15
        friend_hair_color = 'Green'

    return render_template('friendpage2.html',
                           name=friend_name,
                           age=friend_age,
                           hair_color=friend_hair_color,
                           hobbies=friend_hobbies)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.errorhandler(500)
def print_traceback(ex):
    return errorutils.render_traceback(ex)
