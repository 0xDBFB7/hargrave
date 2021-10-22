
from hargrave_base import app

from flask import (request, redirect, url_for, session,
                   render_template,abort,send_from_directory)

##################Serve the index page#############
@app.route('/', methods = ['GET'])
@app.route('/<int:primary_id>', methods = ['GET', 'POST'])
def index(primary_id):

    # if request.method == 'GET':


    # if request.method == 'POST':

    return render_template('index.html',settings={})

