---
title: "Teaching and Coaching Exploratory Testing - Maaret Pyhäjärvi"
video_id: ZWI6MFvxQJk
url: https://www.youtube.com/watch?v=ZWI6MFvxQJk
upload_date: 20180914
duration: 52:13
channel: Association for Software Testing
tags: [Unit Testing, Exploratory Testing, Test Coaching, Software Testing, Software Development, Software Developer, Software Tester]
---

# Teaching and Coaching Exploratory Testing - Maaret Pyhäjärvi

> There is a lot of talk around testing — who will do it, when it needs to happen, boxes it needs to fit in — yet not enough on the actual testing. In this webinar we hope to change that as Maaret will look at one problem in a demo setting. This means live testing (and live coding) to figure out our options to get a test program covered – for code coverage, for spec coverage and for risk coverage.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

welcome everyone today we have marette
who is an engineering manager at
f-secure i know her and you probably do
as well from her constant writing on her
blog visible quality you might have also
seen some other writing she does on
medium or read one of her two books mob
programming guidebook or exploratory
testing both are available on lean hub
lean pub and I highly recommend them she
does a lot of writing and it's great you
probably actually need some type of
bookmarking tool because a lot of it
comes very very quickly but it's all
great stuff
Marie is also the organizer for the
European testing conference she is on
the leadership team at speakeasy where
they help mentor others to put them into
a position where they can become
speakers at conferences she has been a
tester for 25 years and today she's
going to be giving us a presentation on
teaching and coaching exploratory
testing so Marie do you want to take it
away yeah thanks so you probably see my
screen right now that's right all right
so I was thinking of what do I want to
share with all of you and I thought that
one of the things that I really want to
spend some time on on speaking and
showing to you is that for the last
about couple of years probably
but intensively the last six months I've
been spending some time working with
random people usually through Twitter
volunteering to do exercises with me so
teaching and coaching exploratory
testing and I wanted to show you one of
those kind of exercises and one of the
things that I've been doing with with a
lot of people hopefully giving you some
ideas then on how would you be testing
certain types of things so it really all
starts with this idea of a question that
we asked ourselves a lot as testers
whatever we end up with whatever feature
it is whatever product we're looking at
what
API we're looking at whatever piece of
code were looking at
we're always ending up asking how would
you test this and would the way you test
it be any different than somebody else's
how do you know if you're any good at
testing that's basically a a thing that
I pieced I keep asking myself kind of
constantly I've been doing this enough
for last 25 years so that I have these
little stories where I go and take
somebody else's program a couple of
years ago I took a program called
approval tests it's an API for testing
purposes and I talked to the developer
of that open source project and I told
him that you know I want to just test
that approval testing and and that you
know it seems like a target that would
be good to show how to do certain
exploratory testing things on where
there isn't a GUI but there's an API
that that I could just explore and the
developer was kind of well a typical
developer in many ways he's like yeah
sure go for it like you know if you have
any questions I'm happy to answer them
and also he's like yeah sure like you
know it's all written test first and
it's code that I'm very proud of and
there's a lot of tests so you know you
won't be probably finding anything and
then later on this particular developer
he went on a podcast where all of this
this quote comes from and quoting him I
destroyed his thing in like an hour and
a half but as a tester I of course need
to correct people a lot I didn't
actually break anything that wasn't
already broken the the only thing that I
might have broken is his illusion that
doing something test first doing
something in the best way possible from
one person or even a Paris perspective
that they would still not to be
something else that I could contribute
so I basically showed him that he needs
to change the whole API it wasn't
discoverable I showed him things around
environment like if you had couple of
different test runners in the same
environment he couldn't even install the
whole thing
and I found all sorts of promises and
things they were kind of said and and
given us as things that you could do but
you couldn't and maybe the most annoying
thing was that there were a lot of code
samples I could start testing with and
none of them were copy pasted of all so
also the basic getting started with
documentation was something that I I
needed to show that the modern ways of
thinking about what you can do with that
kind of things is something that wasn't
available for that particular project
back when I when I was testing it so I
ended up testing all sorts of software
and always the question that I come to
is is they how would I test this so what
I wanted to do today is instead of
showing you a dozen slides I wanted to
show you one real thing that we could be
testing and kind of ask you I can't get
you to tell me right now but ask you to
think about it how would you personally
be testing the thing that I'm showing
you the thing that I'm testing and how
would the way you test this be different
from from whatever I'm showing so the
target of our testing and the example
today I really encourage you to you know
do this with for example your team's
yourself in in your offices because it's
publicly available piece of code it's
called EULA Bros and it's used a lot in
the the refactoring crafter community
side as an exercise where you first need
to clean up the code and then you can
add more features but what I use it for
basically is you know it doesn't have
any tests so we need to be testing that
we need to be understanding what does
testing look like for this this little
piece of code gilded rose was created by
Emily Bach she is a developer from from
Sweden and EULA Rose is nowadays
available in 32 languages the language
we're going to be working on today is
it's Java just because I happen to have
that environment here on my machine all
and running and gurus is a nice example
in the sense that it comes with a
requirement specification it comes with
the executable code and that's pretty
much in a better way of getting started
with something new that you need to test
that what you usually have in in many
projects where you kind of first need to
go around and ask ask a lot of questions
so let's look at the the specification
first so the specification I put it on
on two slides here and the gray text
here basically says that you don't
really need to read that stuff it's just
some extra text that was was added there
so beautyrx OHS is a shop it's a shop in
a prime location in a prominent city it
is something that is running in
production so called legacy code it's
working for someone right now and it is
a shop where there's certain things that
are being sold there and they are
constantly degrading in quality as the
sell by date approaches so conceptually
very much a regular type of a shop they
have this gilded row system in place
which updates the inventory and know
somebody developed it but basically what
it does it does it all of the items
there's a selling value how long until
the selling date they all have a quality
value how valuable it is and this
quality value goes down over time and in
the end of the each day you can kind of
like say hey time to go for the next day
it lowers values both for the quality
and for selling so this is the first
part of the specification so here we
have that piece of code sorry now a
piece of code is is here all of it that
implements those requirements so it's
not that much it's like 62 lines
total but even if you've you know even
if you read code on a
regular basis you don't like reading
this this is kind of messy and mostly I
don't spend my time reading code but I
spend my time figuring out problems so
this is not what I would be looking at
when I'm asking how would I test this
Emily was kind enough to give us an
example and something to kind of get
started with so what Emily gave is one
unit test that we can run and it's
passing the 1 unit test introduces this
little method called check item so kind
of like if you look at it it says
there's something called any it's a
string item there's something of 0 which
is the selling dates how many days you
can still sell it and there's another 0
which is the value of quality so they
are just books is that you can fill in
just like when you're exploring on the
user interface level when you're
exploring on an API level you just
basically see boxes that you can fill in
so we have these three boxes that we can
play with we know from this one example
that if we give it give the item name
any and the days are zero and the
quality is zero the quality after we
move on by one day which happens here
with the update quality method the value
is still zero so if we start with zero
it ends up with zero so we have
different options on how we could
approach this so again now think of how
would you test this so I'll go back to
showing some more of our requirements
because the basic idea of what box is
we're filling in and what's there
meaning that's not yet telling us much
about what would be we'd be testing so
the requirement specification also comes
with these business rules of things
around how quality and sell by date
should work together
so there's all of these different
sentences saying things like the quality
of an item is never negative so
different people depending on who I've
been working on this problem with either
they read all of these in detail but
after they have either read all of them
in detail or selected something what
they need to do is start testing it so
if you just read and and plan and wonder
you don't yet get much of anywhere
hands-on the software the using the
actual application it's kind of like an
external imagination for anyone who is
doing exploratory testing it gives us
the chance of learning with the
application so let's take the quality of
an item is never negative
let's try try how that that one works so
we have this way of playing with the
values so we have a test something and
we have a quality value here which is
the last one here and it says quality
should never be negative so you know
let's say minus 10 sounds like a
negative number what do we expect
there's two ways I could be testing this
right now I could be running the test
and seeing what it gives me this is
legacy code so whatever is coming out
right now that is what we have right now
in production or I could be looking at
the specification and thinking what is
the value that I expect it tells me
quality is never negative so I would
probably be expecting that the quality
is zero or something positive even if I
if I start with an input that is
negative so let's see what it does I
learned that if right here on the left
hand side if I give it a minus ten in
the beginning it still gives me a minus
ten in the end so my expected value of
zero won't work it will be a minus ten
let's see if I run that again that seems
to be right so again just you know
writing down some
potential bugs quality can be negative
that's against our specification so
again going back to the specification
there's all sorts of different things so
again I could take the last line I could
take the first line nothing says
anything about the order in which I have
to deal with them but it kind of feels
like right now I don't really understand
this application too well so maybe the
the first line here would help me
understand it a little bit better so the
first line on this this one says that
once the sell by date has passed the
quality degrades twice as fast I don't
really want to test this claim as as it
is but I do want to understand right now
and how things work around this
degrading and and the idea of getting
closer to a degrading day so if I have
another test which I give a really bad
name to right now because I do not want
to think about it right now I still
don't even understand the application -
well I want to understand what does it
mean that the quality degrades so so
let's say we have ten days of selling
time left and the value is let's say
five just in case so that they are not
symmetric because if we use the same
values and there's certain confusion
about those it's harder for us to follow
so this makes make sense so what would I
expect so ten days it's not very close
to the the expiry date probably it
should go down so if it was five
maybe it's now let's say four I don't
have to fill this in I could just look
at what what it gives me so it seems to
be four so it goes down by one in this
case so now I think I've seen in a basic
case so now I'm interested in the claim
that I actually saw in the specification
it said approaching the selling date it
degrades twice as fast they didn't have
anything to say
now it was asked the date has passed so
date has passed if we are let's say on
the negative side and we start with five
if it degrades twice as fast I would
expect this thing to be three rather
than and four and again I can guess
whatever and it seems to be doing doing
all of that so I can do this kind of
like requirement by requirement
expiration look at every single thing
that I see and figure out how do I cover
the whole specification but on my test
machine here I also have another way of
running this so I'm just using my
keyboard shortcuts here I'm usually
running this with command shift f11 on
my Mac and today right now I want to run
it with ctrl shift F 11 which basically
on my machine with my Eclipse runs it
under coverage so under coverage I have
these three things that I've tested so
far and I can take a look at Gilda rose
and see which lines uncovering so all of
the things that appear is red
they're giving me hints unlike oh I
haven't been there anything that is
green is I've gone there with all the
different routes that the program can
can identify I know that there's more
routes than both the programs can
identify but this is you know a good
starting point starting point in that
sense and then there's yellow lines were
basically I've been on that line but
there's another route that I could also
call Sobe addressing so now I have you
know even more options like why have the
specification I have the code how do I
put these together how do I actually
want to test this what's my my
exploratory testing approach so I wanted
to still introduce one more thing on the
way we could be doing this so a lot of
times we do these kind of simple tests
with this simple unit test I'll assert
things but I have a thing here called
approval tests
with approval tests what I can do is
just do a little bit less of copy
pasting a little bit more of
combinations so some of the things that
I want to do is you know just focus on
on trying out the different values
because this is a very value driven
exercise input value driven exercise and
see what kind of things as per the spec
I to cover so to do this I want to
introduce combination approvals and with
combination approvals I know that my
method that I'm using here that I was
using also with the the other tests that
we were using or I was showing I was
using this this method with three inputs
so I'm gonna use these three functions
type of thing and I'm just gonna call
the function that we used on the tests
and I just shouldn't write too much
otherwise I will probably make a mistake
on what I write I did probably already
make a mistake this so check item the
first parameter looking at just it from
the line 13 here below the first one
would be items so many of them many
items i want to introduce many items i
want to introduce many sellings and I
want to introduce many qualities I also
now want to just quick fix these first
nine my keyboard shortcut thing is it
gives me a bit of trouble here just
creating local variables for these I'll
just do these all three at once and then
introduce here that this first one as I
see from below here it's of a stripe
stripe string the two others are
integers just should not type because
otherwise I do mistakes always and for
these four things I can introduce 10
values just like I had in the previous
tests I'm just getting to a point where
we're able to do the same things as with
the previous tests so if we look at the
previous test I had values here a value
of any a value of zero a value of minus
ten ten and a five so just collecting
these all together so four qualities I
have minus one ten and zero so four
qualities minus 110 and a zero for
sellings I had zero misty sorry
qualities I had five five and minus ten
sorry that was in the wrong place five
and I minus ten and I had here these
values and here I had just the value in
E so this is basically getting me to a
place that already includes all the
tests that we did at first I could have
already started with this but I wanted
to show you something that some of you
if you're working with with a third base
things have have seen before so let's
run this test and what I expect now is
that I haven't defined any of the
circuits I haven't also cleaned up after
my my previous play so what I see here
right now or what we see here right now
is combinations for all of the values
that we introduced so we have the the
item any with the ten days and the
quality of five and we were checking
that it became four it seems to be here
line three just about what we were
seeing before also we have
here the value of of quality being 0/10
first and the days being minus or base
being ten and quality being minus ten it
still say it stays negative on all of
the three different cases but also we
have this minus one days here where
there was five and it gets to the free
so all of this is as we have already
looked through the specification and
what I basically then want to do with
this one is I want to move them over to
the right hand side approve them and now
I have a test that I can run that passes
with those values so now I'm in a better
place for my really quick exploration of
values so now I can really decide
whether I want to go with the
specification if I want to go with the
code or whatever whatever I want to do
and I usually have myself I have a
strong preference towards the
specification kind of making sure that
every single thing that the
specification claims gets gets checked
on so we've checked two cases on selling
date when it has passed it degraded
twice as fast when it hasn't passed it
was just going down by one we saw that
the quality of an item was negative but
it's not getting more negative so it
isn't changing so maybe that's what the
specification means it's definitely a
discussion point then it starts talking
about things like aged brie or so for us
or different kinds of items so I want to
just introduce those those items here so
first they aged three we had a rule
saying aged brie increases in quality
the older it gets so as I introduce age
to brie into the tests I expect this
test to fail because I haven't yet
approved any of the things with age
three and it gives me the combination so
now as an exploratory tester I can you
know look at this so okay I'll give it
values of aged brie
and with 10 days it's not old at all
it's getting a little bit better it's
getting there too value of 6 so what
about line 7 where we do the same with
where it's old it gets twice as good so
it goes up by 2 seems to be kind of as
as per specification and again I can
read every single line or I can sample
all of these are choices that I make
when I'm testing this misapplication so
I have the basic rule that I was told
this works in production everyone's been
very happy with it and you know we are
not changing it right now in any way yet
so maybe even if I had a question or a
bug that I wanted to report you know I
can make a note of that but if it works
in production we can accept that and
even if there was a bug if there was an
API that had that bug maybe we can't fix
that bug without fixing all the things
that depend on it so just accepting what
what it what the code gave him now is
sort of a safe way of doing things as
well as long as I know know that I'm I'm
ok with what I want to speak about on
the specification side so again I can
just run this so next item says that the
quality of an item is never more than 50
so well I have the values of minuses but
you know more than 50 it sounds like you
know 50 is something but more than 50
you know 51 sounds like more than 50 so
maybe I'll put both of these values and
again you know I don't have to know
exactly what it means beforehand I can
go back back and forth between my tests
and my specification and my
understanding and try to figure out what
does it actually mean then that the
quality should never be more than 50 so
it seems like if I give a quality of 50
for aged brie it still says phase 50 if
I give a quality of 51 it stays 51 and
if the values of quality go down they go
down by one just like for the NES
anything else and these are still going
up from the 50 because they're aged
Breen seems to be that I wouldn't say
that the quality can't be more than 50
there's no input validation I can give
values higher but when I give it a big
value it doesn't seem to be increasing
it anymore
so still a point of discussion but could
also be just what what we wanted so I'll
just again approve this and I now have a
few more tests that I've created that
are now running for me that I can use
them for later so then I have this claim
here saying sulfurous is a legendary
item and it never has to be sold or
decreases in quality so I'm really
curious on this like putting this thing
called so first I can't even write so
let's put there so for us that's what
the specification says so I run this and
again now you need to pay attention with
me I have all these items here that talk
about now what do I get if I use tool
for us as an input and I like to look at
the values that are somehow you know
allowed something that should be it
should be okay
so using sulfurous as a value where we
have 10 days to sell it and it starts
with 5 it goes down this goes down by 1
so it ages and the value of quality goes
down by 1 so it doesn't seem like this
is working but this is making me think
maybe there's something that I don't
know and going to the code again I've
done this before so I've run into this
problem before I can see that my
specification is using a shorthand
version of the name of the item so I
might want to know the bug against the
specification that maybe we want to fix
the shorthand because somebody else
might be making the same mistake as I do
and thinking so for us this is what the
shorthand version is is okay so let's
you know explore and try like what if we
changed it to our results change
and now looking at the exact same thing
the value of 10 and 5 the days don't go
forward it's Filton the quality doesn't
change it's still 5 and it seems to be
so for all of the values that I can see
here so again
seems like it it works as a specified I
also have a thing called backstage
passes here then it says backstage
passes like aged brie increase in
quality as selling value approaches and
learning something from the previous one
I really want to find the string right
from here so again the same thing using
shorthand sorry and adding that to the
list so we have some more values that we
can take a look at for the concert
passes now so I don't know if I have all
the different cases here for days so
there's expired raise it says after it
was expired or after the concert is gone
the value goes to 0 looks nice when
there's 10 days and goes to 9 days the
value goes up by 2 so there seems to be
ok things in general but some of the
values are clearly still missing in
comparison to to this this whole claim
here so it says quality increases by 2
when there's ten days or less we saw
that and by 3 when there's 5 days or
less so we're gonna need the 5 days here
on the selling side so again more values
into whatever we're exploring so adding
those values I don't really care how the
other ones worked but I could also look
at those I care now mostly about leave
the concert tickets or so that I could
hit this so for the claim of 5 days or
less that the value goes up by 3 yeah on
161 it seems to be doing that so again
can use as much time as I feel I need to
verify the results before I accept them
or I can just go with the rule of works
in production it's legacy code we can't
change it anyway without talking to
other people who might be depending on
it so right now
you know on a shallow level at least I
think I have stuff around the
specification covered there's this
quality atheon so for us but I don't
really care about that much but I'm
curious on on how well am I doing with
my my exploration with the specification
just running it under code coverage
again and seeing how I'm doing so it
seems there's a lot of green right now
but there's some values here that are
somehow difficult or different so I see
a value of selling around 11 and I see a
value of quality around 50 and I really
want to avoid too much thinking right
now because again I'm mostly kind of
trying to understand how do I even get
this on the test and I can look against
the specification or my understanding
anything that I see from here so for
qualities values around 50 well we had
over 50 so let's say we put 49 there and
for sailings the value was 11 that was
mentioned there so we didn't have we
have 10 but we didn't have 11 so let's
just try these first run again our tests
what we have we can check whichever we
feel like checking right now I don't
feel like checking any of them I just go
and copy paste and accept my my results
make sure that my my tests are running
and see how I'm doing against my code
right now so I do not see yellow anymore
so seems like I I have now covered the
the code as well so again all the time
I'm exploring I am looking at at how how
things are so right now I think I've
covered the specification I've covered
the code what am I done
I don't think so
there are some of the things that I for
example know of but by my heart having
done this before
you can also give an input value that
would be something of this sort
so with leading zeros and what happens
with that then with leading zeros
it starts with assuming it is a value of
72 so it's clearly looking at it as
something that I did not know that I
inputted and from that interpretation
seems to be at least for any going down
by one which is exactly what what I had
in mind before so again you know I can
add all of this here and again now I
have a few more tests again that I can
run and well it won't change much of my
my code coverage because that isn't the
case that actually is in the code it's
more about the assumptions that we make
on the system so this is the demo that I
wanted to do with you and I kind of
wanted to show you this and then kind of
go back to the idea that I've done this
with many people who have never worked
with code and coaching people on doing
things like this it's still the same
thought process that we use with user
interfaces we have C boxes we put values
in them we need to somehow identify what
we're doing and what we're when do we
say we are we're going to be done so
this exercise is very much around
coverage so I just demoed you basically
exploratory unit testing of legacy code
legacy code is great in the sense that
you know if it works in some way even if
it's wrong we can talk about the way it
works wrong but we probably can't easily
fix it because somebody might have built
assumptions on it but we can explore on
unit test level just as well as as any
other test levels this just happens to
be a very small and nice exercise
to start with so that's why I wanted to
show that to you today I also showed you
how I combine kind of my ideas of the
world kind of things like oh maybe the
numbers are not just numbers as if we we
normally think of them maybe there's
other examples of numbers we covered the
whole specification but we also covered
the code that the specification alone
didn't drive us to cover so we looked at
different kinds of criterias of when we
would be done but there would still be
more you know I've only done this on my
own machine maybe there's other machines
other environments other dependencies
that we need to test so environment
coverage is definitely something to
still look into then I usually when I
demo I don't get to spend so much time
on the application I spend a little bit
more on this one today so I showed a
little bit deeper testing but there's
way more that we could explore around
this so somewhere maybe medium between
shallow and deep testing is what I was
showing today but the difference is
really on how we learn and the control
that we ourselves as testers take when
we're learning that's something that I
often look at on how people notice when
they learn or how many times they need
to try before they figure something out
needing to get things at once isn't
necessary you know trying things five
times is fine as long as as you keep on
actively asking yourself what am i
learning why am i doing more of this is
there any new information that is coming
my was also what I showed you is what I
would call disposable test automation we
started off with the asserts where I was
actually deleting the tests that I was
using just to explore in the beginning
but also towards the end we just kept
all of the values we went to a format
where it was really easy to add values
and more test cases so we ended up also
looking at kind of test automation as
documentation which is something that
you would have when you're exploring an
API or a piece of code
so from my perspective it's kind of like
exploratory testing was this box that I
put test automation in but I work with
other people who have a box of test
automation and they put exploratory
testing inside it and basically the
difference is just that for me when I
explore my focus is always on assuming
that I want to test something different
the next time you know I don't pay so
much attention of the I can keep these
for later on but I don't mind it's okay
if it gets created there and a lot of
the people that I work with who work
from the automation specialist
specialist side they first focus on
repeating and then they later add more
values so that they can do exactly the
same thing that I was was just demoing
for you so a lot of times this coaching
stuff with real example solving real
problems happens in a paired format the
way I do it with people face-to-face but
also over internet is with strong style
navigation so we do this with the thing
that whenever somebody has an idea the
other one needs to take the keyboard so
if I have the IDE on my machine and we
are doing this exercise with someone who
is remote they will use their words to
tell me what happens and nothing happens
unless they speak about it and the exact
same thing I do this a lot with mobs
groups of people it just scales into
more people contributing to the same
problem and mobs can be really
insightful figuring out the different
ways of how would you test this so this
is what I had to show you today an
example of exploratory testing of
something it could be anything you can
take your own application you can take
any piece of code you have on any level
bring together a pair or a group and
make sure that you're helping others see
how you would test it
fantastic thank you very much and so if
anybody has any questions there are a
few that came in or not that came in but
that I had but if anyone else has
questions go ahead and put those into
the questions panel now and we'll get
them asked but so Marie you were talking
about shallow versus deep testing is
that can you elaborate a little bit on
that and specifically sort of how you
differentiated between shallow and deep
testing while you were in the code is it
simply about just the different way you
question the application or was it more
about like the values that you used so I
would differentiate it like I usually
talk about this idea of kind of like we
are learning in layers I wasn't learning
much when I was demoing because I've
been doing this with about 50 groups so
far so I was doing things that I've seen
before so I wasn't really peeling any of
the layers so what I mean by shallow and
deep testing is how many layers were
peeling so I was more like introducing
layers into semi deep like a little bit
deeper but not very deep testing it but
I could also be doing like it depends on
how much time I have like how much am I
able to learn and pick up about the
application everyone else who was
watching this you haven't seen this
probably before and for you even
understanding what the application is
about what are the values that the
middle value is the selling and the last
value is the quality you're probably
just peeling those layers with a lot of
the examples that I'm showing at first
and that would leave you if you didn't
give yourself enough time it would leave
you on a more shallow level in your
ability great so another question was so
typically when people think of
exploratory testing they think and I
think you sort of mentioned this but
they typically think of testing through
the UI or or doing functional tests
but that's not what you did you you did
exploratory testing but on the unit test
level and so is that for someone who is
not used to that that might be a big
hurdle how do you suggest do just
suggest people try it do you think that
there is a big hurdle or that is that
just sort of a misconception so I think
there is a bit of a hurdle but easiest
way to get through that hurdle is is
finding one of your team's programmers
and doing it with them so they might
actually be having already ways of doing
things like this probably have already
some unit tests and with their guidance
you could just be focusing on the idea
of you know these are just boxes we need
to put values in them the values have a
meaning and they have a meaning for the
output that we are supposed to be saying
so I show this from the perspective of
code basically well today's exercise in
particular to to dispel some of the
delusions that you couldn't do it that
way but most of the testing that I do
myself as well is on the level of either
user interface or a higher level API I'm
just not comfortable waiting for the
whole product to be ready before I start
testing so that's why I work on on many
levels and finding someone who knows
more and works with you is a great way
of getting started fantastic
ok so we have a technical question how
did you set up differs as default a text
editor in Eclipse actually that might be
something that's good for like a follow
up unless it's a really quick answer so
I didn't actually set it up as default
in in Eclipse it is the default that has
been set for me for approval test so
it's part of the set up for approval
tests so approval tests uses this
concept of a reporter where we put when
it fails it pops up something it could
be a web page it could be a
a headless thing it could be a gift or
it could be different dev tools
depending on what I'm doing so that's
where it came from
it's part of my setup for for running
approval tests great and somebody else
asked how do you go about promoting mob
programming and pair programming in a
skeptical environment so usually by
mentioning it many many times that we
wouldn't have this problem if we were
moving for example but the practical way
that I usually do things is I ask people
to humor me for an hour or an hour and a
half and just try it I might even try to
avoid mentioning that we're doing
mobbing I'm just saying we're doing a
workshop and working together let's try
this out so usually through the the good
experiences of doing something and
having fun together that's where it
would catch his on the skeptical
environment they will probably talk to
you with more more effort than the one
and a half hours that goes into doing it
on trying to talk you out of it and I
know personally myself that when I
started ma being four years ago I would
not have believed that I would enjoy it
I actually wrote blog post that I
wouldn't and after I had done it for a
while I realized I had not only learned
to enjoy it but rewritten my history and
again remembered that I've been
programming since I was 12
or something about 12 14 and I had now
15 languages that I've programmed in so
most of my times goes with the tester
identity I don't work on the level of
code I work with programmers but I work
on the business concepts and value
concepts more but mo being brought me
again back to this this idea of I can
contribute on on that level too and it
rewrote my Kerouac history of how I
remembered my relationship with code
so that's an interesting distinction so
you and I think you've said this a
couple of times do you work with
programmers and you work with code and
you know how comfortable you understand
it but you you're not necessarily
programming right can you talk a little
bit about that so my main thing that I
read with code is is I look at pull
requests and I understand how many lines
are changing that's much more relevant
than what's the contents of it and I
understand what kind of business
concepts or feature concepts they're
changing and I pay attention to to those
because I work with programmers who
already spend all of their time on code
and we're really in my teens need people
who focus more on the value and the the
risks perspectives so for me it's more
of a choice of where I use my my my
available kinda like mind space I have a
limited space that I can use and it's
the same with developers and a lot of
times developers end up using their
space for code oriented things and
there's also the other perspective of
value in the actual end user running
environment and we will probably be
missing many things if we don't look at
that so that's just what I do so code is
a way for transferring that information
if the code and the person disagrees the
code wins always so that's what I care
about the code but most of my time goes
in and the idea of we are creating this
software for some real people and
someone needs to be caring for those
perspectives and that's I really like
that too and the other thing that I'll
say is that that sounds really
complimentary right so if programmers
are focused in one way and you're
focused on a complimentary way to sort
of help help tests like you're not
covering the same things you're working
in in your example focusing on sort of
the business impact and what what what
risks are involved
we had another question and so some
people say that all testing is
exploratory because testing is about
getting new information and exploration
is really the only way to get that new
information what is your take on that is
there testing that is not exploratory
and what would that look like so I've
been lucky or not having to work on
projects where testing isn't exploratory
for a long time but I do remember my
history of working in projects where we
prepare test cases for six months to get
ready for 30 days of acceptance testing
when the whole software is ready
and while the hands-on testing tries to
be exploratory there the 30 days and
learning in layers gives you so many
limitations that that's just not
exploratory testing in the same way that
I think of exploratory testing so we can
have a very limited way of what we can
learn while with testing and the level
of learning available and our ability to
react to that learning is what defines
how exploratory that testing is for me
so there are setups that I keep on
seeing where people are not doing
exploratory testing but I would say all
good testing ends up having exploratory
aspects to it great and that looks like
all the questions that we have unless
there are any last-minute people
pressing buttons or typing otherwise I
think we'll say thank you very much
and we learned a lot so thank you more
eight and hopefully I'm continuing to
pronounce that name your name in a
reasonable way but thank you very much
for your time and somebody just said
another just a great presentation and
there's there's thank yous coming in so
we'll call it there like I said this
will be available everyone will get a
email with a link
to the video and thank you very much is
there anything else that you'd like to
say before we go I'm good thanks for
coming all right thank you everyone and
have a great day
[Music]
[Applause]
[Music]
[Applause]
[Music]
[Applause]
[Music]
