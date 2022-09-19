#!/home/arthurdent/Programs/miniconda/bin/python

import cgi
import cgitb
cgitb.enable()


open('run.log', 'r+').truncate(0)
# for some reason, w+ or w doesn't work here.
import logging
logging.basicConfig(filename='run.log', filemode='a', level=logging.DEBUG, format='%(message)s')

from boilerplate import *



output ('Content-Type: text/html')
output ('\n')



import os

import configparser
import collections
config = configparser.ConfigParser({}, collections.OrderedDict)


arguments = cgi.FieldStorage()




import hargrave_types
from hargrave import *



TEMPLATE_DIR = './'
template_path = TEMPLATE_DIR + os.environ['PATH_INFO']

config.read_file(open(template_path))

render_template(config)


# print("<TITLE>CGI script output</TITLE>")
# print("<H1>This is my first CGI script</H1>")
# print("Hello, world!")

debug("test")
# item = form.getvalue("item")
