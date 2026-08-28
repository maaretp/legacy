---
title: "Finding bugs serendipitously"
date: 2018-10-02
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/10/finding-bugs-serendipitously.html
---

# Finding bugs serendipitously

*Published 2018-10-02, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/10/finding-bugs-serendipitously.html>*

---

Serendipity means 'lucky accident'. As I speak of doing shallow exploratory testing, a colleague expressed their fear of finding all the bugs they find serendipitously.  
> "I feel like most of my bugs are serendipitous, and that concerns me."

I wanted to share a story, and a perspective.  
  
As I joined a new job, the one before this, I was determined to do hands-on good quality testing on my first week at the new job. I've had the experiences of joining companies before, where I find myself being trained into the company, without actually doing any of the work I was hired for in the first weeks. And I wanted things to be different. I wanted the old saying of "people taking months in a new job before they are productive" not to be true and set that out as my goal.  
  
As I arrived office, they gave me access to the system I was to test. I could barely get my computer open, log into the system with my credentials, bookmark the page to remember where the system was and I was already dragged into a four-something-hour meeting spree where they poured information into my head I have absolutely no recollection on.  
  
In the afternoon, I returned to my computer with the original determination, and I opened the application only to see a big visible crash.  
  

[![](../_images/screen-shot-2018-10-02-at-7-40-13-855e45ca.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXXrEthbiQbCztN-2-Y85SDStnq5hadSuGLq0QAyd7Ocpo5VunZndKs1yRuwFf6sA95wyPohp48yp2fSBbG39lFeraTjlDOAsfmL-RmFAERQjYlCxqTDPE-kZZZ5SOGHhSGye_fHHBGNI/s1600/Screen+Shot+2018-10-02+at+7.40.13.png)

I had done NOTHING. No use of my brilliant testing skills. Very very shallow testing at best. Anyone would see this problem. Except they did not.

I had serendipitously found a bug of linking one particular subpage of the application (I had managed to click ONE thing after logging in before linking it) that crashed when login was no longer valid, and when we investigated the bug with the developers, we learned it was also the ONLY subpage of that type. I honestly got lucky that day, but I would have over time increased my likelihood of running into this with the ideas to do exactly this I was in control of because of the Elisabeth Hendrickson's Cheat Sheet.

A lot of the depth in testing comes with skill, and knowing how to exercise a variety of ideas. But much of it also comes from serendipity combined with recognizing problems when you see them (a skill!) and just sticking with the applications longer.

Serendipity sounds like just luck, but it is particular kind of luck combined with skill and perseverance.
