---
title: "Testing, A Day At a Time"
date: 2022-06-13
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2022/06/testing-day-at-time.html
---

# Testing, A Day At a Time

*Published 2022-06-13*  
*Source: <https://visible-quality.blogspot.com/2022/06/testing-day-at-time.html>*

---

A new day at work, a new morning. What is the first thing you do? Do you have a routine on how you go about doing the testing work you frame your job description around? How do you balance fast feedback and thoughtful development of executable documentation with improvement, the end game, the important beginning of a new thing and being around all the time? Especially when there is many of them developers, and just one of you testers.

What I expect is not that complicated, yet it seems to be just that complicated.

I start and end my days with looking at two things:

- pull requests - what is ready or about to be ready for change testing
- pipeline - what of the executable documentation we have tells us of being able to move forward

If pipeline fails, it needs to be fixed, and we work with the team on the idea of learning to expect a green pipeline with each change - with success rates measured over last 10 2-week iterations being 35 - 85 % and a trend that isn't to the right direction with an excuse of architectural changes.

Pull requests are giving me a different thing that they give developers, it seems. For the they tell about absolute change control and reality of what is in test environment, and reviewing contents is secondary to designing change-based exploratory testing that may grow the executable documentation - or not. Where Jira tickets are the theory, the pull requests are the practice. And many of the features show up with many changes over time where discussion-based guidance of the order of changes helps test for significant risks more early on.

A lot of times my work is nodding to the new unit tests, functional tests in integration of particular services, end to end tests and then giving the application a possibility to reveal more than what the tests already revealed - addressing the exploratory testing gap in results based on artifacts and artifacts enhanced with imagination.

That's the small loop routine, on change.

In addition, there's a feature loop routine. Before a feature starts, I usually work with a product owner to "plan testing of the feature", except I don't really plan the testing of the feature. I clarify scope to a level where I could succeed with testing, and a lot of times that brings out the "NOT list" of things that we are not about to do even though someone might think they too will be included. I use a significant focus on scoping features, scoping what is in a release, what changes on feature level for the release, and what that means for testing on each change, each feature, and the system at hand.

In the end of a feature loop, I track things the daily change testing identifies, and ensure I review the work of a team not only on each task, but with the lenses of change, feature and system.

I tend to opt in to pick up some tasks the team owns on adding executable documentation; setting up new environments; fixing bugs and the amount of work in this space is always too much for one person but there is always something I can pitch into.

That's the feature loop routine, from starting together with me, to finishing together with me.

The third loop is on improvement. My personal approach to doing this is a continuous retrospective of collecting metrics, collecting observations, identifying experiments, and choosing which one I personally believe should be THE ONE I could pitch in just now for the team. I frame this work as "I don't only test products, I also test organizations creating those products".

It all seems so easy, simple and straightforward. Yet it isn't. It has uncertainty. It has need of making decisions. It has dependencies to everyone else in the team and need of communicating. And overall, it works against that invisible task list of *find some of what others have missed* for resultful testing.

Bugs, by definition, are behaviours we did not expect. What sets Exploratory Testing apart from the non-exploratory is that our reference of expectation is not an artifact but human imagination, supported by external imagination of the application and any and all artifacts.
