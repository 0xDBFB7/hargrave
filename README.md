Hargrave is inspired greatly by [ELOG](https://elog.psi.ch/elog/).

ELOG is very nearly what I wanted; however, I like working "in-place" on files, and wanted a
specific directory structure as to project files, folders, and sources.

### Security disclaimer

Hargrave uses Apache's SSL user certificate functionality for login; a CA is created locally and used to generate signed user certs in order to authenticate browsers.

Anyone who can access Hargrave immediately obtains full write permissions to the server's drives.

If you're going to use this, make sure that the http port in question is firewalled and inaccessible externally. If you want to publish a read-only copy, I recommend you set up a physically separate server (a GCE VM, in my case).

### The name

[Lawrence Hargrave]( https://en.wikipedia.org/wiki/Lawrence_Hargrave) was a badass.

  Workers must root out the idea [that] by keeping the results of their labours to themselves[,] a fortune will be assured to them. Patent fees are much wasted money.

  The flying machine of the future will not be born fully fledged and capable of a flight for 1000 miles or so. Like everything else it must be evolved gradually. The first difficulty is to get a thing that will fly at all. When this is made, a full description should be published as an aid to others.

  Excellence of design and workmanship will always defy competition.

### My requirements:

- [ ] Configurable auto-generated project directory structure
- [ ] Plays well with gitignore
- [ ] "process steps" entry, with custom per-experiment parameters and rigid schema
- [ ] Adds and removes images from media/ from gitignore as desired (and as size allows)
- [ ] "file link" procedure - link project description to README, say
- [ ] SSH compatible?
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
- [ ] inline latex to html/png
- [ ] ~~android app integration?~~ Using certs obviates the need for this.
- [ ] "copy process" button
