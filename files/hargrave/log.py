import logging
import hargrave_conf

logging.basicConfig(filename=hargrave_conf.LOG_FILE,level=logging.DEBUG)

def log(message):
    logging.debug(message)
