---
title: "Fighting against Automation isn't doing anyone a favor"
publication: "Around the World with 80 Software Testers (book)"
date: 2020-04
url: https://leanpub.com/AroundTheWorldWith80SoftwareTesters
source_retrieved: https://leanpub.com/AroundTheWorldWith80SoftwareTesters
kind: book chapter
language: en
---

# Fighting against Automation isn't doing anyone a favor

*Around the World with 80 Software Testers (book) — 2020-04*

Source: <https://leanpub.com/AroundTheWorldWith80SoftwareTesters>

> Retrieval note: text extracted from the author's PDF of the article (the original publication is offline or paywalled); layout is approximate.

---

Chapter for #80SoftwareTesters

Fighting Against Automation Isn’t Doing Anyone a Favor

By Maaret Pyhäjärvi (Finland)

With 25 happy testing years behind me, I can’t help but to reflect on what I learned about testing
after spending two years as an engineering manager. I learned that while a tester work never
drove me to boring and stupid clicking work, the manager work surely did - there was little space
of variation you can introduce to approving people’s hour reports and still get the outcome the
people need.

Testing is about variation. Identifying things that could be different, and intentionally making
them different. Keeping your eyes open when you do so, and when keeping at it, enjoying the
gift of serendipity - lucky accident that brings you the observation of things that were broken
even you did not anticipate! Variation shows as fast forwarding a year of production, all the
different kinds of uses and scenarios to the short timeframe you spend on testing. Users
stumble on bugs, testers simulate the masses to find bugs intentionally.

With the love towards spending time with the application, I would always find the reasons why I
did not have time to automate some of the testing I was doing. After all, I wasn’t repeating the
same things, and automation would force flows that are repeatable. For a long time, I did not
work on implementing automation, but I always had an opinion that it wasn’t perfect, it wouldn’t
do all the things we aspired for it to do.

Being Vocal Against is Time Away from Supporting

Given a chance, I would look at metrics showing how little proper testing automation was doing.
I would look at how bugs were found either without automation or while creating automation
(and testing manually because that is what we need to do to create automation). I would look at
people spending weeks and months in creating tests that did little to no testing.

Being vocal, I would find myself explaining how it is not all we hope it would be, and how it
never would be all that. I would spend significant time ensuring that people were aware that 100
% automation was not a worthwhile goal.

Surely, automation did not flourish. I wasn’t helping it, I was hindering it. I was eating away
motivation from people given the task of figuring out automation. And I was depriving those
people away from the ideas of what and how we could test using programming that was beyond
repeating automatically the same tests we had run with humans attending them before.
Even though I, an exploratory tester, knew the idea of opportunity cost - time used on something
is time away from something else - I could not stop myself from investing in the negative,
warning agenda. And I was not alone with this choice of how I invested my time.

The Best Thing That Happened Was That I Left (and Returned Later)

Where I work now, we have a really great combination of attended and unattended testing. Just
as we are releasing, we run our test automation and watch one run with human eyes while
automation is ongoing, to spot things that require human elements. We can always stop the
execution, and move to having manual execution continue where the automation left off.
Automation ticks off 200 000 tests a day, inviting us to explore if it fails and making space for
exploring things where we don’t think automation serves us best. Automation covers multiple
environments and allows a human to only check the details where it is failing and inviting
exploration.

We’re very happy with the way we do exploratory testing, using automation as the way of
extending our reach by being a platform of fast-forwarding us to where we need to get, handling
masses that would be hard for people without preprocessing, and doing both unattended and
attended testing. It enables us to make hundreds of changes fairly quickly, and deliver those
changes to production where they improve the experience of use for some millions of our
customers. It’s not that we couldn’t analyse and target testing that was completely manual, It is
that we can use that energy on other things when automation does some of the harvesting for
us.

With what we have now that I have helped build in the last 3,5 years through enabling a team
approach to all this, we would not have if I still used my time against automation. The way I look
at it, one of the best things that happened to this organization is when I left it earlier in my career
while I was still using a cautionary tone, and allowed for people to freely discover the foundation
we built on when I returned for my second round in the company.

Moving to Automation, the Whole Team Way

Allowing automation to exist does not mean everyone does automation the same way. The
whole team, together does the testing that needs doing. There is still room for identifying risks,
creating ideas on how those risks could be targeted in testing, finding new formulas to test over
following existing ones. There’s still work that requires attending an aspect of testing, even if the
execution part of it was automated. And with software systems as our external imagination, we
need time on the software to think how, beyond simple bugs, we can make our software better.

Automation has been one part of our transition, another one has been our attitude to bugs. We
don’t prioritize them, we just fix and forget them. Documenting in automation allows for
forgetting. Again opportunity cost is at play: our users will be happier with a fix (or a decision not
to fix), than us using the same amount of time on deciding on the right time for fixing.
Your move?

Perhaps you are an automation specialist. Grow better at connecting the programming you do
for testing purposes into testing purposes. While automating, you are also exploring. If you allow
yourself to work from a scripted mindset, you miss some of the power you have at your
fingertips with programming for testing purposes. Work closely with developers, because unit
tests can cover ground you try to cover with your automation. See the whole picture, not just
what you got assigned.

Perhaps you are a manual exploratory tester. Start reading code and recognizing patterns
around how it changes, and how that is related to what you are testing. Don’t deny yourself the
understanding of what has changed. Start reading automation logs. Start reading test case
names in automation. And most of all, start speaking up about what you’d like to test and how
your programming colleagues could benefit from what you know about the application we are
testing and the risks of the domain.

Perhaps you are a developer. Spend time with your application and your users' problems, and
care. Remember you are not alone. The other developers work with you. The testers work with
you. There is always a second pair of eyes available so that you don’t need to be left alone with
big responsibility. The business opportunity of having people specializing in testing is that they’d
blame the developer and point out mistakes. It is that together we can condense schedules and
achieve a higher level of quality than you could alone.

Back to My Purposes in a Team

For the last few years, I have been realizing that personally as a tester, I serve my team in many
different ways.

I am a catalyst that enables things that wouldn’t happen without my presence. For the last two
jobs, I have found myself working with developers who can test, and sometimes what they
needed for that was to look at me and say “You’d want me to click here”.

I am working against inertia and entropy. Inertia is the idea that we don’t need to change, but
just keep ticking away as the process defines. Entropy is the idea that without continuous effort,
things turn messy. Neither one works in favor of great software.

I raise others, by in addition to reporting bugs, I report achievements. If there’s something I am
proud of, it is the new positions and raises people around me have received for this work.

But above all, I am a tester. I take joy in finding bugs, finding information, and getting us
together to make good use of that information. For great products, and for great team
productivity.
