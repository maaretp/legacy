---
title: "Think Testing as Fixing"
date: 2018-09-01
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Agile]
source: https://visible-quality.blogspot.com/2018/09/think-testing-as-fixing.html
---

# Think Testing as Fixing

*Published 2018-09-01, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2018/09/think-testing-as-fixing.html>*

---

"Wait, no! We have not promised THAT!", I exclaimed as I saw a familiar pattern forming.  
  
There was an email saying we would be delivering feature Gigglemagickles for the October release. We had not really even started working on it. We had just been though our priorities and it wasn't on them. And yet someone felt certain enough to announce it.  
  
I started tracking what had happened.  

- In June, someone asked if Gigglemagickles might work from a tester. They reported that they had ONE TEST in test automation that wasn't failing. It wasn't testing the whole thing either, but it wasn't failing. We could be carefully positive.
- In early August, someone asked me if I thought it should be done, and I confirmed it should *if* we could consider not building a software-based licensing model that would enable forcing a different pricing. We did not agree we would do it, we just talked about it making sense.
- In late August, it had emerged into emails and turned into micromanagerial Jira tickets assigned for individuals in my team telling to test Gigglemagicles for compatibility.
- Since it was now around, another micromanagerial command was passed from a developer for a tester to start testing it.
- As I brought the testers back to what needed to  be done (not Gigglemagicles) we simply added  a combination test in automation suite to know if there was a simple way of seeing Gigglemagicles did not work beyond the one test.

What a mess. People were dropping things they *really* needed to do. They were taking mistakes as the new high priority order, without much of critique.

Half an hour later with testers back on track, we found big problems on other themes that we had promised. Diversion was postponed.

We failed again at communication. Gigglemagicles alone was probably ok as a client feature. But it depended on a backend system no one asked about or looked at. And it depended on co-existence with other features someone was now adding as a testing task for us, at a time when there was no time available. We had fallen to the developer optimism again: we don't know of implementation tasks, so let's promise it is ready. The bugs we have not yet found are not our concern. The testing undone isn't my problem.

Let's all learn that we need to think of testing as FIXING. If we don't have things to fix after testing, we could just hand it out now. But we do, and we need to know what to fix. That's why we test.
