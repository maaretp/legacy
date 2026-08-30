---
title: "Use of Rapid Reporter in Exploratory Testing"
publication: "Testing Circus"
date: 2014-04
url: https://drive.google.com/open?id=0B07e3JZGe_haMjZPUXQwLThlbnM
source_retrieved: https://drive.google.com/open?id=0B07e3JZGe_haMjZPUXQwLThlbnM
kind: magazine article
language: en
---

# Use of Rapid Reporter in Exploratory Testing

*Testing Circus — 2014-04*

Source: <https://drive.google.com/open?id=0B07e3JZGe_haMjZPUXQwLThlbnM>

> Retrieval note: text extracted from the author's PDF of the article (the Google Drive copy needs sign-in); layout is approximate.

---

Experience report on taking notes and reporting

       Use of Rapid
       Reporter in
       Exploratory                                                                - Maaret Pyhäjärvi

         Testing
During my years as tester, I've been fortunate to work       so instead of me asking to trust me to do things
with organizations that value the contribution of smart      differently, I asked if it was ok to document the testing I
individuals and allow for the thinking space intellectual    did in detail but a different style than test cases - using
work requires. I would call that Exploratory Testing,        a notetaking tool Rapid Reporter, created by Shmuel
although we tend to talk of just Testing. I've been          Gershon (http://testing.gershon.info/reporter/).
allowed to experiment and try out approaches and tools
that would help me and my colleagues to keep the
complexities of testing under control, without a lot of      I introduced the tools with a demo and a picture
external requirements on what and how to document.           explaining the central concepts (picture 1 - next page) of
Most of the documentation pressures, for me, rise from       what I was about to do to get a go ahead to not do things
within, from my need to recall things that happened,         as before.
and to make sense of the overall picture of what I've
learned in many small steps, allowing others to get          Rapid Reporter is a small standalone tool to create
some of the relevant information faster.                     tagged notes with timestamps. The tool itself sits on top
                                                             of my open applications, being readily available as I
Two years ago, I joined a new project as the only tester     proceed with testing a web application in a Windows
in a team of developers. The team had worked hard on         environment. It allows me to make notes of my latest
getting their testing to take form with the lead of the      information, classify it with predefined tags, and later
project manager. As there was no specialized tester,         go through whatever notes I created, in case I would like
they had organized to create test cases for the              to take the most recent information into some other
developers' ideas, and asked another developer to help       form of documentation. My notes get saved as per
out in executing those tests. The experience was that        session csv-files and I place them in a folder structure
without the written test cases, testing would not            outlining the areas of the application I'm testing.
happen. The fear and distrust was clearly a driving force,

                                                 www.TestingCircus.com                  April 2014            - 27 -
Picture 1. Central concepts around my notetaking

I have a set of tags I use to classify my notes with Rapid Reporter with a predefined meaning. For my set of tags to
use, I've extended Rapid Reporter giving it my set of tags on a command line. Some tags I use for calculating use of
my time (Test/Bug/Setup/OffCharter). Some tags I use to count amount of results from Testing
(Bug/Question/NextTime). Some tags are there to make sense for assessing coverage (Environment/Data). And
some just so that I would remember the bits I really consider relevant to use later on (Note).

With the tags and their meanings to how I use the tool, it makes sense to use a Rapid Reporter csv-scanning tool
SBTM created by Ru Cindrea, to automatically create reports in Excel that show the division of time realized allowing
me to explain if my testing is progressing and sums up the amount of results tags.

I also outlined, that I would collect the NextTime -ideas on a backlog (which we kept in Jira), to show how the
amount of work remaining is developing as testing proceeds. And that if there was other useful documentation (e.g.
specifications I would write learning by testing as the project did not have such), I would collect that information in
our wiki, not as test cases but more as things to enhance someone else trying to learn the areas I was testing.

I progressed with testing using Rapid Reporter, and doing also a lot of OffCharter work to learn the application I was
new to. I would read a bunch of Jira issues with newer information overwriting the older to learn what the
application was supposed to do as there was no up-to-date specification. I would read the existing test cases to
learn that it's possible to have 3 tiny pieces of relevant information in 39 pages of test cases. And I would use the
software to see how it works, and log bugs.

                                                 www.TestingCircus.com                 April 2014            - 28 -
As days passed and testing continued, taking notes of time allocation was relevant in particular. Whenever I use
tags Test, Bug, Setup and OffCharter, I intend not only to write a note that is related to the tag, but also mark down
the time of when I did that. This allows me to see how long I was working between the last Test-tag and another tag
that has impact on time calculations. With the information available, I could mine out for a report the time I used
for Test (I'm actually covering the software and making progress), Bug (I found something that I'm investigating),
Setup (I'm getting ready to do testing) and OffCharter (I got interrupted with something other than I was planning
to do in the session). Picture 2 provides an example of the automatically generated information I could have
available from Rapid Reporter csv-files.

Picture 2. Example report from a fake project created automatically from Rapid Reporter csv-files

The tool helped me make it visible that with the amount of bugs I was logging from the testing, the time used went
in a significant portion to isolating and logging the issues, and I wasn't making much progress on covering features
of the application, as I needed to come back to everything after it had been fixed. Then again, just the amounts of
bugs in Jira I would log were a surprise and created similar visibility as the problems had not been seen or isolated
with the testing done before my time with the organization.

As time passed, I got better at writing down things I would be interested in for the future. I would not write down
everything I do while testing, but always consider the future value of what I would write. Does it help me
understand what I've covered? Does it help me recall what I've learned so that I can build on that? Categorizing the
notes for coverage areas (folders for the csv-files to reside on) also helped me create a map of how to go find the
information.

                                                www.TestingCircus.com                 April 2014            - 29 -
