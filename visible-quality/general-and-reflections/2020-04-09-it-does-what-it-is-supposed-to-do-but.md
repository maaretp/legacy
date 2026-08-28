---
title: "It does what it is supposed to do, but is this all we get?"
date: 2020-04-09
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2020/04/it-does-what-it-is-supposed-to-do-but.html
---

# It does what it is supposed to do, but is this all we get?

*Published 2020-04-09*  
*Source: <https://visible-quality.blogspot.com/2020/04/it-does-what-it-is-supposed-to-do-but.html>*

---

Yesterday in a testing workshop I run 3rd time in this format online, something interesting happened. I noticed a pattern, and I am indebted to the women who made it so evident I could not escape the insight.  
  
We tested two pieces of software, to have an experience on testing that enabled us to discuss what testing is, why it is important and if it interests us. On my part, the interest is evident, perhaps even infectious. The 30 women participating were people from the Finnish MimmitKoodaa program, introducing women new to creating software to the skills in that space.  
  
The first software we tested was the infamous Park Calculator. The insight that I picked up on came quite late to a bubbling discussion on how many problems and what kind of problems we were seeing, when someone framed it as a question: Why would the calculator first ask the type of parking and then give the cost of it, when a user would usually start with the idea that they know when they are traveling, and would benefit from a summary of all types of parking for that timeframe? The answer seems to be that both approaches would fit some way of thinking around the requirements, and what we have was the way who ever implemented this decided to frame that requirement. We found a bug, that would lead to a redesign of what we had, even if we could reuse many of the components. Such feedback would be more welcome early on, but if not early, discussing this to be aware was still a good option.  
  
The second software we tested was the GildedRose. A piece of code, intertwined with lovely clear requirements, often used as a way of showing how a programmer can get code under tests without even reading the requirements. Reading the requirements leads us to a different, interesting path though. One of the requirements states that quality of an item can never be negative and another one tells it is maximum 50. Given a list of requirements where these two are somewhere in the middle, the likelihood of a tester picking these up to test first is very high - a fascinating pattern in itself. However, what we learn from those is that *there is no error message* on an input or output beyond the boundaries as we expect, instead given inputs outside boundaries the software stays on the level of wrongness of input not making it worse, and given inputs barely at boundaries it blocks the outputs from changing to wrong. This fits the requirement, but goes as a confusing design choice.  
  
The two examples together bring out a common pattern we see in testing: sometimes what we have is what we intended to have, and fits our requirements. However, we can easily imagine a better way of interpreting that requirement, and would start a discussion on this as a bug we know will stretch some folks ideas of what a bug is.

> With both of our test targets yesterday, we identified a bug where it fits a requirement but the requirement was not up to par what users would want. You get what you ask for, not what you could ask for if you understood how software works.
>
> — Maaret Pyhäjärvi (@maaretp) [April 9, 2020](https://twitter.com/maaretp/status/1248309974809411586?ref_src=twsrc%5Etfw)
