                   
from flask import Flask
app = Flask(__name__,template_folder="frontend", static_url_path="/frontend")
app.debug = True

# from .backend import hargrave_conf
from .backend.flask_standard_routes import *
from .backend.backend import *
from .backend.flask_static_routes import *
from .backend.log import *