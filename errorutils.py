import sys
import traceback
from flask import render_template

def render_traceback(ex):
    exc_type, exc_value, tb = sys.exc_info()

    exc_text = '\n'.join(traceback.format_exception_only(exc_type, exc_value))
    traceback_lines = [('File {}, line {} in {}'.format(*x), x[3] or '')
                        for x in traceback.extract_tb(tb)]

    return render_template('stacktrace.html',
        traceback=traceback_lines, exception=exc_text), 500
