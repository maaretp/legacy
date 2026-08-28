---
title: "Fascinated with ApprovalTests"
date: 2016-06-22
updated: 2017-07-23
theme: test-automation
labels: [Approval Testing]
source: https://visible-quality.blogspot.com/2016/06/fascinated-with-approvaltests.html
---

# Fascinated with ApprovalTests

*Published 2016-06-22, updated 2017-07-23 · Labels: Approval Testing*  
*Source: <https://visible-quality.blogspot.com/2016/06/fascinated-with-approvaltests.html>*

---

Last Friday, I watched a group of software craftsmen agree on 3 \* 20 minutes of paired demonstration on a refactoring Kata "Gilded Rose", and then changing their mind after the first 20 minutes.  
  
The first 20 minutes was a pretty awesome demonstration of [Llewellyn Falco](http://twitter.com/LlewellynFalco) and [Aki Salmi](http://twitter.com/rinkkasatiainen) pairing in strong-style using ApprovalTests in Java. The first 15 minutes went into a cycle of adding tests using LegacyApprovals (that I knew from C# as CombinationApprovals) adding criteria to a one line of code based on what Emma code coverage tool was hinting might be missing. With every expected result, they just documented as ApprovalTests what current one was, over trying in any way to understand or describe it yourself.  
  
The last 5 minutes they cleaned up some code, covered with 100 % unit test coverage.  
  
The 5 minutes after their time-box the group used on extending to mutation testing, adding some more tests as PiTest-tool suggested some of the existing tests were weak.  
  
Total: 1350 tests with one line of code, and expected results defined as "if it works in production now, let's just keep it that way".  
  
On Saturday, I took part in a code retreat, and used ApprovalTests on some of my sessions. This left me thinking why I'm particularly fascinated with ApprovalTests.  

1. The tests in the file format with explanatory padding make sense in the world I think in.
2. The "recognition" part is what I feel I have special skills on anyway as an exploratory tester
3. The idea of filtering and processing depending on what technology you're testing to keep focus on testing makes sense to me
4. There's practical solutions to things that I've thought sometimes as too hard to test, like running combinations quickly or keeping tests that work against an external service fast (iExecutableQueries stuff, where you do slow stuff only on failure).
5. The idea of doing special things on failure for granularity makes sense, and changing reporters when investigating reminds me again of exploratory testing.
6. I like how this feels so much like exploratory testing on unit level.

Knowing the developer who created this stuff isn't actually a negative either. But for me, that would be often more of a reason to find actively reasons not to like it.I don't endorse friend's stuff blindly.  
  
Better do some more exploratory testing on the tool. Next up is understanding how well the claims of what different Approvers do is actually consistent over the implementation. And then I was thinking of finding ways of breaking it in the environment of use.  
  
If you want to pair on this, ping me. Just some educational fun on someone's open source project.
