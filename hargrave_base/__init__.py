                   
from flask import Flask
app = Flask(__name__,template_folder="frontend", static_url_path="/frontend")
app.debug = True

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from .backend.hargrave_conf import DATABASE_URL

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

# from .backend import hargrave_conf
from .backend.flask_standard_routes import *
from .backend.instance import *
from .backend.flask_static_routes import *
from .backend.log import *