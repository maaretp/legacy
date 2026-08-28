---
title: "Test Automation Smells so Obvious Anyone Could Notice"
date: 2018-01-23
updated: 2018-12-26
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2018/01/test-automation-smells-so-obvious.html
---

# Test Automation Smells so Obvious Anyone Could Notice

*Published 2018-01-23, updated 2018-12-26 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2018/01/test-automation-smells-so-obvious.html>*

---

Like so many exploratory testing enthusiasts before me, I can easily find things to do with my time so that I don't have to go dig into the realms of test automation. But every now and then, unlike so many exploratory testing enthusiasts, I go and take a dig at automation anyway. It reads mostly like English anyway.  
  
  
  
Here's my list of things to work on inspired looking at one set of tests today.   
  
**Tests that don't test only tour**  
  
So you have some kind of structure with your tests. You have test suites / sets somewhere that bundle things together. You have some tests going into those suites /sets. And you have some libraries you can use. Great start. But take a look at the things in this that are considered tests. Can you find any that haven't got a single verification, asserting that something must be true? When you do, these are tests that don't really test, they tour. They are a path to getting to a place where you actually want to do some testing. Don't muddle them together on the same level as things that actually are checking things.   
  
**Tests inheriting tests over libraries**  
  
Inheritance can make things very muddled for  your random stroller. You're trying to read steps of what happens, and for sake of similarity, someone came up with the great idea of inheriting and overriding to create the differences. Same things would appear like they could be done with libraries, instead of test cases. Do you really have to conceptually mix up test cases with inheritance?   
  
**Randoms inside a test**  
  
You see a test that says TestABC. Great, it looks like this is a test that tests ABC. You continue reading, and a call to random pops in front of you. Whenever this test gets run, it always does ABC but there's a few different ways to do ABC. Someone decided to leave which of the ways you get to faith, making sure every time it fails you need to go and check which of the options was broken. Isn't there enough lack of deterministic behavior in the tests without adding randoms in?   
  
**Avoiding passing values**  
  
Reading the code, you start realizing a whole lot of method calls look like they're the same yet they are not - quite. There's some little detail on each that differs. Your method could take an argument, and you could do some magic with the argument. But for some reason it seems it was a better idea to create a number of separate methods to call, without argument but each including what looks awfully lot like a thing that would have belonged in the place of an argument in its name.   
  
**Duplicating to my corner**  

There's a directory there somewhere, that uses a label you recognize as a concept meaning ownership that draws you in. And you find a nice cozy corner of clearly laid out tests. Reading through their names, you start to feel like you've seen some of them before. Searching confirms - there's a well organized little corner there somewhere what everything is concisely together. There however is a lot of duplicated code elsewhere. But that must be someone else's problem.   

**A Fool's Coverage**  

As an exploratory tester, you start realizing how much coverage there could be if the collaboration between what you learn and know would better turn into automation. You identify some of the English in the tests that makes sense in the world of using the application for exploring it, and realize how little of your ideas have ended up encoded into the tests. Whatever is in, gets continuously monitored. Running the same thing a thousand times isn't really yet that much in the coverage - it's a version of a fool's coverage.   

Here's a thing: anything I can name and recognize, I can fix. And while these feel obvious to me today, they clearly have not been equally obvious when they were introduced. What does your "let's fix these" list look like?
