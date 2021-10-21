

## Overall goals

Suits every topology:

Standalone within a project, server, 


why a database over simply markdown text?

clean question and answer format
programmatic access

sometimes you'll want to put text in multiple places


## Standards config language

config language versus python class because reload might be easier

bioGUI uses XML. Pretty reasonable decision.

ConfigParser 

restructured text has a nice "custom directive" module, specifying "arguments", that might be useful for this purpose
https://docutils.sourceforge.io/docs/howto/rst-directives.html
however there seems to be only minimal support for exporting
https://github.com/sphinx-contrib/restbuilder


HCL does not allow multiline strings.

yaml is bad

yaml also needs indents for blocks 

hdf5 for standard files? allows images to be baked into a single file?