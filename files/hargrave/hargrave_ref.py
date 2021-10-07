import json
import hargrave_conf
import os
from log import *

import pybtex.database

def log(message):
    logging.debug(message)

def add_reference(form_dict):

    i000f(form_dict["raw_bibtex"]):
        bib_data = pybtex.parse_string(form_dict["raw_bibtex"], 'bibtex')
