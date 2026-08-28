---
title: "Approaching zero bugs"
date: 2016-04-19
updated: 2017-07-22
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/04/approaching-zero-bugs.html
---

# Approaching zero bugs

*Published 2016-04-19, updated 2017-07-22*  
*Source: <https://visible-quality.blogspot.com/2016/04/approaching-zero-bugs.html>*

---

Zero bugs. Stop coding bugs. I can't help but smile a little whenever I hear this but often choose to step away from the argument. This was a topic, however, that [Arlo Belshee](https://twitter.com/arlobelshee) addressed at Agile Alliance Technical Conference.  
  
I don't really care much for zero. But I care for numbers becoming much smaller than what we're used to. And that is the perspective I listened into the discussion around the fancy marketing term.  
  
The core idea I picked up was that *when your code reads well, you make less mistakes*. And that your ability to read code is more important than the executable tests keeping your code harnessed. Even more, it could be that the amount of code comments could be a negative indicator on the ability to code with less mistakes, as good code reads kind of as English.  
  
I've been speaking about the fact that my team does continuous (daily) delivery without test automation around. It's nowadays so normal for me that I don't really put much effort anymore into explaining it to others. But when I still talked about it, I heard we're irresponsible. I heard it is not possible even if I've lived it for almost two years now. And it is possible with a team of 10 developers and one tester.   
  
The zero bugs discussion gave me new tools to look at what we do and what might make us successful in what we do.  

1. **We focus on code readability.**  
   We're cleaning up and rewriting regularly. I encourage this behavior - even if it means I get to help test same things over and over again, as the amount of test automation is ridiculously narrow.
2. **Developers do exploratory testing**  
   The developers test themselves quite extensively. This is actually the main reason I'm driving forward test automation in my team still, as I feel the manual testing must make us slower on this part. We're careful. But with care, we also succeed in introducing very little regression while delivering features with a steady pace.
3. **Tester adds perspectives to exploratory testing**  
   When I test, I still find problems, so we're down to small numbers only after addressing the internal feedback. For the last year, the developer's testing skill has increased significantly, and a part of succeeding with this is my new discipline of avoiding writing bug reports (replacing them with discussions).   
     
   There's a special approach on how I find my problems, and I still try to open it up better with my team. I read shape of code commits to know what I will cover. I will compare the shape I see to the shape I expect based on discussions. And shape of discussions is a form of both what is said a lot, a little and not at all. The shapes are models and I overlay a lot of different models to make up my mind of what to cover.

I see value in what I do to keep things great for production, but also love the fact that I'm increasingly less needed - I call that progress. But listening to the zero  bugs discussions, I get the idea that I might have been discounting the value of my other activity as a tester: making sure my developers are empowered and supported in their need of keeping the code readable, to their best current knowledge. I love how they pick up new things and ideas and hate their old stuff - that's how it is supposed to be.  
  
The more we practice, the better we get. How often are we allowed to fix our past mistakes, made at times we knew the least? I would hope the answer is: every day.
