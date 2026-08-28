---
title: "A Developer's Idea of Exploration"
date: 2018-03-29
updated: 2018-12-26
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/03/a-developers-idea-of-exploration.html
---

# A Developer's Idea of Exploration

*Published 2018-03-29, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/03/a-developers-idea-of-exploration.html>*

---

"We did a neat thing exploring today", a developer exclaims. I look, interested, wondering what is the source of excitement this time. It's not the first time they've been excited about doing things clearly very close to my heart. But a lot of times we find our ideas of exploring take very different, yet fascinating turns.  
  
"We did this combinations test", they explain. "We took bunch of values when we did not feel like thinking too much, and passed them all in, and created combinations", they continue. "We learned about behaviors we did not think of", they finish. And we agree that is wonderful. Learning while testing, appreciating the new information, absolutely something we share.  
  
There's been little remarks like this coming my way a lot recently, and while I can share the excitement of learning something we did not know, I also find that  the ways of going to "as close to exploratory testing as I usually do" as a developer isn't quite where my exploration is.  
  
There was a session about property based testing, and generating test cases to run through same partial oracles. Just doing it wider does reveal things of unexpected nature, especially when you have a way of identifying some relevant aspect of correctness with a property.  
  
There was an exercise of creating combinations for a 3 variable method, finding out the application does not work as specified on its boundaries. Just having more cases easily available and visually verifiable revealed information of unexpected nature.  
  
All the three examples I've had recently, are ways of programmatically doing more. While they uncover relevant information, there's still more to exploratory testing.  
  
This makes me think back to exploration of someone else's web app we did in a mob yesterday evening. Just some things I remember us learning:  

- For a system aiming to enhance datasets to acceptable, it makes no sense that when there is a condition preventing the dataset from ever being acceptable, we would first need to fill in some info when the condition of rejecting exists without any additional info (a problem in the order of tasks in the process)
- For uploading files, we'd like to be able to use explorer over just drag-and-drop. It matters how most others do things.
- When a user interface view would include many things to show in tables, having relevant tooltips for some but forgetting placeholders for others less obvious creates confusion.
- When you must choose of of two but not both, automatically emptying the other field isn't exactly the best way to present that.
- When rejecting an input, logging it might be useful.
- When failing so that there's a big visible error in the log, it would be very nice if that error was made visible also for the user.
- When having a recurring element of guiding users, filling it in three different ways makes little sense.
- When you can get to a functionality with one click as there is just one option, hiding it in a menu requiring extra click won't be helpful.

None of these would have been found by the "let me just play with my unit tests" approach to exploring. Then again, none of what we did would have found things that approach could find.  
  
It's not this or that, but this and that. And it's lovely when developers show ideas of applying the same ideas with the tools at their hands. I hope to get to experience a lot more of it going forward.
