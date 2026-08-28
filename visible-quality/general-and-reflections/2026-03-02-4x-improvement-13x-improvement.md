---
title: "4x improvement, 13x improvement"
date: 2026-03-02
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2026/03/4x-improvement-13x-improvement.html
---

# 4x improvement, 13x improvement

*Published 2026-03-02*  
*Source: <https://visible-quality.blogspot.com/2026/03/4x-improvement-13x-improvement.html>*

---

The world is awfully abstract these days. Everyone and their uncle seems to know what "testing" is, and a good half of them would volunteer to explain it to me, in detail. From those conversations, I still conclude it's awfully abstract.

When one person talks of testing, their days actually look like coordination. Ensuring pieces of the whole become "ready" is a pattern that allows for seeing if they work together. Addressing feedback that does not need change of state for the ticket, that needs returning it to developer or that needs needs to addressed separately either as change management proposal, or as a problem that we could wait with a while. Now that we are moving from "testing" to "quality engineering", and "shifting left" + "shifting right", it's increasingly unclear what of it is testing. And frankly, that does not matter as much.

What matters is quality results, and our signal of knowing. Calling that "abracadabra" might be sometimes helpful.

A similar conversation is one around productivity, that is awfully abstract. When we compare productivity, particularly for improvement, the comparisons are local to a task rather than evidences of approaches in scale. But I wanted to tell you two pieces of those comparisons.

**The 4x story**

With being a consultant, a thing that comes sometimes is that the client needs to react to a diminishing budget. They used to have a team of 5, and now they can have a team of 3.5. People aren't half. You can budget and pay them half, but they tend to find it hard to do equal amount with their other half. You might also think that the half includes you being able to ask any time, effectively leading to full time service to pull with half the price. I have found these particularly fascinating while in consulting.

From the fascination, I asked a colleague to revisit their output / value with numbers from a sampled timeframe. One month, separated by a year. One month where their work was 100%, and one month where their work was 50%. We know the incoming money is cut by half. What happened to the value delivered to the client?

Turns out that the monthly output / value has doubled. In the two months compared, roughly same amount of changes were made to the software and tested. Roughly same amount of changes were returned to sender for undone work. Same work for half the price!

But there were additional things. In the 50% timeframe, the team's tester had volunteered on specification work and that too fit the time. With clarity and ease for testing of those features where beginning and end meet, we could argue a factor of 2x on output / value.

What really changed:

- The later time includes less learning of the system, as the system is incrementally being changed and the same person has been acquiring the layered knowledge.
- Learning happens on the other 50% that is not paid, and the value of the growth of that other 50% shows up in the paid work. The whole *quality engineering* transformation thinking enabling the improvements is no unpaid.
- Risk-based change testing on assigning varied size timeboxes of effort rather than applying a standard filtering was necessary to the budget cuts, but no risks of missing with incorrect decisions have yet been noticed.
- Finding issues on software at large rather than on the specific change has been cut down, but it may also be naturally cut away by the continued years on the same application.
- Releases aren't the same in the two months: one had hotfix and one a release. We know those are testing where visible results are not expected but effort is significant. Smaller batch size keeps all releases in the hotfix kind of process.
- Active time on testing is the only real way to talk about coverage of testing. That really needed optimizing to not lose out on results.

In analyzing this, **we concluded 4x improvement** that would only be possible when the cognitive load of the other assignment for the full person is in support of this assignment. Improvement comes from growth: learning risk-based change testing, specifications as means over task expansion, better forced boundaries of entry quality. It is likely not sustainable when a second project requiring application specific learning comes through, and it is operating on a risk limit.

I also wonder: should we have been able to cut the output / value in half, and communicate the investments we ended up making in improving the work. If we don't, people end up thinking the best way to improve testing is to basically force a 50% fee reduction. While it happened this time, it also happened this time since a significant collaboration and coaching effort on updating the ways we think about testing is ongoing.

**The 13x story**

Another output / value -based comparison on test automation work shows 13x improvement. This comes from comparing 24 weeks of test automation without Github Copilot Agents and 3 weeks of test automation with those. The amount of test automated per time unit: 13x improvement.

Again, we are comparing things with a lot more variables than just Github Copilot Agents. The main variables are:

1. **Learning**. It slows you down. The first number includes learning what test automation is, what the test target is, what the team is.
2. **Pressure**. On the latter timeframe, it was either finding success or end of the work.

While the 13x sounds great and fancy, it comes from intentionally comparing apples and oranges, so to speak.

Having people's attention with the number, let's address the real deal:

- Github Copilot Agentic use was far from obvious. It needed metrics to guide it, expected behaviors of tool user addressed in pair and ensemble testing sessions. And it needed time to sink in.
- Learning to walk while having a bike next to you just won't work. We are really seeing the power of learning making a 13x impact, rather than really Github Copilot.
- Github Copilot agentic use relied on the hyper-reusability built on the first segment of time. Creating next ones when code can be reused is a lot more straightforward.
- Drift of ready. On the first batch, I was around to analyze in detail if this matches the expected test. On second batch, I haven't looked at the steps yet. There is a chance of appearance of progress by shortcuts that easily happen because *pressure*.

**Conclusions**

I won't make the best tool salesman with how critically I look at the improvements. But I will be great at delivering improving value. Perhaps that should be the target, after all?
