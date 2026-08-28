---
title: "Automation tests worth maintaining"
date: 2017-07-22
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2017/07/automation-tests-worth-maintaining.html
---

# Automation tests worth maintaining

*Published 2017-07-22 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2017/07/automation-tests-worth-maintaining.html>*

---

A retrospective was on it's way. Post-it's with Keep / Drop / Try were added as we discussed together the perspectives. I stood a little on the side, being the loud one, leaving room for other people's voices. And then one voice spoke out, attaching a post-it on the wall:  
  
"It's so great we have full test automation for this feature"  
  
My mind races. Sure, it's great. But the automation we have covers nothing. While creating it for the basic cases, we found two problems. The first one was about the API we were using being overly sensitive to short names, and adding any of those completely messed up the functionality. I'm still not happy that the "fix" is to prevent short names that otherwise can  be used. And the second one was around timing when changing many things. To see things positively, the second one is a typical sweet spot for automation to find for us. But since then, these tests have been running, finding nothing.  
  
Meanwhile, I had just started exploring. The number of issues was running somewhere around 30, including the announce of the "fix" that made the system inconsistent and I still deem as a lazy fix.  
  
I said nothing but my mind has been racing ever since. How can we have such differences of perspectives on how awesome and complete the automation is? The more "full" it's deemed, the more it annoys me. I seek useful, appropriate and in particular over longer time not just on time of creation.  I don't believe full coverage is what we seek.  
  
I know what the automated tests test, and I often use those as part of my explorations. There's a thing that enables me to create lists of various contents in various numbers, and I quite prefer generating over manually typing this stuff. There's simple cases of each basic feature, that I can run with scripts and add then manually aspects to what I want to verify in exploration. I write a lot of code, extend what is there but I rarely check in what I have - only if there was an insight I want to keep monitoring for the longer term future.  
  
Cleaning up scripts and making them readable is work. Maintaining them when they exist is work. And I want to invest in that work when I believe the investment is worthwhile.  
  
The reason I started to tell this story is that I keep thinking that we do a lot of harm with the "manual" vs. "automated" testing dichotomy. My tests tend to be both. Manual (thinking) is what creates my automation. Automation (using tools and scripts) is what extends my reach in data and time.  
  
Tests worth maintaining is what most people think with test automation. And I have my share of experience of that through experimenting with automation on various levels.
