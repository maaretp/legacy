---
title: "Devs Leading the Testing I Do"
date: 2018-09-12
updated: 2018-12-26
theme: leadership-and-management
labels: [Agile]
source: https://visible-quality.blogspot.com/2018/09/devs-leading-testing-i-do.html
---

# Devs Leading the Testing I Do

*Published 2018-09-12, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2018/09/devs-leading-testing-i-do.html>*

---

Dear lovely developer colleague,  
  
I can see what you are trying to do. You try to care about testing. And I appreciate it. I really do. But when you try to care about something you don't really yet understand well, it creates these weird discussions we had today.  
  
First I see you creating a pull request casually mentioning how you fixed randomly failing unit tests. That is lovely. But the second half of the sentence made no sense to me. While you were fixing  the randomly failing unit tests, you came to the conclusion that rewriting (not refactoring, but rewriting) a piece of logic that interfaces with the system in a way unit tests would never cover was a good idea. I appreciate how you think ahead, and care for technical quality. But did you at least  test the feature in the system context or just rely on your design working after the rewrite, based on the unit tests?  
  
Then I initiate a constructive discussion on how our system test automation does not cover that functionality you rewrote. I'm delighted with another developer colleague pitching in, volunteering to add that to test automation right away. For a few hours, I'm walking on happy clouds for the initiative. And then I talk to you again: you tell me that while the colleague already started, you felt the need of writing them a Jira ticket of it. And because there was a Jira ticket, I no longer should pay attention to the fact that your changes are in the release candidate we are thinking of giving to customers any moment now, as soon as testing of them is done. I appreciate that you think tracking it will help make it happen. But have you paid attention on how often tracking with Jira means excuse of not doing it for now in our team? And how you assigning work to others means that fewer and fewer of us volunteer to do the things because you keep filling our task lists identifying all sorts of things everyone else could be doing and assigning them around?  
  
The day continues, and I find two features I want to personally spend some time testing. The first one I pick up is created by yet another lovely developer. They didn't tell me it was done either, but my superpowers in spying folks pull requests reveal the right timing for the test. This is created by someone new, so I do more communication than I would do normally. And I do it visibly. Only to have you, dear lovely developer colleague again telling me how I should test it. Or rather, not test it. How there is someone else somewhere that will test it. Obviously I follow up to check that someone else has promised to do, and they haven't. Or they have promised to do something different. Like 1/10 of what needs doing. So I walk over your great plans of leading the testing I do, only to find out that the feature I tested don't work at all. So we talk about it, and you seem to agree with me that this could have been level of testing that takes places in our team. It would, in fact, be testing  that takes place not only in our team, but by the developer introducing the feature. Missing it once is fine. But not making it a habit through feedback is better. I introduce some ideas of exploratory testing on how I will make it fail, once I will first get it to pass once. You show me thumbs up, as if I needed you to approve the testing I do. I love how you care. But I wonder do you realize I care too?  
  
So I move on to the second feature I found, and confirmed that it will not be fully tested elsewhere. And you keep coming back to correct me on what I should be doing.  
  
Could you please stop assigning me Jira tickets that isolate testing from the pull request or the request of implementation you've worked on? Could you let me design my own work and trust that I know what I'm doing, without trying to micromanage me?  
  
I appreciate you care, but we all care. We all have our say in this. Stop leading the testing I do, and start sharing information you have, not assigning me tasks.  
  
I already think you're lovely. Imagine how awesome we'd be if you started believing I can do this? That we all can do this, and that you are not alone in this. That you don't need to track us, but work with us.
