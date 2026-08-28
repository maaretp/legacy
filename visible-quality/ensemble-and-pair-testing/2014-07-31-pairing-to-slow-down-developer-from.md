---
title: "Pairing to slow down a developer from starting new items"
date: 2014-07-31
updated: 2017-07-23
theme: ensemble-and-pair-testing
labels: [Pairing]
source: https://visible-quality.blogspot.com/2014/07/pairing-to-slow-down-developer-from.html
---

# Pairing to slow down a developer from starting new items

*Published 2014-07-31, updated 2017-07-23 · Labels: Pairing*  
*Source: <https://visible-quality.blogspot.com/2014/07/pairing-to-slow-down-developer-from.html>*

---

My last two posts have been about small batches and crazy reasons that make small batches take a long calendar time. As usual, I wasn't happy with just saying I don't like how things were, I needed to try something different.  
  
First, I sent an email to the developer and our manager suggesting that I have two ideas of how to slow the developer down after done-without-testing as I felt that taking another task when this one was not yet really done was premature and source of problems. I suggested to:  

1. Allow the developer to spend time studying instead of moving to another interesting feature he would not like to come back from. In general, the option of just moving to another task should be less tempting and the realization of getting quickly back to the thing that isn't yet done should remain the priority.
2. Make the developer responsible for the testing task following the development task, with the realization that he will need to invite me to pair up with him to do it well enough for now.

The option to choose between the two wasn't real. Number 2 was the only real option. Number 1 was to emphasize that we actually were supposed to have a rule on limiting work in progress.  
  
So today, the developer walked up to me first time asking me to test with him. So far I've been the one polling for a proper time and done that way too rarely. We sat down with two computers and two browsers, and started testing.   
  
With all the issues fixed from last round, I asked if he was confident in the feature now. He said he wasn't - because there was always something I would see that he just didn't. We talked about the starting choices of what to do first and why, and he seemed a bit puzzled on my way of thinking - the problem area seemed more condensed to him with less links around the product.  
  
We found problems in the changes he had just made, and we went through how it should work in different scenarios testing it through. He would take a pause from testing, fix things in code and deploy a new version that made things better.  
  
When he seemed to think we were done, I wanted to try a few more things. Just because I just thought they could be connected and I had not tried them yet. We found problems specific to IE9 and how data (unneeded null values) got saved in editing scenarios. We learned that there was a connection to history feature that was forgotten during development and did not work. And that there's a multiple selection feature that this feature wasn't compatible with.  
  
With a few hours of testing, we looked at the problems we now knew and agreed it would take a bit of time to come up with how to deal with them, and alone time might be useful. Before we parted, we still tested the other feature he had been working on that left me waiting on Monday and found no issues. And agreed we'd spend an hour together on each feature he completes from now on, because it's just more efficient and fun.  
  
Need to keep reminding the developers that they can't outsource quality to me. Even if they know I will find problems they miss, that just isn't acceptable approach. Collaboration is good.
