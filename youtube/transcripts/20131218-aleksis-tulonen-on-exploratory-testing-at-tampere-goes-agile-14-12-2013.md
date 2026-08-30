---
title: "Aleksis Tulonen on Exploratory Testing at Tampere Goes Agile 14.12.2013"
video_id: n5Q2-bcpNLw
url: https://www.youtube.com/watch?v=n5Q2-bcpNLw
upload_date: 20131218
duration: 12:17
channel: Maaret Pyhäjärvi
tags: []
---

# Aleksis Tulonen on Exploratory Testing at Tampere Goes Agile 14.12.2013

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

and i will be talking about exporter
testing
because time is limited two first few
words about myself i work as a software
dustingconsultant.comic
which is located in helsinki
and i'm also founding member at
international society for software
testing parlini organization is trying
to advocate skillful testing
that's enough about them if you have any
questions afterwards come talk to me or
just use google
then i also want to thank michael bolton
and james park i had some conversations
related to this topic and they helped me
a lot so just let that be known
now
before we are talking about exploratory
testing we need to be talking about
definitions and by definitions i mean
the definition of testing and the reason
for this is that because
my understanding about exploratory
testing is highly based on how i see
testing
and also when i'm talking about testing
you will understand what i mean
and this is not the universal definition
not the one and only but i can find it
reasonable for me testing is
experimenting with something in order to
evaluate it
this could be saying experimenting with
the product in order to evaluate it but
i don't want to restrict your thinking
to something concrete like already
written software
because we can test ideas from the
moment there's the first idea about
product
we can test it
important part about testing is
evaluating when we're making experiments
and receiving information if we don't
care
what that information is we're not
judging it
then in my my opinion we're not testing
we need to be some kind of
way evaluating the correctness of the
behavior
now
testing is what it is but there can be
different missions
most common mission behind testing is
i'm just trying to find important bugs
but there are others for example when
there's let's say i'm testing a web
portal there's the first build of a web
portal
at that point i'm usually not trying to
find all the important parts instead i'm
just trying to see if it can work is it
festival
i'm experimenting with something in
order to evaluate it but there's a
different mission behind it
now
the experiments can be boiled down
basically to asking what if
what defines at -1 to this field what if
there's a user logging in who doesn't
have any privileges
getting the answers that remain requires
all sorts of skills if i'm asking
what if there's 5 000 users trying to
log in simultaneously whatever the
simultaneous means in this i probably
need different skills
compared to when i'm asking what if i'm
using the minus one to some specific
field so we need skills or we need
people colleagues who have the skills to
find out the answers
but then you also need knowledge
to bet so you can even ask the questions
knowledge about technology
business domain users
only then you can ask the questions
about the what if
what should happen
now
basically it's boiled down to this
this is one of the reasons also when i
go to a project i try to learn as much
as i can
everything about everything in the time
i have available because then i will be
able to ask those questions
it's also good to understand that
testing is about mental
when i'm
evaluating the test process i'm
evaluating the mental process of testing
what happens on the keyboard
what documents are written
that's important but there's some kind
of thinking behind that
and when i'm trying to become better at
testing i'm trying to become better at
that mental process of thinking
all kinds of ways that users can
interact with our software
just remember the mental engagement when
we move to exploratory testing
now
exploratory testing i like to define it
as an approach to testing that
emphasizes tester's ability to explore
an unknown object or space through
concurrent test design and test
execution
we can leave the concurrent out of here
for now
and focus on the first part
now exploring traveling through an
unfamiliar area in order to learn about
it when we ask the questions
get the answer
or the information and i will evaluate
it
then we are learning we are exploring
now there's a wonderland approach
because exploratory testing is an
approach it's the way of looking at
testing from a certain angle
and from this angle
we're emphasizing destro's ability to
explore
now i've also underlined testers because
don't confuse this to a role of a tester
i'm talking about the person who is
testing and that can be anyone in the
team because exploratory testing is not
something that is restricted to only for
the parents of people who are considered
testers you will learn more in few
slides
okay there's other definitions and i
really want to mention this freedom and
responsibility this is longer definition
like cam kaner
and
there's one part emphasizes the personal
freedom and responsibility of the
individual tester to optimize the
quality of his or her work
if we are given the freedom to think
freedom to approach the testing problem
as the best we see
then we need to honor that
responsibility by optimizing the quality
of our work
continuously
basically this can mean if we're
doing some data comparison
and we could be doing it a lot faster
with the tool that we have the skills on
then we should probably do that because
it's our responsibility to optimize the
quality of our work
or if we are testing with the test data
that could be improved
so it would give up give us more
information about the product then we
need to do it of course we will consider
the opportunity cost
but it will take the time away away from
something else but we need to have this
process thinking process
now i think this is related to what
brian marrick one of the authors of
agile money fester has said at the end
of each iteration each team member
should be able to say why she is worth
more money to her employer than she was
at the beginning
this is from a paper called two
for cotton agile values discipline and
skill i have to link later
and
this applies to exploratory testing we
need to optimize the quality of our work
continuously
so we will be able to explain why we are
more worth money now than we were a
month ago
i mentioned earlier the congruent test
design and best execution part
i think this is a powerful metaphor for
that
brett victor has this essay called
learnable programming where he's
describing
what what are the good elements of our
own programming environment
and this explains the congruent test
design test execution well i will read
it because this is important in two ways
most musicians don't compose entire
melodies in their head and then write
them down instead they noodle around on
an instrument for a while playing with
patterns and reacting to what they hear
adjusting and sculpting
an essential aspect of painters converse
and the musical instrument is the
immediacy with which the artist gets
something there to react to
economist or sketchbook serves as an
external imagination where an artist can
grow an idea from birth to moderate by
continuously reacting to what's in front
of him
now
when i'm testing
i get an idea what if
then i'm interacting with the software i
observe how it behaves i'm reacting to
what i see
you could say that the product is my
external imagination i cannot come up
with the best ideas only on my head i
need to interact with the software
and through that pros continuous process
loop kind of process i get that to the
point where i have a really good idea
what is a
major threat for our product
now i said two ways this is two ways
important because
lately i've been
i've been lying trying to learn python
on code academy
and natural part for that is just
creating functions
so
when i'm trying to create a function
with the most simple argument
most simple
way i'm
writing a piece of code which will
hopefully make it i run it i observe how
it behaves maybe i made some adjustments
then i run it i observe okay now it
works with the most simple argument
then i think i'm reacting to what i see
uh
what other arguments could be
problematic for this function
maybe i add an alif
there and then i
check how it works with that argument
again i'm observing how it behaves i'm
reacting
and continuously trying to make the
function better
i think
we are exploring we're asking questions
we're learning
and we're also evaluating
we're putting some kind of judgment on
the correct behavior of the function
which means we are exploratory testing
while creating a function
and this is important to remember
now
summarizing
exploration freedom responsibility
mental engagement experiments
so what what's the big deal why am i
talking here today
one of the big reasons is
that most bugs are not obvious
they're not out there in the open
they're not phoned by following a script
or walking the happy path
they hide all over the spaces that tend
to be big
if we want to have chances in finding
them or preventing them because we're
thinking often they are bugs in our mind
as laura kosovic was telling earlier
then we need to become good at exploring
and the process i'm doing
often on the higher level
can be related also in the code level
because that's also exploratory testing
if you can relate to earlier metaphor
that's why i'm here today
okay there's all sorts of
sources of information here
here's also the leprechauns of software
engineering fellow rappers await which i
totally recommend that everybody will
read
because that will change your thinking
towards
anything that is said to be a fact
statistic
you will search for data after that and
think about the truthfulness of it but
there are others
if somebody is familiar with lego
mindstorms
there's a book mindstorms like monster
storms was
named after this book
and
according to brett victor this book is
the best book about learning
i don't know i just started reading it i
have it with me if somebody wants to
check it out today
all kinds of different sources that i
think have helped me
better coming better at exploring and
asking the questions
now is the time to discuss
