---
title: "All I got for a week of programming was one lousy test script"
date: 2018-01-12
updated: 2018-12-26
theme: programming-and-technical
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2018/01/all-i-got-for-week-of-programming-was.html
---

# All I got for a week of programming was one lousy test script

*Published 2018-01-12, updated 2018-12-26 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2018/01/all-i-got-for-week-of-programming-was.html>*

---

From the title, you might think the post is about venting on how slow it is to learn automation. If that's what you are looking for, this is not that post. Instead, this is a post about insights of what happens while we program test automation.

There was a fairly simple end to end scenario that needed testing. The tool of choice was Python, and examples of doing something fairly similar were plentiful.

To maintain the focus, the scenario was first drafted just as code comments. The steps the script should go through. The verifications that needed to happen along the way. The way we would determine what to make note of while the test was running, and what would be things that need to stop the test from proceeding as it just makes no sense.

It could all be very simple, except it almost never isn't.

First of all, to figure out the scenario, some details of what to check require the external imagination: product we are testing. Seeing the details of what could be verified need hands on the computer. We could call that automating, but what we actually do is mostly manual. Sometimes we can run the start of the script to get to the point of pondering. But  the pondering is still a manual process. We look at what is available that we could programmatically access. We think of what is good enough to determine if things work, and how the actual application would allow us to see things with code.

As we get to a manual process, we learn that while I wanted to do a thing, for some reason it does not work. We find bugs. Some of the bugs we notice when we just run through the scenario manually. Other bugs we notice, because automation is picky. Where a person can just work around some deficiencies, automation may get us momentarily stuck. Something else needs changing before the script can proceed. And we end up with todo-markings in our automation code, even fixing the problems on the application ourselves just to be able to make progress.

Towards the end of the week, multiple little learnings later with blocking bugs fixed, we finally get the script to a point where it runs in its intended scope. Allowing then to think outside this little agreed box that took the whole week, there's more. But also, just going though this one scenario is already making the work of adding another easier. There will again be bugs, but they will be different. The scenario we already automated gets run since its introduction, alerting us on possible regressions.

I write this post because I read that "Testing as an exploratory, investigative activity, cannot be replaced by automated checks". It bothers me how often we testers say this. The automated checks are done by people too. The human part of a check precedes creating the automation that successfully executes things. It grows as we add more checks. Many times when automating, we need to look with more detail.

The risk to good testing isn't in including automation into the way we work. It is in not looking wide if automation gives you the sense of already covering what ever scenarios are relevant. The risk is the automators who say "this is fully tested" when there really is one happy day scenario with one set of very limited data and selections.

Automation has so much power as a way of executable documentation.
