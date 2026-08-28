---
title: "Seeing Negative Space"
date: 2018-08-30
updated: 2018-12-26
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/08/seeing-negative-space.html
---

# Seeing Negative Space

*Published 2018-08-30, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/08/seeing-negative-space.html>*

---

Have you ever heard the saying: "There is no I in the TEAM"? And the proper response to it: "Yes there is, it is hiding in the A-holes". This is an illustration of the idea of negative space having a meaning, and that with the right font, you can very clearly see "i" inside the A.  
  
I'm thinking this because of something I just tested, that made me realize I see negative space a lot as a tester.  
  
The feature of the day was a new setting that I wanted to get my hands on. Instead of doing what a regular user would do and look at only settings that were revealed, I went under the hood to look at them all. I found the one I was looking for, set it False as I had intended and watched the application behavior not change. I felt disappointed. I was missing something.  
  
I opened a project in Stash that is the master of all things settings. I was part of pushing for a central repo with documentation more than a year ago, and had the expectation that I might find my answers there on what I was missing. I found the setting in question with a vague hint saying it would depend on a mode of some sort, which I deducted to mean that it must be another setting. I asked, and got the name of the setting I needed with an obvious name of "feature\_enabled". I wasn't happy with just knowing what I needed to set, but kept trying to find this in the master of all things settings, only to hear that since we are using this one is way 1 out of 4, I could not expect to find it here. I just need to "know it". And that the backend system encodes this knowledge, and I would just be better off if I would use the system end to end.  
  
Instead of obeying, I worked on my model of the settings system. There's the two things that are visible, and the two things that are invisible. All four are different in how we use them.  
  
Finding the invisible and modeling on it, I found something relevant.  
  
It's not only what there is that you need to track, you also need to track what is there but isn't visible. Lack of something is just as relevant than presence of something when you're testing.
