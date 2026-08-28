---
title: "Managing Testing based on Threads"
date: 2018-09-28
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/09/managing-testing-based-on-threads.html
---

# Managing Testing based on Threads

*Published 2018-09-28, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/09/managing-testing-based-on-threads.html>*

---

Session-based Test Management is a form of managing testing based on sessions - time boxes where ideally we could maintain focus, have a clear charter and generate some metrics by counting things around time boxes and results. I believe it is not one practice but many, but way too many ways we manage testing based on session get bundled with the original description of a technique that is very specific.  
  
Later on emerged the idea that sometimes assuming you could maintain focus for a time box may not be possible. You might be interrupted, for various reasons. You may be jumping between this thing and that thing, and that way of managing testing was then dubbed Thread-Based Test Management.  
  
Here, I wanted to describe one very recent experience from my work, that utilized managing testing based on threads, and some observations around how we ended up organizing and what unfolded in the activity.  
  
Yesterday, we were wrapping up a release. Making a release in general is still a bit of an effort in my team, even if we have moved from it taking a week into it taking a few hours. But yesterday's release was special. It was a release we were shaping together to introduce two major product upgrade paths. each with their own logic, risk of dependencies in a complex environment and need of many pairs of eyes in verifying the functionality, each configuration and environment and problems we may be experiencing and resolving on the go.  
  
We had strategized on a whiteboard the day before, in a session I considered magical. The three people around the whiteboard built on each other, added knowledge, clarified priorities and made an action plan we were ready to execute. The overall work would be done by eight people, which means a bit of coordination is required unless we somehow magically dance just right together.  
  
In the morning, we got the build we through could be the one. We knew there were many things to do, and started a discussion thread - one single thread - in out teams chat. It did not take long for it to grow to hundreds of messages, and confusion to emerge on who was doing what, who was talking about what and what was really done and what was just a miscommunication. A colleague jumping into the discussion at some point exclaimed the awfulness of mixing it all there, and while I and the two others around the whiteboard could track with the model inside our heads, the other five people and everyone watching was in pain.  
  
Seeing it did not work, we came to two immediate solutions.  
  
First a Jira ticket got created by one of us just announcing they would now track the work there because the discussion was awful. They wrote down 13 steps to making a release, mentioning the two upgrade paths each as one step.  
  
Almost same time, I pulled out the tasks intertwined and introduced them as threads: things we'd try to drive through, with some idea of priority and their status as they were named.  
  

- Thread 1 was about "release as usual" - all the moves we had done and practiced for all the previous releases and it was just business as usual.
- Thread 2 was about the most business critical of the two upgrade paths, and we had not set up the environment to be able to test that at all.
- Thread 3 was about the second upgrade path and we had just identified a blocking bug that needed addressing before it would make sense to finalize it
- Thread 4 was a surprise path of fast forwarding thread 3 in a specific way
- Thread 6 was doing thread 2 in production environments
- Thread 7 was doing thread 3 in production environments

Half a day later, we added thread 5 (because just for the fun of it, of course someone needed to make a joke of an off my one error) on yet adding test automation for thread 2&3 and not accepting to have to do this stuff without help of some tooling ever again.

Teams wasn't making the thread management that easy, jumping focus where ever someone typed in something, and due to the abilities for us to use teams in anything but one long thread, we did not always trust a comment hit the right one. But they did, and we clarified and worked through each thread. The visibility per thread enabled people to call out for help in a more specific way, identify problems with each of the separate goals we were working towards and make priority calls of what we'd do first and later as this was heavily changing as we identified and investigated problems.

The Jira ticket looks clean, as if one person did it all. The threads in the discussion enabled us to start with a task that we discovered as it was happening, and coordinated many people pitching in information from test results, investigations, availability of fixes and plans for next steps and definition of being done with each of the threads.

I wanted to share this experience as a reminder that threads may be a thing you want to visualize to share the load. Uninterrupted time is not something to use on all tasks. Sometimes threads are the best thing you can do. And they may enable discovering the work that really needs doing, whereas Jira ticket gets people to deliver what was asked and forget to discover many things that are implicit.
