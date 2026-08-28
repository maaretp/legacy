---
title: "Management: 80 % feels better than 50 %"
date: 2011-11-05
updated: 2018-12-26
theme: leadership-and-management
labels: [Agile]
source: https://visible-quality.blogspot.com/2011/11/management-80-feels-better-than-50.html
---

# Management: 80 % feels better than 50 %

*Published 2011-11-05, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2011/11/management-80-feels-better-than-50.html>*

---

I never feel too good going back to Quality Center for the tests we just did, but this time we managed to use it so that it did not cause us too much trouble.  
  
Our "test cases" in the test plan, are types of data. A typical test case on average seems to have 5 subdata attached to it. All in all, a lot of our planning was related to understanding what kinds of data we handle in production, what is essentially different and how we get our hands on that kind of subset.  
  
We had two types of template tests in use for the steps:  

- Longer specific process flow descriptions: basically we rewrote the changes that were introduced in the specification in detail in minimum number of workflows, and ended up with about 40 steps, and 5 main flows.
- Short reminders of common process flow parts: these had 5 steps and just basically mention the main parts that the system needs to go through, little advice for the testers.

Our idea was, that for the first tests we run, we support the newcoming testers with the longer flows. And when they get familiar (they have the business background, it doesn't take that much), we enable them to do things in exploratory fashion with the feeling of being in service role towards own colleagues - it's an internal system.  
  
Before we started testing, I took a look at the documentation, numbers and allocated time, and made a prediction. We'd get to 50 % measured against the plan in the timeframe. After the first our of five weeks, we were at 4 %, and I was sure we'd stay far behind my pessimistic prediction.  
  
We also needed to split the tests in Plan to 5 instances of the test in Lab, to make sure we would not end up showing no progress or being inable to share the work in our team, as one of the things to test were potentially a week worth of work. We added prioritization at this point, and split things so that one of the original test cases could actually be started on week one to be completed on week 5 - if it would ever be completed.  
  
We did our finetuning while testing, moved from the detailed cases (creating more detailed documentation on what and how we were checking things) to the general ones, and with face-to-face time talking on risks we cut down each actual test run in different way, basically building together understanding of the types of things we had already seen and could go with the risk that it may not work but we won't bother, since there's stuff that is more relevant to know of right now.  
  
With notetaking, I encouraged the testers to write down stuff they need but taught that blank means nothing relevant to add. They run the tests in QC lab and made notes there in the steps. The notes we write and need are nowhere near the examples that go around session-based test management.  
  
The funny part came from talking with some of the non-testing managers, when they compared my "50 % is where we will get" to the end result of getting to 80 % as the metric was taken out from quality center. It was (and still is) difficult to explain that we actually did end up pretty much on the level I had assumed and needed to cut down about half of what we had planned for, we had just decided we'll cut out random amounts of each test, instead of something that they decided to assume was comparable.  
  
Yet another great exploratory testing frame with the right amount of preparation and notetaking. And yet, with all the explaining of what really happened, management wants to think there was a detailed plan, we executed as planned and and the metric of coverage against plan is relevant.
