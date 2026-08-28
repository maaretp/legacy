---
title: "Re-testing without the tester"
date: 2017-01-19
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2017/01/re-testing-without-tester.html
---

# Re-testing without the tester

*Published 2017-01-19*  
*Source: <https://visible-quality.blogspot.com/2017/01/re-testing-without-tester.html>*

---

Some days we find these gems we, the testers, like to call bugs. Amongst all kinds of information, bugs are often things we treasure in particular. And we treasure them by making sure they get properly communicated, their priority understood and when they're particularly valuable, reacted on with a fix.  
  
We're often taught how the bug reports we write are our fingerprints and how they set our reputation. And that when something relevant was found and fixed, the relevant thing is worth testing again when a fix is available to see that the problem actually has gone away.  
  
We call this testing again, the precisely same thing as we reported the bug on, re-testing. And it's one of the first things we usually teach to new people that there is a difference in re-testing (precise steps) and regression testing (risk around the change made).  
  
Today I got to hear something I recognize having said or felt many times. A mention of frustration: "they marked the bug closed as tested, and it turns out they only checked that a big visible error message had vanished, but not the actual functionality".  
  
This was of course made even more relevant with external stakeholders coming back with the feedback that something had indeed been missed.  
  
What surprised me though was the quickness of my reaction to mention that it was not \*just the tester\* who had failed to retest the fix. It was also the programmer who did the fix, who had completely closed their eyes on the actual success of whatever change they did. And to me, that is just something I want to see different.  
  
It reminded me on how much effort I've put on teaching my close developers that I will let fixes pass into production without testing them - unless they specifically ask me to help because they are concerned of the side effects or don't have access to the right configuration that I would have.  
  
Re-testing needs to happen, but re-testing by a tester is one of these relics I'd rather see more careful consideration when it is done.
