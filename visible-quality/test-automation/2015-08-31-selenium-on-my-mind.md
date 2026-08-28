---
title: "Selenium on my mind"
date: 2015-08-31
updated: 2017-07-23
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2015/08/selenium-on-my-mind.html
---

# Selenium on my mind

*Published 2015-08-31, updated 2017-07-23 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2015/08/selenium-on-my-mind.html>*

---

Selenium Webdriver has been the theme of my week - a theme that would appear to continue because I choose to continue. I’m struggling with my feelings about this, as I find working on the test automation the most boring part of my work I could volunteer on. But I volunteer to investigate deeper how I think while testing this way (working with tests as artifact focus) and how I think while testing the usual way (working with improvisation on the application with tests as performance). I have a working theory that I’m seeking evidence against: that I find more complicated yet relevant bugs when exploring without the form of artifacts keeping me on a leash. As a sort of corollary, I’m investigating a claim that I don’t enjoy test automation because I’m not fluent in it, through becoming more fluent before dumping the activity - unless I change my mind on what I want to spend my life on.
  
  
In the last week, I’ve done pretty much all-Selenium activities. Mobbing Selenium tests with my whole team. Pairing with a summer intern on creating more Selenium tests. Group/pair activities have been helpful as they both fulfill my need of being social at work, but also keep me honest and progressing on task that really isn’t one of my favorites.
  
  
I seem to find some of my motivation from playing with the dynamics. While last week we focused our efforts into automating scenarios for existing features that should be monitored, today we experimented with focusing on a completely new feature I’ve never tested manually before.
  
  
I was navigating (fixed pairing style since last session and was much happier with the work) and while I had many scenarios on my mind, I chose first one that I’d like to see included in the tests. It was almost the simplest one, but with a twist: a theory of error, a hunch I find so common on what would be likely wrong.
  
  
The feature was tiny. We have a dialog that lists packages, where we have previously hidden all packages considered “ready” for a particular user role. We now needed to extend it to show the ready packages. To test this, we need to play with two different user roles to create different states of the packages that then should or should not be visible.
  
  
My first hunch was that if something was wrong, one thing that would be wrong is that there’s two types of “ready” packages, ones that are made visible for the other role and others that are not. And that’s what I chose as our first scenario. We clicked through it manually to note that there’s a bug. We laughed at my ability to guess priorities and decided to try out something a developer from outside our organization once suggested me: reporting a bug with a failing test. The little framing difference created just enough variance for me to get out of my general Selenium boredom that I fight, and we were progressing very nicely on automating. There was all the usual obstacles we see with finding the right things to wait on so that the test would run reliably, but those felt more of a thing we just keep seeing on the route.
  
  
When the test was done and we run it, it passed. We were expecting a fail with the last thing we were checking. The bug was not visible, although both of us knew it was there. So we started looking into steps of our test where we reused existing pieces and isolating the exact conditions that would cause this bug. We learned that the bug would show only if there was exactly one user of the other role to handle the package, and extended our page elements and test data to include differences in the scenario.
  
  
Looking back, we used about 5 times the effort on isolating the bug and reporting it this way over the usual “Jira issues” way. But we did not do this to save time, but to try our how it would feel.
  
  
As we finished the test, the developer whose implementation we were testing walked by and got excited about the failing test. He suggested pairing to fix the problem. I was just leaving with other things scheduled, but our summer intern - my pair of the day, volunteered to pair on with the fix. He seemed really happy with getting to work on the application instead of just the tests. Sad that it had to happen for the first time on his last day at work.
