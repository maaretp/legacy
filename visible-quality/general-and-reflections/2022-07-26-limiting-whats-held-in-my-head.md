---
title: "Limiting what's held in my head"
date: 2022-07-26
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2022/07/limiting-whats-held-in-my-head.html
---

# Limiting what's held in my head

*Published 2022-07-26*  
*Source: <https://visible-quality.blogspot.com/2022/07/limiting-whats-held-in-my-head.html>*

---

I'm struggling with the work I have now. For a long time, I could not quite make sense of why. I knew what I was observing:

- a tester before me assigned into this team could not find their corner of being useful in a year
- a tester after me stayed less than a month
- a tester before us all felt overwhelmed and changed to something else where work is clearer

This project repels testers left and right. Yet it has some of the loveliest developers I have met. It has a collaborative and caring product owner. But somehow it repels testers. And I have never before experienced projects that repel testers while having developers who love testing like these folks do.

In the six months I have spent with this team, I have managed to figure out some of the testing I want to do and I've:

- clarified each new feature for what is in scope and what is not in scope, and tested to discover when those boundaries are fuzzy
- learned how to control inputs, the transformations happening on the way, and how to watch the outputs
- shortened release cycles from years to months
- introduced some test automation that helps me track when things change
- introduced test automation other people write that exercise things that would otherwise be hard to cover, allowing for the devs to find bugs while writing tests
- had lovely conversations with the team resulting in better ways of working

I have plenty of frustrations:

- I can barely run our dev environment because I hate how complex we've made it and can almost always opt to avoiding working with tests like the rest of the team - it took me 5 months of avoiding and having all my code on the side, now putting some of it together and losing debug
- We use linux because devs like it, but customers expect windows because they like it. Discrepancies like this can bite us later and they already do if you happen to join the team with a windows workstation (like all testers other than myself who changed to Mac recently)
- Our pipelines fail a lot, and we're spending way too much time on individual branches that live longer than I would like
- Our organizations loves Jira, and our team does not. That means that we don't properly fake using it. The truth is in the commits and conversations (great) but I feel continuously guilty for not living up to some expectation that then makes it harder for testers who think they can rely on Jira for info.
- We have so much documentation that I can't get through it in a lifetime.

So I have done my share of testing, I live with frustrations, and navigate day to day by juggling too many responsibilities anyway. What am I really struggling with? The adaptations.

I have come to limit heavily what of the things the team discusses I hold in my head. I don't need all of it to do what I have set out to do. I model the users' and other stakeholders space and I care about tech for the interfaces it gives me for visibility. I model what ready looks like and how we can make it smaller. I don't accept all the tools and tech, because there's more than I can consume going on. I focus on what others may not look at on the system.

I start my days with checking if there is anything new in master, and design my days around change for the users. I choose to mention many things over doing them myself. I limit what I hold in my head to have energy for seeing what others may have missed.

There is no simple "here's your assignment, test it - write test automation code for it" for me, there is always someone (currently a junior I'm training up on programming/testing). Most test automation in this team requires diving in deep into the depths of the implementation. The work is intertwined, messy and invites often to deep end without focus time unless you create it for yourself.

So I struggle: finding a tester to do this work seems increasingly difficult. Training newbies feels a more likely direction. And it makes me think that some of this is the future we see: traditional testers and test automation folks won't find their corner of contribution.

This world is different and it calls for different focus - intentional limiting of what we hold in our head to collaboratively work while being different.
