---
title: "Intro to contemporary exploratory testing: A demo session | Maaret Pyhäjärvi from Vaisala"
video_id: CQTuI5y2NFI
url: https://www.youtube.com/watch?v=CQTuI5y2NFI
upload_date: 20220617
duration: 1:00:43
channel: Codementor
tags: [codementor, developer, programming, coding, mentorship]
---

# Intro to contemporary exploratory testing: A demo session | Maaret Pyhäjärvi from Vaisala

> We often don’t do a good enough job at manual testing and testing automation in our projects to obtain the results we seek. This is when contemporary exploratory testing comes in, where developers can put learning in the center. In this talk, we will demonstrate with an application to see what happens when we combine testing done and automation created.
> 
> What you'll learn from this talk:
> • “The Automationist’s Gambit” - making sacrifices to win more later in exploratory testing
> • How to do more than regression testing with automation
> • How attended vs. unattended testing is a better framework for resultful testing
> 
> 🔗 Link to the event page
> https://www.codementor.io/events/contemporary-exploratory-testing-ekwhhkyqkg
> 📆 Next event: How to start building serverless applications on Azure
> https://www.codementor.io/events/start-building-serverless-applications-on-azure-ei5arisaka?ref=youtube
> 💻 Find a coding mentor
> https://www.codementor.io/
> 
> Timestamps:
> 0:00 Introduction
> 4:38 Audience-driven testing & demo
> 31:58 Complete list of tests & 4 common traps
> 38:20 Summary of important concepts
> 46:14 Q&A
> 
> ---
> 
> Follow Maaret on her socials:
> 🐦 Twitter: https://twitter.com/maaretp
> Portfolio: https://maaretp.com/
> 
> ---
> 
> 👋 Stay connected with us on social:
> Twitter: https://twitter.com/codementorIO
> LinkedIn: https://www.linkedin.com/company/codementor/
> Facebook: https://www.facebook.com/codementor
> 
> #Developer #testing #exploratorytesting

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

