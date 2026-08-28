---
title: "Benchmarking results - Human, Human with AI, AI with Human and where we land"
date: 2026-02-12
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2026/02/benchmarking-results-human-human-with.html
---

# Benchmarking results - Human, Human with AI, AI with Human and where we land

*Published 2026-02-12*  
*Source: <https://visible-quality.blogspot.com/2026/02/benchmarking-results-human-human-with.html>*

---

When I first started talking about resultful testing years ago, people thought I had a typo and meant restful testing. I did not. There is a significant results gap between the level of quality a developer team without tester like me produces, even when they aren't sloppy on their quality practices. Any tester feels useful when quality is low enough to be garbage collection but when baseline quality is decent, it takes a bit more skill to produce results that are still expected.

So results are list of bugs - anything that might bug a stakeholder - that we could consider starting conversations on. If we don't see them, we can't actively decide on them.

[![](../_images/pic1-c2150b36.png)](../_images/pic1-c2150b36.png)

A well-maintained illusion is both when we don't test, and when we don't test well. The latter is hard one for testers to deal with, because when your career is centered around doing something, you tend to believe you do it well. Even if you don't.

To know how you do, you would benchmark your results with known results. There's plenty of test targets out there, and I have dedicated a good 20 years in teaching testing by testing against various test targets.

Today I cycled back to run a benchmark comparing an application with known issues from a year ago when I tested it; to the same application today when I test it with AI; to results of 57 human testers who are not me but were assessed with this application to decide on their entry to particular client projects.

- human tester (past me) found 45 things to report -> 62%
- human tester with AI (today's me) found 73 things to report -> 100%
- AI with human (today's me constrained to prompting) found 40 issues to report -> 55 %
- AI without human (ask to test with playwright) found 4 issues to report -> 5%
- 57 human testers found on average 13.5 things to report -> 18%

The test target for this benchmark is a buggy version of ToDo App, hosted at https://todoapp.james.am/ with source code at https://github.com/TheJambo/ToDoInterviewTest and my answer key at https://github.com/QE-at-CGI-FI/todoapp-solution. The whole experiment reminds me of this quote:

> "AI will not replace humans, but those who use AI will replace those who don’t." - Ginni Rometty, former CEO of IBM

The way the tasks were done aren't exactly the same.

- The human tester (past me) had to explore to list features while testing.
- The 57 human testers were given a requirement specification based on the exploring the human tester before them modeled making their work essentially different and, I would argue, easier.
- AI with human got to use the requirements specification and was able to find 3 more issues with it.
- AI with human used 14 prompts to get to the reported level. It was prompted to use the app, the code, the generated test automation, and each one found more unique issues.
- AI without human relied on a single prompt to use playwright to list problems.

The AI in question is:

- GitHub Copilot with Claude Opus 4.5
- Playwright Agents out-of-box files installed today

My conclusion: start using AI to do better, even without automation Github Copilot is helpful. That alone won't suffice, you need to learn to ask the right things (explore). You need to be skilled beyond asking to find the things AI won't find for you. The bar on this benchmark moves as I discover even more, or realize I should classify items differently. Not all things worth noting have yet been noted. Testing is never a promise of completeness, but we do need to raise the bar from 18% level where my control group of 57 human testers land.
