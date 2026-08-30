---
title: "Maaret Pyhäjärvi"
video_id: yWJY1rDqLBI
url: https://www.youtube.com/watch?v=yWJY1rDqLBI
upload_date: 20150423
duration: 1:16:26
channel: SB Agile
tags: [iMovie]
---

# Maaret Pyhäjärvi

> Exploratory Testing - Explained and Experienced by Maaret Pyhäjärvi (April 2015)

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

few slides about SP agile first. Uh so
the mission uh we founded SP agile one
year ago.
Yeah. So we just realized it's the year
it's our year anniversary now. So
visualize some cake. Uh perhaps next
month we'll have some people to mark the
occasion.
Um yeah so the mission is to create a
living sustaining agile community. uh
provide inspiring new ideas about agile,
how we can apply it in our our daily
work and just fun opportunities to bring
people together in Santa Barbara uh
network, make friends and all of that.
And yeah, we're affiliated with the
scrum alliance and the agile alliance.
If you are working towards any sort of
scrum designation like a CSP or
something like that, we can provide
endorsement for units or something. Uh
you can ask me about that.
uh feedback. Uh we also uh would love to
hear what you think about our meetups
and how they were. And so at the end of
our meetup, you'll notice some yellow uh
high-tech forms on your on the table
here. We'd love it if you could take the
time to fill it out. And I should remind
you if uh memory serves. Um thanks to
Appfolio for sponsoring this event um
for sponsoring um our guests here. I
also want to introduce Luan Falco who is
another uh guest that is with us uh
today as well and thanks to Folio. Uh
yeah, so just some housekeeping things.
Uh there's garbage uh outside you
there's outside this office, you know,
pizza and salad. If you want more water
or anything, help yourself. And we have
a sheet at the back if anyone is looking
to trade information about uh uh job
possibilities.
I also want to announce our speaker next
month. We have Craig Lurman who will be
talking about uh largecale scrum and uh
we're very excited about that. So it's
on May 20th at 6 p.m. we'll be
announcing it on the meetup group.
Uh probably cake as well. We've got to
write that down. Yeah. And we're also
looking for speakers at SB Agile. We
would love it um to have more local uh
speakers. So if you have an idea of a
talk that you'd like to bring to the
group, we're all ears and we'll schedule
it in. So uh let us know.
Yeah. And also if you want to volunteer
for SB Agile, we uh have a regular uh
weekly halfhour call where we just talk
about um the direction of the group and
you know what might we bring to the
local area to help grow and develop uh
our our community. So, uh, just, uh, uh,
give let me know and some social media
stuff. You know, we're on meetup.com,
we're on LinkedIn, Twitter, all that
good stuff. And
yeah, so super excited uh, to introduce
once again Marit Puare.
Okay. Been practicing that. So, Marit is
actually um, she's here from Helsinki,
Finland. Has anyone been to Finland in
the room?
Okay. One.
Okay. Cool. Well, it's our chance to do
so going forward. So, um, MA uh
organizes several uh agile user groups
and communities uh in some international
and uh finish conferences related to
agile testing.
She is uh a a software testing
specialist at a product development
company uh in Finland uh specializing in
construction design and they do daily
continuous delivery without test
automation.
So that sounds interesting. Met is also
an avid blogger and you can find her on
visible quality.blogpot.com blogspot.com
also on Twitter Maritt P on Twitter but
you could just Google her name Marett
and the results will come to her her
work so it's pretty cool um yeah so
without further ado here's Mar
[Applause]
So we'll be talking about exploratory
testing.
Uh the idea with the talk, the things
that I want to share with you is that um
a lot of times we we just talk about
testing. But I wanted also in the short
talk that we'll have to have you
experience some of the stuff that it is
related to explor exploratory testing.
So we have a few exercises. So you need
to also you know be oriented to to do
some testing in the the session. Not
anything very complicated, not anything
very uh very uh complex but u a few
small exercises will be will be
included. Uh the uh things that we'll
talk about are related to testing in
general. So uh the way I see it is that
testing is really about feedback. It's
about finding things that are uh uh
unknown. It's about uh bringing them out
and having discussions around them. Some
of them might be bugs, some of them you
might want to fix and some of them you
might might not want to fix. But I feel
that uh in a many in many cases it's
been quite different to to do testing in
in agile context than it has been in in
a waterfall context context. Uh I
started off uh testing about 20 years
ago and we really didn't talk much about
agile at that point yet.
uh and now that I work mostly with agile
teams and and agile development, it's
kind of the way where I always take my
teams when I join my teams if they are
not yet yet doing that. I'm starting to
notice that a lot of the things that we
do in agile, it's kind of the best thing
that ever happened to testing. Back in
the days when I wasn't doing agile, it
was quite often that I would find some
problem and I would go and talk to
somebody about it and I would hear first
that well um yeah, it's kind of a
problem. Yeah, sure. But actually not a
problem. it's a new requirement that
you're talking about. Nobody wrote in
the specifications that it's supposed to
work this way. And then when it's not in
the specifications, what we would
basically do is we would put that thing
in a in a database somewhere. We would
hide it and it would never come back
from there. So it's kind of like a lot
of these uh information that you would
provide that nobody reacted on. There
were also some problems that I would
find where basically somebody would tell
me that well uh it's it's uh not so
relevant. uh we are so short with time
that at this point we're not going to do
anything and I could agree kind of yeah
sure it's not that important well sure
we can go into production with that but
again 500 typos sure we can go to
production but do we really want that so
uh all of these discussions were kind of
like all the time that that we'll
postpone that whatever we can and there
were also problems that were like really
relevant was like all over the the the
user interface you could see it very
visibly it actually blocked you from
doing important things and if you would
find these kind of problems one day
before you would go to production you
would actually often hear that well it
doesn't matter it's going live anyway so
a lot of times I would feel in the
non-aggile context that I was providing
information doing exactly the same
things that I do in an agile context but
uh a lot of the feedback that I was
giving uh wasn't as well received so for
me agile and agile testing in particular
it's been kind of like a life-changing
experience because now when I tell about
problems uh with the continuous is
delivery to to production. We can
actually whenever I find stuff uh we can
discuss that we can decide on on fixing
that and the whole tone of discussion
around problems and and and feedback
that I'm giving about the product, it's
quite different.
Uh even in the the uh non-aggile world,
I I've always done testing in a
particular certain way. Uh I've never
been big on on uh scripting my tests.
I've never been big on on uh writing
detailed instructions for myself or
others on how to do testing. So I've
always been in the world of of
exploration exploration because I
believe that's a way of uh finding
things in in a more like efficient way.
But what we'll start from is kind of
like giving you some ideas of of why
I've actually like learned to think
about testing the way I have. Uh we're
going to uh look at the a couple of of
numbers related to testing. So this is
my basics of testing mathematics. And
the reason why I'm showing this uh to uh
in in this this talk is that I used to
work in a in a university. Uh and I used
to talk to professors about my research
and my teaching about testing. And I
kept hearing from the professors that
actually what you're doing is not
testing. It's project management. It's
configuration management. It's risk
management. But it's never testing. And
usually uh that whatever they were
saying that that what I was talking
about is is whatever they were doing in
their own research area. So they were
kind of seeing similarities and and and
wanting to see that that actually it's
it's something different than software
testing. At some point I learned that
maybe it's actually better to ask them
what is testing then since apparently
I'm really bad at telling what is
testing like information gathering doing
using software none of it worked. So I
asked them and it turned out that they
think the research I was supposed to do
is is think of creating this magic
machine a black box where you put in a
specification and out comes all the test
cases that will find all the problems
like okay so we live in a bit different
world so just to emphasize the kind of
the world I live in I created this
testing mathematics that we'll go go
through together.
Uh the first number uh that we go
through is is number 20.
Uh number 20 is is related to uh uh uh a
kids game that I've noticed that people
in in US have been playing a lot more
than than my colleagues in Finland ever.
Uh 20 questions
and the idea with that game as you
probably uh have already uh idea of that
is that you have a limited budget just
like in testing you can't test
everything that they could be. It's just
not possible. Not even with automation.
There's always more that you can you can
add there. So, you need to somehow uh
find the best questions to ask. And
there's two different strategies on how
we could do this. Uh the traditional
strategy, the waterfall type of
strategy, uh the scripted type of
strategy would be actually to write the
test cases down before you start
testing. And then as quickly as
possible, you would run through the
tests. You would have the 20 questions
and you can ask them. But you can
imagine that when you're looking for
something that you don't actually know,
you don't know where it is, what it is,
you have pretty much no information, you
know there's a problem somewhere. It's
not the most uh efficient or effective
strategy strategy to do things and it
actually uh uh takes away time into
doing things that might not be as
relevant. So when you learn, you don't
take the learning in. So you kind of
like you don't change your your plans
and and and focus better. So, we'll play
the 20 questions. That's our first
testing exercise that we'll do today.
I've written something on the paper.
Actually, can't even remember what I
wrote. I need
Yeah. Oh, now I remember few words for
every time. So, I have a word on the
paper and as a team together, I want us
to find out with 20 questions what it
is. But we'll use the exploratory
testing strategy, which is that we can
think of all the questions in the world.
There's uh good questions related to
forking uh uh like a smaller area. You
probably have experience of that kind of
questions. Uh you might want to think as
many of those as you want. Get your
techniques up to a shape. But uh what
you do is you can ask a question. I will
answer yes, no, or I can't tell. And
then you can decide what is the next
question you want to ask based on the
information. Let's see if we can find
out what I what I wrote here. So anyone
willing to start? I always like say in
Finland in particular that uh if you
don't ask a question like maybe every 30
seconds, every 20 seconds, we're going
to use one question anyway because like
in testing if you're paralyzed and just
look at the the screen and you're not
doing anything. Time flies by anyway. So
you better get started.
So anyone wants to start?
Is it living?
Is it living? Yes, it's living.
How many letters is it? You need to say
something where I can answer yes or no.
Is it less than 10 letters?
Yes, it's less than 10 letters.
Is it the name of a person?
No, it's not a name of a person.
Is it an animal?
Yes, it's an animal.
Is it a mammal?
Uh, yes. It's a mammal.
Bigger than a bread box.
I can't tell.
That's one of the first questions.
Is it a herby war or a carnivore?
Uh, yes or no?
Is it a carnivore?
Yes, it's a carnivore.
Does it live on land?
Yes, it lives on land.
Is that a pet?
Yes, it's a pet.
Dog.
Yes, it's a dog.
or 10. I I got mixed up in the end
because I gave up on my my fingers. So,
but I need to check back on that. So,
again, uh when we're learning, when
we're listening when the software talks
back to us when we test and and we're
changing based on whatever the software
is telling us, it's a much more
efficient way, effective way of doing
things. You're actually finding new
information and you have much more a
higher likelihood of finding problems
that are actually hiding in the in the
software.
The second number that I have is number
16. And again, there's a small exercise
related to this. Uh, it's an exercise
about expecting the unexpected. So,
let's try if we're awake for doing some
testing together.
here.
[Music]
Some of you maybe have seen this or
similar thing, but I'm going to like as
a group exercise still going to go uh
walk you through the experience.
On the video, there's two teams passing
basketballs. There's people in white
shirts and there's people in black
shirts. And during the video, we're
supposed to calculate how many times
someone in white shirt is passing the
the ball to a white shirt player. So how
many times the white uh white uh pass
the ball?
Since this is a testing exercise, I have
a test case for you. Uh back in the days
uh before extra testing was big. Uh test
case design uh tools were big. We would
do uh test cases in the tools and we
would run them basically the questions
list of questions and we would say yes
or no, pass or fail. So uh the test case
has an expected result
uh which is 16. I would expect that 16
is the right answer for this. So for all
of you imagine uh filling in a test case
uh uh in in a tool you need to tell if
it's a pass exactly 16 or fail something
else and then of course reporting the
bugs related to to the fail. Are you
ready to test?
So, how many of you would say the test
was a pass? Exactly 16.
A few people. Okay. Did somebody get
more than 16?
Less than 16. Was there somebody who
wasn't uh patient enough to calculate
count?
That usually happens as well. Okay.
Anything else to report?
Gorilla.
Yeah, the gorilla.
Gorilla.
Which one of you saw the gorilla?
Gorilla.
We're talking about a gorilla, so it's
kind of like obvious thing. Let's go
back a bit. Still the same video. I'm
not changing anything. Just going back
on the video,
if you've ever seen this before, it's
kind of hard not to see the gorilla.
And on the second time, it's kind of
hard not to see him as well because he
kind of goes in and and bangs the the uh
chest and and leaves. So, it's uh kind
of obvious that there is a gorilla.
Do you have anything else to report on
the video?
The color change. The color of the
color change the curtain color. Did you
notice that?
I guess you did. Anything else?
There was one of the players uh the
black shirt players left the the field
in the middle of the game. It's probably
also kind of a at least in some way
relevant. The reason why I'm I'm having
you do this exercise
is is that um
when we're doing testing in particular
exploratory testing, we're actually
looking for the things that nobody knows
they are there. If there was a
specification or a test case uh or uh
some kind of a document saying that uh
that that here is a problem, the
developers probably could have also
checked that particular problem. The the
things are usually unexpected. they are
the uh things that we don't know that
they exist before we we run into them.
So, we're expected to kind of cover the
the software in a uh to to surface these
these unexpected unexpected things.
And uh the gorillas, the curtain color
changes, uh players leaving the field,
we're more likely to miss them if we
have a very detailed scripted case
telling us what to focus on. And again
if we find problems like this uh like
the gorillas uh if we have a test case
that says to count to 16 is it a pass or
a fail there were all these different
problems that were not mentioned in the
test case so there's always this idea
that that uh what do I actually set the
status of the test case to and we maybe
should be thinking of things in a bit
different way which leads numbers and
this 1639
is a number that reminds us that uh
there's different routes and that all
not all bugs
are are equal. So again, I have a a
video here because uh I'm nowadays not
on a Windows XP machine and this is
something that I would want to de demo
on on a Windows XP machine rather than
uh than on my Mac.
So uh uh we took a bit of a video on on
how things work uh on on on the the XP
machine. So on the video uh this is not
the same kind of video where you'll be
testing continuously.
On the video uh we basically uh using uh
word pack on a very simple feature we
add some text there and we want to
change the text size.
So, uh, to be able to see what there is,
we're going to first try to make it a
bit bigger and then
get to a point where we actually see the
text. So, there's the the little uh uh
box there. You see numbers going in
there? That's what we're testing with
this particular exercise.
Uh there was the number 1639
that we'll use.
I'm want I want to add it into the the
the font size box. And since we didn't
on the first exercise uh the 20
questions, we don't want to come up with
the questions in advance and uh we don't
want to have the expected results from
the second one. We don't want to have
them in detail. Now it's very important
to remember that we need to stop and
think what is the plausible thing that
would happen. what we imagine could or
should happen. So we need to actively
stop ourselves. That's part of of
exploration, being in control of how we
test. So if I uh write there 1639, what
do you expect will happen?
It will break. That's a I say typical
tester view that there's probably a
bucket there somewhere. But but like if
it works correctly, what would be a
correct behavior? What what what we
could expect?
the the font size will be really huge so
it keeps on growing. Okay. Anything
else? Anything
you will just get the max amount
you can't render a certain amount.
Yeah, it it might say that it can't
render a certain amount. So it might be
going over the the limit. So let's see
what happens. So we change that
gets to the right number, the magic
number and you press enter. And this is
what happens.
The number must be between 1 and 1638.
So there's a reason why I chose this
particular.
It's exactly on the limit. And that's
something that testers do a lot like
search the boundaries and and play with
the boundaries and try to to trick the
boundaries. Uh the thing with software
is that you can usually do things in
many ways. So uh this is not the only
way to change the font.
So you could also go into the stop that
again uh click uh right click on that
and and and you get into the font
dialogue where you can also do the same
thing. Now we've already stopped to
think what's the the the right uh way of
of working. So if I write there on the
size 1639 what would you expect to
happen?
Now same error it's again too big.
It's not.
So again, we write that there.
That's funny.
Sorry. That's what happens. Now we get
the other option. And I don't think you
can't see it, but uh it says there in
the the little box it says 1638.5.
Continue from here on. It gives you
gives you an error message. I think the
video has the error message. Like does
it? I don't know. I haven't actually
looked at the video that long. So I
usually stop here.
So, but uh uh when you're trying to get
to that and edit that, it's going to
give you the message that actually you
can't even enter that here. You can then
change it back to to smaller, but but
it's going to be kind of like keeping
you in the loop for a for a while. So,
the 1639
is basically teaching me or teaching us
uh about two things about exploratory
testing. One is that uh there's so many
routes through the program. It's
relevant actually what you do before and
what you do after uh whatever you're
testing. So you can find different
routes and and trying to come up with
these when you don't actually have the
software at your hands. It's going to be
much more difficult than actually
exploring the software intentionally
trying to find different ways of doing
the same functionality or imagining ways
where the functionality would be
connected. And when you find the bug
like we found the bug now it doesn't
work actually correctly because there's
a difference there. either one of them
should be different. Uh we notice also
that not all bugs are equal. It's not
really that relevant bug to fix that
particular one. Uh I think it's actually
more fun when they haven't fixed it
because I can show it and demo it in in
sessions like this. It's kind of a
problem when they fix it. And I imagine
uh like real users in this particular
case wouldn't mind that so much. It's
it's a minor annoyance. So we also need
to do uh decisions on on when we
actually don't fix all of the problems
and we need to decide when are we going
to use time on reporting problems
reporting problems because not all of
them are as relevant. The last one I
don't have an exercise for this still
but the last number is to remind us that
uh testing and software in general is
very complicated complex things there's
a lot of things to remember. There's a
concept called human envelope which
basically means that people can remember
only a certain limit certain number of
things. 5 plus minus 2 is somewhere in
mid 80s. It was 7 plus minus 2 uh in in
7879.
And there's an an update on the article
on 2001 saying 4 plus 1 is what we can
nowadays remember. That was 14 years ago
I think. So it's it's uh nowadays if you
remember one thing at a time you're
sometimes lucky. So you really even
though I talk about the questions and
coming up with the questions on the fly
when we do exploration we need an
anchor. We need something that helps us
remember the complicated multifaceted
things that we have. So we need to take
notes because otherwise we'll forget
things and we need to create reusable
notes that we can use as checklists.
It's really important.
So this all is about experience some of
the core stuff about exploration. So if
you had an idea of of how testing works
from a traditional point of view, a lot
of these experiences are kind of
conflicting uh with whatever you have uh
from from that side.
So uh exploration it's kind of like
looking at things from different
perspectives.
So typically in agile we would have
developers
uh with programming emphasis. We would
have developers with testing emphasis.
Someone might say programmers and QA
people. And uh typically you would look
uh with a different background with a
different uh point of view. You would
look at things differently. From one
angle it might look like a cat
the picture and from another angle it
might look like a bird. Or if you're a
professional uh testing person, you
might look at the picture and say um the
lines are not quite even. Sometimes it's
a bit like lighter there, they're not
connected properly. So maybe that's
relevant on how much you have pushed the
bend or you might see that there
geometric shapes. Maybe that's the
perspective that I would need to take.
So you can find a lot of different
perspectives into your your software and
that's what you bring into into testing
and that's the idea of exploratory
testing. So we take the perspectives and
we're trying to be disciplined about how
we put the perspectives together. The
most important tool to testing is a
person and the brain of that person. And
that tool is what we need to sharpen
when we do exploratory testing. It's an
approach. It's not a technique.
Sometimes in agile teams I see that
we're doing exploration for the last two
hours. We have this like time boxed
exploration. But basically how I do uh
testing or exploratory testing in my
team is that when I wake up in the
morning uh the first thing that I start
thinking about is is testing. Whenever I
I talk to developers and they answer to
me back on on what they advise me to
test, I'm actually exploring their
knowledge about what they think I should
do and I'm I'm enhancing that from my
own perspective. So the whole mindset of
of how I think is is exploring,
learning, putting things together and
finding the best way to learn from all
the various sources that we might have.
So it's really an approach, not a
technique. Uh it's it's a way of of
thinking whenever you're testing. It's
also exploring is a great way of
learning other things as well. But but
for the purposes of testing, that's what
we call exploratory testing. It's
defining the unknown unknowns. It's it's
to find the information that we don't
know that exists and and trying to be
effective about that. So sharpening the
tool which is your mind so that you
could uh come up with better ways of of
of uh coming up with ideas where to go
look for things. It's discipline. You
need to be able to tell your story of
what you're actually testing, how you're
testing, why you're doing what you're
doing, and what did you actually do.
It's not random banging at the keyboard.
It's a performance, not an artifact.
It's not the test cases that end up
there. You might have the same thing. We
were looking at the gorilla. You might
have the exact same thing on on the
computer screen and you're just there
sitting looking at the screen and
actually whatever happens in your head
that's the thing that happens in
testing. So it might be completely
different. You might be focusing on the
gorilla. You might be focusing on
counting. You might be focusing on the
curtain color or you might find
something completely different that
you're looking at. And and you can't
tell that from just the document that
says count to 16.
uh uh you can do uh exploratory
performance testing very easily. That's
actually how my team does performance
testing. So we have a basic idea of what
kind of things we want to measure in
performance and then we change things
around those. We add a bit more users.
That's explor exploration as well or we
we change the data in some way that we
find relevant or find new scenarios. We
do exploratory test automation uh uh
meaning test automation to make the uh
exploration more effective
uh uh for example handling massive
amounts of data uh uh getting that
somehow pre-processed so that then you
can have a person look at that and find
trends within the data and we do
exploratory regression testing uh
meaning uh whenever uh we find problems
related to regression they are of course
regression problems but the testing that
happens it's never exactly the same.
It's always somehow different. The data
is different. The user used it is
different. I have like pack of of
different users like this is created
three years ago and haven't been used
since. This is created two years ago and
haven't been used since. This I created
a minute ago. And they're all relevantly
different. I find different problems
when I use them. And I don't always use
them all of them, but but I try to kind
of like rotate between these different
ideas.
So you can kind of think of of
exploratory testing as as as fine-tuning
the the uh tool that is the the tester
the thinking tester. Uh I I kind of
compare it to uh learning to drive a
car. My sister a few years back went to
driving school and from her first lesson
she told me that she remembered only two
two things. She remember the teacher uh
take it take her to uh driving traffic.
She was so much panicking about driving
traffic after the first lesson that that
she couldn't remember anything else than
that and the fact that the teacher was
kind of cute. That was all that she came
back with and and she asked like can you
kind of like can you help me remember
like here's the stick and here's the
gear and then what did you do with each
of them? So then she was ready to kind
of like start putting the things into
practice that were theory until that
point. But she couldn't remember any of
that from her first lesson. And we learn
testing kind of same way as we learn to
drive the car. We learn first to to look
at at some aspects of it. We learn to to
focus on the details first or one kind
of detail and then we go go and and grow
from that so that we can think of
details and long-term plans at the same
time. We can have many different kinds
of ideas and we can put all kinds of
different ways of learning together with
whatever way we're we're doing doing our
testing and using our software. So it's
kind of like there's different things
that you need to learn individually and
then you can start putting them them
together.
Uh whenever I talk about exploratory
testing I get to hear that uh well
that's something we always do. We have
test cases but we still explore within
them. And that's actually true. You can
explore within test cases and and any
good testing person testing whoever is
doing testing would do that. It would
kind of be stupid to say that you were
asking about 16, I'm going to say pass
and I'm not going to tell that I saw the
gorilla. That would be foolish way of
doing testing ever. But uh giving it a
name, it's it's been us usually useful
and especially in agile saying that we
also need to have things that are not
the the the automated tests that are
kind of follow the script anyway that
don't add or change things as much. Uh
it's good to have a name for for the
thing that we need to need to have
there. And at least I feel so that uh uh
exploratory testing is the disciplined
uh way of doing manual testing. So I
require a bit more than than just like
banging on the keyboard and and doing
something for a couple of hours. There
should be a story that you can tell why
you're doing it. What did you actually
find out? Uh what did you do and and
what comes out of that? So you need to
be able to defend your choices.
It's kind of a a big thing in in uh
exploration. So the way I do this myself
usually or way the way I learned to to
think about this is is that I I uh
practiced a lot like I had an A4 leaflet
where I would uh have uh basically empty
sheets and I would imagine it being
split into four different areas the A4
sheet and every sheet on that paper was
a day of work. So, I would work one day
and and I would then turn the next page
and I would use Post-it notes to to put
uh stuff on on that that uh uh blank
paper. On one top corner, there's a
vision or a sandbox. That was usually
the paper that I kind of like could move
from day to another. And when there was
a new paper coming in, that means I
learned something new about my
responsibilities and my sandbox. So, I
could see that from my from my notes.
When did I change that? when did I
format the the the the few sentences
somehow differently and the sandbox was
basically describing what I'm doing like
for example I used to work at FCQ in an
installation team and we had all these
different teams responsible for all of
the different components into the
product
product and uh I my my note said that
I'm responsible for installations after
an installation I would typically uh
test firewall or fire uh virus
protection or stand control or whatever
different components to see that the
installation succeeded and the product
works and I usually like the other stuff
more because the installation is kind of
boring. It's like install and check and
install and check. So I would again just
to keep myself awake I would uh probably
uh explore a bit on the other areas. But
I needed to remember to go back to my
own area because that was my sandbox.
That was the the area that I was
supposed to leak. even though it was
okay for me to play a bit on the other
ones sandboxes, there was nobody else
coming on my sandbox to actually cover
all the aspects uh that that were there.
So I needed to kind of be in control of
of of where I spend my time. So it was
my mechanism of of remembering that
current charter was a thing where I
basically put a post note saying what
will I do today. Today I will test three
installations upgrade installations and
I'm going to do a bit more uh uh
detailed checking after those. So it's
going to take me a few hours for each.
So it means I'm I'm going to actually
spend a lot more after the installation
on that. And if I would notice that I
would do something different, it would
again work as an anchor for me to remind
me that hey, maybe I need to actually
continue tomorrow on the same work
because I thought in the morning it's
going to be whole days work. It can be a
five minute work just because I did all
the other stuff today instead of
focusing on whatever I was supposed to
be doing. Then there's stuff about
details. There's basically three kinds
of notes I I post there or put there. Uh
there's bugs, things that I find that
are not quite right. I can stop my my
testing the whatever I was doing trying
to cover right now. I can stop that and
and go report and talk about the bug
right away if I want to. But I can also
make just a quick note and spend the
whole tomorrow on on on investigating
them further trying to understand how
they reproduce and and what kind of uh
things there are. Then I have questions,
things I would like to go and ask which
I found really relevant to to make notes
of because I was I used to be the kind
of person who would go and ask more
questions as soon as they had them. And
it's very destructive for developers
when they get interrupted every five
minutes with a question. So rather have
like a few questions piled up and I also
learned that about half of my questions
I had already asked if I just stopped
and thought about them then I would have
the answer myself. And the third kind of
of detail that I would write is X is
basically ideas for regression test
cases for automation. I work in a team
uh where I'm the only tester. Everyone
else is a developer. So if I have an
idea of a thing I never want to do
again. Sharing that idea is very good
thing to do in agile. So I learned that
best by testing things I never want to
test again in that way.
And the last corner is about other
charters. Basically what will I spend
time on tomorrow? what else should I
spend days on? And and and all of this
like details and and and long-term
things. I get them uh with experience. I
do them like simultaneously, but I could
also take time on on just focusing today
on identifying new charters. So I don't
have to do all of it simultaneously, but
I can like the tester is in control.
That's the idea. So you find your own
style, what suits you best, and you do
all these either in the same day uh or
uh in different days. uh working as a
tester, thinking as a tester, being in
control, uh working as a tester,
thinking as a tester, being in control
as a tester. What you at least have to
get out of it is buck reports. You need
to tell somebody else that you solve
problems. There's a saying uh that a
tester that doesn't report bugs well,
it's kind of a refrigerator light that
is only on when the door is closed. Not
much use.
So you have to that's that's the minimal
thing that you have to add to be doing
exporting. You have to talk about the
problems you find. If the information is
just for you, it's not not good yet. But
there's also other stuff that you can
take out of this. All the ideas of other
charters, the ideas of exploration, you
can put them in whatever tool you have.
Excel is a good tool for this. And you
can prioritize them in a backlog way. So
whatever is on the top is what you
should be doing next. And at some point
you will be out of time. you can see
what you will not do and you can make
better decisions about how far are you
before you're done. Uh you can uh write
playbooks, playbooks and coverage out my
playbooks are pretty much uh documents
where uh I'm passing information for new
testers who were joining in the area
like like quick learning about why this
product exists types of the things that
I have like learned about the the
application at high level and coverage
outlines their checklists of of what
kind of features are there. I typically
create those while I test or update them
after after I've been testing a bit. So,
so they help me in the future sessions.
Uh there might be session sheets. Uh I
needed to do these for a project manager
who thought I'm not working if he can't
see uh in writing all the test cases
that I do. So as a as a like a
compromise, I would uh write down
whatever I was thinking while testing
instead of writing it in advance and and
just categorize that. That's session
sheets and session sheets typically
include also some kind of numbers and
metrics like where my time went set uh
setting things up so that I can start
testing testing actually covering the
product and and increasing coverage or
bugs I am stuck because I'm actually
reporting bugs that I didn't think I
would be needing to report at least I'm
not in this scale so only the testing
time will actually increase the coverage
knowing how much of your time goes into
testing it's a really powerful metric
and the uh different uh bugs, questions,
uh ideas for regression test cases and
and new sessions. Knowing how many of
those come out, that's another metric
that I typically get from the the
session sheets. I usually summarize them
in some way. There might be a manager
somewhere who's coaching. Uh in my
current organization, nobody's coaching
me. I'm coaching myself on testing. I
might be coaching developers
occasionally on doing these kind of
things. and and especially when you're
working in a team uh it's also relevant
to somehow summarize what's our
perception of quality and my favorite
way of of reporting quality in an
exploratory context is actually thumbs
version quality good uh uh something
that we probably should fix but we can
talk about that we shouldn't talk about
fix and how well do I know well uh eyes
closed I think it works maybe uh I know
something I've actually used it and I've
actually tried testing it to best of my
extent uh So, so you can quite easily
get that kind of information. And I
noticed at least at one of my companies
that it was a very powerful way of of
reporting about testing when you have 15
uh testers in a room with the product
manager saying we don't know anything
but it still doesn't work for the really
well for what we know so far. So, uh
it's kind of a different experience than
than having a a document that says that
we have this many bugs somewhere hidden.
So, the personal aspect of of it is is
relevant.
uh to do this the tester is in the core.
Tester is is uh and tester skills are in
the core. So one of the first things to
learn on how to do these kind of things
better is to find a cheat sheet. How
many of you have seen the Elizabeth
Hendrickson's cheat sheet on on expert
testing? Some of you have. This is a
really good twopage document. So instead
of writing a whole bunch of test cases
that will help you print this out, make
notes to it and print it out again and
make more notes to it. That's a really
great way of doing testing. It has these
ideas of how you would use a product so
that you can think in like you can use
it in a more versatile way. Like for
example, let's take a example there like
goldilocks. It's one of the huristics.
Goldilocks means uh too small uh just
right uh and too big. You probably know
that in the story. So whenever you have
a field where you can put for example
text into, don't put anything there. See
what happens.
Put just the thing that would be right
for it. And put something that is way
too big.
Uh there's also uh things like one of my
favorites there, interruptions. That's
the coffee break.
Leave the software in some state. uh
make a note where you left it and go for
lunch, go for coffee, talk to people and
when you go back try continuing from
where you were or at the end of the day
shut down your computer or don't shut
down your computer try different
scenarios what will happen and the some
of the problems I've seen from from this
is uh I've had systems where you
actually can't continue like it logs you
out but you can't even do the same thing
again to the point where you were left
off because it's somehow the data the
ids are now locked
So you will find problems and and this
is like a uh two uh pages of of uh
things that testers have learned in a
very concise format. So whatever your
role is when you do testing, this is
very valuable information. Uh this kind
of huristics on on how to do do things
there.
Uh there's also another a little longer
checklist that I advise you to go and
take a look at more. It's called
exploratory testing dynamics. It's by
James Bark and Michael Bolton. And
basically the idea with that four-page
document is that it it splits uh things
that you might want to think about into
four different boxes. There's things
that you might want to produce out of
your testing. The word products that
will help you and support you in
testing. I chose uh playbooks and and
and checklist for my thing, but there
might be a lot more ideas and there
actually is a lot more ideas in this
document on what your work products
might look like, what kind of models you
might want to create while you're doing
uh when you're documenting your testing.
the skills and tactics, individual
skills that you might want to learn to
be better at so that you can find the
like steering wheel uh and and trying to
put things together in the right order
so that you're kind of like unconscious
unconsciously doing them. So, uh shaping
the the individual skills, there's a
nice list of those skills. There's a
list of testing polarities which
basically means that you think kind of
like in the way of hot and cold, small
and small and big. Uh a long list of of
how you bring different perspectives in.
So if you have trouble of coming up with
a perspective, that's a really great
list for that. And then there's a test
strategy elements listed basically what
kind of things you might want to have
answers for when you think about quality
and testing of a product. So again, a
really good uh list in that sense. And
the part of that that I like kind of
best on on that list is the exploration
skills. There's three kinds of skills.
There's skills about self-management. My
A4 paper is basically self-management
only. Uh then you need to be able to do
testing. You need to be able to develop
ideas, find different sources and not
just take one source and and use that
but find all the sources and and
prioritize.
And then there's a lot of uh uh skills
about uh how do you actually examine the
product? How do you come up with the
different views and and look at things
things differently?
The tools you can use uh and you
probably should even consider using
automation. There's other tools as well
uh than than just uh creating your own
scripts. I'll have some of that on the
next slide. Uh the example that I have
down there is from uh one of my previous
employees employers um was working in an
insurance company and what we were
testing is basically an XML interface to
calculating pensions. The whole Finnish
nation, six million people, everybody's
pension is supposed to be calculated
correctly. We knew that out of that
sample there were error messages that
weren't supposed to be very common. The
number 67 code means means will be
handled manually.
So there shouldn't be too many of those
after our system is done. We expected it
to be like a half a percentage. It was
over 50%age. And it's very hard to
notice these kind of things if you're
doing individual things. So you are
supposed to think of how automation
enhances whatever you can do. So
exploratory is not against automation.
It's kind of like a way of thinking
thinking how you bring in automation.
And the other tools, my typical tools
are mind maps. You're not seeing the
mind map. It's just there to to remind
us about mind maps. There's usually some
kind of structure. You can see some
colors there and some kind of like
different groupings. There's usually
features that I identify, things that I
will put in the checklist when I work
with the product longer. I stop using
mind maps at that point, but when I
learn about the new feature, usually I
use a mindm first. Uh there's bugs that
I've seen. uh there's uh system level
ideas on the left hand side and then
there's uh things I would like to do on
on the on the bottom right. So everybody
has their own style usually on on doing
these but the idea is that you can
change the structure.
Another tool that I use quite much uh in
some organizations that are not yet
buying into the exploration idea is the
little yellow thing there up there. It's
called rapid reporter. It's this little
uh field where you can write text uh
with different labels. There's test and
and bug and setup and and note and and
config and and all sorts of different
labels that you can use. You can set
them up whatever way you want to set
them up. It follows the time how long
you've been testing and it kind kind of
also keeps track of how much time am I
for example using on the test category
calculating between different labels. So
it enables me to create uh reports out
of the data automatically.
But to write down everything that I'm
trying to do right now, I don't do that
in most of my my projects. But uh
sometimes there are people who kind of
feel that uh to get out of test cases,
you need to have something that is as
rigorous and that's the way that I I
tend to then then do things. Uh this uh
Windows software thing. So if you're
working on some other environment, I
tester for example is for the mobile
applications. So like the uh that's
another note takingaking pretty much the
same same kind of thing as as that one
except of course with Siri uh on on
Apple Apple side you can talk to it and
it can make notes for you based on that.
So it's kind of a nice tool.
So all of this exploration stuff it's
really about finding information.
I don't go and I break the software. The
software was already broken when I came
just like anyone who uses it for testing
purposes. It was already broken. We just
searched that. So the only thing that
gets broken by testing is the illusions.
And there's certain kinds of or
different kinds of illusions. I kind of
list the basic kinds here. There's a
illusion that we think that the code
does what it's supposed to do. And
that's the first illusion that everybody
kind of buys into that we need to find
the bugs. We need to find the things
where it doesn't work at all the way we
we meant it to work. But there's an
equally important illusion thinking that
the product does what it needs to do.
Like from the perspective of the user,
we find new features.
And in agile, I think one of the biggest
and strongest things that I've
experienced is is that uh we no longer
in my team, we no longer care if it's a
bug or a new feature. We care if it has
value for the end user and how it's
visible for the end user. So we might
want to break illusions about that as
well. Then there's illusions about your
process uh being able to deliver with a
change in mind when you start changing
things. Will it break? Uh Heidi was
mentioning that we do continuous deploy
uh continuous delivery without test
automation uh architectures and and as
trying to keep the code as clean as we
can within our skills. It's a big part
in not breaking it even if we don't have
that much test automation. And then
there's of course exploration that uh is
based on on discussions that that we
have there. And then uh the fourth uh
illusion that we typically or I
typically at least work with this is the
business side of it. The business model.
Do we even need this feature? It was uh
on the backlog very high priority. But
have we actually talked to the end users
that we wanted? Is this actually going
to respond to their need? Uh is the
money coming in the way we thought it
would come? like there's a business
model way of work. So on that level
there's also like a lot of illusions
that need to be broken and all of this
stuff. Uh I find that exploration is a
exploratory testing is a great way of of
learning about these things and pacing
them together in a in a way that
supports the the organization quite
nicely.
It's really about serendipity lucky
accidents and and patience continuing
what you do like not giving up after two
hours. You test it for two hours you are
not anywhere yet. You actually need to
give it time. It's a learning process.
Any learning takes time. Serendipity,
the lucky accident. It's it's the idea
that uh it seems that testers tend to be
more lucky in running into problems and
than people with other roles. There's
two reasons. The more I practice, the
more luckier I get. So, you start seeing
things, you start like building that
kind of information into you. But also
uh uh there seems to be something
inherently uh different in in people who
end up being testers. So that they just
somehow do things in a way where they
they just stumble on the problems
sometimes even by accident. And
exploration is a way of of kind of uh
begging that accident to happen. So
giving it more chances that that you
will run into that. And perseverance is
really about keeping trying like
continue. Don't give up on two hours.
You tested it for two hours. It's now
done. It takes time. You develop your
ideas. You you come up with new
perspectives. You sleep a night and you
come up with a fresh eyes and and you
pick your own results and break it and
find find new ways of looking at it. I
think this is an Einstein quote. It's
not that I'm so smart. It's just that I
stay with the problems longer.
And and that's kind of the the attitude
that you need to do. And if you actually
do love testing, if you like doing it,
it's a lot easier to do this stuff. And
I feel that's one of my my core things
that I I've learned.
I find that the world has already
changed. We used to do this like
traditional testing. I call that
commodity testing like having the manual
uh automation replacements.
Uh my habit nowadays is to outsource
that to India and then get rid of it
because when it's further away from our
office then then we get to the
exploration side much easier like not
focusing on that. It's it's easier to
see the value when it's it's further
away. So we get to the the other side.
So uh commodity testers from that we're
kind of moving more towards skilled
testers, explorers uh of products and
businesses testing as a performance
and all of this we do in the agile
context mostly nowadays. So uh this is
RSD's uh rapid software testing agile
testing ecosystem. I really like this
way of thinking about what is included
in in in testing in an exploratory way.
You discover something that is worth
building. you uh develop the design. You
do all kinds of testing already to
develop the design uh to talk about what
you're actually building. Then you build
some of it. Uh you build that as cleanly
as simply as you can because you want to
build uh with a change in mind.
Uh you foster testability so that uh you
have the change actually in mind. So you
can actually do that again and again.
You can go through the cycles without
problems. You study what you've built by
imaginatively and suspicially
suspicially uh experimenting. You kind
of do this like deep testing that
doesn't happen just by quickly checking
that it's okay but you actually like
investigate from various perspectives.
That's where I spend most of my time on
and again from that you might find new
requirements you might find bugs and the
whole cycle goes on on again and there's
all these kinds of things that you can
do in like different corners testing
wise and I advise you kind like to take
maybe a bit better time and and looking
at at stuff that there is but this is
kind of the cycle so testing is the
feedback that we have in in agile agile
as as such and we just share it for the
whole team instead of just the the
tester
So that's what I had on my slides like
to invite questions, thoughts and and
feedback at this point.
Anything you want to ask, comment? Does
this sound familiar?
How how long have you been investing?
Uh I started in 1995,
20 years about
I was a developer for about seven, eight
months at some point. I was convinced
that uh testers are not respected. Then
I learned that average developers or
below average developers, whatever you
want to say, they are not respected even
as much as good testers. And nowadays I
find it that um it's kind of nice to be
the best paid person in my team even
though I have developers in my team and
architects. So I actually on the
architect salary. So uh there is a lot
of like uh when you actually practice
this and you finetune your skills then
it's It's kind of it's definitely not an
unrespected position in any way anymore,
but it's it's more about not accepting
to be converted, not accept except ex
accepting to to kind of take
instructions from outside and being a
passive person, but it's more about the
activity.
Does this sound familiar to you?
How many of you do export investing in
organizations?
some of you
towards that direction. Okay,
you're look you're looking nervous.
I'm like, well, we kind of do. I don't
testing. I thought was interesting. I'm
I'm actually in the UX uh department,
but I thought a lot of this stuff kind
of related to what we do and some of
usability testing we do. We actually do
write these tasks and we have our our
customers follow through these tasks,
but we kind of uncover other things
while we're doing it. And um I think
it's interesting sometimes to not be too
restricted to just those tasks that you
might have. And yeah, it's a little bit
more external facing. But
yeah, this is more like learning. It's
really about learning. What's the way
that you learn about products and and
and you usually have different people
with different perspectives on what kind
of thing you're about to learn. Some
people might look at the usability stuff
more. Some might look at the
functionality stuff more. And at least I
uh from my perspective I'm kind of used
to looking at usability, security and
and functionality as the three top
priority performance as fourth
as as the kind of like highest priority
things that I I need to kind of give
feedback on.
just uh tends to build up.
Um I think exploratory testing rather
than following a strict very detailed
script and response to that is like well
how do I ensure quality then how do I
you know make sure that the right stuff
gets tested how do I audit it how do and
and thinking about that you know that
that's the exact same set of questions
that comes up when people first hear
about agile and you know um what do you
mean we just write a story and we don't
write a specification document that's
100 pages to outline every case that the
software is going to do. You mean we can
just trust people to you know have these
discussions and collaborate. So um my my
question is you know how how do you
ensure quality when when you're using
that approach and because the answer to
how do you ensure that people are
building good software when you're not
specifying every detail is not it just
works better. It's there are a number of
techniques that ensure that like
collaborating more certain you know
there are certain principles behind
that. Can you elaborate on some of the
principles that make that possible with
exploratory testing?
Uh
just like with test cases you usually
have some kind of structure that helps
you remember things. I just opened this
this one example. It's ciphered work
really well because it's in Finnish. I
couldn't get the the English version to
show up.
There's also stuff in in English there
because I shared this with a a Romanian
tester at some point and we had to kind
of have two different languages there
side by side then.
So uh just like uh with the the
traditional stuff uh the test case
oriented things you can still like have
things that you have on your checklist
that you need to remember to test all of
these. They are just on a much higher
level. There's like for example there
this says equipment history. It's a
feature that we have and then uh there's
details hidden here which basically says
that uh the things that um uh kind of on
the detail level are are difficult to
remember difficult to find out they are
usually written here. So if there's
nothing uh that doesn't come from it
just doesn't show show properly here but
it's if there's something that you can
kind of like easily deduct we don't
write it down. So it's not like saying
we don't have any checklist at all. But
for example, when we do uh we do a
feature, we don't test all of these
every time. We basically we sample we
sample on the the the different
browsers. We sample on the different
features and it's kind of based on the
idea that I I've talked to the
developers and I've used the product for
a while so I know which areas are
connected. So if you change this area, I
need to also spend time here to see if
there's a an invitation. So uh that's
one of the ways and the other technique
is is the for auditing purposes if you
take a video all the testing you do and
you write notes all the time to go for
the video uh you don't have even that
detail of of like rigorous ri
vigorousness uh with the old style. So
there's just like a different techniques
and doing the same thing.
So I've been observing Mar's testing for
a while from bit of an outsider view. I
come from the Apple world where most of
our testing is automated. So this idea
that you could do continuous deployment
without automated test was unheard of
for me. Uh so one of the things I know
is really can you show really quickly
the um
the dark function code or the dark
function uh product.
So
this is a little piece of software that
we were using for a sample to see sort
of how testing works uh from this point
of view. I'm just going to show it to
you really quickly to get an idea of
like how she dissects software. This was
something that was really kind of odd to
me.
Uh where is
you can set the play button top
down
watch
do it.
It's a bit slow.
So this is sort of like a little sprite
thingy.
Yeah. Just really quickly sort of show
them your basics of how this program
works.
show where's my
data.
So the idea with the program is is
basically you have this sprite either
individual sprites or sprite sheets
where you have uh different animation
pieces that you can put together. You
can identify the different elements here
and then you can create your the
animation so that you can have like a a
moving GIF animated GIF or you can have
uh the coordinates in the sprite sheet
so that you can use it in your game
application to animate your characters.
So it's it's that kind of very simple
editor application.
Right. And I had the same sort of
thought. This is fairly simple. Can you
show them the mind map you made for
this? Uh, I'm not online, so I'm not
sure if I can.
I need the the U web for that cuz it's
it's on it's not online.
Connected to the internet.
Do you have an Ethernet? Could you
connect to that?
No,
I wasn't expecting.
I have a hot spot.
Where's this going?
Okay. Do you have an internet cable?
Thunderbolt adapter.
Thank you. Is there a doctor in the
house?
We have loads of these different
short
[Music]
unlike USB. It works on a second try.
I don't know if I have it on.
Nope.
It's not that simple.
It usually takes a couple seconds.
Try it again.
Nope.
It's very small, but the mind map is
actually here.
See if I can take that one.
Make it significantly bigger cuz then
you can see that it's a work around.
It looks like it might be connected.
Skype woke up. So it means this one just
woke up.
I need to find it somewhere. It's of
course not here.
So for that very simple program and this
is probably representing about two and a
half three hours worth of mind mapping.
This is the map that she's come up with,
right?
I don't know yet of any pretty much
anything about the product,
right? But from my point of view, there
should be like three elements on this
map, right? and she has like this huge
topology and when she goes and tests it
you'll see her sort of being like well I
haven't been in this area for a while
let me go over here I haven't been in
this area like so rather than having
like a set checklist like that we just
saw there I see her a lot more having
this sort of a much more detailed map
than I would ever create and then her
sort of saying which areas have I have I
not been to and that tends to be more
the methodology I've seen her use to to
get this kind of robustness in coverage
that
I was trying to do by lots of test
cases.
Does that
Yeah, that's that's really cool.
And then back to your point earlier
about playing 20 questions, right?
That's the when you're in then in there
exploring it, you're listening to what
it's telling you and that may take you
to place the map than you thought you
were going to go.
And like for example, on this map, you
see the pink areas there. There's
questions like overlapping areas marked
in a file. There's things that I don't
know how they will work and I will
probably investigate further or there's
just things that I already notice while
I'm looking at something else. And then
it's kind of like my way of of marking
down that I I need to look at this more
in more detail and and there's more
colors coming in as as I kind of I've
covered this and I'm happy with this and
it just keeps growing and at some point
uh when the if the product doesn't
change much uh I just turn this into a
checklist which is basically the format
that I showed you in Excel because
usually then you you have to test all of
this stuff in different environments.
It's on a Mac and it's on a Windows
machine and and it's on a slow machine
and fast machine and there's a lot of
these different polarities that you take
into account.
It reminds me of the idea in an agile
story that it's it's not a complete
specification. It's a placeholder for a
conversation. And it seems like each of
these isn't a detailed stepbystep test
case. It's a placeholder for exploring
something.
Yeah, it's a good way of putting it. So
you don't use automation at all for
those regression tasks. You just have
this checklist.
When I started three years ago in the
company, they had already been doing the
software for about 20 years. There were
different uh versions of the software
that I'm testing right now and they had
never had a tester there. They had not
done automation either. So they just put
it in production and they they survived
and they did once a month.
Uh and when I joined I started making
the developers do automation and I
started doing testing myself and and the
visibility kind of started improving on
on what we had and just me alone and the
20 developers in two teams there was
more to fix than they could do in a
year.
So we didn't really need more testers
there
like that's that's the point.
So uh but again uh it wasn't not an
agile
shop. It was not the kind of shop where
you would actually like build with
testing and testability in mind. Just
kind of the opposite. Uh we had a
problem with the unit test that we were
adding that people are not very good at
unit tests but they don't have the
practice
and they still add them after the fact
that our test development is way too
difficult for them still at this moment.
So after three years we did some unit
testing for like about a year and and
nowadays when we have changed the
architecture they just vanish the unit
test. they don't even tell that they are
taking them out but they banish the old
unit test. So they don't stay together
for for more complex changes and they
give up on them. So so even though we
have been building automation it's a
very low level and we've add added uh
selenium tests about last six months
we've been doing selenium tests those
are actually been like starting to get
in a pretty good shape. they actually
find relevant problems and developers
are really into them. And we have these
what we call automation checks or
database checks basically which is uh
kind of monitoring the production on a
daily basis seeing certain types of of
patterns happen in production then we
can talk with the end users more about
what they're actually doing. So kind of
like the feedback loop towards the end
users is something we've been automating
but uh the level of automation is so low
still after a few years that it's almost
non-existent.
But we're working on it. Maybe next five
years they'll get something done.
But you don't you haven't decided
intentionally that it's not worth the
effort and I'm not going to pursue it.
It's definitely worth the effort because
um even though testers as personality
tend to be more patient than developers
like testers uh tolerate tedium whereas
developers automate tedium. That's a
really good pair to to have. uh uh three
years with the same product uh even I'm
starting to find sometimes difficulties
in coming up with new perspectives and
I'm heavily dependent on meeting people
in meetups like this so that I can keep
myself my my machine in a shape let's
say that way
the thinking machine like if you get
bored that's kind of the end of it so
you need to find ways of of keeping
yourself engaged
and people is my way of keeping myself
engaged
I have a question about this seems to be
heavily reliant on the person's ability
to be creative and investigate things.
So how do you train that or how do you
find the right person and
how do you train that?
I had uh for about two years I had a
tester a junior tester from Romania join
our team.
Uh she did a talk about year ago in
Euroar uh on her first experiences. It
was called uh fooled by the unknown
unknowns because basically what she did
is she tested the her first feature. She
thought she was done and I took a look
at it and I showed her that it wasn't
done at all. So that's the difference
between like non-experienced and
unexperienced. But what basically she
took from that experience is that she
learned the types of things I would pay
attention to and we started pairing a
lot more after that and sharing
information. So the coaching pairing uh
uh talking around a mind map what do you
have here and what did you mean by this?
Please explain your rationale to me like
why do you have these and what did you
put in first and and what are you going
to do next on the mind map level those
qu those discussions are the way that
you coach new people into this and I've
seen uh old testers old testers in the
sense that they've always been doing
things based on test cases I've seen
them pick this up uh I've had problems
with certain people not picking it up uh
I remember one lady in particular who
had the idea that she doesn't test
anything if there's not specific
requirement about that.
So, uh if you if you are kind of set on
on the idea that that you're not
supposed to be active, you need to first
overcome that, of course. But even
juniors, they actually start producing
really quickly when they're told that
they're supposed to explore and and they
are supposed to be able to talk about
what they've done and what they've
learned.
Right now in my team, one of the
developers has decided to become a
tester. It's been an interesting
experience for the last couple of months
because he's saying that uh he never
understood before what I actually do,
but now that he's trying to do it, it's
like a whole different world. There's so
many different aspects to that looking
forward to getting him to talk to us so
that could share that that experience.
But it's more of the learning to think
in not just the one route that could
work, but learning to think about the
other routes that might not work.
Other ideas, questions?
You at one point you mentioned that you
often times in your testing you uncover
business cases that might not longer be
needed like a P3. How do you uncover
that with testing? Uh I usually talk a
lot with the business people knowing
what they're using the product on. uh I
have direct connections through business
to our end users and from those
discussions I'm learning just as much as
from any other document uh then I make
an assumption that this might be
something like that and I go and ask so
it's basically I'm just connecting bits
and pieces that I learned from all
around and I'm I'm surfacing those
discussions
and again if there's a feature we no
longer use getting rid of that is it's a
huge timesaver
so uh thinking about uh is there
actually use for things. It's it's it's
just about it's the thinking about the
different aspects that you might want to
report on.
I think I have that experience every
day.
I feel like you're in if you're into the
product as much as somebody who's doing
testing, uh you realize uh what's
relevant and what's not anymore as
opposed to anybody else in the company
who doesn't look at it in that level of
detail. And again a lot of times like in
the old world testers were told that
they are not supposed to report on
feature requests. They are not supposed
to report on on things that uh could be
like unused features. But in agile we're
actually trying to together build the
product and any kind of information
might be relevant. So it's more about
allowing that kind of freedoms and and
and again remembering what was my
sandbox. If I start only investigating
the business side, am I going to look at
the the current state of the program? So
you need to be like you can uh go to
another thing but you need to remember
to come back to wherever you were so
that you don't forget that the the next
release and whatever testing you're
supposed to be doing on that that's kind
of well one of the priorities that you
need to cover. So you are kind of
thinking on on many different levels
continuously
and again you share this in a team. It's
not just the tester it's the team that
does this. But one of the challenges
that I have with my team is that my
developers uh I I used to say that they
are really bad at testing but now that I
sit with them uh when they demo that
means testing when I'm in the room and I
see them demo and find a lot of problems
uh I've started to see that um I've
learned from this concept of uh holding
the space and I seem to be holding a
space for quality and problems for my
team. So that just me in the room makes
them behave differently. They become
really good testers when I'm signing as
long as I'm in the same room.
Mhm.
L was was telling about this this idea
that if you have if you have kids and
and you have a mother or or father in
the same room, not even looking at the
kids, the kids behave differently. So,
it's kind of the same that they know
that uh quality and testing is something
very dear to my heart. So, it's very
easy to kind of see them.
I don't need to say anything. They just
do things because nothing.
And I think Luan has the same experience
on on being a technical coach that code
starts to look much more good when when
he's just quietly sitting and and being
there. And you might notice that you
have something some something of
yourself that you kind of bought the
space for that people expect of you. And
then when you show up then, oh, we need
to take notes of this meeting, for
example. There might be that kind of
things.
Anything else?
Okay, if we're ending, I'm I have like a
personal request in the end. Uh like I
mentioned L and many times we're we're
dating and uh he lives in San Diego and
I live in Finland. He's actually moving
to Finland for a while. We're hoping to
get back to this very sunny nice weather
in this area.
So if you know any work in this area, I
would very much appreciate the the hints
on on finding me a job here. I will need
to like relocate from Finland. So
there's all the visa stuff of course,
but if you have any hints on on how to
approach that, I will be very happy to
to discuss that. Thanks so much.
Wonderful. And uh thank you so much,
Mara.
And we do have these feedback forms if
you
