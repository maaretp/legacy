---
title: "Optimizing efforts into bug reporting"
date: 2014-05-01
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Agile]
source: https://visible-quality.blogspot.com/2014/05/optimizing-efforts-into-bug-reporting.html
---

# Optimizing efforts into bug reporting

*Published 2014-05-01, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2014/05/optimizing-efforts-into-bug-reporting.html>*

---

A colleague from another company contacted me  asking about numbers on how many bugs testers find per a time unit. I remembered checking that number for our organization last autumn for a presentation I gave, and now checked again to see if had changed. It's not our goal or connected in any way with how we set goals, but I find it occasionally an interesting trigger for thinking through the results. The number had not changed at all - we log 5,8 issues for a day. It was the same when I was the only tester, it was the same when the second tester started learning and it's still the same for the two of us combined. Somehow it's more of a number that reflects the point when we prefer doing something else than logging issues.  
  
We also had a paired testing session for the two of us. During the two focused hours, we covered rather shallowly a new area we had not had time for otherwise to find about 20 issues. As the area was in the other tester's product (current split of responsibilities is that I only manage on this product's team) I left all the issues to be logged for the other tester. Later in the afternoon she mentioned that she will need to leave the logging of issues for next week, as there's resolved issues to work on and two days of out-of-office ahead for her. This triggered my favorite concern, the amount of time wasted on good and detailed bug reporting out of habit. And after all, that's what testers are taught. I replied to say I will quickly put one issue with all the bugs I saw, just copypasting my notes in that one issue. The reasons for unclear summary style reporting are many in this case:  

1. Copy-paste of notes with the unclarities takes me 30 seconds, while clear repro steps in step-by-step style easily take 5 minute each. With 12 in the queue, that's an hour of work!
2. Unclear reporting triggers the devs to talk to me. And they do, often. The positive impact of those discussions have been significant.
3. The oneliners tend to be already enough to get the bug in the first place - most of the time. Not writing for the audience but on template wastes effort.
4. If I reported now, the devs could already fix them. And some of those most likely will before there is the time in calendar that would allow the detailed logging.
5. The rare skill in our team is to see problems. There's plenty of developers to isolate the problems if they're hinted there is a problem.

There's a huge difference in the reporting style for me and the other tester. If you've taken Cem Kaner'sbug advocacy or read articles on clear bug reporting, the other tester does all that.  But the other tester also must invest more time in logging. I write onliners describe just the relevant data, and let pictures talk for me. If my current reports were showcased to externals, they would not be clear enough. But it seems, asking the developers, that most of the time they are sufficient. And they can always trust me to demo things for them.

Imagine the amount of wasted effort on the detailed reports if the detail is not necessary: 5,8 bugs every day for two 25 months with 20 working days. 242 hours if 5 minutes per bug was enough.

I'm a big fan of thinking all activities - including the selection to log issues imperfectly or leave them unlogged completely using your judgement - in the frame of opportunity cost. With another choice of allocation, could you have done something more valuable? Not just the cost of testing, but the costs in development. Bug reporting in the way most books describe is not a best practice. My style isn't either. But my choices seem to fit this particular context - for now. And I can ask, as the test manager, the other tester to start experimenting with a new, quicker style of reporting that will take her probably out of her comfort zone.

*Later addition*: Asking the developers on the preference I learned two things. They find the step-by-step descriptions wasting their effort - they need to learn long stuff to get something they could get in more concise form. And they have been annoyed - without ever saying a word - that all bug reports are logged in evenings, as in they are kept in store for the whole day when there is a chance to do something about them. Know your audience. Ask, try different things. Pay attention to things that people don't say.

  
*Yet another later addition*: I seem to have offended the contracted tester's manager by making a claim of "all bug reports are logged in evenings", when the data shows that only a majority but not all of bugs are logged after developers leave office at 15.00. Just to be clear, I added a the previous report of verbally transferred information, and whether it is all or some, it is a feeling that was was stated. I reported that not to offend, but to note that the pacing of how we choose to report with regards to when we find the issues also has an impact the developers notice.  
  
Choices of my word may be incorrect as in all vs. majority, but they are well meaning to describe recent events that reflect stuff that I have also learned over the years. I don't do safety language that well, but don't intend to stop writing because of it.
