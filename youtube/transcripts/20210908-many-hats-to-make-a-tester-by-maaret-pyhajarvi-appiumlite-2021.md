---
title: "Many Hats to Make a Tester by Maaret Pyhajarvi #AppiumLite 2021"
video_id: bA3gh2MD6WM
url: https://www.youtube.com/watch?v=bA3gh2MD6WM
upload_date: 20210908
duration: 22:32
channel: ConfEngine
tags: [Appium, Software Testing, Test Automation, Appium Conf]
---

# Many Hats to Make a Tester by Maaret Pyhajarvi #AppiumLite 2021

> Recent years have moved teams away from having testers to having developers who test. When we accept we can't automate without exploring and we can't explore without automating, the split to manual and automation makes little sense. We need to discover new ways of decomposing the testing work to share that in the team. 
> 
> In this effort, we've discovered that what we used to expect from one tester, is now split to four developers each with a different emphasis for the team to be successful together. In this talk, we look at how our virtual testing team - a whole team responsible for both developing and testing an application, has split the many hats of testing identifying 15 hats for us to distribute the best way the team sees fit. 
> 
> Who carries the hats of a product historian, on-caller, parafunctionalist or feature shaper in your team, and which of the hats are hard to keep up in your current team composition?
> 
> More details: https://confengine.com/conferences/appium-conf-2021/proposal/15947
> 
> Conference Link: https://appiumconf.com

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

