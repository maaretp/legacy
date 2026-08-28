---
title: "Not the same task"
date: 2016-11-06
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Mobbing]
source: https://visible-quality.blogspot.com/2016/11/not-same-task.html
---

# Not the same task

*Published 2016-11-06, updated 2017-07-22 · Labels: Mobbing*  
*Source: <https://visible-quality.blogspot.com/2016/11/not-same-task.html>*

---

I share experiences and thoughts I've had on mob programming and mob testing from my starting points and perspectives. I don't get to (yet) work with teams fluent in promiscuous pairing, I still struggle with getting people to pair with me across specialties (tester - developer -pairing) and a lot of the problems I'm facing are related to inability to make releases, or efficiently collaborate so that a lot of time would not be wasted on either waiting or doing the wrong things.  

I wanted to address a specific issue in the idea of doing a measured experiment on mob programming vs. pair programming vs. solo programming: the experience that it's not the same task and end result we're doing and getting into.

**The Ladder Effect**

I was mob programming with my team, and we all perceived we were working on something relatively simple: we needed to take out old Telerik UI components and replace them with new family of Telerik UI components. It was a task that most of my team's developers had individually done on other areas and we were mobbing just because we wanted to practice working together - learning together.

One of the developers was navigating and telling what to do, when another stepped in to suggest a better way. As the two had different ideas, we got a third idea and a fourth idea, and had a quick discussion on their benefits. The fourth idea would have never come about without hearing the first three proposals. This is what I think of as the ladder effect: you need the input of others to come up with the idea one of you has that the one having it thinks it is obvious and it turns out it isn't.

If each of the developers individually or in pair would complete the exact same task (which of course we don't, we're not researching but working to create value to production), the task is not the same. The resulting code is not the same.

Not the same may mean it's irrelevant. We always have bugs in production, and some of them are just not so relevant. It also may mean it is relevant. That there's work not done, to be done later either as fixes or as slower progress on the next features due to what was missing from the code.

To get the four ideas in, we would have needed an implementation, people caring to review in enough detail, at least once change of the whole approach to the change with a complete rewrite. So we shouldn't compare solo vs. mob with the idea that the end result in production is the same.

**A Stupid Little Thing**

In a solo work setting recently, I was looking at code to realize that the encouraged practice is to include a copyright header in each of the code files. A lot of the files we had recently been modifying had a reference to year 2012. In many ways, this problem is below cosmetic, as it is never visible in any way to the end users, as we don't publish the code. But housekeeping-wise, there's still a working agreement we'd update this to reflect current year on edit.

In individual work, whoever is bothered with these can go and fix them. But hardly anyone is bothered enough to do anything.

In a mob, when this comes up, the group realizes quickly how stupid and repetitive task updating these is. Where each individually would either just fix ones in their scope or dismiss the problem completely, the mob hearing a second mention tends to recognize a theme they don't want to hear about. And recognizing a repetitive thing that wastes effort of the whole group, it gets automated.

**A Big Difference**

One of the projects I recently completed with my team was a 6-month long refactoring/rewrite of something build over four years. Little did any of us know back when the problem started developing... But looking in hindsight, I can describe the problem. There was a solo developer would always get features done and into production, not the fastest of them all. He believed that code should be a tree in which you introduce a new branch when you get a relevant new requirement. By the time we realized what the beliefs were, he had seven full copies of the code conditioned to different versions of the code from start of the program.

Someone did review it, but the reviews were in vain. In face of a seemingly impossible task, people step down and focus on what they were supposed to do. While others in the team are conflict-averse, I have a tendency of taking up things others don't. Thus the rewrite, as a pair.

If we were mobbing, that result would have never happened. The developer creating the code with a significantly different belief system in what makes code maintainable could have learned sooner. Instead, he was doing code as he had done for the last 25 years.

Whenever I paired with the developer even for half an hour, I was exhausted for a week. I'm sure others had the same feeling. Working with him in a mob, we could share the load of dealing with the differences.

If it was up to me, that developer wouldn't be a developer. But it is not up to me. So I do what is the second best choice, help him learn. Mobbing was powerful in both building up the team to face the challenge, support in dealing with the challenge and eventually find the courage to fix the issue we had let build all too long.

**Starting to pay back is more relevant than cost**

All of the last stories I share are really about the task or the cost of the task to get it actually completed to the same level. But a lot of times, I find, the cost does not matter - time matters. If we have something in production in a week even if it took five people mobbing, over one person working for it for three weeks,  we'd rather get to a point where the investment starts to pay back faster.

We win customer gigs for speed - things that would never be our business' points of success otherwise. We have time to earn more money with the sooner availability. The little extra cost on development can become irrelevant quickly with scale in ability to sell the software.

There was a feature we said would take 6 weeks for us based on our previous experience on similar features. We mobbed on it for an afternoon with 7 people, 4 hours each. A pair of us continued and the feature was done two working days later. So 6\*40 = 240 hours and 7\*4 + 2\*2\*7,5 = 58 hours.

I'm sure the first estimate included significant wait times and interruptions that would happen a lot more over longer period of time. But the realized effort left a lot of time for reading books and studying that tends to be padded into our estimates, even if mobbing and pairing took the embedded time into that away. Fun is powerful mechanism. Yet, the cost isn't relevant. We won a customer case for that feature. That's what is relevant.

**Conclusions**

If I would want to compare individual work to mobbing, I would need ways of making the task the same. Both the individual and the mob would need to produce a result with the same features:

- Same value for production, including same lack of bugs
- Same value for maintenance, only to be revealed long-term
- Same positive impact on the future tasks done individually
- Same positive impact for the business overall

My evidence may be anecdotal, but it is enough for me to try more of this out. I welcome someone with resources to do proper research to do a good comparison. Then again, there's a gaping hole still on good research on individual and paired performance too. Setting up repeatable experiments is a lot of work, and meanwhile I'm happy to help my organizations improve using mob programming as one of the tools.
