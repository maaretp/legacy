---
title: "The Lure of Specifications"
date: 2018-03-18
updated: 2018-12-26
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/03/the-lure-of-specifications.html
---

# The Lure of Specifications

*Published 2018-03-18, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/03/the-lure-of-specifications.html>*

---

There's a fun little exercise from Emily Bache called Gilded Rose. The exercise is intended as a piece of software to extend, and naturally you'd want to have tests before you go on changing it. Coming to it from a more pure testing / tester perspective, my fascination towards the exercise is on how people end up modeling the work.  
  
Gilded Rose makes available:  

- [a Requirement specification](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/GildedRoseRequirements.txt)
- piece of code that "works in production" that is messy and would need extending
- a sample unit test

When setting up the exercise, I hand people the spec, and create a combination approval test with the sample unit tests scope that is easy to extend with new values.

The question goes as so many times before: how would you test this?  
  
Given a specification, most people jump at specification. As first values based on the spec get added, I usually introduce the idea of seeing code coverage as we are adding tests, and some people pick it up others don't.  
  
This particular exercise lets me model on how people connect three types of coverage when testing: covering the spec, covering the code, and covering the risk.  
  
The better ones have  
1) Refused to follow the spec step by step, because someone else must have done that already  
2) Thought of ways to test that neither the spec or the code introduce  
3) Not stopped testing at covering the spec when code coverage is still low.  
  
There's something about a specification that drives people's focus, making them less likely to see other things without added effort. Sometimes, it might make sense to step away from the lure of specification's answers, and see if the answers you'd naturally get to make any more sense.
