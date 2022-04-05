https://ntrs.nasa.gov/api/citations/20170007238/downloads/20170007238.pdf

Topologies:

Follow section 6.8 Decision Analysis  in  Expanded Guidance for NASA SE

Feature matrix?

How do we deal with big flat files

Everything should be absolutely modular.

Pandoc to create html from Markdown blurbs (perhaps cache rendered html) with bibtex.
Or perhaps just direct mathjax

Say we want to link to multiple 

Side panes with rationale like plos one style - paragraph support links

How will schema be shared? In what format?

With a database, how would one define a beaker? 
Beaker should inherit 



sqlitebrowser works great

https://forums.zotero.org/discussion/87671/a-new-python-tool-kit-for-interacting-with-the-locally-hosted-zotero-database




Libreoffice Base as ELN:

linking to images works fine
each table schema ("process") is perhaps hard to share openly
no versioning of schemas

no way to run code to get instrument data
libreoffice base has python api

libreoffice has neat macro callbacks in the events tab of the form editor

actually, I like calligra Kexi better than LOB!
kexi is great; no automatic date insert 
kexi doesn't allow altering database columns after creation atm, which is painful - drwatson does this very well
the arrow-key back and forward 




https://en.m.wikipedia.org/wiki/IBM_3270 protocol is interesting because it's both thin client and server-rendered, but also info is transfereed amd updated live


natural history & museums are good sources of info on long term documentation

when referring to a sequential eqperument, series, etc, saying "latest" is fraught. Say the specific identifier!


A standards organization that figures out the best way to do things amd is funded by selling extremely accurate hardware



heroku hobby - $7 - ssl & certificate management, might be worth it
https://genieframework.github.io/Genie.jl/dev/tutorials/90--Deploying_With_Heroku_Buildpacks.html
no persistent storage beyond postgres


gollum solves the concurrent edits issue by locking the whole file and alerting if someone else changes it. wonder how openbis does it.

Nevertheless, we strongly believe that merely improving the engineering design and the procedural
sequence of the checklist will not eliminate the problem. The pilot is still the center of this task, and
the socio-technical environment in which he operates has a substantial effect on checklist performance, regardless of the type or method in use. Since the pilot is in control and will continue to be
so in the foreseeable future, accommodating the human strengths and limitations in conducting this
procedure should be at the heart of any checklist design. In short, checklists must be “humancentered.” It must be clearly understood by all parties involved in checklist design that if the individual captain chooses not to use the checklist for any reason, no one can force him to use it.




https://en.wikipedia.org/wiki/Outliner is literally what we want!!!!!

We use Leo to organize about 1000 puppet modules managing about 500 linux systems (50/50 real/virtual), of which 60% are "unique", a.k.a., pets, not cattle. Geppetto in Eclipse is the closest thing, but Geppetto only helps with puppet modules, not puppet nodes (hosts).
The good: Leo provides rapid access to understanding the complexity.

The bad: Leo XML file format is collaboration hostile, since resolving git conflicts in its multi-megabyte XML file is out of the question.

The ugly: I've got perl code to translate the XML file to and from a directory of several thousand small files, one per Leo node, and far more git-conflict friendly.

The worst: the version of Leo on which we're stuck used "sentinels" - specially formatted comments - to keep Leo's structure of the file in sync with external changes to the file. Never use that: use a new version of Leo and use its @clean format, which doesn't use sentinels. Not only are sentinels offensive to look at in the managed file, this version of Leo occasionally gets confused and tries to use "//" for puppet comments instead of "#". (Yes, some of what puppet (and thus Leo) is managing is php.) But we're stuck with this version of Leo, because when newer versions of Leo read our Leo XML file, many of the nodes lose their content, namely, a catastrophic lack of backward compatibility. It would take me at least a month of getting nothing else done to re-ingest our puppet configuration into a newer Leo.

https://news.ycombinator.com/item?id=17769892
https://news.ycombinator.com/item?id=17774932












https://github.com/vijithassar/lit-web


https://pycco-docs.github.io/pycco/



Adding columns to kexi

Kexi currently does not allow columns to be added.
however, there is a bash script that works around this:

https://websvn.kde.org/*checkout*/branches/koffice/1.6/koffice/kexi/tools/add_column/kexi_add_column

got a strange error in the chroot (covidinator/scripts/run_chroot.sh)), that 

/home/arthurdent/kexi_add_column.sh: 40: /home/arthurdent/kexi_add_column.sh: Syntax error: "}" unexpected
root@DeepThought-Ryzen-Debian:/# ls -la /bin/sh
lrwxrwxrwx 1 root root 4 Nov  8  2014 /bin/sh -> dash

called with bash



cool:

https://community.kde.org/Kexi/Plugins/Web_Forms



https://github.com/drivendataorg/deon



both template and thing should be YAML.

Not every implementation of YAML has every specification-defined data type. These built-in types use a double-exclamation sigil prefix (!!). Particularly interesting ones not shown here are sets, ordered maps, timestamps, and hexadecimal. Here's an example of base64-encoded binary data.

---
picture: !!binary |
  R0lGODdhDQAIAIAAAAAAANn
  Z2SwAAAAADQAIAAACF4SDGQ
  ar3xxbJ9p0qa7R0YxwzaFME
  1IAADs=
Many implementations of YAML can support user-defined data types for object serialization. Local data types are not universal data types but are defined in the application using the YAML parser library. Local data types use a single exclamation mark (!).

---
myObject: !myClass { name: Joe, age: 15 }

https://stackoverflow.com/questions/43058050/creating-custom-tag-in-pyyaml