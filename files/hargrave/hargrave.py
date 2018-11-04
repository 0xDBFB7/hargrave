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

def check_git_status(input_dir):
    """
    A convienience function to see if the input directory is a git repo.
    Returns 0 if input is not inside a repo.
    """
    cmd = ['git', 'status']
    p = subprocess.Popen(cmd, cwd=input_dir)
    p.wait()
    return p.returncode == 0

def run_command(cmd,input_dir):
    """
    Another git convienience function, this time just running
    an arbitrary command in an arbitrary location and waiting until quit.
    """
    p = subprocess.Popen(cmd, cwd=input_dir)
    p.wait()

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
    return render_template('index.html',settings=root_json["settings"],
                                        projects=sorted(root_json["projects"],key=lambda k: k['opened_count']))


def validate_project_form(form_dict):
    """
    A little bit of server-side validation for the 'new project' form.
    Returns 0 if everything looks good,
    or dumps a dict with an error message if something needs attention.
    """

    if(not form_dict["project_id"]):
        return {"success":0,"alert_message":"You haven't entered a project ID."}

    if(not form_dict["project_id"].replace('_','').isalnum()):
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

def create_project(form_dict):
    """
    Now we want to
    1. Add project to the root.json project listing (this might not be required later on, as
    it might be easier just to search for existing project.json files in PROJECT_DIR)
    2. Create a folder with the project ID in projects/ if it doesn't yet exist,
    and create all subdirs as requested in settings.
    3. Create a file called hargrave_project.json if it doesn't yet exist.
    4. Initialize a git repo (if it doesn't yet exist), make an initial commit, and set the remote origin.
    """
    PROJECT_DIR = hargrave_conf.PROJECTS_DIR + form_dict["project_id"] + '/'


    root_json = hargrave_fs.get_root_json()
    #Existence checking is done in validate_project_form - not sure if that's ideal,
    #but whatever.
    project = {}
    project["opened_count"] = 0 #number of times this project has been opened
                                #primarily for alternate sorting
    project["last_opened"] = time.time() #Last time this has been
    project["display_name"] = form_dict['display_name']
    project["project_id"] = form_dict['project_id']
    root_json['projects'].append(project)
    hargrave_fs.write_root_json(root_json)

    for subdir in root_json['settings']["default_directories"]:
        os.makedirs(PROJECT_DIR + subdir, exist_ok=True)

    #Are we importing an existing project?
    if(not os.path.isfile(PROJECT_DIR + '/hargrave_project.json')):
        project = {}
        #All timestamps are unix epochs, purely because I happen to like unix time.
        project['start_date'] = int(datetime.strptime(form_dict["start_date"],'%Y-%m-%d %I:%M %p').strftime("%s"))
        project['creation_date'] = time.time()
        project['display_name'] = form_dict['display_name']
        project['project_id'] = form_dict['project_id']
        project['author'] = form_dict['author']
        project['references'] = []
        project['parameterized_logs'] = []

        hargrave_fs.write_json(PROJECT_DIR + '/hargrave_project.json',project)

    if(not check_git_status(PROJECT_DIR)):
        run_command(["git","init"])
        if(form_dict["remote_origin"]):
            run_command(["git","remote","add","origin",form_dict["remote_origin"]])


@app.route('/new_project',methods=['GET', 'POST'])
def new_project():
    current_root_json = hargrave_fs.get_root_json()
    #Form data is sent via a JS/ajax post request. The reply is injected into an alert.
    if request.method == 'POST':
        validation_result = validate_project_form(request.form)
        if(validation_result):
            #If something's wrong with the user's input, throw up an error.
            return json.dumps(validation_result)

        create_project(request.form)

        return json.dumps({"success":1,"project_id":request.form.get("project_id")})

    return render_template('new_project.html', USERS=current_root_json["settings"]["users"])


#The project ID can be supplied as a get request variable
#purely so that the link to a specific project can be shared
#without having to do any fancy magic
@app.route('/project',methods=['GET', 'POST'])
def project():
    root_json = hargrave_fs.get_root_json()
    if(not request.args.get("id") in [x["project_id"] for x in root_json["projects"]]):
        #We could use a prettier error page here.
        return abort(404)

    project = [x for x in root_json["projects"] if x["project_id"] == request.args.get("id")][0]


    if request.method == 'POST':
        if("open_in_file_browser" in request.form.keys()):
            open_in_file_browser(project["project_id"])

        return json.dumps({"success":1,"project_id":request.form.get("project_id")})

    #This'll keep incrementing even if the user's just browsing around in the project.
    # project["opened_count"] += 1
    # project["last_opened"] = time.time()
    # hargrave_fs.write_root_json(root_json)

    return render_template('project.html', project=project)
