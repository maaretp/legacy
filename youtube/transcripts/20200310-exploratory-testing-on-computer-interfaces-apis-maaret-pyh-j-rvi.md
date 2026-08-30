---
title: "Exploratory Testing on Computer Interfaces (APIs) | Maaret Pyhäjärvi"
video_id: Wh3MTHyA1tQ
url: https://www.youtube.com/watch?v=Wh3MTHyA1tQ
upload_date: 20200310
duration: 30:40
channel: Serverless Architecture Conference
tags: [serverless conference, serverless architecture conference, sla con, serverless paltforms, cloud services, cloud native, sla, 2019, developer talks, videos for developers, serverless, Maaret Pyhäjärvi, F-Secure]
---

# Exploratory Testing on Computer Interfaces (APIs) | Maaret Pyhäjärvi

> Exploratory Testing is a skilled multidisciplinary style of testing. Many have learned to apply it on user interfaces that naturally speak to testers as their external imagination. Yet with systems of today, it is important we move that skill of smart thinking with external imagination to interfaces hidden from users – public and private APIs. How can you use exploratory testing on something that does not have a GUI?Let’s shape up our skills of exploring both the functional and parafunctional aspects of a system through its APIs in their operating environments, without forgetting developer experience of having to maintain and troubleshoot these systems. Let’s learn to be intentional with our APIs, instead of being accidental – through delivering relevant, timely feedback. Intertwining test automation and exploration, we include considerations of the best for today and for the future. For great testing bringing value now as well as when we are not around, we need to be great at testing – uncovering relevant information – and programming – building maintainable test systems. At the core of all of this is learning. What we lack in a set of skills, we can compensate through collaboration. 
> 
> Speaker: Maaret Pyhäjärvi (F-Secure) | https://serverless-architecture.io/speaker/maaret-pyhajarvi/
> 
> 🤗 Join us at the next Serverless Conference | https://serverless-architecture.io
> 👍 Like us on Facebook | https://www.facebook.com/Serverless-Architecture-Conference-251472682389305/
> 👉 Follow us on Twitter | https://twitter.com/serverlesscon/

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

