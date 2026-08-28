---
title: "Semi--automated tests, with an advanced version"
date: 2016-03-06
updated: 2017-07-23
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2016/03/semi-automated-tests-with-advanced.html
---

# Semi--automated tests, with an advanced version

*Published 2016-03-06, updated 2017-07-23 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2016/03/semi-automated-tests-with-advanced.html>*

---

Remembering back a few jobs ago, I was working with a great team of testers and we were trying to figure out automation. We put together weekly retreats on the other side of the company premises to find time away from the regular work and interruptions, working on adding incremental value through automation to the testing we were doing.  

Back then, one of the leaders from test automation perspective introduced us a concept of semi-automated tests. There's things that are easy to have the computer do, and things that are harder to have the computer do. Tests that would take us to the point where human intervention was required and then just pop up a message allowing you to do your bit after all the leading into -steps automated was useful. We really needed something like that back then: a reminder that with "test automation", it's not about automating all things testing but some things testing - any that is useful.

Today I remembered this experience as I was exploring [ApprovalTests](https://github.com/approvals/ApprovalTests.Net) with [Llewellyn Falco](http://www.twitter.com/LlewellynFalco) (the main developer of this open source project). He was showing me a particular group of test, using fancy words like iExecutableQuery and at first, I was somewhat disengaged. Hard words of stuff that don't map out in my mind. He run the first test, explaining what was going on and I started connecting pieces. With third and different test, I realized the usefulness of what he was doing.

He had unit tests running on 3rd party software, and I was thinking these cannot exist, making me more disengaged than I should have been. The idea on how the tests were set up were interesting and useful.  
  
His test would create a call to the 3rd party app (diff tools in this particular case) and save it into a file and launch that 3rd party app.  This would only pop up on failure. If the call had remained the same, he would only verify the call, but on1st time and later on failure he needed to see also that the 3rd party app did what was expected.  
  
This was a much more advanced way of doing the semi-automated tests I found useful already a decade ago. This turned the semi-automated while testing once into automated for regression purposes. Surely it does not test "the real thing". But the abstraction it tests feels useful.  
  
With all the tests I've been seeing, why haven't I seen more of this before? Have you?