uh welcome again everyone to the appian
light conference uh without too much of
a due i will uh hand it over to marath
i'm really really
glad that she's able to join us here and
talk about the many hats
to make a tester what a brilliant topic
uh thank you maritz and over to you
thank you it's great to be here
so i was thinking what would make sense
to talk about in appitium conference
because when i looked at the conference
programs like oh i want to join that
conference
but all of the conference program is
kind of speaking to just one part of all
the interests that i have as someone who
is doing testing it's speaking to the
part around
the tool
and using the tool to solve whatever
problems we have in in the
the test automation space
but
a lot of times especially looking at
things right now in my team well we my
team isn't doing mobile plation but we
are definitely doing automation some of
the expectations that we are managing
in the team are not just about kind of
you know creating that automation and
solving the technical problems but
there's also other things around it so i
wanted to kind of address the
expectations and what does it mean to be
a tester or to work within the testing
space
and give you
an overview into the types of things
that are i'm having a conversation on
these in my current organization now
so first of all if you think of yourself
you know at some point you join an
organization you join a project and they
give you a role they might call you a
developer they might call you a tester
they might call you a product owner but
kind of the roles that i have in mind in
this case are the that are working with
hands-on work towards delivering
software contributing in any of the
various roles around software
and regardless of what the role that we
have there is well it might be a tester
role but we probably expected to do some
testing
if we are expected to do some testing
they're probably going to give us some
kind of a test environment
in the case of of uh things around
appium it's probably going to be some
kind of mobile application form
hopefully someone has either
already set it up or they can give it us
to as a service or they are going to
give it to us as a kind of like the the
first task we had is to to set up some
kind of a mini environment in which we
can do the testing we're going to do
hopefully they don't just give us the
device the devices but they'll also give
us kind of the tools or we are just
going to go and get the tools because
all of the things around testing
nowadays come from the fact that we are
using automation tools both for robotic
process automation we might do that even
in the in the mobile space but we're
definitely doing that in the web space
and appium is kind of a nice tool in
that space a really good option kind of
to to work across various different
platforms and and and user interface
technologies so we're giving those tools
we have some knowledge we have some
information maybe it's already being
built maybe we have already a framework
or maybe it's kind of like an empty
slate that we get start to start with so
we know that there will be these tools
but we need to start from growing from
our own experiences or maybe even
collecting the experiences into that
organization that hasn't done it before
but this is a typical thing we get
we also usually get this is a
conversation i've had with many many
testers in the last two weeks we get
some kind of an expectation of how quick
we are i've been looking at numbers of
pull requests in the last few days
and i have an expectation that if i have
a
developer software developer who is
focusing on on mostly the code and not
doing much of the
other work around quality
uh
two full requests a month sounds like a
small amount of results for four full
weeks or 40 hours of work
and i don't know what the right number
is but really small numbers make me
curious so kind of expecting some kind
of schedule i'm expecting some kind of
progress to be made in a a you know
reasonably short amount or chunk of time
so that's probably going to be given to
you as well some kind of an expectation
on how quickly you're going to be
contributing and how often you keep on
contributing and how to see
you continuously taking things forward
whether it's radiators or or other
mechanisms that's still going to be an
expectation
and you're probably also going to be
given some colleagues some of the
colleagues will do exactly the same
thing as you will do so if you were
hired as a tester in that organization
there might be other testers in the
organization as well but there's also
going to be other roles and those other
roles will also be taking part in
testing in whatever
uh agreement uh shared agreement that
you create in that that team so so
talking to the other people working with
them and making something useful for the
the whole of you is is going to be part
of the the work you do
so
and as an expectation has an outcome
you're probably going to be providing
well some kind of list of of problems uh
information of
what works what doesn't
information of what's been implemented
what we could still be adding having
those conversations around that
information
some test automation which i think of us
as the better and the more modern way of
doing any test documentation i basically
refuse to write much of other test
documentation and automation
and
i think sometimes the most important
thing that you're expected to deliver is
a better version of you that is better
tomorrow than you were today and a bit
again better in a week than you were
this week so this kind of continuously
growing self but also making sure the
others are not going backwards but
rather forwards with you so keeping
everyone on board because that is an
expectation so this is kind of you know
simplified way of saying the work we're
expecting to do in teams
around testing regardless of the role we
end up being in is is something of of
this sort
and
because
it's not that complicated you might have
also heard that there's been this whole
conversation in the community around
this idea that the tester is you know
it's just a role
in a team that anyone in the team could
pick up and i'm kind of here to today to
share on the idea that you know yes
that's true but they're still kind of
you know and there's more
so one of the things that happened in
the last couple of months is that john
shared on twitter this nice uh visa on
responsibilities of engineering manager
and when i was looking at this picture
kind of like all the different hats that
engineering manager has to has to carry
i was noticing that a lot of the the
labels he was using are kind of like
from the the designer space in a way
kind of thinking around how to build
products and how to understand what kind
of features are right for it
and
the piece that i find myself
contributing in the piece of being a
tester in these teams it's kind of
hidden there on that one line as one of
those black little post-it notes
on the side of writing code there's a
thing called testing so under the the
role of code and pixels
so probably you know you could explode
this and try explaining in the way the
role or the many roles of a tester and
that's exactly what i then did
on the day following john's tweet
so i created a listing based on
observations from the last year in the
project that i'm currently working on
where i was trying to explain that we
have five people we call system testers
and yet we have ten other people we call
developers in that team
and the five system testers can do all
the testing but we need to somehow
figure out across the whole team of 15
people how do we distribute the hats
that we you know the work that we
consider to be testing and i had given
it already some kind of like you know an
outline an earlier outline of lots of
things i was seeing people do but i
attached kind of these labels i made
them kind of more convinced and i
attached them into a similar visual
inspired by the work that john had done
and also i looked at four exemplary
people from my team you can imagine that
the d4 there is a someone who identifies
completely as a developer developers do
a lot of the test automation work in my
current team
whereas then different kinds of testers
actually still end up somehow picking up
a little bit different kind of profile
of work so let's talk about the rows a
little bit so we are in appium light
conference so we definitely need to
start from you know the core of what the
modern software testing i think looks
like which is that automation is not a
thing we question it exists it should
exist the question is just how much
today and how much more do we need to
learn before we are on a sufficient
level in our organizations but every
step forward is taking us that you know
one day better mindset that should
always be part of every activity
that we're trying to do so we'll
definitely start from kind of you know
the hats
that come to you
if you join that organization as a test
automation
developer type of a person like a tester
with automation specialism so we would
definitely be expecting uh there to be
code like you are going to be writing
code and if there are no you know
commits and pull requests into the
version control
uh if you don't change anything test
automatically won't get any better but
the other part of what you're probably
kind of on the first level expected to
do is to contribute in the conversations
around features in helping shape how can
they be more testable and what are they
like so that you know what kind of cases
even the basic positive cases which is
only a small part of the things we need
to test
what would that look like so you
participate actively in those
conversations definitely these roles are
the forefront of it
the two other roles that i picked up are
things where
all of the test automation specialists
that i work with in my current team can
have challenges with so i wanted to
emphasize that to you today
the on caller is this idea of a role
that you are always expected to be
available for your team
within the working hours in the is that
when there is a change coming to your
system
you will also make changes to the test
automation system that match whatever
is is going on in the the system under
test that you are you are trying to uh
so you're kind of like trying to make
sure that you know if something
today you could be able to
with your pipeline designs or at least
someone having a conversation in the
team that this is now broken maybe we
should be you know fixing it and it
wasn't broken before so kind of like
that reaction creating that service in
the team but also the other side of it
the designer hat is is equally important
so it's not enough to just do the bdd
positive this is how we show that it can
work but we also need to do what we
called in the past and call it negative
testing so trying out uh various
different things that you shouldn't be
doing but also trying out combinations
of all kinds of features so that you can
let the bugs kind of you know
reveal themselves out of the software
expected to design
the ideas that make all the
relevant issues somehow surface
then
on the other roles or the other hats
that you could have as a tester well
probably
building that pipeline and and keeping
it up to date i hope it isn't as painful
and as effort-worthy work for all of you
as it has been in my team in the last uh
uh in the last month we've been
measuring how many days out of our month
we had the test automation
radiator green
and that was 4 out of 22 days so not a
very high percentage but 4 out of 22 is
much better than the 1 out of 22 that we
saw in the previous month so definitely
we are making progress in that but it
also means that the pipeline maintenance
keeping kind of things up to date it is
actually a fairly large amount of work
and some of my colleagues in testing or
test automation said that when you've
invested here in the test automation you
can expect that it's going to take half
of your next year in just keeping it
alive so a separate hat for that is a
good idea in the sense that it helps
talking to the managers about the
expectations of what you will be doing
as a tester
uh if you have that device farm or like
right now i have a farm of
uh well devices iot devices uh which are
you know some kind of mobile devices but
not the the common purpose ones
we're doing embedded software it's
probably gonna be a huge amount of work
to to set up an environment of all of
those devices that you can run
and we do that definitely for automation
purposes
set up remote
abilities to connect
and also then of course you need to
think in future like what would it take
to make our test automation better
then there's this idea or area of the
things that a test manager used to do
i put this
label collection here as a reminder that
this is work that i find myself doing
but i also find myself to be the only
tester remaining in my organization who
does this so to see the future of these
labels even though they are test
oriented labels is that the managers the
product owners learn to think in terms
of testing as well but unless you teach
them and unless you negotiate with them
unless you help them understand these
things they won't be able to help
and contribute in these areas but it
might be something that is also expected
of you
and then finally
my three favorite things here on the
hats the product historian i find that
that's a role that some people very
naturally take who have been testers in
the past so when you ask about how did
we decide on you know having this
feature like this or how do we decide uh
having this problem out there they can
give you the exact jira ticket that
shows that you know we decided this is
okay
and they can give you the documentation
that is 157 pages long this is from a
couple of weeks ago at my office and
they can point out that it's on page 37
on the second half at this point where
you want to read for that one piece of
information you were looking for
para functionalist as a role is uh or as
a hat it's reminding us
that it's not just the functional stuff
so we need to figure out security
reliability performance usability at
least those four in addition maybe you
could add testability there as well but
i would kind of like to see it as part
of the other roles and if you are
technically inclined
nothing says that you should stick to
only
shaping system automation you could just
be a
participating in the unit level
development work
and
also help make sure that we do a good
job on that area
so all of this together it's basically
being that you know the tester label the
the the one role that we
don't need to put on one person
we need to actually explode it you might
find your own labels in your own
organization same things
but it might be that across your team
you will figure out who of your team
will take which of these and even if all
of these are things of testing they
might not be things that the person with
a tester or test automation
label in your team does so instead of
thinking three amigos the business
person the developer and the tester i
suggest you would think in terms of for
example the uh the bono six thinking
hats
approaching the problem from six
different perspectives or if you want to
make it a little simpler
make sure you have two pairs of eyes
and the two pairs of eyes is basically
your way of saying
that never leave your colleague alone
with something as important as making
software for multiple users to use and
enjoy
finally i wanted to conclude with the
idea that this work is what i call job
crafting you are making the job you have
the job you want
but to be really good professional in
whatever you are doing in software
development
i believe you need to make it visible
which bits and pieces of
the vague
hats or the weight role of testers you
are going to be taking
and what do you expect of the other
people around you
and if you rate intent and others see
what you are doing they might be picking
up the other pieces or you might be
needing to say those out loud
so that's the message that i had for you
today and i hope you have a fun testing
and and enjoy your your conference in in
the epm space
all right thank you marit that was
brilliant i think you finished dot on
time so greatly appreciate that and what
a lovely message to leave the audience
with uh you know take the job and make
it what you really want to make out of
it like make it into what you love
actually
uh and so that's uh great if there are
any questions we could uh take some
questions now if you want to leave the
questions in the q a section please we
can take some questions uh
alternatively marath is also going to be
available in the hangout uh
section so on your screens you will see
on the left hand side uh in the menu you
would see hangout uh so you can go there
and you'd find a table with mark's name
on it and you can go join the table at
any point in time up to eight people can
uh
have a live video face-to-face
discussion and uh rest of folks can
watch the video without necessarily
having to join the table and uh
we we hoping that this will allow you to
peep and see a conversation and decide
if it's interesting you want to join in
or not you know
you know check before you commit kind of
a situation
so uh
if there are any questions uh i see uh
there is one question
okay i have uh anonymous attendee uh
question from an anonymous attendee uh
what is the day d1 d2 d3 and d4 refers
uh two uh i think in your slides you had
the d1 d2 d3
it said developer one developer two
developer three and developer i have a
big belief that all testers are
developers
and i would rather call us all
developers than than separate us anymore
into the
the role silos
okay cool
any other questions
all right i don't see any other
questions for now but i think we can
have
folks join the table and have a
face-to-face discussion with marath over
there
again i want to thank all the uh folks
for joining in this session greatly
appreciate that i also would like to
thank all the
volunteers behind the scene who have
made this possible without whom uh this
conference wouldn't be possible and uh
last but not the least uh the sponsors
who uh who helped us put this conference
together so greatly want to appreciate
them as well
uh if uh during the there are there are
10 minutes breaks between the sessions
for you to uh get out of one session and
join another session uh you could also
uh take time to visit the sponsor booth
so if you click on the left on the
sponsor section you would be able to see
all the sponsor logos and then if you
click on that you get to visit the
sponsor booths they have some
interesting goodies over there so i'd
appreciate if you can
visit the sponsor see what they're up to
as well
so without
too much uh delay i will try and close
this session and have maret kind of
continue to the hangout session so folks
can meet her there
thank you again so much thanks everyone
take care bye
