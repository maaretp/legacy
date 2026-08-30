---
title: "Practices Change - Moving to Delivering Continuously by Maaret Pyhajarvi #AgileIndia2019"
video_id: J2qLwAFN7_8
url: https://www.youtube.com/watch?v=J2qLwAFN7_8
upload_date: 20190420
duration: 46:27
channel: ConfEngine
tags: [agile india, agile india 2019, AgileIndia2019, delivering continuously, continuous delivery]
---

# Practices Change - Moving to Delivering Continuously by Maaret Pyhajarvi #AgileIndia2019

> Delivering continuously - easier said than done. As I joined my team delivering Windows Desktop products two years ago with the aspiration of implementing continuous delivery, I was told it cannot be done. It started from the fact that making a single release was five-day effort, and continued with “no user would allow us to deliver frequently”.
> 
> Two years later, making a release takes us two hours and the way we work together looks very different. With the principle of fixing maintenance issues in the latest release has resulted in improved flow forward and savings of effort in supporting small number of releases.
> 
> This talk goes through our lessons learned on the journey of shortening release cycles to a continuous daily flow.
> 
> We’ve experienced three essentially different sets of practices, with the core difference coming from release frequency. The good place is when we deliver continuously. The soulsucking place is when we deliver on two week cadence. And the insane asylum is when we deliver just once at the end of the project.
> 
> Think of it like this: a pool is not just a bigger bathtub. The things you can do in a pool are different to those you can do in a bathtub. While both are containers of water, they serve different purposes. It is the same with release frequency. While it is all still releases, the continuous ones enable different practices.
> 
> More details: https://confengine.com/agile-india-2019/proposal/7961/practices-change-moving-to-delivering-continuously
> 
> Conference Link: https://2019.agileindia.org/

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

