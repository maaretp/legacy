---
title: "We love our little boxes"
date: 2016-11-30
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2016/11/we-love-our-little-boxes.html
---

# We love our little boxes

*Published 2016-11-30*  
*Source: <https://visible-quality.blogspot.com/2016/11/we-love-our-little-boxes.html>*

---

There are days when I feel I shouldn't tweet, because my \*intent\* is just to make a note of something and someone else takes it as "Interesting, I want to understand this" - and a long discussion emerges. Twitter really isn't a good place for having discussions and personally I at least seem to be confusing people more than clarifying over that medium.  
  
So this is a place for a blog post. Here's what I said:   
> Puzzled on how so many people (programmers) don't see that keeping track of minor changes is more work than making the minor change now.
>
> — Maaret Pyhäjärvi (@maaretp) [November 29, 2016](https://twitter.com/maaretp/status/803519989504425984)

Let's first talk about the principle. For years, I've been working as a tester and I view my job to include working through information and uncertainty. I'm somehow involved in an activity that makes a discovery of something missing or off, and then we'll do something about it when we know of it. Making lists of things we are missing is core to what I've been doing.  
  
However, reading through lists is a huge time-waster. There's a lean principle of avoiding inventory, and lists of things we should/could do are definitely inventory. Creating and maintaining the lists is a lot of work. And a lot of times with focus on a shorter list in a group that does development is better. Let's deliver this value first and look at what we know the world looks like after that, right? So I've chosen to try to work on value we're delivering now.  
    
My usual example of minor changes and tracking is my inability to unsee or dismiss typos in applications. I can go by them, but they leave me backtracking and drain my energy. But there are a lot of these things where, if I look from just \*my\* perspective as a developer, I could do the "minor" task also 5 minutes before the release. But the trouble is, there may be others who will backtrack all the way until the change is done.     
  
I see two patterns of how these discussions  with minor changes go (that are really honestly minor).  
  
**Case 1: Yes, this.**  
  
There's tool with a local testing script for making sure our schema follows the rules. I change the schema, and I get told to run the local script. Except that the script won't run. Going through the code, I learn there's a parameter I need to use, no clue what it would be. And when I ask about it, I learn that in addition to the missing parameter, I also miss some libraries.  
  
Instead of passing this information to me (and the 50 others who will run into this), the fellow I go to programs relevant error messages to the tooling, so that anyone coming after me gets the info from the trying to run the tool. And all of this happens while I sit with him, with changes being in the version control by the time I walk away.   
  
A day later, I see someone else struggling with the tool. They appreciated the error message right there and then. No backlog. Small thing, do it now. Same amount of time would have gone into just making the backlog item.   
  
**Case 2: No, not this.**  
  
  
  
  
  
There's the schema and it's shared with 10 teams. It's actually only becoming a contract between the teams, so it's work under progress. Reviewing it in a group with representatives, we agree on things that need doing. Like splitting according to our rules. Like removing values that are not in use ("it says DEFisEnabled" and there is no DEF at all yet, maybe in 6
months). Like making sure the names don't confuse us ("it says ABCisEnabled" and "true"
means it's disabled).    
  
So we agree they need to be changed and they keep not changing. Because no one volunteers to change them. No one volunteers because anyone could volunteer (including me). And only one of us (me) will be directly suffering the consequences on a continuous basis with the mental load of remembering what works, what doesn't and what still needs doing.  While we're avoiding doing things that are part of
that value we should be taking forward together, the side effects hit
other people than the ones avoiding the work.   
  
**So...**  
  
We
all have our ideas of what else we could be doing, and a lot of times
that does not come from the perspective of value, but choices of the
type of work I personally would like to do. If I'm a C++ developer and
we need a Python tool, that is surely a task for someone else? If I'm a
senior developer and the change can be done by a junior, that is surely a
task for someone else? If I can find someone, anyone, to do it, it
isn't my task to do. Because when it isn't mine, I can do more of things
I personally would choose to do. Like complex algorithms. Or only
testing. Or studying more of something I'm into because I don't have to do \*that\*. You name it.    
  
I could frame my original question to be: why so many people volunteer to only work on things they see as "their job", without caring about the overall flow in the system. And all this is a very human thing to do. We like our boxes. We like staying in our boxes. And we love the idea of someone else doing the stuff that doesn't belong into the boxes I like doing.