Yes,
uh uh
I've been doing testing for 25 years,
and I find that the work that we end up
doing is sometimes
a little difficult to explain in the
sense that uh there's kind of like if
you imagine this answer key to all bugs,
this this idea that you have a list of
all the things you'd like to find, and
you could get it in writing, that would
be great. But you never get that answer
key to all of the bugs. You always only
get this kind of like you can think of
it like an empty paper that you're
supposed to fill uh with the right
information so that your customers don't
have to test for you and fill that paper
with surprises that take too much of the
attention and create too much friction
between you and and the customer.
And uh I've been doing this pretty much
well uh my entire career uh working uh
in development teams, in product
development. And uh I find that uh what
I often end up doing is maybe best
described with uh words of my current
team and and they're developers.
In in the sense that just couple of uh
days ago they were telling me that uh we
wouldn't want to be recruiting a tester
at all into our team. What we want is is
them, every single one of us, to learn
to to get that uh answer key uh
fulfilled, uh filled in. And uh
that the invitation is for me to teach
them to be brilliant testers, and then
going and and sharing that somewhere
else.
Uh but
uh in order to do that, I wanted to
today kind of like just go in a on a
very practical level on a real
application.
I I can see Lydia who was there in in
audience, and she's seen this
application before, So, I I know that
there are some people who've kind of
like had some experience with this. So,
I'm I'm kind of relying on you also on
on on helping me with some of the good
ideas. And I'm pretty sure that even if
you haven't seen this before, we can
come by with with some of the ideas.
So, the idea here is we have that answer
key to all of the box that we're
supposed to fill. And in order to fill
that, we need to fill that empty paper.
So, we have an application. It's in
production. It's been created for
testing purposes
by Alan Richardson, a UK-based person uh
uh doing all kinds of teaching
activities.
And I chose originally this application
based on the fact that he was saying
that it doesn't have much bugs. It's not
very bug
full in in that sense. And when you
don't when you have an application that
supposedly works quite nicely,
uh you get to use a lot of your energy
into trying to figure out what it does
and how would you know if it actually
fulfills those promises, and you don't
get kind of derailed by all of the
different problems that you you can
sometimes see. And especially in modern
teams that I work with, I would expect
that I don't see a huge amount of bugs
all the time. We're doing small
incremental changes, and not everything
breaks. Uh we usually have test
automation in place uh that is from our
previous rounds of testing.
And it helps us kind of keep this
baseline hygiene level of of quality.
So, that's kind of what I would expect
uh from this application.
And uh
to test this application, we would need
to use it.
So, my question uh to you uh is how
would you test this? You would need to
choose something
to put into the field. You can see I
actually already run it once I'm showing
it to somebody else.
But you would need to put here something
on on this text field so that you can
start seeing it in action. How would you
go about testing it? Write in the chat
some of the ideas of what are the first
thing that you would personally want to
do.
I'll just move back to the chat window.
Some ideas on how would you test this?
What would you put in that
in that window?
Oh, you can't see my screen yet. So I'm
actually doing a bad job in my demo
sharing my screen. Now you can see it.
This is the application.
How would you test this?
What would you write here?
What could you try?
So I can see some faces looking at
things
as in kind of like
trying to figure out what it is.
Click the button. Definitely is one of
the first things you could consider
trying.
Special characters sounds very tester
type of a thing. We haven't even seen it
ever work and we're already kind of like
attacking it with something that we
expect that might be causing trouble.
Maybe something I would leave a little
bit later. Extra long text similar thing
kind of like maybe see it work first.
No text at all. Just clicking the
button.
Trying with some simple words. Submit
and see what happens.
Figure out happy path.
Check the implementation. Maybe the like
awesome ideas. Like we have so many
things we can do all of it at once.
Uh,
maybe uh, discouraged words. We don't
really know what a discouraged word is
here yet because this is a new
application for us.
Uh, and someone on the window is there,
uh, Lydia, clearly reading the the text
that uh, maybe you could try the verb to
be because there's some instructions on
on what the application is is kind of
supposed to
supposed to do.
Uh,
I'm definitely all for the last actually
option here. Open the dev
tool uh, tools and and see what it it
has eaten.
Uh, there's no reason we should be
exploring blindly ever. Uh, we can
always look at things. Uh, we can see
uh, the sources here.
The whole code is here so we can read it
if we like to.
And uh, you can probably actually see
here exploratory testing want to run it
on your own computer
while you are looking at what we're
doing here together in the demo session
today, you could also do that to figure
out uh, things that you like.
So uh, we have a lot of options and I
think uh, the option that I I like well
in addition to just kind of like looking
at this this uh,
uh, code here, looking at if there's any
errors or on the the console. I like the
idea of just seeing it work. And this is
where I want to do not traditional
exploratory testing but what I call
contemporary exploratory testing uh,
with automationist gambit. So instead of
ever allowing us
uh, to write anything on the user
interface here,
I want us to drive this with automation.
So, there's no reason whatsoever why we
couldn't be writing automation as we're
exploring, and that way we are
continuously writing very detailed
documentation of the exploration that we
are doing.
And that's what I want us us to do today
in in this session. So, we need to
select something
that we're going to try. So, some There
were some suggestions on text.
So, Linda
suggested to be verb. I think somebody
suggested no text at all, extra text.
There was
I think just writing test was also
suggested here here somewhere. So, we
could try any of these.
So, in order to to start just getting to
that test case, our very first test
case, we can right now for a moment park
any other ideas. Like, we have probably
a gazillion ideas of which we which we
could try. But, focusing on that very
first kind of like demo test case, what
we want to do is is somehow manage I'm
using Playwright and Python just for for
demo purposes today.
Uh we could write here something, and
and you can notice that since I've
written on my computer some backups so
that if I mess anything up, they are
already existing here. Uh the GitHub
Copilot is also very helpful for demo
purposes in the sense that it's trying
to fill me something that already is is
quite nicely available. So,
I would like to put in the text. So,
again, inspecting here, seeing that yes,
indeed, that's an ID called input text.
I could put there some text, and instead
of this to be or not to be,
uh let's just put that to be which Lydia
there was was suggesting. So, our test
case kind of like, we're building it
step by step and and exploring further
with this.
Uh
yes, we would want to then, after
writing the text, we would want to be
clicking the button.
And again, looks like maybe that might
even be exactly the correct ID. Uh
uh that we have there
and uh
uh we would then probably want to be
doing some asserts.
Well, word count seems to be two. It
counts actually right for us.
Discouraged words and possible
violations. I can also kind of like take
all of them
from whatever the Copilot is now
proposing on on my machine. So, we have
a basic test case. We have never
actually in this group, all of us
together. We've never used the
application on the user interface.
Uh maybe you have on your own computers
already, but we can kind of get to a
place where we'll just run the test
here.
See that something happened and and see
what went on. Let me just
see what's going on. So, yeah, I
was a little bit overly certain on on
what I'm getting.
So, I'm getting a failure on on the to
be.
I'm asserting for one and I'm getting a
zero because obviously this discouraged
words, the to be word, wasn't zero. It
was one. And I can just kind of like
fix my test.
See if things are happier
based on
on kind of like my my actual intended
test case. So, I have now a single test
case. We've explored one thing. We've
seen that if we write here to be,
I can also show it here.
The word count is two, discouraged words
is one, and possible violations is is
zero.
So,
from this moment on, when we have no
matter what the API is, it could be unit
level API, it could be
a REST API that we use, it could be a
protocol API, it could be the user
interface and Playwright as the API.
After we have our first test case, what
we basically can do that then is to
refactor it. And instead of making me
today watch me kind of move things into
into variables, I'm just going to kind
of jump into fixing this
this test here
into the right values. So, we had two
words and a single thing.
Oh, sorry. This one.
I I
Well, I can fix definitely this one.
This is now the exact same thing uh
that we wrote, but I wanted to fix this
one into parameters.
Sorry.
So, parameterized test, exact same test
values that are different. And I'm going
to run this now from the command line
rather than having to run all of the
different tests there. So, I want to run
parameterized tests. So, I'm just kind
of fast-forwarding a little bit today
for the demo purposes on on the code
that we were writing. It's still going
to the page, it's filling in text, it's
clicking on the button, and it's
checking the three numbers that we were
checking. But now, instead of giving the
numbers as part of the script that we
first wrote, it's now been refactored so
that we can parameterize things and it's
still that single very same test that we
run before.
And hopefully we can see that it's it's
running. It gets us gives us a a green
pass.
And it is leaving us exactly where we
used to be before.
So now we're back at the exploration and
the question to you, what other things
we would test?
So someone suggested maybe trying
longer texts.
Someone suggested maybe try no text.
And and we can definitely try both of
these. And
when we're exploring
by looking at things
and on the user interface or on the the
code level,
we could just say that a longer text is
let's say uh
1,000 A's and that should give us uh
1,000 words and there's nothing that
should be a violation here. So that's
our longer text. It's not pretty,
probably.
Uh but it is giving us
uh 1,000 A words.
And when we again
run this
well, we can see the first test run and
the second test run. Let's see.
We have test one.
What's
with my
thing? Maybe someone is seeing where's
my mistake now. One test. I I would
Yeah, so
I got them them here.
Is that a comma?
It is a comma. It's It's right, right?
But it's only running that that second
one. So let me just take the first one
actually out for now.
For now, so we can leave that here. And
I want to actually do a small change so
that we don't have to feel so rushed. My
Pytest INI here says that you wait a
little while.
Let's wait a little while longer as
we're running this.
So, we can now kind of like visually
verify what are we actually getting?
We're getting all those A's and we
should be
getting a green pass.
So,
two tests
and
our possibility of of extending this
a line by line.
I still think I should have two tests
now.
What am I missing?
Anyone see where my mistake is on my
parameterizing? No?
One, two.
That's a text. That's a text.
It looks correct.
But I am not getting two tests. I am
getting two tests.
It was just that I was so quick on
seeing them
that I didn't even notice that I have
two tests. That's my big mistake.
So, all is fine. It's just my my eyes
that are are jumping.
So, the question is more ideas. What
else should we test? This has bugs. It
has actually
quite a relevant number of bugs. And
just like when we are writing uh
test automation or whenever we're
exploring without automation, uh the
quality of our ideas is actually what
drives the quality of our results.
Any proposals for ideas on what you
could try? You could try numbers.
So, uh
uh
to be or not to be, a little longer
text. Uh so, if we add that for example
here, well, we can just quite easily put
new things. To be or not to be.
Uh well, to be
or not to be. I want more words. So,
again, 1 2 3 4 5 6 words, right?
Uh
to be or not to be, to be verbs. And
that's what what would uh give us the
the right kind of things.
There's all kinds of ideas that you
could try. Script injections, HTML tags,
varying the cases, math equations,
hyphens, special characters, and even
that uh very favorite one of ours. We
wanted the empty text, and we would
definitely expect the listing of zeros.
Uh
all of these are kind of like uh you can
just kind of list whatever ideas you
have, and then run them, and your test
is is definitely uh growing.
Someone is already there uh getting to
the idea of what I want to take us to
next. That uh
there is a lot more on every single
application that we're looking at than
than uh the idea of putting some kind of
weird text or or uh uh disallowed text
or even the naughty strings uh that we
can use directly as an input because it
it's available in in that format.
Uh
instead of using all of that and kind of
like to seeing things and and seeing it
count, maybe we would want to, you know,
see this work in in some way that is is
somehow relevant. So, this is an
application called E-Prime.
And uh there is this little link here
that takes us to a web page that
describes
uh uh in short, that E-Prime is this
idea of writing English so that we can
avoid all the different tenses, all the
different formats of the verb to be.
Uh there's uh functions of to be, so
there's this all kinds of like identity,
class membership, whatever type of
things, which would make really great
test cases, kind of like as
specification
that we have tried to be verbs in in
different kind of sentences.
But also, there's very nice examples
here
uh on uh just uh writing uh different
words.
And maybe uh we could just start with uh
something lovely like this one.
A list of words that should be uh
forbidden.
We could create a single test case out
of those, or we could uh create multiple
test cases out of those.
Uh and the question here is, what are
our expected values? We have uh two
strategies basically on on defining
uh that
uh right values. 0000 is definitely not
the the correct one.
Uh but
uh
instead of uh that, we could see uh
running it, uh how many it counts, and
then check whether what we're seeing it
count is the right way. This is what we
call golden master testing.
Uh you need to verify visually with your
thinking whatever you were getting
before you capture it
uh as a way of comparing against next
time. Or you can very carefully
handcraft by counting 1 2 3 4 5 6 7 8 9
10 11 12 13 words.
Or is it? How many words is that
actually? I counted 13. Is that 13
words?
What do you think?
Anyone? You could write into the chat.
Is 13 the right amount?
Maybe? Maybe not.
I wouldn't ask if it was the right
amount, by the way. You might be guess
that.
Uh each of these isn't and wasn't and
weren't
uh
uh apparently
by me googling that in an earlier
session. I have learned that
and that uh they are actually two words.
Uh how they are supposed to be counted.
So, if I wanted this to be really
correct, I have 17, just like someone
else said there.
And out of these 17, uh I have three
that are contractions and one that is
not a to be verb. So, I should have uh
four less. So, I I should have 13 that
are uh rejected as kind of like against
the prime. And I still don't know what
the third word uh third category there
is.
So, I can quite uh expect that this uh
fails. Uh
uh but how it fails may be then relevant
for us to look at. And now, since we're
looking at kind of all the different
tests in in order, uh we might also kind
of just, you know, for for uh speed
reasons, we might want to run these
tests one by one from the the IDE. We
can do that. Or we might want to just
comment out some of those those tests.
Uh
so that we can see what's going on. So,
we can see that 1733 didn't produce what
we we expected.
Uh
expected uh and instead of getting 17,
we got 13. So, so this one didn't quite
work the way we were expecting. The 13,
uh original one, was what we were
actually getting. And And this one
actually should have been four. But I
can't write calculate, apparently. One
less.
So, these were calculated as single
words rather than two words. So, in a
way, that found us a bug, and we could
just, you know, instead of going to a
bug reporting database, we could say
that we have a bug here.
And the bug is that uh uh
it's is two words. So, again, a quick
way of writing that
uh down for us so that we remember it
later, and we should definitely uh talk
to someone or make some fixes in our own
very own code uh based on on on this
this realization.
So, we have now a test that is is
failing. We could leave it failing, but
then we can't run it in a in a CI
environment. Maybe we want to just see
it fail.
Uh we can choose either way uh that we
we want to do things. I now prefer to
leave it as as commented out uh thing.
And the other thing actually had before
we do that, let's just look at this. If
we turn this into 13 and and run that uh
particular one again,
I'm going to just comment this out
because it's
easier for purposes of of running this
forward.
So, we have that single one uh 12
violations uh and we have a pass. So, we
have only that one uh failure here. And
now uh we would be happy to kind of
comment this one out with the note of of
uh of that bug above it.
But I want to take us then back to this
this specification because obviously we
looked at the specification
uh
uh because we uh probably can also find
there other things than this single line
of things.
And we have this listing here.
Which looks equally promising as a thing
of of copying into our code.
As as a test.
And we would again similarly
need the the numbers here.
How many words? 1 2 3 4 5 6 7 8 9 10 11
12 13.
And
14 and 15. I can't calculate apparently.
I can't also write enough of the zeros.
So with this one in particular, I'm
really keen on just kind of running it
and I'm seeing what it gives me. If I
can calculate or not, both of those
options are same. You might have noticed
that we saw now not only red, we saw
some blue.
And we see that our first assert there
were first zero
is actually giving us back
a one rather than than what we expected
to get.
So what we are seeing as the
way this works right now, this
application
is that there's 10
of these these uh
uh
so-called
what is it called? I've forgot already
again. Expected violations.
Rather than than anything less.
So with
that we kind of see that the the blue
text, let's take it just here.
Maybe it allows me to use my computer a
little bit better.
Uh we can see here that we have some of
the words marked as as blue.
And also actually by the mistake of me
copy-pasting and pressing enter, we also
see yet another bug that requires us to
think in terms of of ways programs can
fail where the enter in the end of all
of this
the new line is actually taking the last
line into its own uh own uh
uh starting line here.
In the the output, so the outputs don't
work quite correctly uh when you have
that new line. And also the calculation
actually gets confused uh with the fact
of of uh having
having extra
uh space in the end of the the things.
So, I I left that to be there in the
beginning, which I originally didn't
want.
I also left that one, and this is what I
really intended to show you.
Uh I just uh do the usual thing humans
do, making mistakes that reveal
information. It's called serendipity,
a lucky accident. And uh sometimes uh
you do that by accident, sometimes you
push your luck by going through lists of
things
uh that uh
would typically make programs fail,
which is kind of a typical technique
that we use in in exploratory testing.
But uh we can see 15 words, uh one on
the red side, 10 on the blue side. And
we learned that the blue side of words
actually is on uh possessive words. So,
when it's an ownership thing, you don't
really know if it is the to be verb or
an ownership thing. So, it's kind of
this application's way of saying it
requires some human attention not
smarter way of implementing than what we
have
right now available in this this
particular version.
But
the correct functionality here is that
these dot s's would be actually
belonging into that possible violations
category. So, that's right.
Whereas these three here
should be marked as discouraged words.
So, anything with r e it's missing it's
an omission
missing piece in our implementation.
So, r e not recognized.
Has to be
four.
So, we have our second bug
bug here
written down.
And if we wanted to then have our
third bug written down, we probably had
this this idea here where we were doing
text and we were doing a what was it new
line?
Where's my backslash?
Can't use my keyboard for today
clearly.
New line
test.
So, two words with a new line in
between. Maybe I don't want the spaces.
I just want the new line in in there.
I would expect two words and similarly I
would expect this one to fail.
Because I know there's a bug in in that
particular uh scenario.
It got uh back to one
even though there's two words. So, yet
another bug for us
uh to report on.
Word count incorrect.
So, what else would you test?
I've shown you couple of samples of of
the types of things that you need to
kind of come up with so that that you
can find uh bugs on this one. None of
these were uh
weird
uh characters on the user interface.
They are all basic uh positive cases.
And that's kind of where I generally
want to keep us today for the demo
purposes rather than going on the idea
of let's try all kinds of weird things.
There's plenty of non-weird stuff to to
try as well.
Any ideas on what you could try?
You can again write on the chat window.
What else should we test?
You feel out of ideas, it seems.
So, let me just kind of then fast
forward into
maybe the most complete version that I
have right now available for demo
purposes here on my machine.
So, uh this particular one is a
collection from various sessions.
Uh we've run
uh on uh
uh exploratory testing or contemporary
exploratory testing in the sense that we
are making our notes in automation.
Uh we haven't really cleaned it up and
made it ready for continuous deployment
system uh and we might want to even
throw this out in the the end of the the
testing session and just report the
bugs. We might not care to keep all of
these around. Or we may want to clean
them up and and keep them around for
later. But we have uh multiple cases
here. And like the note here says, nine
of these
uh contain a bug.
But uh unlike on the three that we just
listed, these don't mention which ones
have uh those bugs.
Uh this one, typesetters and typewriters
apostrophes.
Uh that's one of those bugs. So you have
different kind of ways of doing that
apostrophe. Maybe that's a relevant one.
Uh one where you have uh names with that
dot s and and calculating uh the blue
ones. There's mistakes on that uh when
you end up with a two-part name uh with
a dash in it.
And my absolute usually favorite to even
start with, this particular one. It is
not nine words. It's eight words. So it
has already a bug. So kind of to
conclude on on what I'm trying to
uh kind of show you here,
is that uh looking at an application
like this, uh it has four major traps
that people usually fall into when
they're trying to do exploratory testing
of it.
The first trap is uh what I call test
data trap. And as per the comments in
our uh chat window, many of us would
have actually fallen into the test data
trap. And the test data trap is that we
are using easy uh illegal test data
even. And we're using uh early on before
even understanding how the application
works, we are using uh all kinds of
weird values.
and those are bound to be of lower
priority in in general. So, starting
with those might not be the best move
for us. So, that's the first trap that
we would like to maybe avoid. The second
trap is what I call test automation
trap. I avoid it or maybe algorithm
trap. I avoided it today by only
focusing on on these values as in things
we count in automation, but if we write
here text and we start creating
something to identify the blues and the
the reds
uh, and lack of them and and all the
different combinations, it very easily
takes us 10 15 minutes to to build
something and depending on how much we
struggle with that in the moment, it
might take us even longer time and it
drives us a kind of like maybe
prematurely before we even understand
the application
uh, to spend time on a detail that
actually doesn't necessarily add a lot
to testing of at least this particular
application. So, we would need to be
maybe careful with that.
Uh, the third trap that this application
invites us into is this e-math e-prime
link here. So, the page that we looked
at has a lot of different kind of
examples. It has the e-prime Bible that
I have even actually at some point
bought here on my computer.
Uh, it took me a while to figure out how
to take a Bible in a PDF form and then
turn it into a text and then save it
here and then use it on those tests and
kind of like, you know, go through these
steps. None of them individually very
complicated, but all of them were kind
of like set up related activities that I
might not necessarily need in order to
get the first early on feedback. And
while I now know in those tests that I
have that this file called Bible has
31,172
words,
uh it did take me yet another 5 minutes
of of kind of copy-pasting it elsewhere
and and seeing comparisons on how
different places are calculating the
words and and what would I like to use
as my oracle on the numbers or
correctness of numbers. So, all of that
was kind of leading me to a different
place around this this kind of like
figuring out how to determine if if the
test is passing or not.
And then the
fourth
uh usual trap is what I call a bug trap.
Uh
if you start with
to be or not to be,
um let's dilemma.
You might imagine you are doing really
well
on kind of seeing and discovering the
functionalities. This is a brilliant
demo example, but I've also seen that
this kind of thing which includes a bug
can lead us into
the
the trap of focusing on finding
different ways word count fails on an
application that isn't called
word count, it's called E-Prime.
And in the end of our whatever limited
amount of time, we might think that
because we have now 10 bug reports,
we've done a good job, but we've
actually not found any of the relevant
to this particular application bugs
that we were we were looking for.
So, we want to avoid those traps.
So, I kind of wanted to
show you a couple of slides here in the
the end of this.
On on sort of summarizing what we just
did.
So, what I tried to show you is that,
you know, we can start from a single
line of code and write that single line.
And we can see that single line of code
fail. I was not doing a single line, I
was doing three lines first and then
only seeing it it fail because of the
mistake, fixing the mistake, seeing it
pass.
And then kind of getting to place where
we actually have our first test and
maybe we even feel that because we've
seen it fail, we can trust it. We went
through all of those different steps.
We went through
changing that same thing, exact same
thing, refactoring a little bit, but now
using variables and and then using
parameters so that we could just
actually focus on not writing automation
at all, but just kind of thinking in
terms of what could the different values
values be be for us.
And
in terms of uh
moving then forward, we took some things
from the specification. We could have
been a lot more thorough. We could have
also beautified the specifications. I
also have here uh
a example.
Let me just open you this one.
Which I rarely use in in the first
demos, but if we would spend time on
writing the most beautiful documentation
we can think of, this is equally
executable
and you can just write your new test
cases on the next lines. It is just
implemented in that BDD style and it
might be useful in in some of the the
project. So, you can really turn your
specification into into tests, maybe
even beforehand rather than than now
what we're doing today, which is after.
Uh you can guess the values likely to
fail. You could run this on a different
browser, multiple browsers, and uh the
time you used to spend on setting up the
automation, it starts paying itself back
the more you get to repeat with use of
that automation. And uh you maybe can
leave it around, or maybe you can throw
it away.
Uh it helps you document some of the
things. It makes you completely
oblivious uh to some of the other
things.
Uh for example, uh what we don't easily
notice
is that there's a bug where the
uh text box resize uh is broken, and and
it doesn't even actually fit in the
screen. It might be that I have actually
fixed it in in this particular version
that we use today.
Uh but basically, what this style of of
of combining things uh attended and
unattended uh testing is giving us It's
giving us documenting. It's giving us
extending of reach. It calls us back to
the same details later on, and it forces
us to really think in terms of of
detail. What do I expect? And and forces
us away from kind of like what I would
maybe call sometimes sloppy thinking.
Like we forget all the possibilities we
had. And when we see what we've written
down and what we can actually run with
the the uh the rerun later on, it guides
us into more detail of of looking at at
at things.
So, the conclusion kind of here uh is uh
uh with this contemporary exploratory
testing is that I believe that you can't
automate well without exploring, and you
can't explore really well without
automating. And instead of thinking that
you have this kind of like
exploratory testing cloud on top of the
triangle here, what you have instead is
you have two ways of thinking about it.
The first test, something easy that
someone gave you as an answer and then
all the things we expect on that answer
key to all of the box that you need to
grow as part of of contemporary
exploratory testing. And again, another
way of kind of visualizing that is is
that a lot of times as developers
especially, we work on the intent. We
have the developers intent and we
definitely want to work on that on the
unit level. We have the customers intent
that we are listening to very carefully
and we document that on acceptance
level. And we have the past intent, all
of the things we have ever promised on
any level and that's what we think in
terms of regression testing.
And exploring is the
questioning of is our intent going to
match the impact that the users on all
levels are going to be experiencing.
So that's that's kind of what I wanted
to demo for you today and
yeah, now it's good time to take
questions and have any conversations
you'd like to have
on on the the testing topics.
So you can put questions on the chat. I
think you can also
try going into the
unmute button. It might actually work
for you. I'm not quite sure, but I think
that's also a possibility.
While you're looking at those, I want to
kind of leave you with an aphorism
maybe. I'm sorry.
This is usually where I if I do a
presentation version, this is where I
might start. I believe that everyone can
test just like everyone can sing.
But not every one of us finds all those
problems we found today.
And unfortunately, it's not enough to
try the the weird inputs
because even a broken clock is twice
twice right right twice a day and we
want something more out of our testing.
So let's not be the broken clocks and
that's why we need more thinking when
we're doing the testing that we're
doing.
All right. Well, thank you so much Marit
for that very interesting session and
thank you everybody who
contributed to to this session. We have
a little bit more time, so I just
encourage you
Yeah, like ask any question you have
whether it's in in through the chat or
you could also Yeah, I believe you can
you can unmute yourself and and speak
out loud if it's easier that way. Yeah,
you know, that we don't we don't get an
expert in a room every day. So
take advantage of this opportunity.
There's some really brilliant
exploratory testing that I'm watching my
team of developers do right now where
there's just the basic possibility of
injecting an object into a fairly long
processing halfway through and then see
what comes out the other end. Very
similar to what we did today. Just kind
of parameterizing, categorizing,
thinking about things. And the amount of
problems they found on something that
they considered done
just by being encouraged to try that. I
think we all need to do more of that.
Yeah.
All right.
Any questions?
Oh.
Okay, we got something more, right?
Yeah.
So, are there any exploratory testing
tools
I would recommend using? Anything that
aids in this process?
So, in a way I believe that any tool is
useful, kind of like uh
uh
the IDE and just writing things down. It
creates certain uh
uh rigor into the way you do your
exploratory testing.
Uh sometimes maybe mind maps are the
lightweight way of writing your notes
and changing your mind about things.
Things are much easier to move around in
a mind map when you kind of like
categorize the things you've learned and
and only kind of go into anything that
commits more time at at a later uh
stage. But, there's also like specific
tools for for exploratory testing, which
usually add kind of on top of of basic
note taking. They add maybe kind of like
generating ideas or making proposals or
giving you prompts on things you could
consider.
So, my number one rule for uh testing in
an exploratory fashion is that since
we're looking for that gap of results,
the things that are invisible, that we
don't yet know of and no one can really
tell us except past experiences, those
prompts uh are really useful.
I rarely use tools that give me prompts,
but I use all kinds of of checklists and
helpers in in that sense. So, the the uh
the um
uh
there was the list of
uh different kinds of inputs that was
also mentioned in the chat, the the
naughty list, uh naughty strings list.
That's an awesome one uh
uh to use to help you kind of figure out
what kind of inputs are possible. But,
again, uh you probably want to select
thoughtfully rather than rotely out of
that list, so that you think in terms of
if I'm now finding something, is it
going to be relevant? And in what way is
it going to be relevant?
So, any tools would be helpful. And uh
what I'm dreaming of is is uh still a
tool that uh takes your notes and
compares it to generally the notes it's
ever done before and gives you hints on
things that you are not paying attention
to anymore. Maybe that's coming across
when machine learning becomes more more
commonplace in in in these these things.
So, there's definitely a lot of work in
the space of uh
uh bringing information at our
fingertips like Copilot is doing for
programming. It's not like it's removing
the need of a programmer. Uh someone
needs to review every single line that
writes.
But, uh it is giving us those those
prompts and and and suggestions. And
it's kind of cool when you can take a
look at uh with Copilot, you take a look
at the 10 different solutions it provide
uh
provides you. And when you hate every
single one of the 10,
uh then you usually find the number 11
that it didn't suggest uh that you just
weren't thinking in that moment. And I
believe similar tools are are about to
emerge in this this uh exploratory
testing space as well, helping us
remember different kind of prompts.
Note taking can take a lot of time. So,
writing automation my rule nowadays is I
I prefer using my time on documenting as
automation over documenting in any other
format.
And uh
uh I used to write uh traditional test
cases because organizations kind of
forced and guided us into that.
Uh
uh I used to write very detailed notes
while exploring when I wasn't trusted
with uh ability or willingness to test.
That was basically what people didn't
trust in.
Uh but nowadays uh it's much rather out
of the 100 things that I I I come by, uh
I maybe want to leave five of them
behind as automation, so that I have
this like spider web where I can find my
next day's dinner. Uh that it helps me
really explore more effectively as as
kind of things are progressing forward.
Every day we can just grow that
just a little and and keep that at our
fingertips.
Yeah.
Yeah, thank you for that. Any any other
questions
before we wrap up?
Okay.
I can still maybe say one more thing.
Well, there's actually question.
Oh, there we go.
Uh so, have any favorite patterns or
heuristics or advice for communicating
testing results uh that are generated on
this approach?
Um
Uh my general pattern, maybe I can
actually show tell you the example that
I I shared just yesterday because I
needed to summarize six months of of my
work for my manager and how my pattern
of of of summarizing that was.
Uh
I told uh that uh we went from about 100
test automation things on all levels. We
counted all things, unit, integration,
and and end-to-end level on our
application. From about 100 things that
we had written down as executable ways
of of remembering uh things by tests, uh
we went to about uh 600 uh in the last 6
months.
Uh I mentioned that uh from uh one
category of types of of of things, kind
of like one way of making those notes,
we went to four different kinds of of
categories. So, we have now the unit
integration and and the end-to-end
stuff. Uh and we had the BDD style as
the fourth category. We are doing some
of the things experimenting in that
space. So, kind of mentioning those
numbers.
And then I mentioned that the difficult
part for for me to still explain of my
work
I definitely I can tell about the number
of bugs we found, but I don't think
that's the relevant part. But the the
gap, the invisible gap, there's no easy
number of telling about that. So,
instead of telling the number that my
team and I ended up in the last 6
months, I told him a story of a previous
team where I reported over 2,500 bug
reports over the course of 2 and 1/2
years in that project until the day when
I realized that I kept repeating similar
things in different places, and I was
doing testing wrong. Because what I
needed to do instead of reporting so
that I can calculate them later on, I
needed to go to the manager to the
developer and show the bug that I found,
and magically with that pairing of
fixing the thing and talking about how
did this happen?
All those 2,500 things just melted away,
and people learned. How do I find them
in the first place?
And that gap I can't tell it by the
numbers of how many things I find.
But I don't think that's the right
question from anyone who's managing me.
So, so showing the numbers of always
growing in the documentation
which is a liability in a sense. This
test automation is a liability for us.
We need to maintain that. But still
growing considering that it's useful to
grow, and then then showing that there
is work happening in this this gap space
of results
that we wouldn't be getting and that it
shows up as as us learning. So I had
this also this visual of I asked my team
6 months ago on how well these different
practices work and I showed how they
they rate the same things right now and
of course it's kind of nice to notice
that the the thing that says testing
practices, it used to say everything is
bad and now everything was good. I think
it's just a little illusion. So my next
6 months is showing everything still bad
but maybe then we can get to actually
good by by getting away from the the
illusion of of thinking we we knew what
we're doing. So this is a it's a
learning process learning all of the
things that you know some people have
thrown over 25 years. So
telling stories is my favorite pattern
definitely.
Awesome. Oh, thank you so much. Yeah.
Stephen, am I unmuted? Can you hear me?
Yeah.
Ah, okay. So first of all I want to say
thank you and
that that was nice and it was totally
different from the last part
the last time when I saw that and we
didn't go in that direction so I didn't
have that kind of advantage.
And that was interesting and I'm
wondering I got triggered honestly in
the last part about heuristics and like
how to communicate the value of the
team. Now recently I became a manager of
uh
testers and we all know Iria and she
says hi but
I I see some familiar people and uh
the question is how to like
is the only way to tell a story every
time? Because what my manager wants from
me is to have
okay, maybe not even quantitative but
qualitative characteristics and they
want to see some trends and I can tell a
story how cool we were and how
big issue we prevented.
You can do both. You can always do both.
But so again uh
kind of like uh when you tell a story uh
but you add to it uh where's my
my browser is here somewhere.
Where is my browser? Oh,
here it is.
I've been minimizing all kinds of
things.
So, when you tell a story but you add to
it some kind of a a picture that that
may be uh says the same thing or uh if I
would have it open right now, I could
show you the numbers that I collect
every 2 weeks. The numbers tell the
story without me uh saying a single
word.
So, the stories are enforcing the
message that we want people to get.
But they are not sufficient alone. You
need a visual of some sort, numbers and
and this qualitative kind of like asking
for things. Uh
these kind of things are usually also
also relevant.
So, again kind of nice to see that
this thing is doing much better than it
used to do when before the I had I was
even in the team.
But again, this this kind of like
figuring out how do you get the message
across? Show both numbers and tell a
story. So, uh be consistent. It's not a
single time, it's a continuous
communication.
Yeah, but the the problem is that we
need some numbers and I'm struggling
what to count.
Uh
I can say what I counted for my team
right now. I count uh how many uh
merge requests we have because I believe
that uh if you don't make any changes in
code, nothing changes for the better. It
just stays the same. There's not going
to be improvement without change. So,
change and and that it happens and that
it's it's possible for for the team that
is relevant.
Uh it is even more relevant nowadays
because with infrastructure as code, all
of our our well, Docker containers, all
of that infra uh is also code and none
of those get fixed unless we are also
making those merge requests. And and our
tests are also uh code which our
documentation, test documentation, or
executable documentation, they're also
code. So, unless those are, you know,
growing and moving and and unless we're
we're making changes, it's not going to
get better. I look at uh
number of well, percentage of how many
of the merge requests when they're
merged end up in a green pipeline. Our
number, I think, last time was 65%. I'm
not happy with that. It should be 100%.
So, again, when you get to 100%, it's no
longer relevant. But meanwhile, keeping
kind of the conversation ongoing that it
needs to be that that getting to that
100 and never going down is is
necessary.
Uh I calculate how many things we say
we've done and what what how many things
we demo.
Uh I do calculate how many Jira tickets
we have, but that I only calculate for
the the purposes of saying that you do
realize that's only faking work and it
is not representative of of real work. I
have no test case and numbers as such
other than well, I definitely look at
the the numbers of how many have we
documented in automation and I don't
show numbers of how many bugs we found,
but I show how many do we still have
open. And we have this rule of uh uh
stop the line. So, basically, when we
get more than 10 bugs reported, we're
going to stop everyone's work until we
are again back at zero.
Uh and that is a certain kind of like
sense of hygiene for the team so that
you never have to actually be uh long
away from the the productive work. So So
I choose my metrics based on what I
believe creates a good atmosphere or a
good working environment for a
developer-centric way of working in a
product development team. And
that's how I come up with the numbers. I
would probably do it differently in a
different organization, but this is what
I do right now in my current team.
Mhm.
Thank you.
Awesome. Well,
thanks so much everybody. I think
because of time, let's let's do a
wrap-up.
Yeah, thank you Mart so much for your
awesome examples and experience. Really
ex-
enjoy having you here. Do you have any
like final remarks or encouragement that
you want to leave everyone before before
we go?
I'll give you one thing. Uh
if you want to learn more about this
stuff that I talked about today, the
application was on exploratory
testingacademy.com. There's also a whole
course on
learning to do that and learning to look
at things in a different perspective. So
if you need to practice that, maybe you
want to take a look at that.