good morning everyone my name is marek
Parvati and I came here from from
Finland and I have the the privilege of
sharing some of my lessons and stories
and things that I've have gone through
what at work a lot of times I find that
when I go to agile conferences and I
listen to so-called gurus the people
that I have read books from like the the
morning's keynote I feel like a total
imposter I've been only doing agile
since 2001 like you know I'm complete
newbie to late 2001 is few years back
and well I've been around in the
software industry for 25 years but it
stills me if I'd it was yesterday when I
when I started and a lot of the stuff
kind of like what I read in books I get
inspired by that and I try very hard to
apply that at work I do stuff around
continuous deployment continuous
delivery I am a huge fan of more
programming that's absolutely one of the
most biggest favorite things that I have
and I do things like what I talked about
yesterday things like having no product
owner so that the team holds all of the
power so I do many things around agile
in in the organization but still kind of
thing that I have because I work as part
of a team usually my title is the lead
quality engineer but for the last about
six months I've held the title of a
senior manager so I'm managing a team of
twelve developers and we are delivering
software together I'm a manager with
very hands-on role so I still test with
my team most of my time I just have to
do certain procedures around growing
people and making sure we make notes of
having had discussions about their
career path and and growth but all of
this stuff can like you know working in
the real real projects and particularly
being stuck in one organization I don't
actually think of it as being stuck I
think of it more as than like choosing
to be stuck to seems to spend a relevant
amount of time with a particular
organization some of the things that I
feel
in that case is that I can't do all of
the things as the books say I have to
actually start with through things that
are you know I hear things on the stages
here that let you know other people say
that they have gotten rid of it but I
actually have to you know do those
things and and that's kind of one of the
motivations of this talk here today that
I keep on striving for better we keep on
striving for better we keep on trying to
change things but the change sometimes
it's costly it takes money but
especially what I find is that it takes
patience it takes time it takes
continuous small changes mentioning
stuff that you would like to be
different for multiple people and just
not giving up being persistent being you
know driven towards whatever change
you're trying to drive in your
organization and again I kind of tell
the stories that I tell here from the
position of my title was one of a QA
engineers so that's not the highest
title in the organization and still I'm
telling stories usually around things
where we could make a relevant change
starting from something that I initiate
as just someone working in the team so I
hope that's part of the story and
inspiration that you can take home today
that I believe that you know all of us
with persistence can can do stuff like
this so we're going to talk about an
experience of moving into continuous
delivery
this is actually an experience that I
have had in multiple organizations will
have changed jobs I enter a place where
we don't quite yet get it and then I try
to get us to move there and I'm kind of
like you know take us to that route and
it seems to be a repeating pattern and
it's it's a journey that that is not
always well never completely there so
when I talk about continuous delivery
what I mean is that that we have
probably still somewhere in this overall
pipeline a person involved so it's not
automatically from from checking
something in to the baseline that we get
it all the way through there's usually
still in my processes there's there's
someone at some point
doing some kind of decision at least if
nothing else nothing else and we're
still striving to get to the other city
which is the continuous deployment part
where where all of the decisions would
be made as the codis is being created so
that's that's the world that we're
talking about so I work in a company
called f-secure have secured us cyber
security software and my team in
particular it's a corporate endpoint
team and we do Windows endpoint
protection clients which basically means
you know simply said antivirus firewall
that type of things so different
mechanisms of keeping a personal
computer safe and I joined this
particular team and this particular
company two and a half years ago it's
now my second time around in the same
company I also used to work there 12
years ago when that company was starting
to implement agile in the first place
and it's actually a really fascinating
thing to kind of like you know going
into a different organization or
actually a couple of different
organizations and then coming back home
so to speak and I'm looking at kinda
like what has changed while you were
gone and I'm looking at some of the
things we're kind of you realize if you
were some of the block books of progress
while you were there so so it was
actually good that you were away away
for a while but again when I came back I
came back still at 2016 into an
organization that told me that in the
team that I joined delivering frequently
would be impossible so we had usually
typically we would have smaller we call
the maintenance releases about quarterly
and then a major release about two times
a year so every second one of the
releases was a major one with some cool
new features and every second one was
kinda like you know patching it and and
we were very used to that that rhythm of
of working and as someone who works a
lot with testing I know how painful it
is to be in that kind of project the
last weeks just before release are awful
and having been in better places I know
that that's not the life
of a human being if you can have a
choice you do not want to have that but
you would want to have this you know
steady pace of getting a good night's
sleep and not having this you know
rushed feeling in the end trying to get
the right information together at the
right time it should be you know every
day is the good time to get that
information and and I knew from my past
experience in other companies that had
implemented things like continuous
delivery and it was a complete game
changer for for testing related stuff so
again doing smaller things was was a lot
not easier so I started having this
discussion around like well why is it
impossible like I believe we could do it
and and I got a couple of answers that
were kind of relevant and foundational
the first answer was that well the type
of software we are doing
no one does continuous delivery on that
type of software so you know even Amazon
like they have whatever 30 thousand
computers you know that's only 30,000 we
have five million we have to install in
millions basically like anytime we
deliver we talked about millions of
computers because we're talking about
home pcs not servers somewhere so while
the usual stories around continuous
delivery that I could find were around
this idea that you know your users in
mathletes were somewhere and they were
connecting to a service with some
interface somewhere the world that I was
now joining again was a world where an
individual computer could basically have
whatever in it if it was a a consumers
computer you know your home home
computer
I can't prevent you from installing a
VPN client there that maybe doesn't work
together with our software and I have no
idea which VPN client you're going to be
using same thing with other antivirus
software most networking applications
and a lot of the programming tools that
we actually use conflict with anti
viruses because there's so much file
editing going on in the way that we work
that depending on how your environment
is set up I just
cannot have all of your computers at my
word I can't build that kind of an
environment so there's no docker image
that I can take out of all the millions
of different kinds of computers that are
completely under someone else's control
but of course the situation that I came
into the team that I came into is it's a
little bit different so I don't work
with all of our products we have a
shared codebase but I don't work with
all of our products I work in particular
with this one product which is oriented
towards a service security as a service
and that since it's for corporations
also means that corporations have this
habit of you know just at least a little
bit having a more similar environment
within their company so so that their
administer
see the whole scale of of variety but
the basic software that we're building
it's still for essentially millions of
different computers whatever flavor of
Windows it used to still be Windows XP
that was supported all the different
ones that have come out ever since you
could have any of them in your computer
and that was the environment we were
building for so I started looking for
others who had done things like this I
wasn't actually able to find many but I
found many that had you know done
similar steps in some scale at least so
I was sure that that there is nothing
that would completely block it so we
just needed to kind of like invent and
and figure out what the practices here
would look like and the other thing here
what people would say is that well since
this is a corporate thing it's a for
businesses no user no company no admin
would allow us to deliver frequently so
again all of you know the interruptions
like maybe you you know you need a
reboot that's kind of a bad thing every
time you deliver Windows software you
know from your own in those machines
probably by heart that it's super
annoying that you have to be rebooting
all the time so we had all these you
know considerations of like you know we
don't want to cause so much trouble like
what if we would do this you know even
once a week like they would just
remember us after the reboot
engine that you know makes everyone
reboot regularly so that's not really a
perception that you you want to have and
the first thing that we actually could
come up with on this one is is that in
the recent years we've actually been
implementing a completely reboot les way
of introducing new updates to do that
and it's not that special in that sense
but but we were just so used to the idea
that there would be a reboot here and
there and and and and there's nothing
that we can do until we learn that of
course there's something that you can do
it's the reboots are always caused by
locked files if you don't have a locked
file then you don't need a reboot so if
you figure out a way of going around
that it's just a technical problem then
then it's all possible and the third
thing that everyone kept telling me on
why this would never work is that well
to build a set of installers so that we
could make a release it took us five
days usually by at least one person
fully working on it but usually by
another person at least occasionally
supporting so it's probably like more
like 7 Mondays that it was taking and
there were some aspects of testing in it
so so not only the the building but some
aspects of testing that needed to be
done manually but that was actually
quite little that needed to be done on
that side but the big part was was all
the different things on giving you the
right executables together into the
right kind of package having them signed
so that there's different people signing
they have to be actual people involved
in that signing process because if we
end up releasing software that somehow
gets compromised and you know someone
can fake being our software that's kind
of a sick serious thing for a security
company we do not want that so all of
the signing mechanisms related to
Windows we had to have to have those in
place and that was a really really slow
process and even though we have made it
a lot faster it's still the process that
makes us from keeps us from having
continuously deploying things
automatically because there will always
be that manual step
unless I manage to complete my so far
two-year project of trying to get the
practicalities together so that we could
have automatic signing and the proper
trust relationships technical trust
relationships in in place so the the
people stuff is it's now okay but the
technical implementation is still kind
of on the way but this was was really
the case where where I went and a lot of
the discussions that I needed didn't
have were around kind of you know funny
that you should say that it seems that
you know other people are able to do it
and even other people inside this
company are able to do it like why are
we not looking around at all so first of
all in an antivirus software it's not
just that it's one layer or one
component it's actually a lot of
components it's 54 components that we
are building within my team and the
teams who build into that system but
also there's this what I call service
components basically databases that need
to actually be changing every single day
multiple times a day because otherwise
if someone comes up with a new virus we
don't have a detection for it we don't
have a removal for it we need to
actually be moving just as fast as any
of the bad guys in in this area so we
had actually been doing this this kind
of you know continuous delivery even
continuous deployment on that area for
quite many years I didn't even realize
that we were doing this already before
the whole continuous delivery continuous
deployment became a big thing because it
was so kind of like you know separated
from what I was doing on the higher
levels of the product that I wasn't or
many other people weren't paying proper
attention to it we also during the the
first year of my return in f-secure we
completed a long long project that had
been been going on for quite some time
which was basically introducing a in
there's the databases part which is on
the bottom then there's an engine kind
of framework somewhere in the middle and
then this whatever I'm building with my
teams on the top so the middle layer
they had decided at some point that they
want to go version
basically by so that they don't have to
care about which version it is there so
all the api's need to be compatible to
different directions and you know all
the stuff that we talk around how to
make make these fast deliveries possible
so we were just about to do that and I
was there for the first year to complete
a delivery of the client that included
the change into the version las' version
less engine framework and it didn't
really feel like we would get the full
benefit out of it if we didn't really
follow with the the whole product into
the same same mindset and also we had
figured out with the some of the newer
technologies I don't know how many
generation of technologies were right
now in it's still the same product we've
been building it for 30 years now but it
has completely been rewritten so many
times that I I think nothing of the
original is there anymore but in the
current version there's this possibility
and and we have to get out how to do
reboot less upgrades which was a big big
blocker so having these kind of
discussions unlike you know we could
actually do this we maybe could you know
try what if you know in some scale we
would start doing this maybe we can
figure it out maybe we can delay the
actual decision and we can try it out
first
that's how we kind of got together and
really why would the product facing part
be so different it's not actually that
different so again as a security company
we realized that you know since we are
working in defense against so-called bad
guys we really cannot be moving so slow
and different threats around how people
are trying to get on the computers and
how we are even detecting if something
bad is happening they've been changing
so much that we can't really wait three
months to have a fix available we need
to somehow figure out on on how to be
just as fast as as the other side so to
speak so we didn't really put together
any project it was just something we're
in the devel
the team that I worked in back then in
the lead quality engineer role we talked
I talked in particular to my manager and
I got the manager convinced that he
needs to put one goal into everyone's
annual goals and the one goal said you
need to be able to release in two hours
that was a one year's goal and everyone
was a little bit grumpy first at that
I'm like oh look we get these insane
goals like it's you know so much work
like if we start practicing these five
days every time we don't do anything
other than releasing and after the about
the week of grumpiness it's like okay
fine we have to do it let's just take
care of it right now and you know a few
months later it was almost like magical
when you got when I got over the idea or
the team got over the idea of not
wanting to do this it didn't seem like
it was such a big deal after all
it wasn't super expensive it was just
that we need it to be very you know
structural and think through what are
the the faces in our releasing and have
everyone everyone in the team implement
bits and pieces that would help the flow
so that we would have test automation
that we can easily run on different
environments different combinations
different products and we would have all
the different tools on on building a
package in a reliable way
out of the in the trunk and it wasn't
that big of a thing but we got to not
two hours but well actually three hours
in that that timeframe another thing
that is kind of good to understand
around in these what we were doing and
what kind of things we were practicing
is around the way we're building things
so a lot of the practices kind of the
originating point even for us to do
things is we think of us in like we're
not doing XP extreme programming even
though we're natural house the technical
practices are not in that side but our
technical practices are more of one's
like an internal open source community
so all the code is available for
everyone anyone in any role has access
to the code and can make pull requests
pull requests are usually
out of a branch that leaves less than
than a day so it's a very short-lived
time there's a rule well rule more like
a saying that I keep on quoting to
people who have trouble getting their
their things merged in is that you know
it should be the burden of the statue
when you do smaller things you usually
suffer less so if you're staying in a
place you usually get it by stuffed by
the passing birds and that's really a
lot of the experience in the in the
version control but we're basically for
the windows clients for the 54
components that we're building we are
sharing them with teams well teams in
Helsinki there are several teams in
Helsinki so mine is just one - twelve
people but there's other teams as well
then we have teams in st. Petersburg
working on that and we also have an
office in Poland and now this year we
are moving also to have some of that
development into the same codebase from
South Africa so our practices have to
scale to the idea that we don't get to
meet everyone every single day but we're
putting things into the same codebase
and out of that codebase we are making a
release basically by taking out whatever
is in the trunk right now and making it
available for for our clients so my side
is that the little sauce for businesses
think the orange one and all the numbers
are from only from that perspective
but since every other direction into
this this kind of bubble that we have is
also committing code into the exact same
codebase we need to have common rules on
how to do that and basically it is to
never break the trunk always have test
automation unit testing and and the
higher level test automation and make
sure that it stays blue blue all the
time and I don't even consider that a
release practice that's just a way of
how we work together so that we have any
chances of knowing where where we are in
all of that but I just checked that we
had 42 people
tributing lines of code into the the
code basis last year for the components
that my team is responsible for
releasing and one component had nineteen
contributors so mostly were actually
being quite successful with the idea
that you know anyone from any team can
go and make the necessary changes in
whatever component there's just the
Guardian available in the other teams so
for us this all meant that we needed to
find a new way of delivering a new way
of delivering so that we would have not
just a cadence like you know not every
two weeks on a Friday we would make a
release we didn't want that we wanted
that whenever something valuable wasn't
available something that the users could
benefit from or where we would want to
see that it's not risking the users we
would want to deliver that throttle the
release a little bit so that we could
see that you know the first computers
the telemetry shows that they are
getting it nicely and then only open
their the channel completely so that all
of the millions get updated and the
release is when they were tiny the
testing effort even the manual thinking
testing effort around that is much more
manageable but then then if you have
this huge huge thing that you need to
work on and we kind of focused all of
our energies into making something
valuable and estimates is not something
we consider valuable and that's
something we'll we kind of got rid of us
as we were starting to do this faster
releasing as well so I find from my
experience having gone through this now
with two different organizations where I
have worked in that this whole getting
to less than a week preferably daily
releases it's a complete game-changer
and sometimes when I have then
discussions with people around like why
would I think of it as a game-changer we
know we're still testing we're still
developing we're still releasing we're
still managing we're still doing the
same things in in many ways there is
nothing new
in the world in the last 20 20 years I
need to kind of go back and say like why
do I then feel like I'm living in a
whole different world right now than the
world I lived in 25 years ago when I
started in this industry like if it's
nothing new
why is it that it feels so different so
this whole continuous integration
continuous delivery and and the fast
feedback cycle it has clearly changed at
least my profession the testing
profession completely and talking to my
my fellow developers I find that it has
changed their life quite relevantly as
well so what I didn't try to kind of
explain to people and try to figure out
on how to kind of say this is I find
that metaphors are maybe the best way
that I can I can try to approach it I
find that you know if you think of two
things that look kind of the same you
had a pool you know swimming pool or you
have a bathtub you know both of them are
containers of water well some one of
them has a little bit more water but
it's still water you know just like you
know it's still testing it's still
developing it's still water why are
these different and it's really easy
sort of for us to see that of course a
bathtub and a pool they are a completely
different thing there are things you can
do in a bathtub and there are things you
can do in a pool so I don't know looking
at the bathtub we have in the hotel
yesterday and my daughter here in the
first row using that bathtub and
drinking some soda in that bath next to
that bathtub I see all the the the cans
dispensed I was thinking maybe she was
having a party at the bathtub but
usually normally we would think of a you
know a proper party to happen rather on
a poolside than a bathtub side so that's
that's really not a thing we have things
like lifeguards we need lifeguards when
we have multiple people in the same
container of water but we didn't need
them when we had the bathtub and we were
just using that as the container of
water
so there are things you do in a bathtub
and there are things you do in a pool
and and they allow you to do with very
different things and this is how the
continuous releasing the past small
slices of delivery
changes our world that it enables us to
do things that weren't there before so
one of the materials that I really
really enjoy on kind of using as a frame
of reference on where we are is I have
to be it from here because I can see
from there by poor hum-hum and so I'm
definitely just a practitioner and these
kind of like great thinking pieces are
really really helpful in in
understanding kind of where we're going
so when I say the things change when the
rapid releasing started to happen
practices have to look different we can
do different kind of purposes it gives
us a very different environment so you
would branch differently you would
probably test differently you can't test
in the old way anymore where you would
have a release every three months you
can't test in that way when you're doing
a release more frequently your
architecture needs to change your
releases cannot be scheduled and planned
and not kind of like you know taken as a
plan and being made sit in a release
train which is a safe work version but
they're kind of you know organically
flowing through there the whole system
probably also the practices around
infrastructure and databases are going
to be changing so some of these words
here are much more relevant for the the
web-based services type of world that I
don't live in so I find that when I'm
trying to kind of place us on that map
we're somewhere more on the right side
but in many ways we're somewhere in the
in the middle because we haven't yet
figured out all the ways to get all the
way to the right or how it would
actually be different and in this kind
of a environment but again if we have
this we need to make a release right now
we take the trunk and in three hours it
can be out
it's not a bad solution that we we have
in place so so it's definitely something
something kind of nice that we've done
so all of this kind of leads me to this
idea that even within the same
organization we are not all safe
so I mentioned 42 people my team is is
12 people not all the people in my team
has actually committed anything last
year because some of them identify still
us as testers who don't do automation so
they might not have have any commits as
such but they're more like you know
preparations participating in
discussions bringing in certain
perspectives so I find that I really
really love to be in my team I really
enjoyed there I like the fact that we
can work without a product owner and we
get to make decisions about the health
of the product we get to do all the
operation stuff we can look at the
telemetry we know more about our
customers from you know what they
actually do then than the theoretical
part of what they say they would do so I
find that kind of like right now my team
that's my good place but I don't always
get to just work within that one corner
we sometimes having that common code
base I need to go and work with some of
the other teams and then I've given them
these really loving nicknames I called
one of them a soul-sucking place which
basically means that they have very
by-the-book agile practices where they
stand up every day and have discussions
around things and very team inclusion in
everything sharing everything almost
feels like they talk about what they eat
today but you know you need to share
that in the team and it's a little bit
different place and I feel like it's
using a lot of my energy not of the
value that we want to deliver but more
on on certain kind of like you know risk
aversion practices that's what I would
call it so risk aversion practice is
nowadays they they seem to be sucking my
soul out so that's why I call it even
this for this name and then we still
have sometimes someone comes up with out
oh we need to build a new product
completely
and we set up a project I will give it a
date it's gonna be out in September
that's when it needs to be out there and
we might not have even recruited the
people to do that project when we say to
date and it's going to be out in
September and that's the style of
projects or delivering that I call the
insane asylum and it is kind of targeted
towards this idea that we would only
release once in the end so in my good
place we release either daily or weekly
so any day of the week could be that
release day but our idea is that we
since it is a relevant size of a package
that we will be updating with the
changes from the 42 teams we still do
not want to deliver that we're figuring
out way of still splitting it in smaller
pieces but we don't want to do that more
than once a week once a week but we want
to be able to do it on any day of the
week not just on a particular day then
with my soul-sucking place we usually
work with two-week cadence so the day
when we are doing a release like
everyone knows that it is really well
kind of scheduled like it's gonna be
every Thursday so there's a planning and
then you know all of the moves towards
what us releasing and there's this this
kind of like joy boredom boredom boredom
boredom a little bit of joy pain pain
pain and that's kind of like a profile
with the two weeks so again the pain
isn't as high because it's only two
weeks but the pain you can control the
peak of pain there always and in the
insane asylum I really wish this
wouldn't any more exist but even with
what I do
I still live through this in the end of
the project we're supposed to have it
all available and we are sometimes still
struggling with having 20 30 teams
working in these projects get them to
the idea that we should at least for
ourselves be delivering continuously
even if we didn't give it to the
customers you know you don't have to
share the link that's fine but make it
available don't keep it on your your
development machine only or only in deed
I environment the attitude to quality is
often very different in these three
places in the good place we usually talk
about like this kind of concepts or like
I really care about production what's
going on in production how can we make
production a little bit better and for
example right now my team has less than
20 tickets in JIRA out of those millions
of customers we have only 20 tickets
because when you take it comes in we try
to take care of it fix and forget that's
the basic idea
so we care about the production and how
the feedback and and and things in
production are a lot in that that type
of a model in the middle ground place
where we still work on an agile cadence
it sometimes feel like we need to you
know get together and plan and move a
little slowly and think of things and
let's make one more plan and and the
current work you know rapid
whiteboarding isn't and the production
orientation is it isn't quite as much
but it's kind of a risk aversion it's a
little bit more there and in the insane
asylum when they're trying to get
control over it I find that the motto we
use mostly in the organization is I care
about my feature of the production and
we need to repeat this a lot of times
for every single developer care about
your feature all the way to production
but it's not enough you need to care
about the feature beyond well in
production actually that's that's where
you go into so these are easy to see
when when there's so many different
kinds of projects the way we deliver in
the good place is that we start together
we finish together and it's a very
organic discussion oriented way of doing
things you know you go on a whiteboard
when you want to have a discussion you
you call and do a remote whiteboarding
session if you want to have a remote
discussion and when you are about to be
done you're never delivering anything
all by yourself you're never alone so
there's always the safety net of of
other team members so you can pull
whoever you want and make sure you know
everyone is always available for others
but there's no strict process saying
that you know this person it's approve
doing your work it's just you need a
second person because we don't want you
to be alone the solar sucking place does
a bit of this zero left like who gets
which ticket so it's in this state these
people take it I really think that zero
stuff is is one of the things to mostly
suck out my soul and the insane asylum
is anything that you can think of you
create a new ticket in JIRA and then
someone is trying to make sense out of
those tickets on how they are like you
know how many of there are like is there
any progress and where we are and then
at some point of the project when
someone is worried about the schedule
then comes the the managers usually the
high-level managers who force everyone
to sit hours and hours in the meetings
scheduling all the tickets so that we
know if we're gonna make any schedule or
what the schedule is gonna look like and
I just look at that kinda like why are
we still doing this like we have managed
to not do this in so many projects why
why some still end up end up like this
so it's a long path for us to grow in in
our organizations maintenance also very
different to in the good place it's a
fixed and forget and when things go
wrong things break in production like
you can revert it but a lot of times
it's actually faster to fail forward so
you can stop that you know in my world I
can stop the the impact being any wider
but I often cannot revert an individual
person's computer but I can make sure
you know all of their hundreds of
colleagues or thousands of colleagues
don't get to experience the same problem
that the first one saw so failing
forward and fixing that one computer
antics in the overall deliverable is
much more of the the way in the so
certain place usually we spend so much
time with estimates that we don't have
to deliver as much and in the hints a
Lana Simon asylum it is really building
these maintenance projects there are
about half of the effort that we we
generally use so it's always the cycle
of new features and then maintenance new
features than maintenance so going
through that cycle and we're so used to
it that sometimes it's hard to avoid it
uncertainty in the good place you know I
feel quite tolerant with the level of
uncertain
I get the the colleagues together and we
have discussions even when I'm here I
can have a discussion online with them
also well I'm lucky enough to be here
and not having to be there at the same
time that's part of the way we are
trying to work so that there's no
dependency on an individual person I
kind of enjoy being at conferences the
soul-sucking place
well uncertainty is managed but
sometimes I say that we use about 70% of
our time into the uncertainty and 30%
only into the value so they can be a lot
of practices around that and in the
insane asylum it feels like you put a
gun to your head and and there's one
bullet out of six and that's how you
kind of like deal with it right you just
have to take whatever comes because the
risk is so large that it's hard to
manage anymore so you haven't split it
up so all these different places
different projects you know none of them
are hopeless they're just on a different
place in the past and we need to keep
telling the stories within our
organizations to get us get the other
teams get everyone onto the path of
having the the lesser pain the practices
do change the development practices the
testing practice product management and
management practices Jeff talked about
all of these different categories
actually in the morning keynote and it
feels really like you're in a completely
different place so the good place is one
where you somehow end up with a
reputation of flow like you know things
just go through your team so no one even
asks you of schedule you know they tell
you of things of importance and you will
say like oh I acknowledge this is
important they just assume it comes out
they don't ask how long it's gonna take
you they know that you will do it as
quickly you know in small pieces as
possible and that's what I get to
experience so it's it's a completely
different relationship with the business
people when they don't you know ask you
know how much is this gonna cost us at
first and they don't really care about
that answer that's only for them to say
that they can't get trust your delivery
ability so they don't want to pay for
the estimates it's it's a a comforter
for them
there's a lot more effort available to
put into the impact and the value that
goes out of them whatever engine we have
that is is delivering this and less into
the all kinds of padding risky oriented
management practices and and change
control boards and their things where
you realize you know you put a list of
things you're doing whether it's you
know time to take care of this right now
fix and forget and then there's things
where you know time takes care of them
like some of the things just aren't as
important as others and you start seeing
these patterns a lot more when you have
the continuous feedback cycle on what is
pressing in the production right now
what would be the thing that you would
look at right now
the code base is your ultimate truth
instead of all of the documentation that
you try to wishfully think that that you
would have so that's a nice thing and
testing really kind of flows together
with all the rest of that team so that's
a very nice and collaborative and close
relationship it's not only automation
but it is only the you know thinking
through all the things that might break
because of this that that we're doing
doing together and finally when you have
this continuous feedback loop it is like
you listen to that feedback and you get
a little bit better if you keep on being
the same you're saying in a year but if
you're a little bit better 1% better
every single day in a year you're
actually 38 times better than you are
right now so learning listening to
feedback that is absolutely the winning
winning way of working so we talked
about this idea that a path tub and a
pool are two different things
they're both containers of water but
they serve completely different purposes
and in the sense of continuous delivery
and continuous deployment delivering all
the time it enables you completely
different practices thank you
I think we have time for a question
anyone feel like asking a question
there's couple I can repeat the question
okay I can hear you and I can repeat
your question hello actually just wanted
to understand like you just mentioned
that in your team there is no pew right
so I just wanted to understand how the
user stories are coming in and if there
is a change or manipulation in the user
story how has a team you are taking care
of all those activities so can you brief
me something in that sense the question
is since we have no Pio how does that
work I spent 45 minutes explaining that
yesterday so there will be a video with
a long long version of that answer but
it's really the same way as business
people would get those you know they
they fish them around and they put them
in some kind of a list they have some
idea of what's most important we do that
but we also know the technology impacts
of whatever we decide on on doing that
so it's very similar it's just that the
belief system is that serving the
customers right is the most important
thing that we should do and the most
important thing should not be left for
one brain
it should be every brains problem so
that's basically this the summary of all
so I have one more question like it's
related to continuous delivery so like
you just explained how how have you
implemented the continuous delivery in
your team so for example if I want to
implement the same thing which you are
implementing in your team and how to
make sure like nothing is breaking when
it is going into production like we
should take off care of test automation
or continuous testing how you're making
sure of all these activities so this is
again I find it difficult to answer some
of these
so having test automation is a good
thing my first project in my before
before this company when I went to
continuous delivery we did it completely
without test automation
so there are other practices that you
could apply as well so I think we should
have a longer discussion about this
after that yeah I have a question so
basically you you spoke about variable
frequency time boxing but will that not
break the cadence if there are multiple
applications you know going going into
boxes boxes so it's again what I mean by
that is it's like if we want to do one
release on this week it might be any day
of the week instead of having a
particular day when you're scheduling
doing a release and I do work still
towards figuring out ways of changing
the product so that this could happen
different times of the day so that
whenever it is ready it is not you know
you could deliver that application right
away my question is as you went through
this transformation journey what was
your project management strategy like
yeah because how do you convince those
people who are with this 1980s mindset
to accept this and what are the new
matrixes that you came up with instead
of the old ones usually don't have
project managers for most of the things
we are very team oriented and the teams
kind of work in a networked manner so so
that's that's kind of we've organized
this this like a network way of
co-managing whatever we are delivering
but yeah the lean practices are very
heavily there definitely in many other
things we can have a longer discussion
about this so that I can understand the
question better so yeah thank you so
thanks everyone I think it's it's time
to take a break and I'm gonna be around
all day today so I would be happy to
have more discussions on any of the
topics you that you know piqued your
interest Thanks
