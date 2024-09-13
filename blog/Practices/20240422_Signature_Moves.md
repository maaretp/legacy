# Learning the hard way, experience

Over my career, I have done my fair share of good results in testing. There are two signature moves I wanted to write a post on, and what I learned while failing at both of my two signature moves after I first thought I had them pocketed. 

These two signature moves are changes I have been driving through successfully over multiple organizations and teams: 

* Frequent releases

* Resultful contemporary exploratory testing with good automation at heart of it

## Frequent releases

Turning up the release frequency is an improvement initiative I have done now for over 10 different teams, products, and for four organizations. And the products/teams/orgs I have done this at, only of them are the optimal case of a web application with control over distribution channels. I've been through this the hard hard way - removing reboots from upgrade cycles, integrating processes that were designed for non-continuous such as localization and legal,  including telemetry to know if we leave customers hanging on versions - all of that is an article of its own. 

Succeeding with this is not the interesting part, except for the latest success of my current team making releases routine after dropping the ball and suffering through a 4 month stabilization period last year. I dare to call it again a success since we made our 5th release this year last week, and included the best scope and process we have had in that. 

Why did we fail with a stabilization phase then? We can surely learn something from it. 

The experiences point us to failing at communicating and collaborating with a non-technical product owner. How can that create a four month stabilization phase? Leaking uncertainty, and pushing uncertainty to a time it piles up. We leaked uncertainty in functional scope, but also in parafunctional scope, and when pushed to address performance and reliability, we found functional scope we had not recognized existed. 

From breaking the main and not realizing how much we had broken it (automation was still passing!) cost us extra stress and uncertainty. We would look at tasks as "I did what you asked", not as "We together did what you did not know to ask". 

And when we tested, we failed at communicating our results effectively. New people, new troubles, and they accumulated quickly when we did not want to stop the line to fix before moving forward. We optimized for keeping people busy, over getting things done to a shape where they could be released.  

Having my team fail with my signature move taught me that there is much more of implicit knowledge on continuous timely testing than what we capture with automation. Designing for feedback, and making it timely takes learning, and this year we have been learning that with a short leash of releases.

## Resultful contemporary exploratory testing with good automation at heart of it

Framing test automation as worthwhile notetaking mechanism while exploring has become so much of a signature move of mine, that I have given it a label of its own: contemporary exploratory testing. When we explore, some of it is attended and some unattended. Test automation, when failing, calls for us to attend. Usually pretty much continuously. 

Working with developers, we have learned to capture our notes as lovely English sentences describing the product capabilities in some tests; as developer intent captured in unit tests in some tests; as component tests ad as subsystem, and as system-of-systems tests when those make sense. We have 2500 tests we work with on the new tech stack side, some hand-crafted, and others model-based generated test we use as reliability tests allowing longer unique flows be generated and tracked.

We learn about information we have been missing, and we extend our tests as we fix the problems. We extend the tests with new capabilities. How can all this successful routine be a failure?

It turns out there was a difficult conversation we did not have on time, one of validation. And when a problem is that you are building your product so that it does not address the user needs, none of the other tests you may have built matter. Instead of being a help, they become friction where you will explain how changing those all will be work, at a time when work is less welcome. 

This failure comes from two primary sources: carefulness on a cross-organizational communication due to project setup reasons delaying the learning, but as much as that, unavailability of more senior test/dev folks on a previous project delivery. 



Both the two failures are successes if we learned and can apply what we learned going forward. For me they taught a career change is in order: I don't want to find myself spread so thin that I don't recognize these expensive mistakes happening. So I will be a tester again, fully. Well, surrounded by testers, as director, test consulting, with a hands on consulting role starting June. Looking forward to new mistakes, and correcting the mistakes I make. Because: mistakes were made, and by me. Only taking ownership allows us to move forward and learn. 

* recommendation of a book: 

> Mistakes were made (but not by me) - Carol Tavris & Elliot Aronson