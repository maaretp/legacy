---
title: "Breaking Illusions with Testing - Maaret Pyhäjärvi - DDD Europe 2019"
video_id: v0pNA8a7dbY
url: https://www.youtube.com/watch?v=v0pNA8a7dbY
upload_date: 20190514
duration: 48:25
channel: Domain-Driven Design Europe
tags: [ddd, dddeu, dddeurope, software, software architecture, domain-driven design, testing, modelling, domain modelling, unit testing, integration testing, user interface, ui]
---

# Breaking Illusions with Testing - Maaret Pyhäjärvi - DDD Europe 2019

> Domain-Driven Design Europe 2019
> https://dddeurope.com
> https://twitter.com/ddd_eu
> 
> Breaking Illusions with Testing 
> 
> As a tester, I don’t break your code, I break your *illusions* about your code. My work centers around finding the model you’re missing out on, to discover what you don’t know you don’t know, or things you know but have forgotten. I focus on identifying theories that don’t hold true in a world that is empirical. I break illusions so that with the information we have available together, we build systems worth using for various stakeholders. 
> 
> This talk gives you a perspective into how a tester models an application domain through using software systems as their external imagination. We look through examples of illusions that need to be broken and skills you need to break them. 
> 
> Illusions come in many forms. Illusions may be about the code doing what it’s supposed to; about the product doing what it would need to; about your process is able to deliver with change in mind; people having the skills to deliver well and about the business growing with uninformed risks on the product and the business model around it. 
> 
> Testing is not just the technical checks but more relevantly it’s about discovering information about threats to value you’re trying to create. If you have little concern for the domain understanding, you are likely not doing a brilliant job at testing. Assume less, research more. See things others don't. 
> 
> Biography
> Maaret Pyhäjärvi is feedback fairy with a day job at F-Secure, where she works as Engineering Manager. She identifies as empirical technologist, tester and programmer, catalyst for improvement, author and speaker, and community facilitator and conference organizer. She was awarded as Most Influential Agile Testing Professional Person 2016 and has spoken at event in 24 countries delivering close to 400 sessions. With 25 years as exploratory tester before stepping into a role to manage developers, she crafts her engineering manager job into being a mix of leading a team of 12 and doing hands-on testing. She is a serial volunteer and organizing powerhouse contributing to European Testing Conference and Speak Easy, as well as Finnish non-profit scene. She blogs regularly at http://visible-quality.blogspot.fi, posts articles on Medium and Ministry of Testing the Testing Planet, and is author of two LeanPub books: Mob Programming Guidebook and Exploratory Testing.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

