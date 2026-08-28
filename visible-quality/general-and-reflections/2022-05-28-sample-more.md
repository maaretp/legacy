---
title: "Sample More"
date: 2022-05-28
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2022/05/sample-more.html
---

# Sample More

*Published 2022-05-28*  
*Source: <https://visible-quality.blogspot.com/2022/05/sample-more.html>*

---

Testing is a sampling problem. And in sampling, that's where we make our significant mistakes.

The mistake of sampling on the developers computer leads to the infamous phrases like "works on my computer" and "we're not shipping your computer".

The mistake of sampling just once leads to the experience where we realise it was working when we looked at it, even if it it clear it does not work as someone else is looking at it. And we go back to our sampling notes of exactly what combination we had, to understand if the problem was in the batch we were sampling, or if it was just that one sample does not make a good test approach.

This week I was sampling. I had a new report intended for flight preparations, including weather conditions snapshot in time. If a computer can do it once, it should be able to repeat it. But I had other plans for testing it.

I wrote a small script that logged in, captured the report every 10 seconds, targeting 10 000 versions of it. Part of my motivation for doing this was that I did not feel like looking at the user interface. But a bigger part was that I did not have the focus time, I was otherwise engaged pairing with a trainee on the first test automation project she is assigned on.

It is easy to say in hindsight that the activity of turning up the sample size was worthwhile act of exploratory testing.

I learned that regular sampling on user interface acts as keep alive mechanism for tokens that then don't expire like I expect them to.

I learned that for expecting a new report every minute, the variation of how samples every 10 seconds I could fit in varies a lot, and could explore that timing issue some more.

I learned that given enough opportunities to show change, when change does not happen, something is broken and I could just be unlucky in not noticing it with smaller sample size.

I learned that sampling allows me to point out times and patterns of our system dying while doing its job.

I learned that dead systems produce incorrect reports while I expect them to produce no reports.

A single test - sampling many times - provided me more value than I had anticipated. It allowed testing to happen, unattended until I had time to again attend. It was not automated, I reviewed the logs for the results, tweaked my scripts for the next day to see different patterns, and do now better choices on the values I would like to leave behind for regression concerns.

This is exploratory testing. Not manual. Not automated. Both. Be smart about the information you are looking for, now and later. Learning matters.
