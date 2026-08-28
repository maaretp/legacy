---
title: "Lessons learned on avoiding testing"
date: 2015-06-17
updated: 2016-08-02
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2015/06/lessons-learned-on-avoiding-testing.html
---

# Lessons learned on avoiding testing

*Published 2015-06-17, updated 2016-08-02*  
*Source: <https://visible-quality.blogspot.com/2015/06/lessons-learned-on-avoiding-testing.html>*

---

I'm a tester. I love testing. It's great to look at an interface from a user perspective, and find out how it could fail. Send in something, see what is the response, learn and come up with new ideas. The same intellectual stimulus is there, looking at an interface directed for a human user or a computer user. This can fail, and I'll find out when.  
  
As I was talking about test strategy with a group of great people over a testing dinner last night, I was testing what I was saying. I had this out of a body experience (very mild!) of looking at what I was explaining, and I realised that while I tried really hard to focus on ideas that guide my test design, I ended up mentioning, over and over again, ways of avoiding testing I've focused on.  
  
Don't get me wrong, I test a lot. My testing is far from shallow. But I spend some of my effort on building an environment where things don't fail when I'm not around to test. And where I can do new things, instead of repeating the same old ideas.  
  
**1. Enable technical excellence and beautiful code**  
Here's a discussion that I've seen happen in organizations. A developer mentions that something should be refactored, because it's actually not that easy to comprehend. A project manager / product owner hears her out and puts the thing on the backlog. And prioritizes it so low it will most likely never climb up from there.  
  
The "refactoring" here isn't a small "let's change it just a little and tests will protect us". It could be ripping out a self-made solution and replacing it with an external component we do not need to maintain ourselves. It could be that whatever was coded, should be significantly reorganized or even partly rewritten, as it was done when the smart developer knew a little less than today as she too learns every day.  
  
As a tester hearing that discussion, I used to look at it as something between the developer and the project manager. But having spent enough time with developers, I've grown empathy. I know how much a developer is in pain to even say out loud that his code that he thought six month ago was good isn't good. I know how much a developer suffers when the cleaning work gets postponed, indefinitely. And when a developer suffers, quality suffers. I suffer, as I run into stupid bugs a happy developer would never leave around for me. Morale is the key.  
  
So nowadays, whenever I hear this discussion starting, I take a proactive, constructive approach and start negotiating on how soon we could do the changes. I explain the long term costs. I build a business case if needed. And over time, I've built an atmosphere where my team's developers actively identify how we could improve and we drive the improvements through.  
  
In the past, I wasn't only passive, I was sometimes actively against. With year-long projects leading to a single release, the clean-up work was a risk. It would probably break everything. But with agile, we can contain the risks.    
  
**2. Build room and skills for unit testing**  
Most of the refactoring we do happens with little to none of automated tests around. Our unit testing goes in cycles, where we add them, think they are not useful in the way we implemented them, remove them and then start missing them again.  
  
We started from none. I did a lot of talking to convince the people in control of the money (time) on giving developers learning time for unit testing. I got us training. And I still get us training.  
  
Requiring something without proper room in schedules for it just won't happen. And the skills take time to build. Time and examples of successes. I'm here to not let us give up. Many of the things that cannot be done, cannot be done because we just don't yet know how to do them.   
  
**3. Call for the best possible contributions for quality**  
I hang out with my team, and while I look at myself as a helper providing quality information, I'm also very much a senior, active team member. I'm often one that mentions risks I feel I could not address by myself: security, performance, maintainability, usability. And when called for, we together agree on how we address them. Performance testing with proper tools is done by people with proper tools - licenses dictate who can build and run them.  
  
I often suggests pre-testing activities too. When something is ready to be tested, I'm often the one who suggests another developer to review the code before I get started on it. Judging from facial expressions, I've gotten somewhat good at guessing when someone is hoping to get through lowering the team bar on technical excellence. And I usually also hear this right away with an estimate on how much this will delay the time when my testing would be useful. But over the years, I've learned that things that look great in the user interface can be the biggest mess of all times when the first changes / fixes must be made. And maintainability of the code plays a big role in that, reviews are just the key to do it.  
  
I also often speak about avoiding reviews, because they are always a late feedback. Wouldn't everyone like to get help while doing it, instead of hearing they did it wrong? Calling for pair programming and even mob programming has ended up being something I do. Because better code makes it easier to test-and-fix without breaking it in surprising ways. Regression happens for a reason, and spaghetti code without structure is a major reason. Something we can avoid, though.    
  
**4. Holding the space**  
Before I test, I ask developers to give me a demo of what they've implemented. This is often very funny event. If I call it "pairing", I get negative reactions. So I call it demo. Sometimes I guide the developer to show me things I would test first, just to move the experience of things not working from me to them. But over time, I've started being more passive as the expectations of what will happen has been established. And I've started to see amazing things.  
  
A developer comes in with a feature they have tested. We sit together and I don't say a word. He shows it, and starts showing things I could ask for without me asking. And pointing out bugs. It's been amazing to see how a developer can test their own feature really well, when their mind is in the right place. And to get it in the right place, they seem to need a "totem", in this case me, holding the space and quietly reminding there's a purpose we're here for.   
  
**5. Being undependable and hard to predict**  
I've heard the argument, that as testers, people need to know what services they can expect from us and what is out of our scope. With experiments, I've learned that for me in this particular project, it works great to be someone others cannot depend on, and being predictably unpredictable.  
  
Sometimes I don't test a feature. After all, all the features have been tested by the developer before they reach me (I do participate before implementation starts too). So we can also release them to production without me looking at them. But whenever I won't look, I say it out loud. And from the reactions, sometimes I can also see that it is the right thing to do.  
  
When a developer asks me for help in testing, I never refuse. But I pass some of the common expectations, forcing people to ask when they need it.  I do this with a consideration of risks, but with agile and continuous delivery, small changes just don't carry as big a risk as some things I've played with in the past.   
  
**6. Passing work forward**  
When I test, I find ideas of things I wouldn't want to have to notice are broken. Key functionalities, key flows for the user, fragile components or use cases. I collect these, and discuss them with developers. From the discussion, developers automate things for us in testing. It could be a unit test. It could be a selenium test. It could be a database monitoring test.  
  
Our automation grows from ideas of work I pass forward.
