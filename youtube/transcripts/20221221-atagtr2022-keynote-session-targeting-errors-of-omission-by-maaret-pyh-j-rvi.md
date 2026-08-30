---
title: "#ATAGTR2022:Keynote Session - 'Targeting Errors of Omission' by Maaret Pyhäjärvi"
video_id: L1QsUXQhiMs
url: https://www.youtube.com/watch?v=L1QsUXQhiMs
upload_date: 20221221
duration: 51:36
channel: Agile Testing Alliance
tags: []
---

# #ATAGTR2022:Keynote Session - "Targeting Errors of Omission" by Maaret Pyhäjärvi

> #Keynote Session by Maaret Pyhäjärvi, "Targeting Errors of Omission" at #ATAGTR2022.
> 
> To know more about Maaret and her session,  please see the following URL:
> https://gtr.agiletestingalliance.org/maaret-pyhajarvi
> 
> The #ATAGTR2022:
> It was the 7th Edition of “Global Testing Retreat” happened on 10-11 December 2022. It was a 2 day #Virtual #Conference
> 
> 60+ #Speakers
> 4 parallel tracks
> 2 Panel Discussions 
> 5 #Keynotes 
> 38 #Interactive Sessions 
> 
> For more info about the Global Conference, please check: https://gtr.agiletestingalliance.org/
> 
> The Organizers:
> Agile Testing Alliance (ATA): https://agiletestingalliance.org/ 
> DevOps++ Alliance: https://devopsppalliance.org/  and
> International Institute Of Information Technology (I²IT): https://www.isquareit.edu.in/ 
> 
> Linked In: https://www.linkedin.com/company/agile-testing-alliance/ 
> Twitter (ATA):https://twitter.com/AgileTAlliance 
> Facebook: https://www.facebook.com/AgileTestingAlliance 
> Instagram: https://www.instagram.com/agiletestingalliance/ 
> Twitter (ATAGTR): https://twitter.com/TestingRetreat
> 
> To know more about the upcoming events, please visit: https://ataevents.org/

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

