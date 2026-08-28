---
title: "Evolving scoring criteria for To Do App for recruiting"
date: 2025-02-08
updated: 2025-02-09
theme: career-and-recruiting
labels: []
source: https://visible-quality.blogspot.com/2025/02/evolving-scoring-criteria-for-to-do-app.html
---

# Evolving scoring criteria for To Do App for recruiting

*Published 2025-02-08, updated 2025-02-09*  
*Source: <https://visible-quality.blogspot.com/2025/02/evolving-scoring-criteria-for-to-do-app.html>*

---

I have used various applications for assessing people's (exploratory) testing skills in recruiting. While it's already a high-stress scenario, I feel there needs to be a way to \*test something\* if that is the core of the job you'd get hired for. I may believe this because I too, was tested with a test of testing 28 years ago.

Back when I was tested, the application was two versions of Notepad, one the original English and the other a localized version with seeded bugs. My setting for doing the test then was one hour in front of a computer in a classroom, being observed. There were 8-12 of us in total for each scheduled session, we were all nervous, did not know each other and most likely never even introduced ourselves. We did our thing, reported discrepancies we identified as clearly as we could, and got a call back or not. I remember they did these tests in scale. The testing teams we had weren't small, and we were all total newbies.

This week I assigned To Do app as the thing to test. For newbies, I make it a take home assignment and recommend using under two hours. For experienced testers, I spend half an hour face to face out of the max two hours of interviewing time we allocate. The work of people is not back yet, but the work of me looking at the application myself got done.

The most recent form of this take home assignment is one where I give two implementations of To Do App, and explain they are what developers use to show off their best practice for applying front end frameworks.

1. Elm: <https://todomvc.com/examples/elm/>
2. Angular: <https://todolist.james.am/#/>

I ask for outputs:

- A clearly catalogued listing of identified issues you’d like to give as feedback to whoever authored the version
- Listing of features you recognize while you test
- Description of how you ended up doing the assignment
- (optional) example of test automation in language and framework of your choice

The previous post listed the issues I am aware of, and today I created a listing of scoring the homework.  In case you have your version, or would like to talk about mine. I am still hoping for the day when some of the people doing the assignment \*surprise me\* by reading about how to approach these exercises from my blog.

I can't expect complete newbies to get to all, but what worries me the most is that too many of seasoned testers don't even scratch the surface. We still expect testers to learn testing by testing, often without training or feedback.

#### To Do Application -Assessment Grid

ESSENTIAL INSIGHTS

Architecture: frontend only

Same spec for both implementations

Material online to reuse

Reading the room, clarifying assumptions

Optional is chance to show more

Presenting your work is not just description of doing

ESSENTIAL ACTIONS

Research: find the spec as it is online

Research: ask questions

Meta: explain what and why you do

Learning: showing something changed in knowledge while testing

Bias to action: balance explaining and results

Modeling function, data, environments

Recognizing tools of environment

Choosing a constraint to control perspective

Stopping criteria: time or coverage

Classifying and prioritizing

Clarity of reporting issues

Reporting per implementation and common for both

TL;DR - expect lazy readers

Using and explaining a heuristic

Awareness of classes of data (e.g. naughty strings)

Surprise me (e.g. screenshot to genAI)

RESULTS

Functional problems (e.g. off by one count, select all, tooltip)

Functional problem, browser dimension (e.g persistence, icon corruption)

Usability problems (e.g. light colors, lack of instructions)

Implementation problems (on console) e.g. messages in code and errors in console

Data-related problems: creating empty items

Data-related problems: trim whitespace

Data-related problems: special characters

Missing features (e.g. order items)

Typos

In-app consistency (e.g. always visible functionality that does not always work)

AUTOMATION

Working with selectors

Reading error messages

Scenario selection

Locators

Structure and naming

Describing choices

Readme for getting tests to run

MISTAKES THAT NEED EXPLAINING

Overfocus on locators while application is unknown and automation is not in play

Wanting to input SQL injection string

I ended up cleaning this all and making it available at GitHub: <https://github.com/exploratory-testing-academy/todoapp-solution>
