
from . import hargrave_conf
from hargrave_base import app
from . import imports
from flask import (request, redirect, url_for, session,
                   render_template,abort,send_from_directory)

import os

# from flask_autoindex import AutoIndex
# AutoIndex(app, browse_root=hargrave_conf.CWD + hargrave_conf.STANDARDS_DIR)


@app.route('/standards/', strict_slashes=False)
@app.route('/standards/<path:path>')
def send_standard(path):
    if path.endswith('/'):
        list_of_files = {}
        for filename in os.listdir(path):
            list_of_files[filename] = path + filename

        # return render_template('index.html',settings=root_json["settings"],
        #         projects=sorted(root_json["projects"],key=lambda k: k['opened_count']))
    else:
        return send_from_directory(hargrave_conf.STANDARDS_DIR, path)

