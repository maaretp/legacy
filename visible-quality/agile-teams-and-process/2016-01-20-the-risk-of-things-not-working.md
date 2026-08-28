---
title: "The risk of things not working"
date: 2016-01-20
updated: 2018-12-26
theme: agile-teams-and-process
labels: [Agile]
source: https://visible-quality.blogspot.com/2016/01/the-risk-of-things-not-working.html
---

# The risk of things not working

*Published 2016-01-20, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2016/01/the-risk-of-things-not-working.html>*

---

Yesterday morning, a developer suprised me: "We just did a major refactoring, removing the model from our code and moving all responsibilities to core. I was thinking of checking this into the integration." After a few clarifying details the change could be summed up as *we changed everything*.  
  
As usual, when my teams devs change things, they test themselves. They have little of unit tests they could just run, so they explore the application. But with changes like this, it's hard. There's no specific place to check - it could be anything. It means the developers test less.  
  
The change comes my direction, and I test a basic positive scenario of sampled features from my checklist. I find nothing on this change but spend a few hours on this. From the idea (Monday evening) to production (Wed morning), things go pretty smootly. A day in production, no problems.  
  
When I decide to be done with this, I'm painfully aware of how little I tested for a *change of everything*. I could easily spend weeks on testing it. But I assess the risk, knowing from my testing that the basic flows work and we publish it. There's a significant risk of things not working, but I remind myself: not tested does not mean not working.  
  
The experience leads me to think again about many of the discussions we have on automation. How so many times people assume that anyone (or me) would actually run the tests that automation could run, if it was implemented. I don't: not testing does not mean it does not work. How people don't see that an option to investing in automation that helps repeat some tests is that you work in a context that allows you to publish with the risk of things not working. Risk is not a fact, it's a chance. Playing on the risk is a gamble.  
  
We've done many things to make the gamble worthwhile from production monitoring to abilities to fix things quickly to deeper understanding of our business and users. Testing is just one piece in the puzzle. But as a tester caring for the system and user experience, it's a piece that glues perspectives together.
