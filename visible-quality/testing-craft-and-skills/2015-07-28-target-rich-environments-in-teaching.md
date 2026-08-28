---
title: "Target-rich environments in teaching testing"
date: 2015-07-28
updated: 2016-08-02
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2015/07/target-rich-environments-in-teaching.html
---

# Target-rich environments in teaching testing

*Published 2015-07-28, updated 2016-08-02 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2015/07/target-rich-environments-in-teaching.html>*

---

Some years ago, I looked at all the testing courses I was doing and I felt embarrassed. I had to come to the conclusion that on a course *talking about testing* is completely different from *doing testing*. All my courses by that time had exercises, but none of them was exercise-centric. They were entered around folklore, thing I had learned in working on testing that I felt would be useful for others.  
  
I love hearing people's stories about testing. I love telling my stories on testing. And according to the smile sheet grades, I did well with my stories. But the skills of testing don't really get built without actual experiences on trying to test, succeeding and failing and getting feedback. Seeing hands-on examples of how other people tests.  
  
I started experimenting with what I called "Exploratory Testing Work Course" - a course where we'd take an application and ideas of exploratory testing and test to learn more on how to test.   
  
For a long time, I've used FreeMind as the target application. It's great in many ways. It's open source (although it is very hard to get to compile from the sources...). It has relevant downloads and presumably a user base. And it's full of bugs. It's what I would call a *target-rich environment for testing*.  
  
Target-rich environment can be great in teaching testing. When you find problems all over the application, it gives you a feeling that you're in the right track: you can be good at this. I've had very insecure testers on in-house acceptance testing oriented courses who just needed the encouragement to shine in their tester role. And for this, target-rich environment is great. Everyone finds problems. Everyone finds problems others won't find. And exploring makes finding the bugs easy and fast.  
  
But this is a slippery slope. After logging a hundred bugs on a feature, I ask if we could advise releasing it based on what we know about it. And the answer is almost unanimous: no. But we're actually talking about software that has been released, software that is in use and software that does not have a forum full of angry users complaining about the bugs we're experiencing.  
  
So recently, I've been occasionally changing the target application to a company-specific application. The courses where we explore software I have never seen before and learn about it to find problems have been great with turning focus into learning testing as opposed to learning a new subject matter with an unrelated app I just nominated. It's been interesting to see how little people think around their own software, how few questions they ask of its purpose to exist and how hard it is seeing connections. And I've been trying to find a way to replicate some of those lessons to my exploratory testing courses by choosing another test target.  
  
Most recent one I'm using is Dark Function Editor. It creates 2D sprite sheets. Animated gif editor. Around it I've found it possible to teach seeing things while using it. But for finding bugs that sucks. It has bugs and I've found many. But many people will have hard time seeing the bugs there, as you need to work harder to expose them.  
  
Testing should not be that easy. But sometimes it is. So think about it: do you work in a target-rich environment? When testing is easy, you need to work harder to stretch to different ideas and observations. Like when walking on a field full of holes, it takes a lot of energy to walk steadily around the holes. Which one do you actually prefer as a tester? Would you feel disappointed if you tested for weeks without finding a single problem?  
  
I believe agile is taking us slowly towards less target-rich environments. In those environments, more skill is required in the exploration you do.
