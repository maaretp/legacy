---
title: "What do you mean, I should support this?"
date: 2013-02-26
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2013/02/what-do-you-mean-i-should-support-this.html
---

# What do you mean, I should support this?

*Published 2013-02-26*  
*Source: <https://visible-quality.blogspot.com/2013/02/what-do-you-mean-i-should-support-this.html>*

---

I'm enjoying my tester privilege of appreciating nice bugs. There was one particularly worth appreciation with our product last week, when we learned that there are proxies that do encoding-transformations on our URLs thus breaking our product that won't handle the encoding (around &-character in particular).  
  
The customer wouldn't know why they get a big visible error. They just tell us it doesn't work. Or to be a little more precise, they tend not to tell us, we get to see their experiences from our logs when they are of that  type.   
  
After realizing what was happening, it was relatively easy to go around.  
  
The fun part with the bug started, when I told my other development team about this bug - that we should, as a team, also remember that our product works in an environment we're not in control of. The response was quite direct and can be paraphrased as "not our responsibility". With a little discussion, we are now with the conclusion that it is our responsibility thought the technologies and architectures we build on. Some handle this better than others, and if we choose one that needs a bit of support on that, we'd handle it if only we understand we should or could.  
  
It's so easy to see things as external even though for the customer they are just one part of the product experience.
