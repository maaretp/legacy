---
title: "Tools Guide Thinking"
date: 2019-11-21
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2019/11/tools-guide-thinking.html
---

# Tools Guide Thinking

*Published 2019-11-21*  
*Source: <https://visible-quality.blogspot.com/2019/11/tools-guide-thinking.html>*

---

I have spent a significant chunk of my day today in thinking about how exploratory testing is the approach that ties together all the testing activities even when test automation plays a significant role. Discussing this with my team from every developer to test automation specialists to the no-code-for-me-tester, finding a common chord isn't hard. But explaining it to people who have a different platform for their experiences isn't always easy. Blogging is a great way of rehearsing that explanation.

I frame my thinking today around the idea I again picked up from [Cem Kaner's presentation on Exploratory Testing after 23 years](http://www.kaner.com/pdfs/ETat23.pdf) - presented 12 years ago.

> "Tools guide thinking" - Cem Kaner

Back then, Cem discussed tools that would support exploratory thinking, giving examples like mindmaps and atlas.ti. But looking back at that insight today, the tools that guide a rich multi-dimensional thinking can be tools we think of as test automation.  
  
We have a tool we refer to as TA - short-hand for Test Automation. It is more than a set of scripts doing testing, but it is also a set of scripts doing testing. To shortly describe the parts:  
  

- machinery around spawning virtual environments
- job orchestration and remote control of the virtual machines
- test runners and their extensions for versatile logging
- layers of scripts to run on the virtual environments
- execution status, both snapshot and event-based timelining

Having a tool like this guides thinking.

When we have a testing question we can't see from our existing visualizations, we can go back to event telemetry (both from product and TA) and explore the answers without executing new tests.

When we want to see something still works, we can check the status from the most recent snapshot automatically made available.

When we want to explore on top of what the scripts checked, we can monitor the script real time in the orchestration tooling seeing what it logs, or remote to the virtual machine it is running and watch. Or we can stop it from running and do whatever attended testing we need.

We can explore a risky change seeing what the TA catches and move either back or forward based on what we are learning.

We can explore a wide selection of virtual environments simultaneously, running TA on a combination we just designed.

We want a fresh image to test on without any scripted actions going on, we take a virtual environment which is at our hands ready to run in 2 seconds it takes to type it into a remote desktop tool.

It makes sense to me to talk about all of this as exploratory testing, and split it to parts that are by design *attended* and *unattended.* A mix of those two extends my exploration reach.

With every test I attend to either by proactive choice or reactive choice being called in by a color other than blue (or unexpected blue knowing the changes), I learn after every test. I learn about the product and its quality, about the domain and for exploratory testing most importantly, I learn about what more information I want to test for.

Tool guides my thinking. But this tooling does not limit my thinking, it enables it. It makes me a more powerful explorer, but it does not take away my focus on the *attended* testing. That is where my head is needed to learn, to take things where they should go. Calling \*this\* manual is a crude underrepresentation of what we do.
