---
title: "Reading specifications with thought"
date: 2013-10-28
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2013/10/reading-specifications-with-thought.html
---

# Reading specifications with thought

*Published 2013-10-28*  
*Source: <https://visible-quality.blogspot.com/2013/10/reading-specifications-with-thought.html>*

---

There's a rock I've hit hard too many times recently and the pain I feel is clearly telling me there's a need of changing. As part of me processing this, I thought I'd blog. After all, it's been too long.   
  
Starting with an example, simplest out of the selection. We've been adding a feature to our product, which is about printouts. I've seen the spec, read it as thoughtfully as I did in that time, and waited a little to get the feature implemented to do some testing.  
  
It turns out that the feature was nice in isolation of other surrounding similar features. It turns out it was nice on picture and text, but when put together with live scenarios, there's more than first meets the eye.  
  
So I log a bug on that. We eagerly discuss it with the team and decide on a change to what we had thought previously. Implement and again comes testing...  
  
It turns out that we missed yet another scenario. While the first issue was that printouts of two sorts worked differently on main view, the second one is that there's more than the main view and again inconsistencies that would lead us to a different design.  
  
I'm frustrated, as I did not see these coming looking at the spec. Then again, anyone else did not either. But failing twice in a row, with very similar pattern, is just painful. And we keep failing with a similar pattern.   
  
So thinking about what to change, I realize I'm puzzled. I could take more time to test the specifications, since I seem to have some touch to seeing the problems with the live product. Then again, someone else could do that too.  
  
Positive side: no one in the team is initiation discussion whether these are bugs / should be fixed. Just frustrated with the inability to remove the root cause that keeps us stomping on similar issues again and again.  
  
For anyone handling tester's issue reports - there's usually more than
the one described symptom. Removing a symptom without addressing the
underlying problem isn't taking us where we'd want to be.  
  
Off to reading the next specification, with scenarios I just defined to support my thinking. Perhaps these will help the others see problems too, time will tell. Reading with thought is quite different from just reading. So many things between the lines that make us waste everyone's effort.
