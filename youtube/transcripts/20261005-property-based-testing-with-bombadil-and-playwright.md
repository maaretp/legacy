---
title: "Property-based Testing with Bombadil (and Playwright)"
video_id: ZjoN2_FDG8Q
url: https://www.youtube.com/watch?v=ZjoN2_FDG8Q
upload_date: 20261005
duration: 26:16
channel: Maaret Pyhäjärvi
tags: []
---

# Property-based Testing with Bombadil (and Playwright)

> When AI makes the thing Cem Kaner found hard to teach to testers at large 14 years ago something you can do and learn within a day, a talk is in order. Well, especially if that makes also an excuse to deliver my talk number 600. We all should know what properties are, and how they matter in test automation. Particularly if we use model-based / property-based tooling, but also otherwise. Some things should always be true, and finding problems I was missing on a little AI-app I was using to teach with this technique and the systematic approach it allows for in automation-assisted exploring is worthwhile. 
> 
> This talk was delivered for CGI Testing Community, and shared in public for your convenience as everything in it is public information.

## Transcript

_Auto-generated captions from YouTube; no punctuation or casing. Lightly de-duplicated._

All right.
Uh we had something else planned
originally for today. Uh but as that got
cancelled, I decided that this is a good
opportunity for me to kind of steal some
space and and share with you something
that is very fresh and and very exciting
for me. Uh well, basically there's two
things that are kind of exciting. This
is actually in the number 60 600 uh talk
that I am delivering. So yes, I am
counting uh uh but also uh the contents
of this presentation are things that I
have done uh this week uh for the
purposes of of um having to teach
specificationbased testing to a group of
developers and wanting to build that
that kind of like a bridge in a in a bit
longer session. But I felt like this is
something that everyone should know and
if you don't yet know this uh this is my
opportunity to you know make you more
aware of of how test automation of of
the modern days today's test automation
in a way could work or should work and
and what are the struggles that we've
had and some of them which we have
solved over the last 10 years. So we're
talking about property based testing and
you can see from the style of slides
that my original idea was not to present
you slides. I created this like an awful
lovely script that I I have um on on uh
going through. But since uh we are
living in the age of AI, you give the
script that you know and you're happy
with and and you're kind of like
comfortable uh to an AI and say make it
visual and and that's what I did. Uh no
edits uh whatsoever manually on the the
presentation side. But you can also see
that the style is not exactly CGI style.
So colors are CGI colors, but style is
is not exactly that. So I I basically I
created a a talk and a demo for for uh
your purposes only uh one-time
presentation only. I wasn't planning on
on starting to become the educator of of
all of this uh in the future. I hope
that there's someone in the audience
that would volunteer to be that.
uh we'll talk about bombadil and
playwright but uh actually instead of
talking about bombadil and playwright we
will be talking about a thing called
properties property based testing what
is a property and how does that work
so basically about a month ago uh I
mentioned there on our one one of our
channels that there's a new tool in the
house the tool is called bombadil and uh
it's not just that bombadil was somehow
kind of like unique and exceptional and
all, but they were kind of nice in the
way that they were wrapping uh a running
of a web UI, generating clicks on a web
UI, uh adding logic on what you would
click on a web UI and this idea of
property based testing uh together. So
this tool it runs in a loop. Uh it it
figures out where you are, what you can
click, what kind of things you can uh
write into the different fields. Allows
you to uh take control over the the the
things maybe specify that you know these
kind of fields you write numbers, these
kind of fields you write text. These are
the kind of numbers you would write. The
it automatically generates you scenarios
where you basically you click different
things in different order. But the idea
of it is that the properties are things
that are always true
and wherever it ends up whatever it ends
up clicking it is always checking for
these always true uh assumptions. So so
it's it's a bit of a different way of
thinking about it. You're not uh kind of
like handcrafting which things you're
clicking. You're letting the clicking
happen automatically. You can direct
that in some way. But the essential part
is is these properties. Kim Kirner
talked about properties maybe like 10
years ago uh 101 15 years ago it's it's
already been a while and and he made an
observation about the properties that he
was asking testers back then to to
design that testers at large were unable
to define properties like we couldn't
for the life of ourselves we couldn't
figure out what are these properties
what are these things that should always
hold true like all of us can say things
like obviously I don't want to see big
visible error messages. That's what we
can say. But kind of these rules where
you know like you would go into the
business rules and saying like you know
you you're not ever allowed on a banking
application for example if uh the
balance can never be negative or uh if
you get declined the money can't vanish
and and and and never you can you know
go above whatever set limits. So we we
didn't really have the the vocabulary or
the skills to to define these kind of
things and these kind of expressions
properties they are super essential in
test automation because they are
actually the assertions the checks that
we need to automate. So instead of
handcrafting every single one of our
things that we are looking around the
user interface, we need to find a way of
saying things that are more usable,
reusable and that's what property based
testing testing is about. So uh uh the
way that this this usually then builds
into tools is is that uh uh when you
want to write property based tests well
obviously you would start probably with
a tool that is essentially for property
based testing uh uh the authoring of of
that test automation it probably
nowadays would happen with AI like for
me uh uh I definitely didn't write any
of the code myself all of the authoring
work was done by AI for this talk. Uh
but then the execution part, it's not AI
that does it. It is actually that uh uh
property based testing tool, the walker
walker that uh walks around the user
interface, in this case web user
interface or well it could also be a
tester who has you know decided which
buttons to click because they are the
end toend flows that users have have
expressed. Uh properties are in the
space of oracles law. So how can you
tell whether things work or not? So uh
even if property based testing tools
intertwine this execution and oracles,
you can also take the properties and
just you know boo push them into other
uh other tools that you would maybe
have. So what I did for demo purposes is
uh I had that prompt. That's how I
created my my property based tests. Uh
uh I told uh uh uh GitHub copilot that I
have a project here uh it's called ATM
and uh I was fixing it on Tuesday this
week. So I want the Monday's version
into one place and the Thursday's
version in another place so that I can
demo for my colleagues uh uh the
difference between the the Monday and
and and and Thursday uh versions. So
there's a before the fixes after the
fixes versions that I I set up. So I
started with that and then uh I prompted
on hey give me uh basic simple most
basic that I can think of property based
tests uh with default properties. These
are things that should be true for all
systems. Uh uh no HTTP error codes. So
no big visible error messages, no
uncaught exceptions. Uh don't hide the
messages if they happen. Uh don't uh let
them happen kind of like um under the
hood so that that users just don't see
them. Uh don't uh expect something to
happen that never comes back. Alert on
that and and no errors also in in the
console like simple ways of you know
four ways of saying no error messages.
That was basically the default
properties. Uh so I uh uh prompted
And I said I want to be able to run
these tests from the command line by
saying demo Monday or demo Thursday. And
uh that's you know like you know make my
wish come true like magic. So if I would
now run uh demo Monday you can see that
uh I am writing it with a small letter
instead of the the large letter. uh well
AI already is you know deciding for me
that I won't probably remember when I'm
demoing whether I write capital letters
or not. So it's doing some of this this
thing for me kind of like it's it's
clicking buttons I could have also
configured it it so that that it it has
the the browser open. Uh usually for
debugging purposes or demoing purposes I
might have set that up but I didn't say
I want to keep the browser open. So most
of this stuff you can also run in in in
headless mode. So uh usually uh the
default time that you end up with is is
uh 60 seconds. So for 60 seconds it's
clicking everything and the test target
that we have it's that uh ATM there. So
I have the the ATM here. Let me just
show it to you.
There's my
thing here.
So this ATM uh clicking on it uh you can
see there's like an admin panel or a
debug panel that gives a little bit more
control but you would you know uh you
would try to figure out if if the ATM is
working and I've done you know I've I've
actually tried to do my best in creating
a simulation that wouldn't be full of
bugs. So I didn't want this this to be
uh failing all the time. So the one
minute uh your version for uh Monday's
version which is supposedly the more
broken version uh that uh uh passed but
we only tested for uh the let me just
sorry find my thing again here. We only
tested for for these kind of things. So
no big visible error messages or hidden
uh error messages. Uh I could obviously
run this against the Thursday version as
well, but uh randomly I picked the
Monday one for better chances today. So
both these versions pass whether you
believe me or not. You can go and and
install these on your own machine and
play with them. Uh uh writing that demo
Monday or demo Thursday, you get 60
seconds of watching it do some kind of
clicking. And again, if I would have
prompted for it, it would have actually
let me watch it. It's it's kind of
hypnotic when you can see what it writes
and and and and and pay attention to the
the uh numbers.
So uh this doesn't notice if the the ATM
rules are broken in any way because I
didn't have any properties like that. Uh
but also as uh the uh AI tooling was
trying to generate me the test cases, it
wasn't happy with the test cases that
got generated. So first kind of like in
every single field it was trying to
write the letter D one or many times I
don't know where the D comes from
because it doesn't definitely come from
the Bombadil tools name. Uh usually
people choose something that is kind of
like you know familiar to them as as the
default. Maybe that's why it is a D. Uh
and then it realized that hey actually
there will has to be a a generator that
creates numbers because this is very
clearly a thing of of numbers. So it
already fixed it for uh for the demo
version. Not a very complicated one to
set up and I I recommend you would try
these kind of things yourselves.
Uh for uh then uh kind of getting to the
the actually interesting stuff uh which
is the teaching the spec domain. Uh the
way that you do this is uh obviously you
can ask uh AI particularly say uh use
playright CLI and and go and figure out
what the application has and figure out
the properties. So you could do uh
agentic exploratory testing specifically
for properties on the user interface.
But also there is a a uh antithesis
skill uh called research that you can
run against the codebase if you have
access to the codebase and it runs you
an analysis of the kinds of things and
again somebody created a quite essential
uh nice uh uh property based testing
helper skill uh and and when that ran uh
it created me a listing of helpers
action generators uh total of of of more
than uh uh 30 properties.
So I think 34 is is currently the number
of properties my my tests include. Uh
and uh again I didn't have to do all of
the things that Kemp Ka talked about
years ago where they said like testers
can make sense of this. AI can make
sense of this in a very very lovely way
and then we can kind of like you know
try to then decipher like it's called
this do we understand what this is? So
that's that's how we would uh build
these these kind of things. So uh for uh
these tests uh basically uh I ended up
uh saying that uh uh I already did this
earlier this week. uh uh I ran the
research skill and I had already created
that research scratch book uh where the
reasoning of what the property should be
and it added me 20 more properties and
then I'm like oh for demoing I don't
want to have to say demo Monday now I
want to say magic Monday and magic
Thursday so uh let's see you know uh if
we have magic Thursday which is uh the
version where I fix things. You can see
the asterisks here. The ones with the
asterisks are things that were broken on
Monday that I did not know until Tuesday
when I tested with property based
testing this application for the first
time. So, it found actual real problems
that I needed to fix in my application
before I was using it for for teaching
uh better analysis of of high quality
higher quality software. maybe not even
high quality because again this is a a
simulator but a lot better. So for magic
Thursday, uh what it does, I told it for
demo purposes, we really want to see it
move. And again, the same story, 60
seconds of doing things that came out of
that research skill. Some of those are
properties, some of those are
generators. And if I didn't like the
fact that it writes really really long
numbers here in the user interface, if I
wanted it to kind of like stick to more
realistic numbers or smaller numbers, uh
I could guide that
uh as as uh as I I go through this. Uh
since we're running against the Thursday
version, uh I know for a fact that uh
for a 30 minute run, I can still find
usually the one problem that I haven't
yet figured out how to fix. uh uh but uh
usually if I take a 60-cond run, I'm
rarely so unlucky in my demos uh that it
would manage to to find that. Whereas
the Monday's version,
uh when we get to that, if we run then
the magic on Monday,
uh I would expect us not to have to use
60 seconds because actually it gets to
the uh you are breaking your business
rules very quickly. finding two
violations.
So I had well I could also guess what
these these mean uh by understanding
that you know uh if you uh withdraw
money elsewhere you are able to uh
exceed the account limit uh I can just
tell you that means a bad problem in an
ATM or um uh if I uh don't uh respect
the account limit similarly it means a
bad problem and all I had to do is is
generate tests uh apparently because I
had a tool that was able to walk the the
user interface or the APIs. Both of
these are actually included in the in
the tool and able to express as
properties the things that I was was
expecting. And this is how we should be
doing test automation. So the Monday
version stops in seconds. The Thursday
version well holds at least for those
60-cond demos and and trials but uh does
fail uh somewhere in about 30 minutes or
did fail. I did try fixing that but I
haven't had the 30 minutes time since to
to run it. So it might also be that my
latest attempt of fixing it by showing
uh the fixing agent the logs that uh
were reporting these these are really
readable for computer uh and then uh
reading kind of what are the changes uh
that's how you would move through uh uh
building systems like this.
Well, I wasn't happy with what I had
done even though I had, you know,
generated uh all kinds of tests and
found actually four really relevant
problems for a simulated ATM. I I kind
of like wanted to also show you that,
you know, this is not something that you
can do with bombadil. The bombadil is
not the magic. It's the tester thinking
about the properties, the things that
should always be true. That is the
magic. So taking these to you know your
your existing test automation be it
robot framework or be it uh uh playright
or or some kind of an API tool uh taking
properties on that level. It's basically
a code plug-in that you can do. So for
purposes of that I created magic
playright Monday and magic playright
Thursday. And you can even see I think
this is where I accidentally told AI
that I want to say magic playright
Tuesday because I already got confused
with the days and yet like magic it
understood me and it didn't make me feel
stupid like many of my colleagues when I
happened to say the wrong day even
though I know exactly what day I meant.
So sometimes, you know, it feels like
working this way is so joyful because
you can avoid some of the hard
conversations and the bad feelings, but
then again, I always remember the bad
feelings are how we built those
relationships. And me reacting to that,
saying, you know, to my colleagues that
I already knew this, they usually
eventually learn the the idea that maybe
they don't have to correct every single
typo, especially when we're using tools
like this.
So the Monday version uh that fails
after five steps uh and the Thursday uh
version passes all of them.
So again here so we have this magic
wave right and we have the Thursday
version because we would obviously want
to see first that uh that uh after the
fixes uh things work. I didn't even
actually try this uh when I was
preparing the demo. That's how much I
nowadays trust that that these kind of
basic things AI is is usually able to do
for us.
So, uh it runs it on the background and
and tells me I had a one uh test with uh
well 17 properties. it doesn't calculate
the properties here and and that runs uh
whereas as the thing for Monday uh
that's the other implementation
uh fails on step uh uh expectation on a
on a particular property. So I could
just take these very same properties
almost automatically into into whatever
format of test automation I already had.
So this was not 17 but 13 properties
uh that it it put there and I just
decided that for demo purposes I'm not
going to be struggling with the rest of
them even though I have an idea that
asking in the right way I will get all
of them as part of of of some uh
playright kind of of scenarios. So uh
that's uh kind of where I concluded on
the on the demos then to get to
summarizing all of this experience. So
uh you should be testing uh with
properties. You should be testing with
automation. You should be exploring
while automation is is is is your tool.
This is very much manual thinking work.
The tools of AI and the code that's just
helping you you know do some of this
work and and you can turn it into actual
automation uh by putting it in a
pipeline where it gets run again and
again and again so that you don't have
to be the human as the loop that runs
the automation. That's not automation.
Human in the loop looking at results
mostly green that's what we want human
as the loop running automation it's not
automation as per current uh
understanding
uh the things that uh you need to kind
of understand uh behind choosing these
tools is is that if you choose bombardil
you will uh drive your browser uh uh
with a chrome developer protocol and the
only uh browser you're able to drive
with uh Bombadil's version of CDP is
Chrome. You can't run that on Firefox
because obviously Firefox doesn't have
Chrome developer protocol. So, so it is
single uh browser thing that you are now
testing. But then again, if you're
caring about business rules, maybe
that's still a smart move to do that.
uh the uh playright uh tool uh also uses
Chrome developer protocol but they have
gone around this browser limitation so
that they have added well they have
self-built a version of Safari which is
not actually called Safari it's called u
uh called uh web driver I'm sorry not
web driver but uh it's called u well
anyway there there's the the um the uh I
keep forgetting what it's called but
anyway there's a version of Safari
that is just the engine kind of like a
fake version of Safari, not the real
Safari. There's a fake version of of of
of
uh uh Firefox that is not really the
real Firefox, but it's made for testing
purposes. It's it's good enough so that
it's better than just Chrome, but it is
not the real browser. And if you need
the real browser, this same technique,
same idea of properties is also usable
with web driver by that runs real
specific versions of browsers. And and
you might know this as selenium, but uh
web driver by is just a protocol that
selenium has reference implementations
for. So uh whether it's Selenium or any
of the other tools in that family that
then has an impact on on on whether
you're able to cover different browsers.
So this is something that you should be
you know aware of and and and making
design decisions in your testing.
Uh I couldn't stop uh with my simple uh
oh I found four relevant problems I
thought I didn't even have. So I had to
try this on on a couple of more real
size applications. So I did the very
same steps on Prestoop which is a a a uh
online com e-commerce platform uh an
open source one. Uh I found hundreds of
real problems there. I did confirm
couple of them and now on my list of
things to do is uh talk to the people
who have created Prestoop and give them
fixes or at least talk to them about the
fixes that they might want to have
because uh when generating um the API
related properties against their admin
API, there's some pretty bad bugs that I
I ended up finding. So I now feel guilty
and and responsible and having to find
some time to go there. That worked like
a charm. really nice experience. Whereas
when I tried dynamics 365 financial uh
um finances and operations which is one
of the platform products that we use
that was awful experience and I
recognized that it's an awful experience
because the tool and the tool and the
system that I was testing they were in
conflict
and uh I already did talk yesterday uh
on on social media with the developer of
this tool and he's kind of like already
sending me messages saying please please
please talk to us a little bit. Give us
the scenario and we'll fix the tool. So
apparently uh just saying out loud uh
that uh you weren't able to test
something like this, the developer comes
to you and offers to fix it. So I I
inherited some more work for myself uh
uh from these uh work that I can of
course also opt out of. So my take on
this is is that uh there's things that
you might you know uh take from this
into your day-to-day. the idea of
properties. I hope that you would start
thinking in terms of properties and
maybe identifying those uh for you. But
there's also so much more uh that would
need to uh need to happen. Uh I won't
try to put in this 30 minute talk today
some of the other things that I've been
uh you know very much geeking on in the
last couple of weeks. So these are talks
that you know whenever I find time I
might actually uh deliver. But this is
also to show you that that getting
excited about new things and just
showing what you were able to do with
those things with AI, it's actually not
that complicated.
This wasn't a huge effort for me. It was
a a series of a few prompts. So again,
kind of going back uh to this this
listing here, I'll show the agenda this
way. Those are the specific prompts that
I needed to do to implement this demo.
uh and and and show up uh here uh as
soon as I had an idea that this is
something that that connects with
something that I I want to do. And the
words that I use here, LLMs for
note-taking and summarizing, uh LLM
wikis, caveman, all of those would need
someone to show them. And this is kind
of like an opening also for the next
year of our community. We don't need a
leader to step up and and volunteer to
share. Maybe you should be the one going
caveman so that I don't have to.
That's what I wanted to share today. So,
we have a few minutes I think for
questions.
