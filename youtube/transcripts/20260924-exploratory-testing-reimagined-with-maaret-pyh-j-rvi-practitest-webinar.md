---
title: "Exploratory Testing Reimagined with Maaret Pyhäjärvi | PractiTest Webinar"
video_id: BULFWhYG-LM
url: https://www.youtube.com/watch?v=BULFWhYG-LM
upload_date: 20260924
duration: 48:55
channel: PractiTest | Intelligent Test Management
tags: []
---

# Exploratory Testing Reimagined with Maaret Pyhäjärvi | PractiTest Webinar

> Traditional testing often relies on scripted test cases—which can act as step-by-step instructions on how to miss bugs. In the age of AI and agentic testing, the role of the tester is evolving rapidly from simple verification to deep, judgment-driven exploration.
> 
> In this session, Maaret Pyhäjärvi shares groundbreaking benchmark insights on task expansion, human-AI collaboration, and modern exploratory testing. Discover how combining human expertise with AI tools yields dramatically higher bug discovery rates and redefines quality engineering.
> 
> Key Takeaways:
> - The AI + Human Performance Advantage: Why exploratory testers paired with AI dramatically outperform traditional testing approaches and standalone AI agents in discovering critical issues.
> - Task Expansion in Testing: How testers are moving beyond basic bug reporting to starting earlier in code reviews and continuing further by submitting fixes.
> - Agentic Testing in Practice: How AI agents handle UI, accessibility, and regression checks while humans provide essential epistemic judgment and imagination.
> - Contemporary Exploratory Practices: Why test cases should be captured as the programmatic output of exploring rather than the input.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

