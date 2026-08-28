---
title: "One thing at a time or mixing it all together"
date: 2013-04-04
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2013/04/one-thing-at-time-or-mixing-it-all.html
---

# One thing at a time or mixing it all together

*Published 2013-04-04*  
*Source: <https://visible-quality.blogspot.com/2013/04/one-thing-at-time-or-mixing-it-all.html>*

---

With the stuff I'm currently testing, I've been heavily pressed with schedule. I'm pretty sure I had half of the time compared to what I would need, and I wasn't aiming for perfection.  
  
With the schedule pressure on my, I realized I was doing too many things at once, not completing any of my ideas of what to test. To a degree, that wasn't a problem, as I was still finding relevant problems (ones others think need to be fixed before we release) with that strategy too, but I wasn't very happy with myself trying to explain myself why none of the things was not done.  
  
Yesterday I decided I'll dedicate today on just one idea of how to test. I set up the old version and the new version, with exactly same production data with migration magic done in between and run the two version side by side. I decided for today, I will focus on just problems on the data being shown differently with an easy oracle - the version that was not remade in the last six months for maintainability and problems where functionality is present in the old version but missing from the new.  
  
I had a very productive day, and I feel more satisfied with myself setting to do something and knowing where I am with that - halfway through as the 20 newly identified problems did slow me down from my optimistic schedule - and having a nice list of variables I could still attack with the same comparison approach.  
  
How I tested before? Mixing all the aspects. I would use different users, data, browsers for pretty much any functionality I'd work with. That works too.  
  
It's easy to say now that I should have done this change earlier. There's nothing that was exactly preventing me from doing it. Just my concept of best use of time that was finetuned with seeing the bugs that mattered enough to get fixed and finding a way to test to target those now.
