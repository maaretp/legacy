---
title: "Thinking of Heartbeat"
date: 2016-12-12
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2016/12/thinking-of-heartbeat.html
---

# Thinking of Heartbeat

*Published 2016-12-12*  
*Source: <https://visible-quality.blogspot.com/2016/12/thinking-of-heartbeat.html>*

---

At where I work, every room seems to have an always on monitor for a test automation radiator. You know, one of these screens that, if all is well, turn dark blue after a while to indicate there has not been failures in ages (whatever the "ages" is defined to be). One where any shade of blue is what you seek and if you see yellow or red, you should be concerned.  
  
As I've walked around, the amount of not blue I see has been significant. My favorite passtime, almost, is to see how people respond to someone paying attention, and the reactions vary from momentary shame to rationalized explanations.  
  
One of the teams that has made more of a positive impact with their dark blue radiator got more of my attention, as the bright colors weren't taking the focus. I started reading names of the things and run into something interesting: Heartbeat.  
  
As I saw those words, I had a strong connection to the idea of what that could mean. A small discussion confirmed: heartbeat tests are the set that gives us information on is the system we're testing even alive enough that we could expect any other tests give us any information.  
  
For the things my team tests, to have a heartbeat we depend on the backend systems including a bunch of things running somewhere in Amazon Cloud. If any of the things we depend on fails, we fail. And for granularity, we want to know if the brokenness is for internal reasons (we should learn something) or from external reasons (we might have more limited control).    
  
With all the teams I see, I only see one that has a heartbeat measured with test automation separately.  
  
One team's heartbeat (a core dependency) is another team's core functionalities. You only need a heartbeat when you can't observe the other is alive from other means - their test status are not reliable or available/understandable to you.
