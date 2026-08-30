---
title: "Intersection of Exploratory Testing and Test Automation"
publication: "Quality Matters"
date: 2020
url: https://drive.google.com/open?id=1GzIUGBViMB2Kjq6tUOCSRPHpY95IeA9t
source_retrieved: https://drive.google.com/open?id=1GzIUGBViMB2Kjq6tUOCSRPHpY95IeA9t
kind: magazine article
language: en
---

# Intersection of Exploratory Testing and Test Automation

*Quality Matters — 2020*

Source: <https://drive.google.com/open?id=1GzIUGBViMB2Kjq6tUOCSRPHpY95IeA9t>

> Retrieval note: text extracted from the Google Drive PDF.

---
Intersection of Exploratory Testing and Test Automation

The software world keeps splitting testers into manual and automation testers. Thinking this way both misses the mark but can also negatively impact the way you organize your testing. We are at an intersection of Exploratory Testing and Test Automation, and need to understand that the road forward isn’t one or the other, but that the two are the same.

An Example of Exploratory Testing

Exploratory testing is a way of testing where we rely on learning while we test.  We learn about threats to quality (turning risks into facts), about the domain (why such software exists) and about the next acts of testing. We can do exploratory testing on something we’ve never seen before, and we can continue our exploratory testing where we last left off, considering all the relevant changes since we last tested.

For a new feature, in my current place of work I seem to go with a starting recipe of first seeing it work – allowing the feature to act as my external imagination as next acts of testing start bubbling up – and seeing it work with a code script.

The code script gives me many benefits for my exploration.

Documentation. It leaves a note of what is the basic positive flow I identified.

Environment coverage. It runs in a test automation system (TA) over a selection of Windows Workstation and Server environments that I now can look at while the script runs them, or just look at the test results from logs.

Timing issue coverage. Running over the next hours automatically, I get to see if the code script runs reliably and rely on tools alerting me if the new code script brings out crash dumps – a common type of mistake for this particular technology.

Access to further exploration. Telling the script to add a thousand things instead of the one is a minor addition. Connecting to the virtual machine of interest where I want to look at how a more advanced scenario than just seeing it work turns out after the simple thing is done.

If I want, I can keep the script I created and over time it starts to serve as a regression test. At first it adds a lot of things that have never been tested before, far beyond regression.

If I want, I can remove the code script, because code is disposable. I can build code scripts knowing that they are created as disposable automation.

In the end, I will know having tried a hundred things, even if I left behind that one script.  We probably have fixed a number of issues, and improved the unit tests.

But… You Described Test Automation?

Over my 24 years of tester career, I have come to appreciate that exploratory testing includes use of tools. I would be a fool trying to test in an attended fashion something where unattended gives me more data I consider useful and more reach with different choices of where I use my time.

My colleagues hired as Developers responsible for test automation may find themselves doing almost exactly what I do as an exploratory tester. The difference, if there is any, comes with what we consider most important.

As an exploratory tester, I would focus first on new information. If automation gives me new information, it’s in.

As a test automation specialist, I would focus first on capturing tests as code scripts, trusting the regression aspect alone makes my work worthwhile.

Both are right. It is not one or the other, but both. Exploratory testing is not ‘manual’ and Test Automation isn’t ‘automatic’ regression only.  People and code are involved in both!

The Intersection

We arrive at the intersection of exploratory testing and test automation as we have work in our teams that one person alone cannot do, and we all bring unique skill combinations to work. We have different years of experience, and different strengths.

Our industry grows in size, doubling every five years. That means half of us, should we be equally divided, have less than 5 years of industry. Focusing learning on some skills first may make sense but the cycling between building both exploratory and automation skills is more like a quarter than a decade.

In my 24 years, I have had the time to look at both and I will always be primarily an exploratory tester – automation will sit in that frame. For people with less years of experience, working together – collaborating closely – will bring results.

We come to an intersection where testing, whether we call it automated testing or exploratory testing, they are same if not similar when done well. To do well, approaching it from both roads is necessary. The exploratory mindset brings in test design and coverage. The automated mindset brings in continuous testing and expandability.

Existing automation allows for exploration reach.

Creating automation forces exploration of details.

Failing automation is an invitation to explore.

Branding “exploratory testing” and “automated testing” as mutually exclusive is the most impressive act of shooting oneself on the foot I have seen in any part of tech profession throughout my career and that is saying A LOT. –Noah Sussman, 9.6.2019 on Twitter.

Use either word, and recognize that they mutually encompass one another to be successful.

For you future success, what matters is learning. Learn ways that make the work you do more impactful.

If you find a way of making yourself 1% better every day of the year, you are 37.8 times better in a year. Learning on learning pays dividends.

And while you are at it, remember to have fun and never be bored. Testing is an awesome career. We are finding relevant information and building systems that help sustain our ability to deliver value for the customers. In this interesting work we get to do it with other smart people.

About the author

Maaret Pyhäjärvi is an exploratory tester extraordinaire with a day-job at F-Secure as Engineering Manager. She is a tester, (polyglot) programmer, speaker, author, conference designer and a community facilitator.  She is Most Influential Agile Testing Professional Person 2016 and Top-100 Most Influential in ICT in Finland 2019. She tweets as @maaretp.
