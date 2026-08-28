---
title: "Driving test automation forward as a product"
date: 2018-02-07
updated: 2018-12-26
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2018/02/driving-test-automation-forward-as.html
---

# Driving test automation forward as a product

*Published 2018-02-07, updated 2018-12-26 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2018/02/driving-test-automation-forward-as.html>*

---

I'm in a middle of a very complicated relationship, best defined by love-hate. On some aspects of it, I just LOVE what we've done. Yet on other aspects, I HATE where we are. It feels both a little schizophrenic and balanced. And I'm talking about the test automation I work with.  
  
I work with it by being on the sidelines. I know I can step in whenever I feel like it, but no one requires me to. I can look at it both as an insider and an outsider. My place and position is unique. I find that I see things others don't pay attention, and my attention brings out things others wouldn't be paying attention otherwise. And I share about this position for you, my dear reader, because there's something you could consider here:  
  

- if you are deep into automation, what a step back can give you as perspective
- if you are not deep into automation, what you can make sense of just by seeing concepts and reading code "as if it was English"

I'm working out my relationship with test automation because I'm no longer ok with test automation doing a bad job at testing or myself being a blocker for others by focusing on what it cannot do over what it can do.

There's things that I love, and where other people's appreciation helps me appreciate things more.

- Our ability to run automation that kicks off 14 000 clean OS instances up and down a day is quite an achievement, and that from "I want a clean OS to install on" to "I can start installing", it is a matter of a few seconds.
- When a new person joins and isn't left to discover the environment on their own, it takes a day to get started. Comparing this to new person joining discovering it on their own being weeks, basic proficiency being closer to 6 months I'm even a keener fan of pairing new hires for their first tasks.
- It runs and it is kept running. It enables releasing in a way products of this complexity could not be released without it.

  

There's things that I hate, that others seem to hate much less.

- It guides new hires to create a corner of their own over sharing common assets
- It has tons of embedded decisions over time that allows others to be judgmental about "not doing things right" for later hires
- Reuse of things has a manual coding element, taking days of coding to just introduce a concept like "same tests to another environment".  And people rather spend the days on the manual task than create an abstraction.
- People think of it as "testing a lot" because it runs often even if for a very limited set of things to test. It distorts \*managers\* concepts of how well we've tested, when same thing 1000 times is not 1000 times more testing for real.

So when I said I will reframe myself as an architect, I find I reframe myself first as test automation architect. I choose to work on things that drive the overall structures for the better. And just expressing things I would like to see us work on brings me to an interesting place of shining a light on things that have been that way.

Since I don't still end up dwelling in the code and implementation details all my days, I see concepts. I see that there's tests that are small (that I want more of) and tests that are large (that I want less of) - and I see that the structure does not help me see them. I see tests, test specific methods and common methods, that again the structure does not help me see them. I see products, applications and components, and that again the structure does not help me see them. I see similar use of resources, like having malware samples, temporary data and persistent data, and I see that the use of those isn't consistent.

I'm in a place where I have the vision of where we might head to for good or better, with limited ability to implement it all by myself. I might be paralyzed by my abilities alone, but others with different abilities may be paralyzed by not seeing things I see, or requiring things I require. In the last three years, I've acquired a superpower that allows me to still do much about this: pairing and mobbing.  That superpower, in addition to making it possible to turn my great ideas into code, gives us all a chance of learning together. And I'm looking forward to it.  
  
Test automation is a product that tests our other products. Caring for overall quality of it is just as necessary as caring for the details of each test.
