---
title: "A look into a year of test automation"
date: 2017-08-22
updated: 2018-12-26
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2017/08/a-look-into-year-of-test-automation.html
---

# A look into a year of test automation

*Published 2017-08-22, updated 2018-12-26 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2017/08/a-look-into-year-of-test-automation.html>*

---

It's been a year since I joined, and it's been a year of ramping up many things. I'm delighted about many things, most of all the wonderful people I get to work with.  
  
This post, however, is on something that has been nagging on the back of my head a long time, yet I've not yet taken any real actions on doing anything other than thinking. I feel we do a lot of test automation, yet it provides less actionable value that I'd like. A story we've all heard before. I've been around enough organizations to know that the things I say with visibility into what we do are very much the same in other places, with some happy differences. The first step to better is recognizing where you are. We could be worse off - we could be not being able to consider where we are with evidence of things we've already done.   
  
As I talked about my concerns out loud, I'm reminded of things that Test Automation has been truly valuable on:  

- It finds crashes where human patience of sticking around long enough will not do the job, and makes random crashes into systematic patterns with saving results of various runs
- It keeps checking all operating systems where people don't do that
- It notices side effects on basic functionality in an organization where loads of teams commit their changes on the same system without always understanding dependencies

However, as I've observed things, I have not seen any of these really in action. We have not  built stuff that would be crashing in new ways (or we don't test in ways that uncover those crashes). We run tests on all operating systems, but if they fail, the reasons are not operating system specific. And there's much simpler tests than what we run to figure out that the backend system is again down for whatever reason. Plus, if our tests fail, we end up pinging other teams on fixes and I'm growing a strong dislike on the idea of not giving these tests for the teams themselves to run that need pinging.  
  
Regardless of how I feel, we have now invested one person and a full year into our team's test automation. So, what do we have?  
  
We have:  

- 5765 lines of code committed over 375 commits. That means that we do 25 pull requests a month, of average size 15 lines per commit.
- The code splits into 35 tests with 1-8 steps each. My reading perception is that I'm still ashamed to call the stuff these tests do testing, because they cover very little ground. But they exist and keep running.
- Our test automation python code is rated 0.90/10 with Pylint. The amount of complaints is  2839 things. That means that every second line needs looking into. The number is worse as I did not set up some of the libraries yet.

In the year, I cannot remember more than one instance where the tests that should protect my team (other teams have their own tests) have found something that was feedback to my team. I remember many cases where while creating test automation, we find problems - those problems we could find also just diligently covering manually the features, but I accept that automation has the tendency of driving out the detail.  
  
I remember more cases where we fix automation because it monitors things are "as designed" but design is off.  
  
I know I should do something about it, but I'm not sure if I find that worth my time. I prefer the manual approach most of the time. I prefer to throw away my code over leaving it running.  
  
There's only one thing I find motivation in while considering I would jump into this. It's the idea that testers like me are rare, and when I'm gone, the test automation I help create could do some real heavy lifting. I'm afraid my judgement is that this isn't yet it. But my bar is high and I work to raise it.   
  
As I write this post, I remind myself of a core principle:  
> all people (including myself) do the best work they can under the pertaining circumstances.

Like a colleague of mine said: room for improvement. Time to get to it.
