---
title: "Maaret Pyhäjärvi - Let's Do a Thing and Call It Foo - NewCrafts 2023"
video_id: 7Xu4xg9dZ0s
url: https://www.youtube.com/watch?v=7Xu4xg9dZ0s
upload_date: 20250711
duration: 44:59
channel: Aardling
tags: [ddd, domain-driven design, software, software architecture, cqrs, event sourcing, modelling, microservices, messaging, software design, design patterns, sociotechnical, crafting, functional code, software practitioners]
---

# Maaret Pyhäjärvi - Let's Do a Thing and Call It Foo - NewCrafts 2023

> NewCrafts 2023 - Organised by Aardling (https://aardling.eu/)
> 
> https://ncrafts.io
> https://bsky.app/profile/newcrafts.bsky.social
> https://www.linkedin.com/company/ncrafts/
> https://mastodon.social/@newcrafts]
> 
> 
> About Maaret Pyhäjärvi:
> Maaret Pyhäjärvi is a tester extraordinaire specializing in breaking illusions about software through means of exploratory testing. She is a software specialist with soft spots for hands-on testing, helping teams grow and building successful products and businesses. She's been working with software since 1995 in various roles and delivers talks as popular speaker in Finland as well as internationally. She works as a tester at Granlund and trains testing on the side through Altom. Networking through public speaking is her favorite pastime, and she delivered over 30 presentations in year 2015 around the world.
> 
> In addition to speaking, she is a serial volunteer for different non-profits driving forward the state of software development. She's currently the chairman of Software Testing Finland ry, the main organizer for Agile Finland ry's Tech Excellence Finland Pod, volunteering mentor for Speak Easy volunteer with Learn with Llew (teaching kids) and the head organizer for European Testing Conference, aiming to change the world of non-profits and conferences to be more sustainable than pure volunteer organizations can ever be.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

[Music]
good morning
everyone
uh we are going to talk about Fu but
we're going to talk about Fu because
what I really want to talk about is
testing and the reason I want to talk
about testing is that I've been doing
testing for 25 years except right now
I'm actually a manager of about 26
people uh I didn't want to be a manager
I still do the exact same things as I
did when I was a tester so I still test
as a manager I still care for you know
bugs in the organization that I fixed
before uh and I'm only a manager because
I had a couple of people that I didn't
quite get along and it was easier to
replace them by taking their jobs rather
than you know actually fixing the the
root causes that were uh behind those
those things so I am a tester even if
I'm a manager even if I'm sometimes a
developer even if I'm sometimes a
business analyst and I find it really
really difficult to talk about the thing
that I care about which is testing
because everyone uses these very kind of
like belittling demeaning uh words
around testing a lot and uh the whole
field of testing is actually filled by
by these
terminologies that make it even more
difficult for us to talk about the real
thing that we want to do which is you
know
testing and that's why today what I
wanted to do instead of you know talking
to you about you know words around
testing unit testing exploratory testing
manual testing automated testing as if
these were different things these are
not actually different
things I wanted to give you an example
that was inspired by me going into a job
interview because I was unhappy in my
organization last Autumn I went to a job
interview they made me pair program with
a
developer uh I taught the developer
during the pair programming session that
they were quite many things that they
didn't know about their little Kata
exercise that they made me go through
they offered me a job and I refused
because I felt that uh there is no place
for that kind of judgment in pairing or
ensembling or teamwork that I felt in
the the setting of The the job interview
so again uh you can change things by
talking about them you can change them
by your behavior and sometimes you know
what you are doing after you've done it
and you find new words to describe it I
assume most of the audience today is
probably developers and I work with
developers they are brilliant at testing
uh and one thing that we do when working
uh as developers is that we give things
names usually after the fact and that's
kind of why we talk about
F I hope most of you at least after
today all of you have heard the idea
that if you don't know what you would
want to call a thing that you're just
now creating just call it fo
just call it
anything but call it something that you
hate so much that you want to replace it
by something better
right I don't particularly like the word
Foo I think it is a really bad name and
I would hope I would never have to find
it in my code
bases but I know that I have written it
down many times and I know my colleagues
have written it down uh many times and I
know that I have received based on this
talk that I have done in a few places
before some thousands of of other
proposals of words we could use as a
replacement so that they would be more
useful than Fu but fu is not the key the
key is we don't really understand what
we are doing and what we should call the
thing we are
doing before we have kind of seen it in
action and we should always work with
the mindset that we work with our code
in also with our practices and and we
should name the thing after we've seen
it and when we realize that we have a
better name for it it's okay to rename
it so that's kind of the gist of of why
we are here
today uh there's another gist to this
which is that as a tester I have always
kind of believed that it's not code that
I'm breaking it's the illusions of
people that I'm breaking this is
something that I talked about in 2017 at
start of my talk and it turned out that
Romeo took a screenshot put it on
Twitter and it became apparently his uh
most popular tweet ever so uh it's still
a relevant thing for new people who have
never heard of that that's what testing
is about it's breaking Illusions it's
not breaking the system but it's
breaking Illusions and me uh here today
I'm here because Romeo asked me to come
I don't know any more submit to
conferences I've done about 550 talks so
far and I'm uh still happy to be here
but uh the reason I come here is that
this is where I quit speaking three and
a half years ago Paris so it only feels
uh good that you know I'm returning back
to speaking in the same physical
location where I quit three and a half
years ago because of kids they wanted me
to be home so no other particular reason
but I'm always talking about testing not
only testers even if I am a tester I'm
also so many other things uh I have many
lovely developer colleagues over 25
years and a lot of them actually I would
say all of them have been good at
testing the only reason they have ever
been bad at testing is that someone told
them that they are too valuable and too
important to be spending time on caring
about
quality and if we for some reason don't
care about quality I can take a very
high price you know of work we are doing
just drink coffee with the whole of the
money and give you just about anything
and it you know it goes with the the
criteria that we have so we have
actually always cared about
quality so with this uh it kind of gets
to this idea that I often find myself in
teams in a role where even if I was a
developer even if I was a tester even if
I was a manager the idea kind of nagging
in my head is that my job one of the
jobs that is asked of me is to find
something that others may have
missed and it's kind of like an open
thing like it's a you know empty A4
paper no one is giving me test cases to
execute so I'm not doing manual testing
I think manual testing doesn't actually
well it shouldn't exist I know that it
exist in the world it just hasn't
existed for me in 25 years at the word
and the description that people have
when they say that manual testing is
kind of boring I've never done that work
not for a day I've done something
different I'm not sure what to call it I
have suggestions we'll get back to those
but my task has always been to find
something that the others may have
missed and it's not because the others
can't find anything it's because to get
to the level where we are really truly
happy with the
quality uh we usually have in the better
teams that I have had a privilege of
working especially with uh recently with
the good teams there's still a gap there
are days when I log in to our so-called
test environment and I can't get in and
it's because nobody was looking at the
alert that was coming from the
monitoring
system and I had to kind of you know
react to that and remind us and have the
conversation in the team that we should
care about the the alerts that we have
it used to be that I needed to do that
because we didn't have the alert of
course we learned from you know not
having the alert and put the alert in
place but we still have you know a bit
of a distance and even with the well in
my team right now about 1,600
programmatic tests where most of them
have been learned from you know missing
things and then adding a check in place
uh even still when I look at the
application it speaks to me it's kind of
like my my external imagination it
Whispers you'd want to click here you'd
want to try this and it makes me it
gives me joy every single day when it
Whispers me and I do what it asks me to
do and then something new is discovered
but what gives me the most Joy with my
team right now is that in half an hour
after I have said I found something that
is interesting they're coming back to me
with here's a test that you know repeats
it right now but and here's a full
request that fixes it as well uh yeah
try something different the next time so
it's always finding something that
others including the past me have missed
that's the assignment that I work
with but what makes discussing this
sometimes a little difficult this whole
results Gap it's great if this is small
like working with a team like this is
it's pure
joy this is maybe the uh qa3 that Ida
was talking about yesterday pure joy but
most of the teams are not pure joy when
you're trying to work with them as a
tester and it's not just about the
process but it's about kind of the
mindset and belief systems and and and
the way that we do things and some teams
are unfortunately for you know various
system conditions system meaning people
systems are providing less than good
outputs and in these teams I have over
the years work with them uh exactly same
kind of processes but just the practice
that ends up having we end up having is
is a little different sometimes my work
has felt like I'm picking up pizza boxes
so kind of like you know kids living
room floor they eat pizza today it's
pepperoni uh and you remind them you
know to take out the pepperoni pizza
boxes and they are saying Oh but you
know this was was minced meat you didn't
say minced meat and and and kind of like
continuing this and then again couple of
weeks later forgetting that you know
pepperoni was a forbidden pizza box or
it's not just pizza it's actually
anything that makes the the room untidy
that we should be uh taking care of and
it's not necessarily joy to work in
these kind of teams but these teams need
someone to work with them and grow them
and feedback is the best way to fix
these kind of themes and having these
conversations so with that in mind kind
of like the mindset that we are looking
for that results
Gap I wanted to take a simple
example so in that job interview they
gave me Roman numerals anyone done that
as a
cutter like yeah crafter Community
usually half of the group at least has
done that and we like almost we have
like a routine like I know how to do
that like my eyes closed in tdd nowadays
like I do I I know exactly how to do it
but I didn't want to do the tdd version
I wanted to do the let's find something
others may have missed version which is
the testing assignment version and to do
that my pair here today that I have
captured in these slides is GitHub
co-pilot so uh it doesn't actually
follow my te DD very nicely uh but it it
kind of you know it starts guessing
already at the point of me saying that I
want integer something it's already
guessing integer to Roman I guess it
knows something that I have done before
already because it's already at this
this level of guessing or maybe it knows
that because
today I named the file roman. py not
important program. py that I usually use
it's already combining those two things
and it's making guesses like I even just
on the comment level it's already
starting to guess for me what is it that
you wanted out of me and this is what
paars also do kind of like you know
their guessing based on our feedback so
so uh or well also from their own
experiences of course uh I have the
power to accept I have the power to
start fighting with my pair just like
you know in in an ensemble or in a pair
we have the same kind of dynamic and I
can't do any of this code stuff unless
I'm in a mood which means you can see
the lovely colors it's called
mermaid uh I I love the colors uh uh and
also uh whenever I write code I see
little stars twinkling on my IDE uh I
need that in order to find code
fun uh well there might be other things
but that's a part of the The Joy so in
case you need the extra um maybe you can
you can try that one out as well so I
get the okay so fine I'll accept integer
to Roman and I want to kind of write my
name
down and obviously it doesn't know who I
am even if it knows that I have been
solving this problem and I have been
writing my name multiple times in
various files on my computer it still
keeps thinking that I'm somebody else
I've been collecting over the uh year
and a half when I've been doing this
talk now uh I've been collecting names
that it proposes I have yet to find a
single woman it's never guessing a woman
so apparently all the code that it has
ever learned from is is probably from a
man or only men write their own name in
the code that's another you know aspect
that I can think of but you know it's
just you know a fun thing to kind of
note these kind of things where where
things are not just kind of as you would
expect them to be I'm sure that we
wouldn't need to keep ourselves so down
in the the coding word world but it's
also making me immediately think that
hey now I find I'm applying my uh is
there something we might have missed is
there an illusion we might need to break
I'm applying that now on co-pilot and I
don't want to test co-pilot it's not my
thing to
test like actually that's not what my
organization ever pays for me like they
don't care if my tools work as in kind
of like you know test them and make sure
they work they want to pay someone else
to take care of that
and they want me to take care of
our similar lack of you know excrements
so uh I want to be kind of you know
taking a step back and remembering I am
not testing the tool but I can't go
forward without saying that I am
actually always testing this tool as a
manager I am in the power right now of
saying can my team use this tool a few
levels up from me directors and vice
presidents have made a decision we are
using this tool
and I have told them that unless I find
an appropriate way of giving back to the
community as the
organization I'm leaving the company if
my team is using this because I feel
like we were not asked that the code
that we contributed over the years would
be available so I think it might be
legal but it's most definitely not
ethical and I might not be able to fix
the E the ethical problem but I will be
able to do some compensations of
promoting the people who have been doing
the work which I have found close to my
heart uh all over these these
years so yeah uh definitely not testing
the tool but can't you can't really move
on without noting that so what I instead
do is I want to get a Roman numerals uh
uh
implementation and uh all I need to do
is basically say that uh I have a
function that I'm setting up and it's
already kind of starting to push me the
the code that I want so I took a
screenshot of one of those suggestions
it's also often giving me suggestions
kind of like options uh I don't only you
know have to choose this one if I press
uh control and enter it gives me 10
different things to choose from so I
could start with kind of reviewing the
code and kind of like working through
like which one of these would I want to
take I might not want to take the first
uh option or I might want to exactly
take the first option or I might want to
be for testing purpose I want to be
really difficult and take always the
last option assuming they are in some
kind of a priority order because again
it probably gives me more to test if I
take a bad version but I have kind of
this like dual purpose I don't want to
just test I've never wanted to just test
I want the working solution so testing
is kind of just you know it's it's
moving with the thing that we are
actually actually trying to do so I
don't try to set the fire just so that I
can say oh look how many fires I want to
choose something that could uh
work uh I uh don't take the bad ones I
took a screenshot of one of the bad ones
I uh you know even the manualist Tester
the person who never writes automation
recognizes that this might not be a good
thing this might be really hard one to
test because you have to test every
single thing separately but having sat
through this exercise in Kata sessions
with various levels of groups I've
actually seen some groups implement this
until they later on they then clean it
up and and want to kind of go and and
move forward it might be that someone
wanted to stop and leave this for
co-pilot to find in the code
basis uh I suspect it was not
intentional but uh well definitely it's
there for for uh trying things
out similarly uh when I then uh kind of
like start to look at the uh answers uh
I could choose any of these
Alternatives so uh it definitely gives
me a lot of options and usually uh
having looked at this uh I I created the
exercise originally with pairing and
ensembling with people having looked at
this with about 10
people uh the choice the uh almost like
a paralysis that you have like uh not
being able to choose which one of the
bad ones is the the the one that you
want to
take it's sometimes a a bit difficult so
again let's do a thing call it fool we
can rename it later we can also change
the code that we have you know more
knowledge on as we are moving forward so
so trying to uh review the Perfection
isn't also the the goal that we would be
doing uh to test this I kind of in
hindsight can tell that to be
accountable for testing this there's
these five things well actually there's
a six thing that I added on this
particular version of the talk but these
five things are kind of the minimal that
we have to uh go through we have to test
against you know does it match our
intent as developer
we have to test against domain as we all
understand it like you know how Roman
numeros work right you don't by the way
you don't I'd be surprised if you know
all of the things I will tell you about
Roman numerals during this talk
today I didn't know before I tested but
now since I have tested I know plenty of
of more
things uh you might uh want to not have
to know all of these these things and
you know just refer to somebody else's
uh implementations and somebody else's
kind of guidelines and even that you
know you might want to do in a
programmatic fashion and uh probably
there's going to be something where you
know most of the testers by profession
that I know of and have watched doing
this exercise where they always start
but I think most of the developers want
to finish with is the so-called people
filtering
aspect they will put all kind of things
in and we will probably want to do
something with the inputs uh uh even if
it wasn't part of whatever GitHub
co-pilot originally proposed to us so
let's first jump into the the intent
part so let's say we have this you know
a very basic implementation it has uh
value errors and type errors so some
basic error handling is already you know
present it looks kind of you know nice
in in that sense and it has all these
kind of like you know different letters
defined for thousands and 500s and
whatever uh type of
things does this work are we done have
we tested it enough we looked at it see
any problems
anyone yeah it's kind of hard to see the
problems without seeing you know
examples of execution so to get out that
developer intent if we didn't as
developers write it down in tdd or
whatever style of testing you want to
apply then probably the testers are
going to be asking some of the questions
and they might ask them again even if
you did write them down because they
can't read them in the format you wrote
them down they're going to be asking
some of the questions on what have you
actually
tested uh what kind of values did you
try what should I try and probably you
know the ones asking you what do you you
recommend that I should try and you
telling them the things that you could
have done but you didn't do they are not
the ones that are the most you know
valuable in that scenario but if you can
tell what you already did and and their
aspect is kind of like you know
stretching on from that then probably
you're going to get a little bit more
Illusions uh broken but you know you
could create some tests it's it's uh
well having done kadas various kadas uh
it's it's kind of routine like you you
pick an example and you pick another
example and and and you make your
choices and and you can have so many
different routes on what number you
start from what do you end with and and
just kind of like not to feel like
you're doing manual testing because you
are actually doing manual testing here
by the
way uh don't do the same route every
single time start from a big number
first or small number first or you know
just something in the middle you know
the gold Delux rule so that you have for
more fun or start today from a non-
number because this is supposed to
handle num numbers or maybe you know you
can take from yesterday start uh with a
u Arabic number because they are
obviously also supposed to work so you
pick up these little cues and you make
your choice of what you start with but
most likely no matter where you start
you're not going to call yourself done
until you have you know captured some
basic samples maybe having seen every
single letter once that might be your
rule uh somebody's rule is
uh just having a single sample is enough
for this I don't need anything more and
maybe you know uh if uh you're aware uh
that you could also uh generate kind of
like uh uh all different combinations or
you could look at things in a file kind
of like you know review the results
outputs of your program maybe the style
of what I would call explorate
exploratory testing maybe the style of
what you want to do with testing is kind
of like you know put stuff in a file and
then spend whatever time you want on
looking at whatever is in that file and
thinking whether you like it or not uh
the simplest way of appro uh approval
tests is is kind of like saying that my
Oracle the thing that I'm comparing to
is that if it works currently someone
else will tell me if it's
wrong meaning uh it works in production
that's our rule quite often and it saves
a lot of time it saves us a lot of time
and we do want to to use that but we
also want to be aware that we're using
it and not fool ourself claiming that
you know we already did all the the
right things so we are thinking and we
are making uh our decisions so I have
some shapes of
approaches that I can use in in this
case I can try asserts you know examples
collecting examples I can try multiple
examples you know parameterized tests we
probably have that in pretty much all of
the languag even if I picked python to
uh show these things in today uh we can
try approval tests where you don't
really care about the output before you
see the output and then you look and
approve the output and if the output
ever changes you consider that a bad
thing or you might even uh try uh
hypothesis it takes a lot of wrangling
for me actually still to get my head
into the idea of like there's common
rule that must be uh uh available that
we can describe you know the rule of
having to have all the different letters
given enough samples enough numbers as
inputs all the different uh numbers
letters need to be generated in some of
these that I can test in this kind of
style where I'm just you know looking
for a pattern and I can describe the
pattern or I can just you know not care
about describing the pattern because it
takes me time to actually write this I
can just you know spend some time
manually testing looking for the
patterns so am I automating am I doing
manual testing I'm definitely doing a
lot of thinking I would call this manual
testing because I've always done manual
testing this is exactly what I've been
doing so um we've looked at this and
it's developer
intent do you think that all of those
passing now tell us that the software
works
did you see a bug
already
anyone no bugs no
visibility so again this is where in the
interview setting my developer would
have been very happy already you know we
have tested we've tested in different
styles we've talked about you know
awareness of of different perspectives
but uh even if we did all these six
things I wasn't quite yet done with what
we were thinking of doing we had
reviewed things we had created inputs
outputs uh scale we had looked at
Behavior boundaries we had looked at
coverage we had looked at sampling and
wider Nets uh we had looked at
properties like all of this stuff this
is what we always talk about when we
talk about kind of how do we test well
in our developer teams like this is kind
of already it's not a full list but it's
kind of a a a good list of things to do
already from a developer testing
perspective
uh does anything in this slide bother
you right
now are they not correct I think they
are
correct why are they not
correct because they are correct there's
just three different domains embedded on
this single
slide uh in a clock tower uh number four
is i i i i that's how it goes if it's a
valuable Glock if it's a luxury Glock
you are expected to see I I I I not four
and if you never asked are we creating
this application for a luxury clock you
would have created the wrong
thing what about f i i i i i five what's
the domain anyone
know burying people
tombstones so in tombstones uh number
five is uh uh this and number 50 is
xxxxx so again you know I already kind
of revealed you the domain things some
of them but it's not all unfortunately
so we're going to go a little bit
further on this one so you know as a
tester I would obviously go for you know
an authoritative source and no my
product owner is never the authoritative
Source like my product owner is uh wrong
as often as the rest of us like he's
just as human as as the rest of us so I
get the benefit of arguing with the
product owner as a job
description in a kind
manner that is something that we need to
take time on the entire team but I'm
asked to hold space for the team to do
that like not just doing whatever feels
you know the first natural thing but
asking like why are we doing this what's
the domain what what examples do you
have can you show me an actual
customer and looking for specifications
that the product owner didn't write and
seeing if if those are are somehow off
so I learned uh that there's a so-called
good reference
source uh Roman numerals uh website and
you can kind of uh give there a number
and you can get a reference uh playing
with it uh also taught me and reading
the the specification also taught me
that I thought thought 4999 was the max
it's actually not the maximum in in
Roman numerals it's just where we always
end our cutas in because it's simpler
there's a new font necessary after that
so we need to extend our
implementation so in order to get the
new font or the kind of like parentheses
the the representation of the bigger
numbers that this one does know how to
do we would need to think further than
the simplest possible sample that we
have like we are still working on that
simple small Cara and already we are
kind of like you know thinking of things
that that weren't part of that kind of
like end criteria where we always
happily uh end the the uh the kataa so
the upper boundary is way
higher so again you need that new with a
hat font uh there's other proposals of
using parentheses on representing that
if you don't have a new font available
but there are references that say how to
implement all of this
there's also um uh samples where you
could compare to for example Excel
Lovely programmatic by the these two are
I I picked them because they are lovely
programmatically available interfaces to
test against so my laziness uh is is is
well played when when I can kind of like
you know just go through all the numbers
and then do all of the testing in the
lovely generated files because I care
about looking at the problems it's
usually well it's not somebody else's
problem but i' like to think it could be
also somebody else's problem to to
participate in in the uh creation of of
all of that even if I didn't know
programming some testers don't they
still think in this way where they can
find the problems looking at at at those
samples that we've generated so find the
way of integrating but the interesting
thing is that Excel introduces this
concept of five different kind of Roman
numerals you never asked me if I wanted
the classic Roman numerals nobody ever
asked so maybe I wanted to simplified
and if you didn't ask obviously with the
same price that you offered because this
was a fix price project I'm going to
want the better thing now that somebody
else told me that it exists and I could
have wanted it because you know
obviously it was your job to ask I don't
know if you have ever had this style of
conversations with your product people
but I seem to be having this in in some
sort of a
scale so uh what I would then want to do
doesn't take actually much time I want
to create a way of of uh collecting
references you know from that Excel from
that browser page and you know recently
I've been very much liking using uh uh
uh playwright as as a way of of running
things uh against the web API I've also
been liking selenium because I'm in the
selenium project leadership committee so
I'm supposed to take that open source
project forward so I'm doing a really
bad job of taking it forward go by going
on stage and showing your play right but
you can actually do the similar simple
things with with selenium as well it's
just that we all love the new shiny not
the Old Reliable around for 20 years
that we have been able to rely on our
production use and it hasn't caused us
that much
pain uh or the same pain is ahead with
all the other tools as well because it's
not a tool problem that we're solving
it's something else but yeah you know
again going away from I want to test
this application into all the tools
we're always testing everything around
us so I can uh create these references
with the playright uh with uh well
whatever python Library uh I first found
Googling on on getting to uh Excel uh
that's why it's excels not Excel X SD
the more Modern Way of excel there was
an easier sample and I just got lazy
because I didn't really care for the
perfect implementation I cared for the
perfect information that's all I cared
about and I'm okay making compromises on
your things that you care about as long
as you do the same for mine so it's kind
of you know mutual thing and I'm okay
with the fact that sometimes the things
I care about are not the things our
project needs to care about right now
there's so many things I care about that
I can easily pick the next favorite
thing and and just use all of my energy
and my love for figuring things out for
for that uh I usually like using
approval tests for this style of kind of
comparison testing kind of generating
things in files and comparing things in
in files it gives me kind of fast
feedback and and not having to wait that
5 to 20 minutes to generate all those
numbers these are not necessarily
optimized for Speed they wouldn't be
things I want to keep around in a
continuous integration environment but
they are things that are teaching me
something right now and even if I throw
away this manual work of half an hour 20
minutes whatever I ended up using on
this it doesn't matter because not all
tests are meant to be kept around
forever
right so we already talked about the
clock towers the luxury clocks so that's
also an aspect so the business rules uh
even with the simplest things I can do
this with any of the katas it's not just
Roman numerals it just happen to be
Roman numerals because someone made me
annoyed with a a job
interview but uh it could be
anything uh and you don't really know
where they are and you might want to
actively find them and spend some time
on on finding them so again on the
domain there's basically seven
rules uh you need to be the resident
expert you need to be curious enough to
know the domain and learn the domain and
model the domain while you're learning
it so that you can teach it to others
who come after you on the relevant parts
from a programmer perspective or a team
perspective you are not only optimizing
for today you are also optimizing for
those who come after you and running uh
automation is a great way of leaving
something useful behind for
others but also uh writing uh good
summaries not the details of test cases
round in a manual fashion but writing
good summaries of of what's kind of you
know important and surprising to you
that you have learned while you've been
working on a thing is probably also
going to be
better there's rules you need better
experts your resident experts even the
one who have been taught Roman numerals
in school I had one of those to pair
with in in one of the sessions where I I
practiced this this
exercise uh uh you need to always kind
of you know question your experts and
find uh uh better ones and make your own
better by understanding if they are
aware of the world around them and we've
had great talks on kind of you know
creating that Awareness on on the world
here uh finding better oracles is is
something we would do and thinking of
the users kind of going to the error
messages as well is is something it
could already be part of the developer
intent but if you somehow manage to miss
it you probably can add to that but you
can also add to the environment it's not
just this uh on my way here when I was
flying I was reading Sarah danner's
fairly new book on uh management for the
rest of us because I felt like you know
being a new manager uh I need to give a
chance for someone to tell what am I
missing because I think I know what I'm
doing already you know the usual
illusion that new managers have but uh
she started the book with this this kind
of a very developer quotes which made me
laugh people are not pure functions they
have all sorts of interesting side
effects and I had you know like my eyes
popping out on like have you not seen
the side effects of software even the
pure
functions like we have had planes
crashing because of entertainment
systems it's probably quite a pure
function that we tried creating there
but it didn't take into account the fact
that the hardware could fail in a way
that causes a software side
effect and then things are
failing so again we are really designing
and questioning things for much bigger
things than what is kind of in the in
the scale so we're accountable we are
the ones especially co-pilot stuff
coming in we are even more accountable
than ever on asking these questions and
there's plenty of these questions to
ask and with the the questions that
we're asking it's not that we have to
ask every single time the same questions
unfortunately every single time we have
to manually craft new questions that are
appropriate for that time that context
those people that we right now working
with because there's nothing I think of
as as as the worst practice then
creating acceptance criteria by force
with a team where we already know what
we are creating and accepting but we
have to sit in that meeting for that
half an hour writing it down kind of
like you know pretending it wasn't
already obvious maybe there was
something that we needed so we couldn't
go to the conversation we all already
know because we work very closely in an
ensemble together we can't do that
because someone has decided that there
needs to be this artifacts that we need
to be creating in this collaborative
style so again everything is something
that we can question they might be
useful now but they might also be
something to look at
later uh there's some bugs you know I
have found bugs I don't really care
about listing those bugs today in in
that detail but what I want to close
with is that we've been doing full I
call this fu fu looks different on
different applications it looks
different on on different code bases it
looks different on different languages
probably different people uh and I call
this contemporary exploratory testing
because I am a tester I train other
testers new testers into this world and
I teach them basics of programming while
I teach them how to test and I hate the
so-called manual testers that I have to
recruit because they are thinking
they're supposed to write documentation
and not do
testing that's what manual testing
usually means nowadays and I hate the
so-called automation
testers because what they usually do is
they write the simplest possible thing
in an Automation and they forget about
the whole purpose of testing so I get
the worst of both words with these
labels if I'm recruiting so I'm trying
to create a new label I'm going to call
this contemporary exploratory testing so
it's founded on the exploratory
centering mindset that I I have been in
all 25 years but it's contemporary
because it is not manual I was manually
crafting code and you would probably
call that
automation I just choose to call it
manual I have learned over the years
that this is really true a majority of
bucks we can find on the unit testing
level we are not trying hard enough with
the
collaboration we need to try harder
and it's great having teams that want to
do this we are looking for both the kind
of the traditional artifact driven
Styles you know in the moment we are
looking for this performance style we're
working on all the different levels and
layers and we are looking at different
people's intent not just the developers
intent and we don't only care for intent
we actually care for the impact that's
where we need to be disillusioned right
I believe nowadays that everything that
doesn't need to be automated can get
done while automating but when you are
hiring a new promising tester if you
make them learn automation first you
make them a a a junior programmer and
they could be a brilliant tester in half
a year if they could just focus on the
information first in 25 years they'll
have time to learn programming it comes
later
but give them a chance of learning one
thing your team needs right now first so
that's my call to action for for all of
us and also go back to your work and
find something that others may have
missed it's not testers it's testing
it's all of us thank you
[Applause]
I think we might have a room for one
question if we want to take that but we
can also have kind of like you know more
private conversations I think there's a
kind of a big
crowd does anyone feel like they have a
question where it would be really
relevant for us all to get the answer
taking care of everyone that's you know
what we do as as responsible
professionals right let's have
one-on-one conversation I'm around so
please come and talk to me that's the
reward that I always look for in in
doing these talks it's not an easy thing
to get on stage always and it's not an
easy thing to travel but if I meet new
people who love this same thing and I
want to figure this out that's the the
reward that I'm looking for so please
come and talk to me thank you
[Music]
