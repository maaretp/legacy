---
title: "From avoiding tech debt to having tech assets"
date: 2017-06-12
updated: 2017-07-23
theme: ensemble-and-pair-testing
labels: [Mobbing]
source: https://visible-quality.blogspot.com/2017/06/from-avoiding-tech-debt-to-having-tech.html
---

# From avoiding tech debt to having tech assets

*Published 2017-06-12, updated 2017-07-23 · Labels: Mobbing*  
*Source: <https://visible-quality.blogspot.com/2017/06/from-avoiding-tech-debt-to-having-tech.html>*

---

The question I always get when talking about mob programming is *how could that be a better / more effective way of working* *than solo work.* The query often continues with *do you have research results on the effectiveness?*  
  
As someone with a continuous empirical emphasis on my work as a tester, and someone with background in research work at university, I'm well aware that the evidence I care to provide is anecdotal. I have other things to do than research nowadays, and having done that I realize the complexities of it. And while anecdotes are research results, I can work with anecdotes.  
  
One of the themes I like collecting and providing anecdotes on around mobbing is that to me it makes little sense to compare an individual task, but a chain of value delivery. Many times with mobbing, we end up with significantly less duplication of code, as someone in the group acts as the memory to tell that they are using something of that sort somewhere else.  
  
Here's an anecdote I just today added to my collection: "QA person, where were you 9 hours ago when your knowledge would have saved us from all this work?". A team of programmers was mobbing, and wondering how to work on a particular technology. For everyone in the group, it seemed like there was some significant implementation work for somewhat of a scaffolding type of work, and the team set out to do that work. Later, another person became available to join the mob and with the knowledge available to them, eradicated all the work until that point, just having  the information available: an appropriate library for the scaffolding would already be available, and was used on the tests.  
  
I've seen my own team talk around an implementation, starting with one strong idea, and ending up with the best of what the group had to offer. I've watched my team express surprise when days of work get eradicated with knowing the work has already been done elsewhere. I've watched them come to realization that whatever they would have implemented solo, would have been re-implemented to better match the ideas of architectural principles or the best use of common components.  
  
I've also had chances of seeing a mob go through about ten solutions to a detailed technical problem just to find one with least tradeoffs between maintainability, performance and side-effect functionality.  
  
A lot of times the best result - paying back in the long term - does not emerge ever from solo work. And that just makes the comparison of what did it take as effort to generate some value in mob vs. solo all the more difficult. It's not the task, it's not the delivery flow, but it's the delivery+maintenance flow that we need to be comparing.
