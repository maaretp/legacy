---
title: "An Exploratory Tester's Zephyr"
date: 2020-07-29
theme: exploratory-testing
labels: []
source: https://visible-quality.blogspot.com/2020/07/an-exploratory-testers-zephyr.html
---

# An Exploratory Tester's Zephyr

*Published 2020-07-29*  
*Source: <https://visible-quality.blogspot.com/2020/07/an-exploratory-testers-zephyr.html>*

---

Zephyr, in case you did not know, is a Jira Test Management extension. I dislike Jira, and I dislike Zephyr. But what I like and don't like does not change (well, immediately) the whole organization, and I play within general bounds of organizational agreements. In this case, it means an agreement that tests are documented in Zephyr - for some definition of tests.

This post is about how I play within those bounds, enabling exploratory testing.

**What Zephyr Brings In**

Zephyr as a Jira plugin enables some very rudimentary test specific concepts:

- **Ticket reuse**. When the jira ticket is a test, it can be run many times, like for example for each build we test. Normal Jira tickets are more straightforward in their lifecycle.
- **Steps**. For some reason people still think tests have steps with expected values. If you don't know better, you might use these. DON'T.
- **Mapping tests to releases**. You can tell what test ticket connects with a particular Jira release. It shows the structure of how testing usually progresses in relation to changes.
- **Grouping**. You can group tests inside releases into test suites. You have many reasons you might want to group things. Zephyr calls mapping and grouping cycles.
- **Run-time checklists**. You can keep track of passes and fails, things in progress. You can do it either on level of a group of tests or on an individual test. You have a whole own view to making notes while testing on a particular test case, execution view. It seems to imagine all your test needs in one place: bug reporting, steps, notes.

**What I Bring In**

When I document my plans of testing, I create a few kinds of tests:

- [Explore] <write a one line summary here>  
  These tests can be for the whole application like "Gap analysis exploration - learn all the problems they don't yet know", or a particular purpose like "Release", or an area of particular interest like "Use for people with disabilities". If I can get away with it, I have only one test case titled "[Explore] Release" and I only write notes on it at time of making a release. What this assumes though is that release is something more continuously flowing rather than one final act in the end - agile as if we meant it.
- [Scenario] <write a one line summary here>  
  These tests are for very high level splitting of stakeholder perspectives I want to hold space for. They are almost like the ones I mark [Explore] expect that they all together try to summarize remembering the most important stakeholders and their perspective in the product lifecycle. These are in the system context, regardless of what my team thinks their component delivery responsibility has been limited to.
- [Feature] <write a one line summary here>  
  These tests I use when I have bad or non-existent documentation on what we promise the software will do. These tests all together try to summarize what features we have and try to get to remain, but as a high level checklist, not going into details of it. These are in the context of the system, but more towards the application my team is responsible for.

I use states of these tests to indicate scope ahead of me.

If a test is Open (just like a regular Jira ticket), it is something I know we expect to deliver by a major milestone like a marketing release all the little releases work towards, but I have not seen a version in action we could consider for the major milestone scope. It reminds me to ask if we have changed our mind on these.

If a test is Closed, it is still alive and used. but it is something where we have delivered all the way to production some version of it and we intend to keep it alive there.

If I can get away with one test case, that is all I would do. There are many reasons for me not to be able to get away with it: a newer colleague we need a shared checklist with, me needing a checklist and creating it here with minimal extras, or auditing process that would not be fulfilled with just that one ticket of [Explore] Release.

The updating of test status is part of release activities for me. Someone needs to create a release in Jira, which usually happens when the previous release is out. For that release, I add at most two Cycles:

- Pre-Release Testing
- Release Testing

Again, if I can get away with it, I have only one: Release Testing and within in, I have only one test: [Explore] Release that I mark passed and write notes if I have something useful to say. Usually the useful thing for me to say is "release notes, including scope of changes is available here <link>".

The way testing works for me is that I see every pull request and nothing changes outside pull requests. I test selected bits and pieces of changes, assessing risk in the moment. I also have a set of test automation that is supposed to run blue/green (pick your color for 'pass') that hunts down need of attending to some detail. And I grow the set of automation. If you need 'proof' of passing for a particular release, we could in theory get that out of version control but why would you really want that?

The Pre-Release Testing Cycle, if it exists, I fill it when I think though what happened since last release and what still needs to happen before the next one and I drag in existing tests from all three categories [Explore], [Scenario] and [Feature] to be a checklist. What this cycle contains tells about themes and features I found myself limiting to. And when a Pass on the cycle isn't sufficient documentation, I can always comment the test ticket.

My use of Zephyr is *very* different to my colleagues. Perhaps also to your use?