good morning everyone
we're gonna spend a while talking about
illusions and in particular breaking
illusions so the story starts
and a few years ago I would like to say
not in a galaxy very far away just you
know in Finland where I'm from and I
identify very much as a feedback fairy I
have my golden wand and all things like
that feedback fairy meaning that I
usually work in teams I come with a gift
of feedback and many people would call
me a tester so what I do is testing what
I love is testing and I really enjoy
working together with whole teams and
and doing all testing related stuff and
a few years ago I wanted to do a session
for a conference about testing something
without a user interface so I took a
look at somebody's system there was a
nice developer who kind of volunteered
that you know if you want to test
something in public you can test my
thing like you know I don't mind and
approval test it's basically this their
testing library where you can create
golden master files and there's no user
interface like any unit testing things
it's something of that sort like yeah
sure you know I'll take that I don't
really care what I'm exploring what I'm
looking at you know probably there's
things that I'm gonna be finding and the
end result was this so the developer in
question an American man with a little
bit of an attitude sometimes he kind of
got surprised he said that whatever I
was about to do on his thing in a couple
of hours I broke it I destroyed it
completely and the words that he was
using kind of were pretty strong on on
that side so I took the challenge I
spent some time with the application I
didn't think I was doing anything
particular you know like I set it up I
set up the environment I look at the
documentation
I tried to use his unit test that he had
for the system and you know pretty much
none of that worked quite us as I would
have assumed and the the API itself
it was completely undiscoverable for
somebody who was new with the
documentation at hand so sure you know I
broke something but it wasn't actually
his software that I broke it was just
his illusions and this is what I keep on
doing like you know this one thing a few
years back it's just a reflection of all
of the things that I've been doing for
the last 25 years and I absolutely love
doing testing I love looking at things
we believe in I love looking at the
software and figuring out if it works as
we intended or if there is something
some information that I could bring back
as a feedback very hopefully with a
smile on my face and not you know
delivering the message of you know by
the way your baby is kind of ugly in a
nasty way but rather you know figure out
a way of approaching things as in like
this is a bug that is so cool that I
can't even believe that somebody would
intentionally do this this is actually
not intentional it is just surprising
and a lot of the things that I keep on
finding I like that so I spend my time a
lot breaking illusions but I've been
doing this for 25 years
so kind of like you know looking over
time like I feel like I've always been
doing testing I've always been a tester
but yet I find that when I look at
people joining in the industry right now
they're very much doing different things
than I am I don't even know this when
I'm growing so I also identifies a
polyglot programmer a couple of years
back I realized I've been programming in
50 languages but I never talked about
that really right now for the last six
months I've been a manager of a
development team of 12 and I worked my
ass off I don't know if I was allowed to
say that but I work a lot for the idea
that my job still looks exactly the same
as it used to look as a tester so there
are many things where you can change
roles and grow and do all kinds of
things but there's still some kind of a
home ground that you identify with and
this breaking illusions
and the skills around that I don't think
it's just something that testers need to
learn testers cultivate that skill often
because when you have your mind space
focused on a particular thing and
learning that thing you know if you're
actively learning you're usually getting
better at that right but instead of
thinking of this as only testers doing
it I find that some of the best Explorer
some of the best testers in my teams
that I've worked with in the recent
years are developers business analysts
all that sort of groups so for me
looking at these basic illusions or the
breaking illusions it kind of splits
into over time I've been thinking about
this a lot it splits into six illusions
that I find that I need to spend time on
so the basic ones are things around you
know what people usually assume testers
might do looking at the code whether it
does what it was supposed to do like if
you know programmer had an intent it had
a specification it had somebody's
expectation of what it was supposed to
be doing is it actually doing that and I
would wish that in the current
test-driven test oriented test infective
teams world I wouldn't have to find so
many problems around this and I am
really happy with the 25 years of
timeline to notice that this is now a
very very small portion of my time in
general like you know if we know what we
want there are many people who can could
check for that but then there's this
whole space of like what we wanted is it
what we really really wanted is it what
really matters to the users whether
that's the right thing to build and a
lot of times did we know enough about
the environment that we were building
for so that's another thing that I often
find myself looking at and the third
basic illusion is well security related
things I work in a security company
especially right now so for the last two
and a half years and I find a lot of
times finding that you know there's this
remote execution possibility it wasn't
supposed to do that but if it does that
I would like to know
and these are kind of like you know
everyday discussions around what kind of
feedback we might might need to be
delivering what kind of illusions need
breaking but I also with the 25 years of
kind of like growing and taking
different kinds of roles and different
kinds of responsibilities and actually
not taking different kinds of roles but
just responsibilities I find that I'm
also doing other illusion breaking
around things like are we working in the
right way is the process something that
we actually you know enjoy and like
whether the people actually know how to
do things properly if they should
actually go on a training course or or
you know just pair up with somebody else
or learn things that way and also with
the business models but like this is a
list and this doesn't actually tell you
much about what does it really mean in
practice so let's look at a little bit
of that practice like what does it look
like what did I actually do what what
was it that I did I thought was nothing
but apparently it was something because
this developer with the open source
project and and all the focus on
test-driven development didn't manage to
find all the problems that I managed to
find so what I did basically is that I
looked at the API the the product the
application that I had kind of ass as if
it was supposed to speak to me and with
25 years of program whispering
experience it actually does speak to me
I don't think I'm completely insane but
I do hear applications all kinds of
interfaces telling me who you'd want to
try this value you'd want to click here
or you want to do that twice there was
something interesting that you saw the
first time maybe you didn't pay
attention and I am a lot more creative
at discovering that new information with
the program in front of my face with a
picture I can also do a lot of things
with the post-its on the wall I already
can do a lot of things there also one
kind of an external imagination but
there's something particular about the
real executable application that makes
you learn more vivid things so the first
thing kind of that I did is
I follow this main rule B usually in
testing we call these heuristics my main
heuristic is never ever be bored and
some people who have ideas about what
testers do this might be you know
completely against whatever you're
thinking about testing but I have to
tell you that I have never ever done
boring clickety-click work before I
became a manager then I have to go every
single week and press the approve button
for people's hours I never ever did that
as a tester so when I look at an
application as my external imagination
I look at it and my kind of like past
experience with it as in what have I not
yet learned what new could I bring into
this you know spending time with this
and what did I do last time so that I
can intentionally do things differently
and this increases my chances of running
into problems that you know nobody
expected another heuristic is that when
you start off with something you can't
actually expect very high high things of
you know doing the best job ever
search sure you have your your history
and your knowledge from the past
projects and all that but every new
system is a new system you need to be
actually approaching it as a as a new
problem and you're learning about that
particular problem and you're trying to
be aware of the things that are baggage
from your your old past experiences and
also the ones that you know it would be
usable here so again the idea of
changing whatever you can and this
heuristic is particularly important in
the sense that the first thing that I do
is not that I write test automation the
first thing that I do is not that I
create test cases the first thing I do
is I explore the application before I am
ready to create documentation and then I
can decide whether automation in nine
times out of ten is the right way of
documenting that result of whatever I
was discovering with the application and
this is actually how test automation is
built in general someone first discover
stuff about the application how long
they spend on discovering before they
start creating documentation there's
many variances
to that but you don't do that when you
know the least that usually means then
that you would have to rediscover things
if you would go for that so for that
approval tests in particular I had to
learn it a little bit write some notes
for myself but I wasn't intending to do
automation but you can't run an API
without automation so I had some
throwaway automation a third thing again
heuristic going into more specifics is
this idea that when you see something
that you can play with you keep on
poking it this is something alexander
slavic a lady from from germany suggests
that actually a lot of testers seem to
be doing so we're naming these
heuristics very actively so you keep on
trying until you know you find something
and when you're persistent with whatever
you're learning and and you want to
really understand that deeper that is
usually providing you more information
but I also have you know this whole
history of working with testing and all
of the heuristics for quite some time I
know that you can't read all of those
heuristics but we have loads of them in
the testing community and we share them
very actively so the heuristic table of
testing has some of the things kind of
like how you approach things like idea
generation how do you know if things are
correct consistent with different kinds
of things
there's approaches on how you could test
how you could look at non non functional
aspects so there's many many different
ways of approaching a problem and when I
go into a new product looking at that as
my external imagination this is the tool
set that I come to the product with like
I know all of these heuristics and
there's one particular one that I
applied first with approval tests so the
first thing that I did with approval
tests is that I you know was looking at
it and I wanted to kind of generate
ideas from from different perspectives
so you know it has some kind of
structure so I opened the the the the
IDE and I I browse through whatever
structures they were I realized that
there were some some names that I didn't
like
didn't understand you know already
building a mental model of what that
structure looked like but usually going
to developers code that's not where I
provide the most value in couple of
hours so what I focus on first usually
is functions you know what do I do with
that I also would look at things that it
can eat what kind of data it takes
what's the platform it kind of resides
on what's the environment it requires so
I also kind of built this environment
where it uses couple of drivers on my
different language systems and I was
comparing between different languages so
all of these were generating ideas on
you know I'm making choices I have very
little time and I want to provide some
useful information I want to help and
teach people how to do that and also
operations kind of like long term things
like why would anyone want to use this
type of questions and time usually time
is something that is always difficult
when you you identified with an
application so I looked at things I
couldn't make sense of things easily so
obviously I wouldn't spend time alone in
my chamber I had the developer so I
asked him like what is this supposed to
be doing and he gave me this list like
you know one half of it called approvers
does this the other half of it called
reporters is supposed to do this I'm
like whoa rich source of claims I can
test against any of these and again I
can easily spend weeks actually finding
more problems with every single one of
these and yet still I have only spent a
limited amount of time trying to find
find problems in that I also drew this
kind of like a sketch for myself you
know a model of of what kind of
environment it sits in so it's somewhere
in the middle it uses all kinds of
things test runners diff tools
documentation exists all that sort of
things so the things I had to find is
that the unit test didn't run on my
machine or actually some of them are all
they had forgotten to put in the latest
changes towards the unit test that we're
fixing them so they actually had a
broken version out there so that was
kind of like the first thing that I had
to discover then the second thing that I
had to discover was that when I had two
runners I was doing c-sharp first
and I had both in unit and another
runner on my my environment it wouldn't
actually start at all
so apparently no one had told him or
even tried you know using an environment
multiple runners it was supposed to be
working there was no reason why he
wouldn't accept that it didn't and then
I tried copy pasting from documentation
finding that it was any G's so you can't
really copy paste from images and then
kind of trying to discover the API was
really difficult so there were many many
things that kind of from different
perspective ended up coming out and of
course since I was learning about the
application in a limited time I was also
making loads of notes on what kind of
things I was learning and categorizing
this and I would love sometimes to take
a video of how these mind maps that I
create while Alan testing how they kind
of like emerge how things change and
move because even negative space empty
space or unbalanced view in a mind map
it's actually his heuristic that tells
me that there's either wrong model for
me here or I am missing something and
all of these kind of things are things
that I might want to be reacting to so
this is an example of doing things with
an application like I do this for my
work all the time I approach different
kind of features this way I get involved
early on if we're ever doing any like
white board work I try to do it there as
well but a lot of times listing all the
possible ways it can break very early on
it's by the way the best way to kill
something that actually could be
valuable but you haven't yet quite
figured it out so sometimes that's the
reason why why some testers are not
always welcome in the the early stages
like if you feel half of the time with
something negative that might not be the
best way to do things but then again we
can all prioritize but I also realized
you know that's looking at these basic
illusions but there's a bonus one
clearly on top of this this approval
test experience and highlights which is
around my current work so
there's also this illusion that whatever
we tested whatever was the best that we
could do while testing we think that
it's you know good enough and and you
know we already found relevant bugs and
we fixed many of them but when you put
things in production you can have things
like them we have this one system that
I'm testing right now with 1 million
users about give or take 1 million users
and when we started introducing through
testing ideas and like we want to figure
things out like how does it actually
work telemetry so that it tells us when
errors happen we realized and about half
of the people who are trying to use it
actually are not able to use it and we
learned that that has been the case for
years and yet they don't call home so a
lot of times this is the change that I
need to be driving this is the illusion
that I need to be driving that the work
we do in the name of testing within our
companies already is sufficient usually
it isn't the real users are so much more
versatile that we want to get the the
feedback feedback from them as well but
again I've spent few years on learning
to do this stuff and configuring out
what kind of illusions are there and I'm
realizing that while I still spend more
than half of my time hands-on with the
application and and enjoying the fact
that we are releasing fairly
consistently about every two weeks every
week into the million users that we're
serving they are Windows machines so the
continuous delivery means physically
installing 1 million machines somewhere
out there across the world so that's a
different level of continuous delivery
again an illusion that I was told 2 and
a half years ago it's impossible to do
seems to be quite possible we're doing
it right now
so there's many of these things and
claims that people have where you
actually when you have this mindset of
paying attention to illusions you feel
like oh we need to change the world like
it's not really like this so the first
type that I wanted to talk to you about
is this illusion of business models like
we believe
that you know whoever represents the
business we have some people who
represent the business and even in in
this audience we somehow believe that
they have this magical information that
they know what actually the end users
are willing to pay for and they usually
know a lot of that stuff like they know
how to go and ask the users and and the
users will give you you answers like oh
yes I would absolutely love that feature
in my previous place of work we had one
of those cases where we were asked to do
a relevant sized feature and we went and
asked the user unlike would they
actually want that and oh yes we
absolutely loved it we we need it and we
started working out all the details of
how they want it but I was sensing that
there is something fishy here there's
something that I am not quite convinced
with and what I wasn't convinced with
was the the sales people's belief that
this is gonna make more money for us and
that this customer actually would be
willing to you know put their money
where their mouth is so I devised a
little test I went to the business
people and I suggested that what if we
made a contract that they paid you know
five ten percent it doesn't really
matter but you know contractually we
bind them and they pay some money
upfront you know you can even have all
the money up front I can make a promise
that if you know that is you know
something that they want like you know
we'll figure out a way of delivering
that incrementally so that they don't
have to wait their whole life it's not
that big we can make these arrangements
and we went and did that
and what we learned is that the customer
wanted the feature as long as it didn't
cost a cent so sometimes these kind of
illusions where you know you think you
do all this work and it pays off they
are the most expensive illusions that I
find that I have to break with break
breakers and and also things around kind
of how much do we need to test and how
much good quality something needs to be
before it hits the users the first time
it's an illusion that I find that I have
to break with the testing community a
lot of times like we don't want to
invest upfront all the money when we
don't actually yet know if the customers
are really going to flock in with the
a church that we have have in mind
there's also this little nice illusion
that I find myself telling stories about
around how we deliver software a lot of
times people believe that when you get a
bigger thing it's gonna be cheaper and I
really enjoy this Allen Kelly's
illustration that software is really
actually cheapest in the small cartons
and this is pretty much the illusion
that I I work with when I want to
deliver every two weeks every week to
the million users so that we can control
the risk that is related to us breaking
the systems that that we're building
then another type of illusion that I
find myself breaking a lot of times is
you know people and skills related and
having kind of this dis knowledge and
and understanding on how things work and
I wanted to take a specific example of
this so two and a half years ago I
joined my current team and I absolutely
love and adore my team but back then we
were a little bit challenged we were a
new team we hadn't really worked
together so we did some team-building
related activities and I organized this
team-building when we went to this
escape room called Hannibal so there's
the serial killer that is after you and
you have one hour to escape like you
know or something to do with with your
teammates
but there was one detail that I didn't
tell my teammates about this fun
experience which was that I had been
there before I actually haven't
officially told them still yet so maybe
they will learn after I talk about this
on this stage I've done it on other
stages so yet I have been safe and it's
also on my blog it has been already four
years so you know it's not like it's
private information but I didn't tell
them that I had been there before so I
wanted to you know figure out if if we
work as a team and in particular how I
the tester in that team was treated
heard and listened to and it was kind of
interesting you know people being in
these different places and
and trying to get out and and I was
trying to interject sometimes you know
when people first figured out themselves
like I wouldn't do anything I was just
you know enjoy the ride
but when we got stuck like I knew the
right answers there was this one
particular case where there was this
table and you had to actually you know
get on that table with your hands no all
the way out there and had to scream you
have to scream your lungs out that was
the only way to go forward and there
were hints you know giving us this
information and I knew this because I
didn't figure it out last time I was in
the room and I counted 12 times of
mentioning that in different ways kind
of like trying to highlight it to my
teams and then actually the final thing
having to physically get on that table
because I wasn't listen to the
information that was correct wasn't paid
attention to so sometimes the skills
that we need to build in the teams are
the skills of hearing everyone and in
particular when we're doing design
related work when we're doing
implementation related work the best
ideas are not the ones necessarily where
people shout the loudest but there might
be really good ideas actually usually
there are really good ideas from the
people that we normally don't get to
hear so this might be something to pay
attention to then the fourth special
type of illusion it's about the
processes the ways we work and this is
definitely my all-time favorite illusion
nowadays to break so I still enjoy
hands-on software and I you know I cry
little tears if I can't spend my time
with the application that we're building
every single work week but this is where
a lot of my energy actually comes from
comes from so the process is the ways we
work they might be very different in in
many ways so one of the illusions that I
particularly enjoy is this one about how
it's effective for us to work so this is
a picture of a meetup group I'm one of
the people there in the
in the picture and we're all staring at
this one screen where this one person on
a computer doing something so about four
years ago I had a pleasure of meeting a
wonderful gentleman actually here in the
first row with his will and he did a
talk at a conference I was organizing
and he talked about this idea of mob
programming using only a single computer
as your your entry point to programming
and having the whole team work in a
particular structure and I was like
that's the craziest idea I've ever heard
like that's not gonna work and this is a
heuristic that has also before proved to
be really really powerful for me so when
I recognized myself thinking that is
impossible it would never work I tried
to stop and think unlike but that person
you know that's a smart person
they have real experiences maybe I'm
wrong maybe they're right and I can't
say that if I didn't try that again with
whatever I have now learned about the
thing that it's actually so bad thing so
I spent some time probably three four
six months I don't remember the
timeframes exactly anymore I spent some
time convincing my teen that that you
know we would want to try this thing
called more programming and they were
absolutely refusing like no way that's
the stupidest thing that we could ever
have had heard and overall then I
figured out that the best way to get
that done in my Pentium was to say like
oh I'm feeling kind of lonely here I'm
the only tester I don't you know I don't
get enough attention I I you know need
to you know humor me a little bit here
and they said like okay fine we can do
anything for two hours for you like that
thing is stupid still but anything for
you for two hours and we sat together in
a room we had a facilitator we were
doing refactoring cleaning up code
renaming pulling out methods
restructuring things committing
regularly and we learned tons in that
two hours about each other about the
waste different people worked and also
about the the status of what kind of
models what kind of things we had in the
and how that matched whatever models I
had so this was a good experience there
was one person in my team who didn't
really enjoy it much they said that it
feels like we're in kindergarten and
also then we learned that you know if
people don't like it you know it's okay
for them to opt out then the rest of us
can have the party and and well with
about six months of doing this every two
weeks they said that oh that looks like
a fun thing can I come join so again
when people are clearly enjoying
themselves and having fun it invites
them them in but for me the main
takeaway from this whole mobbing thing
was that I had forgotten that I have a
computer science studies thing behind me
I had forgotten all the languages that
they made me program in in school I had
forgotten that I can actually do all of
that and I realized that you know I can
start doing it again and I also found
new ways of doing it for example the big
insight for me was that real
developers.googl nobody told me that
what's what's the deal with that so I
wasn't actually so bad
googling and these kind of things can
like open up things for me and also
looking at my blog I realized that I was
saying I will never want to be a
programmer and now I'm saying I'm a
polyglot programmer I kind of
confidently you know do that with my my
teams and pair up with with different
kind of people so this idea of cognitive
dissonance sometimes things that are
part of your identity you feel you don't
do them because they are not you and
when you end up doing them kind of by
accident you rewrite your whole history
and that's what what happened to me so
there are big big illusions that we need
to also break on our own belief systems
and and this whole idea of programming
was was one for me I also do a lot of
process related illusion breaking in my
own organization and I know that I
probably have people hating me for them
no no no no lists but that's actually
the easiest way for me to describe the
ways we've learned to work in in my team
right now
well we do continuous delivery we talked
about that already and the continuous
delivery is not kind of the usual
continuous delivery because there was
the little illusion of yeah we can
install million machines every every
week if we want to so
the AWS related services actually made
that made that much more possible than
it used to be back when we were telling
that that it is completely impossible I
stopped using JIRA years ago like I am a
tester and I don't write JIRA tickets if
I can avoid it and what it means is that
the ten minutes that I could write the
ticket on I used that ten minutes to
walking to that person or talking to
that person making a call to that person
if they're in a different different
country and I make them see what the
problem is and if they're like oh you
know can you write me a JIRA ticket so
that I remember it later it doesn't seem
to be very important so you know you can
just forget it or you can make your own
notes you know that's an appropriate way
of doing it or more likely like you know
I have time now we could pair I could
learn something while we're pairing like
I love doing this this stuff so trying
to kind of introduce a more
collaborative way of working
no estimates is something that I avoid
mentioning usually in public because
there's so much weird discussions around
it but the simple idea of rather asking
like not asking how long is it gonna
take for us but why can't we make it
smaller that's so powerful that with the
time of not doing the estimates magic
we've done other magic for our end users
a year ago we got rid of our product
owner it happened so that first they
were sitting in our room and everyone
was sort of reporting to them so the
team dynamic was bit off in that sense I
first went to the product owners manager
and asked if the product owner could
move into another floor it's kind of
like you know shipping them to another
country that's how it works and yeah a
few weeks later they changed the room
the team was completely in a mess trying
to figure out who do we talk to know
that we don't have the one person to
talk to and we figured out that we could
actually talk to each other and then
over time we realized that you know it
was so difficult you know you have to
ask that person who wasn't
in the room what do you want to ask like
what does he say actually realizing that
we had most of the answers already in
the team so we introduced this idea of
of not allocating the most important
problem that we have in software
development which is the customer and
making customers awesome to single
person and single row but actually
sharing at a promise to us we changed
the product owner kind of as it was
before we changed it into this this idea
of of you go fishing for us like if
there's a gazillion customer meetings we
don't want to sit in those at least not
all of them because there's so many of
them you go fish
bring us fish and remember if you bring
us a bucket of fish so that we can make
food for the family for dinner and we
only need to fish to feed the whole
family and the rest of it is probably
going to rot so you know pick the best
fish instead of carrying it all around
it's gonna be heavy work for you as well
so it just you know improved a lot of
the the ways we work with the customers
and I was kind of happy to realize that
next week again called one of our
customers and partners and said like hey
can you come over to tea talk to our
development team oh yeah sure what time
would Wednesday be okay
so having this this kind of relationship
where even in a product company with a
lot of customers you can actually call
different ones to get the the
perspectives without the filter that we
have at least learned that it's actually
seems to be creating illusions rather
than than dispelling them so we did that
then no product projects is a thing also
we try to do so continuously flowing
features through the whatever machinery
we have rather than setting up these
these big elaborate things the whole
organization is still very much on the
projects but but mightiness is trying to
work on a bit different way and no scrum
basically meaning that whenever
something is ready can come bound style
like pulling it and and putting it in
production if it's valuable enough
there's no reason why we actually need
to have a cadence for for releasing we
have brought all of that stuff down what
so all of these things around illusions
they're really about learning
they're really about the idea that when
you go to work
I would hope that every single one of
you go to work with the attitude that
every single day is a chance of learning
software industry seems to be doubling
in size every five years which basically
means that if we have a representative
group of people at our work or in this
kind of setting about half of us would
have less than five years of experience
we don't all have all of the knowledge
and experiences but we can definitely
get started with with learning it's not
about someone knowing kind of absolutely
more than somebody else we all have
things to learn from each other and some
of my fondest memories of learning in
the last two years come from the fellow
who joined us two years ago at age of 15
and me forcing them through all kinds of
things including talking on a stage in
front of 500 people at age of 16 so
there's many different ways for us to
learn but it starts off with
appreciating that we want to do it and
every single contact we make with others
it's a chance of doing that looking at
things from this pester kind of
perspective you have this idea that
whatever someone models I'm talking to a
modeling community in particular
whatever someone models when you look at
it differently you probably are going to
see something else so no matter what
model my team's draw me I will always
draw another picture that looks
different there has never been a model
that I can agree with because I never
agree with myself when I sleep over the
night and it is really useful in
breaking those illusions so from one
angle yeah sure it says you can look at
it it looks like a cat the other angle
it says it's a bird but actually the way
I look at it is not whatever the label
say I'm noticing its hand-drawn you know
some of the lines are a bit you know
fluffy like they they're not quite
strongly drawn and I wonder if that's
intentional if it was me no meant to be
that way
maybe it's supposed to communicate
something maybe you know maybe there's a
thing that I could see just focusing on
that particular aspect I'm also seeing
some kind of shape some of them are
closed some of them are open
maybe the shapes mean something and just
the color of the paper seems to be
really complicated did have you know
entered into this particular picture so
that I can't turn it into nice and white
maybe there's an intention behind that
so all of these things kind of looking
at whatever with curiosity in mind and
figuring new things out it brings brings
me in your perspectives so what I do I
again break the illusions I sometimes
show up at office and say hey do you
have an hour let's play I did this this
week just for the purposes of of this
conference and having something really
fresh for you that's my 17-year old
colleague right there in the front the
other one has a little bit more age than
than the 17-year old and well you know a
very nice group all in all we were
testing these boggle cubes which is
basic the game of Scrabble the word game
you mix them up and you try to generate
different kinds of things or different
kinds of words and what comes out of
this I was well we found bugs of course
but what I really wanted to go for is is
to understand what this group of us
together what did we learn this week
about testing that we either didn't know
or had forgotten so the first lesson
that we learned is that if we try to use
these kind of systems like we were users
we're probably not going to do a really
good job of testing there's more intent
to testing than what users have a users
intent is different testers intent is
kind of like fast-forwarding the whole
production in in shorter time frame and
understanding where the risks are a new
information might might be so we
realized that
there was a clear difference in in you
know just using it to figure it out and
intentionally exploring it and trying to
figure things out so we also kind of
drew this on the background you can see
this this text here we listed all the
features that we could find when we were
exploring and that was a big part of
that the being intentional but then we
also realized again being reminded that
the intent isn't enough like you know we
can think we know things and we know
what we know but honestly we don't not
know the things we don't know and we
can't prove that information because we
don't know we're missing that
information so through that play the
thing that comes up with is serendipity
a lucky accident where you will run into
a problem that you did not expect like I
had no clue you could do that like there
was no hint saying that he could do that
but he could and with the boggle cubes
we had three sets of the vocal cubes the
surprise for us was that when we have 15
of them we can combine them in
interesting ways in the middle of the
game and Meister came up in in ways that
probably no one intended and we really
didn't think of that as as a thing and
also we could play with more than nine
five five cubes and and and work on on
that kind of things the third thing we
learned is that the intent means kind of
recognizing your own control when you
realize that something is very difficult
to do like we had this you know randomly
given letters and we needed to combine
them in some way five letter
combinations when we started generating
those they were really really you know
long list of things I can't actually
calculate that in my head or remember
how many it is but the list was quite
long then we realized that we can remove
one cube and we have followed their
combinations and that made the problem
of what we're testing a lot more
manageable so again controlling things
controlling variables that you recognize
that you have you can do first the easy
thing it doesn't
mean that you don't do the hard thing
you can do the hard thing when you have
first learned how the easy thing works
so understanding kind of your power and
and the fact that when you've done it
once you're not done it's a big part of
how I test on testability we were really
frustrated on getting always a different
random five letters so you could never
verify if the score you got or the
maximum score line was our focus if the
maximum score was possible like you
couldn't you know make a list of things
and get the exact same letters so that
you can try to see if if you can get the
max score that was way to complicate it
because you didn't have control over
these these cubes and it just reminded
us that whenever we feel this way with
our applications that's the time to
bring in the developers to join us the
designers to join us the business people
to join us and share the pain of trying
to do it and usually that then means
when the pain is shared the knowledge is
shared that we built things smarter next
time so that we can do things a little
easier the fifth lesson that we pulled
out is that we realized we have tools we
were not given to us like usually we're
not actually given all the right tools
but we need to also be imagining what
the tools could be like that that we we
can use in our our testing you pull in
whatever you need you build whatever you
don't have don't just wait for someone
having thought of that for you so if you
have an idea of how you could do things
probably follow through that idea and
then as the sixth lesson we realized
that yes we would love to automate a lot
of stuff especially around the
permutations and integrate that to
Google vocabulary so that we can figure
out which ones are really words and and
all that sort of things and we realized
that within the hour that we were
intending to spend we couldn't build
that tool but probably I expect to see
some afternoon where someone who spends
a few hours building a tool like this
just for
you know trying out what kind of things
you can do when you you have the whelen
and that power and that's the final
lesson on this we learned it really
didn't work but even if it doesn't
calculate the scores right the question
it is does it really matter what's
quality for something like you know fun
boggle cubes we we were laughing for an
hour on trying to you know put things in
in some kind of an order and I figure
out if it works you know as this target
the quality is really high when you have
bugs as a game the quality is really
high when it's it's fun and and and
you're doing things that that you enjoy
and the problems really only matter when
they end up being things where people
react to them by walking away from your
system leaving you because of the
problems that they're facing and you
really want to be paying attention to
the kind of things that matter to the
people or matter so all of this illusion
breaking it's really for me it's about
lucky accident following by figuring out
unknown unknowns trying out hypotheses
and keeping and sticking with the
problems longer so the quotes that I
really enjoy on on this side is that
well there's this disc all fur on a
partner polymer who keeps saying that or
has said that if if they practice more
they get more lucky and a lot of times
you know testers came to seem to be
saying like you know I'm just really
lucky like I don't find bugs the bugs
find me like I actually have to work to
find most of my box and some of them
find me sure but for most of them I
actually have to work for them but when
you've spent long enough time with your
external imagination in front of you the
box will wave at you and they say look
here I'm here you want to come here and
then you will find me so you get more
lucky over time and also the other wise
thing on just speaking with things and
and figuring things out is from Albert
Einstein not that
we generally are actually so smart even
the ones who are kind of considered the
smartest of the whole lot but if we
stick with the problems and we don't
give up that usually makes us a little
bit more lucky or smart in getting to
the results so as the final idea I kind
of want to summarize this as approaching
testing the illusion breaking as
deliberate discovery skills with an
external like a an external imagination
that you can use so if you look at those
numbers there one two four five what's
missing in the middle three this is what
you're missing but it also could be that
what's missing in the middle is not
three any other suggestions
yeah like time so again whatever you
would look at there's always a different
perspective and you have to be very
actively looking for that perspective
this is something this little example
something at least he'll a shared with
the community and I appreciate her
perspective of looking at us testers on
what kind of things we're doing and
expressing that appreciation so that we
can better talk about the things we do
so that's what I had to share for today
thank you
[Music]
you