I also started paying attention to where the effort and     not isolate the bug right in that session but use different
my focus went while using the tool. While this style of     sessions on isolating the bug to be able to progress with
documenting was not particularly painful, it created a      my original idea of what I would like to know after the
structure that did not necessarily allow me the full        session. Often I learned, however, that my brief note was
freedom that trust in my focus and skills gives. A month    not enough to recall what had happened, and finding
with Rapid Reporter ended up being a proof of concept       the steps to reproduce would have been easier if I did
of my trustworthiness, and as I suggested to not use        not postpone it. The notes helped me learn the types of
that anymore based on opportunity cost (time I could        things where I would log the bug immediately and the
use on producing more value than on the notes that          types I could postpone.
make me trustworthy), I no longer needed to address         -- While the session is often suggested to be a focused
the questions of not doing testing without marking test     timeframe, I found it useful to consider a day of work
cases done.                                                 focused enough for our purposes. My sessions were
                                                            significantly different in sizes, ranging from the full day
                                                            (skipped lunch and breaks for the fun of testing) to
I found the tool very valuable as an option to making       times between the breaks or meetings. I learned that my
notes. While it's a great and useful tool, there were       typical day would have 2-3 1,5-hour focused sessions and
many things I learned to tweak on how I would use it so     a lot of asking around to give and get information that
that the tool would serve the purposes I had in mind -      was relevant for the testing.
including reporting - and not get in the way of how I       -- I used the OffCharter - tag a lot to mark time on
think while I test.                                         testing something that I originally did not think would
Some advice I have marked down for my future self on        be the theme of the day. Towards the end of
this that could be useful for others taking the tool into   experimenting with the notes, I became less disciplined
use:                                                        with my time keeping, as I felt it took quite much
-- I found it useful to fine-tune my message on the time    energy.
calculation tag types with Note-tagged things following     -- One set of notes is saved on one csv-file, and one
the original Test/Bug/Setup/OffCharter - tag. For           csv-file can be placed in one folder representing an area
example, when I was working to understand a problem,        of coverage. Whenever moving from a coverage area to
I often marked down a quick Bug-tagged note to get the      another, I had the habit of starting a new session just for
time to be calculated under Bugs, and I might work to       coverage and time tracking to make sense.
isolate the problem for a long time after that, either      -- I found it easier to assess what I had covered than to
using Note-tagged notes or more often, writing steps to     plan what I would cover. The time allocation isn't precise
repro in Jira.                                              but it did not need to be, it gave direction on what areas
-- You can take screen shots with the tool. When you use    had had the time allocation they would deserve as per
Shift-button together with clicking the camera icon, you    their complexity. What I looked at and pointed out
can edit and mark your notes directly on the picture. I     mostly is that if no time on an area is used, it does not
found it useful to take a screen short right after a Bug-   mean it works since there are no known issues, but that
tagged note, because the screenshot shows your most         if there are issues, we just don't know of them
recent note and it made it easier to make sense of my       -- The folder structure allowed with the scanning tool I
notes and pictures later on this way.                       used had one level of scanning depth, so no subfolders
-- If a brief Bug-tagged note helps you remember to         allowed. When I tested the full product, my folders were
come back to isolate the bug later, I found it useful to    areas of the product. When I tested one area, I had a

                                                www.TestingCircus.com                 April 2014              - 30 -
separate folder structure with division to folders that      lowers the quality of the work resulting from running
made sense in that area.                                     them.
-- I also had sessions that were not about any of the
coverage areas I had identified but touched all around       Instead of making notes of the details of what we do
the areas. Those I saved on the root folder I would create   while testing, we tend to focus more on discussing what
reports from.                                                more is there to test - what ideas we haven't covered.
                                                             And making a map of the areas available that help in
                                                             recalling what there is to remember on a higher level.
With nearly two years in the company, I work closer to       Rapid Reporter - or any other note taking tools for
the developers than the idea was at time of me joining.      testing that focus on categorizing things as you learn
My team knows I love my testing work, and they see a         them - are great and useful tools. But the core of it is the
part of my results in the bugs they get to fix. The          thinking tester. Use the tools in smart fashion.
concerns of sharing information and helping others
know what happens in testing will not be resolved in
writing more documentation of any form that people           The tool was just a cherry on the ice cream - just what I
don't read, so instead we discuss more of what and why       needed to make things flow. But the basis of using the
I do, allowing smart individuals to deduct the details.      tool comes from the lessons over the years from James
                                                             and Jon Bach. I would suggest reading up on session-
We've learned not to create 39 pages of test                 based test management (SBTM) for ideas of one
documentation with 3 mention-worthy details, and             approach to manage exploratory testing where Rapid
instead discuss around mindmaps and checklists. I still      Reporter fits in nicely.
occasionally remind my team members that while the           More recently, I've enjoyed using a mobile application
39 pages had only 3 things worth the paper, there was        adaptation of the Rapid Reporter ideas I describe here
still 98 features we identified on that area alone,          and you might want to check iTester for iOS - especially
together, that are now listed in a checklist. Running the    if Siri (the voice recognition technology) actually hears
test cases was a cause for missing all the bugs I have       you correctly and allows you to skip much of the writing
helped to find since then, that we can find when we          by talking.
don't box testing with appearance of test cases that just

Maaret Pyhäjärvi works for Granlund Oy, a Finnish civil engineering company, as testing specialist
working with two software product teams since 04/2012. She has worked with software and system
testing for 17 years in various roles mixing management and hands-on testing work with researching,
teaching and consulting. She's a frequent speaker at conferences and helps build the software and
testing communities further by volunteering in Agile Finland Executive Committee and Finnish Associa-
tion for Software Testing steering group.

                                                 www.TestingCircus.com                  April 2014              - 31 -
