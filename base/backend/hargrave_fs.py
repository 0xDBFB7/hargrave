################JSON import and helper functions########
import json
import hargrave_conf
import os
from log import *


def log(message):
    logging.debug(message)



#So, what's required in the root-level project json?
#Timestamps and author and stuff should be in the per-project json,
#since otherwise you wouldn't be able to just send someone the project folder.
#We want projects to be almost entirely self-contained for ease of sharing.

