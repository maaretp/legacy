---
title: "My #1 thing to Add With Testing"
date: 2018-01-07
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/01/my-1-thing-to-add-with-testing.html
---

# My #1 thing to Add With Testing

*Published 2018-01-07, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/01/my-1-thing-to-add-with-testing.html>*

---

Over the years, I've had the pleasure working with many kinds of developers. There's been those who struggle and barely get the code written, and testing for them is often somewhat painful. Fixing makes things more broken. And everything I touch feels broken. The majority, however, succeeds fairly well both in creating something and changing it on feedback. And then there's the small lovely group of test-driven developers who again are almost like a different species on the level of trust (or mechanisms of creating/maintaining trust) one can place on their changes.  
  
There is, however, one type of testing that I've been thinking about, that tends to find problems of relevance with all sorts of developers. And that is one focused on the *environment* around the software we are creating.  
  
I remember a big revelation years ago on what **system testing** can mean. I was testing a security scanning software on a mobile platform, and majority of things I needed to test was whether other applications and services other applications use still work with this software installed. It was by no means obvious. The system was much more than the mechanics of the software we created. It was everything our software touched. The software was special in comparison to many others, hooking deep into the operating system in ways that with the possible combinations of differences in firmware could result in interesting behaviors.  
  
As I was testing ApprovalTests for the first time, the very first things I went through were environment setup. I had my C# environment, with two different test runners (there's more options though) and I started setting up the thing I was about to test, failing miserably. I had just hit a bug that soon got fixed (and forgotten) - the installation path through nuget would fail in cases where there were more than one runner installed. Again, the software failed for the environment it was put in.  
  
Similar problems were there with the latest feature I was testing. It was fine "on my machine". But if "my machine" got more complicated, with competing ways of using same services available, it would fail in interesting ways.  
  
So, when testing, remember you're not testing just the software as the requirements seem to state. That software is supposed to live in an environment with other software. It has a lifecycle. It relies on shared services.  
  
Sometimes, the environment with other software is not for your company to control. Who gets assigned blame on a problem of incompatibility? Usually the one who comes in last. You might at least want to think through what other software your software is supposed to live with, and test for those.
