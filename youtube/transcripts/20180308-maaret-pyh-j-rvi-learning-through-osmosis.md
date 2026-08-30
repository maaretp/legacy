---
title: "Maaret Pyhäjärvi: Learning through Osmosis"
video_id: F1V_JcpfWiY
url: https://www.youtube.com/watch?v=F1V_JcpfWiY
upload_date: 20180308
duration: 48:39
channel: Agile Testing Days
tags: [osmosis, mob programming, mobbing, mob testing, pairing, coding, testing, agile, programming]
---

# Maaret Pyhäjärvi: Learning through Osmosis

> Working in a mob teaches everyone things they did not set out to learn
> 
> Many different roles contribute to building software: product owners, business specialists. testers. Yet knowledge of programming keeps these roles at a distance. In this talk, Maaret Pyhäjärvi will share how she has come to programming: not through wanting to program and taking courses on it, but through working with programmers in a style called mob programming. This talk serves as an inspiration for programmers to invite non-programmers to learning code a layer at a time, immersed in the experience of creating software together to transform the ability to deliver. Lessons specific to skill sets rub in both ways, leaving everyone better off after the experience.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

[Music]
[Applause]
so I don't think I'm sensitive but I do
try to listen to people and I know a lot
of people who are more sensitive than I
am and I do try to be their voice I
didn't get the song that I chose which
is fine but I would have really wanted
you to hear the song by Sarah Burrell
I want to see you be brave that's kind
of my message for all of you and all of
the talks that I really deliver are
about me kind of going a little bit
above her outside my comfort zone trying
things that I don't believe in and
figuring out that they are things that
make a hundred eighty degree turn on my
career and I've pivoted on so many
things over the years that it seems
crazy I used to do test cases now I do
exploratory testing I used to believe
that I need to warn people about
automation and now I know that warning
about automation it's the energy that we
need in developing automation and the
talk that I'm gonna be doing today is
basically it's on more programming and a
particular style of of communicating in
a group so that we end up learning from
the others the things that we didn't
even expect nowadays I identify well I
of course I always have identified as
long as I can remember as a tester I am
a tester at heart but when I need to
introduce myself to people who are not
from the software community I often say
that I'm a feedback fairy you know I
come to my team with a bit of news
things that they can react on so I'd
bring them the gift of feedback and when
they welcome that they can actually do
some awesome things with with that and
the identity of a tester I've been with
that for over 20 years
but in the last three years I've been
adding stuff to my identity and in
particular on this
I'm kind of not mentioned I've become a
polyglot programmer and I'm kind of
happy nowadays to say that I identify in
that group group as well I do lots of
other stuff as well but we can talk
about those those things afterwards if
if needed the thing that we are talking
about today is learning through osmosis
osmosis is this chemical reaction and it
speaks volumes to me because when I was
growing up I wanted to be a chemical
engineer I didn't want to be a software
engineer I wanted to be a chemical
engineer I went as my first year in the
university I went to study chemistry and
my doctors told me that it's gonna kill
me probably in two years if I continue
because I'm so allergic to all the
chemicals and when I saw my friends who
were not allergic to almost suffocating
in some of the organic chemistry labs I
decided that maybe my doctors are right
even though I was stubbornly you know
going for for that fourth for a moment
in time but osmosis is kind of one of
the things that you know I have a
history with it and on and this idea of
of of somehow things moving without a
lot of energy or effort putting in into
that so it's a reaction that makes
things move without energy and you know
learning usually requires us a lot of
energy so I wanted to talk about this
very specific way of learning that I
didn't even recognize that it was
learning until afterwards I could say
that I had learned something that I
never would have thought was possible so
the reaction for me this is me at a very
young age and the other one is me at a
little older age my name
Marit it comes from this idea of a lapis
girl so someone from the northern
Finland so my mom used to make me wear
those those sloppy stresses because she
thought it was cute and that's just
about the only picture that I dare to
show from my childhood but that little
girl she was raised to be self certain
she was raised to make sure that she
knows her things at school I remember
that one
the things that really identified me
that I was always prepared
I had this Swedish teacher at my school
and every time I went to the Swedish
classes she made me translate the texts
and I had this reputation in my class
that I could translate Swedish word by
word exactly as it was but nobody knew
my dirty little secret I worked like
crazy translating it in advance word by
word because I was so afraid of having
to speak up in the class so I became
very much like an individual contributor
and looking back still three years ago
when I started learning pair programming
pair testing and actively making myself
uncomfortable by working very very
closely with others I would have said
that I'm more of an individual
contributor and I'm most likely going to
be uncomfortable if I have to be very
close close with others so there's been
a big change in in that mindset and
we're going to talk about how that
experience happened so the thing that
really changed my mind
in a way that I can only talk about in
hindsight I could not have told this
story in advance it's finding more
programming so I want to share my story
on how that that's happened for me a few
years ago I was speaking at a conference
in in UK test bash and my story back
then was that I felt very different in
my team I was back then not yet that
f-secure I was in a different company
and I was working in this team of 10
developers as the only tester I was the
only tester I was the person who laugh
out loud when I found a bug like this is
so cool no one can do this on purpose
this is amazing look at this and they
would look at me like hmm it's great
you're having fun and you know they were
very nice and they fixed all the bugs
and they were saying thank you and we
had great collaboration as such so they
were welcoming the gift of feedback but
they didn't really understand why would
I get so you know hyped up about this
this whole finding box thing
on the other hand when they would talk
about things like JavaScript and new
libraries and and you know let's try the
the c-sharp next version and maybe we
can do it you know only to some of the
classes in in our projects I was like
hah so you know everyone has their own
thing so that was kind of our our
division we were respectful to each
other but we had very different things
that we were interested in it wasn't
only that I was a tester that made me
different I was also the first woman who
had worked as in the software
engineering discipline in that company
and there wasn't another woman anywhere
nearby because it was an engineering
company they were already very few women
and even in the software engineering was
even narrower so a lot of times I needed
to hear jokes and and things that I
thought that don't just happen so much
in Finland because again in Finland for
example we don't have the word he and
she there's just one word for those so
so some of the discussions are not not
quite so generally but in this place I
really stuck out the things that I would
do in this team is really testing so my
idea of testing was that that I would go
about and instead of breaking the code I
would just you know identify things that
people believe in and I would show
evidence if those beliefs were not
founded so I was in the business of
breaking people solutions some of the
illusions were around the features that
we needed to build like and one of my
favorite illusions related to break back
then was this idea that we needed to
build this feature that would take us a
significant amount of time I made the
sales people sell that feature before we
built any of it and the customer
wouldn't pay 20% in advance which
actually then revealed that they would
not have been paid paid the money after
all so I was kind of identifying these
these different kind of illusions and
that that was my my job there but when I
was supposed to do anything more
technical code
Oriented maybe I've said that rather
that way I would get comments like this
I had colleague who regularly made jokes
about how women don't write anything
except comments in code and this isn't
exactly an inviting thing to you know go
and start writing code where someone
says this to you and I was like you know
I'm smiling don't touch me you know I'm
a tester I don't need to code I don't
care about coding it's not part of my
identity three years ago not part of my
identity
this doesn't touch me and after the
identity change this definitely touches
me so a lot of times I realized that
being a tester it's very gender safe
place to be in this industry because we
have amazingly equal representation in
in this community and it's lovely to see
in this conference how well you're
succeeded on on that so that's awesome I
also identified very strongly with this
dislike of programming I don't want to
do it and it's actually funny now that I
actually do like it after three years
it's funny to realize that actually I've
wrote my first program at age of 15 it
was called test if you're popular
you know girls tend to like doing tests
the women's ladies girls magazine tests
and I just you know I wanted to program
that I put amazing amount of hours into
creating this graphical art of writings
one of the words in and like block text
so that I would few know make the mouth
move and and get something visual on the
screen and I had completely forgotten
how much I enjoyed that when I was 15
and I had somehow come to this idea that
you know it's not for me and this list
of programming languages that's actually
the languages that I have programmed
during my lifetime so far and I expect
that to go up still quite significantly
before before I'm done with this
industry but it's interesting that you
can program in this many languages and
you can tell yourself you are not a
programmer
so something changed and the first
change that really happened to me that
is that I got a daughter and I realized
that if I'm teaching my daughter that
code isn't something that you will need
it's okay to you know understand it's
just these problems around this I might
be taking something away from her that
otherwise would be available to her
because again if she doesn't know that
it's not fun
maybe she can make up her own mind so
what I started doing at when she was
aged four is to go into her kindergarten
and teaching all of her friends
including her and that you know girls
and the whole group programs and I need
to learn something get a little bit
comfortable with some of the exercises
they are not very complicated for kids
so that I can you know get this this
idea across and this picture is from a
year ago I bought the Linda Lee Lucas
programming books for her whole class on
one of my nonprofits and again I keep
her thinking that women program her
friends program and she doesn't need to
like it but when her friends like it she
wants to be like one of them that's the
trick on how to get women in this
industry so friends you play especially
girls the social relations are really
big big thing so I also tried to figure
out although I kind of early on on like
what kind of other things I could do
there's a guy here Llewellyn Falco
somewhere I don't know where he is in
the room right now back in there and he
has this nonprofit called teaching kids
programming in Java and we went to
different schools together paired up
he taught 12 year old 13 year olds and
and you know kind of like got some ideas
there so that I would be ready to help
my my two kids both my daughter and my
son in these kind of things so so this
was a really big changer for me but the
even bigger change came with this
strange idea three years ago I organized
the conference in Finland called
sampling tamper it goes agile and I
needed a keynote speaker for that and I
invited this guy from from USA
his name is Woody's whale and he is one
of the kindest
kindest and friendliest people that I
have met very much talks through his
experiences and he shared this story
about this weird weird idea called more
programming and the idea was that you
can put people together so that they
work on one computer only one computer
for the whole group and that can be a
really effective way of creating
software I thought this was the most
ridiculous idea there was ever I said
all the things that might be on on
anyone's mind who doesn't know what this
is really about I said that you know it
looks like there's one person working
and the rest of them are watching but
when I actually started looking into the
dynamics I'll explain those a little
more to you I started realizing that
maybe this was something I'd like to try
and the reason wasn't that I wanted to
you know learn programming I actually
hated the idea that I would have to
waste my days and you know be there when
when people program and participate in
that it was a waste of time for me but
the thing that was important enough for
me to want to try this with my team was
the fact that we didn't collaborate too
well we had all of that you know
challenges of of you know sometimes not
telling me what was going on or
understanding what we were building and
you know all the regular collaboration
challenges and I was thinking maybe the
programmers will end up talking to each
other better if I just you know create
this space where where that thing could
happen and that kind of draw me into
this you might see that in this picture
there's this little girl there on the
right she is nine years old this picture
is not from my work it's from one
conference in agile conference in the
USA and that nine-year-old girl is one
of these programmers daughter at first
they invited her to join she said no and
then they did a bit of this more
programming exercise here and she said
looks like a fun game I think I can play
and joined in bossing the programmers
when it was her turn to navigate or tell
what what we're doing and when she would
sit in front of the keyboard the others
would tell her letter by letter what to
write so finding
exactly the right level of of
communicating for the skills level that
she had so I thought if a nine-year-old
can do this why couldn't I so I tried I
started trying this out at first my team
said absolutely no no way we would do
this like it's you know it sounds
ridiculous and I kept trying and trying
but while I was trying I I went to
various meetups and I would do this with
with random people that I could get
together I did TDD Tatas I did some some
kind of testing exercises all sorts of
things like whatever I could do
different languages I started getting
comfortable with you know working with
random people and and trusting that they
would be okay with me and that will say
you know seeing that that everyone in
the groups was very nice to me it was a
very important experience to me but
finally I also got my team to try this
and the excuse was you seem to like me
you seem to be you know okay with me
I really really want this experience
please do it for me and they said oh how
could we deny when you asked that way
like why did I get this before like why
didn't I realize that I can test you
know ask something that I want
personally and it's a very powerful
thing it's okay to want things there
doesn't have to be this like you know
overarching big ideal for all of these
these things so I got to try it with my
team and I remember the first time I sat
with my team and more programs we did a
refactoring exercise we had an external
facilitator present and I don't think
I've been as afraid as I was in that
particular case I knew I would be
discovered as a fraud
I hadn't been actively working with code
for ages they seriously will need to
tell me to write letter by letter and
this coming with the group that already
made the jokes about women don't write
anything but comments in code got a
self-fulfilling prophecy so I did that
anyway you know for the benefit of the
team that's my idea and I realized that
I sat in front of the keyboard once and
they would tell me letter by letter i
sat there again and I had already seen
everyone else doing things there and I
already knew what they were doing
so I started correct by
Moses act like picking up things like oh
I can see that that was already done I
can model after that and I can do that
again and after the first session we
started doing this as an exercise of
learning exercise on different kind of
activities on a weekly basis so it
really was was a a good thing to do but
for me personally the really big part of
getting into this was to feel safe in a
place where I wouldn't necessarily feel
safe if I thought of all the aspects
that they were we're on this so - for me
to pick up all those details my mind
needs to be awake and one of the best
making instance was that after I had
panicked on the keyboard because I
needed to you know be there and on the
spot and and you know listen to others
and do whatever they're telling me I
could just you know go away like now I'm
out of the inner circuit for a moment
and at that moment when I Britt had this
deep breath out and I was free from the
keyboard that was the moment where I
could listen and that's where I felt
safe and when the code wasn't mine
there's a lot of helpful usually men but
also women out there who give me loads
of comments so that my code that I check
in is as perfect as possible but it's
kind of overwhelming when everyone is so
helpful so none of this would happen
because it wasn't their code or my code
it was our code so that was a very
different things I felt very safe in a
mob safe in a way that I would not have
felt in a pair with someone who I know
that believes that women can't do this
anyway I started noticing things that
happened with my team I started
correcting some of the mistakes that's
happened so that's you know they happen
color could have ascenders there was a
mistake happening
I could correct it I could say like
there was one case where we were
changing GUI components for example and
they were asking out loud this question
that you know is it one or many and you
know all the programmers in the room
that work here it's one like yeah yeah
let's continue programmers
hey what are you talking about are you
talking about how many things the user
will select in this GUI component
they're actually selecting a mix of this
and then I showed them a scenario
the actual users will use that oh that
would be an expensive mistake if we
would have implemented it with that
assumption an hour later when we were
doing a retrospective they didn't
remember it without me reminding that it
had happened that's how powerful it is
if the ego isn't in play and you can do
it in on the spot also a lot of times
brought these ideas to my team about
what's relevant what is really the thing
that we need to do so when I got bored
when they're you know tweaking some
little detail on a car are we really
like you know needing all of this then a
lot of times out of that comes the
discussion that you know the users
actually do this and that is you know a
minor detail they don't really care
about that so much so I could be the
users voice in in many of those cases
also I was really afraid that I will
slow everyone down because I am there to
learn in that group but I realized over
that year that my slowness made them
communicate clearer but also they
thought better they decided what they
wanted to do they make it clear where we
are going and heading so that the others
would also understand so when they try
to you know make space for me they
actually made space for themselves so
that was a great great experience as
well and a lot of times I could also
sneak my things in you know as a tester
I'd like to see that we try different
kinds of users I'd like to see that we
try different kinds of data I'd like to
see that we don't only test with the
Chrome browser which is to develop a
friendly browser at least was back then
but we would actually use that everyone
hates this ie and making them open that
just in the right time we would see
things that would vanish and never
actually show up again after that so I
could introduce also stealth exploration
but my real kind of end to this this
experience came with the idea that I had
been doing this for over a year with my
team on a weekly basis I started to be
you know comfortable with code again I
started to feel like I might you know
survive with
I might even you know sometimes do that
myself especially around selenium cases
implementing some automation there and I
decided to join a weekend-long
all-female hackathon just you know go
there nobody knows me do something we'll
see
and I decided I will go there and I will
never tell them that I'm a tester I will
just let them assume I'm a programmer
and I was really careful never to say
what I actually do for my work I was
just you know going there like you know
you put me in whatever box you feel like
but I'm not giving you a box right now
I'm not giving you my identity and what
I then suggested for my four-person team
is that what if we would be more being
on creating the Halloween hack again
that we were supposed to create and
three of my four ladies said yes to this
and the fourth one says this sounds like
a waste of time just give me some of the
you know things to do and how it turned
out eventually it's well I didn't get
you know blown on on my cover I thought
I was a programmer when I told them in
the end of oh we didn't know like we
could not have noticed that I was a full
contributor in my three-person team and
the most senior lady the one who didn't
want to spend time with any of the three
of us who were doing the mobile session
of that she only created graphics in the
code because we were moving so fast with
adding features that she was always
behind us and she couldn't contribute on
the side of code so she decided to
documentation and graphics the most
senior of our developers and that was
kind of sad that we couldn't get her to
join but it was also a very powerful
message of how a mob works that the
three of us were smarter together and
these three ladies that I worked with
the middle one is also quite a senior a
front-end programmer so we had a lot of
help with having her around but the
other lady in addition to me in this
picture she had never seen code in her
life before that weekend and what she
said after that weekend not only that
she thought I was a program it's just
like the programmer in the group thought
but she also said
that she felt the program was hers it
was her as much as of any other one and
and that was a very relevant thing for
her to experience so that she had the
courage to go forward all the other
all-female teams ended up with those who
didn't program created the documentation
so we completely in one weekend reverse
this dynamic by by Moby and all these
experiences really led me to this idea
that we should call ourselves
programmers a little more easily it's
not about being perfect it's not about
being professional even if you've
written code that's your start of being
a programmer and programming it's then
just like testing it's a thing that has
so many layers forward it's kind of like
writing you know anyone can get started
with it but it actually takes years and
years of practice to get really good at
it and it's never-ending
testing programming writing they're all
things like that so we should give
ourselves a little more credit on on on
the things that we're already doing and
even if the programming wasn't my thing
in a mob what I could do is I could have
an idea that I didn't know how to
transfer that into code I didn't know
how to do the translation but I had
people who were close enough to me that
they would actually listen to what I had
to say and they could help me do that
translation so that was a very powerful
thing so this was kind of like how I got
into more programming and during this
experience it kind of rewrote my history
into the idea that I can be not only a
tester who is afraid of programming or
doesn't you know care for programming
but I can be both the tester and a
programmer and there's a certain little
supporting in those two two roles but I
want to give you some ideas on how to
how the mechanics of this actually works
the first idea is that you bring a group
together six maybe eight people maybe
ten people whatever the number is that
works for you and
instead of having all those people do
solo work like one doing things first
and the other one doing things next all
of them work in the same space in the
same time at the same problem you know
collaborating in a very tightly knit way
and this then means that if some of us
individually we have this you know good
moments and we have this you know
not-so-good moments for various reasons
skills differences how we feel about
things right now or all of these in solo
work all of that ends up into the end
result where we're working on and that's
what the testers usually do we try to
identify the the curve of each developer
and identify how they're strong and how
they're weak and and especially that's
what we call risks the developers don't
know certain things or don't care to
think of certain things and they fail
very often we identify those and we come
and know clean up a little bit bit
afterwards but in Moe being the idea is
that we get the best out of everyone
into the work we are doing in real time
by having everyone available at that
that's my moment so the roles or the
dynamics on how this works this these
are pictures from various mobs that I've
done usually outside my company this is
one in in Helsinki last year the roles
are such that there usually is sorry
this way this is fellow here driver
driver is the person who is not allowed
to think taking commands from the others
that's the rule so it is actually it's
the resting position in a mob it's not
the most scary position even though it
always feels like that it's the resting
position where if the others don't talk
to you in a way that you understand you
don't do anything that's the first rule
so we have a driver who doesn't think
can speak back can ask for
clarifications can suggest to do things
differently than than they're told so
can you know having like a real
personality but doesn't make the
decisions that's the first rule the
first row
the second role that there is is that we
have navigators usually especially in
practice moms we have someone we call
designated navigator
so this person here standing up as far
away from the keyboard as possible needs
to speak up so loudly that everyone in
the group can hear and so loudly that
the person who is writing things on the
keyboard will also hear so that's why
the physical distances is relevant that
person tells what needs to happen and
they tell that on the highest possible
level of abstraction if they tell that
you know you need to create a class that
does this and anything already happens
or everything happens by that then we
don't need to tell anything more then
you just review that whatever you
actually intended was happening but if
you need more detail you know if
movement doesn't happen then you sink
into location where is the thing that
you need to do where you need to go so
as you get started and then details
telling exactly what needs to be written
letter by letter even if if nothing else
else's is or higher abstraction doesn't
doesn't help you this is also from
Helsinki this is one of the meetups and
it was great to see that in a
programming meetup we were working on a
Python I think on this one three women
two men that's what it's supposed to
look like again women flock together
that's that's a real observation all of
these roles are these two roles are
actually to go back to this previous one
still the other ones in this group these
people were sitting
they are also navigators so when they
want to speak usually in the beginning
they speak to the designated navigator
who voices the decision so that the
driver doesn't have to listen to
everyone but over time we grow so that
people are considerate to others and
don't speak on top of each other but
actually will like everyone in the mob
or in the the navigators group can can
speak about this so we have these roles
of being a driver being a designated
navigator or being just navigator in the
in the mob and we usually
move around in the room or at least if
we had you know a chair that is set for
our own settings we take the chair with
us and we you roll it in front of the
keyboard that's the typical typical
thing to do but we usually move about
every four minutes
I've tried times of two minutes it
really helps sometimes create this this
you know idea that I can do my things
this is a group mind we are all working
on the same thing and bringing the best
of each one of us us into that and I've
sometimes seen some people use 15-minute
timers but that often lowers the energy
in the room so four minutes this is a
it's a good time this picture is from
this Monday so if anyone is recognizing
themselves I I took a picture of you you
were an amazing group really well learn
to work in in one day together so that
was a really fun fun exercise usually
then after each session like in the end
of the day or in the end of a couple of
hours of of doing this we have a
retrospective meaning we talk about what
just happened what did we notice that
that went on and it was anyone
uncomfortable was anyone you know
particularly delighted about something
that happened so that's very important
continuously learning make sure it makes
some space for that that as well and a
common question that people ask is
what's the size of the group this group
is from test Bosch Brighton and I think
I had 23 people in this group it worked
quite nicely we rotate in two minutes so
the bigger the group the shorter the
time you get to spend on the keyboard
but the idea really is not that you have
a fixed amount of people in the group in
a mob but more on the side of if anyone
or everyone who is there feels like
they're contributing or learning and
then the group is still the right size
if someone turns out they are not
learning anymore and they cannot
contribute anything either one of them
then you might want to split that group
into in the smaller smaller units then
there's a rule usually that when you
come up with two ideas you don't stop
and discuss them
you actually do both of them make a list
usually start with the one that is less
likely to be the right one and
surprisingly often it happens so that
the one that people would have fought
hours and hours that it's not the right
one to do in actually when it's been you
know developed and coded and and done it
turns out to be good enough and actually
not so bad that it needed all that
discussion against it so play with that
dynamic so that you have bias for action
that's kind of wrong
one of the things this group is from a
video from Hunter industries where mob
programming started so for the company
where woody zoo will use to work and
Hunter has nowadays several mobs working
in the same spaces so they've really
grown their company and brought in a lot
of new people with this mechanism and
and they still keep on working in in
that way they just do it eight hours
every day I did it a couple of hours
every week so my experience is more on
the on the learning side what I learned
also then is that the best ideas usually
if then win if you really care about the
work over the credit I've had numerous
cases of arguing with some architect who
knows that their status and a knowledge
means that this is the right way to do
it I'm a it's gonna have bug like like
that it's gonna be insecure no no it's
gonna be this way but when you're
actually have to sit through
implementing that it creates a very
different structure so usually get the
better ideas into interplay that way all
of these dynamics nice are kind of like
you know getting started level level
ideas min Llewellyn wrote a little guide
book so if you go to lean pub and if I
in this book there you can just you know
take it to zero there the price and and
just download it so it might be helpful
on understanding some of the deeper
dynamics that I can't address today in
this this this talk but as the last kind
of idea into this talk I really want to
go back to the idea of osmosis and
learning through osmosis
and Mamba is my way of like
automatically learning in that that's
place I don't really know what I go
there to learn but things just rub off
they get the distributed so that we have
more of an equal amount of things that
we didn't used to have after we've
worked together so that's kind of a
surprising surprising thing I've mopped
on all kinds of activities in my
previous company I did a lot of of
programming in a mob we also did quite
much exploratory testing in a mob and I
was happy to see that all of my
programmers turned to be brilliant
exploratory testers so it works both
ways I became a programmer they became
testers and they became actually pretty
good testers I've done a lot of test
automation selenium API level testing
but also unit testing automation sitting
together with the mob TDD I usually get
to do in practice sessions I've yet
worked not yet I have yet to work in a
company that would be doing TDD in in
the real production code so that's one
of the things I really look forward to
from my future application programming
we did a lot but in my current company
there's basically two kinds of
activities that I've had people do now
we've done performance testing in a mob
and it made a huge difference in getting
the message across on on some of the
severe problems we had just at the right
time there was a really good experience
but also we've done security testing you
know people having very different skill
levels on what they know about security
and and develop those skills skills
further so it could be any kind of
activity where you want the information
to leak that you're doing in animal
format I started talking about mobile
testing kind of the idea that you know
you go into a mob and you'll be a tester
in the mob and you don't you know think
of the program or identity you don't
need to give up your tester identity you
can be a tester in the mob and you can
do most mob testing and then it also
that means that sometimes the activities
are actually framed completely around
testing
either automated testing or exploratory
testing which is manual as for how you
usually command things or use the
keyboard but it's actually happening
inside people's heads when we're making
all those decisions that lead to the
good information that we need to need to
maybe find the big thing that cut to me
through osmosis I kind of found this
this term cognitive dissonance as I went
to see a psychologist who decided if I
could be applicable to a job that I
didn't tell except he I talked to him
about this more programming thing that
I'm really into and he said that it
sounds like there's this this phenomenon
in play called cognitive dissonance
there's this idea that if you believe
something very strongly but then you do
things that are against your beliefs it
makes you uncomfortable and that
uncomfort makes you learn it makes you
change either your beliefs change or
your behaviors change and for me the
whole idea of remembering again that I
actually do enjoy programming I actually
always did I had completely erased that
memory it came back and now I need to
face all the hard stuff around actually
being a programming woman because that
is very different than being a tester
woman in this industry testers are all
treated mistreated in our organizations
that's what I've learned so far when we
go into a mom
there's also smaller things that we
learn this this kind of like idea of
accidental learning we don't know
exactly what we're teaching to the
others but we're doing something and
then it'll go what did you just do but
you did that's so fast and then someone
said oh there's this keyboard shortcut
why didn't know there was one and would
you go and ask this from someone hood do
you know what keyboard shortcut that I
can make can make me faster in a thing
that I didn't know that can be made
faster no that's not a question you
would ask right so this so many of these
things that might be you know you pick
up things that other people do and other
people will tell you to do things in a
mob but then you realize maybe I
actually apply this this elsewhere as
well so you don't have to be intentional
about learning but kind of like happens
by serendipity lucky accident you will
learn things that that you then realize
that now you have have learned this idea
of learning continuously it's kind of
core to our industry we get a lot of new
people coming in the size of Industry
doubles every five years so there's
always people who come in and start kind
of like from a lower level but the idea
of learning is very very powerful if you
spend an hour every day to learn and you
manage to get with that hour of
investment one percent improvement four
minutes into that one day you cut four
minutes into being able to do the things
that you you were doing for it actually
pays you place back already in 28 days
so less than a month if you one hour is
enough but also we were looking at this
with with one Llewellyn in in particular
you can actually use five and a half
hours out of your eight-hour workday to
get that 1% improvement and you will
still be at the same place in a year and
where your head others later so learning
is a really really powerful thing and it
cumulates so you really need to think of
it as finding ways of learning and a lot
of times people kind of feel like you
know I'm already better than you are and
they have this like linear linear
viewpoint into what they can learn but
it's actually isn't linear it's
multi-dimensional there's so many things
that you can be either better or worse
at and there's always something that you
can learn from every person there is and
Moe being gives you a place where
through doing things you can actually
figure out what that that thing might be
so I find that experts no longer are the
ones who know the most but they are the
one who learned the fastest and mobbing
is one way of learning I invite you to
do all the other mechanisms of learning
definitely but don't dismiss this
operate
unity of learning through osmosis of the
things you don't even know that you
needed to ask the others the others
won't do it a talk in conferences on the
things that don't know that other people
need because they might think they're
obvious so this is a great mechanism for
that I wanted to finish with a very
little story of my latest colleague and
a teammate who is equal to me now he's
been in the company now for about six
months
little less than six months he started
in in June the first week when he joined
us in June I didn't get to move with him
but I used to exact same mechanism of
how we discuss things in a mob called
strong style navigation with the idea
that he would sit on the keyboard we
would have a shared task that we were
pairing on I would tell him what to do
on the highest possible level of intent
and when he didn't know what to do I
would tell exactly the details of what
needed to happen we spent a week during
this retrospect in reflecting drawing
architecture images of the things he had
already experienced in practice and what
happened is that he is really a full
member in my team the difference here
strong style is that kind of if he had
an idea I would say hey now you know I
can take the keyboard like it's your
idea I can do this for you and I was
actively making us change change roles
but what this gave him in the end of
that one week is that he said I never
knew testing would be this much fun and
he actually became a lot better at that
and I've heard comments from previous
teams that he has volunteered with us as
part of his his practices before joining
our team I've heard that they don't
recognize him for the same boy and the
same deliverables that he is doing now
so he clicked something there was
something that clicked and what I'm
particularly proud of is that on the
Tuesday of that first week he told me I
see what doesn't like programming
that was a lunch discussion he doesn't
care for programming that's another
thing he wants to do on Wednesday
morning he showed up and said I came
here a little earlier because I wanted
to start this JavaScript course
so apparently 50-year old are you know
easier to convince than the old ones and
now just a week ago this is a quote from
one of my teammates it took him only 24
40 seconds forgetting him his second
automated Python tests to get checked in
through this whole pull request process
which involves other people because he's
learned to bring the team together and
work in this way with him so that he
gets the information he needs so that he
can learn through osmosis so I can do it
he can do it I believe that you can do
it as well people change their minds
yeah through experience
so that's kind of what I wanted to say
it's lasting and there are people here
other than myself who have done more
programming I met yesterday Philip I
took a picture of him I wanted to add it
to my my last thing here Philip has
learned about this with me in Swiss
testing days I think earlier this year
and I really loved him sharing his
experience with me and the idea that
they had a lot of regulation before and
now that they're more being they don't
need all of that regulation because
common things emerge we have Lisa V haka
here she's done that more programming
with her team and there's a lady named
Suzanne that I just you know
accidentally found in the women
interesting yesterday she lives in a
more programming team full-time find her
talk to her find all of us talk to all
of us so that's my message for today
thanks so much thanks so much questions
could you give an example of how mobbing
works and farms testing performance
testing performance testing so what we
did is we built or extended our tools
that we created scripts for performance
testing we identified some of the
scenarios that we wanted to control and
then we were growing the the loads and
seeing what happened with the system and
we brought the developers from various
teams into the mob that will fix it and
tweak it out there in real time so it
for me it looks very much like it looks
like as an individual work but you just
bring in more people and you share the
context and when 10 people say things
are wrong it's a lot stronger message
than one person saying that so more
questions
I March I just want to find out what's
the best way to convince your team to
actually adopt my program is it via
stats over your slides I don't know
really I have to say I don't know what's
the best way to get teams to try this
because my current team doesn't want to
do this when we did this once they got
stuck with a particular tweak in
JavaScript five developers couldn't get
things done and all five were still
convinced that they would have been
faster alone five smart people couldn't
figure it out together but they were
sure they would have figured it out
alone so I'm I don't know how I will
convince them but I will do this with
the people who want to try it and my
main rule is if someone doesn't want to
do it it's better to let them be outside
I had a colleague who didn't want to
join us
and after half a year of seeing how we
partied once a week we had great time
together he said can he join so starts
with people who want to do it have fun
make the fun visible that's the best
thing that I can give you no questions
okay
thanks so much
[Applause]
[Music]
you
