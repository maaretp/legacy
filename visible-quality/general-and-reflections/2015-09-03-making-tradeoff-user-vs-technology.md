---
title: "Making a tradeoff, user vs. technology"
date: 2015-09-03
updated: 2016-04-26
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2015/09/making-tradeoff-user-vs-technology.html
---

# Making a tradeoff, user vs. technology

*Published 2015-09-03, updated 2016-04-26*  
*Source: <https://visible-quality.blogspot.com/2015/09/making-tradeoff-user-vs-technology.html>*

---

In the last few weeks, there's been an ongoing discussion at my work about a particular feature. As we finally had the discussion with the right people all in the same room, we finally came to a conclusion. And I tweeted:  
> Interesting discussion about decisions: can reasons of technology really drive us to create significantly worse user experience?
>
> — Maaret Pyhäjärvi (@maaretp) [September 1, 2015](https://twitter.com/maaretp/status/638602110771326976)

Let me share the backstory to this.  
  
The feature we've been discussing about is sort of the core of the user experience with the product we're building. I've never seen it as anything complex or complicated. It's a user interface to add in particular data. It was the first thing we implemented (that much of a core) and it's been enhanced based on user feedback, e.g. with keyboard use. It's founded on a component we call "old grid" - a free open source component, that just recently decided the next versions would no longer be free to use.  
  
Some months ago, we were implementing another feature and decided to take in a new technical component "new grid" from one of the commercial vendors. We already knew our current "old grid" turned commercial, and it appeared there was a better one available from someone else.  With the idea of replacing "old grid" with "new grid", we included it as an integral part of the new thing.  
  
As the feature came together and could be tested, both myself and the end user representatives voiced out concerns that the functionality on top of the "new grid" wasn't giving particularly good user experience. There were two clicks on things where one was sufficient before. There was uncertainty about what part exactly could be editable. And there were difficulties coming up with a way to get things to be as good as they were with the "old grid".  
  
As components are code, you can always change how they work. But changing something to work in a way that it was not intended tends to end up, from a technical team perspective, into a maintenance nightmare. Every upgrade is major reimplementation. And the ways to change things are often awful hacks that barely stay together. We looked, and while changing would be possible, it would not be easy. Awful hacks are not welcome.  
  
We had already bought the component. We had not only bought the component, but coded it into a complicated feature that wasn't now good enough. We had discussion-wise committed to taking the same component everywhere in the product, lowering the user experience with the core feature too.  
  
So it was time for the discussion on what we would do. We had reasons of technology to use the component we had and extend its use without creating awful hacks - hacks that we felt are theoretically possible and could just make things worse. We had the user experience to consider.  
  
All the ways to build the thing we needed without an awful hack ended up as worse user experience. We were very close to deciding that this would be the case. But we ended up, to my surprise, with adding the awful hack (and considering changing component to something that would do what our users need).  
  
We also checked with the component vendor.  
> "Forcing the Grid to be in edit mode at all times is not supported out of the box and adding such feature is not planned. You can achieve similar behavior using ... however such custom solutions have certain drawbacks and negative performance impact."

I've had similar discussions before. In the tradeoff, the user experience often loses. Technology and "things that can't be done" wins. Can't be done includes a component of cost, with work to implement - and in this case, reimplement. But so does user experience in the wasted time for the users.  
  
The whole discussion was somewhat of a comedy to watch. In a team of people who all agreed to listen to the users and not feed them with things they did not want, we stopped one with a leading question to only have another one with a leading opposite question jump in. With all the different leading questions in the table, we got the honest answers though. And I believe we made the right decision, even if it was different from the decision we made three months ago with different knowledge and understanding.  
  
I'm still hopeful that with smart people in the development team the "awful hack" will end up as little less awful.
