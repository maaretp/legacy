---
title: "When bugs feel too simple"
date: 2014-01-03
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2014/01/when-bugs-feel-too-simple.html
---

# When bugs feel too simple

*Published 2014-01-03*  
*Source: <https://visible-quality.blogspot.com/2014/01/when-bugs-feel-too-simple.html>*

---

I've spent today testing a feature reading its specification. I let the specification reading bring ideas into my head, and follow them - with the result of logging quite many bugs.  
  
One bug in particular was a tipping point today on how I feel about my usefulness.  
  
I was reading the specification mentioning copy feature, to realize that I've tried the feature but I have not really owned the data I'm copying, that is, intentionally creating it to be something that I would find relevant for this copy action. So I created the maximum data (filling in all the fields) with data that I could recognize (naming everything so that they tell about their location) and hit the copy button.  

[![](../_images/error-642e6c09.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDO0v8AgHseWYQ_SGtyTt00K3fnEd28YqrunwRFstNg-bJkxr7GCgdeTHAGSQ0oX3ko6tQF_uPJ_Goh23kjSycMSEC7qH0AIUP2itUTdhJTgjDyJwrdVcUc-XBWArWghDVXnlY2X3moKk/s1600/error.gif)

  
  
  
With some more tests, I could pinpoint the piece of data that was causing the problem, and the problem is not about the contents of the data I entered, just about me filling anything in to a particular field.  
  
With  this bug, I could not help but to feel frustrated. A very simple way to see if a feature works is to use it. And if you will use it, why not use it with full data?  
  
This example is from a team with me and six developers. I'm a part timer on the product, developers are full timers. And yet we, continuously, over and over again, regardless of all the discussions about developer testing end up with this: evidence of not having used the feature.  
  
I went digging into the bugs I've logged in the last few weeks, and came to a very depressing conclusion. None of the bugs I've found required any more sophistication than this one. All it takes is a little time with the product.  
  
Need to start doing something about this. Again and more. This is not a skills issue. This is an attitude issue. Developers can test this. For a reason I don't really get out of my team in discussions, their testing for these issues just does not happen often enough.
