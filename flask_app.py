from flask import Flask
from flask import render_template
import time
import errorutils
import random

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

@app.route('/time')
def time_dependent():
    time_of_day = time.strftime('%H:%M:%S')
    weekday = time.strftime('%A')
    minute = time.strftime('%M')

    last_minute_digit = minute[-1:]
    if last_minute_digit in ['0', '2', '4', '6', '8']:
        even_minute = True
    else:
        even_minute = False

    return render_template('time.html', time_of_day=time_of_day, weekday=weekday, even_minute=even_minute)

@app.route('/view/<viewname>')
def infoview(viewname):
    template = 'views/' + viewname + '.html'
    return render_template(template)

@app.route('/randomview')
def infoscreen():
    templates = ['views/image.html', 'views/text.html', 'views/webpage.html']

    # Exercise: Modify the next line so that is selected a random
    # element from the templates list.
    #
    # Hint: Use the random.choice() function.
    selected_template = templates[0]

    return render_template(selected_template)

# Show a formatted error message if there is a programming error
@app.errorhandler(500)
def print_traceback(ex):
    return errorutils.render_traceback(ex)
