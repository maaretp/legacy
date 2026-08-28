---
title: "Why should a tester care for unit testing?"
date: 2015-03-27
updated: 2017-07-22
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2015/03/why-should-tester-care-for-unit-testing.html
---

# Why should a tester care for unit testing?

*Published 2015-03-27, updated 2017-07-22*  
*Source: <https://visible-quality.blogspot.com/2015/03/why-should-tester-care-for-unit-testing.html>*

---

I run a workshop session together with Ru Cindrea today at #TestBash on TDD with Lego Robots. It's a session that from a facilitators point of view turns out to be very different in an agile (developer-majority) conference than in a test conference. Right after the session, one of the participants came to chat about things and asked a question:  
  
Why would a tester care for unit testing? Isn't unit testing really developer's business?  
  
There's a few reasons I see why I care, and I thought sharing those might be useful for some other testers too.  Yes, test-driven development or unit testing is typically something developers do - an integral part of development. Yes, test-driven development is more about design than about testing. But there's still great number of things make it worthwhile for testers to get their basic understanding on test-driven development in some condition.  
  
**Reason 1: In software development, it's about all pieces together building a full view**  
  
If as a tester, I'm totally unaware of what my team's developers can do and have done with unit tests, I will not be able to adjust my focus based on that information. I will miss the information I can get now, knowing at least a little of what their unit tests include through reading them. And without that information, I will do different decisions on where to allocate my limited time.  
  
While unit tests and system tests serve very different purposes, they both co-exist (with a lot of other mechanisms) in developing software. We tend to see different aspects in small scale than when looking at user flows.  
  
**Reason 2: Without unit tests, everyone suffers so perhaps I could help**  
  
As a tester, I've noticed that in projects where developers don't do unit tests, two things happen: 1) features flow through development very slowly, as developers analyse and test their changes, and 2) testing on system level slows down as simple problems are found. The problems are most often features that vanish without an intention, as the code did not hint about the feature. It's hard, if not impossible to remember later on all the intentions we have built into our code.  
  
To help with unit-testlessness, knowing what they are about helps me help the team in getting them done. Sometimes I help by talking to managers on how important it is to organise time for developers to do unit testing. Sometimes I help by suggesting what the unit tests could include that they are currently missing. Knowing about unit tests help me talk to the developers about things I'd like to see tested with code, and together we can figure out if there's a way to monitor my concerns on the level of unit tests.  
  
Some developers find unit testing really hard. Without a gentle nudge, they won't spend the time to learn to overcome the difficulties.  
  
If I declare unit tests a developer concern only, I miss a lot of collaboration opportunities.  
  
**Reason 3: Change and readability are things that I find relevant**  
  
The software I work on has the habit of changing a lot. There's continuity with the work we're doing, and a never-ending queue of more work when the previous is done. Change is something to embrace. But when changes create a tone in the team that suggests that tests are on the way of change, it's good to know how to respond. I've been through this type of discussion numerous times: when every change invalidates all the tests, it seems like a waste of time to create new tests to be soon thrown away.  
  
The tests are not supposed to all break on a focused change. If that is the case, there's something wrong with the tests. And a simple observation that the team seems to be throwing away tests can be a helpful discussion starter.  
  
I can also help with readability of the test. I don't need to understand every detail to see if the names of the unit tests make some sense, and allow me, especially with support from a developer in a team, to understand what the tests watch out for. I can suggest better names for things, or go even further: work out how to do good unit tests and lead by example, changing what was there to something that is more readable when we get back to changing this code a year later.  
  
**Reason 4: Test-driven development is my best hope for relevant unit-level test automation**  
  
The more I look into unit testing and its dynamics, the more it appears that teams that learn to do test-driven development over after-development unit testing, get their tests to stick better. While it appears to be painful at first to learn (so many developers tell me they hate TDD as it just won't fit their ways of developing) when learned, it produces unit tests with a regular pattern.  
  
There's so many obstacles for adding the tests later on when the code was not designed keeping testing of it in mind. When you just got the thing to work, changing (and potentially breaking) for adding tests creates an incentive not to add tests that were too hard. And the level of what there is stays low.  
  
**Reason 5: Collaboration (pairing, mobbing) changes responsibilities**  
  
When everyone in the team pairs with other team members, or the whole team does mob programming together, the idea of who does what blends into a new mix. Testers are expected to participate in these activities. And all of a sudden, the discussion through defining the driving unit test on what a clear api call would look like are not as far-fetched as they were before.
