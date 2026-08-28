---
title: "Social Programming Approaches"
date: 2021-06-30
updated: 2021-07-02
theme: programming-and-technical
labels: []
source: https://visible-quality.blogspot.com/2021/06/social-programming-approaches.html
---

# Social Programming Approaches

*Published 2021-06-30, updated 2021-07-02*  
*Source: <https://visible-quality.blogspot.com/2021/06/social-programming-approaches.html>*

---

A year ago, I was preparing for a keynote coming up in autumn 2020 where I had promised to talk about *social software testing approaches*. Organizing my experiences, I wrote [an article for bbst.courses](https://bbst.courses/blog/social-software-testing-approaches/)  and started the work of replacing mob and mobbing with ensemble and ensembling.

I described four prominent social software testing approaches, two for groups and two for pairs.

- Ensemble testing
- Bug bash
- Traditional pair testing
- Strong-style pair testing

Today, I started thinking through the programming equivalents of these, and how I have come to make sense in the concepts. I have long ago accepted that everyone will use words as they please, and more words in explaining how we think around the words is usually better. Today I wanted to think through:

- Traditional and Strong-Style Pair Programming
- Ensemble programming
- Swarming
- Code retreats
- Coding dojos
- Hackathons and Codefest
- Bug Bust

**Bug Bust** is a new type of event that resembles Bug Bash on testing side, focused on cleaning up easily identifiable code bugs. I have not seen anyone run one yet, but I noticed [AWS is setting this up](https://aws.amazon.com/blogs/aws/new-aws-bugbust-its-game-over-for-bugs/) a thing to do, and time will tell if that turns out to be popular.

**Hackathon** is the closest programming equivalent to bug bashes on the testing side. Hackathons come to programming with the idea of creating a program in a limited timeframe, usually in a competitive setting. A hackathon comes with a price, seeks survival of the fittest solution, and seeks to impress. I generally hate it for its competitive nature. It says there is a *team* but how the team works is open. The competition is between teams. Similar time-boxed things without the competitiveness have been dubbed as "20% time" and codefest [[Hilkka Huotari writes about this here in Finnish]](https://www.linkedin.com/pulse/viisi-vinkkiä-onnistuneen-codefestin-järjestämiseen-etänä-huotari/), still seeking this idea of bringing together small teams on something uncertain yet relevant but a bit off the usual path of what we're working on for *limited amount of time* for *emergent teams*.

**Coding dojos** are practice-oriented group sessions. Having experienced some, I have come to think of them as *pair working* and *group watching*, with *rotation*. Truth be told, coding dojos are a predecessor to ensemble programming.  Coding dojos usually happened in combination with *code katas*, rehearsal problems we would do in this format.

**Code retreats** are also practice-oriented group sessions, that are organized around *repeating solving same problem* in code under various *constraints*. The usual problem I have experiences some tens of times now is the game of life, and there's whole books on constraints we could try and introduce. A constraint could be something like taking so small steps that tests pass at 2 minutes and gets checked in, or the solution needs to seek a simpler, smaller step. The work is done in *pairs*, pairs switched between sessions, and the learning experience framed with *regular retrospectives* to cross-pollinate ideas and experiences.

**Swarming** is a team work method that I differentiate from ensemble programming with the idea that it brings together *subgroups* rather than teams, and is *inherently temporary* in nature. The driving force for swarming is a *problem that needs attention* from multiple people. I have come to swarming from context of kanban boards and work-in-progress limits needing special attention to one of the activities we model, and swarming is a way of ensuring we can get the work moving from where it has been piling up.

**Ensemble programming**is about the *entire team* working as a team together on *one task at a time*. To work on the same task, it *usually means sharing one keyboard*. A new group ensembling looks an awful lot like a coding dojo, with *guardrail rules* to enforce a communication baseline, except we may also be working on production code related tasks, not just rehearsal problems. A seasoned group communicates on an entirely different level, and the dynamic looks different.

**Strong-style pairing** is ensemble programming as a pair. It asks for the same rule as the ensemble has where i*deas and decisions come from the person off the keyboard*.

**Traditional pairing** is the pairing where *one on the keyboard is doing programming* and the other off keyboard is *reviewing and contributing*.

We have plenty of options for social programming available to us. Social programming is worthwhile because we don't know what we don't know, but sharing the context of doing something together brings us those serendipitous learnings, in the context of doing. How much and what kind of social programming you sprinkle into your teams is up to you.
