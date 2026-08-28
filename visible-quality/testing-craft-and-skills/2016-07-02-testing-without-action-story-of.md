---
title: "Testing without action - a story of performance"
date: 2016-07-02
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/07/testing-without-action-story-of.html
---

# Testing without action - a story of performance

*Published 2016-07-02*  
*Source: <https://visible-quality.blogspot.com/2016/07/testing-without-action-story-of.html>*

---

I'm reading Daniel Knott's Hands-on Mobile App Testing and at 33 percent, I'm disappointed. I reserve the right to change my perception in the next 67 percent but so far it hasn't lived up to my expectation from Cem Kaner suggesting it as a context-driven approach to test automation.  
  
There's so far a main theme that seems to bug me: there's a lot of "you must" advice, including advice that would be very application specific. Following the advice for some of the apps, I'd end up testing a lot of the OS features instead of our application. But even more I'm bugged about the total lack of discussion about the idea that testing provides *information* and for that information to be valuable, it should be something someone wants to *act on*. The action could be fixing, or knowing what consequences to face when the time comes. And if there is information we know from experience that our developers and product owners just don't care about, at least we should be advised to be careful on how much of the limited time and effort we spend on finding that types of stuff.  
  
Reading the book made me think of an experience on performance testing that illustrates more of context for me.  
  
I was working with a C# web application and we knew the performance experience was not up to par. We had no performance tests, but you did not need tests to know this: hands on the application was enough. We had already spend a lot of time and energy optimizing whatever we could, but we just had an architectural issue and a lot of code based on that architecture.  
  
No amount of testing or no sophistication of testing would have helped us solve that problem. We knew the solution: it would be moving from one technology stack to another. With the current, all data was going back and forth. With the other, we could update only the information that was being touched at the moment.  
  
But there was always something more relevant to work on with implementation. So instead of testing for performance, I used my time on advocating for performance, helping negotiate a time box in which we could start the change. The action was more important than the testing. The shallow information was enough, we did not need details.  
  
Finally, we got to change the technology. And now, having actual possibility to design things to improve the performance in use, we cared for measuring it. At first we just had someone time manually basic workflows, to learn what we cared about. Very soon the programmers would jump in to say no human should suffer that assignment, and automated the task so that the person could just focus on analyzing changes in the numbers.  
  
So, when I read a testing book, I would like to see more discussion about how much time and effort we invest on what type of information. And if there really is information that we won't be interested in acting on, perhaps we should think twice why we spend so much time and advice on telling it must be tested.
