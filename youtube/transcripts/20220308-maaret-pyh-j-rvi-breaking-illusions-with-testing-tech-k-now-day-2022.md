---
title: "Maaret Pyhäjärvi - Breaking Illusions with Testing - TECH(K)NOW Day 2022"
video_id: oQXbs3awemg
url: https://www.youtube.com/watch?v=oQXbs3awemg
upload_date: 20220308
duration: 44:03
channel: TECHKNOW
tags: []
---

# Maaret Pyhäjärvi - Breaking Illusions with Testing - TECH(K)NOW Day 2022

> As a tester, I don’t break your code, I break your *illusions* about the code. And illusions come in many forms. Illusions may be about the code doing what it’s supposed to; about the product doing what it would need to; about your process being able to deliver with change in mind; people having the skills to deliver well and about the business growing with uninformed risks on the product and the business model around it. 
> 
> This talk goes through examples of illusions that need to be broken and skills that you need to build to break them. No matter what role you play, these skills will help you on your path to seniority and impact, and create small scale awe in your organization when applied well. Testing is not just the technical checks but more relevantly it’s about discovering information about threats to value you’re trying to create. 
> 
> There’s no better way to do this illusion breaking than recent practical examples, so let’s look at some samples from my trenches!

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

[Music]
hey
i am going to talk today on the topic of
breaking illusions with testing
and before we go into the topic let's
talk a little bit about who am i
hi my name is maret and i am a tester
these days not everyone is or every team
has a tester anymore maybe we have
someone who does testing but it just
happens so that testing and being a
tester kind of focusing my career has
been around this type of work
and i've been doing this for for 25
years
there's a significant conversation going
around in the world right now on
testing and who should do it and many
teams no longer have specialists like
myself and that's the type of structure
that i'm also building
a lot of times in my companies having
less of my kind but kind of the way that
i frame it is that you know i have these
skills i have many other skills as well
i'm also a programmer i'm a conference
organizer i'm a conference speaker
i do many many different things i've
been a manager over the years i've been
a researcher over the years
and
what i need to do is have some choices
on where do i use my time and i
generally choose to use my time on
testing
and there's obviously a reason why i
choose that
i choose to be a tester because what i
often find myself doing is that i enjoy
the work that i get to do
the work of breaking illusions
when i was talking to one of my
colleagues back in in the days few years
ago and i quoted him
this idea that you know i'm a tester
this is what i do this is why i'm i'm
kind of existing in the projects that i
don't break the code that they created i
break just their illusions the
developers illusions typically about the
code or the product owner's illusions
about the code
they kind of thought that was so funny
uh way of training it that we are
centering our work as testers around
illusions that what they ended up doing
is tweeting it and this uh quote this
saying has kind of you know taken a life
of its own it originates from somewhere
i've used it and formatted it
as part of something that is is kind of
central to the way that i test
and i think of myself as you know
centering my work around breaking
illusions so if we think about illusions
what are illusions uh we usually like to
think that the software that we created
the software that we you know uh try to
pay attention to creating uh coded with
our full hearts or at least half of our
hearts
in the in the game
that it would work and we would
definitely usually generally kind of try
poke it around a little bit and try that
but we'd want to believe that since we
were creating it it would work and as
someone who focuses and centralizes
testing
i approach it with the idea that you
know i'd love to see it work i'd love to
see that this is true but there is a
chance
and it is an existing chance that my
hopes
would be
very quickly proven wrong and i want to
approach things rather from the idea
that maybe just maybe we don't yet know
that things work and that's where where
my work starts
so testing
it is about kind of you know looking at
things very closely sometimes it's
looking at yourself very closely like
looking in a mirror and thinking about
how are you as that tool who is trying
to figure out ways of of how might i or
other people around me be disillusioned
with empirical knowledge but it is this
idea of you know
just paying attention uh paying
attention to spending time with the
application applying uh
uh use of the software either with other
software or what we call manually kind
of being available being fully brain
engaged
into the work and looking at kind of
empirically if i do this what will
happen what is exactly what will happen
and applying a scientific method kind of
like thinking in advance what do i
expect so that we can notice if our own
illusions of of things that used to work
yesterday for example
must be also also broken but what i
still want to emphasize kind of before
we get into in further into this
breaking illusions topic is that we have
illusions about both the good and the
bad
i've worked with plenty of project
managers who are very optimistic and you
know schedule comes first and we always
will not be able to do the schedule
and kind of believing in the on the
positive side but i've worked with
equally many uh project managers who
have been worried about the schedule
believing in and you know seeing risks
everywhere seeing that we're probably
behind wanting to actively communicate
that that risk can add behindness to
other people so depending on who i end
up working with i find myself kind of
like being the the
like the person who's kind of going in
between uh the the the cracks figuring
out the balance on you know if it is
overly positive i will definitely go on
the negative side and if it's overly
negative like actually it is quite often
in teams i find myself being on the good
side kind of like emphasizing also where
the illusions couldn't be broken where
we were actually right about things
working exactly this way and paying
attention to you know nice work that
people have actually managed to get into
that software because i get to see the
software both work
and not work and i want to equally of
course appreciate both
so as a tester
anyone doing testing what you would be
doing is kind of approaching things with
the idea that maybe you don't know it
all yet
maybe there is this real chance of
things being broken and unless you want
to see
that things are broken you very easily
miss relevant information so breaking
illusions requires you to approach
things with an open mind and the
possibility that there will be
information to find
the way i usually end up doing my work
in testing
is that kind of like looking at the
software in the team that i'm joining
it's it's like a little bit of like this
amoeba of going into different
directions and it has some sort of a
shape of course i'm asking questions
with the rest of the team on what the
shape is like but the assignment that i
usually go in with
is that to break those illusions
i need to go and find not all but some
of what the others may have missed
i get to use my usually mostly my full
days on focusing on the ideas of what
are we missing what is the information
we don't yet have available and there is
so much of that information that we
don't have available that i can't of
course even myself as a tester getting
to centralize my work around this i
don't get to do all of it but i get to
do some of it and i get to learn over
the last 25 years i've gotten to learn
how to go about it in an effective way
a few years ago i went and tested
one developer's open source testing uh
tool
and he was encouraged encouraging me on
kind of yeah sure go for it you know
it's all written test first and it's
code that he's very proud of it wasn't
only written test first it was also all
written in pair programming style
but the test suite existing test suite
that you could run with tdd
and bdd in place was also quite
impressive so i took a look at whatever
was was existing on the on the
documented side i'm like
this is not where i should be spending
my time i'm gonna be looking for
something the others have missed
well on the developers words quoting him
from a podcast i destroyed the
application apparently in like an hour
and a half well the reality is it took
me more like three hours so you know the
time was kind of
significantly more but still in a few
hours you can only do quite shallow
testing
and the types of things that i did is i
set up an environment where i could you
know have the tool uh in unison with the
other tools that you would you typically
have in a developer's environment where
you would want to use a unit testing
tool only to figure out that there were
conflicts between the different
libraries that you'd expect to have so
system level ideas i asked and listed
many of the functionalities that i was
expected to find and i just you know
picked some of them that felt like they
were maybe you know interesting or
complex or or would help me first
understand the application and as i went
through the the features i would figure
out that uh some of them were hard to
discover basically saying that the api
needed to be rewritten and this was the
eventual conclusion after longer
conversations and i found many things
where things were not actually working
when i just you know went a little bit
outside the basic scenarios using a
little bit different data than normally
people would maybe use in creating it so
it wasn't actually a very complicated
thing and it didn't require so much but
it did require this idea of you know
going with the intent and idea that i am
about to break some illusions and find
something that others may have missed
i do the same kind of things uh in
various projects so in the last few
weeks at my current work at weisela i've
been testing for example this is one of
those features that i've been testing in
the last few weeks
and i've also been using this feature of
configuring uh
new airports as a sample for
interviewing testers so i've had a
chance of interviewing more than 10
people in the last month or so
with using this example with many of
them and i've made many of my colleagues
do this as an exercise also because i
thought it was a really nice way of
showing
what testing really is about and what's
required to break those illusions
asking uh from that config yaml uh what
would i change here how would i test
this like making it really specific on
what kind of things should be different
i learned that way too many of the
testers that i interviewed would only
choose to basically try values for the
latitudes and longitudes would try
values like
too big and too small and one that is
just right
so kind of like just one positive test
case whereas uh it turned out that for
the implementation of this particular
feature
uh if you would have value such as one
of the numbers zero
or one of the numbers uh set up as as
the chicago oh air
aware airport the minus 87
point a lot of decimals after it
uh you would then end up actually having
the apis
giving a technical error not even a 500
of error but a technical error
and the application appearing as if it
was working even though it was no longer
receiving data so a lot of people kind
of go in and and approach it with uh i
see it work with one scenario and then
focus on i make sure that i can put in
in wrong kind of values but there is
within that positive side there's also a
lot of lot more values to try out
and uh one of the illusions that i've
broken
on myself kind of why i raised this on
this this presentation today is that i
find that i was believing that this is
something every tester knows how to do
and with my sample of about 10 people
right now very few people actually know
how to do this and a lot of us over the
years with the years of experience that
i also called that i've been having
we've learned to
try only the simple things because the
simple things already might often be
broken
and then in the end what could have
happened for my organization if no one
paid attention to this is that we would
be for example selling our system to the
chicago airport only to discover that
the whole system doesn't run when it's
configured to that particular realistic
location
obviously over that a couple of weeks
i've also kind of collected various
examples now and ended up automating
scenarios so that i don't have to pay so
much attention to this anymore later on
but someone needs to come up with all of
those ideas that we try out in the first
place
and sometimes actually a lot of times
some of my best tester colleagues in the
teams are the teams architects and are
the team senior developers who have
experience already in the idea that
things are different with different data
with different ordering of features and
we are doing great job you know
co-designing tests and and and ideas of
how we would test so that we can break
our mutual illusions so it's not just
something that is my
work and my work alone even if i am one
of those people who gets to specialize
in it and use most of my time on
problems like this
but you know i showed you a couple of
examples
uh on uh breaking her illusions finding
problems but the way that i've learned
to think about this this phrase of
testers don't break the code they break
your illusions about the code is that uh
it's actually not just the code we're
breaking and the longer i've been in
this industry the more varied my work is
and actually the more i am paid also for
this election or work that i can do
because i am able to have a larger
impact by connecting dots from many many
different layers so again learning in
layers over the years i've definitely
grown my ideas of breaking illusions not
just about the the code but you know
whatever necessary so if we look at what
i mean by this then
i mean
that uh well definitely there's this
what i call basic illusions in in
testing
so we have that code and we're breaking
the code
and we might have illusions about the
code uh making a product in the first
place so we looked at kind of like code
doing what it's supposed to do not
having error messages or or actually
working in the cases where it's supposed
to this is kind of the core of what we
think when we think about testing but
that's not the only
basic illusion that we're breaking with
testing
the other
almost i would say equally relevant or
maybe in my role it's usually even more
relevant than finding these this kind of
this is where where it doesn't break
uh or doesn't work
is that sometimes we expect that the
product does something we kind of tell
make claims to our users on what kind of
things they get when they pay a number
of euros for the product that we are
selling them or the service that we're
selling them right now
and sometimes uh the expectations
and whatever we have ended up asking the
teams to implement don't match and we
are not aware of it so sometimes the
product isn't doing what it would need
to do and i think of this in terms of
you know omissions we are missing
features we are missing sub features you
know some kind of things that are
reasonable to expect that we would have
the easy examples of course on these
kind of features what it needs to do is
is it needs to survive the product that
we are creating it needs to survive when
we have users who make mistakes
if they end up not understanding what to
write in a field and they end up writing
two in letters instead of two in numbers
they should get a helpful error message
saying i don't understand doing letters
only numbers are allowed here so the
simple thing is kind of you know error
handling so product isn't doing error
handling that it's supposed to do or
would need to do but uh just as much it
might be that we're completely missing
out on some
functionality some kind of features that
need to be there sometimes even features
that someone mentioned we should have
but we didn't really go through
the list of all expectations
systematically so i spend significant
amount of my time in figuring out claims
all around some of them more
authoritative and some of them less
authoritative and clarifying what's in
what's out
are we disillusioned in terms of of what
we are delivering
and the third category of basic
illusions security related things
sometimes we have features that you can
use for bad things well it might be that
they allow you to break into the system
it might be that they
reveal data that wasn't supposed to be
revealed or it might be that they enable
use cases like harassment
that we definitely didn't intend
but someone also needs to think in terms
of the negative uh kind of misuse cases
that we might have around our projects
and all of these types of things are
those what i call basic illusions in
making the product that we really
intended to do
the other kind of illusions then uh the
more uh separate ones from the code
are kind of towards the ideas leading to
code
so the way we work together whatever way
of working we've agreed to have
sometimes it works better sometimes
worse
ideas around that are very typical for
me to address as part of my work
people their skills helping people grow
seeking help for people who are not
necessarily always asking for that help
themselves
uh
is something i find we hold a lot of
illusions around and the business models
kind of like making the decisions and
this is absolutely the thing we need to
implement right now so that we we are
doing the right things for our business
and our product and our company
so uh kind of going outside just
creating whatever was asked and being a
part of of creating the environment that
enables us to create the right kind of
systems
but let's look at couple of examples
first on the basic illusions
i leave
you kind of on this one with the idea
that i've created an entire course that
you can read
uh on exploratory testing foundations
that teaches some of these these basics
but i just kind of walk you through some
of the basic ideas of how this usually
works and i teach in terms of
contemporary exploratory testing meaning
test automation is part of the way you
do exploratory testing you can't explore
well without automation you can't
automate well without exploring because
otherwise you don't have the right
scenarios that will enable you to pay
attention to the possible things that
could be broken in the future rounds of
of your testing
so for this this course what i've uh
centered around is this idea that we
take just a very very small application
and this very small application it's a
good target in the sense that it's
really nothing more than what you see in
the screen right now
there's a link
which basically gives you a wikipedia
page where there's a specification of
how e prime a way of using english
language without using the verb to be
how that works what kind of rules does
it have it has these counters of how
many words uh uh
are there in total uh it counts
discouraged words and possible
violations and you have this this text
field and a prop button where you can
put whatever entry you want it to have
and my demo sentence here to be or not
to be hamlet's dilemma it nicely
shows all of the different features that
i actually often have to discover myself
it's not like anyone told me what
becomes a possible violation i have
learned by using the application and
having conversations on it that you know
it would seem like the possible
violations are things where a human
intervention
on on the inter um
on the interpretation of the the blue
word would be needed it could be with
the to be verb
like a shortened version or it could be
a possessive
and
the implementation isn't yet smart
enough to do anything other than
categorize it for
humans to to look at so very very simple
program
uh i've had a chance of seeing hundreds
of people test this so i see some people
know this that uh my
little
sample text here
the demo sentence it actually already
introduces a bug that's not nine words
that's eight words
so the the uh
the
apostrophe the the little character
there in bit not apostrophe but the
little character there in between the b
and hamlets it's counted as a word so uh
clearly the counting isn't the smartest
possible algorithm in in in this case
and we already have now here a sample of
how it might fail so
when you see that the counting can be
food some people really dig into the how
i can fool the counting and spend their
first hour on that
other people are really curious on this
color coding and the kind of the final
most representative
way for the user to see what's wrong or
what's right in their sentence
so they create for automation purposes
in particular they want to create some
kind of like
a logic a little piece of a a code
that would always know how to recognize
the red words and the blue words and
this
user interface is also created in a way
where it's not a very complicated
algorithm that you need to create but it
usually takes a few moments for people
to to write up something that works for
different combinations of having and not
having
the the blue and red words
in that that sentence so it might be one
of those traps where people start and
and they first kind of create that but
there's a more straightforward way for
testing with automation which is just
kind of looking at the word counts the
color coding uh
really doesn't
differentiate
from the the
word counts it's the same logic well
especially if you go and look at the
code on how it's been implemented you
can make your choices of how you want to
use your time based on that
some people
open the specification they want to
understand how the system works
so kind of like getting trapped into
creating all the different inputs and
some people start with let's put all
kinds of weird inputs into this text
field all of these are valid openings
and it's not just that
wherever we start we don't have to
finish there we can do all of these but
we'll make our choices of what we start
with
in exploring this in spending time and
testing this
there's a high possibility that you will
end up finding problems so i've had kind
of like documented some of the problems
here in various areas and since i have
already spent significant number of
hours with various people on this little
application in the end of my testing
i've been able to tell for the future
myself and whoever comes after me how it
would make sense to test this but in
order for me to give a very specific
strategy on how it is making sense to
test this i had to test it first so this
is not an input to testing it's an
output to testing and similarly since i
have already spent time exploring it i
also have a set of 16 test cases
created in automated parameterized way
and this is actually when you run it it
would reveal that there's 10 problems
that that just these tests
are finding the problems are not well
documented on this one
so definitely spending time with
something like this doing you know
breaking illusions doing testing you
find find some bugs some you know
specific examples that are not properly
recognized if you approach it automation
first
but also if you don't spend time just
you know looking at the application and
and and thinking in terms of you know
something outside the the basic simple
test case that i had documented in
automation you might miss many other
problems so
you go and you look for something that
the others might have missed with the
hope
that after
enough people in your team have gone and
looked for the things the others might
have missed together we've built
something that is relevant
so for me
what this basically is and means is that
you know i start by the heuristic of i
never ever want to be bored and i've
been a tester for 25 years and i still
haven't had a boring day
when i sense that i'm about to be bored
it just means that i am no longer
thinking in enough dimensions i've
allowed myself to kind of you know
drift into this rut and there's an
illusion in me that needs to be broken
this work is never supposed to be boring
if you're logging in with the same user
every day and you think that's boring
how about logging in with a different
user when you create a new user today
instead of using that user that you have
used for the last year every single day
maybe the new user doesn't work has
happened to me in real projects uh when
you log in with that user maybe the
thing you always do first maybe you can
do something different maybe you can
actively look for ways of not being
bored and maybe you can you know drag
someone in to pair test or ensemble test
with you in a group like having a group
of people when you look at things with
other people's eyes it is really
difficult to be bored and you are almost
forced to learn new things about the
software that you're testing
on the heuristic side i also you know a
lot of my uh examples
uh the the deliverables the strategy the
test cases uh they are uh the result of
the uh the testing being done and an
output of that testing rather than input
into that testing so in the beginning i
know the least and i should be paying
attention to yet another one of those
illusions
the idea that we already need to know
things and that we would know things
when we start or that we would try to
get to a place where we really know all
the things before we start we will be
learning while we are
trying to break those illusions
and if we have this learning mindset you
know every day when we come to work 52
days a week
or 52 weeks a year if we are one percent
better we're almost two times ourselves
in a year and if it is every single
waking morning that we approach things
with a one percent improvement seeking
attitude we could be you know competing
with our past selves to the scale of
almost 40 times better in a year
and probably you know it's somewhere
between these that you can try uh
getting to but there's a huge potential
in us being able to connect things in a
smart way and actively learn about
things that save us us a little time in
getting the the work done
and finally kind of on the heuristic
side on how to do this
uh well uh persistence helps a lot
uh alexanderbek one of my favorite
people in the testing field right now is
uh working around micro heuristics kind
of like describing ways how testers
usually approach things
and this poke it until it pops kind of
pay attention
notice something being a little
interesting
getting interested in that and then play
with it until you get it to reveal you
that things were not as you first
imagined they might be so be open to
that broken illusion
finally i want to give you a couple of
examples of illusions broken outside the
field of what we directly associate with
typical testing on the ideas leading to
code and i think these are
sort of in the category of this is not
what i would expect of a tester this is
something i would expect from an every
single professional working in teams
that we want to learn to figure out
where
the truth kind of lies within the ways
we work and and be better at improving
the the way we work
so i have collected some examples
on uh
illusions i've ended up breaking uh this
is by no means a conclusive list and i'm
presenting them to you today in order of
of appearance in my professional life
but it doesn't mean that they couldn't
appear in a different order for you
and it probably only implies that when
you look around at the illusions you've
ended up breaking the practices where
people believe this is not possible or
this cannot be done and yet you can make
it work and you can do it through
experimentation
maybe you'll recognize some similarities
there
the first example that i wanted to give
you is from a few work places ago
on contractual commitments
and us needing to build a new feature
and we had this
conversation that i've had over my
career
so so many times about this new feature
customer absolutely wants it it is
really critical it's business critical
it's something that needs to interrupt
everything else right now it is going to
help us you know as a product company to
go forward
all of the positive signs are there and
uh and yet we have this you know nagging
feeling a lot of times on the technical
team side that
maybe there's a slight bit of air in our
beliefs of how positive this can turn
so in one of these projects and one of
these features i made a proposal for the
business people that maybe you know if
we believe so heavily on this bringing
us the numbers that we were looking at
maybe that particular customer the main
customer wanting that feature
maybe we could already be writing that
contract for the first few percentages
of money
at this point before we start the
feature at least you know it would serve
as a great motivation for any of us in
the team who sometimes you know might be
a little you know worried that we are
building yet again the most important
thing
and the reality uh on the most important
shows to be different
in in hindsight
so in this particular time in this
particular project we ended up actually
writing that contract
and and proposing to the customer a
small percentage of of whatever they
they wanted to
uh or we were
assuming we would be getting out of
building that feature when they now want
to kind of you know expand the use of
the product in their business only to
actually learn that the the response to
that contract was that
they wouldn't be signing it and they
were actually expecting that it wasn't
going to cost them anything extra so
breaking illusions or something where we
would have easily spent entire few teams
time on implementing something for next
six months
getting that kind of
removed from the agenda or approaching
it with a lot more realism in in how
much money it's gonna make with the
short time investments just playing with
the idea of uh let's ride a contract up
front
uh
uh that test case is probably one of the
the best ones i've ever ended up
implementing
outside the the immediate uh
product uh team area
uh and having a significant impact on on
whatever we were building building in
the in the team
so you could you know try experimenting
with test cases that are not in the
regular realm
another thing that i've tried over the
years is ensemble programming
so you might have heard about unsample
programming sometimes also referred to
as mob programming i really prefer
the the little less
violent version of the the term
and
the idea with ensemble programming is
that we have a single computer in use
for the entire team
and we are all programming together
by
one of us
being the voice of the team one of us
being the hands of the team
and the rest of us using our voices in
in kind of co-navigating co-voicing
through the the person who's making the
the main decisions and switching
regularly who's in each of these these
roles
for me this was an experience of
learning a lot about programming
learning a lot about how i could impact
with my testing ideas a programming team
in the moment and how i can make people
forget expensive mistakes ever happening
because we get correcting to correcting
them in such a short time frame and for
me uh the idea of
well cognitive dissonance as in
changing my whole history on remembering
that i have been a programmer well
pretty much
since my teenage years when i i was keen
on writing games
was something that kind of you know
recently centralized my my ideas around
what do i do for my work
teaching me practical hands-on skills so
definitely breaking many illusions on my
side but also on my team's side on the
ideas of what i can and should be doing
and what are the benefits of that
another example that i wanted to share
with you is from my previous place of
work so not from where i'm i am right
now is uh the the experiment we did
around the phrase no product owner so if
this is something of interest to you
there are uh presentations that i've
done a few years back on on this topic
but what we basically did is we agreed
that our team of developers no longer
had a product owner the product owner
would only go fishing for customer
feedback
all the decision power all the the doing
power all the prioritization power was
within the team and the product owner
would
not actually be actively
part of that
would just kind of look at the demos
like other stakeholders and within a
year we ended up improving multi-fold
and being quoted as the best team in
corporate r d a lot of people think this
is probably because we were seniors you
know i had many years many other people
had many years in the industry but it
was actually the sense of ownership and
the 15 year old
with the sense of ownership was working
exactly the same way as some of us
who were much more with a
number of years
on the on the plate
but together us kind of feeling like we
are not being uh ordinary we are
actually active players and we get to
break our own illusions together we
really did wondrous things for that that
year together and it has continued as
far as i have heard from the team since
i left that particular team
another example
is on making shorter releases this is
maybe nowadays my signature move i join
a team i look at how long does it take
to release
and release by release we work towards
driving down the time to release i just
in the end of last year left the team
where we went from 32 days to uh from
the moment when we had everything
together having the release available
for the customers so quite a long
testing period to two days
where the testing period was less less
than four hours in that two days
uh leaving that team again continue
without me
and now moving on to my my current team
where my my current experiment of trying
to change the world
is around clarifying uh story uh accept
stories acceptance criteria uh the way
of understanding scope so that we don't
again create those ordinaries
and we end up giving very specific
automatable examples
with
scoping so that we maybe learn to be
very specific about what we expect that
works after those changes that we are
right now about to be making this is my
first time trying to do bdd so i'm
definitely still learning about this so
i'm finding that i have still many
illusions to break one of them being
that it seems that when i do my best in
finding that acceptance criteria in less
than two weeks away from the time when i
will be testing the same same thing
about 75 percent i can find in advance
but 25 of the acceptance criteria i will
find when i look at the application
and it works as my kind of external
imagination
it whispers me you would want to try
this
and i get to also tell myself how badly
i did my best work just few weeks ago in
trying to list all the different
criteria
i am my better self as someone who is
breaking illusions when i'm looking at
the product when i'm looking at the api
when i'm looking at the code
and that serves as my external
imagination
as long as i allow myself that room that
breathing space to just look at it and
listen to it and think of what would i
do differently now
a few days older and wiser hopefully
getting to
not obey even my own rules but uh break
whatever is is necessary so that we
serve our customers our users the best
possible way
so instead of uh testing maybe you know
you want to use different words i'm fine
with that maybe you want to talk about
examples maybe you want to talk about
experiments they're pretty much similar
to the type of things that i talk about
when i say testing
so all of these these ways of framing
things are are fine
and while this is something that is a
big part of of my professional identity
as a tester i am finding that my main
colleagues developers uh definitely
product owners as well are just as much
into the space of of breaking illusions
with testing and i find that in modern
agile teams the people are used to
recognize as test managers of the past
they are now product owners and we're
actually working on the same kind of
information and disillusionment
type of work
uh just from little different angles
trying to create a fuller picture in in
this whole thing
so to conclude
i love testing i think you should love
testing too
there's techniques design techniques
that you can learn there's approaches
heuristics that help you think in the
right way that you will enjoy and never
be bored with testing
and the assignment
on this one is we go all of us
regardless of our role define some of
what the others may have missed
and never ever be bored
when we're doing resultful testing
thank you
[Music]
do
[Laughter]
[Music]
you
