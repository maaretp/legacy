---
title: "Contemporary Exploratory Testing"
publication: "testproject.io blog"
date: 2021-04-20
url: https://blog.testproject.io/2021/04/20/contemporary-exploratory-testing/
source_retrieved: https://web.archive.org/web/20210420150209/https://blog.testproject.io/2021/04/20/contemporary-exploratory-testing/
kind: article
language: en
---

# Contemporary Exploratory Testing

*testproject.io blog — 2021-04-20*

Source: <https://blog.testproject.io/2021/04/20/contemporary-exploratory-testing/>

> Retrieval note: retrieved via the Wayback Machine (original site is gone).

---
As the month changed, we had just completed a major release. I had been working on it for the last year, and it had started before my time in the organization. 12 subsystems, end to end testing responsibility, and being the sole person in the entire project organization who has tested on every single one of those subsystems in efforts to orchestrate internal teams and external components into great testing. I sighed in relief and anticipation: let the major release of today be the last major release of my life – here’s hoping for continuous releases everywhere! 🎉

The world around testing has changed. Saying it does not change testing is like saying that a pool and a bathtub are the same since they are both containers of water. Yet, they enable completely different purposes and the same applies to testing . Continuous delivery is a game-changer, and my last piece is now in a new game.

## Exploratory Testing Revisited

Exploratory testing is an approach (not a technique) coined in 1984 by Cem Kaner to describe skilled, multidisciplinary testing focused on results, observed live in companies in Silicon Valley. In a world turning testing into test cases, it emphasized keeping test design and test execution together instead of separating them in the way work is organized. We intertwine design and execution and learn between tests in a way that changes the next test we perform for more impactful testing. We learn about the application, we learn about testing, and we learn about our ways of doing testing. This learning requires agency, a human connection between the two tasks with the power of making decisions in the moment over following a preconceived plan.

While some folks are keen on deprecating the word ‘exploratory testing’ and replacing it with just ‘testing’, others seek on minimizing it to a technique applied on top of everything else. I invite us to revisit the original roots, see it in the context of continuous delivery and DevOps, and find out what contemporary exploratory testing has to offer in projects like the one I just completed.

## Doing Contemporary Exploratory Testing

In the last weeks leading up to the major release, we were touching upon the last necessary features. Even if we did not release the product – with hardware and software dimensions – we built it incrementally. One of the last features was related to automating connections, a feature very tricky to test. We were lucky to have contemporary exploratory testing in place.

A visible activity was running exploratory test automation, a collection of to-the-purpose scripts that repeated connections, enabling us to inject a variety of variables that could be different. Every morning the tester would have the collected results of the previous night available, analyze them pulling in developers to speculate on observations and variables to further try, to get the next set of concerns over to the next batch. Within weeks, they simulated variations in scale and fixed problems.

Existing test automation for other features would invite us in to explore changes. We would spend time on having conversations on expectations, allowing the software to be our external imagination and a source of grounding into empirical evidence. We’d collect people together from various teams, to do ensemble exploratory testing – all of us working on a single computer and a shared testing task. Some of the best exploratory testing taking place was done by the developers, in response to symptoms requiring deeper understanding to find a repeating pattern enabling fixing.

When we do exploratory testing, we center learning. The manual – or humanual like Erica Chestnut says – activities and the automated activities intertwine together so we no longer have conversations on separation of the two. Just like design and execution, the constraints we apply on our design and execution are best left unseparated. Creating automation is a people process. We can’t explore well without automating. We can’t automate well without exploring. Learning, through agency of the doer, is critical for optimizing for impactful results.

We extend agency from a person making decisions about design and execution of tests to making these decisions about use of automation. When we enter exploratory testing with programming skills, test automation becomes a way of documenting our testing and extending our reach, forcing us to consider detail and calling our attention to details while we are otherwise occupied. We need to learn between the tests in a way that changes the next test we perform.

## Clearing up the confusion

Reflecting the examples I have given on contemporary exploratory testing, there is a major shift I’m introducing with returning to the roots of exploratory testing as a skilled, multidisciplinary approach to testing. We can no longer think of exploratory testing as a technique that is sprinkled on top of other testing that leads predominantly to automation. Contemporary exploratory testing drives our daily use, creation, maintenance and improvement of automation.

The core question remains. After every test, you ask yourself: what did I learn and what changes because of it? And instead of continuing on your set path, you carve yourself a path where you do the best testing you can, improve the testing you do next, and improve yourself learning continuously. Learning wins over everything and a 1% improvement every day – 4 minutes of 8 hour working day – would improve your results to 37.8 fold over a year.

## Managing Contemporary Exploratory Testing

I do my fair share of hands-on contemporary exploratory testing. But to orchestrate everyone’s work, I do something on top that the others don’t. I split my time into all the subsystems, hands-on. I protect my agency as a tester, and I protect everyone’s agency to enable their best results.

To manage, I don’t do session-based test management. I protect agency. I make commitments on enabling learning through not separating activities that belong together. I design and facilitate overlapping team responsibilities, and ensure we apply social software testing approaches that maintain the agency but enable larger groups contributing.

For those who can’t test, I teach testing. For those who don’t understand domain, I introduce experiences that enable learning the domain. For those who can’t automate, I use the power of yet. For those who can’t communicate, I create social spaces where communication happens, removing myself as the person in the middle. I enable agency in people who think they have lost it.

The skills the future of the testing craft requires have already shifted. Good testing includes exploring with automation as well as without, intertwined. The social aspect of work has never been more important. They say the future is here but it is not evenly divided, and I invite you all to figure out the future. I hope for one where we no longer argue over manual vs. automated, and start figuring out what testing in companies can look like when we are actively learning.