Hello everyone and welcome to Practice
Test Guest webinar uh series after a
short summer break. I hope everyone had
a pleasant summer or winter if you're in
Australia and you're watching the
recording. Um but we are very happy to
be back uh and not just to be back to be
back with uh a very special session for
us or very by the way important in those
times um of everything AI. So we're
going to have first of all we're going
to have a session that's not just about
AI but probably we'll mention that I
will wait and see. Uh so today's session
uh is titled exploratory testing
reimagined and it will be um given or
presented by Maret which I can't
pronounce her last name uh but we agree
that everyone knows her uh for who she
is but I'm going to steal two minutes of
attention of your attention before I
introduce her fully uh and hand over to
her for the session that you've joined
to here uh and do and do introduce
practice to those of you who are not
familiar with who we are. So I'll start
with introducing myself which I've
actually skipped. Uh my name is Noah.
I'm leading the marketing team here at
Practi Test. Um Practest
done. Okay. Uh is a QA is a test
management and a QA intelligent platform
uh with a new vision of turning data
into intelligence. And the idea in our
new vision now uh talks about that we
want to go beyond testing execution
which was done perhaps what testing was
done perhaps five or 10 years ago into
uh transform it into actual business uh
answers and in that uh and this is we
have a test management platform we work
with multiple enterprise organizations
across the globe. Uh so we support as in
order to do that we support every
required security and privacy regulation
the legal requirements the commercial
support everything that is needed um in
to support this in order to give some
sample for those of you who are not
familiar with us uh but would like to
have some social proofing uh so you can
see a subsample of our customers here on
the slide um
across any technology any industry and
around the globe. One thing that I love
about this slide is that for me when I
first joined the company and I wasn't a
tester I expected the customers to come
mostly from ISV organizations because I
thought okay if you develop software
then you need a QA QA and a test
management platform but in reality
nowadays I think everyone on this call
understand that any organization
nowadays needs a test management and
needs quality uh in its essence okay for
its software and essentially any large
organ organization nowadays is a
software organization even if it sells
health services, games, cars and so on.
Uh so I love this slide because it's
just showing how broad uh and and how
vast the industry really is with what
where people can work and what they can
actually find themselves dealing with on
their day-to-day job. Uh which is very
somewhat exciting. Uh and the last but
not least but still wanted to show uh is
that we have conducted uh actually we
have asked Forester consulting uh to
conduct an independent research which is
called the total economic impact about
the impact of working with practice
numbers here on the slide for those of
you who are more of the number type of
people than the logos. Uh so we shown
300 312%
of ROI within 3 years 2.4 4 million
total benefits and a payback period of
less than six months. So this is it for
the marketing part of things and now I'm
going to hand over to Maret. But does do
I need to introduce Maret? Maybe I will
say one word because still I'm a
marketer. I can't say her last name but
I can say something about herself. Uh so
if you're not familiar with who she is
and she will perhaps would like to add
more after. Uh but she is a renown. I
think that for many people when you
think about exploratory testing you
think about Maret uh almost sin in some
cases. Um also working hold on good. So
you introduce this also working as a
director in testing services at CGI
renown um
very frequently keynote speaker in
conferences. Um I think you're also the
chair of right of the latest Euro Star
if I'm not mistaken or no I'm imagining
but that's also
>> no not yet maybe I'm maybe I'm
envisioning uh but what she definitely
is has been renowned selected as the top
100 most influential in ICT in Finland
between the years 2019 and 2025. So this
is also answering where she's from and I
think that this is just around the time
to hand over to you. Thank you all. Uh
one sorry be one last thing that I do
want to mention housekeeping. This
session is being recorded in case you
have to drop. Uh we will share the
recording
probably tomorrow if not later this
week. If you have any questions, please
type them in the Q&A uh so Maret can
answer them and address them at the
later on in our session. Uh and that's
about it. Now I'm actually handing over
to you.
I've been trying to figure out
exploratory testing for pretty much my
entire career, which is about 30 years.
I realize exploratory testing is already
40 years old. I just checked the dates
on on when had I said that it turned 35
now. So, it's it's more than that. Now,
it's 40. Uh, and yet it seems to be one
of those things we don't quite
understand what we talk about when when
we talk about testing.
Uh I called this talk uh exploratory
testing re-imagined uh because I used to
call the the understanding that I was
trying to build in exploratory testing.
I used to call it contemporary because
there's clearly something that is
old-fashioned way of looking at
exploratory testing. But uh it felt like
even the contemporary is is now a little
outdated. So I needed to to update the
the title because uh if you look at
things today uh exploratory testing in
the age of AI it is more important than
it has ever been and it is no longer
this kind of like a technique that you
lay on top of all the other testing.
It's no longer the technique that only
testers apply, but it is actually the
central concept on how we look at things
when we're building software with the
help of AI. Now that we are, you know,
passing some of that control over to
something else, which is a machine in
some way, uh we're actually required to
explore even more. and we are uh on the
joyous journey of of sharing all of this
with all the different roles inside
software development. So this is not a
tester thing anymore. This is kind of
like something for for everyone and for
testers in particular, it's an expansion
of talent. So when we talk about
testing, I kind of like to want to have
a bit of a baseline on on what are we
really talking about. So I I believe
testing is is search for information
that matters and and all testing by its
nature is exploratory and again if we
kind of think of like we look at at the
system and we search for information
that matters anything that we don't yet
know that is actually what matters. It
might be that we knew it yesterday and
we don't know it today because we
changed something in between kind of
like a regression perspective into into
the the changes. It could be that we
never knew it in the first place. We are
building something unique and new like
we what we mean by by doing projects.
All of them are are new and unique. But
we're searching for information that
matters and and sometimes we also find
information that just doesn't matter. So
I think of it kind of like you know if
if you have a picture like it's kind of
like scratching that picture open.
There's an exercise called raster reveal
uh by uh work room productions which is
James Lindseay uh by his by his real
name uh where uh you know you have that
picture this is a picture I took
actually a screenshot of a picture that
he has created and it looks kind of
blackish uh but more towards very dark
gray in in the beginning and when we
start testing meaning scratching the
picture open we start revealing that
information we didn't yet have well we
can see that you know there's something
in that picture so you can see my test
strategy for this picture I chose it
very deliberately uh I chose it so that
that I would focus on the the top left
corner and I've been scratching there
like crazy I've been doing so much
testing but we have no clue uh from the
testing that I did on the information
that that picture would reveal if I
would have done you know the same time
uh on some different places, we would
probably know more. And this is what we
do in testing. We have to choose the the
attention and share the attention over
over time. I could tell you that there's
a dog in the picture. Uh and you could
think of kind of like is is this now
then the the way that you would uh uh
test it or or reveal the picture. Uh I
could also claim that it's it's an you
know it's not an animal at all. I could
say uh there's actually a a white
minivan in that picture. And based on
what I now show you, I would claim you
have no clue based on that specification
whether that's true or not. So again,
you need to search for more information.
That's how testing works. So we would
scratch a little bit more, you know,
like doing a bit more uh kind of like a
an overall pass on on on the the target
that we're looking at. And uh probably
at this point you feel like it's not a
white minivan. It it cannot be a white
minivan. And and at this point of of the
picture, you probably already have an
idea that, you know, I I I have have a
strong feeling that I know what's in the
picture because again, I tried to kind
of like reveal just enough so that we
would get to that that idea. So I would
probably think it's an animal of some
sort. It probably has, you know, four
legs maybe, you know, two pairs of legs
there. Uh I can imagine all kinds of
things. I could call it, you know, done.
I could just say, uh this is a a
unicorn. uh and you know all done. I I
could you know stop testing. It would be
bad testing but it is still testing and
it's very much exploratory by nature
because I can make new choices on how I
reveal the details of of the information
that we are looking for. So I made a a
detailed choice and and I made obviously
the choice of of you know the the bottom
end of of this. So, if I claimed it's a
unicorn, you don't know if it's a
unicorn based on what I revealed, but
you might have an idea that it is in the
neighborhood of of some animals and and
well, it could be a white horse. It
could be a unicorn. We don't really
know. There's all kinds of, you know,
lovely colors and lightsy there in the
background. We don't really know exactly
what comes out of that. So, we can make
it uh more clear. It looks like a horse
or a unicorn. it uh still gets more uh
detailed, more detailed and more
detailed uh when I go for the original
source. And by the time I see that the
original source is called running white
horse, that is actually only the moment
when I know it is absolutely not a
unicorn like those are ears, not a horn
on top of a a a uh imaginary
uh picture of some sort. So again, if
the specification gives us ideas on on
what it's supposed to be, we can jump to
conclusions and and we have to dig in
deeper for the information that matters.
This is basically what we do. And this
is why I think all testing is is framed
in this idea of exploring because we
need to avoid being confidently
incorrect in our judgment and and and
it's very easy to to do that. So, uh,
for us as, you know, someone who
usually, uh, wants to look at things
this way and and reveal that
information, uh, I've been then doing
research on on what does it actually
look like when we're trying to do this,
not on pictures of unicorns or horses,
but on, you know, tiny little
applications or larger applications. So,
I've been doing benchmarking. Uh there's
a to-do list application
which is basically a group of developers
got together to create a showcase for
front-end development. They did their
best job possible uh on creating a a
to-do list app according to the
specifications that were commonly agreed
in probably like 20 30 different
front-end frameworks and languages. So
there's a lot of different
implementations of this particular
problem available by developers who want
to showcase the best work that they can
do in front end. That was the the
framing. So I took the the to-do list
and I used as a benchmarking thing kind
of like you know when we are asked then
to scratch reveal that information from
a real application how are we doing? So
I discovered uh that the highest number
of of bugs in in two different versions
uh of this that we usually give as an
example uh was 73 problems that you can
find in in those those uh applications.
Uh as an exploratory tester uh I uh
first uh said that the the level of of
what I could find there was 62 uh% of uh
the 73. uh when I then added AI and and
guided AI, I got to 55% in a different
uh session. I made uh 57 colleagues in
the the community uh do this exercise. I
learned that they can find on average
about 13 and a half of the 73 problems,
meaning 18% of the problems. uh if I ask
playright agents to test this for me uh
16% so just barely under what is is is a
a larger group sample of of how well
testers are able to reveal these results
so just barely under that and again if
you ask uh by insisting more there must
be more tell me more it already goes
above the the level of of what people
can usually see see in in this kind of
an application
uh future Future talents are new people
coming into the industry. So uh very
small difference with 20 years of
experience in between in in results and
uh well uh the the kind of simplest
let's leave just AI trying to do this
with a a very simple no particular
instructions prompt uh four problems 5%
of of these. So uh to a degree I I've
kind of learned with this this
benchmarking uh that uh well first of
all we don't know usually how to test as
well as we think. We call ourselves as
an industry uh we often call call
ourselves testers or QA but we are so
focused on either test cases or the
requirements that if someone didn't give
us the right answers they didn't already
tell whether it's a horse or a unicorn
that we're expecting to see. We are not
able to reveal that. And the essential
part of exploratory testing at least to
me is that if that information is
relevant even if it wasn't given to us
as a ready thing we might actually have
to go and and look for it. So [snorts]
things are often kind of written in
invisible ink uh and it's our job when
we are exploring no matter what role we
are exploring from to reveal that
invisible ink make those problems
visible. And most applications I don't
have a listing of 73 problems that I
know of in this one so that I could
compare against it. We learn from
production and usually over maybe
multiple months or even years before all
of those problems kind of reveal
themselves and and and we can come to
the the understanding of of did we do
well or not or well enough in in
testing. So I've been at this problem of
benchmarking kind of you know like I I
would like us to be able to do better
while we are exploring. I've been at
this for probably something close to 20
years now. And I find it it kind of a
fascinating problem because when I've
been teaching in classrooms, I've I've
learned that these are very teachable
skills like teaching what kind of
categories of problems there are.
Teaching how to observe, how to play
with the inputs, uh what are the
different options, how do you kind of
consider all kinds of variables. You can
see uh I I I think it's a very teachable
thing, but we don't really teach it in
the in the testing industry. So one of
the things I've now uh recently
introduced is is trying to scale this
from uh me teaching it to a few people
at a time to something that you can
teach yourself uh after this session and
try out kind of how well you do with a
ridiculously small application but it is
still an application with a domain and
you have to think about the domain to
understand what in in what information
is actually really important in that
application. uh on the right hand side
here uh there's some hints that you can
get kind of the hint of of uh on the the
uh f on the uh text box here there are
42 essentially different kinds of inputs
that you might want to try so that you
can even find the pro uh the problems
and there's actually on this particular
application there's 72 bucks that I know
of across 19 different categories and
only 24 of them I consider relevant so
there's a lot of noise also in this
particular application. So this
application is not one of those you know
developers were supposed to be you know
happy and proud of this. This is a
testing target for testing teaching. So
it has kind of like you know some of the
easy things to find. But sometimes
having many problems to find makes
things even more difficult. So it's
essential actually in the kind of going
forward ways of of of thinking about
testing uh that we start fixing some of
these problems because we're not able to
see all of the problems before we have
fixed some of the the current ones. I
included here some numbers from the most
recent teaching session that I have done
uh with this application. I had 10 pairs
of developers not testers developers
testing this application.
uh when we prompted together AI to to
report us the problems on this it
reported five things which was 7%. Uh
the highest pair uh highest scoring pair
got 79% of the the known problems on
average uh they found uh 35 problem uh%
of the problems which is already higher
than what the de the testers without AI
were doing. They were definitely working
with AI these these developers. Uh the
funny part was that 63% of the the
groups decided that they didn't even
submit the results, but since I already
see the results when they wrote the
notes into the application, I know that
if I collected their results and I
submitted them for them, they would find
60% of the results. So there's a weird
idea of of competition that people don't
like to be judged. Uh so uh uh maybe uh
doing this on your own is is a better
way of doing things. And overall looking
at the 10 pairs the 20 people across the
entire group they found 100% of the
inputs and 100% of the results uh with
help of AI and and them exploring.
Uh but no pair alone was able to do it.
So one aspect of exploring really is
that well obviously it's not a
competition but also uh that uh when you
bring in new perspectives and other
people they will start from a different
end. So if you are in a rush having a
what Lisa Chrisin often calls a party
around testing kind of like you know
getting everyone together to look at it
is probably how you would get a a higher
uh score and and result. But just
leaving this for you as as a kind of
like an idea that uh you could do a kind
of like an self assessment on on how
would you do uh yourself uh on an
application where well at least most of
the or some of the bugs are already
known and and and uh can be
automatically compared uh uh your result
your reports can be automatically
compared and and you can get a score on
on the input and the results coverage.
So you can notice I talk about very
different coverages. I don't talk about
code coverage. I don't talk about uh
requirements coverage necessarily. I
talk about results coverage, the
relevant information. Are we able to uh
provide that and the tricks we must have
so that we could provide those those
results. Uh there is also requirements
available in the app. If you feel like
using those um uh some other groups that
I have done this with I know that uh the
more people focus on requirements the
worse they do on the results.
Again since you know you are optimizing
your time you decide which end you're
scratching and the the input that you
take uh has an impact on on whatever you
are producing.
So I've worked in in exploratory style
for for uh well pretty much my entire
career. uh the first job that I ever
took uh over 29 years ago
uh they had this concept of unirected
uh uh uh ad hoc testing that we were
allowed to use time on that was
essentially uh exploratory testing kind
of like you know giving us the the
freedom of doing whatever we felt like
was the right thing to do so that we
could find the information and I've been
kind of adding things like making
decisions or or uh including doing test
automation in it or or um pairing and
and and group work and and developers
and all of that uh for such a long time
that I really needed to kind of like say
that that the the way that I test and
the way that I think of of exploratory
testing it's it's the contemporary kind
of the reimagined style the information
intake if we get uh a requirement
specification uh it will uh have an
impact on what we see and We can choose
to do that on day one or [clears throat]
we can choose to do that on day three.
Uh that's our choice and both of those
approaches are are very much valid. Test
cases in in the style that I work in in
in exploring is is that they're uh
primarily captured programmatically as
test automation and they are an output
of exploring. Uh that's how you generate
actually test automation. and you look
at the application and you figure out
what kind of things you would like to be
able to repeatedly do with that. It's
actually how test automation gets gets
created and uh it's not just that you
would use that for regression. You would
also use that for extending the reach of
whatever your testing is. I [snorts]
rarely write manual test cases.
Actually, I have managed to avoid it for
more than 20 years now. I'm I'm really
good at explaining why we never should
and and if we should, I'm probably going
to use AI to generate something. I just
then don't use it directly. I will use
it very liberally in in in making notes
of of having covered all of those those
ideas.
Uh my testing doesn't usually end uh
with a report uh and and retesting but
it actually expands to this debugging
and repairing and exploring around if we
needed to fix this what do we need to do
around it. Uh the working agreements uh
mean that I often pair with developers
and I explore on a unit testing level. I
know that 87% of production problems
that the escapes to production uh by
some research uh has been shown that uh
87% of them uh can actually be
reproduced with a unit test which
basically means if we were exploring
better on the unit testing level we had
a potential of finding 87%
of the problems that currently are
escaping all the way to production. So
we need to work on all levels rather
than only on the the end uh to end flow
while while exploring and [snorts] uh AI
most definitely for me it's like an
external imagination that raises the bar
rather than the other way around. Uh
Mateo I can see that you are raising
your hand. Uh uh if you have a question
uh I would rather take the questions in
the end. If you're missing out on
something right now like a specific
thing please speak up. All
right,
it's easier to take the questions in the
end. So again, if you have a clarifying
thing like it's now urgent on on this
one, uh you can definitely still kind of
interrupt me. I I can't see the the chat
while I'm I'm speaking.
>> You can keep on going.
>> All right. Uh when I teach, you can
already see that I often use different
kinds of applications. This is uh an
application created by uh Christine
Pinto I think her last name. I can't
remember names right now. Uh uh she
created this uh AI enabled test target
where uh uh vibe coding something uh
with bugs uh you can kind of also try
out your your things. So this is one of
the uh more larger applications that I
have let people play with. Uh we found
on this one we found 32 functional
problems and uh ended up with uh fixing
all of those problems in the the while
we were testing them and uh then also
including both unit level and and end
toend level automation for that. So
that's kind of what I what I would
expect to happen. But I I kind of like
wanted to show that as a a baseline for
the the idea that uh when I uh work with
various people on on trying to kind of
move into this idea of of u uh
re-imagined contemporary exploratory
testing and particularly in uh the age
of AI
uh the uh thing that is difficult to
discuss is uh the past experience
eriences of feeling like there was an
anchor that I will steal away from you
and whether I stole it with talking
about exploratory testing which is kind
of like an internal testing community
related pull off of of uh raising the
bar of the results requiring that we we
see more of the important things or
whether it's like an external pull right
now which is AI forcing all of us into
more unknown territory stories.
Uh that anchor I think was always
imaginary. It wasn't really there. Uh
but I have a lot of colleagues in the
community that I have talked to who tell
me that the anchor didn't feel imaginary
because they could always say that
somebody else didn't specify how things
were done. And that's the thing that I'm
taking away uh with uh exploratory
testing. But if you are not taking it
with exporter testing the AI related
work is is going to be taking it as
well. The correctness uh it's it's
really not defined externally. Uh if it
was your job was comparison and your job
is actually judgment kind of you know
applying judgment on behalf of other
people so that you would build great
software. on the expiratory side uh you
kind of like you know you you generate
the expected uh you say is this
reasonable thing to to uh uh assume that
we would get an imagination is your job
requirement especially now in the the
age of AI so you have to have to apply
that uh judgment so it's not just
comparing to what somebody else told and
what was the intent or what was asked it
was it's now more on the side of what is
actually the the end result that gets
generated and on the AI side uh the spec
becomes now more uncertain. Uh it is now
more of a generated one or parts of it
are more generative one and imagination
becomes no longer a private resource. It
is actually something you share with
your team, share with your your group of
people that builds the system with you
build the system with and the tasks are
are expanding
uh to product side and and the developer
side. So I usually uh kind of like you
know I collect these kind of ideas of of
of what is really changing. These are
from one of my my uh uh colleagues that
I I worked in in learning these kind of
things with that uh uh there were five
things that that she found. This is Arya
Devis uh uh comments that I put on these
slides. Uh five things that she sees
that I really broke for her in making
her do vibe coding and testing the vibe
coded app. uh which was the the idea of
the spec uh and and and the fact that
it's it's you know really uh uh somehow
kind of like an authoritative source. Uh
then uh the code uh whether uh you can
tell things uh from it uh on the
technical quality that's not the only
thing that matters like it can still be
wrong from another perspective if you
don't see things. It's it's hard to to
verify things. uh uh your uh finish line
is is something that you need to set and
you need to agree on and talk with your
team and and you can simultaneously be
uh both very close and too far. So so
like you need a big mix of of techniques
in in order to to do work in in the the
the new kind of of world.
Uh I wanted to simplify this a bit on
kind of like what are really the the
changes like you know you lost the
anchor what are the the changes the
changes uh uh with the anchor going away
uh on the left hand side is is that
we're starting earlier this is not
really the shift left kind of starting
earlier this is the human in the loop
continuously kind of starting earlier so
this is not a project and and doing a
better plan in the beginning this is
showing up for conversation ations that
we would consider are earlier than the
hands-on testing uh would would happen.
So you would probably find yourself uh
doing work that you might not have
always done uh while uh under the
influence of AI availability.
So uh you might be doing uh code
reviews. I absolutely love visual code
reviews. Kind of like, you know, ask for
things that you think are risks from AI
and ask for a visual and you can
actually see things that you did you you
were not able to read yourself but you
can start those conversations early on.
So AI kind of like enhances your ability
to explore those kind of things. uh and
also it helps you to just you know
asking for just finding those issues
rather than saying create me test cases
I will then execute them just ask for
the results ask for the buck reports ask
for the information that is relevant and
and think of of of uh test cases more
like an output for the next times you're
testing rather than an input for the
first time you are testing so that's way
of ways of starting earlier here in this
kind of like um uh expansion of of your
own tasks. Then uh you would probably
also be able to continue further. So you
can report maybe bugs uh with a pull
request.
So you can actually fix uh things and
you can document uh tests uh uh with
test automation. So, kind of like
leaving behind a ability to repeat all
of the ideas that you had or build on
top of the ideas that your team already
has uh maybe documented and say, "Hey,
this one is is something that I'm
finding more problems with. Um uh maybe
we need to to add it here. And here's my
my specific example." So I've noticed uh
that over the the kind of like the AI
use on on this area uh we're able to do
things while exploring uh in a you know
with the same time in a smarter way
integrating the the different ideas uh
together. So I listed my five ways of of
how I usually use AI in exploring. I
added this as a as a uh a new thing that
I haven't yet before included in in this
particular session. Uh the first one uh
we talked about already kind of like
asking to report the bugs. Explore and
report the bugs. Don't ask to generate
test cases, ask to report the bugs, ask
to generate fixes if you have access to
the code. So kind of like going into
into let it do some of the testing for
you. And a great way just a basic tip uh
if you get only five problems out of the
the simple cases that I gave you as a as
a as a things that you can rehearse with
>> [snorts]
>> uh saying that oh somebody told me
there's 54 of them or 72 of them it will
give you a lot more uh and and actually
try to confirm them. So insisting that
there must be more information, it's
actually a great way of prompting for
exploratory testing purposes, great way
of prompting AI to to actually do some
something better, but it needs the eyes
on the application. So this particularly
works well currently with web UI related
things.
Uh a lot of times there's these MD files
that we share and we distribute over uh
the the use of AI uh skills files or
agent files or just instructions that we
felt were you know good reusable
prompts. I call those agentic
information slices. So talk to your
colleagues and share them. If you have
anything good and it's worked for you,
show them what you have done. great use
of AI but it needs to become a team
thing and a shared thing rather than
something that you do all by yourself
and and alone. The third one, make notes
maybe uh you know in whatever format you
have, but tell AI to actually ingest it
into a a a an LLM wiki and and you get a
second brain, a visual representation on
the kinds of things you pay attention
to. And when you grow that thing over
time, it is a really powerful way of of
aiding your exploring and taking uh
really great notes.
I won't have a time to demo all of this
for you today, but that's something to
to search for. Uh fixing bugs instead of
reporting them. We already talked about
this. Uh asking everything visual. You
know, you can see things differently
when you look at the visual. Ask for a
model, ask for a visual. And finally uh
when that test automation needs to be
created treat it as documentation and
[snorts] treat it as a way of fast
forwarding you to a place where you want
to explore more from. So make it so that
that you can also use it for for kind of
a starting point for all kinds of
exploring.
So these are my my favorite uses
currently within exploratory testing.
And again since I talk about
contemporary exploratory testing I don't
think these are anything other than
exploratory testing they are just you
know tips within you know techniques
within uh exploratory testing the
quality slices you know everyone has
their own approach uh on on how they
slice things I've been trying to uh
slowly kind of like uh publish our ways
of of of doing some of the slices. We've
been part particularly on on security
and accessibility uh at first kind of
like trying to upskill over a larger
organization on those and out of that
one of the main things we learned is is
that we don't want to call this any more
testing. We want to call it software
intelligence. So something a little bit
more but again the idea basically is
just to uh make sure that you share
things. Similarly, [snorts]
uh uh sharing things, sharing common
context, talking to your colleagues, not
just talking with the AI agent or AI um
chatbot.
Uh hugely essential. So when I talk
about the ideas of contemporary
exploratory testing, I usually think in
terms of pairing with a real human uh or
ensembling the third person person,
third uh entity in that pair that makes
it an ensemble that could maybe be then
be uh the the the agent uh that you
bring along into it. and and while uh
the uh agents are thinking kind of like
you know doing some kinds of calls back
and forth they are not really thinking
but kind of putting things together in
in a reasonable way. When you have that
real human uh as part of that little
three uh entities or two people and one
entity ensemble you probably generate
ideas of of where did you actually want
to scratch that picture that you weren't
even thinking. uh this has actually
freed up a lot of of energy into great
ideas about exploring when when you use
pairing uh in in combination of of of
these kind of things but kind of
learning the the uh architecture of of
the agents how they they are built and
and learning to share that context with
your colleagues and team it's it's
definitely an an essential foundation
uh the foundation uh that I kind of like
summed summed it up to is this idea of
like, you know, maybe you want to, you
know, try things out together. Maybe put
some of the things uh into pipeline so
that they keep doing some of the work
while you're gone. Maybe you want to
learn to, you know, have experiments and
decide which uh things actually work and
not maybe share it with all of the world
and not just your direct colleagues.
maybe uh uh you know give someone an
idea on what to put in an application if
if you don't have them or pick an
application that has already gone
through these cycles. So we all have
something of of these kind of of cycles.
So going through through things uh this
is just the the kind of way of of of
thinking about it as it's like a you
know a process that that uh runs
through.
So I wanted to uh close uh with the idea
of of uh I hate the idea that agents are
making us work more solo
because when we work solo it is kind of
like this. We have good moments and bad
moments. We have good areas of knowledge
and bad areas and we have those blind
spots that we started with on the on the
results side.
uh if we then ask someone to kind of go
after us uh uh to try figure out where
our blind spots were uh we're losing out
our schedule. So if we could have the
agents help us to kind of like you know
maybe you know level up some of these
things and maybe we could have an actual
other human with an entirely different
process uh or approach or different
background or or attention uh into the
same things. overall we could, you know,
adding people, adding perspectives,
adding these quality slices, we could
maybe uh get the the overall level of of
the work that comes out higher. And now
when the the AI era is actually really
making the guidance and the assessment a
thing, don't stay alone on doing those
assessments. Uh now it's it's time to
pair up and maybe even team up with your
teams. uh because whenever you then go
and work alone, if you have created that
kind of like common understanding in
your team uh you're able to do better
work even uh on your own having learned
something you didn't know that you
didn't know because when you didn't know
it you couldn't ask for it but you can
see it in that moment and and nothing
with the agent says that that pairing or
unsembling is going away. It is really
the foundation. Maybe you end up having
an ensemble of two people and 20 agents.
That might be the the the thing that you
you learn to juggle, but you really want
to uh get the best out of everyone,
including the agents into the the work
you're doing. So my kind of conclusion
to what I wanted to share today, I think
that in this age of AI exploratory
testing and and kind of like the slices
and the techniques and and the juggling
and deciding where you scratch first and
how you repeat the scratching because
there's always more to to scratch in in
those pictures, that actionable feedback
that challenges those well-maintained
illusions that very easily get born. It
has never been more important. And it's
not just the testers, it's everyone in
the software teams that are on this this
challenge.
That's what I had uh in mind. And now we
have a moment for the questions that
people have been hoping to ask. Before
I'll jump and have end with the qu the
questions. First of all, Mar, I want to
thank you for this. That was
fascinating. Um, exactly. Federa just
jumped in and say hi Feda. It said
amazing talk and I agree. Um I want to
and I do want to squeeze in one more
sent actually to connect to what you
mentioned uh about don't test solo with
um exploratory testing. So one thing
important thing that I forgot to mention
about practice test and exploratory
testing is that you can actually
register exploratory testing on the
platform uh and and that helps kind by
the way by sharing those results and
having people rethink and look at it
from different angles. So just I wanted
to do that. Uh and now I'm handing over
questions. I'll start with Lisa's
question. Um with how does BDD or ADD
work in this new AI era? Okay. Uh are
you guiding development with examples?
How does that approach connect in your
opinion?
>> I didn't manage to use it very heavily
even before the AI era. like I I did a
lot of experiments where you know I
decided that for six months in a
particular project we would try to use
examples to to define things and and you
know examples are good in in having that
conversations but trying to drive it
through all the way to code I I didn't
find it as as valuable as as I found the
example in that conversation. So
whenever we are working uh with uh
intent uh examples are very helpful to
to leave around whether you do those
kind of like before you start or make
sure that you have them uh from whatever
slice you end up implementing. I I see
very different approaches in in
different teams. uh but I would kind of
like like to see that um that style of
documentation uh continuously grows with
the the the uh AI oriented development
work that we're doing. Uh I've tried
inserting kind of like examples into
into like you know generated based on
this. I I don't think that has worked
too well for me. I feel like there's a
there's a human aspect to that where uh
AI isn't doing quite the same thing as
as humans do. Thankfully for now.
>> Yeah.
>> At least.
>> So again, kind of like some of the the
language on asking for the right thing
and the intent is is is turning those
examples into, you know, having some
helper words on the technology and and
then you will end up generating a little
bit closer to what you you wanted. But
very powerful for for the human
conversations.
Always an example. And the next question
uh which somewhat connects but not not
100% uh is H asking uh or stating that
he's curious about what role the spec
plays in aligning reality original
intention for a system and he goes on he
say when you say that AI acts by
building internally a spec while we're
doing exploratory testing without using
the original spec as a reference I
understand that it managed to infer a
model from the actual behavior. Okay.
>> Now, that's not quite how I think of it.
Kind of like they probably, you know,
having requirements and specification if
we have those in mind. It is good to
write it down. It is good to agree on
what we're building. Otherwise, we'll
have, you know, as many perspectives as
we have people. We'll end up having some
of that anyway, but having some kind of
like a baseline drafted usually with
examples, it's it's a really good
practice to do. But uh then when we are
exploring when we're actually using the
application we create a different model.
Uh there's some techniques uh uh where
uh you would create two models and you
would kind of like reconciliate between
those two models. That's a great way of
exploring kind of like you know build as
many models as you need and then then
reconciliate between them with help of
AI.
>> [snorts]
>> uh I can give you a person who can give
a talk on on how he did that and he has
really great materials on on on on that
kind of techniques but again just asking
for those kind of things that's what I
mean by exploring uh that you would ask
for kind of like create me first this
model I know that it represents you know
whatever was given as as as kind of like
definitive uh requirements then generate
me a model of what does the application
really do and then compare these and
again kind of like you know apply those
techniques in steps and AI can help you
kind of fast forward many of of those
things. Uh when uh uh the spec got
generated it was more like we had a you
know like empty project. We built the
entire application. We were you know
doing exploratory programming. They call
it VIP coding nowadays though. uh uh for
um you know an application that we would
want to have and kind of like start to
to figure out on on how do we make that
that work and uh when your spec is
couple of sentences or couple of pages
that you start from and it's somebody
else's idea usually in taking that
information and understanding what is
actually relevant maybe having some
conversations it's a good idea in in the
in the background.
Good,
good. So, I think those were the main
questions that we had for today. Uh, I'm
not all of you can read uh the some of
the comments are for everyone. Uh, so I
don't know if you had a chance to read
them, but
I think it summarized very well. Um, I
like that comment specifically um from
Diana saying that was this was a great
appetizer. Okay. Uh, before QC uh and
people are looking forward to seeing you
there. We will also be there by the way.
So uh not myself but some people from
our team. Uh so we will also be looking
forward to seeing also Marit and
everyone else in case you are there. Um
I did wanted to invite you to our
upcoming webinar as well that was
supposed to be mentioned before. Um just
as the last sentence for today uh that
will be hosted next month by Joel
Valinsky our um CEO and co-founder about
transitioning from QA data to decisions.
Speaking of, I really love by the way
your approach about that you overfocus
on requirement, you're missing the
results. So that really resonate in a
different a little bit of different
approach. Uh so we do invite you to join
us. Um we will share the link with a
recording for everyone uh tomorrow uh to
sign up. That will be October 28th. And
with that being said, Maret, thank you
so much uh for giving the session. Thank
you all for being with us today. We hope
you enjoyed it as much as we do. Uh and
we're looking forward to seeing you
again.
