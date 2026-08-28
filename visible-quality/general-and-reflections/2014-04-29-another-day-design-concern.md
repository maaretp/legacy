---
title: "Another day, a design concern"
date: 2014-04-29
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2014/04/another-day-design-concern.html
---

# Another day, a design concern

*Published 2014-04-29*  
*Source: <https://visible-quality.blogspot.com/2014/04/another-day-design-concern.html>*

---

I tweeted a Robert Martin quote from Clean Coder -book yesterday:  
  

*“It is the worst kind of unprofessional behavior to simply code from a
spec without understanding why that spec makes sense to the business"*

As a reply I got a kind note:

> [@maaretp](https://twitter.com/maaretp) And same goes for writing the spec :)  
> — Juha Heimonen (@evilbubu) [April 28, 2014](https://twitter.com/evilbubu/statuses/460873722795409408)

Thus it seems appropriate that I've spent most of today working on a spec, and feel I need to share a few experiences on that. There surely can be a lot of work embedded in the quote of avoiding unprofessional behavior.  
  
There's a new concept we are supposed to work on by the end of this year. As concepts and our experience goes, it tends to be a good idea to play with the concept before jumping into implementing it, to avoid the "implementing 2-3 times just because we did not focus to learn early" -syndrome typical for us.  
  
As usual, two people have had vivid discussions on building the ideas of what the concept / features would be about. They've drawn some pictures that help discuss it. Nothing is set in stone - except the fact that the business representative's calendar is very full, allowing us easy access to discuss with him once next week and then again in a month.  
  
From my initiative, two other people start looking into the draft specification: myself in whatever role I end up with, and a UI designer in as large a role he feels comfortable taking. The quick guidance is that we should discuss after we've read it - same assignment for the two of us.  
  
I read the document to realize that I would not advice implementing any of the stuff the way they've been sketched. The core concepts this builds on are concepts used elsewhere in the product for a completely different scope and meaning. Technically they seem to be suitable (filtering is a general idea), but the user visible concepts have implications that would make things difficult. And there's a new stick-it-on-top-of-the-others view just for this feature - while other features for same users would be elsewhere.  
  
I hint about the problems for the user interface designer, to learn that he read the document, but did not formulate his own view on that. He has a few ideas of how to present the described concepts in the user interfaces sketched, but had not noticed the concepts would not fit our overall idea of what the product is like. We agree from discussion that he'll take another look at the document based on my heads-up.  
  
I'd like to find a way to do two things:  

1. Build the skill of noticing when things don't fit the concepts we have in place. I think of this as seeing the system, and testing is a great place to build an overall view of what there is and how things belong together.
2. Learn to discuss concepts before they give the appearance of some higher-level decisions  are done. As much as I try, the specification by example -type of discussions don't seem to (yet) find their spot in the way we work. And there's more to understanding concepts than just the given-when-thens.

Just thinking about the amount and scope of questioning my dear developer colleagues would need to go through to qualify as professionals seems a lot to ask. So there must be a context-specific choice in play on how to distribute the responsibilities over the skills we have with a nice stretch that grows our skills by taking us out of the comfort zone.
