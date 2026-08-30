---
title: "Five Controversial Ideas to Increase Your Impact as a Tester"
publication: "Women Testers"
date: 2017-08
url: https://drive.google.com/file/d/0B07e3JZGe_haVmRfOUFDLWRMcVU/view?usp=sharing
source_retrieved: https://drive.google.com/file/d/0B07e3JZGe_haVmRfOUFDLWRMcVU/view?usp=sharing
kind: magazine article
language: en
---

# Five Controversial Ideas to Increase Your Impact as a Tester

*Women Testers — 2017-08*

Source: <https://drive.google.com/file/d/0B07e3JZGe_haVmRfOUFDLWRMcVU/view?usp=sharing>

> Retrieval note: text extracted from the author's PDF of the article (the Google Drive copy needs sign-in); layout is approximate.

---

Five Controversial
       Ideas to Increase
        Your Impact as a
             Tester                                                                     - Maaret Pyhäjärvi

Ever since I started my career in testing, there’s been a      for 6 months to an extent where I still have no electronic
mantra I believe in: you should work in a way that you         footprint of my existence in the company Jira as bug
are better tester by the next day. To feed the learning        reports I would have raised.
loop, I do work but also focus on introspecting how I          I still find just as many bugs as before. Now I just
test and how I think.                                          actively work on the idea of fix-and-forget. When I see a
As a tester, I provide information by thinking well, both      problem, I demo it to the developer. It does not take
around our ideas and our implementation of those               more than writing a report. Many times I get a fix while
ideas. I love hands-on time with software and over the         demoing. If I don’t get an immediate fix, I write a post-it
years I’ve grown convinced that the software, in varied        note on the wall. If they don’t get processed and we can
use scenarios, speaks to those who want to listen.             still make releases, they must not be that important.
The main type of information I’ve provided is bug              Except that with the increased collaboration, they turn
reports. I’ve lived on the great wisdom from the Kaner         important. Usually I don’t only get the bug fixed, I also
et al. book Lessons Learned in Software Testing: “A            get the insight from the bug into the unit tests to
tester who can’t report bugs well is like a refrigerator       continuously improve our most granular way of
light that‘s only on when the door is closed” and learned      providing feedback.
to find great bugs and to report them properly.                Controversial idea #2: When asked to test, refactor
In this article, I want to introduce five controversial        As a tester, I’m asked to test. I’m also asked to automate
ideas that I’ve used in the last five years to increase my     some of the testing. When there’s a lot of testing to do, it
personal impact as a tester. I offer them as my                seems clear that having some of that testing automated
experiences. “The value of another’s experience is to          would be useful. But again, I ended up with a different
give us hope, not tell us how or whether to proceed”.          approach.
–Peter Block in The Answer to How is Yes.
                                                               Working in a small team of 10 people as the only testing
Controversial idea #1: Stop Writing Bug Reports                specialist, I had no choice but to share the load of testing
Reporting bugs well has, for a long time, meant writing        work with my team. As automation was requested, it
good bug reports in tools like Jira. I used to take pride in   became a team task. The close collaboration with the
my ability to find and log bugs, to an extent that I’ve        developers revealed that while in the world of
bragged in various conference talks that for the first two     optimizing testing, automating might have been the
years at my previous job, my average bug find (and fix)        investment choice of the day, in the world of optimizing
number was 8 bugs per day, even on days when I was             our development, the choice to use the same amount of
not at office.                                                 time was refactoring. Instead of adding tests, we
I did a full turn in the last few years, actively avoiding     collaborated on cleaning up code. As our code became
logging any bugs to tools. I’ve done this at my new job        cleaner, it was easier to extend without introducing side

                                                       Women Testers                 July 2017              - 04 -
effects. The same side effects we were concerned about        was only working to provide information. If we released
while considering automation.                                 something that did not work, I wasn’t the one spending
It becomes natural to improve things in the scope of          late evenings or weekends panicking at the office. The
what we do ourselves – namely testing. However,               developers did that. Allowing them to learn by having
giving up on my budget for a non-testing activity, resulted   something small break in production was good. Too
in bringing down the numbers of problems I ever had to        much protection wasn’t. Developers care, deeply.
care for.                                                     So I started letting releases go to production without me
Controversial idea #3: Release Daily even Without             exploring them. As the releases were daily, I had plenty
Automation                                                    of opportunities to try different mixes of when I would
                                                              test with various developers.
Every single conference talk I listened to on DevOps and
Continuous Delivery emphasized the role of test               I learned that stating I wasn’t going to test encouraged
automation. We had little to none of that but we were         the developers to test if they had concerns or improve
struggling with the end-of-sprint testing activities. Even    how they communicated their wishes on where I could
with developers pitching in and us doing shared               be of assistance. I figured out that the testing I used to
exploratory testing sessions, it always felt rushed.          do before releasing, I could do with the daily releases
Negative emotions often hint at a need to try out             cadence just as well do after the feature was in
something different.                                          production. Removing my contribution or making my
                                                              contribution unreliable in availability improved the
