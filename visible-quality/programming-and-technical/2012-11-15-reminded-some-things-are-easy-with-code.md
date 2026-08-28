---
title: "Reminded: some things are easy with code"
date: 2012-11-15
updated: 2017-07-23
theme: programming-and-technical
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2012/11/reminded-some-things-are-easy-with-code.html
---

# Reminded: some things are easy with code

*Published 2012-11-15, updated 2017-07-23 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2012/11/reminded-some-things-are-easy-with-code.html>*

---

As part of my usual routines, I reviewed problems found recently in the versions that have been released to production. I noticed one in particular, where it was evident that this one is a recent introduction of a problem in something that used to work.  
  
In particular, we introduced in the latest version a feature for our combo boxes, to make a selection of all vs. none with one click. The change wasn't very large in development size, and as it was not considered very risky (still isn't), I tested it by sampling some of the combo boxes, focusing on ones the developer was more unlikely to check as they were not in his own area of responsibility.  
  
The issue found in the production version by one of our product managers - not by the customers who don't seem to complain about things more relevant than this. The issue was that one of the combo boxes in his area showed more items than the count would tell - the count was always one lower.  
  
From seeing the bug report, it was quite easy to tie the connection. We just changed the combo boxes, and then one of them doesn't work as before.  
  
I talked about that with two developers, one who changed the combo box and one whose area had the combo box that was causing the trouble. We looked at that piece of code, to notice that the call for the combo box was not implemented as instructed. A simple one-liner to fix.  
  
My first reaction was thinking how we could have tested better, to realize this particular combo box was different. Right after that thought, I realized that there was nothing that told us that this one was the only different one. So, already next to the code, I asked if this was elsewhere. With few clicks, I was told there was 686 mentions of the method in the code, and a comment to just give five minutes and I could have my answer.   
  
Five minutes later, I had learned that that was actually the only one left with that particular problem. There had been another one identified during the month, and fixed. But no one asked the question if this was also elsewhere, so we failed to learn all the things we could / should from a sample.  
  
This reminded me of two lessons I seem to keep forgetting:  

- Some things you shouldn't test for with the software, there are just easier routes to find the information you're looking for.
- Encouraging people to address a family of problems instead of the mentioned problem is something that needs emphasis.

When I shared this story to a more distant colleague, the first reaction was that test automation could have caught this. I think not - we wouldn't have automated a check for all the 200 + combo box instances for this particular problem. Instead, we could easily ask if there was something other than testing with the software that would help us understand if it could fail. And a combo box that has always been a problem because it's sensitive to exactly right way of calling was a piece of information that we would have been able to use, if we worked more as a team and less as individuals each doing their separate responsibility.
