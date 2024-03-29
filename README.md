
## Hargrave: The Scientist's Scrapbook

Science, with Texture and Culture!

Is it possible to make an electronic lab notebook that intrinsically makes the user a better scientist? 

"standards framework"

# note: this is an experiment; I've no clue how useful this topology will be.

<!----


- Prompt- and form- based, rich, structured note taking.

Interdisiplinary; physical and experimental sciences, computational, but not clinical.

-->


# Arguably superior software and other things worth reading

An absolutely fantastic resource is https://www.limswiki.org/index.php/Book:LIMSpec_2019_R1

# https://openbis.ch/

possibly the most mature open source ELN-LIMS 

Pros

- customizable objects and form-like entry
- very mature; extensive use in .ch science
- powerful Python, Java, Javascript API
- 
https://github.com/aarpon/obit/tree/master
- really good doumentation
- 
Cons

- How can e.g. a Sympy-rich nomenclature be done? 
- no git interaction?
- not necessarily easy to do callbacks to run
- no provisions for "instrument drivers" - might have to be written in Java or go over Python API?
- java library integration
- Not necessarily designed for consensus of protocols in the sense of hargrave
- no provisions for 

# bioGUI https://peerj.com/articles/8111/

Most closely resembles this (although was discovered post!)

uses xml for the standards

Includes a global templates repository just like the one concieved here.


- https://github.com/open-lims/open-lims

similar user interface. appears to be very well developed 


- kexi microsoft access

# Buhos https://github.com/clbustos/buhos

Fills a slightly ddifferent niche: this is a systematic literature review tool



- LeafLIMS 

written in Python


Lua scripting


what are the norms of this field? do they need to be altered, how does this paper follow them

docker exec -it mystifying_meninsky bash

- renku

big one

- GNU Health

- https://openwetware.org/wiki/Main_Page

- SciNote

Almost every feature I could think of adding is already in SciNote.

- elabFTW

- Wagenaar Lab's ELN / NotedELN

- DrWatson

- Indigo ELN

- Some CERN 

- Galaxy Project

- Benchling
- A wiki. a great option.
- protocols.io
Not making the same mistake twice, or not, requires getting the right information from a vague idea 

- Whitequark's lab notebook
- eLabFTW
     elabftw's API is awesome.
- a google doc.
     one problem is that you tend to just append to the bottom 
     no sense of the certainty of a fact,
    old information is not replaced
- STAR methods
- Galaxy project
- stuff like [lab that bought ipad]
- that one lab's custom lab scrapbook
- that math wiki 
- Docear
- DistillerSR
- http://www.jesshamrick.com/2016/03/07/passing-quals/

> Different people prepare for quals in different ways. One of my labmates prepared by writing hand-written notes in many small notebooks and then scanning them. Another labmate made a handful of slides per paper. For me, I decided to write blog posts on each paper. This approach worked well for me because it forced me to digest each paper by writing a summary, and then to critically think about each paper by writing a “takeaways” section. For some of the papers, I even wrote a quick demo in the Jupyter notebook to help me understand the model or algorithm better.


- Notational Velocity.

https://git-blame.blogspot.com/

search should also include some kind of "category" or "semantic". for instance, I just wanted to note the
following sentence:

"One interesting change is to git help. We now list commands, grouped by the situation 
in which you would want to use them. This came from discussion on usability, 
inspired by one of the talks at GitMerge conference we had in spring."
()

I think that's pretty clever. Now, when I want to write a cli help in the future,
I want to be able to see what I thought was clever for some fuzzy collection involving "help",
without remembering 
Should also be a cross-project search. should also include software output logs
Notational Velocity might do this sometimes...


- F1000 
- MDPI *Standards*
- https://www.pnas.org/content/115/11/2590
- ORNL



- LabFolder 


Proprietary.


- EV-TRACK knowledgebase


https://www.bikalims.org/manual/introduction-and-overview/lims-page-lay-out

not my jam

# namesake

>  Workers must root out the idea [that] by keeping the results of their labours to themselves[,] a fortune will be assured to them. Patent fees are much wasted money.
>
>  The flying machine of the future will not be born fully fledged and capable of a flight for 1000 miles or so. Like everything else it must be evolved gradually. The first difficulty is to get a thing that will fly at all. When this is made, a full description should be published as an aid to others.
>
>  Excellence of design and workmanship will always defy competition.

[Lawrence Hargrave](https://en.wikipedia.org/wiki/Lawrence_Hargrave)'s occasionally-exaggerated contributions to powered flight are well summarized in *Lawrence Hargrave: Myth and Fact in Aeronautical History*. He is known for having kept [meticulous notes](https://collection.maas.museum/object/325754#&gid=1&pid=1). He was, of course, flawed.

<sub>(I'm open to adding a different person here!)</sub>




key ideas:

- wiki-like thing for literature reviews ?!?
- Standards used must first be agreed upon by a consensus system, a mailing list of experts in the field - a publication can change a protocol, or report on a finding, but not both - global repository for standards
- Global propagation and generalization of mistakes on every level. When one person makes a mistake, nobody should ever make it again, in any field
- Human factors in science


