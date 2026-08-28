---
title: "Refining a 34 year old practice"
date: 2018-07-27
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/07/refining-34-year-old-practice.html
---

# Refining a 34 year old practice

*Published 2018-07-27, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/07/refining-34-year-old-practice.html>*

---

Exploratory testing is a term that [Cem Kaner coined 34 years ago](https://www.kaner.com/pdfs/QAIExploring.pdf)  to describe a style of skilled testing work that was common in Silicon Valley, uncommon elsewhere. When the rest of the world was focusing on plans and test cases and separation of test design and execution, exploratory testing was the word to emphasize how combining activities (time with the application) and emphasizing learning   continuously about the application and its risk created smarter testing. The risks exploratory testing is concerned of are not limited to just the application right now, but everything the application goes through in its lifecycle. Automation of relevant parts of tests was always a part of exploratory testing, as the tangible ideas of what to automate next are a result of exploring the application and its risks.  
  
There are a few things in particular that refine what exploratory testing ends up looking like in different places:  
  

- Testing skill
- Programming skill
- Opportunity cost
- Outputs required by the domain

**Testing skill**  
  
Testing skill is about actively looking at an application in a deliberate way of identifying things worth noting in multiple dimensions. It's about knowing what might go wrong, and actively making space for symptoms to show up and building a coherent story of what the symptoms indicate and why that would be relevant.  
  
The less ideas people have about how we could approach an application for testing, the easier job they feel they have at their hands. Shallow testing is still testing.  
  
**Programming skill**  
  
Programming skill is about identifying, designing and creating instructions the computer can execute. It's about making a recipe out of a thing, and using computer to do varying degrees of the overall activity. When applied with tests, it leaves behind executable documentation of your expectations, or enables you to do things that would be hard (or impossible) do without.  
  
Computers only look at what they're programmed to look at, so the testing skill is essential for test automation.  
  
**Opportunity cost**  
  
When testing (or building software for that matter), we have a limited amount of effort available at any given time. We need to make choices of what we use the effort on, and one of those choices is to strike a personal and team level balance of how we split the effort between tests worth trying once and tests that turn out to be worth keeping, documenting and/or automating.  
  
We strike a balance of investing into information today and information in the future. We find it hard, if not impossible, to do both deep investigative thinking with the real application and maintainable test automation at the same time. But we can learn to create a balance with time boxing some of each, intertwined in a way that appears as if there was no split.  
  
**Outputs required by the domain**  
  
Sometimes exploratory testing produces discussions initiated around potential issues. Other times those discussions are tracked in a bug tracking tool and bug reports are the minimum visible output you'd expect to see. And sometimes, in domains where documentation as proof of testing is a core deliverable, test cases are an output of the exploratory testing done.  
  
Some folks are keen on managing exploratory testing with sessions, splitting the effort used into time boxes with reporting rules. Others are keen to create charters for making it visible what time is used on in agile teams as a means of talking / sharing what is the box of exploration.  
  
Your domain defines what outputs look like in scale from informal to formal.  
  
  
All skilled work relies on availability of that skill. Exploratory testing is an approach, not a technique.  
> Agile testing is the idea that developers can test, and that testers can contribute before development. Exploratory testing is the idea that testing is skilled activity.
>
> — Maaret Pyhäjärvi (@maaretp) [July 26, 2018](https://twitter.com/maaretp/status/1022462139280310272?ref_src=twsrc%5Etfw)
