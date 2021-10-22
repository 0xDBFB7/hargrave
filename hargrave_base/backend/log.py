
from . import hargrave_conf

import logging

logging.basicConfig(filename=hargrave_conf.CWD + hargrave_conf.LOG_FILE,level=logging.DEBUG)

def log(message):
    logging.debug(message)
