---
title: "The Squeezed Testing Problem"
date: 2016-06-16
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/06/the-squeezed-testing-problem.html
---

# The Squeezed Testing Problem

*Published 2016-06-16*  
*Source: <https://visible-quality.blogspot.com/2016/06/the-squeezed-testing-problem.html>*

---

This post is inspired by two nicely timed incidents:

  

- a discussion with an aspiring speaker, who was enthusiastic about BDD as a way of testers being able to work continuously throughout the sprint on
  testing
- a tweet mentioning a common theme of tester complaints: “We’re agile. All the testing is squeezed into the end of the sprint.”

  
Let’s talk about approaches in tackling the squeezed testing problem. I find this important because, as popular it seems to be, the BDD stuff is not the
only way forward. I’m sure the ways forward I’m aware of are not the only ways forward.
  
  
So, how could you organize the testing so that it does not end up all being squeezed into the end of the sprint?
  
  
**Approach 1: no sprints**
  
  
I find that Scrum and sprints is what people often start from, and having had 10 years of experience with adopting agile, it makes less sense to me now. So
instead of starting with Scrum, what if you would go for per-feature “sprints”, except those tend to be called Kanban and Continuous Delivery.
  
Don’t fall into the trap of thinking you cannot do continuous delivery without test automation. You can!
  
  
Try thinking it this way. You have feature X you know is important. Even most important right now. You discuss the feature with your team, and chip away
until you find the smallest possible value item you can deliver all the way to production. You then, as a team, do all the necessary work you need to get
it delivered. And all the necessary work includes manual programming and manual testing – nothing special there.
  
  
The strategies you employ to test might differ a bit. You might pair up with a developer to be there testing as it is being built. You may have a working
agreement that you test on a development machine before anything gets into source control. Or you may have a branching model where each fully integrated
feature can be automatically built as a system from its own branch that you can test with the developer fixing things as you find them.
  
  
Who defined that a month of programming would need to be tested in a day? The whole thing could be a two-month thing instead. When you deliver a
functionality at a time, it’s not a big trick to consider the thing done only after it has also been tested and fixed.
  
  
Just work on having small functional slices. You really don’t want 2-month feature projects if you can have half-a-day feature deliveries.
  

**Approach 2: forget about the idea of testing before production**
  
  
I find that a lot of testers are stuck on the idea that system and acceptance testing (that’s what they do) happen before you go live with your software.
But you could also look at testing as something you do almost exclusively against your production.
  
  
If you plan on using this approach, your organization might be better off having some safeguarding mechanisms on how you roll back or do staged releases
(not everyone gets hit with problems at once in large user base).  
  
So when your team is done with the sprint, the system goes live. You test the squeezed testing for the half-a-day you can squeeze in (or can’t), but it’s
really not your responsibility to attend to the fact if it works or not. Someone decided that it will get addressed during production use.
  
  
The changes are perhaps not that big, after all, they needed to fit into the squeezed development schedule of the sprint. Your testing really starts when
the end users using starts – just with the idea that you will *tell* *clearly* when you run into problems and pair up with a dev to get the
fixes done as soon as possible. The end users might not tell they have problems, and when they tell, getting them to express what they did and what is the
problem is a lot of work.
  
  
There’s one big problem with this approach. If you need to find a lot of problems, the developers need to fix a lot of problems and they don’t make
progress with the things they aspired to in the upcoming sprint. But if it works well, you will find missing value items, ideas to improve the user flow
and “missing backlog items” that you can add to your upcoming sprints to improve your product based on the feedback. The stuff you find can wait a sprint.
It’s like you’re an empirical extension to a product owner.
  

**Approach 3: shift left**
  
  
Shift left is the popular idea in agile that you would finally get a practical way of doing the thing waterfall always failed with. Your chances are up
because of short increments – helping build the right product one small right thing at a time seems more feasible than hitting the mark on something big in
waterfall style.
  
  
BDD (Behavior-driven development), SBE (Specification by Example), and ATDD (Acceptance Test Driven Development) all roughly mean the same idea: create
examples of behavior in test artifact format, implement the automation while implementing the features and you’ll hit the mark better and need to do less
of exploratory testing when what you were building was more clearly designed.
  
  
This approach would ask the tester to work on creating the test artifacts (with a product owner and the rest of the team) first as text, and then
contribute to automating. When the test artifacts “pass” against the implementation, the assumption is that the exploring needed is small and fits the
squeezed timeframe. After all, you were exploring already while designing the feature.
  
  
I find that the product is my external imagination, and my best attempts to tell, even for small features all the stuff in advance are limited. But limited
is better than not trying to clarify what we’re doing.
  

**Other approaches?**
  
  
There are a lot of options of tweaking each of these, I’m sure. My main concern is this. If so many testers are struggling with testing getting squeezed to
the end, why are so many testers feeling so powerless to do anything about it?
  
  
We’re in the business of providing information through empirical work. How about using the empirical evidence to change the status quo to something a
little better, one experiment at a time? A good tester has a lot of power. Find the information that matters to the people who matter.
