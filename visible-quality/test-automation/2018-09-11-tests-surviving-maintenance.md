---
title: "Tests Surviving Maintenance"
date: 2018-09-11
updated: 2018-12-26
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2018/09/tests-surviving-maintenance.html
---

# Tests Surviving Maintenance

*Published 2018-09-11, updated 2018-12-26 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2018/09/tests-surviving-maintenance.html>*

---

As we create tests to our automation suites, we put some care and effort into the stuff we are creating. As part of the care and effort, we create a visualization on a radiator on how this test is doing. The blue (sometimes yellow/red) boxes provide a structure around which we discuss making a release with the meaning of basic things still working.  
  
When something turns not blue and the person who created the piece of code is around, they usually go tweak it, exercising some more care and effort on top of the already sunk cost. But a repeating pattern seems to be that if the person who created the piece of code is not around, the secondary maintainer fixes things through the method of deletion.  
  
I had a favorite test that I did not create. But I originated the need of it, and it was relevant enough that I convinced one of my favorite developers (they're all my favorite, to be honest) to create it for me. It was the first step to have a script doing something a colleague was doing over long term, just opening the application and seeing if it was still alive.  
  
I cared for that test. So I tested what would happen if the machine died by letting the machine die.

> We had a piece of automation code that checked a machine remained alive. I let the machine die to see what happens. They deleted the piece of automation for failing.
>
> — Maaret Pyhäjärvi (@maaretp) [September 9, 2018](https://twitter.com/maaretp/status/1038756258906628096?ref_src=twsrc%5Etfw)

The test, like so many other tests, did not survive maintenance. Instead of bringing back the machine it was watching, the watcher vanished.  
  
As I mentioned this on twitter, someone mentioned that perhaps the test was missing clarity of intent. However, I think the intent was clear enough, but debugging for a vanished machine was harder than deleting the test. Lazy won. The problem might have been lack of *shared* intent, where people have the tendency of maintaining other people's stuff through deletion. The only mechanism I've seen really work on shared intent is mobbing, and it has significantly improved in previous cases the chances of other people's tests surviving maintenance.  
  
Lazy wins so easily. Failing tests that could prevent deploys - for the reason of them showing the version should not be deployed - get deleted in maintenance. It's a people issue, not a code issue.  
  
We need blue to deploy. Are we true to ourselves in getting our tests to keep us honest? Or do we let tests die in maintenance more often than not?
