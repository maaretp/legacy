---
title: "Continuous releases are a way forward even without automation"
date: 2014-04-10
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2014/04/continuous-releases-are-way-forward.html
---

# Continuous releases are a way forward even without automation

*Published 2014-04-10*  
*Source: <https://visible-quality.blogspot.com/2014/04/continuous-releases-are-way-forward.html>*

---

Tomorrow is a scheduled release day for one of my products. The scheduled release day approaching creates interesting behaviors: a product management team member requested for no testing today, or the release might be postponed. It feels easier not to know of problems.  
  
Coincidentally, tomorrow is also a release day for the other one of my products. It wasn't scheduled, but as we work with completing a feature at a time, it just got completed so tomorrow it will go out.  
  
The same day as release day left me thinking about the two different approaches, and how much of a difference there can be with one relatively simple change. The first team uses Scrum and sprints with a scheduled release, the second team uses Kanban and releases whenever features are ready, with emphasis on making the features smaller to flow through more fluently. Neither one of the teams has test automation to a relevant degree.  
  
The first team completes development on main, and does fixing after the sprint in a branch, while already working on the next release. The test-fix tail is scheduled to be about two weeks and yet always runs out of time postponing fixing. There's a lot of changes all around, and no change to test those within the schedule. Every day close to two weeks we just hope the testing does not find anything on time, to make the release - still realizing that testing was not done.  
  
The second team completes development on a branch, and tests and fix with focus on time through the process. When development (and testing and fixing) are complete, the feature is merged to main and a bit of final testing is done. We measure the times in different stages and realize test automation would make us faster, and schedule a piece of automation as the feature to complete every now and then. The second team was like the first team just less than a month ago. It's amazing how big a difference that makes.  
  
I love the fact that I can test with the second team continuously. The approach allows us to create a steady flow of features, whereas the sprint-type of model drove us into starting things that we barely completed - leaving most of the testing and fixing for later.   
  
I see two other things that could have helped us:  

1. Learning to build small things of value -- this is still on the list, but is making much slower progress than I would hope to see
2. Automating testing to a degree where the testing tail will be much much smaller -- which seems still hard to arrange enough time for, with all the legacy (testless) implementation

We tried both before going for "continuous (manual) deployment". Now to remove some of the manual work, one item at a time.
