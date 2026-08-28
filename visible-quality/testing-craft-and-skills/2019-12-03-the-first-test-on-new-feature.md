---
title: "The First Test On a New Feature"
date: 2019-12-03
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2019/12/the-first-test-on-new-feature.html
---

# The First Test On a New Feature

*Published 2019-12-03*  
*Source: <https://visible-quality.blogspot.com/2019/12/the-first-test-on-new-feature.html>*

---

Testing various features, I have just one rule:  
> Never be bored.

Sometimes I try to figure out a template to what I do when I test and how I end up doing what I do, and it always boils down to this. Do something that keeps you engaged.  
  
Today I was testing a feature about scheduling tasks of all sorts, and as I was thinking about getting started, I told myself I should test the basic simple positive scenario first. Not that I thought that wouldn't work, but to show myself how the feature could work. I've used that rule a lot, but today that rule did not make me feel excited.  
  
Instead, I started off with a list of examples that was provided. I quickly glanced the list through, and selected one that looked complicated telling myself that if something wouldn't work, that would probably be it.  
  
It turns out I was right. Instead of seeing the feature work, I got to see a fairly non-explanatory error message on the log I was monitoring.  So I run a second test, the simplest sample from the list to see how it could work. From starting testing to discussing a bug with the developer was just minutes away.  
  
Meanwhile, I was having a discussion with another developer to refresh my ideas of test strategy: would we test these types of things in long term reliably with unit tests, yes - getting to a confirmation that while fixing what I complained about, the first developer had already improved the unit tests on it.    
  
Similarly, the fix for the bug was also just minutes away, and I needed to chip in some more ideas.  
  
I ended up asking a lot of questions. Questions around how things would work on leap years and days, impossible combinations of months and days and instead of ending up testing these, the developer volunteered. Questions around how time could be too short or too long for our taste. Questions around what the log would show. Discussions changed my perspectives, and clarified our shared intent around what we were building.  
  
I ended my day of testing with googling evil cron for testing, and had lots of fun with online tools generating me test data I could try. Things that were not supposed to work did and things that really stretched what was supposed to be valid were confirmed. I explored time calculation, passing valid and invalid values. And as always with testing, had a great time.  
  
These are first tests, and I'm not done. Instead of testing this all by myself, I invited a group of people to do mob testing with me on this, to test my own thinking and improve our test strategy around what makes sense to automate even further.  
  
There is no first absolute test. It is never too late to do the thing you thought you should have done first. With testing, very few options expire. You just need to keep track of your options.
