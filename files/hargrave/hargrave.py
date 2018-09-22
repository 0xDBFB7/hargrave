
import hargrave_conf

##################Logging stuff!################
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

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
    try:
        return json.loads(open(filename).read())
    except:
        log("Root json file blank.")

def write_json(filename):
    dumped_json = json.dumps(filename,indent=True)
    #Make a backup copy, just in case something bad happens while writing
    open(filename+'.backup','w+').write(open(filename).read())
    open(filename,'w+').write(dumped_json)

##############Filesystem helper functions###########
from shutil import copy
import os
# def archive_source(url,location):
#     save_webpage(url='http://example-site.com/index.html',download_loc='path/to/downloads')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('template/js', path)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('template/images', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('template/css', path)


@app.route('/')
def index():
    root_json = load_json(hargrave_conf.ROOT_JSON_FILE)

    if(root_json and 'projects' in root_json.keys()):
        projects = root_json['projects']
    else:
        projects = []

    return render_template('index.html',ORG_NAME=hargrave_conf.ORG_NAME,
                                        projects=projects)

@app.route('/new_project')
def new_project():
    return render_template('new_project.html')

@app.route('/page')
def hello():
    return 'Hello, World'
