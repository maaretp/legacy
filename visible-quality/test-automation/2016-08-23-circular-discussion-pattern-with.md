---
title: "Circular discussion pattern with ApprovalTests"
date: 2016-08-23
updated: 2017-07-23
theme: test-automation
labels: [Approval Testing]
source: https://visible-quality.blogspot.com/2016/08/circular-discussion-pattern-with.html
---

# Circular discussion pattern with ApprovalTests

*Published 2016-08-23, updated 2017-07-23 · Labels: Approval Testing*  
*Source: <https://visible-quality.blogspot.com/2016/08/circular-discussion-pattern-with.html>*

---

At Agile 2016 Monday evening, some people from the Testing track got together for a dinner. Discussions lead to ApprovalTests with Llewellyn Falco, and an hour later people were starting to get a grasp of what it is. Even though I Golden Master could be quite a common concept.  
  
Just few weeks earlier, I was showing ApprovalTests to a local friend and he felt very confused with the whole concept.  
  
Confusion happens a lot. For me it was helpful to understand, over longer period of time that:  

- The "right" level of comparison could be Asserts (hand-crafted checks) vs. Approvals (pushing results to file & recognizing / reviewing for correctness before approving as checks).
- You can make a golden master of just about anything you can represent in a file, not just text.
- The custom asserts are packaged clean-up extensions for types of objects that make verifying that type of object even more straightforward.

Last week, I watched my European Testing Conference co-organizers Aki Salmi and Llewellyn Falco work on the conference website. There was contents I wanted to add that the platform did not support without a significant restructuring effort. The site is nothing fancy, just Jekyll + markup files built into HTML. It has just a few pages.  
  
As they paired, the first thing they added was [ApprovalTests for the current pages](https://github.com/EuropeanTestingConference/site-tests) to keep them under control while restructuring. For the upcoming couple of hours, I just listened in to them stumbling on various types of unexpected problems that the tests caught, and moving fast to fix things and adjust whatever they were changing. I felt I was listening to the magic of "proper unit tests" that I so rarely get to see as part of my work.  
  
Aki tweeted after the session:    
> The more I have chance to work with [@LlewellynFalco](https://twitter.com/LlewellynFalco), the more I fell in love with ApprovalTests - this makes refactoring so fast and easy.
>
> — Aki Salmi (@rinkkasatiainen) [August 17, 2016](https://twitter.com/rinkkasatiainen/status/765981477674811393)

If you go see the tweet I quoted, an exemplary confusion happens as a result of it.  

1. Someone states ApprovalTests are somehow special / good idea.
2. Someone else asks why they are different from normal tests
3. An example is given of how they are different
4. The example is dismissed as something you wouldn't want to test anyway

I don't mean to pick on the person in this particular discussion, as what he says is something that happens again and again. It seems that it takes time for the conceptual differences of ApprovalTests in unit testing to sink in to see the potential.  
  
I look at these discussions more on the positives of what happens to the programming work when these are around, and I see it again and again. In hands of Llewellyn Falco and anyone who pairs with him, ApprovalTests are magical. Finding a way of expressing that magic is a wonderful puzzle that often directs my thinking around testing ApprovalTests.