foreign
[Music]
speaker to build
before I go ahead with an introduction
just allow me a minute just check if
she's been out
I am here
okay hi marriage
thank you
okay
marriage is a principal test engineer at
Bessler she is a exploratory tester it's
somewhere and she had been awarded with
two prestigious Global testing Awards
the most influential agile testing
professional person 2016 and Eurostar
testing Excellence award and selected as
the top most influential in ICT in
Finland and as I'm already aware that
she comes with 25 years of experience
more than 25 years of experience and she
has taken more than 400
sessions in across uh more than 25
countries am I right welcome on board uh
marriage and it is great to have you as
a keynote speaker today
she'll be speaking to us uh on topic
targeting errors on commission
over to you marriage stage is all yours
hopefully you now see my screen and
everything is fine in that sense
sorry
just set things up a little bit more now
should be
better for me so
it's an early morning for me especially
when I'm always oriented in the idea of
Saturdays are days off and I'm still
very happy to be here with you because
all of these uh agile testing Alliance
Global testing
Retreat days they they feel like a place
where I'm always coming home it's an
enthusiastic Community a lot of
conversation a lot of kind of you know
ideas pinging back and forth in the
channels and it is you know even if if
I'm feeling a little tired sometimes it
is very energizing to see how engaged
this community is so with that sentiment
I think it's a very great honor for me
to have this this moment of uh speaking
to you all on on the idea of uh areas of
a mission so just looking at the kind of
the description that there was just a
moment ago on me uh I realized looking
at it something that I of course see
because of knowing what I should have
written there is that it's clearly two
years old I think this is now my Talk
number
510 so in a few years there's been more
than 100 extra talks I have only covered
three new countries since I have written
that text and uh around some of the the
awards or recognitions they still
consider me one of the top hundred
influential in Finland not only in 99
2000 but also in 2000 uh two uh well
2022 I mean which is this this current
year so it was just coming out recently
that that they still consider that I am
doing something relevant at least in uh
in the context of my own on community
and on country
uh it's really easy to kind of you know
see people who are visible and and it's
easy to see problems that are visible
but it's not always easy to see people
or particularly see problems that we
didn't expect to be looking for and a
lot of times for us as testers one of
the core problems we have is that we are
expected to somehow make sense of the
world make sense of the applications in
a way that we also see things that no
one else sees
uh this is this General saying of you
know testers we don't break software we
break illusions of people uh and I would
love to think that everyone in the world
is breaking Illusions around the things
that we expect of software quality that
it's no longer testers who test but it
is everyone who tests and that testing
is way too important to be left just for
the testers but I still feel like uh
even with all of us in agile teams doing
our very very best on the quality and
seeing all of the things we need to have
a conversation on there are still things
that require Focus thinking Focus time
in in just considering what's going on
what's going on uh uh so that uh the the
general capability or the the uh time
the testers particularly invest in this
type of information still brings in
extra value
uh when we talk about errors of omission
uh what I kind of
sorry this is not working the my thing
no it works uh so uh what I I kind of
look at is is that uh sometimes you know
some of my managers have told me things
like this
uh you have a colleague there uh maybe
even naming the colleague and they're
working you know through so many tests
today like you know they get 28 tests
covered every day and it seems like
Martha you are so slow
you're so slow because you know like
you've only marked one test completely
today and only two tests completed
yesterday and especially in the earlier
days of my career this was a
conversation I needed to have a lot more
that I need to have these days that when
we're turning things into numbers people
are looking at those numbers as in
comparison and then we need to have the
conversation of What's missing
what happened with uh the the manager in
those days is is kind of and the
colleague that I was compared to was
this basic idea that you know sometimes
you work with systems where error
messages are frequent uh this is a
picture from one of those projects where
error messages back in the days for me
uh was very frequent and uh inter in
terms of
seeing big visible error messages if
that is way too easy to do or very easy
to do you don't actually have to
necessarily cover much of the ground in
terms of of how many tests you're
running we are just basically using all
of your time and just getting the system
up and running and Reporting how many
different problems you're seeing and
there might be these big visible error
messages but when you get away from this
big visible error messages and the
quality of the the system improves then
you actually have to figure out how to
do the testing so that the only thing
you're looking for is not this big
visible error messages so looking at
kind of what was I doing versus what was
my colleague doing uh we were doing back
in those days we were doing installation
testing and I had a very kind of like
versatile theory of what does an error
look like that I would look for I would
compare uh side by side the files and
make sure that the right files were
updating I was looking at features that
were supposed to be new that they were
actually present after installation
making sure that everything in the
installation worked as I would expect
also for the latest version whereas my
colleague had chosen that since we are
doing installation testing uh basically
what we do is is running an installation
seeing if there's any visible error
messages and then running forward so not
really looking for anything other than
obvious and this was an inspiration to
me in the sense that you know we have
very different things inside our heads
as testers we're looking for for very
different things and and generally what
I find myself looking for is kind of
What's missing
so the errors of a mission you know uh
already as a title it kind of means that
I am saying something must be missing
here so you can now kind of look at this
and you can write maybe for honesty and
and openness purposes you can write in
the chat uh what you think is missing
here uh uh you have four numbers uh
something clearly is is not there in the
white space in the empty space that we
have in between
uh it might be that the arrow that I
point there into the middle uh it you
know it kind of leaves our ideas into
saying let's you know just pinpoint and
focus here but as testers you know it
might be also that there's missing
things on the right hand side or on the
left side of this
the this this image or the the numbers
that I've I've written down here and uh
obviously kind of like you know it's
easy to jump to conclusions so we can
very easily think that what's missing in
between is one number because one two
four five it almost screams to all of us
that the number three is is missing in
between but actually what I was trying
uh to illustrate with this is that you
know we're looking at the clock we're
looking at the time and we need the uh
whatever a divider into a clock and uh
maybe that is what we had missed
in the in the center so if we have no
requirements how are we supposed to know
what's there so we can generate this
versatile way of versatile ideas of what
we are putting in in between these two
sets of numbers uh but also uh we need
to start those conversations of is this
what uh we're missing is this still
relevant and the world around us kind of
like understanding what's the context of
the problem we are trying to find uh
conversations on I try nowadays to avoid
the word bug very often because I feel
like everything that could bug a user
that's a bug but what is actually the
impact of a bug or a thing that we would
call as testers bugs is that we need to
start a conversation and the
conversations very rarely are best
started by writing a report and then
running away their rather conversations
where where we as testers are supposed
to be present and have a dialogue kind
of like Ping Pong back and forth on the
understanding and and share more of the
context from why are we bringing out
these type of of conversations
so we look for things to start the
conversation on we look from a versatile
set of ideas on how we would have these
conversations and it's not an easy job
the job that we try to do it's kind of
like steganography here like you have
invisible ink you've written things
uh with invisible ink and you have an
empty paper that you're looking at and
then you're wondering like why would
anyone give us this empty paper and you
need some kind of a mechanism maybe it's
ultraviolet light for for invisible ink
or maybe it is uh uh lemon juice that
you need to put on top of the paper for
for physical invisible ink but in terms
of testing like you can think of it as
it like we have this listing of problems
listing of conversations we haven't yet
had with our teams and no one can give
us a complete list of those
conversations that we need to have
but we have that paper that invisible
ink filled paper and we need to build
the tools in order to make that
invisible ink visible with the tools
meaning it's us being the tools it's us
building tools for us as testers to be
better and make the the bugs the
conversations that's visible
uh I've been doing this exercise with a
lot of groups recently uh where I take a
very small program it's called e-primer
it's been created by evil tester uh Alan
Richardson in in UK and uh what I like
about that particular problem is that I
know I used to say Catch-22 I know of 22
problems nowadays I know of 24 problems
so it's not now catch 24 but I had that
paper with invisible ink that I can
start with and I can visualize the end
result that we have in testing making
all those conversations visible I've
made hundreds of people do that little
exercise and I've noticed a pattern in
how we do that particular exercise we
are usually able to reveal between uh
two and eight problems before we are
calling it done
so very small percentage of the
conversations I would expect us to have
to turn that invisible invisible are
being had out of the experience that
people with a tester background with a
tested job even long-term jobs in
testing are doing and this has led me
into kind of realizing that we still
have generally a very big need in
teaching and training ourselves in the
ways that we turn the bugs the problems
the conversations visible and and make
them happen in our projects
so an important thing
the invisible ink I think of it kind of
like you know in terms of simple term
simple Concepts I think of it as uh our
job is to find something that the others
may have missed and since testing was
too important to be done just by testers
it's something that everyone must
nowadays in in agile projects in
particular well any projects must
participate
we need
a way of of bringing out those
information those pieces of information
that we don't yet have
so in order to find some of what others
may have missed I'm trying to kind of
illustrate it with this kind of of
Concepts
if we are looking at a project that we
think is successful particularly
successful in terms of having the right
conversations having them at the right
time with the right kind of cost having
all of our stakeholders happy delivering
on schedule delivering on the scope that
we are understanding not maybe what
someone is wishing for not something
that someone is requiring because asking
is cheap delivering is where the the
expensive work needs to be done but
having that level of kind of like good
quality solid quality information where
your stakeholders are happy they're even
maybe delighted of of how well you're
keeping your promises how well your
promises of of delighting people rather
than giving them problems are happening
uh this is the level we generally would
Target
uh anything underneath this that's the
listing of what I now call bugs
invisible ink something we need to make
visible
I find myself often working in teams
nowadays uh with teams where uh I would
call it maybe a good team's output like
the quality information is quite nice
already uh we feel like developers are
already doing a decent job in in testing
themselves there's a heavy emphasis on
on automating and documenting
with automation while we're building the
the applications uh uh there's testers
in these teams generally I am in these
teams as well uh working with the the
teams and uh we are able as a team to
produce a fairly decent level of quality
but you can still see that I've drawn
this this Gap here and I've drawn this
Gap results Gap here to kind of
illustrate how my work feels in these
kind of teams as a tester in that team
it's not like I would be jumping to
write a buck report or jumping to have a
conversation every single day I don't
have to manage long lists of bugs
I get to work in a space where the
starting point of my day is that on a
list of bugs we have zero bugs because
we have a zero Buck principle whenever
we find a bug we fix it we address is it
we do the the necessary
actions even if it came from the
production
and and we have a general rule of
whenever it grows over 20. uh even
coming out from millions of users we've
had these rules in place that it can
never go above 20 or we have a stop the
line principle where the entire team
will work on getting the number again
very close or at zero
but instead of jumping at every single
thing coming from from customers where
some of them are are sometimes kind of
like you know understanding mistakes as
well uh we we have used this number 20
uh where where we have this the stop the
line principle because that's clearly
when the entire team for us has needed
to jump on it but my sense of things
when I find things in in this space is
that there's a surprise it's it's a
surprise that I even need to find many
of the things and if you were measuring
as a manager if my managers were
measuring me
in terms of how many bugs I find or how
many test cases I complete they would
generally be very disappointed in me
because uh sometimes well actually a lot
of times it takes me a significant
amount of time to think in terms of how
we use the software what kind of
conversations do we need to have with
the team before I can report the bug
because I've been working so hard with
the team on having the conversations
early on but there is still this Gap and
I absolutely love working in teams where
the level of of of quality is this and
most of the bugs that I have to then
find are what I would call errors of a
mission something we didn't even think
about having a conversation on but it
came to my mind because I had the
permission to use all of my mind energy
G
excitement energy and and focus on on
figuring out what is still that
information that we might be missing
what might be included in that results
Gap digging in deeper in the uh the uh
integration or or uh
intertwining of multiple functionalities
and and seeing uh realistic scenarios uh
that we could see in production that
could surprise us and they generally do
so working in these teams
uh most of my work is actually errors of
a mission
however uh in visala for the last two
and a half years that I've spent here
it's not like all of my teams are
actually like this so I wanted to kind
of have a bit of a reality check on that
side some of the teams that we still
work with in the industry might be teams
with less than good uh output and the
quality information of why we think
we're still doing sort of well is that
when we look the other way or when we
close our eyes
it is easy to think that things are
working until we look at them and we see
that they're not working
uh having a team like this as a tester
to serve and and to grow I sometimes
feel like the bigger results Gap that I
need to experience there is that it it's
a result from the idea that team is
still thinking in terms of the the kind
of old world uh testers are doing the
testing uh we are always kind of you
know leaving the work for the testers so
the developers don't know the general
quality because it's tester's job to
tell about the quality and telling is
not the same as trying to experience it
yourself
and from the point of view of me being
in those teams as a tester it sometimes
feels like yeah I'm a person who picks
up pizza boxes
pizza boxes in the sense that uh uh it's
kind of like you know going into a
living room after having had dinner and
and you know pointing out that the pizza
box that is in the middle of the living
room floor and reminding that yeah we
need to actually take that to trash take
that to trash and that's not really the
work that I'm I'm looking for so in
order for you to have the energy and the
focus to really seek for complicated
errors of a mission you can't actually
be in a team where your work is to pick
up the pizza boxes and and point those
out uh but first like Anna bike is often
seems to be saying or have said uh in
the past at least is is that sometimes
as a tester your first job to do is to
fix the organization so that you can
even do the job that you originally
joined to do so for me ending up in a
pizza box team sometimes the best thing
for me is is to leave I did that with
one of the themes that I've been working
for in in the last two a half years I
probably will go back after they have
now again owned development and testing
without having any testers in that
particular team
but they needed to do the Baseline work
of learning to test as a team before
they could benefit from really having a
tester that works on the on the higher
level
so to make these things visible I you
often end up having conversations around
test coverage uh test coverage I use
usually a conversation model of one two
and three so the primary thing I want to
have a conversation on is is this one
the results Gap the results how far are
we in terms of results how much of that
invisible ink do we need to still make
visible but since no one can tell us
what's written on that white 84 pay A4
paper
uh it's really hard for us uh also to
talk in terms of results so it's taken
me a lot of practice to get to an idea
where you know I can just start that we
can assume there needs to be you know I
can just say out of the cuff 80
conversations in the next month or maybe
10 conversations in the next month I
have usually some kind of an idea I can
see what the conversations are but I can
talk about my progress in terms of how
my understanding towards that coverage
of unveiling the information goes and
and again doing mostly uh work in the
context of exploratory testing
automation is included in that
perspective for me
starting from kind of what is the the
thing that I'm about to reveal and and
just having my own way of talking about
percentage of how far am I with this
this this uh plan that I don't want to
write out in detail in advance it's the
the best way for for a making space of
of talking about the coverage that
really really matters
the second level the number two uh comes
to the idea
that we want in order to support this
invisibility we want also to have some
ways that are less invisible
they might not be as good in describing
the scope of the work and giving a good
percentage number to our managers and
our colleagues in in terms of talking
about how far are we in in terms of the
work but they give us a good
approximation so having those
conversations around code coverage
requirements coverage they are at least
things we can calculate and for me
knowing the for a general fact by
measuring nowadays that out of uh the
requirements that we have co-created
with the team and the management product
management people that we have working
with the team usually uh my best with
the team ends up with 80 percent of the
requirements visible before that stage
of of actually spending time with the
product as my external imagination and
because becoming more creative that 20
extra it's giving me a lot more tangible
way of talking about how much work on
top of all those requirements there is
and also on the the time that I might
need
uh in the team in order for us to reveal
all of that information so again a
starter of conversations uh getting
numbers of code coverage getting numbers
of requirements coverage a definite
practice I tend to be using in in pretty
much all of the projects that I work on
sorry the third number one two and three
is then three coverages that remind me
to extend this a little bit further
remembering that there's not just a
single environment it might be that
you're doing a system that is Windows
and Linux it might be that you're doing
a system that is all kinds of browsers
not just Chrome it might be that you're
doing an embedded system that runs on
embedded Linux on that particular set of
Hardware but even the hardware in your
environment is getting new generations
and needs to be considered a new
environment in terms of of uh
testing of that
of that particular uh system so having
different kinds of projects environments
is it's like a heuristic that generates
a perspective that I need to do
similarly data is is a perspective so
for every functionality I can try it
with many kinds of inputs I can try it
with many kinds of States I can try it
with with many kinds of configurations
and making actively changes uh even in
the same functionality with whatever
variables I'm able to control and
thinking data in terms of of multiple
dimensions and and having mechanisms to
talk about that very essential for
coverage and then of course remembering
that it's also a performance it's not
just using for once after it's been
installed in a CI pipeline it's
installed in my in my my test
environment automatically it's not just
testing there but it's also the
secondary environment where it can never
be automatically installed because it
needs to be uninterruptibly available
maybe for weeks maybe for months maybe
even sometimes you would like to try
simulating all the activity for years
without no reboots resulting
from installing a new system depending
on on the the kind of system you're
doing so performance usability
reliability security
testability interoperability whatever
parafunctional aspects you have you will
want to also dig into those levels when
when talking around coverage
so all of this it's kind of like uh
we're working with negative space we're
working with whatever is invisible and
just looking at this picture here uh
it's actually very clear what that uh
negative space includes sometimes like
if you look at for example for FedEx uh
trademark D or the uh the image uh the
logo uh noticing the arrow there
requires someone once pointing that this
logo actually uses negative space to uh
show kind of like progress in in form of
an arrow but in testing what we're doing
is often actually looking for when we're
looking for errors of emission and and
looking for that better coverage with
regards to results we are looking at
that negative space and trying to see
things there so I had a few things
kind of that I collected on how do I
actually uh try to do this this in
practice that I wanted to share with you
today
first of all uh
I find uh working with a lot of people
that we have uh generally I have
generally a tendency to confuse lung and
detailed uh with something where someone
did a good and solid work
two weeks ago one of my colleagues in my
team one of the developers created a
three a four page long listing
over how a particular feature was going
to be implemented and we got together as
a team to review that three A4 Pages
pages of things we had a one hour 15
minute long conversation and uh with the
three pages for very small features uh
it felt like you know everything was
considered everything was con uh
included and and we had you know we we
left the room with quite big certainty
that we had done a great job in in now
you know detailing and and considering
what we were about to to build
uh in the next week after that when we
started implementing things
we realized that yes uh amongst that
long detail thing there were things that
we had missed and actually we would have
probably had a better conversation uh in
that one hour 15 minute meeting if
instead of writing three pages that we
were looking at and kind of all of us
knowing like yes it looks like a solid
specification it looks really great uh
we would have had just two lines
describing what is the essential change
that we need to have a conversation on
so remembering XP extreme programming as
a mechanism and the concept of story
what was that supposed to be about it's
a placeholder for conversation
and the placeholder for that
conversation would have actually helped
us probably do better in in this
particular case rather than than the the
detailed preparation
so digital preparation we then had a
conversation on how we could have done
this this better and we realized that
the only way we could have done uh the
detailed uh conversation better is that
every one of us individually would have
created our own individual review review
preparation our own uh a uh 3a4 papers
long detailed discussion and compared
them side by side that there's this
human aspect of you know seeing
something that looks fairly solid
uh it's very easy to go and Nod and
having done thousands and thousands of
of reviews of specifications over the 25
years I think that test specification
reviews are particularly prone to the
fact that yes it looks like a test case
it looks like a thing we could try and
it is really difficult to have good
conversations unless all of us come in
with this individual review preparation
so as a sample I just wanted to leave
you with a visual of of what uh really
convincingly uh uh uh
prepared thing that overwhelms people
can look like this is something I
created yesterday evening with Iris
Strauss
uh we had uh this this kind of a
conceptual modeling of what are the
challenges of testing and how would we
categorize them and uh if you look at
this and you try to figure out uh What
uh is still missing maybe you will look
for the one thing that everyone seems to
think is missing here this automation it
is intentionally split everywhere here
because I don't think Automation and
manual testing should ever anymore be
separated there's the part of code
confidence that kind of mentions it but
when you have these many things already
listed it becomes really difficult to
figure out what are the things that you
still think that should be there and
unless you do kind of your own prep work
and then have and come into those
conversations or unless you co-create
this like we did yesterday starting from
an empty A4 paper you probably won't
notice the differences between the two
different people so in most sessions I
like rather than starting with one
person's good preparation is to start
with good preparation from one person
maybe but then an empty paper so that we
can learn together while creating
whatever outcome we were about to create
this leads us to the second point which
is that a lot of times in the work of
not just test specifications but
specifications in particular
if we have misunderstandings
all of those developer misunderstandings
not to test the misunderstanding but the
developer misunderstandings they tend to
either end up in production or they end
up in testing and and us trying to you
know in that short time frame uh that we
we still reserve for finding more things
on top of the early conversations
because in agile we really do try to
front load these conversations where
everyone is involved uh if anything is
misunderstood in a deeper level it ends
up in production and I don't stop
testing when things go to production
actually most of my testing may be about
of the hands of testing time that I
spent is uh spent exploring in
production so that we can improve the
product uh incrementally for the next
rounds so I only need to find certain
types of problems before we we end up in
in production because we're always
implementing things like in small slices
and taking things forward
so for this particular case
my recommended practice for for the
errors of mission is what I call a
revert reverse review maneuver which I
kind of hinted at instead of those three
pages long thing that we all kind of Nod
and look at and need to prepare
ourselves if we come to that
conversation with that empty paper and
we co-create those three pages and
instead of a product owner giving us the
requirements we as a team we get to
interview those requirements out of the
product owner and the product owner
reviews the documentation of the
requirements that we are creating as a
team I've been a lot more successful in
in building really good quality software
when the product owners don't come with
here's your story here's your acceptance
criteria but they just come with one
liner and everything else underneath is
is being written together by the Team
all of the examples all of the
acceptance criterias they are not coming
from whoever is ordering the work from
us but they are being reviewed by the
the people who are ordering the the work
from us so uh changing the mindset uh
that's been a very good way of finding
these these areas of a mission
uh another one that has been very
helpful for me is uh this idea of
actively searching
so during the prep work what does that
really look like
so if you want to see that negative
space if you do a mind map for example
and in the mind map you notice that it's
all tilted to One Direction like
everything that you're modeling like
everything that you're writing right now
today in your testing everything that
you're writing notes about is is under
one single thread there and the other
side of it is kind of like empty it
gives you a way of talking about uh the
things you haven't yet done and and kind
of visually also seeing that but also it
gives you a chance of of kind of like uh
considering uh uh balance in in terms of
of how you could make all of that better
visible in the preparation so uh the
speck of claims for me means that uh
almost every single time someone else
has given me as a tester has given me a
specification I will rewrite that
specification from another perspective
and that helps me to notice that you
know on my list and on the other list
there are things where these things
don't match I can't draw the lines
between my listing and the other listing
and then that kind of uh uh helps me see
the the things that I'm I'm missing
anyway
I'm seeing people raising hands I don't
know if I'm supposed to react to those
in some ways
we can take up one question in the
interest of time uh given the Russia
completing the test the joy of finding
errors probably I think Merit session
I'm asking do I need to like I have I
have still a couple of more things yes
please cover up what's the expectation
here you finish your session
as far as I'm looking I should have five
minutes right yes please yes please go
ahead okay good thank you
so to complete this one uh so create
your own listing compare uh in in that
sense
uh pictures create those visual modeling
is is a good way of doing things
so they usually say different things
than texts I almost always have
something visual to work from and here's
one example from last Wednesday working
with what I call testing dozen 12
complete newbies to testing in US kind
of like trying to figure out how chat
GDP the new system for for AI how that
works and how we would test it just you
know visually putting in context some of
the problems and examples of problems we
were seeing but also just visually
looking at it kind of on the left hand
side you can see
inputs on the right hand side you can
see outputs in the middle you can see
kind of the logic uh the black box of
logic and you can notice that you know
we don't understand the logic very much
uh we have some model of the outputs but
the model of the outputs is very much
lighter and the only control we really
have is on the input so it would make
sense that the input space would be
visually much much much bigger than it
is is currently but when thinking in
terms of kind of input something
processed an output for your black box
and modeling both of those and actively
looking for those things that can make
those essentially different seeing that
in a visual model makes you more
creative in noticing the things you
might be missing so combining visual
with something we do starting from an
empty paper rather than reading all the
existing documentation it generally
helps us
and then the final uh tip that I wanted
to uh kind of point out to as well the
reference uh if you create uh or have
something like that the baselining the
idea of having something in production
that is working well enough for
production it is a whole different world
to work with uh from the perspective of
omissions when you do these like small
rounds from you know it used to work
yesterday in production today we are
putting only this change more into
production the whole way of testing for
things is very different when you're
continuous delivery system creates the
reference for your testers testing to be
the version that was already there in
production and the changes you made to
that so baselining with continuous
releases is is one of the great ways of
of of noticing omissions because you get
that slice small slice of change that
you get to address
but of course you will have then
multiple perspectives performance visual
claims and the fact that humans are
generally not good at noticing change
there's this example from James Lindsey
where you have like a picture and then
there's a raster review when you move
your mouse around the picture underneath
is is revealed and in order to reveal
that picture
if you're kind of moving in just one
corner maybe there's nothing of interest
there you need like broad Strokes around
the picture to start noticing patterns
but when you have once seen that
particular picture and you have to look
at the same picture again it is very
obvious you jump to conclusions much
faster and you're not willing unless
kind of like you know actively taking
the time and effort you're not
automatically willing uh to spend all of
the time investigating the second time
around so creating some kind of
automation baselining that helps keep
you honest it's like almost a way of
expectation for me nowadays that that I
wouldn't survive without one of those
just recognizing the human aspect of of
how I treat continuous change and having
seen things uh multiple times so knowing
that I have have a baseline where
automation helps me is is something that
is is very relevant in in order to to do
things
so then uh kind of to summarizing uh
this all leads me to uh kind of you know
looking at documentation as something
that I would rather not write in advance
I will leave documentation behind uh for
future me to read and I would hope that
it's not 5 000 test cases like my my
current or previous project that well
one of the projects that I'm working
with right now uh is is has left behind
uh because uh reading all of that is is
a bigger course than anything else but
the documentation would look more like
something like this where it's code that
you can run this is a sample for testing
a Roman numerals program created by uh
GitHub co-pilot
you needed to have well I needed to with
a group uh create the tests that I
wanted to leave behind for Roman
numerals and have those conversations of
of what do we care to leave behind and
which of these things maybe we would
want to just you know not keep running
in the long term uh even including
things like approval testing where all
of the combinations numbers from 1 to
100 there's a test that tests for all of
all of that I could just as well also
run a bigger scale of test than one to
100 uh whatever design I end up making
for that particular problem so I've done
a lot of work in terms of moving
exploratory testing to the level of unit
testing
moving exploratory testing to the level
of integration testing moving
exploratory testing to the level of
requirements conversations and I've come
to experience from that perspective that
pretty much uh everything that does not
need to be automated can get done while
automating but it might be that most of
the time and effort that I personally
put into the work of my team is actually
not Hands-On automation but it might be
pairing with someone on automation or it
might be mentioning the thing that I
clearly see that we must be missing
because we are still seeing a mistake of
of missing something while I am spending
time on on testing with the maximum
creativity in the moment that I can I
can provide
and and since a lot of the the problems
in production can be found
uh found in in unit test level I find
myself actually nowadays doing most of
my exploratory testing in pairs with
Developers
rather than just thinking of exploratory
testing as something that is on a higher
level and some of the emissions they're
best found in the conversations of
what's missing from the model and
understanding of what the developer is
implementing right now so I wanted to
encourage you all to kind of you know go
and look for errors of mission also on
on that space
so with that uh those ideas I want to
still kind of like leave a brief moment
for us to have a small conversation
thanks
thank you Merit uh in the interest of
time we'll just take one question uh
that is given the Russia completing test
Joy of finding errors problem and defect
is lost how is that we can optimizing
optimize the test coverage using the
Omission approach and bring back the
pride of finding an error so we'll just
take this one
yeah
I I find that uh there's a lot of things
we can do actually around that uh sense
of of Rush uh by just making some space
actively saying that we take a day here
uh for for finding something more but
maybe it's also some of the the
practices that you've ended up
implementing are practices that I'm
trying to avoid like uh writing things
down in detail so some of that sense of
rush comes from the way we've agreed to
do uh do things so you might want to
figure out if there's way of of getting
away from that sense of Rush like take
control of your own calendar it's kind
of one of my my general practices that I
try to do
but also uh just you know uh when you
find that one thing uh share it talk
about it smile around it uh and and and
say things like uh this is something you
could have not uh you know left
intentionally and share that Joy of
finding something insightful uh with
your team and if they don't share this
the the joy of finding something
insightful and exciting uh with your you
it might be that you also need to
reflect inside a little bit on is the
thing that you get excited is it
actually relevant for the business that
is something that I have had to learn
over the years that some of the things
that I used to be taught as a tester
that I'm looking for and I'm finding
they are not relevant in all of the
different contexts so so also listen
back to the reactions when you're
sharing your joy of finding something so
make space share and and listen back to
the the reactions learn from those
wonderful inputs married and I'm sure
everybody has got a lot of inputs uh
from session that you have given so this
was a session on uh targeting uh
targeting error through machine which
was given by married firm uh I'm sorry
if I didn't pronounce bachery right
if I didn't pronounce your name
correctly uh marriage so it was a
wonderful session and obviously uh we
will have a feedback that would be taken
towards the end of the session or you
can give immediately after this uh
wherein you can give inputs and help us
evolve better in the upcoming
conferences from here
[Music]
