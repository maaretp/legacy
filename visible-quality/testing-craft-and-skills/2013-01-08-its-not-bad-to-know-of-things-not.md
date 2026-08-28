---
title: "It's not bad to know of things not testing"
date: 2013-01-08
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2013/01/its-not-bad-to-know-of-things-not.html
---

# It's not bad to know of things not testing

*Published 2013-01-08*  
*Source: <https://visible-quality.blogspot.com/2013/01/its-not-bad-to-know-of-things-not.html>*

---

I've been having a bit of a hard time with one of my development teams. Hard time comes from being a barometer-type-of-personality to notice changes in the moods, happiness and work satisfaction, and seeing the impact of that in the overall results as in the bugs I need to worry about and the overall throughput going down.  
  
In many ways, this is work as usual. Sometimes things work out better than others. But with this particular case, the trouble is that a technical team beaten to corner enough times tends to stay in the corner, and needs significant changes to play openly again. However, we have a key stakeholder in the changes who thinks no change is needed, no problems are visible and the main problem actually is that the team might not be able to cope with any changes. I consider this a conflict of belief systems, and don't expect quick resolution - while I would never give up on the change.  
  
With trying to explain this to people in twitter, I started thinking how much good as in thinking tools I have from all the years of reading a lot (business, people, agile and testing books are my thing) and sitting though various presentations picking a piece of information here and there, and putting together the stuff that makes sense to me. In the seemingly endless effort to try introduce changes, I realized that I've had a upper hand of engaging the others with three very specific things I was aware of:  

1. Code review approaches  
   When the command is "review code this month", I helped the developer to see alternative interpretations to that. Instead of hearing "wait until all mistakes have been made and correct them", I suggested he would hear "let's pair up, and see what mistakes you could learn to avoid and how I might help you with that". It's actually not the activity of reviewing they want, it's the end result you could get if you reviewed. Pair programming is a modern view to continuous review, right?
2. Documenting a task / issue in Jira  
    When the discussion is dwelling about how the requirements are so inadequately documented in our Jira tasks and how we're so excluded from all relevant decision-making as it's all been done without us while thinking through the detailed enough spec somewhere in product management with limited technical knowledge, I pointed out that we should think of the 3 C's as they relate to every task / issue we have. The Card -part is just a placeholder. It doesn't need to be specific, actually, it's better if it wasn't too specific. The Conversation -part is really relevant - after we have enough detail for the Card which is not much, the Conversation should happen. And as a result of that, we could actually put down the Confirmation -part in whatever format that helps us remember what we agreed on and will be useful. And all of a sudden, it is ok to not have them all laid out at once, since what was one is now three.
3. Specification by Example / Behavior Driven Development  
   When I asked a new developer I'm working with as the tester if we knows what I mean when I talk about SBE, I learned that his exposure to this theme is from me alone and we have not talked much yet. So, I ask him to sit with me next to my computer, and we walk though a couple of examples of Gherkin-style specifications I've been collecting on the area we're working on, basically listening in about the things we talk of and writing them down as examples. He looks at the example point out he could use that in his development. And I finally understand that while I favor SBE in talking about the practice, I would have won him over already if I talked about BDD.

  
With these changes, I shouldn't complain we don't introduce changes. I just wish I had the right words to speed up all the things we could accomplish, and did not always have to do this all through trial and error, finding the right words and the right route to handle all the various details that need working on.
