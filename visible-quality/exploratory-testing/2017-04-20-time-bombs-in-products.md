---
title: "Time bombs in products"
date: 2017-04-20
updated: 2017-07-23
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2017/04/time-bombs-in-products.html
---

# Time bombs in products

*Published 2017-04-20, updated 2017-07-23 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2017/04/time-bombs-in-products.html>*

---

My desk is covered with post-it notes of things that I'm processing, and today, I seem to have taken a liking to doodling pictures of little bombs. My artistic talent did not allow me to post one here, but just speaking about it lets you know what I think of. I think of things that could be considered time bombs in our products, and ways to better speak of them.  
  
There's one easy and obvious category of time bombs while working in a security company, and that is vulnerabilities. These typically have a few different parts in their life. There's the time when no one knows of them (that we know of). Then there's the time when we know of them but other don't (that we know of). Then there's the time when someone other than us knows of them and we know they know. When that time arrives, it really no longer matters much if we knew before or not, but fixing commences, stopping everything else. And there's times when we know, and let others know as there is an external mitigation / monitoring that people could do to keep themselves safe. We work hard to fix things we know of, before others know of them because working without an external schedule pressure is just so much nicer. And it is really the right  thing to do. The right thing isn't always easy and I love the intensity of analysis and discussions vulnerability related information causes here. It reminds me of the other places where the vulnerabilities were time bombs we just closed eyes on, and even publishing them wouldn't make assessing them a priority without a customer escalation.   
  
Security issues, however, are not the only time bombs we have. Other relevant bugs are the same too. And with other relevant bugs, the question of timing sometimes becomes harder. For things that are just as easy to fix while in production and while developing an increment, timing can become irrelevant. This is what a lot of the continuous deployment approaches rely on - fast fixing. Some of these bugs though, when found have already caused a significant damage. Half of a database is corrupted. Communication between client and server has become irrecoverable. Computer fails to start unless you know how to go in through bios and hack registries so that starting up is again possible. So bugs with impacts other than inconvenience are ones that can bring a business down or slow it to a halt.  
  
There's also the time bombs of bugs that are just hard to fix. At some point, someone gets annoyed enough with a slow website, and you've known for years it's a major architectural change to fix that one.  
  
A thing that seems common with time bombs is that they are missing good conversations. The good conversations tends to lead to the right direction on deciding which ones we really need to invest on, right now. And for those not now, what is the time for them?   
  
And all of this after we've done all we can to avoid having any in the first place.
