import configparser

import importlib


def return_standard_structure(standard_file):
    config = configparser.ConfigParser()
    with open(standard_file) as f:
        config.read_file(f)

    return config


def import_standard_handler():
    i = importlib.import_module("hargrave_standards.")
