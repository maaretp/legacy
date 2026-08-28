---
title: "Incremental steps to continuous releases"
date: 2017-05-26
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2017/05/incremental-steps-to-continuous-releases.html
---

# Incremental steps to continuous releases

*Published 2017-05-26*  
*Source: <https://visible-quality.blogspot.com/2017/05/incremental-steps-to-continuous-releases.html>*

---

The last eight months for me have had one theme in particular that I consistently drive forward, in small steps that sometimes feel small enough that others don't realize how things are changing.  
  
There's an overall vision in mind for me: I want to take us through the transformation to daily releases for the windows client + management backend product I'm working with.  
  
**Where I started from**  
  
As I joined 8 months ago, the team I joined that been working for several months on a major architectural type of change - no releases but a build that could be played with internally. We had "8 epics" to drive through the architectural changes, and none of those were done. There was a lot of dependencies all around and making a release someone would use wasn't a straightforward task.  
  
I started in September. The first release went out November 23rd.  
  
There's more than a decade of history on making continuous releases of the detection and cleanup functionalities within the product, but the frame of the product has been released annually or quarterly for production use, and monthly or biweekly for beta - something I was introducing here a decade ago.  
  
When I started talking of daily releases, I was told it was impossible. It took me 4 months to get rid of the "it cannot be done" comments.   
 **The pain of regularity is necessary**  
  
I had a firm belief (which I still hold) that when things are deemed hard, you just need to do more of them to learn how to make them less hard. So I struggled with my team through the discussions of "releasing takes too much time and is away from real work", with the support from our manager setting it a team goal tied to bonuses that we would turn our 4 day release to a 4 hour release.  
  
Each release would see a little more automation. Each release would see a little more streamlining. We would find things that would be difficult (not impossible) to change and postpone those from focusing first on the low hanging fruit, never giving up on the ultimate goal: a touch of a button releasing to various environments.   
  
A month ago, I could happily confirm that the 1st goal as it ended up being written down was achieved.  
> **[Team Capability] Turn 4 day release to 4 hour release**  
> We believe that ability to make our client releases with shorter duration will result in saved time in making multiple releases. We will know we have succeeded when team does not feel need to escalate release-making as a threat to features.

We also worked on another capability:  
> **[Team Capability] Min 2 people can make client releases**  
> We believe that having at least two people with skills, knowledge and accesses to make client releases will result in being able to make releases while one is sick. We will know we have succeeded when release happens without 1st key person present at office within same / similar timeframe.

**What next?**  
  
We have come to a point of bi-weekly releases, which is only taking us to the level I introduced decade ago. But building on that, the next things would be to figure out ways of not breaking the builds within the 2 week intervals, and that change takes me far away from just my own team, including changing the ways test automation supports our development.  
  
There's still work on making the four hours into four minutes of work, and I look forward to stepping through that challenge.  
  
Our very first production environment release was just done. With more environments in play, each 4 hours can easily grow into five times this, so that would be a next step to work on too.  
  
So the vision I'm working for:  
> **[Team Capability] Four-minute release throughout the environments**  
> We believe that having a push-of-a-button release will result in us focusing more on valuable features and improvement for the user and our organization. We will know we have succeeded when releases happen on a daily basis as features / changes get introduced. 

**Why would I, the tester, care for this?**   
  
I have people every now and then telling me this is not testing. But this fundamentally changes the testing I do. It enables me to test each change, isolate it and see its impacts all the way through production. It supports small, human-sized discussions on changes together in the teams and gives us an ultimate definition of done - production value over task completion.  
  
It makes developers care about the feedback I give, and enabled the feedback to be more timely. And it makes way for the necessary amount of thinking and manual work to happen in both coding and testing so that what we deliver is top-notch without exerting too much effort into it.
