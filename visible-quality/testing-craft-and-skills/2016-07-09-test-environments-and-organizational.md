---
title: "Test environments and organizational aspects"
date: 2016-07-09
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/07/test-environments-and-organizational.html
---

# Test environments and organizational aspects

*Published 2016-07-09*  
*Source: <https://visible-quality.blogspot.com/2016/07/test-environments-and-organizational.html>*

---

Once upon a time there was this project I was on. It was a significant system, multi-million euros for each layer. To simplify, there were three main layers.  
  
The bottom layer had a bunch of legacy services for accessing decades of data from massive databases owned by various parties. There was decades of complicated data, which represents history of lifetime of millions of people.  
  
The middle layer was a calculator. It accessed the legacy services to get to the data, and twisted it around for particular types of decisions and summary information.  
  
The top layer had extensive business process logic and all sorts of user interface and batch processing functionality, representing what the organization I worked with wanted to use the data on.  
  
The system had a lot of contractors. A lot, as in tens of them. The middle layer was contracted from one, and top layer from another.  
  
As contractors tend to come, everyone was very much into their responsibility only. I routinely negotiated the amount of testing that the middle layer and top layer contractor could do with mocks/stubs, as they would have loved to keep their life isolated from everyone else. Requiring that the contractors would partially test with an integrated system usually meant we paid more, unless we had understood to specifically require it early on. And often we had not.  
  
When we'd allow testing with mocks/stubs only, we experienced two main problems: 1) the parts of the system wouldn't work integrated as some changes were not compatible after all, and we'd learn this late. 2) the mocks/stubs required maintenance, and the contractors would minimize the testing they did with those, making the testing not representative in the first place.  
  
The stubs gave a lot of good too. They helped keep systems isolated and tested in isolation. They allowed for scrambling data so that a lot of the work could be done outside EU area. They made for very practical ways of noticing when the interface contract was unexpectedly changing, comparing the messages that were expected and received.  
  
We put a lot of effort into figuring out ways of making this easier. Thinking about it I remember in particular design discussions we had around a hardware router box with a 1M price tag, that could run us fast transformations with more complicated logic on what to get and when.  
  
There was a lot of negotiating in trying to get the pieces to match, with everyone sticking to the idea that they knew exactly what their corner was supposed to be. It often felt we were the only ones actually concerned the system as a whole would work.  
  
Sometimes when I look at the stuff people talk around test automation, there's this idea that whatever is needed is immediately possible. Or that there's massive amount of people you can somehow get on the problems.  
  
Context-driven testing means to me that I end up with all sorts of situations. Sometimes I can't buy new hardware.  
  
It took me 3 years to get extra IBM mainframe for our test environment, but I got it. Another 1M. Just installing and configuring it was almost a year-long project. Meanwhile, we did magic with choosing our risks and working around anything we couldn't isolate.  
  
I still don't have a duplicated production environment for my current project, and seems 3 years will not be enough to win that argument. Believe me, I've tried.  
  
It took me 6 months in one of the more agile companies I've worked with to get the test lab upgraded to be available with fastest available network connection (the switches cost some money, people are already paid for), regardless of how much time moving the test images over slower network would eat up.   
  
When people talk about all the cool new technical ways of delivering software without downtime, I still work on organization being willing to invest in the infra that would enable this and organization being willing to find new ways of understanding how good testing could get done, over following the responsibility aversive plan they made 2 years ago.  
  
Companies and what is possible are hugely different. That's why context is relevant. We can still do great job when the companies are not all the way in to the technological advances the field has to offer.
