---
title: "QAstion time: A Year in Test Automation- By Maaret Pyhäjärvi"
video_id: n935eyyq4aE
url: https://www.youtube.com/watch?v=n935eyyq4aE
upload_date: 20211006
duration: 50:02
channel: Xpertise Recruitment
tags: []
---

# QAstion time: A Year in Test Automation- By Maaret Pyhäjärvi

> Maaret is an exploratory tester extraordinaire with a day-job at Vaisala as Principal Test Engineer. She is an empirical technologist, a tester and a (polyglot) programmer, a catalyst for improvement, a speaker and an author, and a community facilitator. She has been awarded the two prestigious global testing awards, Most Influential Agile Testing Professional Person 2016 (MIATPP) and EuroSTAR Testing Excellence Award (2020), and selected as Top-100 Most Influential in ICT in Finland 2019&2020.
> 
> In this talk, we will look at the successes and challenges over the year Mareet has been working with her team. We learn about how her organisation moved from 34 work days release testing for a single product to 2 work days release testing for multiple products, and where the real needs and challenges of test automation lie - in a whole-team quality approach.
> 
> The talk outlines the strategic principles guiding the test automation work at her business; the main insights and changes over the course of the year; and their shift from regression testing to reliability testing on level of the team, and slowly but surely dismantling the dedicated test automation operators through continuous improvement.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

