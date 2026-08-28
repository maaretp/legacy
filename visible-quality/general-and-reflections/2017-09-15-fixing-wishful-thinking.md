---
title: "Fixing Wishful Thinking"
date: 2017-09-15
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2017/09/fixing-wishful-thinking.html
---

# Fixing Wishful Thinking

*Published 2017-09-15*  
*Source: <https://visible-quality.blogspot.com/2017/09/fixing-wishful-thinking.html>*

---

There's a major feature I've been testing for over a period of six months now.  Things like this are my favorite type of testing activity. We work together over longer period of time, delivering more layers as time progresses. We learn, and add insights, not only through external feedback but also because we have time to let our own research sink in. We can approach things with realism - the first versions will be iterated on, and whatever we are creating is indefinitely subject to change.  
  
I remember when we started, and drew the first architectural diagrams on the wall. I remember when we discussed the feature in threat modeling and some things I felt I could not get through before got addressed with arguments around security. I remember how I collected dozens of claims from the threat modeling session as well as all discussions around the feature, and diligently used those to drive my learning while exploratory testing the product.  
  
I'm pretty happy with the way that feature got tested. How every round of exploration stretched our assumptions a little more, giving people feedback that they could barely accept at that point.  
  
Thinking of the pattern I've been through, I'm naming it Wishful Thinking. Time and time again with this feature and this developer, I've needed to address very specific types of bugs. Namely ones around design that isn't quite enough.  
  
The most recent examples came from a learning that certain standard identifiers have different formats. I suggested this insight should lead to us testing the different formats. I did not feel much of support for it, not active resistance either. I heard how the API we're connecting to \*must\* already deal with it - one of the claims I write down and test against. So I tested two routes, through a provided UI and the API we connect with, only to learn that my hunch got confirmed - the API was missing functionality someone else's UI on top of it added, and we, connecting with the API missed.  
  
A day later, we no longer missed it. And this has been a pattern throughout the six months.  
  
My lesson: as a tester, sometimes you work to fix Wishful thinking. The services you are providing are a response to the developers you're helping out. And they might not understand at all what they need, but appreciate what they get - only in small digestible chunks, timed with enforcing the message into something actionable right now.
