---
title: "A Practitioner's Guide to Contemporary Exploratory Testing"
video_id: 9nFYHsXD0cg
url: https://www.youtube.com/watch?v=9nFYHsXD0cg
upload_date: 20240124
duration: 46:08
channel: Maaret Pyhäjärvi
tags: []
---

# A Practitioner's Guide to Contemporary Exploratory Testing

> This is a talk I delivered at Axiom Summit, and it's one of the my favourites that I did on Contemporary Exploratory Testing. It was recorded in 2022.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

such an extraordinary tester a favorite
tester of me actually it's a bless I
would say I guess many would agree with
me on this marit is a principal test
engineer at w Salah she is a tester
author and a community
facilitator she has been awarded the two
prestigious Global testing Awards most
in influential agile testing
professional person 2016 and Eurostar
testing Excellence award 2020 alongside
she was also selected as the top 100
most influential in ICT in Finland 2019
to 2021 indeed super happy to welcome
marit as one of a keynote speaker in
axim Summit 2022 before I hand over to
marit some important housekeeping work
that me as a host I would need to do we
would take all the audience question to
towards the end of each presentations so
feel free to post all your questions in
the Q&A section do not post in the chat
section otherwise certain questions
would be missed so make sure you post
all your questions in the Q&A section uh
only so over to you marit thank
you right I hope my slide is now
visible yes all should be good
uh good afternoon uh finish time uh good
morning Uruguay time uh good evening
very late evening if anyone from the
Australia is is still around uh it's
great to be here in this this Global
conference and have this kind of
privilege of talking to you about uh
contemporary exploratory testing and in
light of what we just heard in the
previous talk you might be wondering why
did I add add this word contemporary to
the title and that is kind of uh one of
the things we'll definitely be talking
about in this
presentation so uh I've been doing
exploratory testing pretty much my
entire career 25 years ago when I
started as a tester uh the first job
that I did I was given test cases yet
those test cases weren't the only thing
I was given I was given a very flexible
budget
and an assignment go find any of the
Bucks that matter anything that you can
find please raise it let's have a
conversation on it and then uh from that
kind of on uh no matter what instruction
someone else provided for me it was
always my responsibility it was always
something I needed to do to make sure
that I am providing those results and
from that experience already 25 years
ago going through very various companies
over these these years I'm
noticing in many cases that we have
these conversations about exploratory
testing being something kind of that
we're adding on top of everything else
so and and it was for me it was
something completely different I wanted
to spend this this talk today on kind of
giving you ideas of what led me into
thinking this is a separate thing uh
what are the changes that this is
enabling in my current organization that
we are more widely now thinking in these
terms and what are the the results that
we're seeing out of that one so going
back to roots of exploratory testing the
word I don't want to give you a long
history lesson but I just want to kind
of remind you where did this whole idea
start from in 1988 this book was
published uh I haven't actually read the
original first edition of testing
computer software whereas the second
edition that I I started my personal
career with I have read that probably 20
30 times by by this date and it is a
great book uh about all kinds of
techniques and thinking in detail about
how do you do how do you approach
testing the book itself doesn't mention
exploratory testing as it like as in
like it is a book about exploratory
testing it is only a book about testing
computer software but it does mention in
one of the sentences
for the very first time this concept of
exploratory testing and introducing that
as the style of of kind of like
multidisciplinary testing that considers
legal aspects considers Financial
aspects business aspects human aspects
technical aspects all of these different
things and requires us to kind of go for
the results and pointing out then
afterwards that this style of test ing
was already common for those businesses
in Silicon Valley that were making
relevant money with software development
so already back in those early days
there was this kind of like a divide in
the world in a way where the product
companies would be doing something that
would enable you know successful
business with those software products
and then the Contracting companies were
creating these safe uh uh very kind of
uh
uh pre-written plan oriented ways of
doing things and and we needed a name
for that that more uh agile style
already way before agile was a thing so
we called it exploratory testing uh I've
lived in Finland pretty much my whole
life and I remember the day when I met
mik Huen who is nowadays retired this
grand old lady already from my
perspective in in that sense she started
working with software development and
testing in
1973 she was working at Kella which is
The Finnish social insurance institution
and she said that pretty much her entire
career from that day when they founded
the first testing unit in that uh non uh
nonprofit oriented organization and had
the very first computer available in
Finland they were doing uh this style of
testing because in Finland we never had
the extra money of of throwing in into
writing documentation that we didn't
find valuable or creating things of of
uh uh kind of like out of CH process or
or someone asking for it so this whole
idea of of being very cost aware was
something that kind of we were born with
being a smaller country with not so much
resources necessarily so while Kem ker
definitely introduced the term I find
that this is a very natural way of
thinking about
testing and uh the term uh is really
important in the sense that we can find
other people who are thinking in the
same way and have the same kind of uh
high level context maybe in
mind uh exploratory testing when we then
started kind of as a community we
started looking at it what what is this
1988 thing that that we started talking
about when Kim ker first came about with
that that term we started talking about
it and there were this this um uh uh
peer conferences meetings where people
would look at things together and the
big realization that came about is that
that the essential part of exploratory
testing is that we don't separate test
design and test execution because when
we separate these two if we keep these
two separate different uh Concepts kind
of like one is done six months earlier
and the other one is done six months
later or one is done six hours earlier
and the other one is done six hours
later in agile the Cycles just keep
getting shorter if we keep these
separate and if we particularly separate
them by the people who are executing
these tests or doing the designs and
then execute the tests we're taking away
the learning that could happen uh we are
having a handoff in between and we're
taking away this agency this power to
decide what to do with that knowledge
and having that attitude of doing
something kind of like making uh
decisions with that responsibility
towards those impactful results so this
not having that separation is the key to
exploratory testing if you look at it
kind of like you know you imagine you
turn your camera into another
perspective if you look at it as it kind
of like all things testing that we give
labels to we have things like security
testing or regression testing or
performance testing or like I I picked
up from joti M's talk today these uh
specific techniques of testing uh where
is exploratory testing in all of this I
find that the exploratory testing is
kind of the glue that helps us uh uh
recognize that there's all these
different approaches that might be
helpful to us some of them we are
already aware today and some of them we
are learning as we're listening to these
conference presentations but in the
frame of exploratory testing we try to
understand how would those be useful for
us in providing the results that we're
expected to to provide so for me this is
kind of the foundation of exploratory
testing so then what's this contemporary
explor testing
then uh looking at teams basically for
the last five years in particular I've
started to realize that this separation
of test design and test execution that
we used to have in
1988 that made the the core of of
exploratory testing back then we are now
seeing with the world around us changing
that the same separation is happening
between the concepts of manual testing
and automated testing and for the exact
same reasons of learning an agency and
having that power to make those
decisions and not just uh try automating
somebody else's kind of test cases
without really knowing why those exist
for those impactful results we can't
keep these separate either and we need a
whole different way of organizing
testing exploratory testing in scale we
can't separate it by saying exploratory
testers don't automate and then there's
these automation people separately
because you can't actually write
automation without exploring the
application and you can't really do
really good job in your so-called manual
testing side without having that
automation available to you when when
we're working in these short Cycles so
for contemporary exploratory testing I
find it really relevant to kind of break
this barrier of of saying that we have
different people or or different
considerations for manual and automated
and particularly I want to emphasize
contemporary exploratory testing
includes automation so you might say
it's automated testing but it's
automated testing just like programming
uh the application is where you actually
have to think about what you program
before you program it so you're also
designing the system as as you're going
by uh creating the system and sometimes
some of those things you will just end
up doing manually because you haven't
yet gotten around of of creating a
script that would help you in in in that
work and it is really the same thing
with any programming oriented activity
that we're doing for creation of
applications so I've been trying to then
kind of draw pictures of of how do I
make sense in the world like what things
must change in the way that we talk
about testing so that we could have
better conversations about this cont
temporary style of exploratory testing
and the first one is definitely this
this pyramid test automation pyramid and
and we keep saying that there's this
unit level test automation scripts and
API scripts and end to scripts but those
scripts are created by the exploratory
perspective we make choices when we
first time run our API tests whether we
want to keep that particular API test as
it was now written around or whether we
want to refactor it maybe change the
values of it so that at least you know
we leave behind some other default than
the original default that came uh with
the advice that we we discussed with our
teams developers so getting kind of
variety into the data variety into the
actions we're doing all of that is
driven by the exploratory the learning
perspective and we do that on the unit
test level we do that on the API level
and we do that on the uit test level and
it makes sense for us to to
question uh whether we have the right
things already documented in our scripts
uh and add those and sometimes it makes
sense to create something that we
automate and then we throw away
similarly looking at the other picture
there that I've I've drawn uh you might
also think of this as in terms of int
intent and impact we often in the world
we talk about this idea that it doesn't
really matter what you intend it to do
if the impact is actually something
different we should be apologizing for
the impact we're making on the people
rather than our intent that wasn't to
hurt someone else and it's the exact
same thinking in terms of where does
export testing sit then in this world
the intent of developers get documented
in those unit tests the intent that we
understand from the customers gets
documented in those acceptance tests the
intentions that we used to have in the
past those are the focus of our
regression tests but the impact whether
we were right with all of our intent
that is what really matters and that's
where exploratory testing sits in in in
this
picture so I prefer talking in terms of
attended and unattended testing not
automated and manual but attended and
unattended I want to have some way of
doing testing while I'm paying attention
to other things I might be creating the
next unattended test while the other
tests that I previously created are
providing me some useful not perfect but
useful results and I might be actually
being called to attend based on the
unattended tests failing giving me a
signal saying kind of like a spiderweb
come here look at this uh and calling me
to explore and it is exploratory action
that I do trying to understand why is
this test now failing is it because uh
the software has changed in a way that
nobody remember to communicate to me I
think that's one of the golden gems that
I get out of this automation people
often forget to mention relevant changes
and whatever scripts that I'm attending
to then will give me that that idea uh
but also it might be that it's revealing
that the intentions that we had in the
past are actually no longer holding
through and uh whether it's me who gets
called or it's someone else in my team I
really like the idea that we are able to
share that that knowledge and that kind
of calling in to attend with our team
and do whole team uh uh test Automation
in that that
sense uh and all of this has also then
led me into thinking in terms of
automation that maybe we should like
with all testing that we do we should be
aware of the use of time so when we keep
talking about things like uh automation
isn't perfect we could have used that
moment of time into talking about
something else and while it is good to
address the concerns that the fears that
we may have around learning so many new
things at once it's also actually maybe
better way of of talking about things in
in reminding all of us including myself
that uh in 25 years I've had multiple
days when I could have learned this and
I could in any of those days spent a
little bit of time just to learn
something small about Automation and in
the last five years I've definitely used
my time a little bit differently and and
uh grown in in this this area a lot but
also uh kind of like thinking in terms
of I I think it was Dorothy who
mentioned in in her talk today that uh
uh she can read code but she really
doesn't write code but actually reading
code and noticing you have a typo in in
some of the strings
and then going and fixing it that's
actually changing code it is part of of
of uh uh the work that needs to be
happening in the team so I feel like
maybe we should be using our time also
in finding the small steps that we can
take rather than focusing on the steps
we cannot yet take and every new day in
our career forward is a chance of adding
more steps we are capable of taking we
don't have to do it all in one big go
but just keep adding things on top of
what we already know is a good good uh
result uh way of doing
things so uh all of this kind of what
change I see happening in the world it
gets kind of summarized into this idea
that what I eventually care for is is
that we need to have good results out of
our testing the testing needs to be
result full and when I first started
using this word result full testing I
got corrected on TW Twitter that uh
restful testing is is a different thing
that I have a typo there it's so close
that it's almost confusing so I'm not
talking about API testing here I am
talking about the fact that in testing
we kind of are given the assignment of
finding something that others may have
missed and when we are going to find
that something that others may have
missed if we had a list of all those
bugs that we need to find and it was you
know like nicely and easily readable
list and didn't require a lot of work to
go through and and figure out what of
that massive list we're going to cover
for this particular application because
we do have those examples globally but
it's just so much material that we can't
read all of it but if we have that kind
of like small list of all the results
that we need to provide in testing we
wouldn't need testing but we don't have
that so our job as testers to provide
those results is to turn that invisible
code of the right answers answer sheet
of bugs make that visible and and uh in
uh some kind of either a system or well
it might be a test automation that we
document our bugs in in a way that they
won't be coming back again again
choosing where you use your time you
might choose to fix a bug and then
document that situation in automation
rather than creating other elaborate
redent of the topic so this is kind of
the way that I've come to think of
testing so how does that then change the
practice in my my
organization uh with the teams that I
work with uh how is how are things
happening uh well first of all it starts
with the idea that we have a category of
bugs uh some of them we can find before
implementing so we should be taking our
time on reading and asking questions and
clarifying whatever claims are happening
before we start implementing
participating in that work some category
of bugs regardless of our best efforts
will escape even our own eyes and when
we use the application to test the
application we use it as our external
imagination we are more creative in
figuring out what still might be wrong
and my recent measurement on my
capabilities on this one after 25 years
of practice is that about 75% of things
I was able uh to come up with before
implementing given my best efforts in
bdd style and 25% of the problems and
things that kind of surprised us and and
could have been you know we could have
tried having those conversations before
uh were still something that I needed to
find by testing and this is just looking
at things that I have before releasing
in but I am thinking of every single
task that we are completing and putting
into production that I am having this
kind of like a loop there's like a tail
of every single task that we do that we
can go back uh to the production and
also look at monitoring and metrics and
Telemetry and make sense of things that
can then have an improvement idea for
our next cycles of of features or or bu
fixes or or adjustments that we creating
on the product that we're doing we have
this idea of wanting valuable
information and any sources of that
information are available to
us uh it means uh we have to grow as
testers I collected here mostly ideas
related to the fact that we need to grow
to be more aware of what information
matters uh not all information is of the
same value there's time Dimensions some
things are really important for now
somehow for future we're always
balancing our work in in in different
time
frames uh knowing uh that uh we can
choose to create a mind map we can
choose to create test case documentation
we can choose to improve our
requirements texts we can choose to add
to our automation all of those are
choices and we choose we make those
choices of where we're investing we need
to be aware that every day of our job is
that we're investing uh time in in
something and uh definitely kind of
learning to invest time in I usually
just you know I look at a a a white wall
uh for a couple of hours every Friday
afternoon and just thinking about kind
of like you know the future and and what
might be coming uh around the corner and
uh having that kind of like time for
reflection on on what do I know now and
what don't I don't know and what how
would I find it out it's also helping me
in building these skills in myself and
in my team as testers to to kind of
become just in time reactive to the
level that it feels somehow somehow even
magical how we can have something kind
like a test environment for example
ready just when the feature needs to
start uh to be developed because it just
takes a while before that new hardware
arrives and if you don't realize that
you will have to pay attention to this
time Dimension it can give the
appearance that you're always kind of
just a little late with the things you
do so so uh balancing things and and
learning to learn really well is how I
think we need to grow uh in the
Contemporary exploratory testing space
as
testers uh another thing we need to
really grow on I think is that we need
to learn to be better neighbors so a lot
of times especially with agile teams I
find that um I'm uh having colleagues
that are very focused on my current team
right now and uh usually it's not just
my team that creates the system there's
multiple teams and it's not that I have
to do the work of the other teams but
often testing is the perspective where
the two teams come together we hope both
of them work uh in isolation already
just fine but the testing of them those
two together the two neighbors together
needs to happen and it's an easy area to
have this uh well I would almost even
call them disagreements on who should be
doing this I just this week had this
conversation that we had a team a doing
a component a and Team B doing a
component B and there was this agreement
on component a plus b testing that it
would happen in both of those teams with
a particular way of of sharing it uh but
there was this ex expect that there must
be a team C because it's so-called
endtoend testing and end to end testing
just must belong to some other team so
making those uh Good Neighbor uh uh
conversations happen uh will help you
address uh those problems that when the
problem is found by the teamc which is
by the way I learn in Twitter customer
if no one else uh then uh when that
problem is found and it's pointed to
your team it's your problem then so you
might want to proactively uh look into
that by being a a better
neighbor I find myself in a dual role
I'm uh a tester uh but I'm also a sort
of a test manager facilitator of
improvement in many ways I also
collected some of those advices of of
how as uh from a management perspective
I could enable uh this kind of
contemporary exploratory testing I find
that my main goto way uh
for for uh creating the space in which
agency and results are possible is that
uh I make the releases shorter so it's
almost like a signature move now over
the last whatever years that I go to an
organization that releases once or twice
a year and I turn them to releasing once
a year once a month and then I turn them
to releasing once a week and then once a
day and until I get to the place where
they release whenever something is is
ready if they let me stay in one place
long enough I will get to that even in
systems like my previous place of work
where we had uh almost two million users
that got affected on their personal
computers not on the common server but
on their personal computers whenever a
release would happen it's just a a
little different uh challenge uh to do
distributed continuous releases than it
is when when you can centralize it on a
nice web server but it is possible and
it's worthwhile and it's worthwhile for
testing because when we are making
changes in smaller scale it's a lot
easier uh to kind of start from a
working Baseline look at the changes
we're making and think around those
changes what testing would we need to be
doing absolutely the the number one
go-to mechanism for me nowadays for for
test management uh instead of having
status meetings I like having uh uh
sessions where we either co-design or
even co- test emble testing is my
absolute go-to method so uh when I'm
concerned that I don't know how someone
is testing I'd rather pair test with
them than review their list of test
ideas uh uh obviously uh it's not just
only pair testing sometimes I like to
give people a chance of writing things
down in a mind map format typically uh
before we go into that pair and execute
from their ideas because different
people require different kind of of time
frames in being uh in the the right mind
space to start doing a certain kind of
activity and definitely uh looking at
how am I doing in terms of impact
reviewing the uh time that we used and
the results is is a go-to mechanism as
well uh then uh on the
evidence evidence part uh this is
something where my current organization
uh has very strong uh I would almost say
feelings maybe but but the history maybe
is a better word that uh tests must be
documented in a particular way and it's
been a really easy way of changing that
culture whenever I can frame it so that
whenever we need to document we can
document that evidence as
automation so uh when asked to write
detailed test cases with steps I would
in any day for purposes of exploratory
testing write rather title test cases
than those stepwise test cases uh rather
than ever writing title level test cases
I would always create mind maps and over
mind maps if I had the that the the
capabilities already buil up in the team
I would almost any day uh build
automation over those mind maps so it's
not just this or that but being aware
that the group we are working with will
have an impact on on what choices we're
making and this has been also then of
course impacting the the recruiting and
and growing the new be testers into the
idea that from day one when they start
on the projects that I work with they
they will be writing Automation and
becoming contemporary exploratory
testers so automation isn't the only
outcome but it is part of the outcomes I
wanted to show you what I think success
looks like when when Automation and
documentation in automation is is is uh
in question you can see the number of
people that are running around there
these are not all testers excuse me
screen has stopped sharing we're not
seeing your screen any oh it's it
stopped sharing
sorry know if you did that on purpose or
not no I did not do it on purpose it was
accident let's try again so now you
should see it probably it doesn't really
matter on the other ones this one is
something probably want to see but you
can see these like little you know
characters moving around uh this is the
whole team contributing to test
Automation in a team uh where test
automation used to be the work of an
individual or a pair of testers test
automation Specialists everyone is now
contributing and this is the kind of
visual that I think in terms of
contemporary exploratory testing it's
not that all the work is done in test
automation it is just that there's a lot
of work done in test Automation and over
a period of year that I have here kind
of like visualized with this Tool uh
there's been quite a relevant number of
things documented in various different
areas uh the structures have been
changing and moving and uh there's a way
of of making sure that you can
understand what the others ended up
testing because you can rerun that test
and if you have open questions because
the documentation is off off in some way
you can still go and and ask them and if
you can't find the answers you can
always do the next step of changing
things in in terms of
that uh we thought about success fa
factors uh for this kind of of style
from the automation perspective so uh if
in a research project uh we kind of came
up with these different perspectives
here uh the Stars here are making a mark
on my previous project and my current
organization so this listing we made it
with my previous uh employer there's one
area Telemetry that we were doing with
my previous employer that we don't do in
my current uh work yet uh but I believe
uh that one is is just a matter of time
and I wanted to kind of point out the
organizing the internal open source
Community mindset I've managed to now
get away from testers or test automation
Specialists contributing to test
Automation and having it as a whole team
activity uh but I still need to move
from whole team activity to all
neighbors activity and and that gets
even more complicated when the scale
grows I was able to do that in my
previous organization having three
business line sharing test automation as
documentation that helped us work on a
product line we'll still need a few more
years years on my my current
organization uh what is different in
this style is that if you look at the
traditional ways which are very kind of
uh uh plan driven ways in uh doing test
automation uh you can't find document
called test automation strategy it's
very much hidden we have ideas and we
can draw them and they are probably
going to be similar for multiple people
no careful tool selection all of the
things we kind of give advice on
Automation in books generally this seem
to be very
unorthodox uh we would add tools and
like Lego bricks we can take them away
if we didn't like them it's always
better to kind of fail towards U action
rather than than be stuck in
speculating uh too much and uh we
wouldn't be measuring uh the quality and
performance of test automation we were
measuring quality and performance of the
products and our feelings in the team
were definitely being being have the
conversation on but of course success
and failure it's always a snapshot I've
spent now two years in Visa these are uh
names of all the teams I've worked with
so far I think I've succeeded with three
teams uh I think three teams that I work
with are still kind of uh on the verge
of inconclusive may be successful but uh
according to my criteria I might still
uh question the success so the whole
team aspect needs a lot more work there
uh and uh there are teams that I worked
with I would still consider that they
didn't yet manage to get here there's a
lot of work to be done against both
enthropy the idea that things get messy
if no one is cleaning them up and
there's a lot of work done against
inertia the idea that nothing moves
unless someone exerts a force and makes
it move and I find that this is the kind
of mindset that we need to have in
multiple team members in order to take
things
forward uh rather than focusing on just
kind of this automation or or how do we
come up with the ideas I find myself
appreciating my colleagues with a little
uh kind of like uh mentions of I noticed
you're really good at this and I spent
one Friday afternoon instead of my white
wall I was drawing these little images
with texts on kind of like badges I've
seen people be relevantly different in
this space uh we have different skills
and appreciating the fact that some
people might be really good at
strategizing but other people will
always be the ones who present the most
clear and easy to follow Demos in all of
our demo sessions because they know how
to show the the positive sides without
uh uh missing out on the risks that need
to be addressed like the different
skills that we have as as people this is
not all of the skills but these are some
where I've noticed that I don't have all
of these skills myself I have some of
these and my appreciation to my team and
my my colleagues around me is that other
people have other skills so it's not
just one profile that we're looking for
in a contemporary exploratory testing
person but it is having something that
the local team is
missing and when I talked about things I
really try usually not to talk about
testers so much I try to talk about
whole teams I try to uh uh uh remember
and mention it's still a little
difficult sometimes for me that the
programmers are sometimes in many of the
teams they are actually the best testers
uh in those teams but it doesn't mean
that the other testers aren't valuable
even if uh there is really insightful uh
testing Happening by the programmers
there's just so much valuable work for
us to do that we need to share in those
teams that that all of us needs to pitch
in and testing is kind of too important
to be left just for the
testers I believe very heavily uh that
everyone can test uh but in order for us
to get uh result full testing it's kind
of like thinking in terms of everyone
can also sing and we know if we've ever
been to karaoke uh especially in Finland
uh we know that some people are uh
slightly better at their karoke
performances and some of them uh would
be maybe even possible to be put on a
big paid stage where thousands and
thousands of people are ready to uh pay
for it but if someone wants to become
good at singing and if someone wants to
become good at testing uh we have all as
humans we have the foundation uh to
start building on those skills SKS uh
one day one step at a time as long as we
remember that we don't just want to
provide any
results even a broken clock would be
finding us a result of the right time
twice a day and as testers we are
expected to be more productive more to
the point uh regardless of the the
working role that we're testing from we
are asked to be more to the point with
our results than a clock that would be
only right twice a day so uh paying
attention to your use of time and your
results is really important so to
conclude this with my favorite saying
nowadays seems to be that testing is
really about going finding some that
others may have missed and uh we don't
know what we're supposed to find unless
we find it first but also this has to to
me at least it has this corollary in 25
years I don't think I have been bored
yet when I'm bored I'm changing
something so when you notice your board
it's probably an indication that you
could be learning a small new skill
trying to do something differently and
uh there's other people who can pitch in
in the important things you are doing
right now to make you space to never be
bored we are not alone on this so thank
you on on my
behalf I think we should have time for
questions yes M thank you so much for
such an insightful session uh many
things I it was very catchy I would just
like to UNH highlight two statements
that you had showed in the slide it was
very interesting you can't automate well
without exploring and you can't explore
well without automating it's something
like you know very insightful um thank
you so much for such an wonderful uh
content that you had showcased us with
today I hope even the audience will be
like right now imple planning to
implement this contemporary uh style of
exploratory testing in their day-to-day
work thank you so much Merit so maybe we
can take up a couple of questions we
have few questions for
you the first question that goes here is
like how do you manage to give the test
automation to all everyone in
team uh usually you manage that by one
task at a time so in teams we have these
conversations of who's doing what today
and we can have those conversations of
who's going to do things around test
automation today uh reminding people on
the fact that we don't want anyone to be
alone especially when we talk about
responsibility that that are handling
millions of people or millions of Euros
you never want to leave anyone alone and
and from that that kind of general idea
that there is responsibilities that
software teams are often carrying are
kind of big it's a it's a really
important way of kind of saying we need
more people sharing this responsibility
we don't want to be alone so asking and
making space in the day-to-day that's my
best advice okay that sounds
clear uh the next question is like in
your opinion what were the main
obstacles that blocked your failed teams
from
success
um I think the communication related
things probably so uh we often have very
different value sets on what good
testing looks like how am I supposed to
do it and what's supposed to be my role
in doing all of this and when we want to
change uh people's ideas of what they
are supposed to do for example if you
have a developer who thinks that uh it's
the testers job to collect the pizza
boxes they leave in middle of a living
room floor uh then uh unless you figure
out a way of communicating that that
isn't really the the hoped for way you
uh will find yourself collecting those
pizza boxes again and again and again
because they cannot be left there there
going to be a big mess and you won't
have time for the other things so a lot
of times it's about not having enough
time to have the one-on-one meaningful
conversations that change the
perspective of those
individuals okay okay quite interesting
yeah so the next question is about
result full testing result full testing
with minimum time how is it
achievable so uh usually I would start
from kind of thinking in terms of what's
important and and what are the
risks uh having worked with certain
Developers for a long time I know what
kind of mistakes they typically make and
what I need to look after each
individual that's a good rule of thumb
for me uh I know uh what kind of things
our customers usually complain about if
we miss them so starting from that end
might be also good uh different
architectures help me prioritize where
risk is more likely so uh uh thinking in
terms of of what do I think others have
already done and what's the added thing
that I need to do or can do on top of
that in order of of addressing relevant
risks to this product uh that's how I at
least minimize my time and then
considering how much time you're using
on on documenting uh whether it's mind
maps or automation uh you can cut your
time a lot but you're going to pay in
long term if you cut on your
documentation and automation time so
when you leave the organization uh you
realize that you could be leaving a
piece of you behind if you automate it
uh and that was for me at least it was
kind of the the moment of of uh
realizing I want to work differently
that I want people to be able to test
some of the things I was able to test
even when I am no longer around because
I will always leave yes very true very
true agree
agree okay so the next question have you
ever experienced that testing is not
given priority and management said Dev
can also do it if you have faced how did
you cope up with it so I also have teams
that have zero testers uh and devs can
do it I I think it's true yeah sometimes
those managers are actually absolutely
right I actually believe my personal
belief is that uh adding one tester into
a team of developers who has never had a
tester might actually be making quality
worse than not giving them a tester at
all so usually when you you're adding
testers you might need to add several
because it's really difficult to manage
the expectation
uh around what this person will do for
you because people always are uh
thinking of of they take some of the
work we are doing now away rather than
adding something on
top uh but yes management has all kinds
of expectations but management are
people too uh I think Dorothy's uh
advice and and and Mar's advice on that
today was really solid on having those
conversations and trying to understand
why are they asking what they're asking
and again like for us testers it may be
good to remember that we can continue
testing even after it's in production
obviously there's the next feature
coming but we might be able to you know
take away a little bit of time while in
production and if we're just ahead of
our customers in understanding things
that will fail we're already providing
value exactly right right um I think we
are running short of time now we have
couple of more questions maybe audience
like this will be answered later on to
you via website again uh again thank you
so much mered for your valuable time it
was
quite
