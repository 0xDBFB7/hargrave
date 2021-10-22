
from . import hargrave_conf
from hargrave_base import app
from . import imports
from flask import (request, redirect, url_for, session,
                   render_template,abort,send_from_directory)

from hargrave_base.standard.render_standard import *

import os

# from flask_autoindex import AutoIndex
# AutoIndex(app, browse_root=hargrave_conf.CWD + hargrave_conf.STANDARDS_DIR)


@app.route('/standards', strict_slashes=False, defaults={'path': "/"})
@app.route('/standards/<path:path>')
def send_standard(path):
    if path.endswith('/'):
        list_of_files = []
        for filename in os.listdir(hargrave_conf.CWD + hargrave_conf.STANDARDS_DIR + path):
            list_of_files.append([f"<a href=/standards/{path + filename}>{path + filename}</a>"])

        table = render_template('table.html',header = ["Standards"], items=list_of_files)
        return render_template('index.html',body=table)
        # return send_from_directory(hargrave_conf.STANDARDS_DIR, path)
        return list_of_files
    else:
        return render_standard(hargrave_conf.CWD + hargrave_conf.STANDARDS_DIR + path)
        # return send_from_directory(hargrave_conf.STANDARDS_DIR, path)


