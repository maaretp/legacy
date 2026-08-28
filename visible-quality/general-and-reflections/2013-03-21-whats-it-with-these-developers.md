---
title: "What's it with these developers?"
date: 2013-03-21
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2013/03/whats-it-with-these-developers.html
---

# What's it with these developers?

*Published 2013-03-21*  
*Source: <https://visible-quality.blogspot.com/2013/03/whats-it-with-these-developers.html>*

---

Funny how varied my job as the teams' tester can be with two very small teams - even within one team - depending on what we're working on.  
  
In the last six months, some of the developers have been working with "refactoring" a major area - rewriting, adding completely new functionality, including a redesigned UI and change to the core concepts the who code relied on. So, not exactly a refactoring, but just a major development effort.  
  
The fellow in charge of this change as the head developer finds incremental development uncomfortable, and prefers to work in layers, where everything is undone until the very last moment. Not exactly a tester's dream. So, I have a waterfall within incremental development model where we normally release once a month and get to do continuous testing.  
  
I created a schedule-sort of a test plan, to show what time boxes I would need for testing, and how that would spread over the schedule, as I just can't do two days of work in one. We got an extra month into development schedule with this, and for a while I thought we were on track.  
  
But, as the schedule was extended, with the unease of incremental development, the extra schedule was eaten up by development. I could test, but not really - as nothing worked and all of it was "known" since it was not finished.  
  
Then, in schedule comes the time when we're supposed to merge the branch with the main. This means, in our terms, that no other features will go out without the new stuff, and if things would be bad enough, it would break the monthly cycle of releases. We discussed whether to merge or not, with developers, myself as the tester, and product management. The decision making was interesting to follow up. Product managers wanted developers to say they have "implemented everything" and declared bugs are not a problem, we can just fix them. My argument of not knowing the bugs yet - not having tested - was dismissed. There should not be many problems anyway, that's why we had "refactored". I tried asking developers on their own testing, and they said they had not done any, because schedule was so tight. Adding 2 hours of product management basic flow testing they decided it works already and a promise of 2,5 weeks of testing next month, they decided to merge.   
  
Since that meeting, testing has happened. The product management 2,5 weeks has turned into 30 % of what it was supposed to be and has found some issues. In total, we've logged 100 bugs since it was "completely done" by the merge, and I'm totally failing in getting anyone to understand that there isn't any feature that would have worked so far so that I could have actually tested it except to log a bug that I can't in some aspect that is relevant.  
  
When I test and find issues, they are always "5 minute fixes". It's interesting though that one developer can do 5 of these 5-minute fixes a day, and the other 0.6 a day. I know they are not really 5 minutes with all that goes around it, but that's still the message I have to listen to - after all the hard work on finding them, which takes definitely more than the 5 minutes on my part.  
  
Again yesterday we discussed the status and the plan. And yet again, the developers say they will just work in order of priority, without doing any estimation of what the risk is to business on releasing the stuff we have now. After all, they are still 5-minute fixes even when the customer needs to find them.  
  
There's two things I keep wondering:  

- What would it take that any of the customers would actually get upset with the quality they are delivered - they seem to settle for an interesting amount of problems
- What would it take that the developers would actually respect the effort that testing takes and would include at least some fixing time in their estimates instead of claiming perfection and not learning from the daily feedback

Fortunately, even in the tiny teams I work with, people are different. But I find it exhausting to be the only tester when I feel constant belittling on "works with eyes closed" and "five minute fix" attitudes. And, they've managed well without tester before. I warned my manager when joining of the quality getting worse when a tester is introduces, as there is a tendency of externalizing the responsibility of knowing if possible.  
  
I keep asking - I'm willing (and able) to do the implementation work to an extent. Would it be too much to ask that the other developers would be willing to do some more of the testing work?   

Talk about "solo player..."
