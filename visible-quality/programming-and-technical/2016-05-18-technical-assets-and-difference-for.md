---
title: "Technical Assets and the difference for testing"
date: 2016-05-18
theme: programming-and-technical
labels: []
source: https://visible-quality.blogspot.com/2016/05/technical-assets-and-difference-for.html
---

# Technical Assets and the difference for testing

*Published 2016-05-18*  
*Source: <https://visible-quality.blogspot.com/2016/05/technical-assets-and-difference-for.html>*

---

This Monday, we released something we've been working for way too long. To get to this point, we've deleted massive amounts of code and refactored (with the definition of it can be refactoring without unit tests with R# in heavy use).  
  
For a period of time, there was a separate code-base for every configuration of the environment. I think we were up to five by time of cleanup.It was a tester's nightmare. If you'd find a problem (and there were plenty, more than anywhere else in our product), the problem was twofold. First of all, the problem was likely to be elsewhere, and it was likely the developer would forget one or more of those places when fixing - not to speak about how slow fixing was. Second, whenever something got fixed, something else somewhere broke. It felt like a house of cards.  
  
Seeing the difference in how this felt was easy to see in my team, since every other part of our application has a different feel to it. When there's a fix, I can count with one hand's fingers the amount of side effects. Fixing feels quick. Also, the fix gets very often applied to different places at once. Surely, sometimes there are side effects but rarely.  
  
The feel of the first and the latter is like night and day. With code like the first, one of me isn't enough for one developer. For code like the second, one of me is plenty for 5 developers.  
  
I've looked at the ongoing discussion long enough to see where the difference I'm experiencing first hand comes from. It comes from skilled developers who build smart technical assets. They actively build and share components to have things done in one place. But the biggest difference comes from communication: they find the components, because they talk.  
  
Mob Programming has increased the amount of practice level talking, and I expect that the continued mobbing will lead to more technical assets - one line of code to do a thing that takes hundreds when reinvented. And the impact on how we test is profound. It's the way it should have always been, but wasn't, not for all parts.