We gave up sprints and moved to a Kanban board,               game for the developers.
limiting work in progress so that we’d have one item per
two developers ongoing. We stopped doing estimates,           It wasn’t just exploring as in using the product. It was
and started discussing how we could make each change          also exploring as in understanding what type of
smaller. And each small change we would test.                 monitoring could provide us information about the real
                                                              users use cases.
We programmed manually, with brains engaged. We
tested manually, with brains engaged. When the                With daily cadence of releases, the while in production
manual work was done, we merged to master and made            and before implementation became the same thing.
a release. With each change being                             There was always a new cycle starting.
small, the testing was easier to
direct. Should anything fail in
production for today’s release,
we would know exactly which
change was introduced in the last
day.
Controversial idea #4: Explore
while in Production
When Lisa Crispin and Janet
Gregory talk about agile testing
and emphasize whole team
ownership of quality and how
testers are not the gatekeepers, it
took me a while for that lesson to
sink in. I’ve worked in
organizations where the team is responsible for quality,      Controversial idea #5: One Computer for Group
but in the team, testers are more active and vocal when
making quality-related decisions.                             My absolute favorite of the controversial ideas is one
                                                              about Mob Programming or Mob Testing. Imagine a
At some point, I realized that I had neglected a piece of     group of 3-8 people, working together using only one
information: I did not put the bugs in the application; I     computer. The person in front of keyboard isn’t allowed

                                                     Women Testers                 July 2017              - 05 -
to think, or at least not to make decisions on what to do.     improvements that I would not have believed possible
The persons not on the keyboard need to use their              while rationalizing based on my previous experiences.
words to express ideas of intent of what should happen         Some experiments stick and grow, like these five grew
on the keyboard. As the ideas are vocalized, anyone in         on me. Some experiments fail and teach us things that
the group can pitch in and you get the best out of             did not quite work out. None of the ways of working we
everyone into the work you’re doing.                           have should be forever. Paraphrasing Alan Page on
It’s not one person working and others watching. It’s an       twitter: it’s a career suicide to keep doing the same
idea of sharing through doing together many of the             things we've always done, the same way.
things we’ve learned and take for granted, that others         For some of these things, you need other people to work
don’t even understand they could learn from us.                with you to do them. For others, you can just do things
I learned to program this way, through osmosis.                differently yourself, for a limited amount of time to see
Granted, I had a background in computer science but a          how things change.
dislike towards programming. The developers I worked           The best thing I ever learned: Ask for forgiveness, not
with learned to explore. The mysticism of how I could          permission. I would have lost out on many of the great
always get the program to crash and fail was no longer         improvements transforming not only the testing but
magical, but the skills, layer by layer, were transferrable.   product development as we know it if I did not just start
And as someone who learns more every day, there                doing it. It’s not the bugs I find, it’s the value (without
would always be another layer to peel.                         bugs) we manage to deliver for our users and
Some teams, like the teams at Hunter, do Mob                   customers.
Programming full work weeks. Other teams, like mine,           Alone, I can become more productive by learning. In a
do Mob Programming (or Testing) to learn through               team, I can become more generative, making us all
doing. In a group, hard problems get solved and easy           better together. Being generative is a whole different
problems get innovated on, and often automated away.           level of making an impact – as just a tester. But
Experimentation – Learn by trying things out                   remember: none of us is just anything. We make
                                                               ourselves into what we feel like being and there’s some
Each of these five ideas has been a thing where I’ve been      pretty amazing testers out there.
hesitant to try it out. For each, I’ve believed they are not
what is expected of me as a tester. For each, I’ve found

Maaret Pyhäjärvi is an empirical technologist, a tester and a non-programming programmer, a catalyst
for team improvement, and a speaker and an organizer. As software professional with a testing
emphasis, her work is coaching herself and others in breaking illusions with empirical feedback. She
works as “just a tester” in product companies, believing no one is just anything with daily focus on
stretching our skills. She speaks in international conferences to learn more through sharing, and her
themes revolve around exploratory testing mindset and skills applied throughout product
development. Maaret is a serial volunteer for different non-profits driving forward the state of software
development. She is the head organizer of European Testing Conference aiming to change the world of
conferences, in addition to teaching skilled testing as both testers and developers see it. She was
recently awarded as Most Influential Agile Testing Professional Person 2016. She blogs regularly at
http://visible-quality.blogspot.com

                                                      Women Testers                  July 2017              - 06 -
