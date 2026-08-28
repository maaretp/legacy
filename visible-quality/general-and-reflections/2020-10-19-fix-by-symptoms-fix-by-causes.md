---
title: "Fix by symptoms, fix by causes"
date: 2020-10-19
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2020/10/fix-by-symptoms-fix-by-causes.html
---

# Fix by symptoms, fix by causes

*Published 2020-10-19*  
*Source: <https://visible-quality.blogspot.com/2020/10/fix-by-symptoms-fix-by-causes.html>*

---

Working with a new tester is both refreshing and inspiring as they go through things I've been through and where my seasoned nature makes things different. One of those things is related to how we communicate on bugs.

The team took upon themselves a change where some information currently stored in a local database in our own objects now move to being stored in a 3rd party system, with a well-defined REST API to get to the information. The developers would do their bit, and as their flow of pull requests was dying down, the new tester raised the question: is this supposed to be ready? Having already tested it throughout the steps, they knew of many things that didn't quite work, and having had conversations on those with the developers, they expected the developers did too. Yet, the state of functionality was not where done would reside, and the tester was confused.

With the confirmation of the problems being unknown, the developer insisted on writing separate bug reports on every symptom. And there were quite a few. What had happened is that while the previous local object to REST API had included read-only information after the change locally, no one remembered to discuss that this one was asymmetric and didn't. There needed to be both the information from the REST API and the local object, and as when you confuse a principle like this, data was getting lost in quite confusing ways.

Discussing the symptoms the tester was seeing made us all feel a little puzzled without the connecting story of why the change was failing. And with failing change and many reports, the disconnect in communication between us all was clear.

As soon as I worked together with the new tester, we figured out what was wrong. And the new tester turned their experience to a metaphor.

It was like we had been building a car, and as they sat on the driver seat, they could experience that they no longer saw through the windshield  like before. They could experience the steering wheel was hard to use, and that reaching pedals was getting next to impossible. They just could not tell why they experienced all this.  They could not tell it was because the seat position had shifted. Not because the change was to change the seat position - the change was to install new car mats on the floor. They were describing symptoms, creating bug reports of each symptom. And the worst part was that they were getting fixes for their symptoms, not yet knowing the reason they had to see those symptoms and a nagging feeling that the fixes they were getting may not address why they are seeing those symptoms.

When they need the chair moved back, they instead get a wider windshield, a pedals adapter and had to live with the bad experience with the steering wheel.

As testers, we are taught to describe what we observe, the symptoms. Yet the way we are able to frame those symptoms triggers memories and ideas of what the right, proper solution is with the developers. And my new colleague is very right that them doing their job on reporting is not sufficient. They can, and should, work on setting the relationship right so that instead of fixing by symptoms, we fix by causes.
