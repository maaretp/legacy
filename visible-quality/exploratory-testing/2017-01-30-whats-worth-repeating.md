---
title: "What's worth repeating?"
date: 2017-01-30
updated: 2017-07-23
theme: exploratory-testing
labels: [Exploratory Testing, Test Automation]
source: https://visible-quality.blogspot.com/2017/01/whats-worth-repeating.html
---

# What's worth repeating?

*Published 2017-01-30, updated 2017-07-23 · Labels: Exploratory Testing, Test Automation*  
*Source: <https://visible-quality.blogspot.com/2017/01/whats-worth-repeating.html>*

---

This is again a tale of two testers, approaching  the same problem with very different ways.  
  
There's this "simple" feature, having more layers than first meets the eye. It's simple because it is conceptually simple. There's a piece of software in one end that writes stuff to a file that gets sent to the other end and shown on a user interface. Yet, it's complicated looking at it from just having spent a day on it.  

- it is not obvious that the piece of software sending is the right version. And it wasn't due to an updating bug.  *Insight: test for latest version being available*
- it is not obvious that whatever needs to be written into the file gets written. *Insight: test for all intended functionality being implemented*
- it is not obvious that when writing to the file, it gets all the way to the other side. *Insight: test for reasons to drop content*
- it is not obvious that on the other side, the information is shown in the right place. *Insight:* *test for mapping what is sent to where it is received and shown*
- it is not obvious that what gets sent gets to the other side in the same format. *Insight: test for conversions, e.g. character sets and number precision*
- it is not obvious that if info is right on one case, it isn't hardcoded for that 1st case. *Insight: test for values changing (or talk to the dev or read the code)*

It took me a day to figure this out (and get the issues fixed) without me implementing any test automation. For automation, this would be a mix of local file verification (catching the file sent on a mock server because manually I can turn off network to keep my files, our automation needs the connection and thus a workaround), bunch of web APIs and a web GUI.  
  
  
So I look at my list of insights and think: which of these would even be worth repeating? And which of these require the "system" for repeating them and which could just as well be cared for on "unit" perspective. Rather straighforward mapping
architecture, yet many components in the scenario. Unlikely to change
much but to be extended to some degree. What automation would be useful
then if we did not get use of it as we were creating the feature in the
first place?    

And again I think there is an overemphasis on system level test automation in the air. Many of these I would recognize from the code if they broke again. Pretty much all but the first. We test too much and review / discuss / collaborate too little.  
    
Can I just say it: I wish we were mob programming.
