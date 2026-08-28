---
title: "Continuous delivery without test automation, first experiences"
date: 2014-06-26
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2014/06/continuous-delivery-without-test.html
---

# Continuous delivery without test automation, first experiences

*Published 2014-06-26*  
*Source: <https://visible-quality.blogspot.com/2014/06/continuous-delivery-without-test.html>*

---

It's been a few months since I managed to get my favorite team at work talked away from Scrum and story points into a Kanban-like continuous delivery of an item at a time. There's a long way to go, but first two months are a good point of looking back at some of the things that happened.  
  
**Giving up on size estimates**  
  
The driver behind the change for us was the frustration with size estimates: story points and hours alike. We observed that the size did not really matter for us, and the ritual of sizing things up was draining our energy. In particular, if there were surprises, things to be learned while doing, we easily ended up with unproductive discussions of how the thing was understood when sized up and how it is understood now as 'requirements changed'. If the team understood the problem, solving it was design. If they did not, solving it was requirements. The externalizing was unhealthy and unproductive.  
  
I kind of like the change in discussions this caused. Instead of sizes we talk of when could I help with testing it and where, and if we can split it into two (or more) deliveries that would already bring value to the end users. Not very good at that yet, but we had not done any of that before the change.  
  
**Releasing regularly**  
  
In an earlier post, I wrote about the feeling of ease with making releases as they are done continuously. It's a routine, not a hassle. While our continuous delivery does not (yet) rely on test automation, we're not as fast as we could be in making a feature release-ready, but we are capable of analyzing our changes  one by one, thinking of likely side effects and testing manually. And isolating a feature at a time makes it much simpler to understand what caused problems. I really loved last Thursday, when the build completely broke with two lines change that was the only thing in the build we were working on towards the release. We jumped right in to solve the surprises that none of us could foresee.   
  
The two months also taught us about releasing regularly through trial and error. As Git and team talking to each other about what we do was new, we had at one point two significant changes put into our integration branch around the same time and as both had a lot to fix (and test again and again) we managed to block our feature release pipeline for a month, making one "traditional" release, very much like the ones we did before. Single piece in the pipeline bottleneck at a time is great, and it also drives us to think about ways of collaborating to make the bottleneck smaller.   
  
**Testing in this all**  
  
In testing of this style, there's been ups and downs. When we refactored a major area without automated tests and with time of a developer who had not originally created the feature, testing was somewhat painful as functionalities went missing: the code just had not given out a hint of such an intent being embedded in the old version. I relied a lot on my memory, tested areas I knew like I've never seen them before and digged through a lot of old Jira issues mentioning piece here and there. The specification existed, but was useless on the level of detail that was relevant this time. It was also painful to test the same connected features again and again and again, as a change would easily have impacts elsewhere. It was clear that the model / design of the features wasn't clear, but got clearer.  
  
The good part with this was that some of the lessons learned ended up in automated unit tests. But still not enough. And it drove my focus again towards extending our test automation capabilities together with the team.  
  
While you *can* do continuous delivery without test automation, you might not enjoy it was a lesson worth experiencing for me.  
  
**Back to usual**  
  
In the last two weeks, we've been doing releases 2-3 times a week. It's nice and routine again. The developing and testing isn't routine, but making the release is - just as it should be. Releasing more often has also revealed some issues in production that we can honestly say that we would not have thought of to test manually / automate. Fixing them has been quick and routine, and the general build quality in releases has not lead anyone to question the idea of releasing more often. I hope we stay that way.  
  
Single-piece flow will still take us a lot of effort, but some nice agreements on how we organize towards that have already been made. I look forward to starting our pair programming trials in autumn, and working out ways to move from working solo on a task to working as team on a value item. The potential is there, while road will most likely be long and winding.
