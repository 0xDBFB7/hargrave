from boilerplate import *
import hargrave_types

def call_type(name):
    return getattr(hargrave_types, name)()

def render_template(template):

    debug(template)
    for section in template.sections()[1:]:
        output(section, end="<br>")
        output(template[section], end="<br>")
        type_obj = call_type(template[section]["type"])
        output(type_obj.render(), end="<br>")

        # for key in config[section].keys():
