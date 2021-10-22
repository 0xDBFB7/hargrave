# ROOT_JSON_FILE = '/home/arthurdent/NAS/primary_a/Projects/hargrave/data/test_hargrave_folder/root.json'
# PROJECTS_DIR='/home/arthurdent/NAS/primary_a/Projects/hargrave/data/test_hargrave_folder/'
import os
# CWD = os.path.curdir 
HARGRAVE_ROOT = "/home/arthurdent/Projects/hargrave/"
CWD = "/home/arthurdent/Projects/hargrave/hargrave_base/backend/"

FRONTEND_DIR = "../frontend/"

STANDARDS_DIR = "../../hargrave_standards/"

# where large folders are persisted.
MANAGED_STORAGE_DIR = "../../hargrave_managed_storage/"
LOG_FILE = MANAGED_STORAGE_DIR+'run/hargrave_log.log'

DATABASE_URL = f"sqlite:///{HARGRAVE_ROOT}/test.db"
