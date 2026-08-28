---
title: "The two language trap"
date: 2016-10-24
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2016/10/the-two-language-trap.html
---

# The two language trap

*Published 2016-10-24*  
*Source: <https://visible-quality.blogspot.com/2016/10/the-two-language-trap.html>*

---

For a good number of years, I worked with an organization that was doing production and test automation code all in C#. The organization got there partially through trial and error with VendorScript and discarding all work of an individual because no one else could maintain it.  And partially from a timely recommendation from me. I had an opinion: it would be better to work on one language and not go for a different language for the testing code.

And I'm simplifying things here. In addition to C#, there was at first a lot of JavaScript. Both in production code and tests. And then later on, there started to be a lot of TypeScript. And there was Powershell. So clearly the developers could move around languages. But common thing was that each of the languages was motivated primarily from production, and testing followed.

The good thing about working on the same language selection was that as the lone tester, I would not be alone even if I would contribute to the automation efforts. The automation was there to support the developers, and while e.g. Python and Robot-framework sales were high (it's from Finland after all), a new language, I believed, would create a distance.

So I changed jobs and the timely recommendation from me was way past being timely, with years of effort committed to a two language environment. The production language being C++, I could see why the choice of the same language for testing was not quite as straightforward. So the test language was Python.

The more I look at this, the more I understand that there isn't a real choice of one language. But the two languages still looks a lot like a trap. Here's some differences I'm observing:

- The gap between 'real' production programmers and the test automation programmers is deeper.
- The perceptions of the 'betterness' of the languages deepen the gap
- People seldom develop equal skills in both, and as new learners they strictly start from one or the other.
- The self-esteem of the test automation programmers in their programmer identity is lower as they work on the 'simpler language'
- There is a lot more of a separation of dev and test, even if both are code
- As an exploratory tester, I will be in a two-language trap - learning both enough to get the information in two different formats to the extent I feel I need it

I feel the two language trap exists, because a lot of people struggle early in their programming careers to just work on one language. There's a lot of language specific tricks and development to follow in both the ecosystems, taking the groups further apart.

So this whole thing puzzles me. I have ideas of how, through collaboration, I could improve what I perceive as suboptimal siloing. How there's cultural work in promoting the two languages as equals in the toolset. How clean code and technical excellence might work as a bridge.

But I wish I did not have to. I wish I could live in a shared language environment. And most of all I wish that those who are not forced by realities into separating production and testing into two different languages, would think twice on their choices.

It's not about what language your tester is comfortable with. It's also about who will help her in the work, and how much will she have to push to get her work to be the feedback the developers need.

When the test fails, who cares? I would hope the answer extends the group of test automators.
