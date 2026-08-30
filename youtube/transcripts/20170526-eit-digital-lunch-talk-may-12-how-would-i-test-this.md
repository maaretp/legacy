---
title: "EIT Digital Lunch Talk May 12 How would I test this"
video_id: qAPOGFFcb6Y
url: https://www.youtube.com/watch?v=qAPOGFFcb6Y
upload_date: 20170526
duration: 31:53
channel: Maaret Pyhäjärvi
tags: [Pair testing, Strong-style pairing, exploratory testing, learning]
---

# EIT Digital Lunch Talk May 12 How would I test this

> Video of a talk I did at EIT Digital Lunch meeting at May 12th.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

hi everyone nice to see so many of you I
know you're heating and I'm trying to
make you say hi
your mouthful that's a very nice thing
to do it's interesting to come back to
all that hearing because this was where
I went to school and I haven't been here
again for a while I did you come back
here like once a year usually talk to
the students about testing
I love days where that empty carrot has
been an out for eight months so whatever
I've done there in the eight months it's
still fairly recent I also work there
about ten years ago and for three years
and I have this habit of changing
company them in two to four years so
I've been around a bit and nowadays one
of the things that ways of being around
is I like doing talks at conferences
because that's one of the best place to
learn work even correct you you know you
get experts listening to you and they
correct you or they say to you the
advanced or anything is it the old you
are my experts today in that sense I'd
be happy to to get your comments and
questions feedback any time so just you
know feel free to staff but I'd be doing
this conference talks a lot not recently
so I just realized that I've done 75 in
the two last two and a half years so
it's kind of like a colleague of mine to
to travel around the world in somebody
else's money films like I suggest
everybody will try that for the standard
white happy forward to know much that's
kind of what I found the thing we're
going to be talking about today is well
the tile is very fancy when there's two
different versions of it it's not big
desert live learning in layers or when I
try to explain this to somebody - Daniel
talked about export or nesting and this
one guy that I was talking to he looked
at me and say like can you tell me still
what that means like he was talking to
somebody who isn't the developers but
nobody knows what it means and I don't
you know if at that point when he was
asking me and if I can for book
something I've
confused oh and how would I explain all
of it had come to my talk is gonna take
them the whole talk to explain it but
then I realized that that I should have
told him that I'm kind of like a
feedback fairy in software projects so I
come with all kinds of information and
use usually the news is that things are
not quite as we opened me you know
something that will work and I know in
the sense that we're the end users
telling you in various form words and
and which might include shouting and
might include not sleeping tonight when
you're fixing things and I tend to give
you a bit more of a head start on
getting the 60s down so as I kind of
think of myself as a feedback there so I
do software testing some for testing and
I learn about applications so that I can
teach the others what we didn't get no
and what we might want to react on so
that's what we're going to be talking
about today and we can also be doing a
little bit of a demo so let's begin an
idea about the type of testing value you
will see code but we will not be running
from today so so that's not being there
the point of the talk today
looks like the slides are working a bit
weirdly here today let me check it it's
not half of my text here now it came
back so it's just all there so the
things I usually do is that I thought
person's on a drug awareness that's the
type of fuse and III provide so we have
all of these ideas or we besides things
to be in a certain way and then you have
to actually use the applications you
know check you things out through web
accessibility but you're also looking
for empirical evidence of things that
you didn't even expect so one of times
the way I think of my work is this kind
of this anapestic I break things but I
don't break the code I break people's
engines so people have these perceptions
they believe that
end users will be happy when we give
them this feature and I tell them that
you know the enthusiasts will be happy
but they don't be giving up money for
that so I have developers telling me
that you know I coded it it should be
working
or it's because I made it work I even
tested it myself and I go and try it and
do it twice for example last week and on
the second time it didn't work so again
without these illusions that we built
from things on power software actually
works and what making it fail and that's
the information that I I tend to come in
second so the approach that I use is
corn exporter this thing so this whole
very complicated term it basically means
that I look at an application I come up
with ideas what I do with it I look at
all the information around me for all
the 23 years that I've been doing these
kind of things and I put them
systemically together to figure out the
information so discover risk discover
things might be missing and being very
rigorous about that
so you determined that the first slide
learning in layers it means that when I
go to a new application I of course will
know much about verification
I have never seen it before it may get
worse just implement it it hasn't been
used by anyone other than you spell
operator instead of yourself and while I
don't know much on the first half an
hour
after the first half an hour I know more
and we are in work it's kind of like the
attitude I think this is a general
professional attitude that would be a
good thing to learn for everyone is that
whenever you go to work on the next
morning you're supposed to be a little
bit of editing and testing is just my
way of being very active and very
deliberate about that learning but all
of this kind of still sounds very
abstract so that's why I want to show
you how that one actually works on
so we're going to be looking at a new
application fairly soon but little we go
into that I'm still wanting to kind of
give you an idea that nowadays we'll
talk about so for adjusting there's two
kinds of software testing that we talk
about there's this usual live-evil who
say traditional way of looking at the
processing and of course testing and
artifact creation your end result is
that you create this you run tests the
discs are creating games tickets are run
and this artifact that helps you do that
kind of fix it's awesome nowadays in the
modern world where we might have a shape
place like a detail check click on test
cases but in the modern days we are
trying to both automated so we have a
lot of test automation based operational
events but we're also trying to push as
much of it into the smaller scale unit
testing schedule as possible but then
again there's different sizes of units
so that's why I use the word unit
testing on this slide so it could also
be automated testing these types of
testing testing an artifact creation it
basically gives us four kinds of things
four kinds of informations if we do it
before we try to implement something
software development it gives us a bit
of clarity on what we're trying to do a
you know an example this is what it's
supposed to do if I do this this is
supposed to happen that's good defective
part of it then when you're implementing
if you have that access automation will
be the test driven development
approaches or think that motor was
cetera you can feedback it was supposed
to do this doesn't do exactly that
then later on you know months pass and
those sets keep on running
on every time you make a change thanks
people running and they show you green
or as well and one of these days they
show you which something is different
than before because they keep on doing
two things automatically in the
background that's when you get the other
value which is regression you get
but for something being different than
before presumably worse than before
another information we're going to react
and the last bit of these kind of
sensing our defensive regularity
depending on how big of a scale we are
looking at there we might be able to
pinpoint immediately oh I change here
this broke here's the connection and
it's also fixed things immediately
whereas if you have a big thing that
you're going through maybe you need to
mend your scores you can read through
whatever results were there before you
can pinpoint it so hopefully it gives
you also this type of test it gives you
granularity and this is a doesn't have a
part of getting this is the test
automation part that most of my
colleagues for example executed and it's
a important work is a full-time work of
several people and code developers but
they are developers and testers at the
same time I participate in this
sometimes but my name focuses on the
other kind of testing the exploratory
part so I think of testing other kind of
testing the one that I focus on as
tempting as a performance kind of like
you know you go on stage and and you are
kind of improvising you're thinking of
what's the next thing that should happen
you have an overall idea of where you're
heading and what kind of things you want
to do but things won't always go quite
as planned you might learn something on
the way and that makes you explain
things for example in on and page it
differently
so this thing is a performance it gives
us a big different type of feedback as a
protostar it gives us guidance there
doesn't say gifts or no pass or failure
it says is this a good direction should
we have a discussion about this in
silver black and white path or not we
might be able after that discussion to
turn it into a passive error or no task
type of feedback thing but before we
have that discussion it's usually more
more of us understanding is these kind
of things are relevant we haven't
and talked about them yet in case is
also a deeper understanding but very
more going deeper so and then
specifically have these cases where it's
all been automated on our new component
you know we write on the live say it's
done we're very fluid in production in a
test automation and I look at it and I
have 30 more issues to find so but these
are understanding of things and how they
connect is something that is easier to
do in this performance type of mode than
focusing on the details
it usually keeps us models meaning I can
teach things to others faster by showing
this for it looks like and it gives us
serendipity which means lucky accidents
I think one of the best examples that I
have out of a lucky accident is when I
started in my previous plays a word
before is teetering on day one nobody
started the new employer employees you
have these like introductory sessions
like somebody that shows you about the
company but they thought it was me so
that they gave me the access to the
system but here's our web application
and I linked it I put the link into in
my mind bookmarks and then I went into
this like you know company numbers how
many employees wrong type of things
I came back about three hours later and
if I didn't have the link it would have
been hard for me to remember where the
application was but since I have the
link I clicked on it and the application
question that's something I didn't
intend on that day but I will given the
application enough chances and being
rigorous about it so that I would found
with later on as well if I wasn't lucky
but a lot of times when we know we spend
time with the application and we do
things actively differently
certainly the ticket of the monkey
accidents of problems that nobody
expected and those are the problems of
end users tend to see a lot not into
anything diseases so I kind of look at
this so that the product it's my
external imagination 23 years with
software testing means that when I see a
new application
please personally India here is button
do this it tells me but well my
background is correct I can say why
would anyone anyone want to use this and
the application says maybe it's because
try if you could do so come on I had
this continuous dialogue with the
application so that's the special part
of oh hold on hold on you and I'm going
to listen to the application because I
spend so much time with various
applications I can collect information
from for business science and from
medical side and can attend and I am a
programmer as well so I can also use
whatever programming tools needed to
extend my reach in how it speaks to me
really asks me to do but the reasoning
is is there the hard part and I'm
noticing that a lot of times while the
program is my external imagination I
might developers and my teammates
external imagination I was staring with
the developers sitting next to him and I
decided to not say a word he would look
at me and say oh you'd want me to click
here I didn't say anything
perfect crash you want me to use
different data here like I'm using over
the same day that once you know that you
should but like I didn't say anything
and they change the data that they be
using an intuitive crash so they know
how to do this like everyone can learn
in layers and actively change their
behaviors with the application it's not
that it's just the specialist everyone
can to study on this but sometimes my
developers need me as the external
imagination so that they start thinking
of the ways it will fail you or could
fail something that they haven't yet
considered so this is shared where you
view
so the second point that I want to do
today is to show you what detection
means with a new application so for this
I will need a volunteer because and one
of the things in software development
including testing happens you know
inside somebody's head that's not an
incentive if I use something and it
happens inside my head and try to use
the computer at the same time it's going
to be almost impossible for you to
follow what I do and why I do and if we
want to see kind of a death type of
things that the intention was that you
see today I will need somebody to be my
hands and the place on the computer I'll
call that a resting place it's not what
you have you don't have to be
responsible for anything all the
thinking all the ideas of what needs to
happen in testing come from outside the
computer so people in the group can
suggest things to me but I'm the main
responsible tester here so I just need
somebody to be my hands and this style
of pairing is called strong style
pairing and I really like doing this
with month for tibarn of keeping your
intern that has been joining us that he
stays to be my hands for the whole made
it was also molested too dated now he
understands testing and he wants to do
this a sport so it's a good thing to do
so or an idea for my head to go to the
computer availability would be my hands
today all right yes
get them cooking I will move here I
think here I can beat up but still the
camera
all right so this is as much coal as I
will show you we have about at a 10-15
minutes of testing that we're already
doing so that's not a lot of time of
testing so we can choose to invest and
testing in this new application with all
of the source code on this machine in
any way work that's the power of export
or next one you can do whatever you want
but instead of you know reading all this
code I want to get something done in the
ten minutes that we're spending on the
computer so let's the start the
application so from the application
there's where we will green button on
the probe we start the application if I
wanted I could treat the code that I
just figure out what's wrong with the
code but you can imagine that's going to
be much slower than and what we're going
to be doing so here you have an
application I have a bit of background
information on it it's called dark
function editor looks kind of ugly right
a connection screen I will really say I
would like to talk somebody about how it
starts up and how bad it looks and maybe
actually we'll start by making a note of
that so in Safari open the Safari and
just my notes like my main tool of
thinking is that whenever I have a
feeling it's a trigger for me to make a
note of something to have a discussion
with someone else or help light our sink
so let's we can also put there bugs like
a pic on the middle and then tab and you
get another note under it yet and right
bugs and then our tab again or enter a
time and under that lets a startup looks
ugly but the story is very like it
really doesn't give us any information
of
so if I would have a commercial
application like this it wouldn't debug
me a really good first impression so
that's something that I would really
want to talk about with them let's go
back to the application a three-finger
swipe to the right I think three fingers
on the most touch and then get there
I've been doing this a bit nowadays not
touching the keyboard which is extremely
difficult to do in the beginning because
we have thousands of hours and like from
our guide through the keyboard but this
whole disconnect it takes practice
and I've been doing this one or two
years old getting getting to survive
with this one so it's out but there's a
file menu click open file menu and I'm
next create something let's do an
animation since I know that there's
these beautiful animations again and we
need some test data created for us
before so you have repositories click on
that and that's function editor that's
what the tool is called is the resources
Star Wars images any other farmers down
here yeah and as we all sprites have
taken the last one so now we have some
test data alternate navigation now let's
stop for a moment I tell you what the
applications about the high level to
light thing about this application that
it's an editor post price you can create
moving animations and that's all I need
to know to get started with testing so I
want to do something with the editor for
that purpose and again I'd ask what are
you would anyone want to use that's
usually that the first question that I
have but before I can really answer that
I need to see you I what can you do with
so can we get anything done here anyone
in the audience what would you do here
click the green button click the green
button was an obese you know so so the
first thing I want to do is make a note
of the back in there yeah
Safari
they cannot not about that it looks an
act inactive in the editor inactive it
actually is inactive I see a group of
people testing this spend ten minutes
before they could figure out press the
green of them let's go try to pee on her
person yes so now we don't test it and
again I have very little time for
testing this today so I need to make my
choices of what I use my pheromone as a
test there very deliberately I just
decide you know I want to find the you
know the sunny day scenario that's
usually a sort of devotees but I like to
send all whether the idea that the
tester I can choose any piece that I see
on the screen that kind of regular
speaks to me and this bit here could
speak to the old it's kind of shouts of
me and release and it's a button it
should be like a neural easy and focus
testing it's a little bit network so
let's try the whole bucket that we have
I could ask usually I would ask him to
make notes of what each of the buttons
are like on this thing every
functionality so that I can make sure
that I I don't see no keep track of what
I've tested and howdy bus is in there
but since I'm saying is hard on the
finances let's destroy them let's treat
the best of us against if they're an
ulcer context or not I know bus on the
plastic pell-mell terrific oh yeah oh
yeah there is something so it's an add
an animation thing so it seems to be
like so move on a high level doing that
let's try the mind by - that's the
delete okay and when we delete did we
didn't have the other ones ask you many
more can you treat that one as well so
much has been to go back to the original
thing so yeah okay so then the past and
I bump again
if they inside one hour active but we
have chosen things try to unite so
duplicates seems inactive I'm gradually
making over this but can't really see it
seems like it's inactive it's hard to
how to say that so let's make a note of
that just the Box today so let's say
animation pane and tab under it and
let's say you put a book inactive it's
probably duplicate and then tap I'm
going to do together I assume I will
find more problems from the duplicate
when I continue testing on it so I'm
kind of building this map of things that
I can move around whenever I want
I'm not going to be demoing much longer
today somehow Philippines go now thank
you for my training on this particular
thing here there's so many other things
that you could use like this double
clicks and right clicks and some of it
works and some of it doesn't
it's almost inconsistently I've had
groups report 30 problems that little
box alone this application in general is
a great demo application for testing
because it's what I would call a
target-rich environment so it has a lot
of bugs it's an open source project
somebody made a tool for his own
purposes open source in anyone other can
use it let's see if there are some one
of the relevant amount of downloads as
well and I've noticed that recently the
developer has closed or both reports
saying only bug reports through
submissions to fix this around so I
suspect that as I introduced some money
into the project where they wanted to
tell how it doesn't work
I've never taken the time myself to
report back to the developer but on my
normal day of work that's all I do I go
and talk to
developer about these problems but I can
also every time I see something I can
actually make the decision we were
interrupted in in order right now or
will I interrupt turn let's say in two
hours when they're about to come back
from lunch and we'll be as much
interrupted by be going and talking
about these these things so people are
more specifically they're susceptible to
or more open feedback that research
actually on this after lunch so if you
are convict and you want to apply for
our freedom for jail most mighty time
when you get that is right after lunch
so you know all these kind of
psychological tricks seems from
something else's a lot of tests there's
going to be and to be interesting but
this kind of testing there's a lot of
free forms with but I would like to
mention that there's actually three ways
of scope they look like how much of this
use I do this as my so more way of doing
also automation within my work I explore
our time box doing something in
different ways and it's the way I
organize all of my work it's very
flexible and and my plans change all the
time so that's one schedule is it's it's
a way of reading as an export register
other people to do this so that they
scope one day a week or two hours a week
maybe having the whole team come
together and take it in this way and
there's also organizations that have
traditional test cases and they scope it
so that they tell the testers to read
between the lines if it says click here
why don't you click twice if it doesn't
say what data to use why not use a
different dataset than you're using
yesterday be always actively difference
or three ways of scoping and there's
even more ways of managing there's thing
called session basis management's click
you laid into a couple of hours what I
do with my maps is called web-based pest
management there's all these bring
people together then our goal by change
limiting on 24
is managing a store interesting so this
can also be very very visible on what's
going on and what you're learning
depending on how much you want to run in
this on this management a lot of the
things that I know that I need to do
come from ideas called tests heuristics
so there's no rules of thumb on what
kind of things typically fail if you can
do this
Goldilocks too big too small and just
right usually some of them fail and one
of my three favorites is that so-called
coffee great tips leave it somewhere
when you go for coffee or lunch make a
note in post-it notes usually where you
left it and see if you can continue
after lunch it's okay if you can't
continue it looks you out but sometimes
you can't get back to the thing that you
were doing before lunch because you left
it in the middle so that would be a more
relevant mark like I said I'm also a
programmer even though a lot of
exploratory testers don't need to be
programmers I've identified as a
programmer for last three years but then
again for realizing that I've written
code in fifteen different languages over
the last 23 years it's kind of funny I
didn't identify as a programmer is one
but the automation of the code that I
write tends to be disposable updates
from our nature so the repression
rerunning and seeing the same problems
that's not usually the problem I'm
solving I'm trying to figure out how
could I get 10,000 rows on the system
without you know taking so within and
how sometimes but that's the stupid we
have those two scrappers and in this
current world I want to throw this
teacher here saying testing is
everywhere talk about these worksheets
left which means try not to dis only
with the application but since we know
what is releasing applications on a
daily basis or on a weekly basis
depending on on the organization
wherever it hears for implementation
looking after the implementation is also
before the next implementation so you
can piss wherever and both the different
style of testing kind of take presidents
or the your activities and you sometimes
and a lot of the 50 melody can happen
against the version that is already in
production only the critical stuff of it
has to happen before so feedback can
happen also after we've already
delivered most amazing features most
amazing aspects for a union in
production so what I'm going to end it
with is a picture from my daughter she's
eight years old I asked her to draw me
the three main roles that I think to run
into as in the world of home testing
there's people like me that's apparently
how I look according to my daughter like
who identify as sisters professional
testers the best ones of us tend to
identify as exploratory testers but some
of us don't want to use that label at
all because you should be able to test a
dancer there's really great testers who
focus on tech information I think of
them as distillation programmers but
they can choose their own identities
everyone is free to call themselves
whatever they want in the world
I get corrected so much on what I can
call myself I feel very strongly about
these kind of things and then there's
testers who like to identify us
application programmers or even business
product owners and even if they don't
realize they're doing testing this whole
learning in layers giving you feedback
being active about things you see it's
kind of cornerstone the way we
collaborate and work together nd in the
world until it is there for a while and
has helped me find people to learn from
but not being a tester not identifying
as a visitor or doing things that are
not testing as such they make me more
valuable so for me it's important to be
a tester I don't need to be the fireman
who starts to be an arson spying a fire
so that I can you know take them out I
can help people take the fires out
before they ever even as a village but
the fires are still a big part of my
life
so that's what I'm going to share today
[Applause]