hello everyone
I learned in my previous talk here today
what I should frame myself in particular
for this talk I would call myself what
you know as a manual QA and that might
be something that you understand
hopefully a little bit better and a
little bit differently after this talk
is is done so we'll be talking about
exploratory testing and and computer
interfaces in particular because I find
that the way the world has changed with
having so much of the api's around us
building micro services and
orchestrating micro services it's not
like the user interface is what we play
with anymore it's the whole set of
whatever bits and pieces we've built and
in order to get early feedback that's
definitely what we will need to be doing
so we'll talk about exploratory testing
and I define exploratory testing by the
words of Elizabeth Hendrickson and she
defines it as this rigorous systematic
approach on finding and discovering
risks by using both analysis techniques
you know looking at things figuring out
what they do but also coupling it with
what we call testing heuristics which is
basically a lot of information condensed
overuse of various kinds of technologies
in various kinds of environments knowing
what kind of things are we supposed to
look at so I could do a whole session on
on heuristics alone there's great
articles I actually suggest that you
would go up and and look for them there
was just a recent one published on
ministry of testing one of the testing
testing sites and it's a nice
introduction into it into that right
side of things but expiratory testing
for me it's basically but if I frame it
in some way it looks a little bit like
this on the center of everything testing
there is someone called a tester I don't
care if they're a full-time tester I
don't care if they're called a man you
QA I don't care if they call a tester
they might be called a developer but
it's someone who is performing testing
that's the core of export retesting and
that person is in full control not
someone who was you know managing or
planning things or creating test cases
for them but that person in that moment
what they're doing is they're looking at
the application and they're making
choices they're learning with every
single test that they're performing so
everything that they see changes what
they might do next they might see an API
give a response that they didn't quite
expect and it might make them you know
tweak a little bit on the the input
parameter so that they would get more of
an a response that they did expect
figuring that out and this sounds like a
thing that we do around just building
api's so testing exploratory testing is
not something that just testers do but
the way we frame it the work of
exploratory testing is usually that it's
you know it concise it consists of days
of work you come to work in the morning
you leave the office hopefully after
seven and a half hours actually eight
hours plus or minus their lunch break
and during that day you are supposed to
be doing something something useful in
some structural way and the way that I
offer structure is is this four
different boxes that we we talk about
here you need to have an idea why did
they hire you what kind of things are
expected of you what kind of features
are you looking at what kind of
information are you providing the
current charters what are you thinking
of doing right now what is it that
you're gonna have done by the end of
today and that could look very different
then details as you're testing you make
notes of oh I see this is not quite as I
expected I'm learning a new thing Here I
am seeing something I wanna remember
later on this wasn't quite as obvious as
I thought like all the learning that is
going on you make notes of those and you
make notes of ideas and like oh I'm not
gonna do this testing right now I'm
gonna do that tomorrow and that's what
other charters is and that's just
basically this truck
of things going on at whatever order you
the tester chooses that's exploratory
testing and a lot of times people frame
this into like you know we need these
management frameworks around this so
that we can even understand how this
goes on in organization and the first
thing that you need is of course buck
reports it could be a conversation with
someone who fixes that quite my
preference rather than writing a report
on it
you might want to track all of your
ideas of chartres what kind of things
you would be exploring you could create
some kind of documentation for future
you could create some metrics you could
have someone helping grow in these kind
of skills and just you know you can vote
on how do we perceive quality just with
thumbs or traffic lights color code so
this is the world of exploratory testing
that I know from 25 years in that type
of roles what I could call a man you of
kill a and in that role what I do is I
look at the product I think of it as my
external imagination and I just wanted
to show you a little bit of a demo on
what that actually looks like so in
order to keep things somewhat simple I
took a very very typical thing that an
exploratory tester a manual QA could do
and this is a little Carter so that it
helps us kind of keep things focused and
we very clearly have an interface here a
user interface or a code interface or an
API on a level of of one message so I
can see you know just looking at it it
already is tweaking or tweaking my
interest in the sense that I can see
there's something it has a name it might
mean something it might not mean
something but it has three boxes that
I'm supposed to fill so you know in my
head if I'm used to seeing user
interfaces this is just the user
interface just like any of the other
ones I am supposed to have use this
check item thing putting in things
called item selling and quality and if I
want to know what it does I actually
have a specification for this I'm not
gonna make you read
I'm gonna tell you the basic story of it
this is a shop it's a shop that sells
various kinds of items so the items are
names of items sellings or how many days
you can still sell it and qualities how
valuable is it at that particular time
so I can give these values in I can
check what I what I get out and I've had
a very friendly and nice developer
creating me a single test already that I
can run run and see how things work so
if I put in something zero and zero
it seems that well the quality that I
get out is a zero so just running it
seeing that it still works so I'm an
exploratory tester I might be now
interested in a lot I can start from
from various various angles I can think
of like you know just generating
whatever values and see what comes out
of it I might not even care what the
values are that's one of my options I
could read the specification that's an
option as well or I could go and look at
the code and come up with some of the
choices that I make based on that and
again no one outside is telling me which
of these three I have to do I have
probably my own preferences but my
strongest preference is always to do
something different than I did last time
because that enables me to learn new
things surprising things and be kind of
on the way of serendipity so I can play
with this just you know I can see from
here that there's other things like for
example there's a thing called aged brie
which is supposed to increase in quality
so what if I just change it here zero
and zero well it goes old probably it's
then gonna be going up in value I don't
know if this is how it works but I can
just you know see it okay actually it
went up in value by two I don't know if
that's right or not but this is how the
code right now works so I can you know
make a note of I think it should go up
by one or I can you know figure out a
little bit more on on what does it do
but we don't have much of a baseline on
worried even does the zero zero that we
started with didn't really give us much
of anything
so the zero zero doesn't tell if this
song
thing would actually be you know working
normally in a normal case so we started
off with it already being old and it's
already being of no value
so let's rather have it of some value
and not yet old why did I put three and
six because I felt like it the only
reason that I had on putting two
different numbers is that for me to
track where the numbers actually are
used it is a lot easier if they are not
symmetrical so these are all these kind
of heuristics ways of thinking around
this this application so again I can see
that it gives me now a five so it seems
to be going down by one if it is that
day's number of days so instead what if
I had it already getting old is it now
getting old faster it's like I got now
four so it goes down by two so maybe
yeah the the the age debris was fine as
well what you can notice right now then
what I'm doing is I am not keeping any
of my values the ones that I have
created the test cases here I didn't
keep any of them most of the time when I
do this demo I actually copy-paste new
test cases and I create all of this
separately but what I would rather show
you is that I really hate copy paste
whenever I have to explore I really try
to avoid copy paste so I'd rather use
its this a tool called approval tests
and in particular combination approvals
so I already saw the HB we already tried
selling values of zero and three and we
already saw qualities of zero and six in
the inputs so if I now run this it just
generates me all the options that I had
and again you know this is an exploring
I can again look at things that you know
what I put in something zero and zero
what I got out something minus 1 and
zero so this is actually already
revealing to me that the days are going
down by 1 and it seems to be a pattern
in all of these that the days are going
going down so having full visibility to
over whatever we
doing is enabling me to learn more and
give me kind of like targets off of what
kind of things I might be doing so for
me to now look at this I can say I like
this these are all correct at least it's
how the application is working right now
we haven't yet changed it it was working
in production so I could also say I'm
just you know making my notes making my
observations having my discussions and
leaving those behind and now I can again
see that okay so those tests are now
passing I have documented some of the
observations that I I created I can also
run this under coverage like obviously I
would put my environment in in that kind
of a shape and I could see that you know
the little things that I have so far
created don't get me much of a coverage
and if you're looking at the
specification below the backstage passes
seems to be a short end of what is
actually in the implementation I might
write a buck about that or I might not
again my choice I am in control of what
is relevant to bring out of the
recession but I would definitely want to
take this value in to whatever tests we
have and again now I'm curious on on
what changes and I got a few new tests
so things with that backstage pass if I
put in a three and a six which seems
like a nice thing to have I am getting
out values of - okay so goes down by one
the day seems like a right thing and
nine goes up by three so there was a
rule around these specific concerts
saying that when it approaches the
deadline it actually grows up in value
more remembering that rule that I do
remember because I did read the
specification this is okay as well so I
could again say it's just that you know
I approve all of this I'm not gonna be
fully testing this I could do that quite
easily by just adding numbers here let's
say five I know there was a 1011 sounds
like a good thing since then was of
limit I will use that one as well so
this might be more of what you're used
to thinking of us in exploratory testing
just coming up with boundary values and
things that are perhaps relevant let's
say one because it feels like a good
number as well and just have here also
some numbers like a 50 and a 80 are
supposed to be some limits and again I
can just generate all of this now I
would have 144 test cases it's gonna
take me a while if I'm gonna verify that
all of this is correct but I could also
say that you know since this was
supposed to work before you made any
changes and and the changes are just
coming I am just doing my exploring to
make sure that you're not breaking
anything later on so I have now hundred
and forty four test cases but basically
what I'm just doing is exploring as an
exploratory tester I would really love
to do things like Oh numbers integers
this is a number this is an integer it's
just a binary number so what about that
what happens and I would learn that ok
binary numbers well they are binary
numbers and they're turned into non
binary and it's a very typical thing
again that a so-called manual Cooley
person who has all these rules of what
kind of things might go wrong could do
whether it adds anything to the coverage
it's another story but at least we're at
hundred and sixty two test cases so what
I was doing here and while I was showing
this to you is that what we're basically
doing here is learning in layers and
what I was demoing is what I call manual
Quality Assurance or testing I was
manually creating ways of executing
something that I needed to test it just
happened to be a method like an API so
what I showed was exploratory unit
testing of legacy code legacy code us
and it was already in production that's
how this gilded Rose kata has been
specified
it is legacy code it is really messy
you're supposed to get it on the test
before you make the changes so that
no thinks around that so it was unit
testing and exploratory testing at the
same time what I was also doing is I
combined my ideas of the world like the
binary numbers the specification oh yes
days five and ten are somehow special
for these concert tickets the code and
the code coverage while I was was
testing so I could use all of that
information I didn't quite complete I
wouldn't call myself done at the end of
the hundred sixty something test cases
but I did you know already get some of
it under under coverage under control
and I already have at least two bucks to
report around the shorthand in the
specification and around the the let's
talk about its binary even intended
should we do something about this what
kind of things really need in
relationship to this I used very little
time so my testing was definitely
shallow and if I would use more time if
I would lay learn on more layers then
that would probably be taking me a lot
further and the special thing or the
most important thing out of this demo is
really this idea that I was creating
test automation at first it was
disposable because I didn't feel like
copy pasting I could of copy paste that
could have kept every single test and
run them again later on but the other
tool was really telling me to kind of
like you know easily generate those
values so it was easing up my way of
creating that documentation I still
don't care to keep that documentation
for the purposes of my testing but it
might actually be useful to have that
documentation around for whatever
development purposes we have so test
automation is disposable documentation
you can keep it or you can throw it away
so that's how exploratory testing
actually happens in in this world and a
lot of times what I see is these kind of
pictures that place exploratory testing
on kind of like as a icing on the cake
there's all these different layers of
other kinds of tests that you're doing
before
in the manual exploratory testing is
there on the top but people are actually
doing this layer here with the demo and
yet we were doing that so it has never
actually been there on the top we have
just put it there on the top it's always
been a part of every single layer here
so what I usually do with this picture
is like please don't show it please
don't make it go around draw it
differently that little cloud needs to
be clouding some part of all of these
different layers of our test automation
pyramid so exploratory testing is really
something that drives our creation of
automation and we can make choices
whether we keep things for us or not so
let's do still talk a little bit more
about the the api's specifically so the
API that I showed you right now was a
very very low level for the purposes of
not having to use network and not having
to introduce you to into anything more
complicated than that
I have also of course examples on using
public API sand and checking values on
them very same principles apply there as
well like if you can see the hole
headers and hole responses rather than
choosing just one that you picked and
picked to be looked at you're gonna find
surprising things out there but the same
principle you know you can do that done
on REST API so you can do that on
libraries frameworks languages methods
command line interfaces and pretty much
any kind of interfaces that we are
creating these days and there's
absolutely no reason of leaving the the
critical thinking with your application
as your external imagination telling you
hints on you'd want to do this you'd
want to try these values you don't want
to leave that for later on so you want
to do this already earlier and it's not
that complicated
you just do something with it you find
out what why would anyone want to use it
what's the common thing of what to do
with it and you try things that you were
not supposed to be doing
with it as well making sure you're
learning as much as possible in layers
so that you're always in control so
don't start with the most eccentric case
at the time when you had just a nothing
yet about the application that's not a
proper exploring but kind of know
knowing where your home base is and
taking trips from there keeping safe
that's what what we do in in export
retesting so having done this for
various applications for example for
that approval tests framework that I was
using as part of my my testing demo I've
collecting collected some patterns the
reference that the approval testing
framework general the creator gave me is
that I looked at his framework and his
api's for like an hour and a half and I
totally destroyed it but actually I
didn't destroy it the only thing that
got destroyed was the illusions of it
ever having worked properly so showing
things around discoverability showing
things around how you use that in an IDE
how you set up a realistic environment
all of those things were surprises to
them rather than than things that they
were already aware of but they were
things other people were experiencing
and to get some of that message across
to this person I actually had to collect
together a little bit of a mob of people
in a conference so when he watched about
ten people recognized agile technical
experts in a conference not being able
to use his API because it was way too
complicated and undiscoverable then he
said basically he would rewrite that to
API and rewriting API so later on you
probably know it's not gonna be an easy
thing to do when it's already in use in
real projects so that's been a a problem
since so some of the patterns you work
with a limited understanding so you need
to focus I talked about this idea that
you are in control whenever you are that
tester you are the center of that
process and you are in control of what
is it that you
can learn what you can grasp what you
can do so if you can take big steps
because you understand all of those
things you know by all means take big
steps but it might make be helpful to do
this kind of like a switch in between
sometimes taking smaller steps sometimes
taking bigger steps because it enables
you to see things that you had not seen
before so I often find myself not doing
the same thing twice even if I do the
supposingly same thing I can at least
use a different set of data and it is
always a chance for seeing new things
but focus deciding what you're doing
making those choices is important you
look at what goes in what comes out and
this is kind of straightforward but it
is important to see all of the things
that go in and all of the things come
out so so making sure that you're open
to those surprises and you don't already
kind of narrow your lens is something
that I would advise as a good pattern
for exploring on APs
then understanding that the environment
might also have somewhat of an impact so
probably there's gonna be some
dependencies versions of whatever other
software that people have in different
ways and your test environment can
include those and it changes what you
will learn looking at your users what
the users look like and in particular
the developer experience is the user for
our API so I know but I have at least
heard a great number of swearing from my
developer colleagues using third-party
api's available in in various platforms
not only on how easy or difficult it is
to build things on the first time but oh
my gosh
how difficult it is when something then
fails in production and you have to go
and begin where the failure is is it our
things or that third-party thing and
having information available for that
purpose so the experience is both right
now and also for the later
asking for the purpose is also a good
pattern why would anyone want to use
this what's the purpose of this data
it's not because someone specified it
there was a greater reason behind it so
maybe we want to to ask around it and
not just asking why would they want to
use it but also think of it as in it's
gonna have a life a life cycle it's
gonna be there you know for the first
time it's gonna be updated we're gonna
want to change it and all the practices
around how do we version our api's like
that's probably one of the most painful
areas where I have to find problems at
too late stages of the project if we
haven't thought about the way we version
our api's and we really have to always
be backwards and forwards compatible
with all of our changes so knowing that
talking about that making that
information available and part of your
discussions is is an important thing and
of course killing it is it's relevant as
well if you learn a concept that you
don't know like I I did when I started
working on api's like I heard about
conservative overloading start strategy
you know figure out what does it mean if
someone uses words you don't know one
you don't want to ask in the moment I
usually rather ask in the moment there's
always Google so every day is a chance
of of understanding this a little bit
more and you don't have to do all of
this alone
collaboration is always encouraged
documentation it matters for approval
tests in particular the documentation
was
images of code samples you can imagine
how much that annoys a developer when
you can't even copy/paste so again a bug
of relevance even if not directly in
that particular code and your
exploration creates documentation just
as much as any other form could then
actually want to move into this one last
pieces of advice
the role of automation into this is that
when you're working on an API you really
have even the so called manual QA is
doing automation saying anything other
is it's kind of funny they might not
know all things programming but they can
do this stuff even if they very much
identified as non programmers and as
many oculus so for them or in general
the existing automation that you already
have that someone who knows more of code
maybe it allows them to use it and play
with it and you know generate for
example hundreds of similar things many
events rather than just one or start
actively changing some input values and
play with it and then use that for
documentation when you create automation
it really is like you're looking into
details so you see problems that you
never did if you didn't go on the code
level so that's a a a good side as well
and when the automation then fails
because it does fail it always does fail
and not always because our software is
broken it is an invitation for us to go
and explore some more so there's
actually no difference in how the manual
queue is do things to how the automation
queue is do things except that the
manual queues are just starting their
journey on learning how to work with
that code and you should bring them
closer to that that work so to sum this
up we have really two kinds of testing
we have what I would call testing as
artifact creation usually this is very
much the decide that we see on the test
automation communities that kind of
automation or that kind of testing gives
us specifications you know we know what
we're building if we have an example of
hand feedback did we actually build
whatever we specified that we was
supposed to regression does it stay
working after we created that and
granularity when it fails this is the
reason it documents the reason and
that's all awesome great and wonderful
whereas the exploratory part
what kind of gross this and makes it
bigger and it is requiring attending to
create more of the oneth automation it
gives us more of a guidance this
direction is better than that direction
it gives us deeper understanding we can
model things we can create ideas of what
we already know and what we don't know
and serendipity lucky accident of
finding the problems that we otherwise
have to experience first time in
production and not all of them very
happy and are nice and all of these
things just go on continuously as we are
making hopefully releases all the time
there's just a little bit different peak
times of them so you can explore while
in production even for your api's so
that's kind of what I thought I had in
mind as final thing I want to encourage
people to remember that learning is the
most powerful thing this is part of
almost all the tops that I do nowadays
if you stay the same you're still the
same in a year if you get one percent
better whatever that way of growing is
you're going to be 37.8 times better
than you were in one year so there's
nothing better than learning and I feel
that exploratory testing at its core
it's only about learning and the expert
nowadays are the ones who learn the
fastest not the ones who know the most
so that's the thought that I want to
leave you with thank you
[Applause]
[Music]
[Applause]
