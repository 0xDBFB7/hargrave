import hargrave_conf

from datetime import datetime, timedelta
import time
import sympy
import subprocess
from shutil import copy
import os
import logging

##################Logging stuff!################
logging.basicConfig(filename=hargrave_conf.LOG_FILE,level=logging.DEBUG)

def log(message):
    logging.debug(message)

#########Flask import and init stuff!###########
from flask import Flask
from flask import (request, redirect, url_for, session,
                   render_template,abort,send_from_directory)
app = Flask(__name__,template_folder="template", static_url_path='/assets')

################JSON import and helper functions########
import json

def load_json(filename):
    loaded_json = json.loads(open(filename).read())
    log("Read json \n{}\n from {}".format(loaded_json,filename))
    return loaded_json


def write_json(filename,data):
    dumped_json = json.dumps(data,indent=True)
    log("Writing json\n {} to {}".format(dumped_json, filename))
    #Make a backup copy, just in case something bad happens while writing
    try:
        open(filename+'.backup','w+').write(open(filename,'r').read())
    except FileNotFoundError:
        pass
        #of course, we can't really do that if the file doesn't yet exist.
    open(filename,'w+').write(dumped_json)
    log("Write complete.")

##############Filesystem helper functions###########
CWD = os.getcwd() + '/'

# def archive_source(url,location):
#     save_webpage(url='http://example-site.com/index.html',download_loc='path/to/downloads')

##############Settings helper functions#############

#This should try to retrieve the settings dictionary from the configured file.
#If the file does not exist, it should attempt to create it.
#Other errors are just propagated out.
def get_settings():
    try:
        loaded_json = load_json(hargrave_conf.SETTINGS_FILE)
        return loaded_json
    except FileNotFoundError:
        initialize_settings()
        loaded_json = load_json(hargrave_conf.SETTINGS_FILE)
        return loaded_json

def write_settings(new_settings_dict):
    write_json(hargrave_conf.SETTINGS_FILE, new_settings_dict)

def initialize_settings():
    defaults = {}
    defaults["organization_name"] = "Daniel's"
    defaults["style_blurb"] = "You're talking to future you."
    defaults['users'] = ["0xDBFB7"]
    defaults['default_root_directories'] = ['sources','media','hardware','firmware','software','mechanical']
    defaults['project_rel_archive_dir'] = 'sources'
    defaults['default_project_categories'] = ['Flagship', 'Technique', 'Learning']
    log("initializing settings")
    write_settings(defaults)



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
    root_json = load_json(hargrave_conf.ROOT_JSON_FILE)

    if(root_json and 'projects' in root_json.keys()):
        projects = root_json['projects']
    else:
        projects = []

    return render_template('index.html',ORG_NAME=hargrave_conf.ORG_NAME,
                                        projects=projects)


@app.route('/new_project',methods=['GET', 'POST'])
def new_project():
    if request.method == 'POST':
        log(request.form)

        if(not request.form.get("project_id")):
            return json.dumps({"success":0,"alert_message":"You haven't entered a project id."})

        if(not request.form.get("display_name")):
            return json.dumps({"success":0,"alert_message":"You haven't entered a display name."})

        if(not request.form.get("start_date")):
            return json.dumps({"success":0,"alert_message":"You haven't entered a start date."})

        if(not request.form.get("display_name")):
            return json.dumps({"success":0,"alert_message":"You haven't set the author."})

        root_json = load_json(hargrave_conf.ROOT_JSON_FILE)

        #Some root json file sanity checking
        if(not root_json):
            root_json = {}
        if(not 'projects' in root_json.keys()):
            root_json['projects'] = []

        if([x for x in root_json["projects"] if x['project_id']]):
            return json.dumps({"success":0,"alert_message":"That project ID already exists."})

        #Write the new project to disk.
        project = {}
        #All written timestamps are unix epochs, purely because I happen to like unix time.
        project['start_date'] = datetime.strptime(request.form.get("start_date"),'%Y-%m-%d %I:%M %p').strftime("%s")
        project['creation_date'] = time.time()
        project['display_name'] = request.form.get('display_name')
        project['project_id'] = request.form.get('project_id')

        root_json['projects'].append(project)

        write_json(hargrave_conf.ROOT_JSON_FILE,root_json)

        subprocess.call(["xdg-open", hargrave_conf.ROOT_PROJECT_DIR])

        return json.dumps({"success":1,"project_id":request.form.get("project_id")})

    return render_template('new_project.html', USERS=hargrave_conf.USERS)


@app.route('/project',methods=['GET', 'POST'])
def project():
    return render_template('project.html', USERS=hargrave_conf.USERS)
