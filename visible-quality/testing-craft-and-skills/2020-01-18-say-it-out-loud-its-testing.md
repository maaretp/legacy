---
title: "Say It Out Loud - it's Testing"
date: 2020-01-18
updated: 2020-04-13
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2020/01/say-it-out-loud-its-testing.html
---

# Say It Out Loud - it's Testing

*Published 2020-01-18, updated 2020-04-13*  
*Source: <https://visible-quality.blogspot.com/2020/01/say-it-out-loud-its-testing.html>*

---

Sitting in front of their computer, with a focused expression on their face, the tester is testing a new feature. Armed with their notes from all the whiteboard sessions, from design review and passing by comments of what we're changing and whatever requirements documentation they have, they've built their own list of *functions* they are about to verify that exist and work as expected.  
  
"Error handling" says one of the lines in the functions list. Of course, every feature we implement should have error handling. Into the user interface fields where a sum of money is expected, they type away things that aren't numbers and make no sense as money. With typing of "hundred" being ok'd and just saved away to be reviewed later, it is obvious that whatever calculations we were planning to do later to add things up will not work, and armed with their trusty Jira bug reporting tool, they breathe in and out to create an objective step by step bug report explaining that the absence of error reporting is indeed a bug.  
  
Minutes later, the developer sharing the same room just pings back saying the first version did not yet have error handling implemented. The tester breathes some more.  
  
---  
The thing is, errors of omitting complete features are very common finds for us testers. Having found some thousands of them over my tester career, I'm also imagining I see a pattern. The reactions to errors of omitting complete features very often indicate that this did not come as a surprise to the developer. They were giving you a chance of seeing something they build incrementally but weren't guessing \*you\* would start your testing from where they would go last in their development.  
  
**A Better Way**  
  
When you build your lists of functions you will verify, how about sharing your lists with the developer. Having a discussion of what of these they expect to see work would save you a lot of mental energy and allow you to direct it to their *claims*, going deeper than just the function. With that list, you would most likely be learning with them that "Error handling" for this feature won't yet be in the Wednesday's builds, because they planned on working on it only from Friday on.  
  
You could also ask in a way that makes them jump into showing you where the function is in code. Even if you did not understand code, you understand sizes of things. Seeing something is conceptually one block of code, another one is sprinkled around when they show it, and something is very big and makes you want to fall asleep just looking at it are all giving you hints on how you would explore in relation to what your developer just showed you.  
  
If you read code, go find some of that stuff yourself. But still, drag your developer into the discussion as soon as you suspect something might not be there.  
  
**Code Reviews vs. Testing**  
  
When organizations review code through for example pull requests, errors of function omission are hard ones to spot without someone triggering this particular perspective. If you have a list of things that you expect to see implemented and one of them is missing, there is no way that functionality could end up working in testing.  
  
Sometimes, when you have a hunch of something that was discussed in the design meetings being forgotten from the implementation, the way to go about figuring it isn't to install and test - it is to ask about the feature. Say your idea out loud, see a developer go check it, and learn that something not implemented has no chance of working.  
  
Jumping always to testing isn't the only tool you have as a tester, even if you didn't write (or read) code.
