---
title: "Maaret Pyhäjärvi on Testing in the Modern Age"
video_id: 0CzA_yll0Fw
url: https://www.youtube.com/watch?v=0CzA_yll0Fw
upload_date: 20240312
duration: 26:12
channel: Semaphore
tags: []
---

# Maaret Pyhäjärvi on Testing in the Modern Age

> 🎙️Testing safeguards the quality and reliability of products. And while there might be occasional misunderstandings, as in any collaborative environment, developers and testers are not inherently at odds. On this subject, veteran tester Maaret Pyhäjärvi believes in delivering feedback constructively.  In this episode, she will share her thoughts on the role of testers, how they can provide “the right kind of feedback” to developers, and how to navigate the nuances of different architectures and documentation practices.
> 
> Read the transcript: https://semaphoreci.com/blog/maaret-pyhajarvi
> 
> #development #testing #tdd #bdd #software #devops #podcast #listenable

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

hello dear listeners welcome to
semaphore uncut a podcast for developers
about building great products in this
new episode Darko the podcast host
welcomes veteran tester morett payari
morett shares her thoughts on the role
of testers how they can provide the
right kind of feedback to developers and
how to navigate the nuances of different
architectures and documentation
practices I hope you enjoy this new
episode and let's Dive In
Mar thank you so much for joining us
thanks for having me Darko uh great uh
can you please just go ahead and
introduce
yourself uh I've been uh in the industry
uh for 26 years now I've been working
with testing and quality related things
pretty much all of my career I've had
various testing titles from test test
manager test researcher then moving over
to management side and then back to
testing titles and then again back to
management titles currently I am leading
a 20 person development team in in
Visa semaphor has released the flaky
test dashboard to help you identify
unreliable tests in your project
identify which tests disrupt your
pipeline and cost you the most all in
one place go to semor c.com SL product/
flaky dests D dashboard to find out more
for us not really familiar with testing
as a as a discipline can you give us
your let's say definition and
introduction to the discipline we come
into this industry that grows very very
heavily with different kind of
backgrounds some people get their first
assignment as in kind of you're writing
test automation you're going to write
PDD scenarios first and only then you
will do application features you might
not call yourself a tester at that point
but if your you know Center of your work
is that you spend time really thinking
about how you capture things in tests
you are somewhat of a tester then uh
other people like myself we end up in
this this industry by kind of you know
paying first attention to the domain uh
what kind of things the customers are
really expecting and you know talk more
to the customers and make sure that
they're getting whatever they wanted so
some people end up uh from that
perspective it's not always evident uh
of of who's a great tester and who not I
have had this this basic experience of
kind of like you know trying to myself
recruit testers into my development
teams and a lot of testers are to
commodity kind of like following
developers doing exactly what the
developers were already doing and not
adding value whereas other testers the
ones that I'm looking for and again I've
been trying to find the right words to
explain this they really add value in
those teams so so again it's not just
testers it's the right kind of TS we
would need for for the teams that
generally um lived you know and and
still live without you know a dedicated
test testing team um there is always
that moment of hiring the you know the
first person within the team and I know
a lot of our customers who are also like
teams of like couple of couple of dozen
of
Engineers that you know some don't have
like a testing team or testing person or
some just you know thinking of
establishing and um let me mention one
other thing that I have been seeing is a
is somewhat of a trend um our interface
towards towards a lot of uh companies
are Developer productivity developer
quality you know developer productivity
and quality teams or developer
experience teams and they end up being
connected to the Quality also a lot of
time um so just want to to to mention
that as U you know quality and testing
are you know um sometimes more connected
depending on the company they're
definitely connected and like I've been
changing jobs every two three years so I
have had a chance of seeing a lot of
different kind of companies including
ones where there were no testers before
me and thinking back kind of like one of
those where I joined there were 20
developers in the organization and I
joined as the first testing specialist
uh I definitely knew that there was a
risk uh that the developers would expect
me to do all things they recognize as
testing and that doesn't help with the
quality like if you throw it you know to
someone else kind of like thought you
already knew what you're supposed to do
and now someone else comes and and you
know they're specializing in doing that
you no longer have to that's usually not
a good thing so I needed to kind of like
from day one I needed to address the
fact that you know I didn't come to do
the testing that you're already doing
that remains there was testing you were
not doing that I came here to do I
established somewhat of a reputation
with that particular team by you know
they had this this well they were
following this metric of of how many of
the logins uh would end up in in a
visible error message kind of like a
user logs in how often will they see an
error message and they knew that they
had 18% like there was a clear you know
very visible measurable gap of what they
could know because they didn't know why
the users were seeing this I couldn't
touch the software for the first year
without seeing these big visible error
messages coming from everywhere and it
was funny because the developers could
see them too as soon as I sat next to a
developer and then we needed to figure
out kind of how to change the whole you
know CI related practices in that team
uh they had some unit tests and you know
some basic tests there but not enough
for the developers perspective they had
a project manager who was insisting that
you need to test on the end to end level
which is not where you get the you know
the the immediate feedback like we are
you know looking for in in the modern
world so uh one of the things that I
needed to do as as a tester or test
specialist in that team is to say we
don't hire more testers we invest more
time in that unit testing that we knew
that we need it so it might be that you
really need to uh look for the the right
kind of feedback rather than just you
know insist on a certain role or a
certain uh person to join that team I
remember speaking with some people in
the in in the testing World um who
advocating for that you know holistic
approach to testing of that you know
Hands-On work with the team and you know
looking from very you know different
perspectives and actually enh enhancing
the communication and you know critical
thinking with within the team um would
you classify your work that you did that
as as as that kind of approach or yeah
definitely it is is that uh I use the
word uh cont temporary exploratory
testing very similar to what some people
would call Holistic testing like it
seems like we we like different words
the usual reason why I call it
contemporary exploratory testing is that
we were doing this kind of of very smart
very Hands-On style of testing already
back in 80s in Silicon Valley like that
was already reported back there but
there's many things that have changed
since for example this whole automation
as documentation automation as something
that enables you to do things during
your work day that you couldn't
otherwise do and it would be silly to
say that exploratory testing is somehow
manual and and doesn't take into account
the you know the realistic cicd pipeline
based work that we have in pretty much
any of the teams that are successful
these days so uh that's why I've called
it contemporary that I've been looking
for the patterns that really enable us
to work together very closely as a team
and and tdd the way that I think of it
it's just you know exploratory testing
on a unit level you really need to learn
to express that
intent and and think in in multiple
Dimensions I finished my University like
in 2008 kind of have a had a very very
limited experience with creating
something which gets packaged and
shipped and should you know work 100% I
usually had the ability to deploy on The
Daily level you know into production and
fix something you know along the way
then I I also met people who like in '
80s and ' 90s did actually a lot of work
on creating the software which is going
to be packaged burn on the CD and put on
the shelves which has a very different
criteria and very different culture
towards you know the quality and you
know uh just a rigorous approach of
making sure that you know it really
works on a some you know High higher
level um any thoughts on on that you
know those two different patterns of
software being
shipped I think there must be more than
than just those two patterns uh kind of
uh if you ship software uh to a user
base where they are rarely using your
software you probably get the chance of
going and fixing it before anyone
notices it but if you have a few million
users uh probably 50% of them will
suffer before you notice your mistakes
so you actually even in the in the
faster cycles of things you have that uh
rigorousness of of what kind of problems
you cannot let go through even even
without the the whole uh CD related uh
uh trouble as well uh we used to do a
lot of bepoke kind of like you know
built tailor made software where you had
access to the production environments
already back in the in the 80s I think
uh kind of like it was on your own
server and and not all of it was kind of
like shipped with a AC so I don't think
the CD and and that stuff changed the
world so much but it definitely
introduced at you know something at some
point introduced this idea of uh uh we
would rather only deliver once and not
bother anyone more than once a year when
we give the the latest and greatest
version and I would imagine that's much
more of kind of like how we think about
uh products and and convenience for the
users rather than the the technical
aspects of of how we deliver mhm yeah
yes and and you're completely
right um but also I think uh there's
this weird idea that somehow people
think that if we deliver less frequently
it's somehow giving us the the
rigorousness like we have the time to do
rigorousness but actually we have time
to take more risks that's my experience
it's the opposite so if you made a
mistake you know even if 50% of those
Millions will see that mistake if you
can you know revert in five minutes it's
a short thing that happened and and we
are really working with the customers to
change this this idea of how often can
they install and why would they want to
install modern JavaScript uh isn't
really a a something that you don't uh
update uh frequently you do have to and
actually all even the older Technologies
you would have wanted to if you
understood security related
considerations at all but uh there's a
lot of of belief systems where moving
slower feels like you are safer MH and
actually it means that you just move
further away and increase your risks
yeah
yeah and in the realm of
um patterns that um that that we use to
build the software um I mean one of the
relatively recent elements that that
came to our industry this concept of
microservices and so on and being able
to ship
independently um from your perspective
the perspective of your discipline is
there like a difference in how you know
teams approach things and in terms of
testing and you know the quality which
is being achieved or it's not really
something that changes things a
lot uh it changes things in the sense
that uh for microservices you really
have to understand apis and be able to
work with smaller pieces with an API so
the conceptual thinking uh for testing
that you would do uh changes it also
makes it somewhat I think uh easier if
and when you have the the the technical
understanding of of you know Services
type of things it makes it somewhat
easier when you're not trying to guess
on uh end to end level what might be the
impacts you can actually well I'm a big
fan of in uh uh infrastructure as code
not necessarily as the tools in that
space But the IDE idea that nothing in
your test environment ever changes
without something changes changing in
the text files like if you get to that
level of of transparency of change you
can actually analyze the change and make
better guesses of of what might be be
impacted obviously level of automation
kind of like having that for every uh uh
interface but also having that across
interfaces so that you know you get the
the
feedback I I was speaking with someone
recently who actually worked in at Apple
in
um ear early 90s and
um he explained to me how uh testing
group was like a whole and it was like a
big team on its own and that change that
they saw that they saw actually is that
that that team was cut down into slices
and those you know testers were sent
around the the
organization to join the development
teams and um he was explaining that that
moment of um testers you know kind of
developers becoming a a boss bosses or
you know managers of testers and how
that actually really hurt their their
craft and and their discipline are your
experience is you know um confirming the
the similar uh
patterns uh I see the similar pattern of
breaking down the testing groups and
having testers and developers work
together in the same groups uh obviously
um I don't see the testers suffering
from having developers as their managers
because you know the developers might
then be suffering having testers as
their managers there's you know equal
representation of both kind of of
managers in in this sense so again
management uh both product owners and
and development managers or engine
engineering managers they definitely can
hurt the the testing culture a lot but
they can also promote the testing
culture a lot they can maybe you know
bring the bridges of you don't listen to
this person or or you're dismissing the
work of this person maybe we should you
know all work together as a team like as
if we are investing in having both kinds
of people in the teams and we are
usually investing maybe we should take
care of you know both kinds of people
with equal rigor or or care yeah yeah
you have to choose the kind of the
virtual aspect and then the the real
kind of teamwork aspect and I find
personally that testers can usually
bring the the virtual aspect of like we
collaborate across the tester role in
the whole organization easier than that
they can Bridge the we are in a
different group than the developers so I
would definitely not go back so I see
that pattern that we broken them and I
think that's the pattern that I am
driving
semaphor has released the flaky test
dashboard to help you identify
unreliable tests in your project
identify which tests disrupt your
pipeline and cost you the most all in
one place go to semor c.com SL product/
flaky D tests D dashboard to find out
more one thing I saw in one of your
recent talks when you
um uh I think that you were trying to
solo how you introduce what you do and
you know what was the of tester and you
use a very interesting term that that I
really like you know um feedback fairy
yeah that whole feedback fairy term it
came from a a um conference where
someone who wasn't a tester or a
developer was asking me what do I do for
work and I said I'm a tester and and I
was like I don't understand what that
means explain it to me like I'm five and
in the moment I I I just you know I
didn't know what to say I I didn't know
and later on you like next night like
middle of the night I wake up and I
realize I should have said I'm a
feedback fair you know I come with the
gift of feedback you know with a smile
on my face kind of with you know actual
Care on how people will receive the news
but also remembering that some of the
feedback is positive like it's not only
the bad news that your baby's ugly it's
also the you know the great news that
that it's actually you know looks like
things are improving things are better
today like maybe if you remember things
two weeks ago they were you know not in
in the shape that that we have things as
of today yes yeah the whole center of a
a tester job generally is is kind of
like look go looking for feedback it's
about the product and it's its quality
it's about the organization sometimes
it's the people's patience it's the
communication patterns that you're
testing and and and giving feedback on
and and trying to do it in a way where
you know you're looking for things that
don't quite work but you're trying to
somehow spin it in a in a positive
collaborative way
one thing that uh generally engineers
and developers don't like to do very
much is documentation do do you see from
your
experience a a way that um you know
testers can improve that that that that
line of work some of the reasons why we
don't like documentation is that when we
read it it's not so useful after all we
haven't quite cracked the the the secret
of what is it use what is useful to
write down for future usually it's
something that we didn't write down uh
we write too much which means then that
there's a cost of reading all of that
and we way too often write it too early
when we know less than what we would
know by the time we have developed
things so with me the the thing the way
that I have kind of learned to think
about this through testing is that we
should document when we know the most so
testing you know test cases or or
automation cases in particular it should
be an output rather than an input like
even DDD is kind of saying you know you
have the test cases first and then you
implement according to those test cases
sure yes let's do that but let's make
sure that everything we learned while we
were doing things gets captured in that
documentation too paying attention to
who's reading stuff and what's useful uh
is is is a big part of it uh what are
they needing and are they really needing
it or are they asking it out of habit
while you were explaining this like
documentation being you know written too
early um I I I I I can't relate to that
and that that drove me to asking a
question about um you know generally
customer
support and connecting that to the to to
the support team because that's kind of
um that's a really high quality feedback
you know uh it can be high quality
feedback uh I have direct access to all
of the emails that the customer send
over to us and from a development point
of view I wouldn't call it high quality
feedback it's high noise to to uh real
information ratio but when there's
information that is really really
valuable clear clear clear uh distance
between the development team and the
support team often means that the
support team doesn't know when the
development team would be you know
having the power of actually changing
the user's experience so we've really
needed to build this Bridges where we
you know read that stuff
together and and pick up the the
important things and surprisingly many
questions are about uh uh I'm not
reading the documentation I don't even
know where to get started that type of
of question so I I don't think that's a
high quality feedback but it is
something that a lot of products will
will face yeah yeah and maybe a question
relates to that um any thoughts of like
um mixing the documentation with the
user interface games are really good at
leveling this kind of information
whereas the the office type of apps are
really bad at leveling and and again
assessing where are you in in your need
of leveling I would like to see more
documentation built into the
applications but then again like way too
often it happens that we don't build the
usability of the application which is
kind of like we put the documentation as
a secondary layer when we didn't do the
usability related work
uh but yeah there's definitely good ways
and and not so good ways of of of doing
that uh I'm often overwhelmed with too
much information but I'm also as a
person you know like I'm also
overwhelmed with uh going into a
training that actually teaches me what
buttons to press I hav needed that level
of teaching for for years but I can
appreciate that there are users who will
actually want and will need that because
you are too native to the to the domain
and you know just speak
almost like a tester trade that the
software Whispers to me it speaks to me
so it's made me a particular brand of a
little crazy in in the sense that I hear
like it's you know it's saying that I
can press these buttons and I can trust
that the buttons you know you know if I
break something because I I press those
buttons there's probably a way for me to
recover from from those as well for the
for the teams that don't have yet you
know have anyone you know in the in the
testing Ro um how would you how would
you recommend that that first person is
you know searched for what what what
should the teams look in that you know
first tester within their teams and
maybe connected to that a little bit uh
what's a piece of advice that you would
give for the you know testing people in
in leveling up their careers so the next
step there is usually I suspect a
pattern that you see and that you would
really want to to convey that message to
those people and that ideally they would
they would he the
advice I I look for three things in in
the first and even in the second
testers I look for someone who knows how
to program I would not hire a tester who
doesn't either know or want to learn to
program anymore like that's definitely a
a Cornerstone you can't read code you
can't get the the information if you
don't want or can't get to that
then I look for someone who knows and
wants to learn the domain kind of like
connecting things from the domain so
that we recognize the gap between what
the users want and expect and the
stakeholders in general want and expect
and do the research in that space and
then bring it back to the theme and then
the third thing that I look for is is uh
collaboration kind of like you know
being able to talk about this stuff with
people who probably have a different
background than than you do yourself so
uh a lot of times I find only either the
programming or the domain in the same
person and I usually find that I can
teach programming easier than the domain
thinking so I usually welcome someone
who doesn't know yet how to program but
I teach them the basics test related
programming and test related code
reading is simpler than the General
application programming
is uh but on the collaboration if you
don't have that kind of like you know
initiative of you know daring to speak
about all of this stuff that you're
uncertain of I don't think that can be
really fixed so so I usually try to look
for for these and again uh same way when
I'm looking for the next steps in
leveling You Can level so much in the
domain and and learning about the
application and seeing problems like a
lot of people who call themselves
testers these days they actually don't
know how to test really well but also I
would look for someone who wants to
learn that automation like it is really
not an option to say that that uh we
wouldn't be part of that world at
all for people that just want to you
know learn more about testing learn more
about you what are the best ways to to
follow you and your work um I write uh
public notes all the time on masteron so
that's the the definite best way to uh
see what I'm thinking and what I'm doing
and what I'm writing uh the second level
of of the things that I write usually
goes into my blog then the third level
is LinkedIn uh I select things that I
feel like are something that I feel like
are ready and and and meant for wider
audiences so I would go go there and in
LinkedIn I also share articles that I
have
posted uh thank you so much for talking
with us hey thanks for having me what a
great conversation we hope you enjoyed
it and learned something new make sure
to subscribe to semaphore uncut on your
podcast player of choice so that you
don't miss our new episodes and stay
tuned
