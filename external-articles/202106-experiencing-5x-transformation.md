---
title: "Experiencing 5x Transformation"
publication: "Agile Thoughts Magazine"
date: 2021-06
url: https://www.agile-thoughts.com/magazine/jun-2021/
source_retrieved: https://www.agile-thoughts.com/magazine/jun-2021/
kind: magazine article
language: en
---

# Experiencing 5x Transformation

*Agile Thoughts Magazine — 2021-06*

Source: <https://www.agile-thoughts.com/magazine/jun-2021/>

> Retrieval note: text extracted from the author's PDF of the article (the original publication is offline or paywalled); layout is approximate.

---

Experiencing 5x Transformation from Infrequent to Continuous Delivery

Recently, I have found myself thinking of milk a lot. Not the most
usual thing to think of, given that my work revolves around quality,
testing, developer productivity. Looking back, I have been through
five rounds of transforming teams from infrequent releases to
continuous delivery, and a lot of my distilled wisdom comes down
to milk.

The first story of milk I find myself telling, almost on repeat, is on
the fact that test results are like milk - they go sour quite soon. If
you have test results from six months ago on a product succeeding in any way in the modern
software organizations, change is a constant. Change takes us forward. It is a reaction of trying
to create something of value. And in absence of change, we have learned to understand that
the world around us changing means we are longer staying on board with what is needed. We
want to keep replenishing our test results, not only because we change our software, but
because we are not able to stop the ecosystems we reside in from changing.

It’s not just test results that are like milk though. It’s also our practices. Every single agreement
made earlier deserves a regular replenish. Instead of collecting rule after rule, we should retire
some of our rules as we come up with new ones. This creates a good platform for
experimentation.

Milk also comes around when thinking about how much of it we should stock. I remember an old
experience where we stocked two with a roommate, and wanted to use older first, only to learn
the plopping sound sour milk makes when you pour it into a coffee cup you hand to your
neighbor visiting. Having some of the same from a later batch gave us an opportunity to try
again, and fix the problem we had just created for ourselves. Next batch can fix problems the
previous batch reveals.

Finally, I keep explaining that software isn’t like milk - it isn’t more expensive in small cartons.
Quite the opposite. Smaller units of delivery keep risk at bay, and risk is expensive.

In this article, it’s not really milk that I want to talk about. I want to share my experience of
facilitating a transformation into smaller batches of delivery deliberately to turn my specialty
work - testing - from stress in the end to continuous flow of collaboration. I find that it’s always
been a journey and while I can imagine a destination of continuous deployment where software
flows many times a day into production, for that level I am still on the journey.

The 5x Transformation

With 25 years in the industry, I found two guiding principles useful in my choices of where I
work:
     -​   Great testing depends on context but how could I recognize that context in action -
          experiencing clearly different contexts.
     -​   Making suggestions as a consultant isn’t my level of involvement - I want to suffer / enjoy
          through the changes as someone in the software development team that is changing.

I come to work on testing and I find myself changing how we deliver with quality, continuously. In
hindsight, it is easy to see that it ended up being the same kind of change I guided five teams
and myself through, and after multiple repeats, I also see how my approach has grown. The five
teams include three different product organizations, three significantly different delivery
environments, and two different approaches to sufficient automation.

 Org      Delivery environment   Approach to Automation     Deployment           Lead Time
                                                            Frequency

 A        Windows Application    Build only                 2 weeks → 3 months   N/A

 B        Web Application        Build only                 1 day → 2 weeks      1 week → 1 hour

 A        Windows Application    Build + Test, extensive    2 weeks → 1 month    3 weeks → 4 hrs

 C        Web Application        Build + Test, foundation   1 week → 1 month     1 hour

 C        Embedded Application   Build + Test, foundation   1 month              32 days → 3 days → ?

 C        Web Application        Build + Test, foundation   3 months             27 days → 17 min

Table 1. The Five Experiences Summarized

Living through this many times, I have come to see how that has changed my perspectives:

Frequent Releases Make Sense
Smaller batches of delivery help us get to a place where we can flow through change in a way
that changes the day-to-day conversations from planning too much to planning just right with a
principle of always moving to better. People work better with smaller changes.

Automate a build pipeline you can rely on
The work starts from making sure that whatever changes in code will automatically become
available in packages in environments where people can see them in system context. Expect
more than build at a press of a button - expect build to start with every change.

Test automation is useful but not a necessary condition
The results of your testing will go sour with time anyway, and while test automation on multiple
levels that indicates unwanted changes and calls people in to explore is useful, it is better
regardless of automation level to work with smaller batches people can grasp.

Delivering to large numbers of endpoints/users continuously is a feature of the product
While updating your web application on your own servers is where continuous delivery has its
homeground, it is just as possible to make it work for a globally distributed set of personal
computers or IoT devices. It has dependency on a reliable update feature, and the more
continuous you seek, the more your feature design needs to include incremental updating to
manage network use. Just your customers' need for security patching often warrants these
features.

Design to hide half-done work
For features that are incomplete, design how they are deployed continuously but released when
ready. Some applications I’ve worked with achieved this by including the UI last, having the
feature off by default without user ability to turn it on, and actively designing for managing the
risk in small chunks. Others used feature flags, making it a challenge to remember to clear them
up and not leave around as combinations to support.

Work cognitive dissonance to the benefit of the change
Changing behaviors we live through changes our beliefs. Cognitive dissonance refers to a
situation where our attitudes, beliefs and behaviors are in conflict, and the feeling of mental
discomfort changes attitudes and beliefs as you work through the behaviors. Involving people in
doing continuous delivery changes them.

Follow the tempo metrics
The Accelerate book by Nicole Forsgren et al. suggests two metrics on tempo and two on
stability. The tempo metrics are lead time and deployment frequency. The tempo metrics turned
into a concrete way of seeing if we are making progress, and with the latest experience, moving
from 32 working days through 11 working days to 3 working days in lead time provides a good
reminder that the work is done improving release after release.

Leaving a team to continue is hard
With experience of moving on and leaving teams where this transformation has been our
common journey, I find that not all of them stick to the same frequency we collectively could do.
Moving fast means usually thinking fast for testing in a system context, and while test
automation helps, it is just one part of the equation. I like to think that just like with the product
always moving to better the teams through this experience are better than without the
experience.

Release Frequency is a Game Changer

I started with milk, and I’m ending with water. I’ve come to understand that while testing is still
testing and programming is still programming, everything changes when we release more
frequently. A bathtub is a container of water. A pool is a container of water. Yet with these
containers of water, we can easily imagine that the purposes a pool and bathtub serve are very
different. We’d find the ideas of a bath guard, bath party and bath slide at least a little funny,
while they all are common purposes a pool enables.
I don’t yet know where my journey with continuous delivery will take me, but just being on that
journey has positive impacts, enabling us new purposes.
