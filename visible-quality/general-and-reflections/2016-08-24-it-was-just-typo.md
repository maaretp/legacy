---
title: "It was just a typo"
date: 2016-08-24
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2016/08/it-was-just-typo.html
---

# It was just a typo

*Published 2016-08-24*  
*Source: <https://visible-quality.blogspot.com/2016/08/it-was-just-typo.html>*

---

As a tester, I'm a big believer in fixing UI string typos as I see them. You know, just going into the code, and spending a little time fixing the problem instead of spending the same (or more) on reporting it. These are just typos. These are changes that I find easy to understand. And yet, I test after I make those changes.  
  
In the last week, I was testing a cleanup routine. Over the years, our product database has piled up quite a lot of cruft, not the least for an earlier (imperfect) implementation that created duplicate rows for everything that was touched in a common user flow. I asked the developer who created the cleanup routine on what it was about and his advice on testing it, to learn that it was "straightforward" and that he had spent time on testing it.  
  
As we run the cleanup routine on the full data, it became obvious that "testing it" was not what I would mean by testing it. The cleanup for a copy of production data took 6 hours - something that no one could estimate before the run started. Meanwhile, the database shouldn't be touched or things will get messy.  
  
So we talked about how we cannot update the production like we do for test environments - hoping none will touch it. We need to actually turn things off and show a message for the poor users.  
  
The six hours and 1/3 of database size vanishing hints to me that this is straightforward because our data is far from straightforward. With very first tests, I discovered that there was data lost that shouldn't be, resulting in what we would refer to as a severe problem of the product's main feature of reports not working at all. To find the problem, all I needed to do is to try out the features that rely on the data, starting from most important: this one.  
  
Fast-forward a few days there's a fix for the problem. And the developer tells me *it was just a typo*. Somewhere in the queries with IDs, one of the groupings was missing a prefix. We talk on the importance of testing and I share what I will do next, to learn he had not thought of it. I joke to tell him that at least he did not tell me it was *just a 10 minute fix* after using significant amount of my time on making him even aware that a fix is needed.  
  
The phrase *it was just a typo* is interesting. We're an industry that has blown up space rockets for *just a typo.* We have lost significant amounts of money for various organizations for *just a typo.* Just a typo might be one of the most common sources of severe problems.  
  
For any developers out there - I love the moment when you learn that it's not about the extent of the fix but extent of the problem the lack of fix causes. I respect the fact that there's fixes that are hard and complex. *Just a typo* is a way of expressing this isn't one of those.
