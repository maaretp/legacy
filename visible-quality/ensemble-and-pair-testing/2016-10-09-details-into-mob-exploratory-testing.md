---
title: "Details into Mob Exploratory Testing"
date: 2016-10-09
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Mobbing]
source: https://visible-quality.blogspot.com/2016/10/details-into-mob-exploratory-testing.html
---

# Details into Mob Exploratory Testing

*Published 2016-10-09, updated 2017-07-22 · Labels: Mobbing*  
*Source: <https://visible-quality.blogspot.com/2016/10/details-into-mob-exploratory-testing.html>*

---

I love exploratory testing, and have a strong belief in the idea that exploration can have many paths to go forward and still end up in great testing. Freedom of choice for the tester is a relevant thing, and I've grown to realize I have a dislike for guidelines such as "find the happy path" first when exploring.  
  
Surely, finding the happy path is not a bad idea. It helps you understand what the application is about and teaches you about putting the priority of your bugs into a context. It gives you the idea of "can this work", before you go digging into all the details that don't work.  
  
I've had to think about the freedom of choice more and more, as I'm doing exploratory testing with a mob. While I alone can decide to focus on a small piece (and understand that I don't know the happy path and the basic use case), people who join a testing mob are not as aware of the choices they are making. People in the mob might need the frame of reference the happy path gives to collaborate. For me, each choice means that it enables something but also leaves something out. Playing with the order of how I go about finding things out can be just as important for my exploration than getting the things done in the first place.  
  
For example, I often decide to postpone reading about things and just try things out without instructions, recognizing documentation will create an expectation I care for. I want to assess quality in the experience of use both without and with documentation, and unseeing is impossible. Yet, recognizing documentation reading matters, I can look at the application later too trying to think of things (with my mind map there to support me) simulating the old me that had not read the documentation.  
  
My latest mob I lead, I ended up with a more strict facilitation. I asked the questions "what will you do next?" and "what are you learning?" much more than before, and enforced a rule of making quick notes of the agreements and learning in the mind map.  
  
When the group got stuck in thinking about a proper phrasing of a concept in the mind map or location of an idea, I noticed myself referring to rules I've learned around mobbing on code. Any name works, we can make it better later, "just call it foo" and learn more to rename it. Any place in the mind map works, we can rearrange as our understanding grows, we don't need to do it at the time we know the least.  
  
Finally, I was left thinking about a core concept of mobbing around code: intentional programming. The shared intention of what we're implementing, working in a way where the intention does not need to be spoken out about, but the code shows it. Test-driven development does this in code, as you first define what you'll be implementing. But what does it in mob exploratory testing?  
  
Working from a charter is intentionally open-ended and may not give the group a shared intention. Even a charter like "Explore Verify(object) with different kinds of objects and contents using Naughty strings -list to find inconsistent behaviors" isn't enough to keep the group on a shared intent. The intent needs to be worked out in smaller pieces of the test ideas.  
  
Looking at this group, they often generated a few ideas at a time. Making  them write those down and execute them one by one seemed to work well on keeping them coherent. So, it looks like I had not given enough credit for the mind map as a source of shared intent for group exploration.
