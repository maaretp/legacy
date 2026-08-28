---
title: "Pains of learning mob programming"
date: 2015-08-24
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Mobbing]
source: https://visible-quality.blogspot.com/2015/08/pains-of-learning-mob-programming.html
---

# Pains of learning mob programming

*Published 2015-08-24, updated 2017-07-22 · Labels: Mobbing*  
*Source: <https://visible-quality.blogspot.com/2015/08/pains-of-learning-mob-programming.html>*

---

Treat one another with kindness, consideration and respect takes a bit of practice. Or better expressed, practicing it makes me exhausted.  

Me and my team did our first session of Mob Programming today without an external facilitator. With troublesome teams, a facilitator is great to have. But this time we were amongst ourselves.  Trying to figure out what goes on in something you haven't done before code-wise and helping the process, it's kind of a handful. Especially when not everyone agrees on the idea of mob programming in the first place, even for training purposes.

**Why are we trying Mob Programming?**

Let's take a step back. Some people in my team of 9 developers and me really have strong dislikes for group work. When I first suggested pairing/mobbing, that was treated as the biggest insult one could imagine with a particularly genderised attack on me. When I later brought in someone to refactor with us in a mob, I was told that group work is a waste of time but after the experience, occasional pairing (if not with me) could be an option. When I asked my team to mob so that I could fulfil my social needs of happiness at work and learn stuff, others agreed to give in a little but one keeps disliking anything that is "intended to destroy the introverts and bring in these stupid collaboration ideas".

I've been looking at how we do, and we're not very good. We can release to production daily, but only because the throughput times are ridiculously long and we throttle what goes through depending on the skills of an individual developer. Individual differences of quality from a developer are significant. And quality is not just "bugs" I see. It's also code that others want to touch.

Courses and training haven't really helped. People fall asleep on courses. You need to learn at job. You need to get better every day. So I work very hard to help people find time to learn, mechanisms to learn. Every day is an opportunity to be just a little better. That's how I test. That's how I want to help developers turn ideas into code.

We need to learn from each other. So pairing and mobbing are the things to do. We’ve identified several team challenges we feel
this will help us with.

  

- **Asking for help** We often get stuck in development and ask Google, where we should ask one another.  As an end result, we have more cleanup work later. We could avoid cleanup by having more brains on the work.
- **Reuse and rework**  
  We could learn to use our technical assets (reuse existing code) in addition to working actively against adding technical debt. We have technical assets we don't use, but recreate as information of what there is isn't shared.
- **Continuous learning**We could learn from one another and have the learning show up right away in what we’re delivering. In particular, we could even out our individual skill differences in technical excellence we’ve already been working on. No course teaches how to work with our code and application specifically, we need to share examples by doing things together.
- **Teamwork**  
  We could get away from feeling alone and isolated. There’s very few other practical ways than pairing or mobbing to expose the practical level knowledge from developer to developer. It’s in the doing we learn.
- **Focus**  
  We could be more focused on an item we’re delivering, making the throughput times shorter without having to consider merge conflicts or additional work in splitting up into something manageable for several people. We could reduce procrastination and waiting, making think time explicit instead of hiding it into tasks. We still control our own use of time, just as always.
- **Skills outside the "developer" box**When working with requirements, we still often take what was asked and deliver that without questioning it enough. User interfaces in particular can be very dodgy. Exploratory testing that actually find bugs happens only when I do it or I sit quietly next to a developer testing and pretending I'm a totem or a mascot holding space for testing thoughts to happen. There's a lot of siloing to tear down on what a developer can / should do.

**Mob Programming to train use of Selenium Webdriver**

I believe very strongly that mob programming would be a constructive way to tackle some of our team challenges. So I've been on the lookout for chances to try it out. Being where we are now just isn't good enough, because we have potential to so much more. If nothing else, less time at office doing the same work much faster.

Last week our summer intern needed something to do, and the developers came up with having him work on adding some Selenium Webdriver tests. I was aware we had one developer who had been adding them and being kind of keen on using them to drive his development, but the skills and habits related to doing tests were isolated to him. The summer intern changed the power dynamic and I went to read through what we had now.  
  
I learned we had 3284 lines of code in the Selenium test project. I reminded myself that we started working on this stuff with me creating opportunities to try it out and create things already two years ago. And whatever was created, had emerged in the last six months. The one developer who had taken the given chance to focus on learning to do stuff with Selenium had used what was given and created quite a nice page-object - utils - tests structure. It was time to get that to the rest of the team. So we agreed to mob with two learning goals.  

1. Everyone would learn to run tests / subset of tests / analyse the results when tests fail to make them a team asset
2. Everyone would learn to create new tests

I find it hard to see that any other mechanism would have lead to the point where we were 2 hours 15 minutes later, where every one of us had not only seen how to write a test, but also written (stumbling  on their way but improving every round of rotation) a part of the scenario we were testing. And we had added test for a relevant scenario that will now run every night. A test I will not focus on while exploring, since I know it exists without deciphering, backtracking and monitoring what is going on with checkins.

The experience was good but also painful. We were really bad at sticking to the roles of Strong-Style pairing. And every time we dropped the roles, the next one up as the driver did not know quite where we were, as you just cannot keep up with reading code while someone silently writes it. One of us was continuously pointing out that this was a waste of seven people's time, while everyone else felt they were learning a lot, in a hands-on way.

During the session we got from one capable navigator in Selenium to three people navigating quite happily. We decided to work on navigation skills sharing next time, and have a designated navigator so that everyone will take turns in trying that out too. And we decided to do a better job in creating a common understanding of the scenario we're automating - this time I knew the test and that there would be problems on  the way, but the problems took everyone else by surprise. A Jira-ticket of a problem is nothing compared to experiencing the problem yourself.

I was really proud of pointing out how nicely our summer intern had reviewed code while working in the mob, fixing things we would have seen when running the test - which was slower feedback that a smart person pointing things out.

But I was also exhausted on the continuous negativity towards trying out something new. I got to hear that "I'm not paid to do this, this socialising is too much work" and "You just want us to play and not do real work, all this stuff is like being in kindergarten" and "I could just be a manager and sit around not doing anything, just suggest these idiotic things that waste time". I was keeping myself as calm as I can, working to dismiss the stuff, trying to believe that more of this will change the dynamics in the team.  
  
I noticed three things I can put my finger on that we caught in the team within the session:  

- Keyboard shortcuts. People learned to use the IDE a lot faster over just short practice. It's just more efficient telling people shortcuts and then telling on a higher level with things happening faster when you don't search around with mouse. And surprising shortcuts were missing from people who do this stuff daily.
- Resharper. We've had it for ages. And many in the team did not use it. Renaming manually to three places becames visible and something we can help with changing when it is visible. And it's error prone.
- Consume-first programming. It was interesting to notice that only some were comfortable with the idea of faking what you wanted to code to have in the test, before implementing it. Most people were first navigating with the idea that you build each piece and put them together in the end. Example was very powerful in that, and I was particularly pleased on how smoothly it came in developer collaboration.

I try to focus on the positive. Others will want to mob again in two weeks on sharing knowledge of TypeScript, and then week later, more on Selenium as the team is back in full composition.

I show very uncharacteristic patience in changing the team. A little every day. And we'll get there, eventually.
