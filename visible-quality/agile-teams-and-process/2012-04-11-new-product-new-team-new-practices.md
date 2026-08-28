---
title: "New product, new team, new practices"
date: 2012-04-11
theme: agile-teams-and-process
labels: []
source: https://visible-quality.blogspot.com/2012/04/new-product-new-team-new-practices.html
---

# New product, new team, new practices

*Published 2012-04-11*  
*Source: <https://visible-quality.blogspot.com/2012/04/new-product-new-team-new-practices.html>*

---

For a bit over a week now, I've been wondering where I ended up in my quest for hands-on testing work. With hard choices on the way, I'm now working for Granlund, a civil engineering company, with a product that handles building-related data. The domain is something I have little idea as of before, and I'm looking forward to learning a lot on that in addition to tuning and changing whatever I can with my testing skills. We have a small team of less than 10 people, and I'm the first and only tester. Most of my colleagues in development seem to work remotely, but within a week, I've had a change of learning they're just as much fun to work with as I expected.  
  
I start off with a redesigned version of a product that has been around for quite a while. The redesigned version is also out in production, new versions of it going out once a month. With customers actually paying for the product, they must be doing something right, even if they never had testers around.   
  
After reading up on what the product is about with a shallow scan of its documentation, I've worked on:  

- Setting up test management based on sessions with Rapid Reporter and csv-note scanning tool to show metrics I will create - as I won't create test case counts
- Learning the product's capabilities (and quality) with doing exploratory testing on its main feature areas
- Existing test suites and redesign of test documentation
- Redesigning a consultant-suggested testing methodology that I just can't believe would provide added value (unless faking testing is considered that to someone I did not yet meet there)

There's two strong first impressions:  

1. I've got a likely case of "asking for testing, when you should ask for fixing" ahead of me  
   I find it somewhat funny that so many people equate testing (quality-related information service) with fixing (making the quality right) and don't think of the dynamics that the added information will bring in. Then again, understanding the business impact and meaning of the existing technically oriented issues is a service I think I can help with.
2. As there's not enough rational testing examples around, it's easy to take the basic book on what's a test case and try replicating it without thinking enough  
   I've enjoyed reading the attempts to design tests in per-feature-area test suites of varying sizes, but all with step-by-step test cases repeating most of the steps again and again. I took on of these documents, 39 pages with 46 documented test cases and read it through in detail to make a mindmap of mentioned features (I do need a feature list to support my testing). While reading and using the product for learning it in practice (a couple of 1,5 hour sessions), I came up with one-page mindmap mentioning 88 things to test and four dimensions that cause repetition on significant amount of testing that should happen, like different browsers, user rights, and such. Out of the 39 pages, came out 3 things I could not directly deduct from the user interface with little information on the actual product. While doing this stuff, I marked down some (quite many) issues I would write bug reports on - if it wasn't the area we're about to rework on in a significant manner right about now.

Looking forward to all this - and the chances it provides for writing stuff and providing examples of something that is doable to "just a tester".
