---
title: "A Pesky Bug that Exploring Would Help With"
date: 2018-12-13
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/12/a-pesky-bug-that-exploring-would-help.html
---

# A Pesky Bug that Exploring Would Help With

*Published 2018-12-13, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/12/a-pesky-bug-that-exploring-would-help.html>*

---

I work with a particularly great team, and even great teams make mistakes. Many other teams, great or less so, would choose to hide their mistakes. I find I wear our mistakes as a metal of honor, as in having looked at them, figured out what I could try doing differently and going into the future again an experience richer. And looking forward to a different mistake.  
  
In the last weeks, we've dealt with a particularly pesky mistake to make from a tester point of view, because it is a failure in how we test.  
  
As bugs go, different ones show themselves in different ways. This particular one has limited visibility to our customers, as they can only see second order symptoms. But the cost of it has been high - blocking work of multiple other teams, diverting them from their intended use to create some good valuable items for our users, and instead making them create tooling to keep their system alive as we're oversharing data towards them.  
  
So there was a bug. A bad bug. Not a cosmetic one. But also not one visible easily for an end user.  
  
The bug was created by one of our most valued developers.  
  
Since it was created by someone who we've grown to rely on, other people in the team looked at the pull request feeling confident in acceptance. After all, the developer is valued and for a reason of consistency in great work. No one saw the bug.  
  
As we were testing the system, we made few wrong judgements:  
  

1. We relied on the unit and system level test automation, that tests the functionality from a limited perspective.
2. We didn't explore around the changes because exploring from another system as user perspective requires special attention and we did not call for it.
3. We relied on repeating tests as we had before, and none of the tests we did before would have paid attention to the volume of information we were sending.
4. We had limited availability of team members, and we only see in hindsight that the changes were into a critical component.

So we'll be looking at changes:

- Figuring out how the pull requests could work better to identify problems or if they are more about consistency of style and structure as they've grown to be
- Figuring out how to better integrate deep exploratory testing activities towards system functionalities (over user functionalities)

I have a few (ehh, 50) colleagues that wasted a relevant amount of time on keeping the mistake from surfacing wider while we did our remedies.

These kinds of bugs would be the ones I'd want to find through exploring. And it would be a reasonable expectation.

Less managing, more testing. My kind is more valuable as not a manager. The work happens hands-on.
