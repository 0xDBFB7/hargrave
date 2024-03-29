![](/kite_1.png)

Hargrave is a way to improve the quality of my research by
- imposing a slight schema restriction on my notes
- integrating equations and PDF sources into proper technical reports
- saving the endless tedium of shifting files around.
- making it easier to disseminate my findings.

As of this writing, I have a total of 60 project folders consuming ~1.5 Tb, ranging in duration from quick, one-day experiments to rigorous half-decade "flagship" projects.

Handling all these projects and notes with just a file browser and text editor is becoming quite onerous. In addition, my note quality is quite poor; images of phenomena are not linked to experiment parameters; etc.

Version control, however, is currently managed superbly via Git; in the interest of not reinventing the wheel, I figured whatever I came up with should probably be compatible with git diffs.

Hargrave is inspired greatly by [ELOG](https://elog.psi.ch/elog/).

ELOG is very nearly what I wanted; however, I like working "in-place" on files, and wanted a
specific directory structure as to project files, folders, and sources.

### Security disclaimer

Hargrave uses Apache's SSL user certificate functionality for login; a CA is created locally and used to generate signed user certs in order to authenticate browsers.

Anyone who can access Hargrave immediately obtains full write permissions to the host filesystem.

If you're going to use this, make sure that the http port in question is firewalled and inaccessible externally. If you want to publish a read-only copy, I recommend you set up a physically separate server (a GCE VM, in my case).

### The name


### My requirements:

- [x] Configurable auto-generated project directory structure
- [ ] Plays well with gitignore
- [ ] "process steps" entry, with custom per-experiment parameters and rigid schema
- [ ] Adds and removes images from media/ from gitignore as desired (and as size allows)
- [ ] "file link" procedure - link project description to README, say
- [ ] Special /documents directory?
- [ ] *all human-readable flat files* for ease of debugging. No database besides json files - this'll make version control a little more manageable.
- [ ] read-only mode for publicizing results
- [ ] "charts" of data - feeds and speeds per material, for instance - custom attributes?
- [ ] some way of categorizing and timestamping images in media/
- [ ] "checkout" function, to get a local copy of a project from a server
- [ ] support for encrypted projects
- [ ] Archive function for urls and sources, so that project logs are fully self-contained
- [ ] media/ directory structure that works well with moviepy
- [ ] Backup function
- [ ] Gitlab integration?
- [ ] Server portion that can host project pages
- [ ] accepts any size of file
- [ ] works "in-place" on files
- [ ] drops a symlink wherever you want
- [ ] custom "test attributes" - custom values like voltage, current, etc to enter per test?
- [ ] Login using a custom CA and user certs
- [ ] when a project is set to public, switches all source links from internal archive to external links for copyright reasons
- [ ] "pinned project" at homepage
- [ ] Project ordering selectable - frequently or recently accessed.
- [ ] inline latex to html/png
- [ ] ~~SSH compatible?~~ No longer required - cert pinning deals with this just fine.
- [ ] ~~android app integration for science on-the-go?~~ Using certs obviates the need for this.
- [ ] Chrome extension for quickly adding references?
- [ ] "copy process" button
- [ ] BibTeX integration.

How can we log cases where a parameter or variable is not known with certainty?
We don't want to promote assumption of correct values, which might happen
if we just have a key/value...Ooh, pop-up footnotes associated with variables!
How it was measured, what questionable features this variable might have, etc.

Oh, we should also have a way to copy sources from one project to another.
