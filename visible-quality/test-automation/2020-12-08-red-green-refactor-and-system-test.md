---
title: "RED green refactor and system test automation"
date: 2020-12-08
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2020/12/red-green-refactor-and-system-test.html
---

# RED green refactor and system test automation

*Published 2020-12-08*  
*Source: <https://visible-quality.blogspot.com/2020/12/red-green-refactor-and-system-test.html>*

---

In companies, I mostly see two patterns with regards to red in test automation radiators:

1. Fear of Red. We do whatever we can, including being afraid of change to avoid red. Red does not belong here. Red means failure. Red means I did not test before my changes can be seen by others.
2. Ignorance of Red. We analyze red, and let it hang around a little too long, without sufficient care on the idea that one known red hides an unknown red.

I don't really want either of these. I would like to work in a way where we bring things back to a known (green / blue - pick your color) baseline, but seeing red is invitation to go dig deeper, to explore, to understand why.

Red being associated with failure is a problem. With Red-Green-Refactor cycles, we want to start with red. Red is an essential part of the process. Trying to make progress with occasional fails is better than not making progress to avoid all fails.

The red allergy is allergy to failing. And allergy to failing is an indication that we don't have a mindset of appreciating learning.

Instead of fearing red, we should fear green/blue. Red calls in for action, green/blue accepts a status quo. W can only trust green/blue if we have, in the process of creating the tests, seen red. Make it fail, make it pass, clean it up.

I think back to the projects I've watched with system test automation, and red is not an infrequent visitor. Red invites work. And with making decisions, we still wish we'd have less red, and faster analysis of the red.

From appreciating the red, to working to get the right red to right hands sooner - that is my call for action. And with a system of systems being automated, the granularity of feedback is a fascinating problem to solve.
