---
title: "Anchoring an idea while Exploratory Testing an API"
date: 2020-07-21
theme: exploratory-testing
labels: []
source: https://visible-quality.blogspot.com/2020/07/anchoring-idea-while-exploratory.html
---

# Anchoring an idea while Exploratory Testing an API

*Published 2020-07-21*  
*Source: <https://visible-quality.blogspot.com/2020/07/anchoring-idea-while-exploratory.html>*

---

One of the things we get to test is a customer oriented API. It's particularly lovely test target for multiple reasons:

- Read-only: It only gets data, and does not allow us to change data. Makes it simpler!
- Time-constrained on API level: You can tell dates as input and it does freeze time for test automation purposes. You don't have to play with concepts of today() and now().
- Limited and understandable UI level edits to data: There are some things we can change from GUI that impact the API but they are fairly straightforward.

The main reason it brought us joy for testing today is that we found a bug on it a few weeks back where particular combination returns 500 error code (Server error) where it should not, and we got to start creating some tests back then to create a nice baseline for the time that bug would be fixed.

The long awaited message of bug fix arrived today, and the first thing we'd do is pull out the tests we had automated the last round (asserts and approvals, I wrote about those earlier as we set the project up). We ran the tests, expecting to see a fail for the assert for getting 500 for that bug. The results surprised us.

We still had that test passing, but now we also had another test failing with 500. Instead of going forward with the fix, we had momentarily gone backwards.

Not long after, we got to try again with a new version. This time it was just as we expected. Within 30 seconds of realizing the version was available, we knew that on the level we automated our tests before, those were now matching today's expectations.

For those of you concerned on the tests not running in CI, it is about the same time to go check they are blue as we did not place these tests as ones blocking the pipeline. These tests weren't designed for the pipeline, they were designed as an entry point for exploratory testing where we could leave some of them behind for the pipeline or for other purposes.

We quickly drafted our idea of what we would test and change today:

- Capturing and reviewing for correctness for the combination that we previously documented as receiving the 500 response for that bug
- Ensuring we could see latest data after the most recent changes
- Having easily configurable control over dates and times we had not needed in our tests before
- Making some of the tests approval files smaller in size as long as they did not lose the idea of what we were testing with them

What turned out to be the most fun thing to test was the latest data. Starting with that idea, we found multiple other ideas of what to test, including things around changing more values on the data, and things around multiple overlapping limits. We needed to remind ourselves, multiple times, that we still have not seen our starting idea in action, even if we had seem many other ideas.

As a conclusion of today, we came to the importance of anchor, and remembering that anchor. If writing it down helps, write it down. If having a pair that keeps you honest helps, have a pair. Whatever works for you. But a lot of times, when we do some testing, we end up forgetting what was the thing we set out to do in the first place. Anchoring an idea allows us to discover while we explore, and still stay true to what we originally set out to do.

We ended up refactoring our test code a bit to make it more flexible for the ideas we had today, and we discovered one test we wanted to keep for future. It started off with one name and concept, yet though exploring we learned that what we wanted to keep for future was different to what we wanted and needed to do today.

> Great chance of pairing on API [#ExploratoryTesting](https://twitter.com/hashtag/ExploratoryTesting?src=hash&ref_src=twsrc%5Etfw) with my trainee as there was a major change on the logic behind the API. Got to experience the ideas of tests we throw away, tests we want to keep for later but for reasons other than we start with, and relying on past tests.
>
> — Maaret Pyhäjärvi (@maaretp) [July 21, 2020](https://twitter.com/maaretp/status/1285570100423254018?ref_src=twsrc%5Etfw)

Truth is, we always throw some away, and that is where I recognize learning and thinking is going on. Can keep and should keep are two different things.
