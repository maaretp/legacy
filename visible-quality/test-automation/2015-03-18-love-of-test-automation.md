---
title: "Love of test automation"
date: 2015-03-18
updated: 2017-07-23
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2015/03/love-of-test-automation.html
---

# Love of test automation

*Published 2015-03-18, updated 2017-07-23 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2015/03/love-of-test-automation.html>*

---

I've always been big on sapient, thinking testing. Thinking testing includes smart use of tools, to extend your reach to whatever you cannot do without. But I've also been very sceptical about value of automation with regards to the overall value you get from testing in general. And I've played well with the developers in my team to have ideas they will help me implement, allowing me to focus less on the programming stuff myself.  
  
Some organisations I've worked with have put a significant effort into regression test automation, with poor results. If there is regression, the automation does not catch it. It is always in the wrong place. It eats up effort to maintain to remain useful. And it might not have been as useful as its cost in the first place. One of my "most successful test automation" experiences in an organisation for years was automation that did not test anything but allowed the organisation to have the courage to dump the manual tests they had listed - being very proud of lack of regression in production. That's a success story of exploratory testing and great development team. Automation played only the part of changing cultural elements that prevented good work.  
  
But recently, as much as I may dislike it, I've started seeing little pieces of evidence that conflicts my core beliefs about test automation. And being a good researcher (empirical evidence FTW), I cannot just close my eyes from them.  
  
**My work and how I see it**  
  
I love testing. But over the years, I've started to realise that I love software more than I love testing. The things we do with software are amazing. The business we build on software are enchanting. When I choose places to work in, I ask a lot about the value of the software I would be contributing to. Testing does not exist for testing. I would not choose to work on a product I did not believe had potential to be financially feasible, valuable, meaningful.  
  
To increase the value, more and more places are seeking into ways of shorter delivery times, incremental value. And this is great, from the point of view of loving testing it enables someone actually caring for the information testing provides, when there's points where the feedback can steer without being disruptive to other goals.  
  
With incremental deliveries, in comes the question of repetition in testing. I've been fortunate to work with teams where "everything that used to work breaks" is not the norm. Developers have been pretty good at dealing with that. They have often dealt with it by thinking hard and long, as they have not had (unit) test automation to support them. And with hard thinking combined with understanding of domain and reading of code, the side effects are not the main effects. The large numbers of issues to deal with result more from developing new features that are not quite there yet.  
  
I've now spent almost three years with the same product and team. I blogged earlier about the idea that [I don't run the same tests](http://visible-quality.blogspot.fi/2014/09/why-would-i-do-regression-testing.html) but always vary things to find new things while having a good chance of noticing the old things too. Believing I don't run the same tests and actively working so that I don't is a core to staying awake and alert. This reminds me on [an article by Bret Pettichord on Testers and Developers thinking differently](http://www.jmc.gov.jo/uploadedfiles/documents/607a7de5-d674-4121-b0c9-b305f5d73345.pdf) and one of the tester strengths, tedium toleration. Thinking the way I do is my way of dealing with repetition and the risk of being bored - I reframe. But three years is slowly starting to get under my skin. I've found great things for wanting to use the product in versatile ways, things that automation could not find. I would look at most of the same things even if automation existed. I could only hope to stop for different problems, or take more risks in just not using some things for now at all. Could experiment more with not testing instead of different testing for the same areas.  
  
From an organisational point of view, I must seriously think if my organisation would be better off in long run if they had more automation (and much much more broken product in production). Especially when I'm gone, and they may not have the skill to find another great tester to join them as there's forces driving "documented test cases" unless you really have a vision of what better in testing looks like. With the same effort, could I or should I have chosen a different path if my own interests wouldn't drive me to exploratory testing?  
  
Recently, we've updated pretty much the whole technology stack - every feature relies on new dependencies. We've rewritten things for better maintainability (still without proper unit tests, which is why I call it rewrite instead of refactoring) so that features are not the same implementation as they were before. We do these changes one thing at a time, continuously, requiring continuously testing. And with these styles of changes, the developers start introducing regression by losing features / scenarios we are surpassingly supporting.  
  
Right now I'm sure that since a lot of the features we are losing make sense to me with product experience, the company would not be in a good state when I manage to leave - something both me and they know will happen sometime soon enough. So putting the list of features into a living specification that resides there, in test automation is an effort we're getting deeper into.  
  
You can't have it all, but the choices in the order of things are beliefs. And seeing where the beliefs take us is just interesting.  
  
**A friend with great results**  
  
A friend I look up to has been working recently with automating tests from a specific idea. The idea as such is old: the vast number of environments that mobile applications bring in is a special challenge. The product in testing is a financially successful, established business. So it is clear they too could not only survive, but thrive to this point without automation that covers such a critical aspect of testing.  
  
What seems to be different though is that unlike before, there is now a chain of services that makes ideas like this more practical. Imagine supporting all the different smart phones out there - there's more coming in as I write this. Instead of having a farm of your own you carefully select, what if someone's business is actually running the virtual farm for you? The same idea has been wonderful with browsers, and to me makes even more sense in the handhelds world. And yes, I love Finnish startups.  
  
Using a virtual farm to run the automation on and seeing the actual valuable results from even the very simple "let's see the app launches" types of tests cross platform left me in awe. We can really do things like this. Things that are useful. I just wish she can show the world the great things they've accomplished. But things like this - from other sources too - make me question my stance on things.  
  
The test automation we did 10 years ago isn't the test automation we do today. Old experiences may be invalidated with what has changed around us. For some organisations at least.  
  
**Reminders of the world changing**  
  
A week ago, I listened to a discussion about teaching kids programming. There was a point in discussion that left me thinking: developers all around the world are taking software into areas it has never been before, doing unseen things with it. Some of the data that is currently being collected, will be used in ways we can't yet foresee. The world has many smart people, putting serious effort into (partially) transforming human-intensive processes with automation. Programming is just automating things.  
  
With automation of any kind, the existence of smart thinking individuals does not completely vanish. But it transforms. I've enjoyed reading about the google car that actually cannot cope with change in the driving settings as calculations to be fast enough rely heavily on built-in maps of the area the car operates on. But those things still are driving around, and problems related to those are being actively thought of.  
  
Perhaps, just perhaps, I should start more actively thinking about how can I as an exploratory tester put more effort into helping my team turn more and more aspects of testing into programmable decision rules. Full automation or partial automation, but forward a step at a time. I find great value in taking steps away from programmatic thinking, seeing things differently.  
  
With these thoughts, it's time to go back to reading Cem Kaner's partial oracles materials. Great testers could help make sense in better partial oracles for automation so that we get closer to good results from a testing point of view with the automation efforts. Regression is such a small concern in all of this.
