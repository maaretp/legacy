---
title: "Maaret Pyhäjärvi 'Exploratory Testing -- Explained and Experienced'"
video_id: alZtLZ2FH8U
url: https://www.youtube.com/watch?v=alZtLZ2FH8U
upload_date: 20120902
duration: 1:39:25
channel: Latvian Developers Network
tags: [User Group, Latvia, Development, testing, Exploratory testing, LDN]
---

# Maaret Pyhäjärvi 'Exploratory Testing -- Explained and Experienced'

> Presentation: Exploratory Testing -- Explained and Experienced
> Speaker: Maaret Pyhäjärvi
> Event: http://www.meetup.com/Latvian-Developers-Network/events/78146752/
> Language: English
> Slides: http://db.tt/OMzMBYw8
> 
> Maaret talked about misconceptions on what it means to do exploratory testing and why would that be relevant both as agile way of doing testing and as an essential feedback mechanism in agile projects. In this presentation, she will go through what exploratory testing is with a couple of exercises and discuss the common misconceptions of its role and purpose in agile.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

before I start I wanted to ask about you
who are you how many of you are
developers anyone
good any of you sers or QA type of
people okay project managers or scrum
Masters or that sort I have these three
categories of of people and some people
are in all the three categories and and
and moving around my name is mar uh I'm
from Finland and as my main job in
Finland nowadays I work in a company
called prund uh we work with uh civil
engineering we have 500 people in the
company and we have 15 people software
development team and in my software
development team of 15 people or
actually couple of te couple of products
uh I'm the only tester in the whole uh
group of people but uh during the years
uh while I've been working uh well I
started with localization testing I I've
moved to functional testing I worked
with small organizations and larger
organizations I worked with agile
organizations or organizations that have
actually gr AG while I was there and I
work with really man driven organization
uh even after I started doing
AEL so one of the reasons uh why I had
experiences all around is well I've done
Consul but that's not the main case I
I've built my whole career on the idea
that I want to learn as much there is
about testing as possible and one of the
best ways to learn testing and about
testing is to do
testing and and to do testing for
different kind of systems and different
kind of organizations I feel that the
the best and the safest way of of doing
it is actually changing jobs every two
or three years so uh then I have an
employer I'm an Insider they care for me
just as they care for anyone else they
know I'm not going to be there forever
but they know that within the two years
that I promise to all of my my employers
uh they will get as much as I can give
them within that time frame and
sometimes uh I might agree I go for six
months like the FC year where I worked I
promised I will go there for 6 months
and I ended up the three and a half year
so some organizations and some ways of
working you might have fall in love with
and the only reason why I left fure and
agile at F secure is actually that uh I
was on maternity leave for three months
I wasn't the way for a long but I had to
train somebody to take the position of
to do the things that I had done and she
was so brilliant in the job that I
really didn't feel like going to take
that away from her after she had sh how
well CL us so that's kind of my
background so I work with testing quite
a while I've done various kinds of
testing and uh quite much nowadays into
agile why I end up there that's a a long
story uh that I'm not going to try to
talk to you about right now but we'll
talk about exploratory testing and I try
to give you some ideas of what that is
and answer any questions that or
concerns that you might have on what it
means but let's first try to see what it
includes uh the other of of the talk or
the the thing that I'm prepared to talk
to you about is that a lot of people
have ideas of uh what's testing that and
uh they have a lot of uh wrong ideas
also about the role of exploratory
testing or what that action includes so
I'm trying to to clarify now ify that a
bit we do a couple of exercises just to
give you also a feel of of the types of
things I'm I'm trying to talk about uh I
call that testing mathematics so the
exercises are around
numbers uh and it's uh sort of a joke
coming from the the era when I used to
do Testing Research at University uh one
of my professors uh when I tried to
explain testing to him he said you're
not talking about testing that's project
management and another one of them said
you're not talking about testing that's
risk management and the third one of
them said that's configuration
management and then I asked them what
testing actually is and they told me you
should come up with this formula where
there a Greek letter like Sigma or
something and it would tell me that you
enter this specification and outomes the
test cases that's what Testing Research
is about and I'm can trying to convey
the message that actually I've never
seen testing as part of mathematics
there's much more psychology in in
testing so let's start from that then I
want to talk about export testing what
it means uh Define it a bit more uh as a
way of of working within testing in more
of a bit of agile ideas type but also
what it means if you do Agile
development and your team need different
kinds of testing including expor testing
what's the purpose of of expor t
that kind of settings and the third
thing uh that I plan on talking uh uh
today is is uh the uh big areas of
misconceptions how to manage explor
testing it's not free for everybody
jumps around type of testing there's
actually ways of managing it they are
not the same as for traditional test
case based testing but there are still
ways uh it's not uh testing without any
automation but it's actually uh
extending the reach of of human mind
with automation or with tools with
anything that we can use and and the
Dynamics the things that you would need
to learn or know
about know about in order to uh get
better at explor testing so it's like
many things but we'll uh go through them
uh to some
level let's start with the testing
mathematics uh I don't have any here I
don't have any any Greek letters and
like I already said I really don't
believe testing is is taking a
specification and somehow mysteriously
using some formulas to come up with the
test cases I believe testing is is
something that happens here and it's not
something that just testers do but it's
actually something that both testers
developers project managers any roles in
the project can do but it doesn't happen
if you don't take time uh to actually do
it and it means you have to have hands
on time with the software in whatever
phase or uh uh state it is uh to do some
kind of use actually this but the first
number we're going to go through is
number 20 and it comes from a little
kids exercise I I learned from Le and
called 20 Questions finish Cas 20
questions but uh I got this from from us
in compass and I took it as as part of
of things that are good to use 20
questions is a game uh that we could
play with two strategies basically uh
the test case based traditional testing
type of strategy would be that I would
ask you to take out your pens and uh
papers and write 20 questions on paper
and then uh I would have a limited time
available for you when you can ask
exactly those question questions and if
anything surprising comes with a couple
of questions out couple of test cases
out of of of the the the the budget but
uh you most likely will get to 18 or 19
because you are so fast in asking no
questions because they are already on on
the paper but the trouble is the thing
that you're trying to find out the
questions is something that you don't
actually know yet and you're supposed to
learn about what you're you're looking
for so the other strategy is this
exploratory testing uh approach type of
a strategy where the idea is that you
can have as many questions as you like
in your head and you should actually
learn certain strategies on on how do
you you approach the the problems that
we have in testing like how do you find
out things how do you know what it works
how do you use the software in many
different ways and how do you consider
different
dimensions so the uh 20 Questions game
I've WR a word
here you can't remember what I wrote I
have to see okay now I
remember uh and the rule is that we'll
play with the expor for testing uh style
of rules so you can think of the
questions beforehand but you can use the
budget that you have for testing the 20
questions so that you can and you should
learn from the answers to the previous
questions and change your mind about
what's the best question to ask
next uh and since this is a game the
question should be formulated so that
I'm only allowed to answer yes no or I
can't tell what I can't tell whether
it's yes or no so only three possible
answers so you have to formulate the
question so that I can I can answer it
in that way so as a group we're supposed
to find out what did I write
here who wants to
start I usually remind people that like
in testing uh there's a limited budget
and the budget is f so if you sit here
quietly I just have a bell ringing every
20 seconds and the budget still goes and
it's the same with testing if you have
the the block and you see the starting
the time so so be brave there are no
questions less than five symbols is it
less than five
symbols no it's not less than five
symbols is it live be sorry is it live
be yes it's a live be is an animal yes
it's an
animal
domestic
[Music]
domestic
me no no it's not a household big one is
it the big
one yes it's a big one
gray color is the color gray I can't
tell not an
elephant which one I take first take
yours guess it lives in
Finland is it
beer beer is iter deer no it's not a
deer is it
[Music]
I'm really bad with my biology but I
will play yes C
grass is it elk no it's not an
elk no less than
five not more than five was the question
as far as
I sorry is it wolf yeah no it's it's not
it's not a wolf you're a 12 so you need
to find questions that limit down narrow
down is it dangerous for human no it's
not dangerous it's
human what what what is the first
letter answer yes or
no if you start guessing
letters no it's not a fox
is the first letter greater than n so in
alphabet's after n no it's
not
for many it was 15 so have five
more I think I might have misled you uh
when we're talking about domestic
animals
I believe domestic animals are are
animals that live at home and now you're
looking for the forests and there's
other places that home and Forest so you
might want to go
there do in the water no it's not Liv
water do we eat this animal
usually usually we don't eat it
I'm bad at answering these questions
because I need it
so what types of
animals can f no it doesn't
f uh does it have have four extra uh
four Mi yes it has four
legs does it have tail yes it has a
tail
hor sorry
horns horns horse yeah no it doesn't
have horse is it horse yes it's a
horse I think the the domestic animal
you false answers first is course is are
consumed they are in sausages yeah I but
normally I would say people don't need
hor I should said I don't know just like
dismiss that and the other one I think
domestic animal is like in a way it's
domestic but it's not like in
ter but I think we got the the basic
idea of the exercise that if we're fixed
if we have fixed the questions that we
going to ask and we are not able to
learn about the things things that we
learn while we are doing testing uh uh
we need a larger
budget larger budget and we most likely
are not going to provide as much value
as we would with the the same budget
that that we have have
available the other exercise number 16
I'm in my computer part so we're going
to do a bit of
testing some of you might seen this
so it's
ready uh this uh uh video is a video of
two basketball teams uh passing
basketball uh from a player to another
and within the video uh we're supposed
to test how many times a white player
passes the ball to a white
player uh since I want to emphasize the
differences between Explorer for testing
and the more of a traditional type of
test case testing we're going to use the
traditional type of approaches on on
this exercise which means you can
imagine a test case in some test
management tool like for example quality
Center where the one of the central
Concepts is is uh that the test case is
a pass if it's if you get what you
expected or it's a fail if you get
something else anything that isn't quite
what you you expected so I want every
every one of you to provide me with a
pass or a fail so you need to count you
need to find out testing this video of
whether there's exactly 16 passes from
white to
white uh the video is not very long so
so you don't have to focus focus too
long but uh I think we can probably
start testing so 16 I want to know pass
or fail
right
how many of you thought it's a
pass okay anyone thought it's less than
16 that's quite common as well anyone
see more the
16 okay yeah they are going all around
so it's really difficult to count and
really difficult to know do you have
anything else to report from yourest yes
I you know the answer anyone else
anything else to
report there was some person some person
any anyone saw the
person you see the
gorilla yeah there was a gorilla in the
middle probably not all of you saw
it uh anything else than the
gorilla I'm not satisfied yet so
anything else you have seen this before
you don't you know all the the three it
was a different with the same idea so
you still missed couple of things
assuming too much uh did you notice the
curtain chased color was bright ready
first and orange in the end and one of
the players we left the field in the
middle of the game so there were a lot
of things happening and and I made you
focus on just one aspect I told you with
a test case I wanted to know pass or
fail so I made you focus on just one of
the aspects and the phenomenon that uh
this video uh is is trying to show it's
called Uh intentional blindness uh
people are blind to things they are not
told to look at and what I worry about
uh within exploratory testing is that uh
if we're told to count to 16 How likely
or actually how much more unlikely it is
that we're going to see the gorilla when
we look at it for the second time it's
quite obvious and we can't miss it but
on the first time a lot of people miss
it and one of the the main things I
wanted to teach uh with this example uh
is that uh testing doesn't happen here
it's not the the action that happens at
the keyboard but it happens here it's
whether your brain is is uh counting to
16 or whether you're looking for
something
unexpected so you might uh want to
consider consider that uh for for your
testing the third exercise I have a
magic number
1639 and this is just the work pack that
I opened from from a Windows XP machine
uh and you can try this with other
windows machines as well it's uh still
available the demo effect let's say that
way it's still available in in future
versions uh if I write here
1639 I want to stop right
now what happens when I present it
that's what you should ask yourself when
you do testing you should actively stop
yourself and ask what is it that I
expect that would happen what do you
think would happen when I present
now I can do it this way let's put there
some text you actually see what happens
font size font size
1639 so error
message really big text those sound like
like possible things to happen and most
often we don't have specifications that
would be so detailed that they they tell
all of these things like if I press this
one what exactly will happen if I press
it twice what happens then so we
actually have to stop and think and it's
good if we have requirements it's good
if we have specifications it helps us
narrow down the the field but still they
are never complete never perfect and
never they have all the answers so I
press enter and your guess was right I
get some kind of error message like you
can see from the number I chose the
number so that it's just barely above
the the allow number so I click okay
here and it goes back to the default but
like with software there's many
different ways of doing the exact same
thing and that's one of the things that
uh uh uh I I feel that we we need
exploratory testing for that we would
identify different ways and different
places uh without actually making it
cost us too much so uh uh from the
context menu
there's also a a choice called font here
so I have again a font dialogue and I
can do the change here what happens when
I present it should be the it should be
the same that's what we we would want to
happen now what happens is that it's
it's really big so actually both of your
guesses were sort of right depending on
where you where you start the the
functionality for what it now shows and
what it says there that's the next thing
I'm going to show you now it gives me
the error message again because that's
not allowed it
says 6
38.5 and I as you saw from the error
message it's not allowed there so now
I'm kind of stuck with the the error
message that that it's still there but
what I wanted to emphasize with this
exercise is that there's so many
different ways in software to do the
same things or similar things and if we
are trying to uh write detailed test
cases to cover all of these things where
they might be relevant with this
particular one isn't relevant risk I
think but there are other things that
are relevant
risks uh it takes us a lot of effort it
takes us a lot of time and it cost us
money so uh since there are ways of
actually in a controlled way doing the
same thing uh uh without actually uh
creating that kind of documentation that
we used that we've been taught
traditionally uh maybe we actually would
like to use use those approaches in in
finding some of the the
problems uh on the last one I don't yet
have an exercise I'm still kind of uh
preparing for for that exercise I I
found one but I haven't still taken it
into into use but the last number 5 +us
two it's a a concept from psychology
called human envelope it's there to
remind uh everyone considering for for
testing that uh human memory is
limited research tells us that humans
people they tend to remember five plusus
two things at once this is from mid 80s
this is 5 plus- two there's an earlier
article from uh I think it's late 70s uh
just before uh uh 80s uh it said 7 plus-
2 and there's a more recent one telling
uh from 2001
and it's four plusus one so for me uh
I'm considering like I'm thinking like
the people today do we actually even
remember one thing at a time so it's uh
to remind me or remind everyone that
actually even though we're talking about
cutting down documentation and and and
and doing things in this exploratory
style which we go
into we actually still need
documentation the documentation just
looks different but it's still exists it
might be pictures it might be uh uh
supporting uh uh checklists like
remember this from that like reminding
us of things so it's more of a
structural uh uh thing than than an
absolute list but we still need the
documentation so that's the test in
mathematics and all of this uh let same
explained uh in text all of this uh is
is going towards uh the idea that for me
all testing actually is
exploratory uh there's ways of doing
testing so that you write things down in
detail and I would probably call that
too exploratory but if you're actually
planning on delivering any results of
your testing there is going to be
surprises so even within the most text
uh test case based approaches there's a
lot of the exper for side side embedded
in that so exper for testing that's a
it's like a mind frame it's an approach
a way to to to go uh and think about
testing and it's uh it's kind of like uh
you're driving a car you need to learn
to do certain things to drive a car you
need to use the the the the uh gear
stick you need to use the pedals you
need to know how to press them and when
to press them you need to remember to to
turn the wheel all all those
things and when you're a newcomer uh it
seems really difficult to to uh do all
of them in the right time frame quick
enough and and in the right order but
when you actually get uh uh to know uh
the activities that you're required to
do when you're driving a car uh it goes
into your SP and and you just naturally
do it and it's the same with testing but
the activities are a bit different the
activities are that we are learning from
the tests we're actually uh executing
the tests uh we are uh setting up
configuring the the environments uh that
we're using for testing setting test
data whatever we we need to do
uh and we're coming up with new tests
based on on what we learned or what we
know and and and didn't uh get from the
the most recent results uh the
definition uh usually talks about
simultaneous but uh one of the things
that we use the daytime today for is is
to show that simultaneous actually comes
only through practice
while you don't have the the these uh
very short Cycles Within These different
tasks you're allowed to actually take
half an hour 1 hour two hours or even a
full day into thinking about what did
you
learn and and and and what uh what's the
the impact of your learning to your next
test cases so you are the driver you
decide how fast you go and when you
press the Bal and and when you when you
stop the the car so uh uh at first you
probably do them slower they are not
really uh simultaneous or intertwined
but the through practice uh in exploor
testing they get so intertwined that it
looks almost like it's it's
simous uh it's disciplined and a planed
approach we uh we're going to look at
the management framework uh still uh
briefly and the last bit I wanted to
emphasize on on this slide is is that uh
people are starting uh on the research
side people are starting to look at
exploratory testing as a real option uh
this is one of the the first articles
that has been published in academic uh
academic side and I'm hoping to get uh
more of of of of like real live case
studies and I'm really proud of youon
who's my colleague in Finland working
for hsin University of Technology and
and doing research with companies on
this kind of thing but the first results
are from comparing students given the
same amount of time for handson testing
uh with or without test cases you get
the same
results uh with exploratory style
without the detailed test cases uh you
get less CLA
positives that's his finding and of
course somebody needed to do the
preparation uh for for the the group
that use the test cases so it actually
took a lot more lot more time so we
should really consider the time frames
of the value that um documentation or
preparations give us and we should react
on on the learnings that we we get from
there uh in actual projects uh uh one of
the ways of of of looking at uh testing
that you would need in an actual project
or actual team uh is to use uh this
testing quadrants it's quite common uh I
think a lot of people at least in film
have seen it before for but there's few
twists that i' I've added here uh from
the very recent uh discussions online
that I been
foll uh the the basics here uh they come
from Brian mer uh and and the the the uh
appearance that I have here it comes
from Elizabeth Hendrickson who just
recently talked about it that we have uh
basically two accesses we have uh things
that are technology oriented more of a
technical in nature and we have things
that are more business oriented then uh
we have things that uh support the team
or help us confirm if we deliver what we
promised there are things that in the
testing Community uh a lot of people uh
like Michael Bolton they call them
checking they don't call them testing
they say checking and testing checking
is is checking for things that somebody
already claimed and uh the uh technology
faing side that's like unit test and TVV
type of things whereas this uh business
facing side uh in agile would be
specification by example ATD acceptance
distrib development or that sort but the
idea is that you know what you're
looking for what you care for and and
you watch for that but there's a lot of
things that we don't know to care for
before we have tested and that's this
investigative exploratory
side of of the the the U the
quadrants uh there's things where we
need to investigate we we need to look
for uh risks uh to external quality and
internal quality uh uh for example for
internal quality uh we might do
exploratory testing uh for example in my
team current team we do exploratory
testing on on performance we don't
actually run the exact same things for
benchmarking benchmarking will be
probably more like here but we looking
for new symptoms that that arise uh for
for the new functionalities that we're
added to the product that we're creating
and usually every iteration every uh
increment that we're doing it's somewhat
different and and we learn uh things
that we didn't actually expect to learn
before we started doing the the testing
and analyzing the things that we can get
out of the the performance testing
testing tool so export testing is not
just up here but it's also down here so
there uh approaches where we or or
things where you should use it on both
then there's a couple of words that I
added on the Elizabeth Henderson's
latest versions the simplified version
that that she published uh uh the
testing Community Michael B in
particular is talking about Med morphic
and polymorphic tests and I think this
is one of the the key things that uh we
need to put together with the actual
testing
quadrants neomorphic tests are tests
where you actually watch uh the same
things over and over again and when we
talk about automation whoever is is like
a specialist in testing or specialist in
expor testing when we talk about test
Automation and we a bit very or cautious
about that we're actually uh not able to
talk about the difference between the
the things theomorphic tests where the
same result is what we're looking for
and the tests where our heads in a
different direction every time we do the
test and where we actually want the
variation that a machine uh maybe can do
where we looking for new information
that we can't tell the machine to go on
and move forward but for agile uh it's
really essential we have a good solid uh
test automation to keep the things
together but still uh it doesn't take
away the need of exploratory testing and
and one of the things I see in Finland
with agile teams sometimes is that they
believe that that automation uh alone is
enough and I think they're forgetting uh
that especially when we are taking and
accepting new functionality into
development our plans will not have all
of the surprise effects and and some of
the best bugs actually are found with be
the surprising things and when you learn
about them of course you should take
them to the let's make sure they don't
happen again again side but it's really
expensive to try to to go through all of
those uh uh details uh without using the
software and finding out which ones of
the concerns are actually relevant
relevant and that's one of key examples
uh in in uh specification by example com
in so I'm a tester you probably already
understood that quite well uh I've done
development for a while but I love
testing I wouldn't go anywhere from from
a testing position and when I started uh
my journey on agile methods H I remember
taking a course with one of the agile
gurus and my manager sitting next to me
asking this one agile Guru what he
should do uh with a tester who is uh so
strong on being a tester instead of a
developer and and the advice was fire
her
question uh it took me almost a year to
understand that of course the way my
manager posed the question actually LED
this quite far and uh if the team was or
if the question was phrased as as
doesn't she want to be a team member no
fire her then I would actually
understand the the the uh rationale but
I believe there's a lot of of work
related to finding out the the surprises
uh in agile team it's not half of the
work but there still relevant work with
the actual teams working side by side
with the developers and that's kind of
what I do nowadays I have two teams I
work with I I spend half of my time with
one team and half with the other uh the
other team has eight developers and the
other one has four so one tester speak
all of these people they do a lot of
testing themselves they're pretty good
at that and they're learning to be
better every day so expert testing is
not just for testers it's also for
developers uh but uh uh thinking uh of
testing some as something that only
testers to or exploratory testing as
something that only testers to that's
actually a really uh narrow-minded way
of of looking at it but uh looking at my
team and looking at the software they
put in production before I went there
they definitely need someone who knows a
bit more about testing so that they can
learn
and that's the role that I see for
myself in in
agilty so when we talk about exory
testing I I think we need to emphasize
uh that uh I always uh when I when I
describe this like basic ideas I hear a
comment like I always been doing this I
just didn't give it a name but uh
there's a difference between I just do
something and I can't explain what I'm
doing and exploratory testing because
I'm actually assuming that if you claim
you're doing exploratory testing you you
can tell your story and why you're
testing what you're testing how far are
you with your testing and how far you
should go with your testing so if you
don't have that story together then most
likely it's it's it's more of a a of a a
playing around than than than what I
would actually hope to see in an
exploratory test testers uh uh uh
approach so uh you should ask really
yourself like can I defend whatever I I
chose to do can I tell why I did that
why I decided to use time on that and
learning is one of the things that you
can use as a like as an explanation I
don't know how this works and the best
way for me to learn how it actually
works is not to read the requirement
specification that's the theory but
actually to use the software and then
read the requirement specification side
by side with the software so I tend to
choose to actually first use the
software
and then uh before I comment on on it
works wrong or not to check what's been
written down and what's been
required and uh if I see for example in
my current work I saw a typo a really
visible typo was really annoying for me
and I was talking with the developer he
said uh it's as required it was
specified that way he was telling me
that uh he got a specification where the
typle was and it was reviewed by three
people so it must must be right so I
actually had to go to the people who
created the specification before we we
actually fixed it but uh uh again it's a
learning that a team should take and
it's just an easy example that I
use about uh the power of of of
specifications that we probably should
should consider so I require a b more of
foresting that than just
uh just doing some testing and not being
able to
explain uh this uh uh uh slide uh is is
from James B uh he's one of the the
gurus of of exploratory testing and if
you ever want to learn things about exp
James Bar Michael Elizabeth HRI great
sources James Lind from great sources
all in
all but the the point with this one is
is that when we're actually talking
about what's explorator what goes for
exploratory uh there's a lot of
different uh uh uh approaches to the
level of documentation or level of
exploration that is
included uh you can have freestyle
exploratory testing it's the the most
free form exploratory testing where you
basically just report your bucks that's
the the uh the uh uh guidance that
you're getting getting for for how you
do your testing and all the rest
whatever documentation you create
whatever you need within that it doesn't
come from outside but it comes from
within the the the
activity uh you can have people working
on different areas but still give them a
freedom to do whatever they feel they
need to do that's the sandbox approach
so don't go like next where working uh
you're supposed to test installations
don't go testing the the virus
protection half of your time otherwise
your own area will not be tested that's
the the basic idea the S boxing Charters
they are like big test cases so the idea
is that they are uh about of a size U uh
well a session is about of a size 1 hour
at almost two hours but you can have a
charter that goes into many sessions so
usually uh uh less than a couple of days
of work so it's not a test case it's not
something that you can do hundreds of
every day but it is more like a
collection of test cases a theme of test
cases uh so to
speak uh you can go for more uh like
detail documentation uh some kind of
scripts uh scenarios of of of things
that you're supposed to do but still
explore around them you can have scripts
that have a lot of things that are not
said that's still exploratory somewhat
but not quite in the in the larg end and
if you're doing pure scripted uh you
better have some machine doing it
because because uh uh having that kind
of work done by humans I don't think
it's it's quite the the thing that we're
looking for but the majority of testers
I know in Finland they work with leg
scripts uh and and uh scenarios and then
they do things within the test cases and
more senior testers tend to use more
time on simple simple looking test cases
than the more Junior ones so that's
that's kind of a rule of F that I noce
from from people so there's a lot of of
Dimensions uh why would people then want
to do things this way uh the tester side
that's quite obvious I think much more
fun much more
responsibility flexibility uh respect
from from the results because you can
actually provide results with the time
time so a lot of the the stuff on testi
side that's kind of obvious but the
challenging side to moving more towards
uh exploratory types of of testing is
the manager side and the manager side uh
uh with an expert for testing
actually promises like controllability
reliability value and visibility and in
order to do this the the the traditional
ways of managing counting test cases
they just don't work so we need uh need
something else to provide that
value I draw a picture of of some of the
aspects there's a lot of of of variables
that you can tweak or change in this but
the basic concepts I put put in this
feature uh the on the center of of
things there's somebody who is doing
testing let's called a personal tester
it could be a developer but uh uh that
person has to be looking at the software
trying to find out uh whether it works
as intended or whether there's something
surprising to find out the tester comes
in the morning and leaves in the end of
the day so we do days of work we could
also think in in sessions like two hours
or one hour sessions but I personally
feel that's bit of micromanagement style
if I go into too detail and I like to
build cultures for testers where I
actually would be able to trust them so
that it's okay if I talk to them daily
or twice a week and whenever they meet
me as a t manager
the tester's day of work uh is usually
it starts from thinking of what will I
do today and if I'm assigned a Sandbox
or a vision like I'm supposed to test
installations that's this corner so I
usually actually use a a physical paper
where I put these things because I have
such a bad memory I forget things I even
forget what I was supposed to do today
when somebody comes and runs and asks
can you do this and can you help with
that so it's a good thing for me to
write this down the sandbox is is the
area I'm supposed to work on uh the
current chter is what I was thinking I
will accomplish today if I'm testing
installations maybe it's three different
installations that I list there these
ones I will think I will go through
today or I will have this kind of an
idea so chter what I'm going to try to
accomplish and again it's not there so
that I would actually do exactly that
but it's to remind me that when I notice
that I'm going somewhere with my tests I
notice that hey I'm there
I was supposed to be here and I can
actively decide I want to be here I
don't want to be there and I can then
change my mind but I also realized I
didn't use the time I thought I would
use on these tests so most likely I
didn't cover them in the way I was
supposed to and it helps me not to cheat
myself in I did enough on this because I
used the whole day on this even though I
was running around like
crazy then I'm the side of here uh the D
text box there's three kind of of
symbols the the first symbol uh is is
for bugs I tend to write bugs uh in in
just one sentences while I test as much
as I can instead of going directly into
a bug recording system or running to a
developer telling about the problem
there's two reasons uh one of them is
that isolating the problem actually
takes a lot of time it's away from this
this current chter and the other reason
is that uh putting it in the system and
running around with it or talking to
people with it uh it actually disturbs
other people's flow of whatever they are
doing and if I do that every five
minutes it's really disturbing for the
developers I think it's it's basic
manners to let them work as well so
collecting months collecting questions
that I have for them I think it's basic
manners and and for me I actually need
these tools to have these BAS manners
because I just get so excited about
certain things and I need to actively
remind myself that is this actually
important enough so that I will stop
doing stop the developer from doing
whatever he's doing or will I wait for
the moment when when it's clear that
he's actually uh changing uh uh his
focus on something else and the x is uh
I might mark down ideas that I have on
on on Brillion test cases regression
test cases I might want to put in
Automation in aile teams uh new uh
examples uh from specification by
example type of of things or uh new uh
written down detailed test cases to
remember 15 years from now what the
systems this particular B is supposed to
do because I've learned as a tester that
sometimes I have to work with systems
that are 20 years old and I've been so
thankful to the testers who have
actually written the key examples down
so that I can use them because no other
documentation is anywhere near concrete
enough to actually support with the the
testing of the old uh systems after 20
years the last uh corner here is other
Charters so while I'm testing I'm
focusing on this one I actually do
continuous planning planning on on other
things I might need to use time on so
tomorrow's work uh day after that and
the future work that I need to do the
things I intentionally leave out from
today what I
uh where I have ideas that I need to go
back to the other Charters go into some
kind of a backlog anyone who's working
an agile team probably knows a bit about
backlogs uh the top item is the most
important one and there's probably a cut
line somewhere where the budget is over
where things don't fit in uh in an agile
team I would typically put uh quality
depth type of of uh items on the common
team backlog like I I did just a couple
of days ago things that I actually
haven't tested and we go with risk I put
them on the backlog if they stay there
long enough I take them out and and and
the inventory because I don't want to
build
inventories but it helps to understand
whether it's above the cut line or below
the cut line and and whether it ever
goes above the cut line so cut line so
there's a good uh discussion there so
the different CHS ideas of exploration
go there but reports usually go to bug
reporting with aile teams uh I actually
prefer talking about bugs with
developers and uh the best bugs or
fastest bugs that I get never see a bug
tracking system and I think that's a
really good way of approaching things
fix and
forget but uh if the risk is I forget
nobody fixes then I will put it down in
in a bu reporing system but I I tend to
try to get rid of BU in systems uh if
possible
uh uh to support all of this for the
tested us there's different kinds of
documentation there's session sheets
session sheet is basically notes uh from
a day's work uh there's the things that
I find relevant during the day to write
down uh there's uh uh some kind of
metrics on how many of each of these I
have how many new uh uh ideas for
testing how many how many questions that
sort of things and one of the things
that I I tend to collect uh with the
session sheets or a Bi weekly or weekly
uh uh mechanism is uh where the time
went I don't want to take it in the
session sheet some people uh put it
really detailed um down there but uh I
usually just ask a rough estimate uh by
weekly so there's three categories into
which testing fin may go it might go
into sale getting ready to be tested
learning uh finding uh data that you can
use whatever uh it might go into testing
actually adding coverage going through
new things or it might go into bugs and
whenever you run into a bug it's
actually not just seeing the bug and
quickly reporting it but you're actually
supposed to write a good report that
makes the developers life easier in
understanding what kind of a problem it
is so it doesn't come back to you as
doesn't reproduce I don't know what
you're talking about so it actually
takes time so it helps to know if that
if most of your time goes into uh bugs
or most of your time goes into setup
you're actually not going forward with
coverage because if you don't have time
for the coverage the coverage doesn't go
off so it's a way of of showing showing
the coverage in in export foresting
there's two other kinds of documents
here that I I write down usually talk
about playbooks for me that uh means uh
like a notebook of things that are good
to know when you're playing with this
particular area of software this
particular feature so uh you might write
things down that are tools that are good
to know things that are good to know uh
things that you've learned whatever
questions you have maybe the answers
should go for for future using in the
playbooks uh if they are not uh obvious
uh after the the the answer
and what I create quite often is is
coverage outlines so coverage outline is
typically uh in me for me it's usually
in Excel it typically has uh couple of
Dimensions like for example I have list
of of features or things that we are
supposed to test and I have the
different environments different
browsers on the other side and different
user rights for the browsers and I just
marked down like I'm testing this
particular area for this browser and
it's always a different browser uh in an
aile team within a monthly iteration we
never have time to test everything uh in
this uh within this iteration especially
since we don't have the automation yet
yet in
place uh from the metrics the numbers
here you can do a metric summary quite
nice graphs there's actually pretty nice
tools that actually help you you
automate these kind of
things uh and on the top hand side here
there the management part of of all of
this maybe the tester uh is not the only
tester maybe they have somebody who is
actually helping people find their own
areas or or uh Focus that we have have
next maybe you find it from the list
maybe you need some help but the test
manager's role in this kind of thing
it's like the tester is in control
tester is the
driver and this is the guy supporting
helping uh and and uh trying to help you
grow uh as the the the uh main tool the
proof there is about it's very strong
like questions what did you do since
yesterday what are are you going to do
by tomorrow What's blocking you except
to talk about the things that we've done
the results that we've
provided uh things that block us uh uh
what would you suggest that you would do
next or what have you learned the
priorities and how did you feel using
your time on this was it good use of
time or or
not so debriefing is is usually within
these kind of of questions and there
might be a group of people uh that have
to put together some kind of quality
report the metric summary might give you
some of that but one of the best
mechanisms that I find for Quality
Reporting is simple as that take people
in a room especially an agile collocated
team take them in a room and ask them
two questions uh how do you think what
do you think about po do you know any
problems in this area
uh no problems we don't know of them uh
we know of some problems but we know
that some less quality oriented people
might want to talk about them and and
try to say they should go for future and
yeah we know about problems so we should
actually not waste our time on talking
about them but fixing them so getting
quality visible and the other question
same way is
coverage uh I've touched it I've tested
it I've actually tested it so so uh you
can make it visible I don't know
anything I think quality is good so that
uh message you get pretty much
dismiss and it's one of the most common
ones but making it visible uh in insute
I didn't have a product manager who
would go against a team of 10 people say
we all have used it and we know it's bad
so uh it's much more
concrete uh uh a gr assessment so
there's ways of of managing exp testing
but it starts with giving uh the
responsibility of the actual work to the
testers so a list of the things uh about
tools and test automation even though we
talk about manual testing it's actually
brain engaged
testing and it's only smart to try to
extend your reach with tools so uh
nowadays we talk about exp test
Automation and the idea is that it's
it's automation where some of the
analysis is still done by people but uh
for example it takes out
um uh it takes out uh some of the things
where you don't need to focus on and and
points you in a mass mass of things it
points you towards things where you
actually need to pay attention as a
person and my little example here is
just to remind me remind about the the
testing on uh a pension
calculator uh uh Ser so service that we
did that we run a a large number of of
uh queries uh through that U interface
and and we learned uh based on the large
number of queries that that uh we had
there we learned that there were certain
uh error messages in cases where they
shouldn't exist and we would have never
been able to run that amount of of cases
one by one and checking them in detail
but just getting the uh the theme the
kind of information we might look for
with automation's help it's uh it's a
really good uh good way of doing things
it's not just automation there's plenty
of tools this is for for uh your use for
for future one of my favorite tools is
called rapid reporter it's a noning tool
for export for testing and especially my
favorite since my colleague in Finland
Lucy Drea from altum uh she created this
scanning tool that takes the the files
that rapid reporter uh makes and
automatically creates these numbers of
how much time it you use on set up test
and bug and and makes nice graphs of of
those so it makes my life a lot easier
not using the paper to anymore we're
actually going with the
rapidor and and and automating some that
stuff as
well uh there's also other kinds of
tools tools that help you tweak your
memory or help you uh uh identify new
things or things that you try uh one of
my favorite things is is a cheat sheet
uh by Elizabeth Hendrickson it's two
pages of of uh say testing wisdom
distilled uh in a document saying these
are things you should try these are
things you should remember uh like for
example uh one of my absolute favorites
is a fistic called crud create read
update and delete if you can create some
kind of thing with your system you
should you should do it a couple of
times quite many times probably but you
should also update it delete it uh go
check it from different places and
that's quite often where the the bugs
hide So within this creation and
updating life cycles so it's a really
nice uh document and there's longer
versions are also available available
but I think this a good starting
point the other Tool uh is the
Dynamics export testing Dynamics so uh
you should learn to split your testing
process the way that you think about
testing in a way that supports uh the
freedom and and the responsibility in
exploratory testing the work products
most likely will look different there's
an list of of the types of work products
that uh exporter testers would typically
consider uh you should need to think in
polarities big small hot cold all that
sort of things so there's plenty of of
these for for software so so go into
different sides of it uh don't just look
from one angle or many angles the list
is really long long in the article
that's that's referenced there you need
to uh start to recogniz your skills and
actively develop your skills recognizing
which bus are relevant uh is is one of
the skills but there's plenty more and
the test strategy understanding what
kind of options we have in the projects
to choose from uh to know which ideas
actually guide our test design that's
what you would also need so all these
are tools for for making your most
important to your mind a bit more sharp
for the the purposes of testing
on the skills side I think
self-management is one of the the core
skills uh in an explor or tester so if
you uh as personality would be like me
who's easily forgetting things and
sometimes a bit
sloppy uh it's a long road and it might
require putting things on paper uh you
need to learn to think in in many
Dimension develop ideas that you could
use or you can
discard but uh instead of using all the
ideas you have you use the best ideas
you have that's the the goal and skills
and you need to be more efficient uh in
in uh using the products in ways that
help you uncover the the
problems so we're towards the end of the
uh presentation part we continue with
the
discussions I think uh exploratory
testing uh fits quite
in different kinds of projects in
different kinds of organizations uh I
have plenty of case studies from for
example from insurance sector pension
insurance which is really uh detail
oriented really document oriented and
they still wanted to turn towards expor
testing actually providing better
results uh there so the strong points we
already talked about Ring new
information and finding bu at the bucks
at a cheaper rate but the blind spots uh
I feel the blind spots uh the biggest
ones that we usually mention are are
misconceptions uh like uh uh it doesn't
allow us to do any documentation
beforehand uh I was working for the
insurance sector we had acceptance
testing in the end 30 days in the end
for one uh test uh uh data that we would
start a test days from on average took
us two mandates of effort to find the
right kind of person to using that
scenario and we need about 200 of them
if you would try to do all that work uh
during the 30 days of of test
execution we would not test we would be
looking for the data so expiratory
testing is not saying be stupid and do
it this way it's actually saying uh if
there's preparation that you should and
you can do maybe you should do it so we
actually collected the data but we left
the details of what we are looking for
within that data we leave that more open
open there so it requires a time frame
time frame for learning but I think uh
actually test case based testing might
also require that that uh uh if you have
uh somebody working on an area where
there's nobody else it's limited by that
person but the same is with test case
based testing
what you know to look for when you know
to keep your eyes open same time fix
there and if you're really sloppy and
you're not willing to start learning to
to control uh your own actions of it EV
uh and and start learning the self
management
skills uh that's a a weak point again uh
and what I draw in the daytime session
is is
that uh I I think of things so that
like there's people who
are
unwilling and there's people who are
willing the people who don't want to do
anything they don't do anything even
with test case
bases they just Mark and done and they
close their eyes completely and they are
always right saying this didn't say I
needed to
that the other dimension that we have is
uncapable versus
cable if you don't know how to test if
you don't have any skills that help you
recognize a problem in we you calling
them oral testing uh you need to learn
that you need to develop the
capabilities if you have a team member
in natural team for example happens to
be here unwilling and
unable it's it's sad but what you do
with that person is you micromanage that
person until you get him or her to
be willing uh first willing and with
Will being willing then pay the
all uh but uh within an natural team you
should actually uh actively change your
management style from
micromanagement to this this uh
typical self organized team uh types of
approaches but uh first you have to get
rid of the people uh people's uh
unwillingness and it usually goes from
talking to people so it's not like kick
them out that's not the resolution I'm
suggesting but find out why they don't
want to do the things the way they they
are doing so that's the idea
so we're at the end put a job there so
taking things on
clear it's time for discussion questions
anything that might uh interest you in
this where
is First several several many slides ago
actually um there was a perspective of
testers and managers
yeah as a manager I'd like to add to
tester
side the close of
responsibility the sense of
responsibility the fact of more
sensibility TR again somebody could
really with best cases somebody could
really get away just executing them and
not thinking much yeah well I kind of
think it just part of the
professionals if you're not responsible
you're not really
professional but um I think there's many
of things that you actually
could I think you're right it definitely
deserves place in the in the in that
other comments
I for the same reason the professional
or just executing the test maybe the
same what you told and what Michael
Bolton told about checking a testing so
if you keep test then you you checking
out but also uh there's a lot of testers
who use test cases but they take some
extra time on testing those test cases
so they actually when they're told to
press a button they press it twice uh
when they're told to press a button they
press another button which says
backwards or whatever and uh they are
actually not even though the test case
might appear as as a check they are not
actually doing it that way I had a
colleague at here uh uh who made a
really big impression on on managers
because he was so fast he was testing
installations he was so fast and we were
wondering what's happening with us like
the more senior ones more longer in the
company what was happening with us being
slower than he
was and what we did is We Gather people
together uh next to White and we started
making notes of of the ideas things that
you need to monitor after installation
so that you know it completes and the
only idea that he had for monitoring was
that it doesn't show an error
message uh it says installation complete
he didn't actually even uh reboot the
machine to see if it works after that so
of course he was much faster than those
who would actually go check that all the
components were in place and they
actually work after the installation uh
that all of the things in the registry
were in place and all that sort of
things so so uh it gets really uh
difficult uh if you have to give all of
this advice
brighting but it's it's a really easy
thing to do is is to take somebody who
you notice the pay it's it's not quite
be the same as with others and and go
through that particular case with with
that person and teach him the skills of
of looking in a bit more directions or
bit more
Dimensions make your resp because this
Cas is just easy you have new
with expor t or you just do it without
any or
use I usually
use a short amount of time like in
traditional projects few days typically
to create some kind of a a starting
backlog of ideas that we have so I don't
go into as much detail as with the
traditional testing do you use use cases
user story no I usually don't use use
cas Cas more like I can actually show
you from data I would like to extend the
question maybe how do you manage backlog
um I'm all for exploratory style testing
but um for example simple questions how
many testers our project need is this
style of testing how can I substantiate
The Climb I need for example two I need
one less now and one one more after
three months yeah and they don't come to
you the new people they don't come to
you you say I need them by tomorrow you
have to actually tell them beforeand
especially if they come from outside the
organization you need to hire someone uh
I think of those parts uh like the
longterm things I think of them there's
usually two things that you need to
think in advance and
plan uh even in AAL projects especially
bigger
organizations uh uh tested violence if
they cost1 million it takes three years
to get one mil that was something I
learned in the insurance sector but even
if they cost only
€2,000 ordering them takes three months
so you need to start thinking about what
test environments you need you need to
start thinking on time uh because it
actually takes calendar time before you
have it ready and set up and delivered
for your use and the other thing which I
find similar which takes long time is
new
people so you need to think uh
especially in aile you need to think of
not the amount of testers but the the
size of the team and they share the work
but when you try to find out how many
testers do I need what you usually do is
you create some kind of a backlog some
kind of a list of of things that you
probably would need to test you would
probably put there some kind of sizes
that you might need you would go that
through with somebody do these seem like
things we would need to use time on uh
and you would come up with a guess of of
how many people do we actually need and
it's uh quite much actually the same the
problem with the test case based
approach that you actually don't know
how many testers exactly you need at
least I have had to go through this
discussion will I need two or more or
whatever number I need in in the
traditional side are just the same but
only with expor style of testing I've
actually given away some of the testers
that have been allocated
by learning that some of the risks we
considered are actually not going to
realize and we don't need as much
resources and it was within an
organization where we would actually
sell those people then to customers and
there was a direct Financial impact of
of of that ability so sometimes I'm
right sometimes I'm wrong when I'm
guessing I need two people but the
challenge is I usually get to know the
manager who decides whether I get them
or not uh I usually they have a lab in
their forehead some of them says say
four and you get two some say ask two
you get two and some say talk for two
days and you get two so uh I usually
learn to to the style of that manager
and whatever I ask uh I have some kind
of a list some kind of
destination on on how much time have you
we used before how big are the changes
and my main Mo of fun is is how many
Developers we have how much development
are we going to do and also what's their
take on on how much testing will they
cover versus how much will they leave on
the the testing side of
of but I think it's well easier in a an
aile team and a bit more difficult in a
in a a team where we do expr testing
within the testing
team do you have other kind of
experiences on on uh how do you do the
planning for
effort uh
currently for example last year last two
years we
actually share in our in our AG team the
analyst also perform the testing they
are more like business people and they
are more like more like to understand on
a large scale how it should work and so
we don't have dedicated testers for
example but
but it's kind of like my current teams
uh for two years they've been uh with
the product in production they didn't
have a tester they tested whatever they
could themselves and then they were
these kind of analyst type of people
business people who would test what they
could uh on side of other things but
they had the so-called responsibility to
accept but you can accept by saying I
trust you I have no choice or you can
accept by I don't trust you I will test
everything and there was a huge gap in
between this and the reason why they
hired me as the first test there was
that the the it was clear that neither
one of the sides had enough effort to
use that H they knew one person for two
teams wasn't enough but one person for
two teams is is much more than zero
persons for two teams and now they're
hiring another one next year H I'm the
one saying actually we have this this
long list of bugs that need to be fixed
maybe you should consider hiring a bug
fixer because you don't need another
tester you can't even handle the reports
I'm
producing but uh it's still an ongoing
discussion on on which way we will go
but the the the business side of it is
still that they have a limited amount of
money to go into
people and and you should make a
balanced choice on what kind of a person
you need and the testers they don't
don't fix the box but neither do the
developers if they have know of them so
that's that's the kind of the rough uh
thing uh that
there other questions
ideas about psychology
of uh mostly about oh T he found the
back by
yeah uh I think uh that uh putting a
face for the tester and putting a face
for the developer helps a lot with the
the
adverse uh approach and I think uh
whoever is is taking her or his career
as tester actually needs to uh consider
the the other person's feelings as well
if as a tester you're supposed to
deliver the message your baby is ugly
maybe you want to do that uh in a polite
uh respectful uh way and and not go uh
laughing about it too
much uh when I work at at uh at the
computer in my own cubicle uh I quite
often laugh out loud when I find a
really good
luck and uh one of the things I did
right in the beginning is I before I
even did that I I apologized to my my
developer colleagues say I don't laugh
at you I laugh at the the the feeling of
success that I get from from being able
to understand or learn how uh these kind
of things might happen and there's been
a couple of occasions when I thought my
my developer colleagues that that uh uh
I can't imagine you programming or
creating this blug that can be done
intentions too creative no one can do
that and I was thanking them for giving
me the experience of seeing those and
they have thanked me for finding
things uh uh within hours or within
days from when when they find them so I
find part of the the adval relationship
it comes from the fact that if you test
two weeks later that the developer
developed he's already doing something
else and what's worse then like somebody
comes and tells you stop doing the new
thing that you're doing and now re to my
feedback I'm so important it's it's it's
it's not a good way of of telling that
that kind of message so we should really
do a lot of work into making feedback
loops shorter and for example one of the
the Practical rules of Thun that I use
is is uh whenever I get a bu back uh
fixed bu back from developer for
confirming if the fix has been done I I
immediately categorize them into two
categories the things that are are are
so simple that the developers actually
do know how to take care of them
themselves and I leave them on the list
those kind things I leave them on the
list until the project manager
completes but the ones where there's uh
uncertainty unclarity uh dependencies
and
risks I actually go many times a day to
see the problems that come back to me
and if possible that I know them you've
done it now I will test it wi away so I
actively look for the opportunity to
make a feedback gr uh as short as
possible and it requires me to leave
other things undone even though a
project manager in my team might
actually think they are the most
important thing that should happen so
that he can see the progress everything
is Clos now so we're kind of in between
this more of an agile type of thing and
and he really a more of a traditional
guy except he wants to be was one
I got this also uh what we do in these
Cas is to
to not make in situation when t comes to
developer and
says you to back here first of all he
can't usually come to developer because
he sits near the developer so it it
makes the communication faster and
easier and
second he doesn't find the b in somebody
his El product find about his product so
he's part of the team Who develops a
product so uh his um job is not to find
a bu and report it his job is to make
the
product working working without bux and
uh working for the customer so he's
interested in all the all the pictur
yeah uh but not all people are quite as
agile did as you would like an A
Team uh uh one of my my team mates uh
when we first met and we tested together
one of the developers he told me that
he's too valuable to do testing that was
his first comment to me I think uh since
I was a new person to him he wanted to
challenge me as well but uh what we
talked about is is uh again an advice I
got from Michael bolon we talked about
the fact that if a taxi driver can't
find the location where you're supposed
to take the customer if your taxi driver
can't find the location takes you to
wrong location that's actually a
worthless Taxi Driver if you need the
map reader next to you and the value is
actually within the map reader so uh
there should be a good like
collaboration uh in all of this and and
thinking of the business people he
wasn't actually talking about me as the
L valuable person but he was talking
about business people in uh our
organization uh they may get less salary
some of them at least uh but uh uh they
are supposed to sell the product and
there the way I think of course is that
there's an opportunity cost when they
are testing to find the problems that
somebody else thinks is too valuable for
they are not doing the other work they
could do which is sell more of the
product and bringing money for for the
company and the same opportunity course
type of thinking is is what I use in
Expos testing for creating test
documentation and that's I think a
really good way of thinking about things
seeing the bigger picture so don't
optimize testing optimize the overall
thing product uh is there something in
particular you dislike about U
developing software why you told us you
like the testing better but uh
um what about development actually
there's nothing I I would really hate in
development one of the reasons that I
don't do it much is that there's only 40
hours a week and there's so much to do
in testing that I don't have enough time
on go
inside uh the other thing is that since
it's been a while since I last programed
I know it would take me a while to
actually get started get all the tools
installed and all that sort of things so
that's another
thing uh but there's uh within
development there's nothing that I would
dislike or or think it's it's it's
something I I don't ever ever ever want
to do but I've used a lot of my my
career uh with the thought that I don't
have enough time at my hands there's
things I would like to do I would like
to go to places I would like to talk to
people I would like to do testing and
spend more time with my family and all
these things and there's never enough
time for all of this and it would be
really nice if there would be these
super humans who can do all of the
things and ruly remember all of these
but whenever I go and do some
development uh it's time away from from
the testing side and I feel there's
still so much to do on that side so it's
just a choice of of of where I want to
invest my time on what I want to learn
how you share your uh what you learn
with others you each you do your T and
afterwards you share us some how these
Lessons
Learned uh within our team uh when I
test the the the result that they
usually see is the bugs that they need
to fix and then we have weekly meetings
where we
talk uh but the first idea that I had
when he said how you share your your
your uh lessons is is the other things
that I learned while I
test and this is an example of of how I
share it I share it with my team in in
case studies I share it with my
community to learn if I did wrong and
this particular one is a case study
about uh wasteful test documentation in
my current
team basically saying their existing
test cases where 46 simple test cases 39
pages in one area and there were three
things that were not blatantly obvious
for me from from first
reading and there was a huge number of
things that actually needed testing that
wasn't covered in the
documentation so what I did is I created
a mind map I used different kinds of
tools and uh with the team we agreed on
this quality assurance goal for us like
what kind of activities we promise each
other we will do now so uh some people
would call these retrospectives but I do
them whenever I feel there's a lesson
that that I have realized and in my past
organizations I haven't been the only
one doing this but it's actually anyone
in the team when they get an idea we
take time and we go through those those
ideas and I think part of this comes
from community building and you're
actually trying to build a community
here so uh I would actually advise you
to use the power of community and and
take your place in sharing some story
that you have don't be afraid of of
somebody telling I would do it
completely differently because you're
the one who actually did it you were the
one who made your choices and the others
feedback might actually help you become
better at that and that's actually the
mechanism of how I've learned mostly
about testing
I talk to my team members uh I talk to
other people in the company I talk to
other testers outside the company uh I
talk to Agile Community a lot and I find
people who are smarter than me who will
teach me how wrong I was and there's a
couple of things I remember that i' I've
learned one of the things is I I didn't
believe in continuous integration and I
should uh really
apologize to uh one fellow in Finland
actually I have apologized that I was so
strong against it when he was trying to
explain to me it took me two years
before it sank in and another thing I
learned that I recognized I actually had
learned from from the materials that I
have created over the years is is that
uh I would not give the same kind of
test case examples anymore for anyone
that I did when I when I taught at Hing
University of Technology so I needed to
apologize hundreds of people for for
teing them wrong things about testing so
again uh you don't you never know all of
it you talk about things you think you
know right now and you can only be
thankful to others when they point out
the CLA in your logic and that's I think
that's the power of community and you're
doing a good job on building one
here so everyone is going to do a
presentation next
yeah okay more questions on this
presentation you had you had few pages
where there was lots of text with those
tools and so on so yeah how do we get
that
information uh I actually send it to
the yeah so he has it and he should
publish it and it's a creative Commerce
license so if you feel like using any
part of it just take whatever slide or
half slide as it's attribution saying uh
you should mention uh that it's based on
on somehow on my materials but I'm
actually never coming after anyone even
though they forget to mention my name my
name is too difficult for most people
so
so thank you my idea I like I've been
working on community building for quite
some time uh and I'm changing jobs every
3 years my idea is that the best way to
keep uh materials that are useful for me
best way to keep them safe is to make
them public so then they're available to
me as well so you can Google them up
yeah I Google them up if anyone feels
like and when it's always clear for my
employers that they are licens in this
this same license uh I can have the
discussions on what I can disclose or
not before I disclose it and then it's
it's usable so it's an approach I've
learned
so uh I had a I have a question about
how to
find places there
to uh check for bugs for because
uh almost half code made is generated
automatically the Frameworks and uh so
it's mostly
bu I think one of the best ways to find
the places uh is to talk with the
developers but still uh use your own
judgment on on uh how you interpret what
you learn by talking to the developers
so I tend to use a combination of these
these like cheat sheets and checklists
and and and list of things that I that
help me remember all the
dimensions but the first thing I still
do in a project is talk to the
developer uh the developers should tell
me that there's nothing to test and
usually test their things first to teach
them there is something to
test uh and then they learn uh to
actually tell me the the answer they
they can tell me instead of the answer
which actually say go
away uh so uh at least I feel I I've
managed to build quite good
relationships with the developers and
theyve learn on what kind of things I
find relevant so I go around and ask I
talk to the product owners product
managers and I talk to the
developers and when they disagree I know
I like
test most technical approach would
probably be that you just look at the
Version Control System look at the last
checkins and then just uh try to assess
what would be the impact and then just
or you could have a release notes
automatically generated from the the
comments that people put on on on check
and you can see from those for example
in ex we have this mechanism where
basically you would get continuous
integration you would get builds
throughout the day and and you basically
get a different from last time I checked
it was this day and now it's that day
and you can see all of the comments in
certain uh way way of of organizing them
so that was really handy but of course
you could also look at the code but I uh
uh quite often still tend to prefer to
look at the the intention which I can't
see from the code I can see the
implementation but I can't see the
intention so I I look for the
intention
implementation look to much
implementation forget the actually use
this software aren't testing like too
much maybe we are find user will never
find never
use but
you uh I had long
discussions with some of my colleagues
about uh testers reading code and
testers looking at code and uh we
basically had two camps uh of of of of
thought in this there were people who
thought that testers uh actually lose
sight of of what's important to the
users they go to close to the the
software the program the Bood uh and
then there were people who were saying
nothing stops you uh from actually
taking a day where you actually think of
the user but still care for the other
like knowing about the details doesn't
mean you have to focus on the details
it's just information that you can
use and I think it's an endless
discussion people will always disagree
uh I had some people who when they
looked at code uh they wanted to fix all
of the problems that they they they
found and uh it's not a bad thing it's
actually a good thing that they they
wanted to fix that they would help the
team by fixing them but uh if somebody
else from the team wouldn't help it
Investing For in the information that we
need by testing he would actually just
take away the investment of information
and move it to the B fixing side and it
might be okay if you do it
intentionally but uh uh within this
particular case uh I I felt uh he said
he he tested what he's supposed to but
he never used enough time to actually go
as as deep as he as he need it but
actually after a couple of years he
actually began a developer because it
was quite clear that that that was kind
his
interest but I feel all of this is about
where you use your time and how you
manage your time and how you choose way
you invest it so so it's again the same
thing uh same thing on
on
previously I think it also depends on
two things clients intelligence level
and their tolerance for the client is D
then basically you should make the sof
full if he D tolerant then you make it
fullprof but you don't care for the more
complicated cases or or for simple like
typos simple like typos so if he's d
dumb and intolerable so he wants full
quality then then it's the worst case
scenario so it has to be completely
foolproof and no visible errors any so
it's you need to assess from the
client's perspective because they will
accept at end and usually they accept
and then you get the money yeah you that
project I'm currently working with with
software that goes directly to end
users I don't have right now I don't
have a a like a c contract customer
relationship I I have that de
money and and like setting the the level
of quality that you expect especially if
you have fixed price then the customers
tend to just raise the bar if they can
and the contractors try to cope hey we
have only this amount of our you can
raise the bar so you need to learn ways
of setting the bar early on with the
customer and they will still change them
on but actually you might want to
protect yourself in some way that
so it takes a lot of energy uh in
traditional projects when you you go
into this argument is it a bug or is it
a a change
request uh but with agile if you have a
hour based contract with a contractor uh
then actually raising the bar just means
you need more schedule you need more
effort
so it's a bit different
there uh what about this this uh what
the customer wants it's not only uh
about what the customer wants but it's
also that different uh areas of of of of
products or software is is completely
different if you imagine radiation uh
treatment and and the software that
controls that it's quite different from
uh uh let's make
a web shop that sells kiss clothes to
anyone who had a spender and it's
probably going to be 100 off or whatever
people who who come this new one that I
just personally built so it's it's quite
different but I feel uh looking for my
colleagues who work with the safety PR
all type of of of things I feel that uh
I'm happy that they are doing
exploratory testing because I'm much
less likely to suffer from the problems
in real life if somebody is actually
trying to consider the real life
scenarios uh thoroughly and in
documented way and I mentioned daytime
here that if you need detailed
documentation from exory testing video
tap is an
option uh a good way of of of
videotaping is is to put this as the
side note the text texting you put
what's your intention because you can't
see that or you would talk out loud or
whatever type of things so so put things
together and and and find a way of of
classifying and tagging the
videos so that you can put certain
videos in a certain box so if somebody
wants to actually see what you did
there's no more detailed proof than than
checking the video or or and the the
notes that you make or testing together
