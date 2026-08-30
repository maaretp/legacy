---
title: "Maaret Pyhäjärvi's Keynote session for #VirtualConferenceDays #ATAGTR2024"
video_id: VAT2Wm34Ecw
url: https://www.youtube.com/watch?v=VAT2Wm34Ecw
upload_date: 20241120
duration: 47:10
channel: Agile Testing Alliance
tags: []
---

# Maaret Pyhäjärvi's Keynote session for #VirtualConferenceDays #ATAGTR2024

> Maaret Pyhäjärvi delivered a Keynote Session on - Sociotechnical Guardrails for AI-Driven Application Testing in #ATAGTR2024 #VirtualConferenceDays
> 
> #ATAGTR2024 is the 9th Edition of Global Testing Retreat , #ATAGTR2024 was held across 3 days this year
> 
> Date: 16th, 17th November (Virtual Mode)
> Date: 8 December (Physical Mode - Pune)
> 
> It was brought to you by Agile Testing Alliance, Devop++ Alliance, I2IT and Tietoevry
> 
> Our Gold Sponsor - QAMentor , Silver Sponsor - Fiserv. and QAAgility 
> 
> To know more about this year's edition, please visit: https://gtr.agiletestingalliance.org/

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

uh I think we're super excited to start
our uh learning Marathon uh with great
uh Delight I would want to welcome marit
uh she brings along around 25 years of
experience in the testing world uh the
audience has to know she was awarded the
most influential aile testing
professional she's also one of the
Eurostar testing Excellence awardees um
she has spoken in about 28 countries
with more than 500 sessions till now
it's a great uh excitement and privilege
to have you with us Merit she also is an
empirical technologist she believes in
Exploration and also uses it as a
technique in her testing she's an actor
speaker author conference designer and a
community facilitator uh she works as a
director Consulting at CGI hi Merit we
wish you uh all the best and a very warm
welcome to
you thank you
you so let's see I'll share my screen
and hopefully you have the right thing
here in front of me yes we can see your
slides
good uh it's an early
morning and I am very much a night owl
uh I love the energizing uh activity in
the in the beginning kind of waking up
and and realizing that there's so so
many things going on in the world and
and what we're really spending this this
next session on is is there so many
things going on in the world of of
testing right now we'll talk about
social technical guard rails a fancy
word in in many ways but social meaning
uh social things that people do
technical meaning some of our insights
get to be implemented in all of the
different tools and the practices that
that we end up employing and the guard
rails meaning we need to figure out how
to walk a kind of a tight rope with uh
lots of options lots of things going on
all the time and lots of of lovely
changes uh coming our way I come to you
today uh from the perspective of uh kind
of like a practitioner in many ways I'm
a practitioner in the sense that uh I
got to uh start working uh with some of
these AI related things uh with somebody
else's money a few few years back while
I was working at F secure still uh we
set up a uh I think it was 2.6 million
euros learning program called research
that's what most of the research in
early Technologies is you get to try
things out you need to figure out use
cases you get to uh see if it works and
then uh when things fail you know that's
what the idea of experimentation is you
know you learn sometimes by failing
sometimes by succeeding when things fail
you write report so that other people
can share that so so learning uh
research uh exper experience sharing
mindset is is kind of the the background
that I come uh to all of this this
in uh so with that learning mindset uh
when uh these large language models and
generating code and generating text was
kind of taking off and GitHub co-pilot
uh came into the the picture uh I got a
chance of kind of like getting myself
into the cues quite
and since uh I happen to volunteer with
a lot of community
activities uh when asked for reasons why
they should give you a a access early on
into any of these tools usually the
activity uh the volunteering in the
community it's kind of like a plus one
you know you go one one step uh above uh
some of the others in the cues so I got
a fairly early access to a a license of
a GitHub co-pilot uh my first uses
actually after one week of having it uh
in my hands was that I went into a job
interview with it uh it was a pair
programming interview I was considering
changing jobs back then in a p uh
programming interview when I was using
GitHub co-pilot in that interview I
ended up actually just showing in the in
the moment that uh when my uh pair uh
didn't actually pair with me because
what he actually wanted to do was assess
me because he was interviewing me it's
kind of nice when you have a pair who is
you know actually collaborating with you
actually giving you some of the things
that you can't remember in the moment
because again you know interview
situations are a little bit nervous but
also in that case I learned that
whenever uh uh I'm using something like
this uh some of the creativity kind of
like the the external imagination the
idea that that you always want to one up
whatever you're getting whe whether it's
your pair whether it's your you know uh
AI assistant uh figuring out the bugs
and the things that people would miss in
general it actually came out a really
good job interview I did get offered
that job I didn't change into that
company because again uh for me pairing
it's it's almost like a a a a sacred
ritual and it's not meant for assessing
other people so you don't call it pair
programming if you're not planning on
collaborating so a lot of the stuff
around collaboration is kind of big part
of the way that I look at the world as a
as a as a
practitioner so a little later we then
got the the chat B and obviously again
you had to be there you know on the
first days one of the sessions I ran on
on the first couple of weeks of of
having chat GPD available to me was to
have people come together in a group I
had a a testing group called testing
dozen we were learning testing together
and I was thinking like it's a great
testing Target we're going to you know
play with that we're going to figure out
if it Works uh and and we'll model it a
little bit kind of you know create a
lovely mind map where you can see kind
of what did we learn and what did we do
and and maybe you know maybe we could
generate some of the ideas of what we
can try still later on and I realized
that it was actually a lot bigger uh
step for people to to go from having
tested uh deterministic functionalities
basically things that always give you
the same result kind of figuring out the
steps and the the uh the uh things that
you would do in a user interface or or
the exact values that you would send in
an API and going into this chat GPD
world where you know small changes in
the input could have a a a major uh
impact on the output and even the same
input wouldn't always give you the same
uh results so so kind of like this this
Pro these probabilistic uh things uh
people had hard time uh testing those
and we had a really great uh session
with 12 people figuring out uh how would
our you know heads need to uh transfer a
little bit into a different position so
that we can uh uh get uh these into into
use but you know from those first weeks
on it's pretty much been a tool of of of
uh uh learning to uh use learning to uh
uh uh apply and remembering to open and
again sometimes I have this hate love uh
relationship with these tools in the
sense that I ask things uh because not
because I intend them to be useful to me
in that moment but I ask them because I
intend them to be inspiring like an
external imagination and some uh most of
the time also then bring out the best in
me so some of my best work actually
comes from from this this idea of of one
up you know like always climb the ladder
uh collaboratively go one step higher
and figure out if there's something new
to learn every day is a learning
opportunity and if we have that mindset
where we're continuously
learning that 1% four minutes out of our
eigh hour uh working day uh one uh
percent there uh if that accumulates
over time that would make us like 38
times uh ourselves in one year and I'm
happy just you know doubling up uh every
single year so figuring out how to
combine things how to inspired by all of
the things that we have going around in
the world definitely a a a big thing for
for
me so uh later on uh coming my way also
uh was was uh things like codium AI uh
integrating this into uh the selenium
project where I'm volunteering uh
integrating that into the the code base
there uh kind of watching people treat
it as if a it was a a uh kind of like a
party uh in the in the U uh code review
comments a party that you kind of ignore
most of the time but then when it uh
once even says something smart and
useful and finds something that other
people don't notice you kind of feel the
buzz that it generates for a moment and
then again it goes into this kind of
like you know an active participant uh
that you uh read you don't pay too much
attention to it doesn't you know
generate you the same kind of of intense
feeling of of having to pay attention to
everything that it says and and and take
care of the the human feelings that are
around real humans but kind of treat it
as you know someone who's just giving
you you know some hints sometimes useful
sometimes not but it's giving you the
the chance of learning and and getting
some of these
insights and then finally uh on my my
journey on on practitioner uh I joined a
new job in in in June uh I uh was put in
a very much a corporate constraint
setting I can't and I'm not allowed to
use all of the different tools on my
work computer so kind of like having
multiple computers really Ed uh amped up
the the amount of money I need to put in
order to play with these these kind of
tools so it's no longer enough for me to
just pay for licenses I am not just
allowed to uh use all of them on on this
particular computer which is my work
computer but I am allowed to use
Microsoft co-pilot and uh in the last
two weeks in my organization we've been
rolling out in a more major way also the
the uh GitHub co-pilot uh so getting
back to that on my my coding assistance
it's kind of like a a welcome thing but
figuring out things around uh contracts
and and and when would you go about and
using one of these tools kind of like
the idea of of uh uh uh a corporation
Trust ing another Corporation because
you can create a contract with them
whereas you know an individual me alone
Mar just by myself uh the contract with
me and Microsoft I wouldn't trust that
uh it wouldn't be changing so much with
kind of one-sided agreement so so
Corporation to Corporation contracts
realizing how that goes and then uh
realizing that you have a lot more
things that you can you can input so
definitely a practitioner and and the
differ between a a practitioner and a
builder uh generally is that that you
would use tools I have used a lot more
tools than what I chose to kind of like
show you on my my uh little timeline
here uh and would be happy to talk about
those but today I wanted to kind of look
into into just a few of of
these just click on this so one of the
things I learned over the years uh uh
out of working with test Automation and
and and getting started with uh things
on on that side was that uh we need to
be very aware of the time that we're
using uh test automation uh AI uh is
kind of like just a a an extension to
many of the ideas on on what things
we're trying to automate uh within
testing so to me uh I could you know
easily take up some space and and uh
explain all the different things that
can go wrong with AI but I've made a
deliberate choice just like I I needed
to make a deliberate Choice around test
automation 10 12 15 years ago that uh
instead of using time on warning about
things and listing all the downsides
which we testers do know how to do we we
are really really good at that we need
to sometimes also realize that we step
are stepping back on the use of our time
uh into a situation where uh we choose
to use the same amount that we would
choose to use on explaining to a manager
why test automation 100% probably isn't
a great idea we can add that one more
percent or even Prill like a smaller
portion uh into the success of our
automation into the success of our AI
tools and into the the Practical uh
empirical experiences of figuring out
where this is useful so this is really
the mindset from which I come into into
this this
topic I don't know why it's not letting
me click on here okay but uh the uh
things we talk about so setting some
expectations I'll show you well I didn't
want to go into demoing so I took some
screenshots uh I'm showing you kind of
three demos or three uh screenshots of
things that I've done so uh doing
oriented things and then I'll sum up
with uh talking about uh the the social
technical guard rails so we'll start
with uh
co-pilot and co-pilot I hope you have at
least some of you already had chances of
enjoying this but giving you kind of
like a brief overview of of what uh
copilot is about and what that pairing
experience was about so going into uh
use of co-pilot you would have your IDE
your integrated development environment
where you would probably be writing your
test automation scripts you might be
writing your book I have been using it
for that purpose as well uh or you might
be writing your day-to-day uh notes and
and no matter what you write it's kind
of like you know guessing ahead uh what
you want to say uh over the couple of
years of using this uh it used to guess
a lot more uh now it's it's kind of
giving me a little bit more space of
first saying what I want to say clearly
someone has been tuning it a little bit
and different days uh depending on what
version of the product you have at your
hands you might be getting a an entirely
different uh version or experience than
what I had on the time when I was taking
these these screenshots so it's
basically guessing uh ahead uh it's it's
having the the power to accept so if You
tab into this then you get the the uh
the uh thing accepted and if you wanted
to say something other than integer to
Roman uh then probably uh you won't be
accepting uh whatever it it's now now
guessing for
you uh the reason why this is guessing
Roman so you can kind of like maybe uh
look at the the context there uh the
context of the file name that I have
already given so my my project is called
New important project and my file name
is called roman. pii uh so again kind of
like uh guessing that maybe I'm doing
something with Roman numerals is is kind
of a safe one so at some point I also
learned to call these important and and
and you know just testing out what kind
of things it then then generates for
me uh I usually uh don't start with uh
naming myself in the beginning of the
project but guessing uh I had a lot of
fun uh collecting different names that
it remembers to uh uh suggest to me
nowadays this particular uh thing no no
longer happens you have to wait a little
longer before you get it to uh guess
your guess names but you can't anymore
get it to guess it in an
entirely uh empty uh file but just kind
of guessing who I am uh there's probably
safer guesses than this but you know uh
with some kind of a probabilistic
algorithm uh it seems like you know
somebody didn't make it so that that the
most probable person would be me in in
in this case and that's again you know a
feature to add later on so so all of
these things are pending to change uh uh
we're probably learning and we're
probably improving any of these these
tools that we use so uh getting into the
the the actual writing of of code and
tests uh you kind of need to get started
you could start with a comment you could
start with the file name uh you could
start with um you know just uh uh
whatever uh structures you need for the
particular language and uh you can very
quickly get it to to uh well either
guess for you or when you have already
inputed something you can ask it to to
guess uh or give you some Alternatives
so in this particular case when I was
asking uh for solutions for Roman
numerals or looking for those getting 10
different uh possible solutions it took
me a little bit of time to actually get
to a a situation where I had other files
on my computer that I had recently used
where I would get it to guess the worst
solution that it can give me as the
first one that I'm seeing so that I can
take a lovely screenshot so again a lot
of this kind of like you know prompt
engineering now not for the positive
effects but more for the getting the
perfect screenshot that I want to share
with you uh today so just you know
reviewing this particular piece of code
you can already kind of say that most
likely this is not the implementation
you would want for a Roman numeral
converter even if you weren't a
programmer realizing the fact that you
know having an if statement for every
single number separately like you can
reason the that uh it's probably not an
algorithm that is very efficient it
might be very effective like it only
does you know whatever you have you know
every single line is is every single
case is is separate and I love this
particular example because because it
reminds me of the 14-year-old myself
that started programming and this was
the code that I wrote so again an
average person with examples have had an
impact on whatever all of these tools
end up generating for us and then on top
of that we're doing some filtering
leaving some of the the things out uh so
you can choose whichever you choose I
would not choose the one that it gave me
after you know a lot of tweaking to get
get to exactly that worst scenario I
might s something like this you know it
already looks better to me at least you
know like looking at it quickly but
again I have multiple different options
that I can choose from and uh if I don't
like the one that I ended up with
because again my focus is really not on
generating the the application code my
focus is always on the tests so I'm
playing with the tests more if if I
don't like it based on the tests that
I'm then doing like these are you know
great testing targets for me uh then uh
I can always generate a different one or
I could even go and write the the
different one uh myself so you know
figuring out that uh uh for review
purposes uh you can choose something you
can go back and and make changes on
things but the mindset is really about
testing that's kind of where I I I got
with these these tools so on the testing
side uh it definitely does generate the
tests for you as well
but uh when it generates the tests for
you it generates you uh tests that you
would not really want to have around so
none of these tests that I took on my
screen are actually generated these are
all handwritten uh by me because the
ones that got generated at first uh were
ones where you have a single test case
and then you have many many many asserts
in that so it wasn't a parameterized
test it was a single test where when the
first sht fails the rest of it won't get
run and what I actually want this is a a
listing and and results which which
tries all of the different combinations
that I had and then gives me a listing
of this is wrong this is right this is
right because usually most of them are
right so I want more granular feedback
so again I need to know this stuff I
can't just rely on Whatever Gets
generated but I need to know what I'm
I'm looking for so what a good
programmatic test look like uh similarly
uh I might not want to you know even
generate these example based tests
there's a library here in the example
called approval tests uh which it didn't
definitely generate for me so I wanted
to kind of do a bit more like
exploratory testing just show me all the
different outputs let me look at them
let me decide if I like them and then
let me approve that this is now the
Golden Master that all all the future
things will get compared against so
again getting those ideas uh you know
having that mindset of of I know what
I'm looking for having that intent in
mind uh the exploratory mindset is is
really really gen uh uh important uh
when you're assessing uh things that
that you have from these uh generative
uh
tools so all of this this uh uh thing
with GitHub co-pilot I definitely want
to use it a lot of the the the uh
teaching sessions that I use it it saves
up uh time in kind of doing some of the
autocomplete uh it it helps in many ways
but I can get also the same kind of
things from you know going into a chat
GPT window and copy pasting from there
or I can get the same kind of things uh
going into uh Microsoft co-pilot and
copy pasting from there but what I
really really like and what my
colleagues in my previous team also
mentioned that they liked is this idea
uh that the extra autoc completion that
you get with something like GitHub
co-pilot the integration aspect of it
it's like as if you have code Google uh
in your fingertips so uh you don't have
to write this kind of like you know
basic boiler plate but at the same time
it generates you some of the boiler
plate you don't want so you need to be
very intentional to not just accept
whatever it's giving you but
continuously review the structures that
you want to be uh going for and and uh
the more examples we have of good things
uh so that the average becomes something
good I believe that over time this is
getting more and more helpful even
though sometimes nowadays I still feel
like this is more of a you know like an
inspiration of I hate this I want to do
better uh so so again uh approaching it
with the the the right kind of mindset
that's what I talk about when I talk
about guard rails the mindset of of of
one uping whatever you're getting uh
whatever you're seeing always striving
for that one% better uh is is a really
really important one one uh to to go
from so uh having to go to stack
Overflow uh well would definitely be
something that I have also done a lot in
my career uh not having to do that uh
also then means that we're changing a
little bit the world around us so
probably people won't uh be right uh the
good teaching samples to stack Overflow
if people are not using those there so
being aware also of the the side impacts
of these kind of changes in the in the
world so I definitely love programmatic
testing uh generating tests on unit
level generating tests with uh with uh
well I do a lot of python and playrite I
do a lot of typescript and playrite I do
a lot of python and selenium I do some
Cyprus I do uh a a lot of API related
work I do a lot of Robot Framework so
kind of like ending up with multiple
languages and not always even
remembering what the syntax looks like
really helpful in in in that case but
the programmatic test kind of like you
know leaving documentation behind the
the thinking there is is is uh uh very
much the the thing that I I need to do
but I also do things where I don't work
with programmatic tests I spend time
exploring
applications and for exploring
applications I usually don't find GitHub
co-pilot the tool of of choice for me
but it's more uh of this this mindset of
doing generative AI pair testing with
very general purpose llms uh large
language models so things like you know
uh uh having the habit of always having
it open in one of my windows and and
kind of like thinking of it as if it was
you know the rubber duck that actually
answers to me and sometimes it just
energizes me on how stupid answers it
might be giving to me and sometimes you
know when it's some of my colleagues who
use these kind of tools and they send
over to me like a a a ready proposal
generated by by one of these tools and
say we can start you know building it
from here I'm like okay so uh again one
up uh I want to do better than what's in
in this particular paper and on uh on
June when I started my new job one of
the things that I I got actually really
uh positive feedback on was uh on uh a
particular proposal for a customer on a
testing project where uh someone else
had asked for the proposal from a
generative AI then send it over to me
and I had to I just had to rewrite it
because it wasn't good enough so again
you know sometimes even the the it's not
giving me what I want it's just a posit
postive thing actually most of the time
it's just a positive thing but you get
into the habit of of figuring out when
is it useful to you when is it not
useful to you and when you have a habit
of kind of like you don't know if it's
it's good yet if you maybe you know you
you get an answer but you don't have the
knowledge of of assessing whether you
like it or not maybe that's a great way
of you know finding a real person and
having also this kind of a pair testing
or pair conversation bringing that
social aspect to to your learning and
your work so that you're not just rubber
ducking uh with the the generative AI
but you're bringing humans into that
loop as well uh some good use cases uh
for par testing for me has been at least
for you know searching of boundaries uh
I'm arguing about uh certain assumptions
you know just you know thinking in terms
of this is my assumption what else uh
could I assume so again breaking down
your thinking and then having a
conversation about whatever you're
thinking like the step or or thoughts
that you have or your options uh you
know feeding those into into one of
these these tools you you get a lot
better understanding when you don't
think it just knows for you because it's
actually not a knowledge Bas base it's
an average base it's giving the averages
of things that it has seen in these kind
of of settings so uh if you recognize
insufficiency and and you're motivated
by fixing it definitely uh uh that's a a
good way of doing things uh having that
freedom of criticizing and saying you
don't like what it says uh like the
amount of energy that I sometimes use on
on trying to not be the blunt human uh
thin uh type of a person that I am
especially with my American colleagues
saying that your text well yesterday I
ended up saying this your text looks
like it was generated by generative AI
did you and and then learning that no it
wasn't and I actually offended the
person that not really intentional not
really what I what I meant to do but
also kind of like figuring out that
maybe you know there are certain kind of
core elements and insights that I was
picking up from the material that
weren't quite the the the uh the
mainstream that you would would expect
but not having to use that energy of of
you know filtering uh and making sure
that you're always remembering that it's
a human that might have feelings on the
other side sometimes it's been very d
uh liberating to
me and also uh you know you dare to ask
things that you wouldn't dare to ask
from a colleague I nowadays do dare to
ask uh things from my colleagues and I
do encourage you to dare to ask things
from from your colleagues so kind of
like a good again a guard rail in in
this sense is this idea that if you
notice that all of your Social contacts
are are artificial and fake maybe you do
need to intentionally go and balance
those things and see real humans and
talk about the insights that you have
acquired in the in the recent times any
learning experiences you have make a
great conversation starter with real
humans and and you'll probably take a
lot out of those conversations as well
so it's just a kind of like a continuous
building on top of of whatever you were
doing uh before and well since you are
still uh with the human in the loop uh
St type of thing uh you don't have to
obey your pair you don't have to do
whatever the pair was saying to you you
can just kind of like you know do uh
some of the corrections it was saying uh
don't do this and and you'll absolutely
not obey that that uh instruction you'll
do the exact opposite or uh you figure
out you know whatever the the the
approach is that you want uh for for the
the particular case that you're at but
building that habit of of of having
these little conversations I've noticed
that in the organization that I work in
right now we had for everyone last year
we had the goal of of you know building
that habit trying to use these tools and
uh still in my my team of about 10
people I had two people who hadn't
actually managed even with the goal uh
connected to our our work hadn't managed
to build that habit and practice and
there was a lot more uh from that
conversation of of what the the uh the
more time spending habit Builders had
built that that then enabled the others
to to take things forward so again you
do something with the Gen pair and then
you take it to your human Pairs and
share those advices and ideas of of what
kind of things others have
tried I do not want to generate test
cases in general but I have noticed
because I always go and ask for things
that I might or might not use from this
these kind of tools I've noticed that
while I might have a lot of experience
and exploratory testing and I might have
you know my ways of of figuring out all
the different perspectives that I want
to do uh uh it's a great coaching
mechanism for uh more newer exploratory
testers to say that you go and you
explain all the things you know in
writing and then you copy paste that
into a prompt and and and you request
you know you could request test cases
but that's too much text to read for my
my taste and I definitely don't want to
read extra text I want kind of like
condensed information rather than any
extra text especially generated one I
don't want to spend the rest of my life
reading text that was average and
shouldn't be uh actually even paid
attention or read by humans so I rather
usually generate Charters or you know uh
top 10 lists or or or something more
concise and uh uh having noticed that uh
uh again the one-upping uh uh attitude
with colleagues Sometimes some of the
colleagues uh are actually doing better
as well uh when encouraged to use use
these uh kind of tools and for me uh
kind of noticing uh the kind of coverage
differences what's in my my notes what's
in in these these kind of notes a a good
way of of reflecting what I what I would
want to do uh there's an article on my
blog on on uh how badly we generally
test logins like there's so much more
than just logging in uh either from a
web application or mobile application or
you know security of passwords there's
so much more uh that we can test
including the fact that uh well somebody
usually builds all kinds of
authentication and authorization systems
which are kind of tied into this login
also including the log out so that you
no longer have access to and and you
might actually want to pay attention to
those and again uh the average text
generated out of one of these these
tools really didn't give me as versatile
choices as I have learned to generate
having been an exploratory tester for
almost three decades so keep being
excited about you know looking at the
applications looking at the different
kind of problems that we're finding and
and learn and learn and learn once and
and once again so definitely these These
are helpful uh and and save some time
but on generating test cases as as such
I wouldn't want to leave them behind uh
because well uh uh the previous project
where I didn't have generated test cases
but I had handwritten test cases I had
2,500 of them and I counted that it
would have taken me it would have taken
me um
was uh 11 full working days if I was
reading them fairly quickly through I
think was one minute per test case which
was much less than I would need in order
to understand those so kind of like the
the time used on on on reading
especially generated text it's not going
to save us time uh writing less and more
concise that's going to save us time
because things get written once but it
gets read hopefully hundreds or
thousands of times so that's a a a
mindset that we need to keep in mind
whenever we're generating test cases and
and other text so so only generate
things worth
reading or uh if it's evidence out of
your testing which some of my customers
also are asking from me uh uh that's not
intended for reading uh we already kind
of Mark it so that that we no longer
will look at it after we've once once
used it so uh some of the the standards
require us to use something of that sort
where uh we need to leave behind
evidence but uh I have a general
preference of recording what I did over
uh writing uh then in in those those
kind of
cases and again it doesn't have to be
all of it and it's good to remember that
these are really text generation tools
uh all of these uh large language models
so they are useful usually for recalling
things uh out of something that someone
in the world has ever written uh kind of
like probabilistic style so these kind
of problems where you're trying to make
it count things or do math for you uh
well you have programming languages that
do this kind of stuff a lot better so
know your tools is is kind of my
advice uh then the third uh
example that I had for you is on uh the
idea of rag which is retrieval augmented
generation and just building on top of
what we had just there before for uh you
can just use rag as kind of like an idea
of inputting larger context so for
example for me I have written a a an
exploratory testing course whereare and
uh I get a lot better advice and a lot
better you know like at least better
advice that I would expect uh to get uh
when I prime it with materials that I
have created which means I also like
them there's the bias of of thinking
that that's something that you have
spent time on is is already useful but
uh getting the the uh very different
kind of answers so you can definitely
feed more input and you can have an
entire database of of
inputs so uh playing with this concept
of rag you can also do it uh for for uh
little uh automation related tasks like
uh the the idea of uh collecting
information from your previous test runs
so that you can fix your your your
locators I don't think this is something
that I would want to use in in in real
projects I believe that uh uh
autocorrecting things uh have a a bit
too much of a a risk of U of breaking
things and I have better options like
talking to the actual developers on
fixing uh my locators or moving the
maintenance over to the developers
there's so many better ways in in a in a
in a systemic scale to fix locate
then applying rag into those and I have
uh some people obviously uh asking me uh
things like uh we have you know
thousands and thousands of test cases
50% of them are failing could we use
this to just you know somehow magically
get them to pass but there's always a
reason for failing and you are not
looking for a a a way of making them
pass without understanding the the
systemic causes of of of those kind of
things so lot of different words uh the
uh uh decision models the the generative
uh language of image generating models
the things where we feed in context and
the uh things where we agentically uh
split our work into smaller
pieces so that we can have multiple
queries into the model uh that then
builds up the thing that the user will
see all of this is is kind of the the
Practical
stuff so to sum up on the social
technical guard
rails uh you can do a lot of good things
with these tools already but there's one
thing that you absolutely need to be
aware of before you go and play like one
major major uh guard rail that will keep
you safe and that is the guard rail of
remembering that whatever you are
writing there you are handing it over to
someone else so all the files you're
copy pasting there all the the context
you're sharing it goes into somebody
else's database and I at least you know
while from Corporation to Corporation I
do trust the the contracts that we're
making from an individual to Corporation
I am very much aware of what's secret
what's confidential and what do I want
to keep confidential and this knowledge
of of of of you take a whatever tool
with with AI it's going to be sending
over some things uh over the
network uh uh usually or at least you
have to look into what it's it's sending
that your data is is is maybe being
moved somewhere a definite awareness
thing before you use any of of these
tools so customer projects are a no no
uh unless you have made again
organization to organization agreements
on on on how that data is is
handled uh on the other guard rails we
we already talked about this kind of
idea of you know splitting the tasks
figuring out what you're trying to do
and and kind of like breaking it down
into the smaller tasks subtask that you
have if you're thinking actively while
you're using these tools and and and
kind of continuously go into smaller
things you get a lot better results so
uh it might be you're asking to uh fix
some of the uh the locators it might be
a a specific feature that you're asking
at rather than the entire system so kind
of that Drilling in and the mindset of
of uh this is the next step that I need
help with really helpful uh guardrail in
in in many many ways figuring out what
you want to leave behind in automation
uh uh and using automation as a a way of
documenting absolutely loving loving
that style of of working and and the
right time time and and awareness of
time in in general and sometimes
realizing that you know you're getting
not what you wanted but the rejection in
experimentation is also you know it's
it's a a learning experience and it
gives you uh well not the Blind Faith
but uh this this kind of like a an idea
of going forward and uh moving to kind
of this this uh well uh instead of uh
generating all the test es that you
currently write maybe you could learn to
write more concise test documentation
rather than uh generating that that's my
my thinking of of improve first uh
ideas uh then there's certain kind of
boundary seeking uh guard rails knowing
that every single tool has a monthly fee
uh uh every single tool has a limit of
how much you can use it and there are
just other tools than these uh per use
type of tools that solve the same
problems being aware of that is is good
uh realizing that the world around you
changes uh due to this uh and and maybe
compensating for you know figuring out
what you consider ethical and and and
and good future even when these tools
are around is is something to to realize
and that's just then paying attention to
that the fact that there is a technical
implementation and architecture behind
all of these so to kind of uh sum it up
all know where you are measure assess
where you are right now and be critical
about is this useful is it saving time
uh sometimes I don't think I'm save time
I think I'm inspired to do better than I
would do uh without these tools uh
experiment together with your colleagues
with your customers uh figure out what
works uh package that into some kind of
of tools and reusable pieces so learn
first package then learn to Habit
habitually uh apply uh all these kind of
tools available to you share whatever
you learned and if you learned something
that is unique uh maybe share it in a
reusable format that's how I I think
will will solve all of this these
puzzles that's what I had in mind for
today handing it back to
you awesome Merit thank you for very
granular and very aptt uh slides and for
explaining it so well uh we have a
couple of questions which I can take in
the interest of time uh I think we have
one of the persons who is interested in
contributing uh in the QA perspective
for AI products on pair testing would
you suggest any particular road map for
it uh contributing to uh uh products uh
well there's a lot of Open Source ones
so you could find one of the the open
source projects one of the ones that I
looked most recently is is one called uh
aluminum so selenium and AI combined
together into into something uh new so
again it's a selenium based tool so
selenium is definitely still an
inspiration to many so that that might
be one uh but uh I would say there's
thousands of tools I've looked at
hundreds there's thousands of tools find
someone uh who uh you feel like you'd be
excited to spend time on and and
volunteer there any communities pretty
much are are good for that thank you um
also another question uh if we use
GitHub co-pilot with a private
repository for code generation uh maybe
on a client project they're asking if we
can be assured that the generated code
and application details will remain
secure and they won't be shared over the
network given that we are using a
private Repository
yeah this is kind of a trust question so
uh would I personally uh maret not a
corporate entity would I trust someone
who has just stolen open- source code
and removed attribution I
wouldn't but would my
Corporation make a contract with the
other Corporation so that there's you
know uh relevant compensations if this
this trust is ever broken I definitely
would so the perspective from an
individual and Corporation will look
different if it is absolutely secret and
you want to keep it secret I would not
share it to another party that's how it
is okay thank you so much Merit thank
you for the clear in detail topic that
you brought us with in the morning and
thank you so much for joining in early
and staying with us um we're so happy to
have you a quick thank you note from the
entire Community to you for always being
enthusiastic and joining our Keynotes
thanks
marit thank you
