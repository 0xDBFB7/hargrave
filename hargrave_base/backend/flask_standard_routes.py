
from hargrave_flask_app import app

from flask_autoindex import AutoIndex

AutoIndex(app, browse_root=os.path.curdir)

@app.route('/standards/<path:path>')
def send_css(path):
    return send_from_directory(hargrave_conf.STANDARDS_DIR + '/css', path)
