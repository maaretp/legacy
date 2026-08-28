---
title: "Frustrations on system test automation efforts"
date: 2017-01-24
updated: 2017-07-23
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2017/01/frustrations-on-system-test-automation.html
---

# Frustrations on system test automation efforts

*Published 2017-01-24, updated 2017-07-23 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2017/01/frustrations-on-system-test-automation.html>*

---

For a tester who would rather spend her time not automating (just because there's so much more!), I spend a lot of time thinking about test automation. So let's be clear: people who choose not to spend their days in the details of the code might still have relevant understanding on how the details of the code would become better. And in the domain of testing, I'm a domain expert, I can tell the scopes in which assumptions can be tested in to a level I would almost believe them.  
  
Back in my earlier days, I was really frustrated with companies turning great testers into bad test automation developers (that happens, a lot!) and these days, I'm really frustrated with companies turning great testers away and rather hiring test automation developers. Closing one's eyes on what is the multitude of feedback that you might want while developing makes automation easier - yet just not quite the testing one may be imagining. One thing has changed from my earlier days: I no longer think of bad test automation developers as the end of those people, as long as they start treating themselves like programmers and growing in that field. It's more of a career change, benefiting from the old domain knowledge. I still might question, based on my samples, the goodness of domain knowledge of testing on many of the people I've seen make that transition. Becoming a really good exploratory tester is a long road, and often people make the switches rather sooner than later.  
  
Recently, I've been frustrated with test automation specialists with a testing background, who automate in the system / user perspective and refuse to consider that while this is a relevant viewpoint, a less brittle one might involve addressing things in a smaller, more technology-oriented perspective. That unit tests are actually full-fledged tests as an option to keep track of things that should work. That it is ok to test a connected system with a fake connection. And that it just doesn't need to be, when automation is on the plate, a simulation of what a real user would do. Granularity - knowing just what broke is more relevant.  
  
I believe we run our test automation because things change, and as a long-time tester, I care deeply what changed. I recognize the changes that my lovely developers do, and I have brilliant ways of being alerted both by them with a lot of beautiful contextualized discussions but also just seeing from tools what they committed. I read commit comments, I read names of changed files and their locations, and I read code. I recognize changes coming in to our environment from 3rd party components we are in control of and I recognize changes into the environments that we can't really control in any way.  
  
And while our system test automation works against all sources of changes, I prefer to think my lovely developers over my users with the test automation giving feedback. The feedback should be, for the developers, timely and individualized to the change they just introduced. A lot of times I see system test automation where any manual tester does the timely and individualized better than the system created for this purpose.  
  
Things fail for a reason. Build your tests granular to isolate those reasons.
