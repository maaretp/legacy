---
title: "Introducing Test-Fix-Finalize week monthly"
date: 2012-12-04
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2012/12/introducing-test-fix-finalize-week.html
---

# Introducing Test-Fix-Finalize week monthly

*Published 2012-12-04*  
*Source: <https://visible-quality.blogspot.com/2012/12/introducing-test-fix-finalize-week.html>*

---

About three months ago, being the only tester in my team of 8 developers all finishing their work in the last minute to release, I was thinking about possible solutions I'd go about suggesting. I started discussions with a project manager and my personal manager with the idea of introducing agile planning and following remaining work so that testing would be included. For various reasons, right when we started talking of this I realized this is not about to go through: the project manager was not ready. So I changed what I suggested and went with the "need time in schedule for testing to happen" and "one of me can't do all the checking & exploring on the last week alone so team needs to help".   
  
The idea was formulated a bit more and soon I found myself in front of a steering group allocating the whole team to "testing" for the last week of each increment we decided to call Test-Fix-Finalize. It's very much a waterfallish approach to leave testing (some testing, not all though) in the end and it's really not what I see us aiming for. But, with a team with no automated unit tests and a culture of "let the others' do the testing" this seemed like a smart next move.  
  
For the Test-Fix-Finalize week we identified our team would be working on brain-engaged testing (sometimes pairing up), fixing whatever was found and needed to be fixed and for any time we could, on developing the unit tests further.  
  
We have now two of these Test-Fix-Finalize weeks behind us, and I feel puzzled.  
  
On the first one of these, we tested to find nothing that needed to be fixed. Yet, there has been few issues in found in production we missed. This doesn't surprise me, though - there's quite much width and depth to what might need to be tested, and the our best bets for choices did not pay off in the optimal way. Most of the team did not work on the release testing though and looking at the issues the added investment wouldn't have been worth it either. Some of the developers worked on unit tests and refactoring to make them possible, and others chose to do manual testing of a major refactoring that looked awful lot like fixing and developing. One opted to help me with the release testing, and while I found something yet nothing that was newly introduced, he just found nothing (yet the area he works in cannot be touched without finding something).   
  
I talked about the experience to realize three things:  

- The developers can get better at checking, but their style of manual testing may still long be just confirming their designs - lots of paired work may be ahead while some already is done. Having them do work they don't know how to do (and sometimes feel like don't want to do) will not provide the results we seek.
- It might be a better strategy to use all weeks, including the final week on some test automation stuff since that approach wouldn't leak much more than the current one but might get better over time. We could take the risks while development still is as careful and fast to fix reported issues as they are now.
- The themes in this particular increment were such that there was not as much to test as had been when I introduced this week. The cycles in how things come in had made the team focus on fixes and enhancements and not major features.

Along came the second Test-Fix-Finalize week. In this cycle I had all developers focus on unit tests, even the ones who wanted eagerly to do manual testing that looks like fixing. We talked and I suggested they'd use the week as an opportunity to learn and try things out - quality over quantity. This month we had significant new features coming in, in the extent that at the start of the month we were already discussing how we'll cope with the last week at all, to learn that we could set up schedules and order of work now - finally - in the order where we considered testing timeframe outside the last week. So to my surprise, two of the three major change areas for the month were tested before the last week. This time with less testing hands on the last week than before, we found two issues that needed addressing before release (out of all the ones that need addressing at some point). One of those issues was such that it alone was worth the effort. Then again, being realist, I know that it would have been caught by the next layer of our internal product management trying things out too - it was way too visible to miss.  
  
End results I'm still processing. There were significant individual differences on whether people could grasp the unit testing and a fair amount of disbelief it will help us finding the things that end up breaking due to their nature looking back at the time I've had the pleasure of being there. We're also noticing that introducing new developers (which we've needed to do) is tipping the scale to another direction than the seasoned product expert developers on the amount of unintended side effects.  
  
One good thing on these experiments, though. I have something to show on the results, and the project manager may finally be ready to bend towards us planning the release together in more of an agile-style planning.
