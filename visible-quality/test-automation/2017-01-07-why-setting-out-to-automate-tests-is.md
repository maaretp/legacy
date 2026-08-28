---
title: "Why setting out to automate tests is a bad idea"
date: 2017-01-07
updated: 2017-07-23
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2017/01/why-setting-out-to-automate-tests-is.html
---

# Why setting out to automate tests is a bad idea

*Published 2017-01-07, updated 2017-07-23 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2017/01/why-setting-out-to-automate-tests-is.html>*

---

On Thursday at work, a colleague was doing a presentation I had invited, on how they've been automating their tests. Organizing sharing sessions comes naturally, both from me being curious and knowing where to find all the best stories, but also from creating an atmosphere of sharing and learning.  
  
As his story is starting, he tells us he needs to explain a few things first. He spends maybe 30 seconds on explaining why finding a way to automate was so needed (malware evolves fast and when you're responding to something like that, you will need to evolve fast too). But then, he spends 20 minutes talking about things most people in the room, identifying as quality engineers, have never done. He speaks of recognizing problems with being able to test, and finding the best possible programmatic solution.  
  
He talked on how they introduced blue-red deployments within the product (without even knowing it was a thing outside windows client software) and how that solved all sorts of problems with files being locked. He shared how they changed, bit by bit, the technical designs so that the whole installation is rebootless because it was just hard to automate stuff that would need to continue after reboot. Example by example, his story emerges: to automate testing, they needed to fix testability. And that just adding tests when you have big problems that are hard to go around when you can change the product makes little sense.  
  
The story makes it clear: to be effective in this style of testing, you should be able to program outside of the tests you're programming, and if you can't, team up with someone who can. Without the view of solving problems programmatically where they make the most sense (design vs. tests), you would be on a path to difficulties.  
  
For a room for of test automators who barely look into the application code, his message may have been intimidating. Setting out to automate test (as in this is what I want to test, designs don't change) is often an invitation to trouble.  
  
Make it first simple to test, then a simple test to test it. The first is much harder. And I find that most of the repurposed manual testers becoming test automators without caring for product structures to make "manual" testing easier are hitting this trap harder than exploratory testers who have been working with the friends with pickup trucks (programmers) all along.
