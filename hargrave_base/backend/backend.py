
from hargrave_base import app

from flask import (request, redirect, url_for, session,
                   render_template,abort,send_from_directory)

##################Serve the index page#############
@app.route('/')
def index():
    return render_template('index.html',settings={})

