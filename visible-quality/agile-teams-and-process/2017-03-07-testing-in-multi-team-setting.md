---
title: "Testing in a multi-team setting"
date: 2017-03-07
theme: agile-teams-and-process
labels: []
source: https://visible-quality.blogspot.com/2017/03/testing-in-multi-team-setting.html
---

# Testing in a multi-team setting

*Published 2017-03-07*  
*Source: <https://visible-quality.blogspot.com/2017/03/testing-in-multi-team-setting.html>*

---

There's a lovely theory of feature teams - groups of people working well together, picking up an end-to-end feature, working on a shared code base and as the feature is done (as in done done done as many times done as you can imagine) there's the feature and tests to make sure things stay as they were left off .  
  
Add multiple teams, and the lovely theory starts shaking. But add multiple teams over multiple business lines, and the shakiness is more visible.  
  
Experiencing this as a tester makes it obvious. I work on one business line and the other business line is adding all these amazing features. If the added feature was also built and tested from my business line's perspective, it would be ideal.  
  
The ideal breaks on a few things:  

- lack of awareness of what the other business line is expecting and needing, and in particular, that some of the stuff (unknown unknowns) tend to only be found when exploratory testing
- lack of skill on exploratory testing to do anything beyond "requirements" or "story"
- team level preference to create test automation code only to match whatever features they are adding

I've been looking at what I do and I'm starting to see a pattern in how I think differently than most people (read: programmers) in my team. When I look at the work, I see two rough boxes. There's the feedback that I provide for the lovely programmers in my team (testing our changes / components) and there's the feedback I provide for the delightful programmers in other teams (testing their changes in product / system context).  
  
It would be so much easier if in the team everyone shared a scope, but this division of "I test our stuff and other teams' stuff" gets very clearly distinguished when seeking for someone to fix what I found. And I find myself running around the hallways meeting people from the other teams, feeling lucky if my feedback was timely and thus a fix will emerge immediately. More often than not, it isn't timely and I get to enjoy managing a very traditional bug backlog.  
  
Features teams that can and do think in scope of systems (over product lines) would help. But in a complex world, getting all the information together may be somewhat of a challenge.  
  
Minimum requirement though: the test automation should be timely and thus available for whatever the team is that is now making (potentially breaking) changes without a human messenger in the chain.
