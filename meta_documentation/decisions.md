

## Overall goals

Suits every topology:

Standalone within a project, server, 


why a database over simply markdown text?

clean question and answer format
programmatic access

sometimes you'll want to put text in multiple places


## Why database



couchDB and couchapps - "document oriented databases" - look interesting for this application

https://h3rald.com/litestore/

oh, sqlite includes json types, neat

both sqlite and postgres include FTS

## Base language

Python because of the huge userbase. Julia was the runner-up; indeed there are some very clever tools like
https://github.com/GenieFramework/Genie.jl

## Standards config language

config language versus python class because reload might be easier

bioGUI uses XML. Pretty reasonable decision.

want to be machine-writeable in the future

restructured text has a nice "custom directive" module, specifying "arguments", that might be useful for this purpose
https://docutils.sourceforge.io/docs/howto/rst-directives.html
however there seems to be only minimal support for exporting
https://github.com/sphinx-contrib/restbuilder


HCL does not allow multiline strings.

imho yaml is pretty brittle. yaml also needs indents for blocks 

hdf5 for standard files? allows images to be baked into a single file?

tentatively decided on configparser.

## Superseding

clearly defining overwriting data is hard.
each column in a standard instance would need its own table!

I suppose this means that information needs to be more finely divided.
therefore perhaps the tables should relate to standards *and types*.
each standard instance FKs to a specified number of Type table, each of which has a superseded FK.

if I want to access a certain parameter programmatically, I want to get the latest one...


how do globally public literature reviews & indexes fit into all this 
do they go in *standards*?



## Meta quoting from within standards

okay, so now I've run into the first problem. I want to quote a NASA document on lessons learned from within a standard.
I can write this directly into the standard, 


zotero quotes are put in .rdf files like this:

<bib:Memo rdf:about="#item_8056">
    <z:itemType>note</z:itemType>