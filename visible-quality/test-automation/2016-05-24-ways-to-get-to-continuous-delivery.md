---
title: "Ways to get to continuous delivery"
date: 2016-05-24
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2016/05/ways-to-get-to-continuous-delivery.html
---

# Ways to get to continuous delivery

*Published 2016-05-24*  
*Source: <https://visible-quality.blogspot.com/2016/05/ways-to-get-to-continuous-delivery.html>*

---

I listened in on a talk today about Test Automation and Continuous Delivery. Paraphrasing what I think the speaker said is that:  
  

- None she knows of does daily deliveries without test automation (and stays sane - we heard of an other example like that though where "expecting normal workdays would just not be appropriate")
- We need to stop coming up with excuses on avoiding the test automation

In the end of the talk, I offered a counter-experience to understand her ideas a little better. I work with a  team that has, for two years now, done daily deliveries and with ridiculously little test automation. I feel we are still very much sane, we deliver quite safely. We are working - slowly - on adding some test automation, but for a long time, there was none. It took us long to build up skills for the right kind of automation we would find useful.

What I believe I learned is that we had an interesting discussion about our beliefs in what to invest in.

In her case, the problem she was solving was that testers were very frustrated with finding simple bugs in manual testing. That is a problem we sort of shared.

In her case, her team sought for solutions in the testing space and went for test automation. She told the audience that their automated tests are valuable, and find bugs pretty much on a daily basis.

In my case, my team sought for solutions in development and testing space, jointly. We had a limited amount of things we could do at a time, and conversations with my developers lead us to decide on investing primarily in cleaning up the code to make it more readable.

I asked the speaker today how their code was, and she confirmed theirs was messy.

So my train of thought is: you can choose to invest in making things better for your testers. If you feel you can invest over silo limits (not within the the testing silo), these two might be your options. You could get to same or in my experience, a better place investing into clean code. But most people seem to go for test automation as the primary investment, even with unclean code.

When your code is clean, your devs can have discussions around it easier. Devs share it easier, ask for feedback more eagerly. Devs make less mistakes as you go about changing it. With less mistakes, there's less of the simple bugs to be found in manual testing.

And when you top that with smart, adaptive exploratory testing like my team does, it is possible to do continuous delivery without automation. Automation would make us faster, but not necessarily safer. The cleanliness of code is what seems to have a connection in how we experience safety in customer feedback.

I don't think this is an excuse to avoid test automation for us. The excuse is that there has been a lot of skills to build up, and we chose to build those skills clean code first, unit testing with asserts and approvals and selenium tests later. And we're just still taking baby steps in the automation front, but doing great on the clean code front, reaping the results in our ability to deliver without breaking production.
