---
title: "Feature and Release Testing"
date: 2020-05-23
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2020/05/feature-and-release-testing.html
---

# Feature and Release Testing

*Published 2020-05-23*  
*Source: <https://visible-quality.blogspot.com/2020/05/feature-and-release-testing.html>*

---

Back in the day, we used to talk about *system testing*. System testing was the work done by testers, with an integrated system where hardware and software were both closer to whatever we would imagine having in production. It usually came with the idea that it was a phase after unit and integration testing, and in many projects *integration testing* was same testing as system testing but finding a lot of bugs, where system testing was to find a little bugs and *acceptance testing* ended up being the same tests but now by the customer organization finding more bugs that what system testing could find.  
  
I should not say "back in the day", as for the testing field certification courses, these terms are still being taught as if they were the core of smartassery testers need. I'm just feeling very past the terms and find them unhelpful and adding to the confusion.  
  
The idea that we can test our software as isolated units of software and in various degrees of integrated units towards a realistic production environment is still valid. And we won't see some of the problems unless things are integrated. We're not integrating only our individual pieces, but 3rd party software and whatever hardware the system runs on. And even if we seek problems in our own software, the environment around matters for what the right working software for us to build is.  
  
With introduction of agile and continuous integration and continuous delivery, the testing field very much clung to the words we have grown up with, resulting in articles like the ones I wrote back when agile was new to me showing that we do smaller slices of the same but we still do the same.  
  
I'm calling that unhelpful now.  
  
While unit-integration-system-acceptance is something I grew up with as tester, it isn't that helpful when you get a lot of builds, one from each merge to master, and are making your testing way through this new kind of jungle where the world around you won't stop just so that you'd get through testing that feature you are on on that build you're on, that won't even be the one that production will see.  
  
We repurposed unit-integration-system-acceptance to test automation, and I wish we didn't. Giving less loaded names to things that are fast to run or take a little longer to run would have helped us more.  
  
Instead of *system testing* I found myself talking about feature/change testing (anything you could test for a change or a group of changes comprising a feature that would see the customer's hands when we were ready) and release testing (anything that we needed to still test when we were making a release, hopefully just run of test automation but also a check of what is about to go out).  
  
For a few years, I was routinely making a checklist for release testing:  
  

- minimize the tests needed now, get to running only automation and *observing automation running* as the form of visual, "manual" testing
- Split into features in general and features being introduced, shining special light to features being introduced by writing user oriented documentation on what we were about to introduce to them

From tens of scenarios that the team felt that needed to be manually / visually confirmed to running a matrix test automation run on the final version, visually watching some of it and confirming the results match expectations. One automated test more at a time. One taken risk at a time, with feedback on its foundation.

Eventually, release testing turned into the stage where the feature/change testing that was still leaking and not completed was done. It was the moment of stopping just barely enough to see that the new things we are making promises on were there.

I'm going through these moves again. Separating the two, establishing what belongs in each box and how that maps into the work of "system testers". That's what a new job gives me - appreciation of tricks I've learned so well I took them for granted.