so i'm christy i don't know if i've i've
spoken with quite a few of you before
i'm a quality and test consultant for
expertise recruitment
um so i specialize on recruiting from
manchester businesses
[Music]
i am currently in sunny north wales
actually in triage bay if anyone knows
um
so
apologies if there is any background
noise i've gone to tell the music down
and they've been very nice so far
and i'll let marek do most of the
talking anyway uh if everyone could stay
muted uh if they can it's always nice to
see cameras on but i understand that
everyone likes that so no problem if not
um
and as i say i'll let you do most of the
talking the wreck so if you'd like to
take it away
sure
i'll try to hide my face so that i don't
have to see myself all the time it
looks weird to be looking at oneself
so uh
my name is marek pujarvi and i'm from
finland so that's plus two hours to
where most of you probably are in uk
uh plus one hour if you're somewhere in
in more like central europe
so it's 2 pm for me if we're assessed
well it might be a little earlier and
lunch time for you
and what i wanted to kind of share on
today uh started from this idea that i
was invited to speak in a finnish
conference that then got cancelled and i
i'm disappointed in the the fact that i
didn't get the chance of kind of like
you know doing the presentation that i
wanted to
and kind of going through the reflection
of what does my last year in test
automation advisor look like
so i tweeted about it and uh well this
meetup was kind of tough to first
contact me and said like hey we can you
know create the space for you to do what
you want it to do
and since i generally
don't do talks kind of like out of the
the the
you know the practical side of things
like the things that really happen in
projects i really appreciate the fact
that and do this one for you here today
uh the schedule how i was kind of
thinking of it is that i've tried to put
some stuff on the slides for about half
an hour
and then i would hope that we can have a
conversation so again i speak to you
today and in general as a practitioner
someone who works in you know real
projects i don't have a consultancy i'm
not doing consulting i'm not trying to
do recruiting either it's more of
i am reflecting uh the work that we need
to do in the organization and in the
teams
and and kind of look for ideas also from
you on maybe i'm still missing something
maybe you have ideas on how i could do
things better or maybe some of the stuff
that i have already gone through would
be useful to you so again from a
practitioner's
point of view
and the whole idea with this one year in
destination uh for me
right now it's been that for the last
year and a half when i've advised them i
have 25 years of of industry experience
in general
i've ended up working with a little bit
different kind of software
and by a little bit different kind of
software is what i mean by that is that
i don't have
a web page as such
i don't have a windows application as
such
instead i have these very physical
looking weird devices
the one on the middle there that's a
weather
wxt weather
measurement instrument so it measures
wind and it measures humidity and
temperature
and uh and rainfall that type of things
so definitely an embedded device but
also that kind of you know the embedded
device that that that sensor part it's
put on top of a mast you can see that in
the other picture there
and uh what i've been building for the
last year with the team that i work in
is there's the uh in the middle of that
under that solar panel that you can see
we also built the solar panel so so that
was also part of the things we had to
build and the whole kind of uh
the powering system that we did for that
but there's the little box like the
brains of the weather station that's
kind of the main central part that i've
been working
and since this the brains don't do much
without the you know the
extensions that you need the solar
panels or the the sensors into this
i have needed to kind of pay attention
to every uh little piece that gets
integrated into this so my world kind of
looks like uh conversations around
conversations around real firmware that
is kind of you know just very used to
that hardware something really small
that is put on a circuit board but also
for the heart of this this weather
station thing
we've been building and extending the
linux operating system for embedded
devices
we've been building applications on top
of it and we have web user interfaces on
the actual device but also it sends
stuff over to the cloud so there's been
also kind of club software that i've
needed to to work with
and for me kind of like you know when i
joined visal i was told that you know if
you haven't worked with embedded
software before this is going to be so
different and in the last year and a
half i've come to the conclusion that
the difference is that we talk about all
those lovely layers of the rainbow like
we really quickly in the same meeting
might go from you know talking about how
the gates and regis is done and how
things are connected physically into
talking about the whatever user
interfaces we have so the range of
things that come to you is kind of a big
one but also i really like the post on
kind of so last week on being
strategically ignorant so just you know
decide i'm not paying attention to all
of the hardware details and the world
suddenly looks very much like
it does
on the regular software side so i don't
think this is so different other than
the fact that some of the hardware parts
mean that we need to build hardware in
order to do test automation into these
systems so we'll talk about that a
little more
the system in how we do automation looks
pretty much kind of like on a high level
scale like this
uh we usually have a linux pc control pc
of some sort
but if you connect it to the whatever
device we are testing right now uh we
call that device under test boot is the
word that we're using
it's usually connected with usb into
that
uh it also usually has
kind of like a more standard
tcp udp type of connection you can an sh
connection into that
that or you can at least send stuff over
the serial using uh
the same kind of control mechanisms and
from the control pc plugging in so
there's usually a maintenance connection
of some sort but similarly also from the
control pcs that we use we have
also uh other hardware pieces that we
can control uh one of them we call katri
i think that's a bit more of a kind of
like specialized terminology uh within
in in the sense that it's just a
physical board that allows us to do uh
what the physical world phenomenon so
for example one of the things we do with
that is that if we want to reboot a
device like we do a quick reboot that
restarts the device that's something
we're able to do kind of like simulating
a press of a button
or similarly if we do a long reboot
keeping you know the button pressed for
like 10 seconds that basically resets
the device back to the factory
installations uh installation settings
and we can also do all of that
programmatically so what we basically
just have operation
side is a lot of different kind of
testability this is
that programmatically control
and
what we've been using mostly in in our
tests is
two different frameworks we've been
using robot framework so that kind of
comes into play a lot in in this this
particular environment but also recently
we using just pure python
a lot in in doing the the exact same
kind of things and for python then using
various libraries that that enable us to
you know just reuse stuff that that
somebody else has created just like the
robot assassin environment has provided
for us
uh if there's anything kind of uh
special about this setup it usually is
the fact that um me coming from
again creating cloud software or windows
software and and pipelines for for kind
of very modern automation before this
one it feels like i went back 15 years
time in some ways because now i need to
accept the fact that
mostly we're able to run
our new builds and build automation only
on a nightly case i can't get it to run
yet on every single pull request it
takes a lot more work to build those
farms that we can either virtualize or
share
in ways that that would enable even more
modern way of doing test automation so a
lot of the automation stuff that we
built is kind of running on a nightly
cadence and when you're used to having
the feedback at your fingertips in your
projects it really felt like time travel
when i when i joined this project a year
and a half ago
or this organization a year and a half
ago
looking into kind of the the history and
what has happened in the last year in
particular
the history in this particular company
on test automation is that long but it's
still fairly long so about 10 years ago
the first people in weissela were
starting around
using test automation
for system level testing so unit testing
has been around a little longer and
actually has grown on the side of this
into a real practice that that
i think we can rely on a lot more
nowadays than we used in the in the old
days but with the system level
automation about 2010 people started
kind of building the first test
automation systems here
and then they kind of ended up with
robot framework and robot framework has
this
special ide called write
robot framework ide
and that's basically it's like the oh
well if you are used to selenium the
selenium ide where you can record things
and and you can combine things on a very
very simple user interface that is
intended for people who don't know
programming that's kind of where we
started off
test automation was done by a
specialized person and test cases were
very much kind of still existing so the
first five years uh was kind of
introducing
people who would start working usually
alone in their own
repos on test automation so now going
back and looking at what we have we have
a lot of this individual person has been
keeping a repo for 10 years of corners
organization
about five years ago then that
recruiting with a little bit different
profile i would say so they started
recruiting these test automation people
as the only people who would join the
new development teams so no longer test
cases were a part of it necessarily
so they went for this this idea where
kind of everyone who is part of the
teams is usually doing test automation
related work
but also then
when that started becoming a thing
the hiring also changed so that
we started to have teams where there's
no test automation people whatsoever
but the developers are actually taking
care of the entire thing but all of this
history kind of looking back at that
time
that the 10 years of time
it's usually been a single person up
until the point when developers started
co-owning automation it's been a single
person solo doing test automation and
with the project that i joined a year
and a half ago the end-to-end system i
started first
on the cloud side and for the last year
i've been looking at the embedded side
it was kind of clear that we will have a
group of at least five people uh sharing
that test automation and a team of 15
people who will be kind of benefiting
from the immediate use of that
automation so the scale started growing
and we needed to figure out how to
actually do this and and and resource
this properly and we've been recruiting
people who are
system testing specialists but everyone
can also write automation so we expect
those two roles combined and the
developers regularly pitching in into
this this automation
but kind of looking at the time of me
seeing this and and having a a view into
what we are changing and what we're
building
when i joined year and a half ago i felt
really like i already said i felt like i
went in time so i came from f-secure
a company that does windows applications
and we were doing continuous every two
weeks releases there
for about 1.8 million users at a time so
imagine
test automation had to play some kind of
a role in being able to do that quite
safely
and then joining uh by salah for me was
was kind of like looking at a team uh
doing these embedded devices where my
first task with the team was to do a
retrospective with the team because they
had had just a very uh i would call it a
painful release at least it was painful
for the product owner that's why he
called me called me in and said can you
look at how we're doing and help people
figure stuff out
uh they had just done 34 days of release
testing
during
they basically
quickly dropped all of their automation
and automation work
they didn't even have time to maintain
it because release testing had taken so
much of their their effort
and they had basically been discovering
uh the tests they needed to do
uh as they they were kind of moving
along
the release making they didn't find that
much problems necessarily uh it's just
that there were so many things that they
didn't kind of plan for or understand in
making of the releases
that the first thing that that kind of
left the team in that moment for that
month and a half
all of the test automation work and and
it feels kind of sad to notice that
that's happening
so i looked at the team and i looked at
the challenges
and we kind of concluded together
that
we had a few things that we needed to
fix in that team
working together with the develop
developers working together with the
system testers in that and the product
in particular
uh the strength of the team was clearly
that the testing actually the system
testing that was being done wasn't
necessarily so needed they didn't find
much of the problems and customers
apparently who weren't finding much of
the problems because they yet wasn't so
many of the customers
but the developers kind of didn't leak
basic problems
so that best automation work or or
testing work needed to find so the basis
of doing good unit testing was already
in place
but there were a lot of other challenges
so they were leading things based on
test cases and when i say test cases i
mean test cases with step-by-step
instructions on what to do
and that wasn't a very particularly good
way of working
then they were doing agile
feature by feature kind of adding into
the existing system but it looked more
like i call it like a leaky feature of
waterfall
so in the end when the developer was
done
that's when they really started working
on the automation and testing and and
they had kind of like change of
priorities on whether to do automation
or whether to do it only manually
and the end result was that if there was
problems they would never find it
someone else would find it afterwards
so i was also leaking
the corona started about
the whole remote work completely through
the team off
they didn't really talk much they didn't
have much of of channels
well nowadays we talk a lot on the
team's channel
we do a lot of kind of screen shares
let's code together let's create
automation together none of that exists
then so needed to be kind of built into
the system
uh the whole
culture was around if you say i need to
do that task i will do that task
tasks were created by someone other than
the person doing them
and there was this whole separation
and test automation
so all of these were recognized as
things we did not want to have
so what we changed then uh third or
actually throughout the year
was that
i
changed teams i was in another team
first
and my team had a single tester me
and three developers
and it seemed like for the success of
the entire end-to-end system project
better for me
to move into this embedded
part the heart of the weather station
that team
with the other
five tester system testers that were
there
so book the lead not really off
there's a lead tester in that team
but i side by side with the lead and as
someone who is a principal level kind of
like a more experienced person
even if there's someone else to lead
i
kind of implicitly joined leading
the team
in in that sense and started behaving as
if like you know i had also things to
contribute in the team
then
we started doing changes on the release
process as such
so we started making agreements on
releasing with the test automation only
no matter how little or how big it was
actually it was kind of little in the in
the beginning we would release basically
uh or the release testing would happen
by only running the automation and
adding one of work on top of uh running
automation and analyzing the automation
and all the other testing we called that
feature testing happened kind of before
that and as part of future testing
we have definition of done include uh
based automation improvements that we
could scope for that that particular
feature
then uh when we had uh previously been
leaking a lot of testing work that made
automation creation difficult for the
team
we
listed all of that as kind of like title
level only test cases
and instead of
the system testers testing those things
we asked help from the rest of the team
and all of the developers were really
excited in getting to kind of play with
the entire system and take in features
and test them
and they found quite a relevant number
of problems that the testers hadn't
found when they had been kind of
juggling the automation and the other
things and and trying to figure out what
the features were so kind of not moving
that information away always from the
developers but giving developers time to
do some of the testing
resulted in really good results
then we started doing more frequent
releases so first it was 34 days when i
started off with the team
then it got to 12 days then it got to 4
days
and now
for last two releases it's been two work
days to make mailings and nowadays we
release two products at a time instead
of one product at a time so we've been
definitely getting a lot better at at
that work
uh kind of just
organizing the work better and and
relying on test automation existing and
being built as part of the process into
that that release decision making
and
another thing that needed to happen kind
of on a strategic level is
agreeing that the test automation
running environments
are not free game for anything anyone
wants to do on any of the days without
communication to the others
so all of a sudden some of the tests you
could actually run them on the
environments because it wasn't so that
someone had again changed it so that it
was running a completely different
version so kind of rules around how we
use our shared environments were were
placed in in there
so that's a strategic side
and then
the year
of making
i think
six releases in that year last year
if i count correctly six releases
uh we made uh tens of features so we
never got to kind of stop with the
release making and stop with the
improvement or stop with the
the feature making so that we could do
some kind of like a concerted effort in
improving automation we've been doing
all of it kind of as part of the work we
were already doing to make those
releases
i thought it was interesting to look at
what did we do in that that year
so the first thing kind of like that
that i noticed that that happened in
that year is that the conversation
started to formulate around this idea
that we can't change things for the
better if we don't change anything so
unless we would do pull requests and get
them approved and unless the automation
was somehow changing we couldn't expect
to get better so that started to kind of
drive the conversation and and drive the
design
of of who would do what next so that we
would continuously be improving and
extending and and making our test
automation more reliable so the
avoidance of uh it must be someone
else's problem we got kind of like a
nice a positive way of figuring out how
to get away from it by by talking around
this idea that we are all contributing
by pull requests and if we notice that
uh someone of us wasn't making pull
requests we could be kind of having
those conversations and like hey maybe
bearing would be you know appropriate or
something like that
then we had over the last year we had
three different developers as kind of
like full-time contributors to test
automation
so sometimes there was more work than
still with all of the other things we
kind of strategically tried doing
there was too much work for
for the testing side
so we developers uh contributing to test
automation and with the idea that when
they then went back to the application
development side they knew the test
automation system and continued
contributing for whatever features so we
got three through this this kind of a
round of
three months in test automation and then
going back to being a regular
application developer except now you can
also do the automation part and that
seemed like a really good practice a
working practice for us
then also kind of naturally what
happened over the last year is that we
had a bit of a change
in people so we had some consultants in
the team who decided that they would be
focusing their efforts elsewhere so we
found new consultants into the team and
when you have new people you usually
also get new ideas and when you have
multiple people with new ideas those
ideas turn into a practical uh
implementation so some of the things
that we really got together because of
the change of people in the team was
this idea that exploratory testing and
test automation are actually the same
thing for us
there's a lot of the things we couldn't
do exploratory testing for without using
automation as a starting point for it so
we learned to talk about testing can
test design and looking at things and
pairing on things in a kind of like an
uh unseparable thing there's no separate
kind of like here's where we do manual
testing but it's all framed around
automation is what we will leave behind
that's our documentation
then we got the idea of working towards
a green radiator
kind of getting people uh rallying up to
that that course
and to separate the the feature testing
kind of like when is the feature down
testing is included in it and we won't
be leaving that stuff
kind of for the release testing time
frame so that was more like a
communication improvement in the in the
team
and we managed to add some nice things
into our test automation system
uh particularly now we no longer
manually scripted jenkins jobs which
are manually configured which we had a
year ago i i'm
much much happier for the fact that
that it's now all going through the pull
requests and and it's all visible it's
something a lot more concrete for all of
us to share
uh we introduced using allure which is a
test reporting frame
on top of robot framework
that gives us a
nicer report
especially the aspect of reporting that
allure gave us was this idea that we
started seeing
uh kind of out of all of the the
previous jenkins runs we started now
seeing when was it last working or when
was it when did it start failing and it
made a significant difference in our
ability to kind of understand what might
have broken things so so kind of that
got a little better
and then uh working with robot framework
we started also experimenting with what
if we would use the unit testing tool
the pi test with allure
to actually running all of our test
automation so what if we remove the
layer of the robot tests would that make
things better for us and we had a summer
employee this summer who spent half of
the summer on pie tests
half of the summer on on the
on the robot tests and their conclusion
was that uh it was definitely a lot
better and easier experience and the
results also show it
so with that uh it was a lot better
experience to kind of just learn python
and and move forward from from that
perspective so that was something we did
in the year as well
i took some screenshots so that i can
show you uh some things uh that are kind
of like more concrete and
practical here
so you can see the yellow parts there
there's unimplemented and missing tests
that's a practice
that uh i started kind of building in
where
you could find all the so-called map
currently manual test cases or in the
frame of the automation so we kind of
brought it all into into code and pull
requests and and that helped us
communicate on the level of the code a
lot nicer so you could find
to do's which were not yet
completed but also we introduced this
idea of unfinished tests things that
were failing
uh like they were not reliable enough so
we would categorize them differently in
our reports and if we had bugs that
needed to be fixed they also got
categorized differently so overall in a
year you know i had a screenshot a year
ago and i have a screenshot right now
on the level of of
placeholders things that
something to test well at least we've
added
some things uh even though we still feel
that there's way way more to do
and for all of you to get an idea of
what does robot framework tests look
like
they
generally read very much like english
they're kind of pretty but the challenge
with robot tests at least for us is that
uh
creating one takes a relevant amount of
time
uh the debugging tooling isn't
the easiest
one and that's why we're kind of moving
towards maybe python and probably doing
bdd related layers if we want to have
kind of breathable easily readable test
cases on top of python
right now no one is interested in
reading this anyway
so we don't really miss the the
it reads to a non-programmer aspect as
much in the team
also in the year we kind of ended up
retraining our management a little bit
to expect that
uh
test automation and other testing are
not two separate things but they are the
same thing and we talked around the
releases we talked about kind of like
the idea that you should expect that the
number of our test cases is growing it's
not sufficient we can't tell you a
number that will give you a good sense
of coverage but if we are not making
progress you will not see a better state
in the team so that was kind of coming
through the continuous releases
for that
and then in the team we also kind of
looked at
some of the things we were doing has
kind of these hats different kinds of
roles
that people ended up doing on different
days so everyone was kind of doing
all kinds of things
but some people were clearly stronger on
forex
hardware prototyping related work and
would kind of take the lab technician
type of role a lot more so understanding
people's competencies and special things
in more detailed level happened
and then finally how things kind of
continue from here
is that
we are now looking at things kind of
across the whole organization not only
with this one team of 5
or 15 people depending on how you want
to calculate it
and we're finding that there's a lot of
commonality between our different teams
and that 10 years of history is still
ahead of us to actually harmonize in the
organization and we started this kind of
like demo your best things the things
that you're most proud of in the
organization
we also noticed with the recruits that
we really need to strongly encourage in
the organization it's kind of like an
external view of people who are doing
good stuff in automation elsewhere
for example this whole kind of green
radiator that's like a huge thing for my
team right now that we've managed to get
to that in the year
i've been working for the last whatever
five years in teams that don't care
about radiator because you basically see
every pull request if it stays green you
know fine or not you don't need to look
at test automation separately so i feel
like we're still some 10 15 years behind
some of the others model-based testing
some of the tooling for virtualization
there's so much work
ahead of us in that space and we need to
start looking at that actively
also i feel like we are in the path of
changing our robot framework tools that
keeps us a little in the old world into
this programmer and maintenance
friendlier toolset so basically that's
uh just removing uh robot framework and
going into pure python which is how we
extend robot framework anyway but we
just wouldn't be having as many layers
there
uh learning testing and test automation
both together kind of like in the frame
of test automation working in that frame
that journey continues and i know that i
will have to fight with my team a few
more times at least the idea that we
will be releasing monthly and this is
non-negotiable
the practice of one year and six
releases is not
yet
fully solidified and all of this kind of
reminds me of the fact that
you can change things uh while running
the projects uh but changing
uh the lessons that people have acquired
over years and years unlearning some of
the the previous uh
understood concepts it takes a lot of
work so
also uh only time will be solving that
so that's kind of what i had
and i was hoping we could have a
conversation
thank you for that
uh brilliant slide there because i love
some of the visuals on that i'm sure
that took some time to put that together
um
if anyone has any questions feel free to
pipe up now and um
and ask directly
and if you don't want to open your mic
you can just write it we can also read
it that's fine
but of course we would love to to also
hear your voices if you're comfortable
with that
does any of this ring a bell to you like
similar experiences anyone
yeah
uh
hi murray i think we met a few test
conferences over time i think we've even
shared a nando's at one point um so um i
suppose a question i've got is
during your presentation you used a
statement i think used it two or three
times test automation and exploratory
testing are the same thing
could you elaborate for those on the
call exactly what that means because
people like myself see them as different
things but i think you've got a
different take on it could you bring it
to life for us
uh yeah uh this is actually something
that i've been working for right maybe
last five years uh kind of the
realization that when kim kaner
originally exploratory testing
he described it as kind of the smart way
of doing testing where
you you have agency
in the sense that you don't write test
design and and test execution you need
both of them to be able to learn
and what i look at as as my kind of you
know realization into that on top of
that is that uh the same thing the same
ages gets lost
if you separate test design
also automation and running with
automation kind of like automation does
the same thing for agency
so you never have good enough
collaboration that the people who don't
do automation would actually be able to
do the best testing they should do
if there's that separation and i've
spent the last five years basically
undoing that separation for myself and
undoing that separation of themes and
training people into the idea that we
can actually do both of them at the same
time automation uh is something within
exploratory testing that uh it kind of
like it's like a spider web
you in when it fails and that's where
exploration starts we call it debugging
uh but it's actually exploratory testing
we are trying to figure out what's the
reason and what is this automation
teaching us but also automation is kind
of like taking us to some kind of a
starting point from which we might want
to kind of you know manually i call it
attended we want to do attended testing
forward from getting to a really
complicated setup with information and
then just checking stuff there that we
found hard to to get right into the
automation screen
so in many ways kind of when you end up
separating them you end up creating a
worse experience of testing and i feel
that contemporary exploratory testing as
i frame it is this idea where you fight
against the separation so that you raise
an agency but it also then means that
you need to build the skills
in people and you don't need to know
everything about automation to actually
already work on automation
but
daring
text that is in that format is already a
great start for a lot of the people that
i work with
great answer
can i also give a shameless plug to your
slack channel that you've started the
exploratory testing slack channel which
has got some great stuff around unit
checking and testing tdd bdd i've
already found it really interesting so
there's a shameless plug for your uh
your slack channel
all right it's it's great that someone
else has has shamelessness when i
don't cheers thank you great talk by the
way thank you yeah so again like a lot
of this is is uh figuring things out in
whatever situation you are in your
companies like i don't believe there's
like you know this is the great
automation looks like
or that i could get there in a moment
it's more like whatever i end up
struggling with right now and actively
moving things so that it's always better
for the next day
when i say that manual testing is going
out of the market soon i wouldn't say
that
uh i would say uh we do a lot of manual
testing to create our automation so i
think actually the the really good
understanding of testing test techniques
and how do you test
is it's coming back
and one of the troubles that we had at
least with the people specializing in
test automation were that they were
developers who didn't understand testing
but they were writing test automation
from someone else's command
so kind of like uh it has there's a
whole different role
that i use the the frame of t a plus e t
like you have to put them in the same
package
uh a lot of the people who have having
testosterone maybe ended up recruiting
didn't know how to test really well they
had kind of raised up the ladders by
learning the program but forgotten how
to test if they ever had known that and
right now i feel like what's coming into
the market is this
this uh frame of uh
having to intertwine the the skills of
thinking
automation and making choices of which
tests will you leave behind as automated
and and and what will you do as attended
testing kind of like being there to
watch the
information unfold
the other question was that are there
some low code or no code automation
tools that i would recommend
to help make automation more inclusive
so
for us even in waisal i have another
team working in we call it group i t
it's basically business systems so
salesforce and and sub and and that type
of systems
and we hired their automation specialist
and we have high hopes for the idea that
that we could you know figure out a tool
where all of the businessy people
can end up writing automation
uh
yet it seems like
uh they can take the trainings and they
can just create a lot of scripts that
don't really serve us well they are not
just creating this kind of like a
maintenance nightmare
so even though they can do it
i don't think the creation of tests in
the first place is the problem we are
trying to solve in the space of
automation we are trying to solve the
ability to keep them around and be
useful over longer term
so
i haven't
really liked myself low code ones
i have paired uh with three different
business people on robot framework
creating test cases with them
and it seems that with a few hours
together they can learn to do that type
of automation
so it's not actually so big of a deal to
teach
business people enough automation
and it depends really whether it's kind
of given to you first as a you know
there's this fun thing we could try if
you would like to learn
rather than you will be jobless unless
you learn this
like if you feel you know negative
around the pressure that that you are
being asked to learn new kinds of skills
it's probably not going to be the
beneficial area for learning
but
a lot of this stuff is kind of it's
teachable it's learnable pipe by pairing
so for the last two summers i've had a
summer employee and they both are
working in the space of automation and
exploratory testing combined
and they only got three
well one got three and other got six
months with me and my team
and and really well in new jobs new
places work where they ended up
taking more salary after they got
trained which was kind of also the
agreement that we had with them so
so
i think
it is more it's a smaller learnable
thing than we give it credit for a lot
of times
but it requires someone who is willing
to really coach and pair
and not just send people on courses and
lead learn
learn alone
there's
nice
question of maintainability being the
issue
yeah
now i know you obviously mentioned about
increasing
ownership i guess or sharing the
ownership of automation across the team
um when you were doing that did you face
any resistance from from anyone in the
teams and if so who who was that from
mainly and how did you overcome that
i have one person who resisted still to
the
probably to the bitter end
and and he is uh the team's main
software architect
kind of the the most skilled and most
fast-moving developer in the team and he
says that he doesn't want to stop for
three weeks to learn robot framework
so my theory is that now that we've
moved our tests some of our tests uh on
the areas that he works in in the pie
test uh he will just you know update
them so i think it's uh
there's a frame of uh
some tools create an extra hindrance for
you
in in going and contributing and and
some of the developers
really do not like the fact that robot
framework as a language is kind of
cumbersome
and well i would have to agree with them
but not everyone gets the choice
of opting out of this work
but i think you know again i i have
another talk that i've done earlier
where i talked about this idea that none
of the advice i can give you on how to
get it done won't work for you
i have 25 years in the industry i've
done 450 talks in various conferences
and meetups over the years
i know
and get to talk to see xo level people
about testing in my company and in other
companies i get regularly called when
someone wants to comment on how testing
should be done in whatever things
especially in finland but nowadays also
globally and that gives me a plan where
when i say something people tend to want
to jump a little higher than when
someone else says says it but also some
of that comes from the fact that i don't
just ask people to jump i ask them to
jump with me
so i show up on a call i share my screen
we write information together i don't
make the people do things that i don't
take part in
but i definitely do have a platform that
is not available to everyone else
uh including the fact that uh
you know you could seriously considering
that refusing to participate in things
that i i suggest in my team
means that you are not very popular in
the team after that and i try to use
that power that i have
in a
conscious way and consensual way
but
i recognize that
my summer employees have taught me
that the things i ask for
are a lot harder to get when someone
else asked for them
and all i can say is find someone who
has some of the power that i have and
use them to help you it's probably your
product owner so spend time with the
product owner and use their voice to get
some kind of you know like strength
behind whatever you're proposing
so
find a way of lending someone else's
credentials
but again you know being interested in
this and and having a hobby of of
researching this and and and trying to
analyze this and trying to understand
what happened
uh
it's definitely a path that you know
anyone can choose to walk on
so and you know enough years given
enough years
i'm pretty sure that i am not the only
person who has that
access
but uh right now in the current
organization
it's really exceptional that i get to
talk to cxo level people about this
thing once a month
[Music]
i've had that before
well thank you for that really enjoyed
that talk um it will be it was recorded
as well so there will be a recording
available so um i'll send it over to you
and post a link in the meetup group as
well when it's done
um we will be migrating as well this
meetup group across to a linkedin group
shortly as well so i'll post links to
that as i went um but it'd be great to
see you all on there as well uh but if
there are no more questions we'll we'll
call it a day there sorry i have one
more question oh here we go
i think uh did one of your slides
mention that you took the brave approach
just to test the release with automated
tests only was that right
yeah
so
so we should were you at the stage where
the team were quite confident they had
enough
automated coverage of critical areas of
the system to take that approach
no no i've done this multiple times i've
done moving teams to continuous releases
six times now
and the first step is even if you had
single test cases automated you just
start doing continuous releases it will
fix itself
just don't deliver it to so many
customers in the beginning
so don't start with 1.8 million users
start with one so you would take like a
canary a canary release kind of approach
yeah kind of canary type of approach so
you give it only to some of the
customers or maybe you don't even have
much of customers in this case we didn't
yet have anything other than the pilot
customers and i was working kind of up
the numbers on the pilot customers on
the side of this
but uh
just introducing the idea
that
how we will work
whether it's not doing any of the work
then that's how we will still work we
don't do separate
extensive release testing that's the
first step
yeah when i saw that slide i thought
well it's quite brave considering a lot
of your automated tests are still in
like an infancy stage so
obviously quite a high risk at all
and i think again this is a different
talk
which uh
i've delivered in uh aptly tools
conference there's a the one about the
continuous delivery experiences
so uh i don't think it's brave at all
because when you do this every single
day you have only one day of changes
done
so the changes create less risk when you
do it frequently
so
