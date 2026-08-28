---
title: "Exploratory Testing: It's not what you think it is"
date: 2016-07-28
updated: 2016-08-01
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2016/07/exploratory-testing-its-not-what-you.html
---

# Exploratory Testing: It's not what you think it is

*Published 2016-07-28, updated 2016-08-01 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2016/07/exploratory-testing-its-not-what-you.html>*

---

I just finished my small session on "Exploratory Testing an API" at Agile2016 -conference. The session lead to two insights I feel compelled to share.  
  
Imagine being handed google search box and being asked how you would test it. You come up all sorts of different inputs quickly,  Some of the very basic searches (character sets, number of words, types of search criteria) might lead to think about something more, like exact matches or searching for something that has a connected functionality like airline codes or currencies or vocabulary definitions. You know that's now all the testing for Google, and probably consider it is not the best way to test Google search all in all. But ideas start flowing quickly.  
  
When presented an API, with a "fill in the blank" type of place, we freeze. The same things we could easily come up with while looking at a GUI, we don't and end up blankly staring at the IDE that is really just providing us a GUI to get using an API.  
  
But the more relevant thing I started thinking is that how much of a disservice it is for all of us testers to let exploration examples always be guided to "fill in the blank" types of exercises. I had someone in the audience who clearly decided that was the purpose of the exploration, and surely, it can be one of the purposes of exploration.  
  
But as a professional exploratory tester, I must say that I find that the examples we're presented at the conferences on quick tests poorly reflect my work. I look at an API, and the only reason for me to fill in the blanks is to acquire information - about the environment where this all sits in, about why would anyone want to use this, what is this for?  
  
As my session gyrated this time to filling in the blanks and less on the actual exploration to learn, I feel more strongly about this. I need better ways of helping testers on the right track.  
  
Because the testers who stay on the "fill in the blanks" track thinking just about inputs, they should have been out of job already a while ago.  
  
It's not about finding any problems, it's about finding problems that matter.  
  
I find it much more relevant to find out why a product isn't selling (well, it's free, so selling is not really what I mean here...) and how it could be easier for new people to get started with it, than figuring out that a combination "a§" ends up incorrectly saved in a text file.
