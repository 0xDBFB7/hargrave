import hargrave_conf
import json
from datetime import datetime, timedelta
import time
import sympy
import subprocess
from shutil import copy
import os
import logging
import hargrave_fs
from log import *
import re
#########Flask import and init stuff!###########
from flask import Flask
from flask import (request, redirect, url_for, session,
                   render_template,abort,send_from_directory)
app = Flask(__name__,template_folder="template", static_url_path='/assets')



@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('template/js', path)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('template/images', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('template/css', path)


##################Serve the index page#############
@app.route('/')
def index():
    root_json = hargrave_fs.get_root_json()
    current_settings = hargrave_fs.get_settings()
    return render_template('index.html',settings=current_settings,
                                        projects=root_json["projects"])


def validate_project_form(form_dict):
    """
    A little bit of server-side validation for the 'new project' form.
    Returns 0 if everything looks good,
    or dumps a json string with an error message if something needs attention.
    """

    if(not form_dict["project_id"]):
        return {"success":0,"alert_message":"You haven't entered a project ID."}

    if(not form_dict["project_id"].replace('_','').isalpha()):
        return {"success":0,"alert_message":"Sorry, the project ID only accepts ⁠⁠⁠\
         letters or underscores."}

    if(not form_dict["display_name"]):
        return {"success":0,"alert_message":"You haven't entered a display name."}

    if(not form_dict["start_date"]):
        return {"success":0,"alert_message":"You haven't entered a start date."}

    if(not form_dict["author"]):
        return {"success":0,"alert_message":"You haven't set the author."}

    if([x for x in hargrave_fs.get_root_json()["projects"] if x['project_id']]):
        return {"success":0,"alert_message":"That project ID already exists."}

    return 0

def create_project():
    root_json = hargrave_fs.load_json(hargrave_conf.ROOT_JSON_FILE)

    project = {}
    #All timestamps are unix epochs, purely because I happen to like unix time.
    project['start_date'] = datetime.strptime(request.form.get("start_date"),'%Y-%m-%d %I:%M %p').strftime("%s")
    project['creation_date'] = time.time()
    project['display_name'] = request.form.get('display_name')
    project['project_id'] = request.form.get('project_id')
    root_json['projects'].append(project)


    #subprocess.call(["xdg-open", hargrave_conf.ROOT_PROJECT_DIR])

    write_json(hargrave_conf.ROOT_JSON_FILE,root_json)
    return AssertionError


@app.route('/new_project',methods=['GET', 'POST'])
def new_project():
    current_root_json = hargrave_fs.get_root_json()
    #Form data is sent via a JS/ajax post request. The reply is injected into an alert.
    if request.method == 'POST':

        validation_result = validate_project_form(request.form)
        if(validation_result):
            #If something's wrong with the user's input, throw up an error.
            return validation_result

        validate_project()

        return json.dumps({"success":1,"project_id":request.form.get("project_id")})

    return render_template('new_project.html', USERS=current_settings["users"])

@app.route('/project',methods=['GET', 'POST'])
def project():
    current_settings = hargrave_fs.get_settings()

    return render_template('project.html', USERS=current_settings["users"])
