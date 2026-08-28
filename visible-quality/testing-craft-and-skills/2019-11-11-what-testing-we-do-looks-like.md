---
title: "What the Testing We Do Looks Like?"
date: 2019-11-11
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2019/11/what-testing-we-do-looks-like.html
---

# What the Testing We Do Looks Like?

*Published 2019-11-11*  
*Source: <https://visible-quality.blogspot.com/2019/11/what-testing-we-do-looks-like.html>*

---

Back in the days before releasing frequently was a thing, testing looked very different. The main difference was that we thought of automation as something that was replacing attended testing, whereas we now see it more as a way of introducing scale of unattended testing we could never have done attended.  
  
The stuff we attend to changed as the world around us shifted. We still do "testing" with just as many hours, but the work is split on working heavily on unit tests, test automation and other quality practices.  
  
I try to explain the change I see with a metaphor: *pool is not a bigger bathtub*. Both these are containers of water (just like software development is just making and delivering code changes), but what you can do in a pool is very different than what you can do in a bathtub. Imagine a bath guard - kind of hilarious. Or a bath party - very eccentric. We create new things we can do with just a bigger container of water, and bringing down the release cycle does something very similar to the ways we work. The whole conceptual model of what makes sense changes.  
  
In efforts to describe what seems to make sense right now, I work on finding words to describe what testing I do looks like to me. It is not a tool for sense making the whole world of all testing, and I don't need a tool for that - I don't work in the whole world, I don't consult in the whole world. I merely describe my lessons from where I am for the organization that I work for but also in my understanding of how the world comes together.  
  

For me, it all is *customer-obsessed*  and *developer-centric*. We all care for where the money comes for our business. And we recognize and appreciate that we have something out there that people are already paying for that we want to always improve and never make worse. But we already have *something valuable*.

[![](../_images/smartdevsturnideasintocode-976fa1c0.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmYLszoJyGSSK8B-iubj33F7EetH6bjimF5Mi7qv_Nv_EEKp6nKEBzVsI_-pv9ZrM3IB_RAhR55in2ZtTxZMjZrwulSM5atkHdZNoR3_HLrgBPwfFDpXZAc-4lBzmzwTFltg02HiOQps0/s1600/SmartDevsTurnIdeasIntoCode.jpg)

*Smart Developers Turn Ideas Into Code*

Since it is already out there, I can't describe a phase of requirements gathering, but rather it begins with a *vision* of value. There is always, even if informally, a mostly shared base of understanding of the types of things we are providing for the customers. I recognize vision not from a document someone wrote, but from discussions with multiple members of community bringing perspectives driving us to a similar direction. Similar, not same, as vision is in its most powerful state when it guides individual actions without excessive coordination.

From having something out there working for the customers and vision, we come to a set of ideas on what we could try to make things better. This part of the process of coming up and acting on the ideas, turning them into code, is where the change gets made.

Some ideas are bigger, and they are hard to grasp alone. Smart people are not alone, but surrounded by other smart people. Together, we can make ideas better, and as such, the resulting code better. Or we can discover the ideas in the first place.

Let me share a small example of how I can reasonably expect my days to be from today.

> I had a Windows machine I had kicked up from an image last week, forgetting that the images in that particular set of images give me a fairly old version of windows, one where our .Net dependency for showing a full UI stops me from seeing the UI that I wanted to test. I run a windows update tool on Friday, and since that takes its time, did something different going back to the computer today. As I remote to the computer, I see the IP but I wasn't remembering the name of the computer. There is one very simple way for me to do it: logging into our security management portal and seeing it there. So I did.

> I found the computer, got things I needed but also noticed we had started showing both IPv4 and IPv6 addresses. Having been elsewhere, I had not followed that detail, but just looking at it I said that I didn't like a detail on how they were ordered. 5 minutes later of me just casually mentioning this, I had a pull request to review that fixed the problem. We added a bit of discussion around what I would test around more network interfaces that was hard to simulate, and another pull request on an additional unit test was created.

My tester-contribution can happen anywhere, anytime, without constraint of a process. It will happen from a foundation of me (the tool) being in the right mind in the right place to connect things. And I cultivate the chances of that lucky accident through discussions but also, hands-on with my external imagination - the product - either directly or through a set of scripts known as test automation (TA).

On doing my work, I rely on an existing structure that we have built and are enhancing as we learn what we are missing:

- A Smart Developer creates code to change the *application*
- Unit tests on local machine to 80-90% coverage
- Pull Request Review - a minimum of second pair of eyes on change
- Static tools of various flavors in the pipeline
- Unit tests in the pipeline
- TA in the pipeline (with TA telemetry)
- CI environment application telemetry
- Change-log driven exploratory testing
- Changes out in other product line continuous beta
- Changes out in internal pilot
- Changes out in early access
- Synthetic monitoring aka. production TA (or machines, in production, continuously monitored)
- Production Telemetry, positive events and error events

The like "TA in the pipeline" is more than a few scripts run, and I will dedicate a post of its own to it later.

With every change, we try to leave things better than they were before. Caring developers pulling in the help they need, and making the help readily available is what testing looks like to me. Testers are developers. We change things, but we also change the other developers perceptions.

We see things other people don't.
