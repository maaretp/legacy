---
title: "Maaret Pyhäjärvi, keynote: 'Perfecting the craft of test automation' Agile & Automation Days"
video_id: uA-VL86nOwE
url: https://www.youtube.com/watch?v=uA-VL86nOwE
upload_date: 20161207
duration: 52:41
channel: testerzy.pl
tags: []
---

# Maaret Pyhäjärvi, keynote: "Perfecting the craft of test automation" Agile & Automation Days

> Maaret Pyhäjärvi, keynote presentation "Perfecting the craft of test automation" Agile & Automation Days, Warsaw, Poland, 21.11.2016

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

it's great to see so many of you here at
this hour
in Finland that's where I come from
people would not show up at 5 o'clock or
the other option for this is you're here
because you love testing and this
automation so much that you would even
spend your nights with that so that's
also a good possibility here so we've
spent the next a little less than an
hour talking about things that I've
learned over the years in automation
I've been doing testing for about 20
years now I've been well he kind of
mentions things that I have as a hobby
I've been teaching kids programming for
the last two years and I've only
actually personally been more into test
automation in the last two years and
you'll hear some of the stories on how I
got into be more keen on automation
stuff myself and not just you know look
at it from the perspective of a tester
or test manager who works in
organizations what I want to talk to you
about today is basically perfecting the
craft of test automation what I feel
that is happening right now is that I'm
seeing that we're actually getting
pretty good in various organizations in
doing test automation having code be
part of the way we test and while we are
getting to be good in including that I
still see that all the organizations who
have even extensive automation they seem
to be struggling with similar things
that kind of bring us together into
these events to talk about how do we
solve the same problems how do we solve
the issues that we have and I wanted to
share some some lessons on that with you
I work at a company right now called
f-secure I've been there for 10 weeks
now so I'm not gonna tell you all the
nitty-gritty details of how execute
works but this is not my first time I
have secured I rejoined a company that I
used to work at 10 years ago and I
wanted to talk to you about this because
there's a bit of a difference in in how
I see the world when 10 years have
passed the company that I left 10 years
ago didn't have much of system level
test automation
that company if secured back then ten
years ago had just started getting
developers introduced with unit tests
and I remember we were struggling I
remember that there were difficulties in
in getting developers to you know figure
out what would a good unit test look
like that wasn't a straightforward and
easy thing and the whole automation on
the system level from the whole product
point of view we had been using various
third-party tools I think at the time
when I was there 10 years ago we were
using if I remember correctly three
different commercial tools back then and
they were always ending up in this like
small isolated you know a couple of
people who were assigned to it super
excited this is a cool two of the best
tool ever and then the rest of the
organization was like oh I had this real
work to do can you please stop bothering
me and it just somehow like died when
when those people moved away but in the
ten years that I was away and I wasn't
doing anything about it I wasn't being
helpful or I wasn't being a hindrance
they had finally managed to do something
about test automation and I joined an
organisation ten weeks ago where their
significant level of system level
automation based on Python based on
self-made frameworks based on team
ownership of that automation and it kind
of looks like though the way III would
like to see that the you know test
automation enthusiastic organizations
are doing test automation right now that
they are actually putting effort into
that they're seeing success with that
and things are working in in many ways
but still there's some challenges
there's still certain things that need
to be addressed and those are the things
that I want to talk to you about today
so I feel that my current place of work
is a good representative in the sense
that that's kind of the things that I
see in a lot of companies nowadays that
we've taken significant steps forward in
automating weave testing we've taken
significant steps in having actually
automated scripts running continuously
give
us feedback and helping us make those
releases and I see that in a lot of
organizations we may have very different
choices of languages some of us have
chosen tools that we heavily rely on
others with we've built our own testing
frameworks but today I find that when we
meet in these conferences we talk about
the fact that there's actually already
like tools and means to do things well
but still there's something that we
might be might be missing the current
day of automation I feel that it's kind
of in the sense that we are looking at
things even automating as a thing that
is done by people some of the best
automation that I see is done by really
really good developers how many of you
identify here as a developer by the way
developers identifying us developers
okay a few people how many of you
identify as tester automate errs
majority anyone here who identifies as a
manual or an exploratory tester some of
those as well all right so we have a
nice mix of offer of people but whatever
we do in testing this whole good world
of test automation it requires that we
have good people with good ideas and the
automation is as good as those brilliant
people make it so that's kind of the the
baseline from where we we start with and
from this baseline I have three lessons
that I want to go through with you the
first lesson is about clean code you
might find this slightly surprising when
we're talking about test automation but
I find that from my decades of
experience all the test automation that
I've seen in various organizations we
have put a lot of effort into test
automation that doesn't actually help us
if we didn't simultaneously think of the
good structures in the test automation
but also the good structures in the
production code that we are testing with
the test automation so if you have a
swamp and it's kind of shaky and you
don't know if it stays together the test
automation is probably
we going to be a little harder and we'll
got to talk a bit more on that later the
second lesson that I want to talk about
today is about bringing the people
together we have all kinds of skills all
kinds of knowledge and different kinds
of experiences and sharing the
information sharing the knowledge that
we've gained there's some special tricks
or ways that I want to share with you
today and the third point is that I find
that well I used the word test
automation and I know that I made just
Richard cringe when he even saw that
word on my slides can't we talk about
tools in testing that's what he usually
mentions I still intentionally talk
about this tall nation but I'd like to
talk about this automation in the sense
of we can understand it as a wider
concept giving us a lot other
opportunities than just the regular
regression idea and I wanted to
introduce you to some of the stuff that
I'm super excited about in automation
that has been around for a few years and
that has definitely been in my life in
the last couple years so that's that's
kind of the agenda for today so let's
start with the clean code aspect so I
wanted to start with a bit of a story
about four and a half years ago I joined
an organization that was struggling I
was the first-ever tester in that
organization they had been doing
software development for twenty years
first ever tester they were making
monthly releases so clearly a tester
wasn't necessary but they needed a
tester because about eighteen percent of
they're logged in users during a working
day so a big visible error message
eighteen percent that's kind of high the
developers in the teams they were
totally puzzled like we don't know what
the users are doing it's totally
mysterious we don't know we have no idea
so they were thinking like here maybe
we'll get here a what they call then a
test manager you know to help the
developers figure out how to do
automated testing better how to do
testing in general better and how to
figure out how to fix the the
application well most of my effort at
first went into fixing the problems by
telling the retro stefson a little bit
then you'll see one of these crashes and
we got together with the developers we
got that down to one level of one
percent but that was just one of the
things that we were doing in general I
was brought in there to help the
developers figure out how do we do
testing how how would we do test
automation how would we do manual
testing so that we as a team would
manage to do things better and I had
one-on-ones with all of the developers
and I was asking them that I was given
now this allocation half of every one of
your time you know under my management
for other half of your time and under
the project managers management for the
other half I want us to do testing what
opinions do you have on this this
testing that we would do and every
developer in the one-on-ones and in
every public meeting that we would have
they kept telling me that seriously you
can't ask us to do manual testing
because it's boring and awful and
repetition and this breaks in every
possible way we hate that we want to do
something about the course of this and
it's the same with automation we don't
want to add automation or unit tests or
system level tests we don't want to add
those if the code is as bad as as it
says gotten to be so my developers all
of them in unison were telling that our
code is a mess
we have not been allowed to clean it up
we have not been allowed to refactor it
and if we're trying to put some tests on
top of this it's just not gonna make
things any better it's just gonna be
harder and more difficult so I listened
to them
and I decided that although I was hired
as a tester I was allocated a testing
budget I can play a six month gamble I
told the developers that whenever I give
you a task to test take it as a
permission to refactor it's your time to
make things easier so that you can clean
the code up and you can you can be
refactoring and that actually changed
the whole way for us on how we built the
software that was a big part of how we
got to the half a percent of the end
user visible errors that was a big part
on how the developers again started to
like doing work on the code and we also
learned as a team that when we would
read the code when we would talk around
the code and we would actually
understand what the code does we would
need so much less of the automation that
you know the higher level managers they
were kind of thinking that you know it's
a testing problem lots of bugs we need
more of testing what we actually need it
is more of a approach for doing the
doing they they code us as a clean one
so I had the choice between doing
testing and doing refactoring and I
started with let's first do refactoring
let's then add some unit tests let's
then add some selenium tests let's then
add some integration tests against the
middle layer things against that with
the data in the user data in the data
bases and like one by one one goal by
one we took steps forward in that world
so all of this really taught me that
technical depth is a core concept that
even the manual tester should be
actually caring about but automation
testers in particular if the code that
your automation tests if it's brittle if
it's unclear if it's badly shapen
probably your tests will find problems
but those problems would be more
effectively and efficiently found by
other means so this whole technical
depth as a concept it's not something
plan for it's not intentional it usually
just happens it's kind of like you know
gaining weight no one I think
plans for actually gaining weight and
and well some people do but it's a man
minority you don't plan for it
but it comes out of the habits and
fixing the habits is a big big part of
of getting better at at these kind of
things if you have messy code you can
add automation but it's not gonna help
you much because it's gonna cost side
effects we did some tests around in
different organizations around messy
code and I remember one organization in
particular where we had this test
automation team we had problems that we
were finding we were reporting them with
nice videos and all that and we were
always kind of like playing this
ping-pong man and chase between the two
different parties in trying to get
things in in place and before we started
more collaborative approaches we
couldn't really really get far with this
one but it's not just the production
code it is first the production code but
it's also the test automation code those
of who you identify as test Automator x'
do you think of yourself as people who
write code who thinks of yourself as a
people who person who writes code as a
test Automator I write code other option
I write two are used tools some people
like this one okay so a lot of times I
find that when we are doing automation
it is actually a programming effort and
all the same rules and and things that
we are talking about how do we do good
code version control having somebody
review whatever we did having team
somehow collaborate understanding the
requirements before we jump into doing
things the exact same things about
cleanliness and good practices they
apply to the test automation code as
well and if there is something that you
can do to make things better
in the world of difficulties in existing
automation I find that often it comes
from the fact that you find ways of
thinking how how your tests could be
smaller like for example last week I
walked to a colleague of mine at the
f-secure and I actually wanted to just
see you know like a show of manual
testing to do some peer testing so that
you could figure out figure out a a way
for me to to learn that application and
at the same time when she was showing me
around the application I was asking like
hey how do you test this and hey how
what kind of tools you have and and
where's your test data and I started
suggesting that hey for automation
purposes since we have brittle tests
sometimes they fail even if they
shouldn't maybe here would be a way of
cutting things so that we wouldn't test
this whole long chain of things maybe
you could fake this part here and the
developers would jump right in into the
discussion and say like hey we can
easily make you that service and it just
turns out that we had never had that
type of a discussion in that team that
we could you know make our test smaller
so a lot of times it's really about
someone opening their mouth and saying
that we could do do this this thing's a
bit smaller and smaller it's better in
the sense that they run faster they're
more granular at least I find it very
painful when my test automation fails
and the first thing I will do is figure
out from the logs on which point of time
or which point of the script this is now
failing and I really like the unit tests
that we have in the sense that they
pinpoint right away that hey here's a
unit test that is failing this is where
we should be looking at so the
granularity of the test is is a big big
part of things and when I talk about
cleanliness of code I really talk about
people you know cody's people code is
written by people tools are written by
people I stole this from a tweet by
Richard last week I probably used it in
a different context than he originally
imagined but I think that whenever any
one of us in our organisation
need to say that our tests are flaky
we're actually saying we're missing
information we're missing skills we're
missing knowledge and the next step
should be to go and find that knowledge
and skill from somewhere maybe it's
within that organization or maybe it's
going search online but there's
definitely a skill to build there we
often talk about automation as something
that is really really key and core I
think it is in the world of agile where
we deliver continuously automation has a
test automation as a big part but I also
wanted to kind of mention the idea that
in the organization that I talked to you
about the four and a half years ago I
joined and let them do the refactoring
at first after a year in that
organization we started doing daily
releases to production we didn't have
any test automation at that point none
daily releases without automation it was
basically founded with the idea that
programming is a manual activity so
testing next to programming can be also
manual activity and we would only merge
things into the main line when the
manual activities were done and then we
would go forward so for almost a year
and a half we did daily releases without
any automation until we started getting
to the point where we started adding
automation layer by layer test by test
one by one so this whole concept of
continuous delivery it's more based on
being able to split the risks than
having the automation there to help you
so I would encourage you to make sure
that you have this the small small
cycles and sleep so my first lesson
really is on clean code I believe from
high experiences in various
organizations talking with various
developers in particular that
we won't be solving the challenges with
brittleness with unreliable automation
and lack of collaboration unless we get
everyone into the same page and a big
part of that same page is understanding
or caring about our code both test
automation code and production code so
that it's as easy to maintain over long
term as as possible so this kind of
leads us into my second lesson I'm a big
fan of a approach to development called
mob programming and it's been for me
kind of a thing where many things have
changed for me in the sense that I
realized about a year ago when I was
doing one presentation that during my
career I've actually been programming in
13 different languages 13 and I call
myself still mostly non programming
programmer I write code when I can't get
other people to write the code for me
but I talk around the code pretty much
every day I look at the architectures I
look at the choices of languages I look
at the enthusiasm that we have around
automation and that's a big part for me
but before I started to understand and
have more empathy to people who feel
differently than I do I felt that there
was much more more of a gap so I want to
talk about a bit about this idea of a
mind share and what that actually means
I find that in a lot of organizations
there's these three different types of
testers I say testers intentionally even
though one of them here is an
application programmer programmers test
like crazy nowadays the amount of unit
testing that agile programmers do it's
sometimes insane any one of you have run
into this infected programmer
has anyone seen one of those maybe the
test infected programmers often are
people who talk to me back then tell me
that they can automate everything
because they are really good programmers
as well so whatever challenge I throw at
them they usually know a way of of
finding a way of automating it but we
usually have these three roles we have
people who are more into I hate the word
manual I don't want to say manual brain
engaged testing exploratory testing
thinking around problems in the testing
domain understanding the requirements of
what would we want to test and what
would be a reliable way of getting
information about that then we often
have people who specialize in test
automation automation specialists I
consider them also one brand of
programmers there's somehow kind of
in-between these testers and the the
probe the application programmers
there's somehow kind of like taking a
bit from the both domains and sometimes
not identifying as programmers at all so
we have these three different kinds of
roles and sometimes actually quite a lot
of times these people just don't talk
too well to each other any of you use
Twitter is there any Twitter users here
I don't see much tweets hit from here so
I had to ask you might be lucky because
you don't get to see the Twitter Wars
let's Twitter war always ongoing with
the people who like test automation and
people who are more into the expiratory
side of testing whether you can automate
on how much you can automate but I'm not
really into that kind of like the the
the barriers between these three people
I want to just recognize that they are
different skill sets different entry
points and if you come into this field
of testing probably you won't have all
the information on day one and you won't
have all the different experiences on
day one and in software in the
three there's a rule of thumb saying
that the size of the industry doubles
every five years which actually would
mean then that about half of us have
less than five years of experience so
it's kind of a natural thing that we
come in into one of these even if we
would move around a lot but we have
different experiences different
backgrounds different interests that
take us into this
so the mind share between these three
different kinds of people is through a
mechanism that we call more programming
or mobile testing I call it mobile
testing whenever it's about a testing
activity if it's about the programming
activity then I usually call it more
programming there's a guy in in San
Diego well California USA called Woody's
wheel and about five years ago he and
his team discovered this way of working
by accident that they would all work on
one computer just one computer to type
in all the code that they would be
building and with that one computer they
would take turns who's in front of the
computer usually starting from four to
five minutes on the computer and then
they would you know rotate around so
that whoever is on the computer that's a
resting position you are supposed to be
just listening to what the others say
and do whatever the others are saying
and not do thinking or decisions of
yourself your yourself and all the other
information comes from these others they
called navigators and navigators will
tell you where to go and what to do with
the computer and you again rotate on a
frequent basis so it's kind of a mind
share with these all of these people you
might see that on this picture there's
this little girl here I have to show her
she's nine years old you might wonder
what she's doing there I used this
picture because I think it's super
inspirational to me this is from an
agile conference in US and this girl was
invited to join the programming mob they
were doing TDD exercises she was invited
to join the programming mob and she said
no I won't
why would I I'm
a programmer I don't know what to do she
wants them do this more programming for
ten minutes and she said this looks like
a fun game dad can I join after all I
know how to play this so the game went
so that they would you know they would
draw an example on a whiteboard the next
test to draw a test drive the the the
application that they were creating then
they would turn that picture or example
from the whiteboard into English
intentional programming and then they
would translate that English in comments
into code so that usually for a sentence
of English there was a sentence of of
code code implemented as well
so she said I can play this game she
would boast this older gentleman here
and tell that I want you to code that
for me she didn't need to know exactly
how to do that and when she took her
turn on the keyboard they would tell her
letter by letter what to type so that
she could do things so it's a mechanism
that actually adjusts to different skill
levels really well I heard about this
about two years ago in a conference that
I organized in Finland and I was
listening to Woody's we'll talk about it
I was like this is ridiculous
it won't work it's just like it can't
work but I took it back to my office and
I started doing this with my developers
once a week and to my surprise the
developers who never really well
understood exploratory testing learn to
explore really well I'm really proud of
the way they test nowadays even without
automation through understanding testing
better they learn to how they could put
that into automation all of us learn to
do selenium that only one of us know
knew how to do we learned how to turn
our unit tests not only into asserts
simple asserts but into approvals as
well like more complicated tests of a
certain format and we learn to add tests
before we would even implement things so
there were a lot of things that kind of
came out from us
working together in in this this format
so the mind share is really to help
different people with different
perspectives contribute to the same task
with the idea that if you have good
moments and you have bad moments
somebody else might have different good
moments and different bad moments and if
these time wise when you're in the same
room if this time wise compensate each
other you get the best out of everyone
into the work you're doing and and a lot
of information is also shared that way
so the idea with mobile in general is
about raising our collective competences
collecting competencies making sure the
individuals come in with whatever skills
they have but they leave with more
skills you're welcome in a mob if you're
learning or contributing and a lot of
times you're doing both and the
contribution contribution might be
anything from actually knowing exactly
how certain automation problem needs to
be solved it might be knowing how you
want to restructure your application so
that it makes it easier to test now or
it might be that you find a problem from
half a sentence that never gets into the
code because your knowledge about that
type of things was was involved at the
right time all of this mobbing has
really led me to believe that we're
doing in this industry right now we're
doing a big disservice to ourselves by
saying that there's this group of test
automation engineers who don't identify
as programmers if those people would
take a few steps more close to the
programmers and the world of programming
they would probably amp up their own
ability to do things and and to
contribute and also I find that looking
at my current organization we still see
these silos of different kind of like
here are
like all groups I have the amazing C++
developers C++ is a super hard language
if you haven't ever heard of that it's
so hard that only the smartest survive
I've heard this in the last 10 weeks
Python is the friendly language the
scripting language that anyone out of
pretty much anywhere can learn and can
get started on but it's also one of the
most powerful scripting languages it's
an actual real programming language that
enables you to do just about anything
you can do with C++ so it's an endless
world but it's a different world and
then there's these people who don't want
to touch the Python code don't want to
read the C++ code but rather spend their
time maybe on the application without
knowing of any of that the other world
and if we don't actually bring these
together if we don't collaborate well
then we're going to be stuck in the in
the troubles of of hoping that things
would be easier that they just won't
won't get get to that so collaboration
helps us a lot with that and the idea
that we wouldn't be learning programming
when we're automating I think that's
just far off all in general sometimes I
hear that when you put this many people
together or even a pair together it's
wasting time and effort but actually it
changes the nature of the work we're
doing when we have a group working
working together if you're working on a
hard problem alone and you just don't
know what to do I have one of my test
Automator x' right now that seems to be
struggling with this kind of approach
she waits for three days or two days and
then when she didn't figure it out
herself then she comes and asks and
somebody helps her over that but it
usually takes a lot of time before she
gives up and like realizes that hey
there's this big gap and if nobody is
would be available to help her the
problem just won't proceed like this
Osia won't won't proceed so with hard
problems when you bring people together
working on it you get a solution you get
the probably even a better solution than
just out of one person but with simple
problems when you're doing something
really mundane something that you know
no one should even be doing alone I've
heard this as a manual tester from some
developers a lot of times that you know
you shouldn't be doing that at all
sometimes then what happens is
innovation they tell you that hey here's
the tool that you never knew how to ask
for this is going to put all the data
for you in the database readily and and
that's one example of the type of
innovation that could happen so you
might want to consider that but all of
this mind share what I really wanted to
share on this is that there's all kinds
of aspects all kinds of tasks that you
can work on in in this manner I wanted
to first make my team do programming
together in a mob format so that they
would learn to talk better to each other
that alone already improved our quality
of tremendously when the developers
started collaborating with each other
better but I also brought in tasks
around adding selenium I brought in
tasks around
let's change components let's implement
new features let's have us all be there
at the same time and I saw how one
person would say here's the thing we can
call another would add like here's
another thing and another and another
and another and you would end up with
the best possible solution that you can
within a very limited limited time frame
so for me at first I didn't intend this
mechanism to bring me back to
programming but after six months going
back into my plug blog where I said how
much I will end up hating this and how I
will do this only for the benefit of my
team because they need to talk to each
other I started realizing that I had
again found the love of programming I
had again found the love of programming
for test automation purposes
and I started realizing that a lot of
the stuff I didn't intend to learn but
it kind of came through osmosis because
I was just in the room there doing my
bits and pieces while well while we were
doing these things but the same thing
also happened on the developers on
learning how to think properly around
test automation around testing in
general and and finding the problems
that we might might have in our our
applications so for me it kind of sums
up to and this idea that we all kind of
think somehow that we'll good at our own
areas but when we put our skill sets
together there's overlap and then
there's whole scaping holes that the
other person's knowledge fills in so
this all the mind share idea is really
on the idea that whatever information
sharing you might be struggling with
having your group come together and work
not on just talking about it but
actually doing something some tasks in
that area you might see magical changes
with people starting to feel more
empathetic or about whatever the other
ones are doing and understanding how
their knowledge could contribute to help
the others in the overall process so
it's not really about what I'm doing and
how I'm optimizing my work but it's
about us working together and getting
things done the third part of what I've
learned is that all too often we're
looking at the world of test automation
from the point of view that we're
somehow stuck in the idea of regression
testing we might be looking at unit
testing and integration testing and
system level testing but we're still
looking for ways of running automation
and again and again and giving us
feedback about how we are in comparison
to past days but even to do this kind of
thing I find that there's so many
things going on in the world of
automation that a way too often we're
focusing inside inwards into our own
organizations and we might not always
see that the things that other people
are doing so I wanted to share some of
the things that have been kind of
lighting me up in in the last couple of
years the first part I think this is
kind of obvious in some ways but I still
seem to be running the into this a lot
that we could be using automation a lot
more in in our environments how many of
you are doing something in Amazon clouds
nowadays I find that that comes along a
lot more often to me nowadays then than
before I people are just spinning up new
test environment test environments or
even production environments we do
Bluegreen deploys so that we can always
have a working version and we can easily
change between different versions that
are running in production when we're
doing web-based applications the whole
environment automation getting set up
automatically running builds making them
making them available automatically it's
a big part of the types of things that
we could be doing and in a lot of
organizations we still maybe don't do
enough of that that's in my experience
another thing that really I like a lot
in the world of automation is testing
through api's even if I to do so-called
manual testing exploratory testing is
preferably the word that I would use I
often do my testing through an IDE
programming tools writing a bit of code
but with the idea that whatever code
I've write it's not meant to be there to
maintain forever it's not meant to be
rerun but it exists to give me ideas
about the things that might be wrong
with that API how we put things together
in that API how we set data up or how we
set different course into a chain of
events
and of this developer experience
perspective a lot so I find that in
increasing amounts I'm seeing and using
automation as something that is to be
thrown away after it's been written and
it's not even intended to be be kept I'm
also seeing other people report and
share ideas about doing BDD so that you
very purposefully write be really
automation tests but as soon as the
feature is ready and in production you
delete all of it because it already
helped you to that point or maybe you
leave just a couple couple of tests so
the idea that some of the automation
that we write is meant to be deleted
it's never meant to stay there I find
that it's a it's an idea that would be
beneficial for a lot of us in in our
organizations selenium is still a big
part of this world
anyone here using selenium in your
projects quite many yeah it's been
around a while and it's kind of become a
de facto standard
I still see really really ugly selenium
code in a lot of organizations that I've
worked with I see very straightforward
basic kind of like procedural structures
which usually come from the fact that we
haven't yet wanted to learn about things
from becoming more of a programmers page
object pattern has been around forever
to help us kind of get forward from from
doing these big clunky clunky scripts
and and get more maintainability into
our scripts but also I'm very happy to
notice that we're talking about things
like like screenplay pattern where we
are trying to bring in the you know
tester perspective intent and small
pieces really small pieces of code very
much the coding principles even even
further into this so that we would have
more maintainable things so it's nice to
know that even something that has been
around
while and has been kind of seemingly
static for a while it's still growing
and going forward so you might want to
if you haven't yet you might want to
look into that look into that a bit
another thing that I keep running into
is the pain of brittleness we can't find
elements and it's also nice to notice
that in various groups there seems to be
these ideas of multi locators having
different ways automated ways of you
know trying couple of different ways of
identifying where the element is that
we're wanting to click and even if what
if one of them works that also takes us
forward so instead of just working on
let's find one that works maybe we could
have this reusable libraries of locators
so this is also something that I've been
liking to see happening on the unit test
side going from just asserts simple
asserts and and simple checks going into
more of the describing the whole object
and pushing information about that
object into a file and doing file
comparisons and having tools that
pinpoint the problems on failure me and
my team at least we've had really good
success and and experiences with this
type of tools doing more complicated
work on typically old code bases that
were not under tests before in a quite
fast manner through approval tests it's
just a different way of thinking about
unit tests in the sense that with
approval as a certs we're defining what
we're expecting with approvals we're
pushing things into a file we're
verifying them kind of as a manual
tester would and then we're comparing
things so again make sure your tool set
is as wide as possible
I've also liked the fact that I've
started to see that I've talked for
years being a tester background person
I've talked about partial Oracle's and
I've watched doc Hoffman
Kim K in a work on this area realizing
that the developer community talks about
the same thing with the name theory
tests all of a sudden we had so much
more common ground with the developers
understanding that we are actually
trying to solve the same things the
ideas were theory test is just that you
have these rules that are always true
and and you generate a lot of data a lot
of examples that you're testing against
instead of having specific examples
again thinking in a bit different way
and finally model-based test automation
this is nothing new I used to do this 12
years ago in one of my jobs model-based
test automation with the idea that you
will draw these you know boxes and
arrows and and you will generate test
code I see that now
in the modern day but in the recent days
for example Spotify still talking about
doing a lot of their test automation in
in these kind of manners generating
tests tests and I think it's a very
promising one approach to covering
combinations and and and like longer
chains in in functionality instead of
writing all your tests separately and
I've seen very good examples of how we
can find long fuse bugs that are hard to
find find otherwise so with all of this
I wanted to just encourage you to not
well take some of the words that I
mentioned here as things that you might
want to be looking into but also maybe
talking to some of your colleagues
around you and asking and asking around
what what's the thing that they're into
and looking more widely into automation
than what is just the usual suspects but
all of this really sums up into the idea
that we've been working hard on
automation for I think several decades
in the last 10 years we've taken
significant steps forward in many
organizations and I find that while I
could argue 10 years ago that this
automation thing doesn't make much sense
I see too much of good and useful
automation these days so that I would
want to be in any way against it quite
contrary I want to be there to support
it but we are not done yet
we're not ready yet the tools are not
always trustworthy enough yet but we
have the ability to change those tools
take things forward and the good enough
of today it's really not good enough of
tomorrow so at least for me looking at
the 20 years of experience that I have
in this industry we keep going forward
every day and the best way to go forward
is together so I encourage you to share
and learn together work together make
sure you have the mind share you learn
things that you never expected to learn
when you work together in a close
collaboration write questions comments
ideas so you mentioned that you work for
a company that for a year and a half did
not have any tests and I was doing
continuous delivery oh yes that's the
point of time they decided to implement
this why because I pushed for it the
reason why I pushed for it is that I
believe I'm quoting one English
gentleman right now I believe that
software risk is best taken in in small
pieces small cartons so while you buy
milk in a big box and it's cheaper
software doesn't work that way smaller
risk at a time is better we were
struggling with sticking to our
schedules and keeping our quality on a
good level when we were doing bigger
changes so the idea of doing small
changes that you can do and put on
production on a daily basis it alone
improved our quality significantly
because it enabled the manual testing to
happen specifically for each of the
changes separately even without any
automation
yes which question you set about like
looking into tomorrow
do you know does any organizations now
are trying to implement like using of
artificial intelligence in automation
because I read
articles that some companies are working
on building like frameworks which will
use machine learning into that yeah i've
also heard about those I've been trying
to follow those and that would
definitely be one of those pet projects
that I'd love to do at some point but I
left it out from my my list of things
because I don't have a personal
experience on that yet it's an
interesting browser Thanks
we had a gentleman there I would like
you I would like you to ask about
differences and pros and cons of screen
play versus page object pattern mm-hmm
why I should resign page object pattern
for screen by screen screen play I don't
know if you should or not I'm not sure
about that and what I'm saying is is
that I'm saying that sometimes with the
page object pattern the things are they
get kind of big already and when you
bring in a developer like a programmer
professional programmer to work on those
they tend to want to refactor them
without knowing about any of the
automation patterns and they tend to be
somehow wanting to go to smaller pieces
that's just you know the usual
refactoring that comes from people who
write good and maintainable code and
when those people then together with me
are looking at like hey there's this
page of the pattern where versus there's
the screen of screenplay pattern they
seem to be more into the screen play as
better expressing intent and being more
maintainable and again I think that
might also be a bit of a preference
thing so I find that sometimes testers
without as much programming knowledge
they might be easier to go into the page
of the site so again it's not either/or
necessarily it's more like an
encouragement of see what else that
would take you to if you would also look
into into that approach just two small
questions little bit less serious than
the previous ones about mine sure
and did you find that there is a
specific group size that should not be
exceeded in this case because the more
people are the group I have a rule on
how I define what would be a good
learning mobile size and the rule is
that during the session that we're doing
everybody needs to be getting on front
of the keyboard a minimum of two times
but preferably three times so if we're
doing two hours of mobile and we have 10
people it means that the the cycle time
is probably around four minutes and then
you barely get twice onto the computer
so it depends on on the kind of how long
you're gonna be mobbing when you mob on
a longer term they usually talk about
two pizza teams American pizzas meaning
about six to eight people finish pizzas
not enough like okay that's much much
than this because it got me curious I
know I will I will live to regret this
question but how do you pronounce your
name my name is Marit to hyeri so the
difficulties are the in in the beginning
and in the middle also that's them
nobody can do that
thank you I think this is a good place
to stop I'm happy to talk with any one
of you after this and it was really
great being here so thank you for having
me
