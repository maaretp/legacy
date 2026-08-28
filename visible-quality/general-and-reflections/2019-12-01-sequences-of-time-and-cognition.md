---
title: "Sequences of time and cognition"
date: 2019-12-01
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2019/12/sequences-of-time-and-cognition.html
---

# Sequences of time and cognition

*Published 2019-12-01*  
*Source: <https://visible-quality.blogspot.com/2019/12/sequences-of-time-and-cognition.html>*

---

Back in the days when we were starting to figure out what the essential difference between exploratory testing and the other testing was, we figure out that we would call the other scripted testing.  
  
We recognized separations of sequence in:  
  

- time - activities separated by time
- cognition - activities separated by skill focus

For exploratory testing to take place, the design and execution activities needed to be intertwined so that both time and cognition could not allow for separation. The reasons were clear:

- designing and planning what to do early *when you know the least* makes little sense has a high risk of wasteful activity
- designing and planning by a "more skilled" person to be executed by "less skilled" person assumes knowledge can be *transferred* with a document instead of seeing it as something *acquired* through effort.

  

With DevOps and Continuous Delivery, the time separation has transformed. We still see some of it in the sprint-based ways of working where we start with BDD-style scenarios very much separated in time even if only by days or hours. That part is scripted testing, not exploratory testing.

The cognitive separation has also transformed. For exploratory testing to be great, the cognitive sequence of today includes using code as a way of executing things and documenting things, and this can only be included if the exploratory tester knows programming at least to a level of effectively pair with others in turning ideas into code. The scripted variants separate the cognitive sequence into the person who designs the tests, the person who automates the tests and monitors them, and the person who tests stuff that automation may not cover, perhaps in what we used to know as exploratory testing way.

Thinking through this, I have come to the idea of cognitive bridges. In close collaboration with teams, the cognition around the testing activity even when it is split for multiple people can either be isolated (not exploratory) or bridged (exploratory).

We used to have cognitive bridges we organized for larger exploratory testing efforts through time-boxing and debriefing with other testers. Now have cognitive bridges in the whole team, and with activities beyond just plain testing. The one that fascinates me the most right now is how the tone of discussing developer intent builds a cognitive bridge.
