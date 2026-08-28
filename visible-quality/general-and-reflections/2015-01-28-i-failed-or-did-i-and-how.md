---
title: "I failed - or did I, and how?"
date: 2015-01-28
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2015/01/i-failed-or-did-i-and-how.html
---

# I failed - or did I, and how?

*Published 2015-01-28*  
*Source: <https://visible-quality.blogspot.com/2015/01/i-failed-or-did-i-and-how.html>*

---

I'm feeling something every tester probably recognizes: guilt about problems in production. No one is saying that I should have found that problem. Everyone, including me, knows I did not put the problem there in the first place. Out of the choices we made on using our time as a team, we failed to understand where the impact could be, and none of the tests we did hit that spot.  
  
It was not just one spot though. It was three.  
  
The reason I feel particularly guilty today, is that I failed to do something I almost always do: ask the developer for clarification on what exactly did he change on a task of "last refactoring from LINQ to EF" - which parts did he refactor this time. Or to be more precise, I asked and I opted to be happy with a shallow understanding, not getting a more precise list of functionality he could see impacted. And his precise list would have included functionality that did not work. But I chose to use my time differently this time. After all, we have a working agreement in the team that a developer (who knew exactly what pieces he changed even if I did not this time) does own testing, to see if things work. With a ratio of 9:1 of developers and testers, testing is everyone's job. So if we failed, we all failed.  
  
While my lips voice out the "*we* missed that" and "if we knew
where it was broken, wouldn't we have fixed it" and "I focused here to
find these other problems by choice, none of us came up with that spot
to check", my head still says I'm better than that. And often I am, just
by staying with the software longer, with more variations, pushing my
luck in systematically going through things from different perspectives.  
  
The feeling of unjustified guilt drives me to look at the symptom of "own testing" a little wider in my team. Not only did we see problems in production, but I've had one of the most unproductive days in a long time. I tested one feature (fifth cycle) to only find out it doesn't work. I tested another feature, to find out that the styles have completely been broken rendering the area unusable. And I asked for a demo (and then tested) a third new feature that did not work at all.  
  
From three in production to three in test environment is evidence that the infamous "own testing" isn't happening, even if we just had yet another chat about it on Monday with the team. All these were problems you could not miss if you just opened the software for the feature that was being changed - there's much more intelligent problems around than just that.   
  
I'm trying to change the dynamics, and here's my list of things I do on that:  

- Move first experience of bad quality from me (externalizing the experience) to the developer by asking for a demo and showing it fails when they touch it
- Introduce simple variation in the demo, by asking to show specific things outside the usual demo flow, again with the intention of moving the experience of bad quality to the developer
- Add Selenium checks on features, in hopes of feedback that does not require the developer to go to the integration test environment personally
- Testing shallowly quickly after introducing a change.

Removing the tester (me) seems like an option, to remove the feeling of someone to watch over you. But we've tried that before I joined, with the end result that our end users become the testers.    
  
I would love if we could learn that the most important work for us as a team is to make the product work. Developers are not too valuable to spend time on actual flow of value over insignificant half-done tasks and features, hitting an arbitrary (and self-created!) deadline. Need to find ways of building more of a culture of working software. That culture not sticking may be the failure I can feel guilty about later on. Accepting status quo and just compensating by testing brilliantly seems like an awful choice. Better than not testing, but there must be more I can do.
