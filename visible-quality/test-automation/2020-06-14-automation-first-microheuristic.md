---
title: "Automation First Microheuristic"
date: 2020-06-14
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2020/06/automation-first-microheuristic.html
---

# Automation First Microheuristic

*Published 2020-06-14*  
*Source: <https://visible-quality.blogspot.com/2020/06/automation-first-microheuristic.html>*

---

Developers announce a new feature is available in the build and could use a second pair of eyes. What is the first thing to do? Changing companies made me realize I have a heuristic on deciding *when* I automate test cases as part of exploratory testing.

Both automating and not automating end up bringing in that second pair of eyes, that seeking of understanding the feature and how it shows in the relevant flows. The first level of making the choice if you start with automating is if you are *capable of automating*. It makes the choice available on an individual level, and only after that it can be a choice.

When that choice is available, these things could impact choosing Automation First.

- Belief that change in the basic flow matters beyond anything else you imagine wrong with it

- When automating, you will visually and programmatically verify the basic flow as you are building it. Building it to a good reliable level takes longer than just looking at it but then remains around to see if changes in software change the status of it.

- Availability of quality dimensions (reliability, environment coverage) through automation

- If your application domain's type issues are related to timing of use or multitudes of environments where one works while others may not. automating first gives you a wider scope than doing it manually ever could.

- Effort difference isn't delaying feedback.

- With an existing framework and pipeline, extending it is an effort to consider. Without them, having to set things up can easily become the reason why automating takes so long it makes sense to always first provide feedback without it to ensure it can work.

- Brokenness of application

- Humans work around broken / half-baked features whereas writing automation against it may be significantly harder.

I was thinking of this as I realized that the automated tests on my current system see very few problems. There is no relevant environmental difference, like with my previous job. Automation works mostly in the change dimension, unlike my previous job.

Going into the moment of making this choice, I find I still go back to my one big heuristic that guides it all: **Never be bored**. First or Second does not matter as much as the idea that keeping things varied helps keep me away from boredom. Documenting with automation makes sense to avoid that boredom in the long run.
