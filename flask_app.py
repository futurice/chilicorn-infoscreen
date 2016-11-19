# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort
import time
import errorutils
import random
import codecs
from jinja2 import TemplateNotFound

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

# Show a formatted error message if there is a programming error
@app.errorhandler(500)
def print_traceback(ex):
    return errorutils.render_traceback(ex)


### Routes for session 2 ###

@app.route('/sessions/<n>')
def session_pages(n):
    try:
        return render_template('session' + n + '.html')
    except TemplateNotFound:
        abort(404)

@app.route('/months/<selector>')
def list_exercise(selector):
    n = int(selector)

    months = ['tammikuu', 'helmikuu', 'maaliskuu', 'huhtikuu',
              'toukokuu', 'kesäkuu', 'heinäkuu', 'elokuu',
              'syyskuu', 'lokakuu', 'marraskuu', 'joulukuu']

    # replace ? with the month name that is at position n in the list
    selected_month = '?'

    # replace ? with a list of month names before the position n
    before = '?'

    # replace ? with a list of month names after the position n
    after = '?'
    
    return render_template('months.html',
                           n=n,
                           month=selected_month,
                           before=before,
                           after=after)

@app.route('/view/textfromfile')
def infoview_from_file():
    # Read lines from a file into an array
    lines = codecs.open('texts/example.txt', 'r', 'UTF-8').readlines()

    first_line = ''  # put the first line from the file here
    other_lines = '' # rest of the lines here joined together.
                     # Hint: To join lines, use '\n'.join(...)
    
    return render_template('views/text_template.html',
                           title=first_line,
                           text=other_lines)

@app.route('/view/<viewname>')
def infoview(viewname):
    template = 'views/' + viewname + '.html'
    return render_template(template)

@app.route('/randomview')
def randomview():
    # Task 1: Replace these with your own content
    templates = ['views/image.html', 'views/text.html', 'views/webpage.html']

    # Task 2: Modify the next line so that is selected a random
    # element from the templates list.
    #
    # Hint: Use the random.choice() function.
    selected_template = templates[0]

    # This will be needed in a later exercise
    automatic_reload = False
    
    return render_template(selected_template, automatic_reload=automatic_reload)
