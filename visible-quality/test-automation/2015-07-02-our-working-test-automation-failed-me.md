---
title: "Our working test automation failed me"
date: 2015-07-02
updated: 2017-07-23
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2015/07/our-working-test-automation-failed-me.html
---

# Our working test automation failed me

*Published 2015-07-02, updated 2017-07-23 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2015/07/our-working-test-automation-failed-me.html>*

---

I'm very happy with the progress on test automation my team is making. We work on three fronts: unit tests (with traditional asserts as well as approval tests), database checks that alert us on in-use inconsistencies and selenium web driver tests on single browser. Slowly but steadily we're moving from continuous delivery without automation to one where automation plays some role. A growing role.  
  
A week ago, our Selenium Webdriver test automation failed us in a particularly annoying way.  
  
We were about to release. I explored the changes for most of the day and all looked fine. I went home, attended to usual daily stuff with kids and finalised my tests in the evening. And as testing was done, I merged the test version to our staging version, ready for next morning to be pushed into production. Somewhere between these two times, a UI developer pushed a change in that broke a relevant feature. I did not notice as I wasn't careful looking at commits in the evening. He did not notice, as testing things he changes happens if he thinks his change can break things. This time he was confident it wouldn't.  
  
The next morning around 7 am, I saw a comment in Jira mentioning that one of the Selenium Webdriver tests failed in the previous night. 7.30 am the version was pushed into production. 8.30 am I read the Jira comment, learning we released with a bug that the Selenium Webdriver tests found. The person doing the release never got the message.  
  
The bug was not a big deal, but it pointed out to me things I've accepted even though I should not:  
  

1. Our Selenium Webdriver tests are brittle and controlled by an individual developer. No one else really recognises false positive and a real problem, but he does. So we were dependent on him mentioning problems to the right people. This time he did not.
2. Our Selenium Webdriver tests take two hours to run and we accept the delayed feedback. When one developer broke the build, he couldn't run these tests to learn sooner. And when he got the feedback morning after, he was disconnected from the fact that the thing he broke late previous night had already reached production.
3. We're making releases without running existing test automation for reasons that are in our power to change. We just haven't, yet.

It's great that we have one developer who is proficient with Selenium Webdriver to the extent that he does his own features tests first, adding tests of changed behavior as he is getting ready to implement the feature. It's great he's build in page objects to make automating easier.

It's not great that we accept the tests brittleness, keeping them one person tool. It's not great we accept the delay. And it's not great we have broke chain of communication with the accepted brittleness.

The most frustrating kind of bug to get to production is one where you had all means to find it on time. And yet it went through. But these things work as wakeup calls on what you might want your priorities to be: remove brittleness, make the tools we have useful for everyone for the purpose they exist to serve.
