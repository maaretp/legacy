---
title: "An Evening Detour to TCR"
date: 2018-12-12
updated: 2018-12-26
theme: programming-and-technical
labels: [Programming]
source: https://visible-quality.blogspot.com/2018/12/an-evening-detour-to-tcr.html
---

# An Evening Detour to TCR

*Published 2018-12-12, updated 2018-12-26 · Labels: Programming*  
*Source: <https://visible-quality.blogspot.com/2018/12/an-evening-detour-to-tcr.html>*

---

At an usually early time for me, I waved goodbyes at the office announcing I was heading to a workshop on TCR and greeted with a bit of rolling eyes and quick googling fingers. It was already established that I was more into volunteering on all sorts of learning activities. [Aki Salmi](https://twitter.com/rinkkasatiainen) hosted a
workshop session on TCR with Tech Excellence meetup, which I just so
happen to facilitate, so I had all the excuses I could need to get over
myself and over  there.   
  
TCR - Test && Commit || Revert - is [a programming workflow](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864)  or a test-driven development flavor. Reactions have been from "well, got to try it" to "why are we confusing TDD more" to "will TDD replace TCR" and it feels like a worthwhile thing to do in a great company.  
  
Aki introduced the thing we were about to be experimenting with. Test-Driven Development (TDD) as we've come to know it has three steps, RED - GREEN - REFACTOR, and Test && Commit || Revert (TCR) removes the RED. If your tests aren't green when run, you lose what you worked on. If they are green, they get committed as the next baseline to work from.   
  
Other than the focus on experiencing TCR, the session was framed by 3x25 minutes of paired work with sharing impressions in between, the Lift (Elevator) kata and whatever the pair ends up choosing as their language.   
  
I paired with one of my favorite people who I yet had never paired with before. They came in with things set up on their computer, so the choice on language and IDE were settled: Python on Vim.  
  
Over the three 25-minute sessions, the promise of having fun was well delivered.   

- The most common reason of reverting for us was syntax - we missed a part of formatting. This made me aware of how much I prefer relying on Pycharm as my IDE, with having my focus free from the details of the syntax. We also had great little discussion on the feeling of control of having to know / do every bit in Vim I wasn't appreciating.
- With another IDE, I find it relieving to work with intent and
  generating frames for the code and the Vim as editor made me aware of
  how much I appreciate other tooling.
- Differences on Python / Java felt evident in running tests with same name that Python just dealt with for us, while we would have had a couple more of reverts if we worked in Java.
- One pair "cheated" by commenting out the failing tests and I'm still confused with it. Being always green if cheating is encouraged is easiest by never having much in the way of tests, and that cannot be what Kent Beck means with "Cheating is encouraged, as long as you don’t stop there."
- With the workflow, I was missing seeing the test fail to test the test before implementing. I disliked the thinking as the computer when I would much rather see the test fail first, but wasn't willing to let the test be reverted just for that.
- Putting the commands together so that your changes are gone on red increased the sense of risk losing your changes and introduced a language of betting a small amount of work.
- Being painfully aware of the risk of losing changes keeps changes small. It would require next level abilities compared to what we were working with though that we could identify making designs driving us to smaller steps for this.

Overall, I think I was just as bothered with "losing my IDE" as "losing the RED".  
  
In the discussions afterwards, there was speculation about would something of this sort be more necessary when working on trunk-based development where folks might commit tests while they are red, but it sounds to me like a different problem to just the programming workflow.  
  
I find all these things useful as ways of learning about what you're comfortable with and how constraints of all sorts impact your way of working.  
  
All in all, this just felt like a relaxed version of [Adi Bolboaca](https://twitter.com/adibolb)'s baby steps constraint, where you revert if you're not green in 3 minutes. With this style, you can see red, but get to a similar practice - making changes intentionally small without losing the feedback of a test first failing to know you're actually testing what you intended.
