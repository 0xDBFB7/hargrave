
from hargrave_base import app
from . import hargrave_conf
from .log import log

from flask import (request, redirect, url_for, session,
                   render_template,abort,send_from_directory)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(hargrave_conf.CWD + hargrave_conf.FRONTEND_DIR + '/js', path)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory(hargrave_conf.CWD + hargrave_conf.FRONTEND_DIR + '/images', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(hargrave_conf.CWD + hargrave_conf.FRONTEND_DIR + '/css', path)
