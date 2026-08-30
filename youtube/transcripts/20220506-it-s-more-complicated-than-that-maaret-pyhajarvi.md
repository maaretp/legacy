---
title: "It's More Complicated than THAT - Maaret Pyhajarvi"
video_id: 5lm-zZsNj6k
url: https://www.youtube.com/watch?v=5lm-zZsNj6k
upload_date: 20220506
duration: 28:11
channel: Sauce Labs
tags: []
---

# It's More Complicated than THAT - Maaret Pyhajarvi

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

it's more complicated than that
these are the words and pretty much also
the emphasis
that i find myself saying a lot of times
at work and it's
a relevant enough sentence for me to say
that i needed to also reuse that as a
talk title in order to explain you the
work that i do
that i call export retesting
hello i am maret i am a tester and i've
been a tester for 25 years
i've also used other labels to describe
myself just to avoid some of the the
misunderstandings around what testers
are
i'm also a polyglot programmer
i'm also a manager
but i do gravitate towards the
enjoyment of looking at an application
having it be my external imagination and
kind of whispering to me where the
problems might lie
and helping my product development teams
in that role build the best possible
products that we can
i have skills or well i do have skills
in being in multiple different kinds of
roles and i could be volunteering for
all kinds of work within my team
but my
time isn't endless it's fairly
sufficient to do the work that i'm
supposed to do as a tester and even
after 25 years i am not done learning
about how do we actually insightfully
find all the different kinds of problems
because it's always more complicated
than that
my work as a tester
or pretty much anyone's work when they
are doing testing in the in the team
is to go after someone else and find
some of what the others may have missed
the someone else might be you yesterday
if you are testing your own thing
or it might be someone some other
developer in the team it might be a
different team
that you're interfacing with
but the assignment of testing is pretty
much always this you're supposed to find
something that others may have missed so
far you're supposed to find new
information
and there is never an answer key to all
the bugs there's this amoeba of of a
system uh
a lot of unknowns some of the things we
think we know
but we have no answer key to all of the
bugs that if you report these bugs
you're gonna be
doing a good job in that case we have
various kinds of taxonomies available in
the field that we can go and consult but
none of them will specifically tell
what's going wrong with our application
so it's always kind of like a puzzle a
little bit of an investigation to figure
out what things we have already done and
what is still valuable to do
one of those examples of doing something
on top of
things that have already been done is
this quote that i've put here on this
very same slide
from a developer whose application i was
testing
he mentioned in a podcast interview
exactly these words that that it was all
written test first actually also it was
written in a pair programming fashion
and it was code that they were very
proud of and i went in spent some time
on it and basically destroyed it in like
an hour and a half well it wasn't really
an hour and a half i would think i spent
more like four hours with that
application i did some interviewing to
require to understand from the developer
what is kind of like a listing of all
the capabilities he thinks you can do
with that application because that
didn't exist in documentation i i took a
look at some of the documentation that
was created to understand what i could
get from there i set up a test
environment that was realistic and spent
some time exploring uh the
functionalities like i would imagine a
beginner
user
just would someone who would understand
anyway the purpose of the application
and have the basic knowledge
the destroying it in like an hour and a
half well the software was already
broken when i got there so i didn't
really destroy it i destroyed maybe his
illusions around the application so
that's what testers do by providing
information we destroy the illusions
that we were holding
and this whole test first pairing it
really creates a strongly held illusion
sometimes that it's all there is
to look at things and it's always more
complicated than that
so what i want to do with this talk
today is to show you three examples of
test targets
and how it was more complicated than
first meets the eye and i hope those
examples
give you an idea
of how you could
test
with the mindset of it's more
complicated than that
and do a better job to provide the
results
some of the information that others may
have missed so that you in your teams
can do a better job testing uh overall
so the first application uh is a login
so you've probably all of you i would
imagine have at least run into a login
even if you hadn't had to build one from
the scratch
and running into login you have ended up
testing it at least you know
unintentionally by logging into the
system
uh the
intention of actually going about and
testing that's what makes it more
complicated so when we go with intention
we can just kind of like start creating
some kind of a listing of things we
would want to test and definitely the
positive cases kind of valid data is
something and then we have all kinds of
invalid cases invalid data that we could
also be trying like varying the
passwords varying the user ids and we
can
create documentation about this in a
very detailed manner
i haven't been in a project that has
done this detailed manner of
documentation for years
but we could be theoretically creating
that this example is from a course that
i was teaching in the early 2000s
and
right now if i would write a test case
myself
a
to leave behind for documentation that
wasn't automated
what i would probably do is is just
write login and it could be anything
between four minutes and and four hours
or four days that i could explore around
that particular thing so testing by
nature doesn't include the depth of how
far we go
with our testing
the four minute test is a test the four
hour test is a test and the four day
test is still a test it's still doing
some testing but we would definitely
expect that we have more chances of of
uh discovering information we didn't
have if we spend a little bit more time
i wouldn't create
documentation
that style but i would maybe create
documentation in this automation style
so it makes sense to me to
think in terms of you know taking
examples from the robot framework
community
uh writing a login test case a positive
test case that just logs in and and and
make sure that everything is fine after
that and already this positive test case
we can use it over time continuously
we can use it for various browsers so
that we never actually have to manually
so-called login to some of the browsers
to see that the login basic things they
work
but obviously it's limited to seeing
whatever the computer is capable of
seeing so whatever we are checking with
our test case only that uh gets checked
but depending on how we think about the
the risks around the different browsers
it already might be sufficient and we
could also of course document on the
same level as on the left hand side we
could document also the negative test
cases and run them kind of continuously
these examples around login have been
around so long that i have shared them
many times before
but it is again more complicated than
that there's more than the positive and
the negative test cases even if that's
how we often still talk about around the
the concept that we teach to to new
people in testing and when i was last
testing login
i needed to do quite many different
things around that login
i explored
kind of
harvesting ideas from within myself
googling maybe using previous projects
previous experiences a listing of
possible problems that i might find
anywhere online
having conversations with the team
and i only documented not all the ideas
that i tried because we did spend
actually weeks testing that login not
hours or minutes but weeks testing the
login i only mentioned the ones that
were successful in discovering
information that was new
complementing functions was this idea
where you know if you log in you need to
be also blogging out maybe well it did
lock you out at least it looked like it
but it only pretended so you were
actually still in the system
performance while it did lock me in it
took its time and when combined with
concurrency it really took its time
so adding more people into the system
definitely had a major impact on their
logging performance
sessions session lengths kind of related
to logging out in many ways
but they were very fascinating symptoms
of of combining
uh session uh
information on the computer with that
login and and trying out the next day
logging in when you weren't supposed to
and seeing problems with that
with security controls we
basically forgot that
customers our users might be forgetting
their passwords and we needed to address
this on the side then of the the start
of the production
that definitely yes passwords
uh are also going to be forgotten and
that the decision we made in in not
having it available wasn't the right one
even though we did make it
multiple users had trouble
combining with browser functions and
password managers had trouble and the
environment while it worked in one it
didn't work in the other
and it turned out that it took us
multiple different environments before
we were able to nail down properly all
of the different environmental aspects
that we had around that that login that
needed to be discovered
so i thought you know in many ways that
having
explored all of this stuff doing
exploratory testing with the team and
not just taking
a login at face value of success or
positive and negative test cases we
would have done already a good job but
it turns out that looking at production
we didn't yet
so we had some of our test automated
test cases running the login test case
running as a monitoring case in
production over a longer time period
the data retention policy doesn't have
all the data available so i have only a
limited time frame that i could take a
screenshot from here
and you can see that
97.15 is definitely at least well it's
not the level of our internal aspiration
of how reliable login should be
and looking at how it really behaves in
production it gave us the extra
information around
the third-party dependencies that we had
around how we implemented login and how
we could learn to react to those
third-party dependencies in a better way
even if it wasn't our parts that were
failing the user's experience overall
isn't as good as we'd like it to be but
then again also this is a system where
97.15 is is good enough so we haven't
had a single customer actually
complaining about this yet
i would expect that comes with growth of
the business on the product rather than
an immediate thing so testing in
production
is also part of it's more complicated
than that whatever that we first
imagined
so
testing for me it's kind of like this
work where you have these tails you go
back to production you you look at
things from the customers point of view
make sure that you have the customer
information they might not talk to you
you might actually have to need to have
some kind of observability
functionalities
in your products
uh but going back and looking at those
kind of information that's a relevant
part of how you would think around
testing in order to provide the results
that overall you're you're trying to to
get to
so that's one example the second example
that i want to share with you on it's
again more complicated than that is from
a course that i've been creating where
the basic idea is that we take a simple
application
and we try to do testing the best
possible testing on this particular
application to do the best results we
can to leave behind test automation
that we can
and and just basically do a good sample
of what would good testing look like in
a project and teaching how to do that
and i call this approach contemporary
exploratory testing basically for the
idea that i believe that automation is
part of exploratory testing and i do
realize that's not the way everyone else
is thinking in terms of exploratory
testing
the e-primer application it's a very
simple application that tells you
whether you're writing proper english
according to rules of e-prime and here
this
screenshot is already from a text that
is a really nice and easy uh sample
one that wasn't given to me when i
started exploring this i needed to kind
of figure out what i would want to use
as a good example and this is good
example because it actually already has
a bug
it
shows
illustrates nicely the different
functionalities that we have here so we
have the red things discouraged words we
have the blue things the possible
violations but it also shows a bug that
it doesn't calculate the word count
correctly
and what i see when i have tested this
with multiple people over the globe in
both paired and ensemble settings
i've had some tens of people spending
time with me on on testing and learning
with this application trying to figure
out how we could teach testing and how
we could learn testing with this kind of
an application and when we see that bug
it's kind of like a trap a lot of times
for the people who are doing testing and
seeing that that problem because when
you see a bug it kind of says there's
more bugs wherever that bug was there's
a
heuristic on that
idea and you might find yourself that an
hour later the only thing you've tested
is the word count which is a secondary
functionality compared to the purpose of
this application which is to identify
the violations against e prime
e prime rather than just counting words
you have other applications for for word
counting so maybe that's not the only
thing you should be focusing your
attention to
if you start with automation i call this
idea the the test automation is gambit
so you open your game with the idea that
you're already creating automation
while you're exploring from the first
moment it's your way of documenting it's
also your way of extending reach
it helps you track what you've done so
instead of writing those those
traditional notes of what you've been
doing maybe you can already write your
notes in in the format of of test
automation it works for certain kind of
applications better
especially if you have an api that
you're exploring a brilliant way of
exploring an api and a simple
application web application like this
also works really nicely on on that
context but the algorithm kind of the
idea that if you want to create
something where the automation always is
able to verify that colorful
multi-colored text there
it requires some logic that you need to
create it's not a fail very complex one
but again if you think in terms of maybe
you had only that hour it's very easy to
use that hour in creating and testing
the algorithm
if you click the link first sometimes i
see people doing that
and i find them kind of falling into the
trap of test cases
behind that link there's plenty of
examples of what is e prime and
systematically starting to go through
every sample there can easily take your
attention for that one hour and anything
outside that given specification you are
then completely blind to it and of
course then the fourth trap that i see
people fall to is the data of test uh is
the trap of test data this is
particularly one that i see testers
falling into professional testers in the
sense that there's this idea of trying
all kinds of error scenarios the
negative testing it's strong in the
community for some reason and it's
actually not the most important thing
that we need to usually do with the
application that's a bit old-fashioned
way of thinking about testing and then
trying all kinds of weird inputs here it
is definitely helping you find all kinds
of weird things that might happen but
you might end up with an hour
where you don't know anything about the
real functionality or any of the
problems that anyone really would care
for in this this application
so i use this as an example just to show
that you know again a very simple
application it's again more complicated
than that so even if i give people uh in
the end of the course i usually give
them this this listing of all the bugs
that we have found by various groups
still with that answer key to bugs now
it's easy to find them people can make
this comparison of well we didn't find
this i didn't consider that and usually
it's about half of these that i see
people
able to find
with this application before they're
ready to quit so our bar for what's good
enough what's results for testing i find
that it's often way too low so it's
always more complicated than that
it's not just the results in this way
it's also results in terms of
documentation we are very easily kind of
ready to say that you know it's a simple
little thing
we don't need to leave any documentation
behind so instead of creating a test
strategy in the beginning of the project
when you start testing something
i think of this strategy the ideas that
are guiding my test design or something
that emerge while i'm testing and i'm at
the at my very best of documenting them
by the end of the project so just a
sample for you and the test cases that
i'm running as i am coming up with
things that i want to test and i'm
finding problems maybe i could create
already automation that i can also leave
behind
even if it guides my focus uh to certain
types of bugs and makes me miss other
kinds of bugs
since it's more complicated than that
it's always more complicated than that
it's not this or that it's not
automation or
attended exploratory testing it is a
combination of these two and we don't
need to separate these two activities
into two different people
unless we have uh the missing skill in
in one of these people and i see a lot
of cases now in real life
uh projects where automation people
don't know how to test
and exploratory testing people don't
know how to automate and contemporary
exploratory testing for me means that i
am actually actively trying to create
people who understand that more
complicated than that also includes the
idea that we can and we should grow
into better professionals in
intertwining these activities into a
modern approach to exploratory testing
the third example that i put here is
from my my project right now so i wanted
to just show that this also runs with
not just uh
examples in uh in in courses
uh every single project that i end up
with i could give you a similar example
this is a really simple one where
there's a location of an airport that we
could configure if we configured
realistic airports like chicago o'hare
airport with specific coordinates
with a specific precision and negative
and positive combinations
we would get a 500 error from the back
end and not having a functional system
and when i'm asking other people kind of
how to test this how would they approach
this
uh unless they use the application as
their kind of external imagination and
others they encourage themselves to use
more than a couple of minutes
of time on really understanding what is
it that we might be missing as
information they miss all the things
that are more complicated than that and
we needed to fix actually uh multiple
problems around this
as i started changing the defaults and
going through the different realistic
scenarios that we have in the production
no crap no uh you know error cases no
weird entries the negative testing as
such because that is really not the most
relevant thing for something
that only an admin with certain
information can go to but even the
positive cases that's more complicated
than first meets the eye so that we can
discover those problems that we needed
to and and fix them and maybe we can
again have automation left behind that
helps kind of understand what we tested
and run those tests later again
so all of this leads to this concept of
contemporary exploratory testing
and i think in terms of contemporary
exploratory testing and resultful
testing because i find that way too
often when i look at some of
my colleagues
and some of the the environments they
end up working in where they they are
somehow encouraged to do not the best
job they can but the quickest job that
they can they turn into this kind of
people that are kind of like a clock
that is right twice a day you know even
a broken clock is right twice a day so
we need to actually spend a little bit
more time in thinking in terms of what
are the results that we're expected to
create and are we really doing a good
enough job
as
of now with the approaches that we have
and could we try doing something more to
at least assess whether the work that we
are doing right now is good enough
i would expect resultful testing to
include both automation and that that
kind of attended testing
attended testing and unattended testing
they support one another i would really
hate to talk about manual testing
because there's no such thing
as manual testing i don't really think
there's such thing as automated testing
either it's very manual work to create
that automation and think in terms of
what do i put in that automation but
it's kind of like a design of that
elaborate spiderweb that makes sure that
we have that lunch available
and we have that kind of network of
noticing and going and attending to
things when when they might require that
because of the changes there will be
holes and we'll be looking at those
holes we'll be seeing those holes we'll
uh
put some attention specifically to those
holes and we can always go around
especially when you have an ecosystem a
system like this you can always go
around and never hit that that network
so uh looking at it from the perspective
of our customers is a relevant thing for
us to
do to build that spiderweb we are doing
resultful testing we are wanting to
catch information with this awareness of
coverage
we want both the good results and we
want also those results to be repeatable
because test results are like milk
they get sour really quickly so we need
to be replenishing them automation is a
non-negotiable in a modern way of doing
exploratory testing or testing in
general but we also want to find all the
relevant bugs and we want to make sure
that we are aware of opportunity cost
that we are making those choices of
where we use our time
and we need to make good choices good
and balanced choices on on those aspects
for me the traditional way of thinking
about exploratory testing is this idea
that you know you separate this this
maybe automation or manual testing
whichever you want to think in terms of
writing and executing test cases and
then there's this thing that you do on
top of that that still exists in many
projects but what i try to do in my own
projects and what i was describing in
these examples is the so-called
contemporary way of exploratory testing
where test automation is actually
embedded inside this this whole work
that we're doing because what really
matters is that when we are doing
testing we go
and dig in deeper to find some of the
information that others may have missed
and we are supposed to do a good job and
it requires that we are never bored
and we should never be bored because we
are always building new things we are
taking things forward and with changes
we can find that motivation of go and
explore deeper every single change that
we are making kind of following the
developers on how they're making their
changes following the environment on how
those changes are happening
and what eventually matters is what our
customers experience we want to do
resultful testing and it's always more
complicated than that
