---
title: "Assert and Approvals, and Why that Matters"
date: 2019-10-30
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2019/10/assert-and-approvals-and-why-that.html
---

# Assert and Approvals, and Why that Matters

*Published 2019-10-30*  
*Source: <https://visible-quality.blogspot.com/2019/10/assert-and-approvals-and-why-that.html>*

---

As an exploratory tester, a core to my existence are unknown unknowns. I stumble upon problems - to an extent people like Marit van Dijk call out that "I don't find bugs, the bugs find me". But stumbling upon them is no accident. I intentionally find my way to places where bugs could be at. And when there is a bug, I try to finetune my ability to recognize it - a concept we testers call oracles.  
  
As I'm automating, I codify oracles. In some ways of automating tests, the oracles are multipurpose (like property-based testing, describing and codifying rules that should hold true over generated samples), and sometimes they are very specific.  
  
Both these multipurpose partial oracles and single purpose specific partial oracles are usually things we build as **asserts**. In the do-verify layers of creating a test automation script, asserts belong in the verify part. It's how we tell the computer what to verify - blocklisting behaviors that cannot be different. Much of our automation is founded on the idea of it alerting us when a rule we create does not  hold true. Some rules are fit to run unattended (which is why we focus on granularity) while others are for attended testing like exploratory unit testing.   
  
Another approach to the same codifying oracles problem comes through approval testing. What if we approached the problem with the idea that a tester (doing whatever magic they do in their heads), would recognize right-enough when they see it, and approve it. That is where **approvals**come in. It is still in the verify-layer of creating a test automation script but the process and lifecycle is essentially different. It alerts us when things change, giving names to rules through naming tests without a pre-assumed rule of *comparing to a golden master*.  
  
Approvals in automation increase the chance of serendipity, a lucky accident of recognizing unknown unknowns when programming, and they speak to the core of my exploratory tester being as such.  
  
**The Difference in the Process and Lifecycle**  
  
  
When we create the tests in the first place, creating an assert and approval is essentially different:  

- An assert is added to codify the pieces we want to verify and thus we carefully design what we will tell us that this worked or didn't. Coming up with that design is part of creating the assert and running the assert (see it fail for simulated errors) is part of creating it.
- An approval is prepared by creating a way to turn an object or aspect of an object into file representation, usually text. The text file would be named with the name of the text, and thus whatever the textual representation of what we are creating is the focus of our design. We look at the textual representation and say "this looks good, I approve", saving it for future comparison.
- Assert you write and run to see green. Approval you write and run to see red, then you approve to see green.

When we run the tests and they pass, you see no difference: you see green.  
  
When we run the tests and they fail for a bug we introduced, there is again an essential difference:  

- An assert tells us exactly what comparison failed in a format we are used to seeing within our IDE. If run on headless mode, the logs tell what the failed assert was.
- An approval tells us that it failed and shows the context of failure e.g. opening a diff tool automatically when running within our IDE. Especially on the unit level tests, you would want to run the tests in IDE and fix the cause of failure in IDE, having it all at your fingertips.

When we run the tests and they fail for a change we introduced, we have one more essential difference:  

- An assert needs to be rewritten to match the new expectation.
- An approval needs to be reapproved to match the new expectation.

When looking for things we did not know to look for, we are again different:  

- An assert alerts us to the specific thing we are codifying
- An approval forces us to view a representation of an object, opening us to chances of seeing things we did not know we were seeking.

**Back to exploratory and why this distinction matters so much to me**  
  
Even as a programmer, I am first and foremost an exploratory tester. My belief system is built around the idea that I will not know the mistakes I will make but I might recognize them when I see them.  
  
I will create automation that I use to explore, even unit tests. Sometimes these tests are throwaway tests that I never want to push into the codebase. Sometimes these tests belong to a category of me fishing for new problems e.g. around reliability and I want them running regularly, failing sometimes. I will keep my eye on the failures and improve the code they test based on it. Sometimes these tests are intended to run unattended and just help everyone get granular feedback when introducing problems accidentally.  
  
With approvals, I see representations of objects (even if I may have to force objects into files creating appropriate toStrings). I see more than I specifically command to show. Looking at a REST API response with approvals gives me EVERYTHING from header and message and then I can EXCLUDE undeterministic change. Creating an assert makes me choose first and moves exploration to the time I am making my choices.   
  
The difference these create matters to my thinking. It might matter to your thinking too.
