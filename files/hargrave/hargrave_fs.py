################JSON import and helper functions########
import json
import hargrave_conf
import os
from log import *

def log(message):
    logging.debug(message)

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

############Root JSON helper functions########
#This should try to retrieve the settings dictionary from the configured file.
#If the file does not exist, it should attempt to create it.
#Other errors are just propagated out.

#This stuff is nearly duplicated from above - not particularly clean.
#I'll fix that once I figure out how exactly project nesting should work.
def get_root_json():
    try:
        loaded_json = load_json(hargrave_conf.ROOT_JSON_FILE)
        return loaded_json
    except FileNotFoundError:
        initialize_root_json()
        loaded_json = load_json(hargrave_conf.ROOT_JSON_FILE)
        return loaded_json

def write_root_json(new_dict):
    write_json(hargrave_conf.ROOT_JSON_FILE, new_dict)

#So, what's required in the root-level project json?
#Timestamps and author and stuff should be in the per-project json,
#since otherwise you wouldn't be able to just send someone the project folder.
#We want projects to be almost entirely self-contained for ease of sharing.

def initialize_root_json():
    defaults = {}
    defaults["settings"] = {}
    defaults["settings"]["organization_name"] = "Daniel's"
    defaults["settings"]["style_blurb"] = "You're talking to future you."
    defaults["settings"]['users'] = ["0xDBFB7"]
    defaults["settings"]['default_directories'] = ['sources/','media/','hardware/','firmware/','software/','mechanical/']
    defaults["settings"]['project_rel_archive_dir'] = 'sources/'
    defaults["settings"]['default_project_categories'] = ['Flagship', 'Technique', 'Learning']
    defaults["projects"] = []
    log("initializing settings")
    write_root_json(defaults)

# def get_hierarchical_json(project=None):
#     """
#     In the future, nested "sub-projects" might be possible.
#     Currently, this only implements "root" project file access.
#
#     Some validation and key:value pair creation is also performed.
#     """
#     try:
#         hierarchical_json = load_json(get_settings()["root_json_file"])
#
#     if(not hierarchical_json):
#         hierarchical_json = {}
#     if(not 'projects' in root_json.keys()):
#         root_json['projects'] = []
#
