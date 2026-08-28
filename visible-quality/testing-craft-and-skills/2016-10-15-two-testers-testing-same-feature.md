---
title: "Two testers, testing the same feature episode 2"
date: 2016-10-15
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/10/two-testers-testing-same-feature.html
---

# Two testers, testing the same feature episode 2

*Published 2016-10-15*  
*Source: <https://visible-quality.blogspot.com/2016/10/two-testers-testing-same-feature.html>*

---

There are [two testers](http://visible-quality.blogspot.fi/2016/10/two-testers-testing-of-same-feature.html), with a lot of similarities but also a lot of differences. Tester 1 focuses on automation. Tester 2 focuses on exploration. And they test the same feature.  
  
And it turns out, the collaborate well, and together can be the super-tester people seem to look for. They pay attention to different things. They find (first) different things. And when that is put together, there's a good foundation for testing of the feature, both now and later.  
  
Tester 1 focusing on automation makes slow progress on adding automation scripts and building coverage for the feature. Any tester, with unfinished software to automate against would recognize her struggles. As she deeply investigates a detail, she finds (and reports) problems. As her automations start to be part of regular runs, she finds crashes and peculiarities that aren't consistent, warranting yet more investigation (and reports). The focus on detail makes her notice inconsistencies in decision rules, and when the needed bits are finally available, not only the other automators can reuse her work directly but also she can now easily scale to volume and numbers.  
  
Tester 2 focusing on exploration has also found (and reported) many bugs, each leading into insights about what the feature is about. She has a deep mind map of ideas to do and done, and organizes that into a nice checklist that helps tester 1 find better ways of automating and adds to the understanding of why things are as experienced. Tester 2 reports mistakes in design that will cause problems - omissions of functionalities that have in the past been (with evidence) issues relevant customers would complain about but also functionalities that will prove useful when things fail in unexpected ways. Tester 2 explores the application code to learn about lack of use of common libraries (more testing!), and placeholders, only to learn that the developer had already forgotten about them. Tester 2 also personally experiences the use of the feature, and points out many things about the experience of using it that result in changes.  
  
Together, tester 1 and 2 feel they have good coverage. And looking forward, there is a chance that either one of them could have ended up in this place alone just as well as together. Then again, that is uncertain.  
  
One thing is for sure. The changes identified by tester 2 early on are things that seem most relevant early on leaving more time for implementing the missing aspects. The things tester 1 contributed could have been contributed by the team's developer without a mindset shift (other than change of programming language). The things tester 2 contributed would have required a change in mindset.  
  
The project is lucky to have the best of both worlds, in collaboration. And the best of it all is the awesome, collaborative developer who welcomes feedback and acts on it in timely fashion and greets all of it with enthusiasm and curiosity.
