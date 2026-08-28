---
title: "Milestone for a test resistant team"
date: 2013-06-29
theme: agile-teams-and-process
labels: []
source: https://visible-quality.blogspot.com/2013/06/milestone-for-test-resistant-team.html
---

# Milestone for a test resistant team

*Published 2013-06-29*  
*Source: <https://visible-quality.blogspot.com/2013/06/milestone-for-test-resistant-team.html>*

---

Whenever someone ask me if we're "agile", I notice I start to feel the need to apologize. Sure, we're on that journey with some criteria, but not there on so many others.  
  
For example, my team is somehow trying to have everyone do "testing", but their idea of testing easily could be "development buffer", "try it once" and "go for coffee, you can relax now". When they manage to find the motivation to pair up with another developer, it's a little better, but the enthusiasm never last long for repeating anything.  
  
While agile teams could be test infected, this one is long on the route to be test resistant and the probabilities of a sudden infection are not getting better yet.  
  
The team has rounds of "let's automate tests in some way" behind them. The most recent one on unit tests went the furthest, with some of the team managing to refactor the code to add tests (one out of nine) and others came up with all sorts of reasons why legacy code made things too difficult for them. The round before that was to take a summer intern and ask him to record tests based on test cases the team had done. Those tests were never run by anyone other than the intern.   
  
For the unit testing effort, I negotiated 1/4 of the teams time over a 6 month period, so unlike usually, the external schedule pressure was really to the problem. We created structures where we could do relevant refactoring, but too  little of that happened. And we had an external coach to help us with the tests just a little, with the end result of us realizing the vastness of refactoring / architectural change that would be needed to get where we want to be.  
  
With  the unit test automation gone and the problems of not enough testing happening, we agreed to do some group exploratory testing sessions. With a few of them under our belt, they seem to do the job for now, but with the late feedback and the repeating nature of checking similar situations are wearing out the developers. This will not last, not for this type of information need.  
  
In one of our group exploratory testing sessions, I drifted off to look at my team mates and think about the next experiment in the efforts to make it better for us. We had failed with UI automation and none was interested in touching it. No one wanted to spend their summer on automating tests that would not be helpful. So I called a consulting colleague in testing, and we talked about the smallest possible thing and timeframe we could set up to do a selenium proof of concept. I could do that myself, if it did not include learning that I did not have time for right now. But I knew enough to explain to my boss why we'd invest on an external to do something like this right now.  
  
The proof of concept was delivered this week, in a meeting with the whole team. The proof of concept showed developers a style of tests they would accept as part of their work. This time, the external did not set up extensive suite of fragile scripts to throw to the developers to maintain, but a few structured examples and a useful explanation of what doing these include for our software. The external did not introduce new tools or languages, but just a driver for the browser interface that could be called from the code as we know it now. Owning small scope from someone else created positive buzz, and if the time frame of setting up was longer, we'd have more implemented but less sense of ownership.   
  
The tests were integrated right away into the local code repository the consultant had no access to. And they ended up being run with the build cycle to find a problem on their first day of existence, a side effect of common services change that did not work in this area quite as the idea was with a big visible error message - just the type of information we usually look for in the release testing. And the problem was quickly fixed to get the tests back running again.   
  
For the first time, I think there is an actual chance this will fly. And next I'll need to find ways of showing what else there is in the lovely world of testing.
