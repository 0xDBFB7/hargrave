
from hargrave_flask_app import app


##################Serve the index page#############
@app.route('/')
def index():
    root_json = hargrave_fs.get_root_json()
    return render_template('index.html',settings=root_json["settings"],
            projects=sorted(root_json["projects"],key=lambda k: k['opened_count']))

