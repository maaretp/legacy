---
title: "An Old Story of a Handoff Test"
date: 2016-10-11
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/10/an-old-story-of-handoff-test.html
---

# An Old Story of a Handoff Test

*Published 2016-10-11*  
*Source: <https://visible-quality.blogspot.com/2016/10/an-old-story-of-handoff-test.html>*

---

It was one of these projects, where we were doing a significant system with a contractor. Actually, all software development was done by contractors, and on the customer side we had a customer project manager and then need to set up a little acceptance testing project in the end of it all. 
  
Acceptance testing was supposed to be 30 days at the end of the whole development effort. If the thing to be delivered was super big, you might have several rounds of deliveries. So it was it in this particular one.
  
  
As the time of acceptance testing was approaching, preparations were in full steam. No early versions of the software were made available. A major concern was that when the 30 days of testing starts, there’s no return. You test, you get fixes and you accept when you have no fixes pending. If the quality is bad enough and blocks testing, you’re not well off. 
  
  
The state of the art approach for dealing with the risk of bad quality that would block your testing and thus eat away your test time was to set up a handoff test, just before the testing would start. It would often serve a few purposes of confidence:
  

- the system to test was properly installed so that testing could happen
- we’re not wasting our specialists time on work the contractor was hired to do

  
For a typical handoff test, you needed to define your tests in advance and send the documentation to the contractor at least a week before the day of handoff test. And so we did, fine-tuned and tailored our tests to be prepared for the big day.
  
  
As the big day came, we all got together in one location to test. We executed the tests we had planned for, logged bugs and were in for a big surprise. 
  
  
The contractor project manager and test manager rejected all the reports. All of them. They reviewed them against the test cases as they read them, forged in iron. “You couldn’t find this problem with exactly these steps and these steps alone”. They did not reject the fact that the problems were not real. They rejected them based on the test cases.
  
  
Some hours (and arguments) later, we were back on track and the real bugs were real bugs. 
  
This experience just popped back from my memories, as I was reading about Iron Scripts where deviation isn’t allowed. I can just say that I’m so lucky to not have seen any of this in … about 6 years. I’m sure my past is still the current struggle for someone.
