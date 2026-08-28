---
title: "Finding bugs that have been around a while"
date: 2016-01-29
updated: 2016-08-02
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/01/finding-bugs-that-have-been-around-while.html
---

# Finding bugs that have been around a while

*Published 2016-01-29, updated 2016-08-02*  
*Source: <https://visible-quality.blogspot.com/2016/01/finding-bugs-that-have-been-around-while.html>*

---

As part of my usual routines, there was yet another release. To keep myself alert and awake, I picked up yet another set of data over using the one safe one automation relies on.  
  
The major change in the release was a new luminaire printout, so I had sort of an idea on testing through some luminaire-functionality still in the staging environment. I brought in a common set of data (lazy selection), and a big visible error message pops up.  
  
Looking at the error message, I could see the application did not agree with my data. The data that was there already - specifically a string "100+" - was failing.  
  
A discussion with the developer later, I stop and I'm feeling puzzled. I had managed to not run into that bug for months and now, just when we were about to release again (daily), it just came my way by a lucky chance (from the change of data).  
  
Users with respect to this bug are like me. At some point they will end up trying to do just this in one of the projects (sets of data) that just so happens to have this condition. They haven't yet, or we'd see that from a log and fix. But since I spend much more time on the software, actively varying, I get there sometimes sooner. And whenever I get there, unlike the users, I take the time to discuss about it with my developers.  
  
Half an hour later the problem is gone. Like it never existed. But I still am stopping to wonder: how could I have found that bug earlier and I formulate a heuristic to take with me:  
> For string fields with imaginable integer comparisons, it's different to try 100a and 100+. Arithmetic is closer to the realm of numbers.
