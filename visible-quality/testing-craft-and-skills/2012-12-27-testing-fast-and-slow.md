---
title: "Testing fast and slow"
date: 2012-12-27
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2012/12/testing-fast-and-slow.html
---

# Testing fast and slow

*Published 2012-12-27*  
*Source: <https://visible-quality.blogspot.com/2012/12/testing-fast-and-slow.html>*

---

A few days into yet another monthly release, this one with team developer's feeling less motivated as the work was analyzed for them and they were asked not to think too much. End result is a nervous tester in the team, when bits and pieces are developed in isolation without much consideration of what purpose they're supposed to serve. There is no spec, and there's a atmosphere of denial for all issues that I may point out. Not a normal case, fortunately. Pressure is on for others as well, I think.   
  
Feeling the schedule pressure makes me test in a different way. I try to do a lot in a short interval of time, and I report bugs quickly without isolating them in detail. I realize I do this with the chance of buying time - with enough relevant issues that we're remotely aware of takes away the nice fuzzy feeling of "all is well since we did not see any problems" but turns us to another nasty, unusual case of having lots of issues were unable to fix because we can't yet reproduce them. And  not having the repro steps is a way of dismissing the info too.   
  
I just realized, looking at the differences in how the business owner reacts, that we really need to talk about the difference in testing fast and testing slow. Changing the pattern here is justifiable, but quite confusing when done without a warning.  
  
I'm not sure which one is worse:  

- releasing with hints of problems we cannot reproduce (yet)
- releasing with a few more fixes (due to nicely isolated bug reports) but not knowing what the users will experience

Seems with the time left I can't have both.
