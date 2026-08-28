---
title: "Assignments in Intent"
date: 2018-02-23
updated: 2018-12-26
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/02/assignments-in-intent.html
---

# Assignments in Intent

*Published 2018-02-23, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/02/assignments-in-intent.html>*

---

We're testing a scenario across two teams where two major areas of features get integrated. In a meeting to discuss testing some of this in end to end manner where end to end is larger, we agreed the need to set up a bunch of environments.  
  
"Our team sets up 16 windows computers in the start state" seemed like an assignment we could agree on.  
  
Two days later, I check on progress. I personally installed 3 computers on top of what we agreed to be what my team would do, and was ready to move on to using the computers as part of the scenario. The response I get is excited confirmation of having the rest of them available too.  
  
The scenario we go through has a portal view into the computers installed, and checking if the numbers and details add up, I quickly learn that they don't. Ones I set up are fine. All others are not fine. We identify the problem ("I forgot a step in preparing the environment" and "It did not occur to me that I would need to verify on system level that they are fine") and agree on correcting them.  
  
Two days later, I check again. It has not been corrected. So I ask where we are, to hear that we are ready, which we are not. Containing the mild steam coming out of my ears, I ask if they checked the list in which they could see things are fine from a system perspective and I get explanations ("I don't have access", "I did not know I have access").  
  
Another day passes by and I realize there's a holiday season coming up, so I check again. They are not fine, but "they should be". I ask for a list of the computers, to learn there isn't one. And I spend a few days tracking the relationship of the IP (given by DHCP, changes over time) as the only info given, matching them to image names and actual statuses of getting things to work.  
  
The assignment was made in intent. No clarifying questions were asked. Given solutions, instructions were being dismissed. Learning did not show up in the process with repeating patterns. And finally, there was no consideration for the handoff that was evident for the planned vacation.  
  
This is the different between a trainee and a senior. Seniors see things and track things others don't.  
  
Today I'm enjoying the results of this prep, finding some really cool bugs having guessed some places where it would be likely to break. Having these issues now and having them soon vanish, knowing that my mention of them here is all I have to show is deeply satisfying.
