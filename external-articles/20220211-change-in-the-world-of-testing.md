---
title: "Change in the World of Testing - New Misconceptions from Old Folklore"
publication: "BrowserStack blog"
date: 2022-02-11
url: https://www.browserstack.com/blog/change-in-the-world-of-testing/
source_retrieved: https://www.browserstack.com/blog/change-in-the-world-of-testing/
kind: article
language: en
---

# Change in the World of Testing - New Misconceptions from Old Folklore

*BrowserStack blog — 2022-02-11*

Source: <https://www.browserstack.com/blog/change-in-the-world-of-testing/>

> Retrieval note: page text as published.

---
In the field of testing, there are peculiar stories we perpetuate. These stories - folklore - become a way to share older generations’ knowledge with incoming generations. They stem from insightful experiences, amplified by the realization that these experiences are incredibly common, and become myths we pass on to newcomers.

In this article, we dig into a few of these modern myths - particularly those related to testing, the role of testers, how testing is done, and who does it. We also bust these myths, shining a light on the actual situation today. We chose to retell these stories specifically because they felt very real and possible back in the day but would make anyone raise an eyebrow today! Tester is an Interim Role Before Being a Developer

Sadly, the idea that a tester role is less qualified compared to a developer is very prevalent across organizations. Especially when it comes to automation topics, a tester’s ability to do proper development work is often dismissed. This can heavily impact a tester’s self-awareness and ultimately lead to the mindset that the role should only be a temporary milestone on their career path. Growing into a development role to earn the respect of peers might be the aim, but this dismissive mindset devalues the work a tester is currently hired for.

What is often forgotten here is that developers and testers, while sharing the ultimate goal of a well-working piece of software, have very different purposes in the software development lifecycle.

There are all kinds of important work that need to be done; and for this work to be done well, you need good, skilled people. There are seasoned developers who have transitioned into testing roles. And there are people who started as testers, are still testers, and love testing.

Instead of thinking testers look up to developers, can’t we all just look up to one another? There will always be things we know better than others, but we must also recognize that other team members come with a treasure trove of diverse knowledge and experience. We can learn from each other across all roles and levels of experience, provided we remain curious.

“Works on My Machine” - Something Developers Say

We have all heard this one - developers saying “It works on my machine”, and testers responding with “We don’t ship your machine”. But who says this, for real? Although the story always has a developer as the active party, our experience tells us otherwise. You are more likely to hear “It works on my machine” from a tester.

At the same time, our work has outgrown our machine. We may still run code locally, but containerization and virtualization allow us to access a range of environments and test if the code works as intended. Even without containers, developer reality has shifted: less software is now designed to work on one machine and most people know it.

So the next time you hear the words “It works on my machine”, pay attention. Though it might be coming from a tester, the fact that some bugs only manifest under particular conditions is a shared problem for all roles. If 'my machine' represents a user device or environment that is potentially at risk of encountering a bug, product owners would surely want concerned teams to collaborate and fix the issue. This, in turn, will help in eradicating the 'works on my machine' folklore.

Developers Don’t Do Deep Testing

A recurring theme among testers is the distinction from 'developers'. A frequently heard accusation is that they do not practice deep testing and that testers maintain this bastion.

But what is deep testing, you might ask? Is it some special investigation to dig out results that testers might miss? It is used, somewhat judgementally, in the context of problems that slip into production. Our first instinct might be to think ‘how did someone miss this? We ourselves would have detected this bug rather easily.’

Contrary to popular belief, we have experienced that developers and testers can both practice deep testing proficiently, but at different levels. While developers test their code in a modular way and at the implementation level, testers do their work with the big picture in mind. This includes aspects such as the usability of the system, the validity and expressiveness of the data, the meaningfulness of certain features, and compliance with specifications.

Many developers can perform deep testing around particularly hard-to-reproduce bugs by deliberately controlling variables identified in collaboration with testers. But assigning deep testing strictly to testers undermines developers’ abilities. Sharing the work with the team across roles enables collaboration, effectiveness, and depth none of us could get to alone.

Both roles are definitely needed in the software development lifecycle and - if given the appropriate time, education and resources - have a specific interest in delivering high-grade products.

By downplaying developers' testing abilities, testers are at risk of actively conforming to prejudice, which they actually want to eradicate - that only testers are responsible for quality.

Testers are Information Providers. They Don’t Make Decisions or Speculate on Causes

In one form or another, we tell stories about where testing stops. The focus on providing information suggests that taking action based on the information is someone else’s responsibility. This becomes especially evident in release decision-making and bug reporting.

We usually leave release decision-making to business representatives thinking they might have additional information that testers do not. Besides, it is perhaps their job to decide on releases. However, in our experience, we have seen that business representatives often share information and generate guardrails to empower teams to own release decision-making - and testing is an active perspective in that decision.

But to provide empowering information to teams, business stakeholders must have enough information to begin with. And this is where testers can really shine because they are the ones doing deployments or rollbacks if production uncovers surprises - testers have access to important information.

Then there are stories around factually reporting symptoms of problems when speculating the cause. These stories are meant as warnings and imply that developers do not welcome advice and speculation on why a problem exists. So - the story goes on to say - instead of helping, you are only going to irritate and annoy developers.

On the contrary, many developers appreciate and expect a more analytical angle from testers. They prefer testers taking an active interest in shared debugging sessions compared to just reporting the symptoms. Curiosity in learning about what is going on beyond the “I see, this does not work” is expected.

Through their cross-team connections, holistic view of the application under test, and their organization, testers can often retrieve more relevant information than other roles. They do this by asking specific questions, enriching the answers with known information, placing it in the product context, and synthesizing new valuable clues from it.

Fully Tested before Production

Systems today are increasingly systems of systems. Value chains from users are put together with pieces from different development teams - some internal, some external. Architecture forces us to change our assumptions. We can no longer say that developers know what they have implemented at all times. Much of implementation is configuring and testing someone else's subsystem to make sure it meets the purpose we are trying to achieve in our solution. We can’t know things the old way, especially with the new world of microservices and AI algorithms we orchestrate.

End-to-end testing is no longer about testing truly end to end, but decomposing the system. Seeing something fail without understanding ‘why’ is quite pointless; we need increased architectural deliberation. And we need to think in terms of trust chains, not testing things that are already tested to make space to test for things that are not yet tested. Updateability - changing parts of the system without testing the entire thing - is non-negotiable.

There are also stories about testing while in production. Experiments to explore missing functionalities can now be done with production versions of systems because we now know that there will, most definitely, be a future version. This is something we could not take for granted before.

Testers Don’t Need to Code

Conversations online are often around people looking for work in the IT industry that does not require programming. The most common responses suggest taking up roles like product owner, scrum master, designer, or tester. So a narrative where testers do not write code - and are valuable - still exists. While this is largely true, it fails to capture the versatility of testing work, and the discussion of how unnecessary it is to frame our work as 'not programming'.

Testing is a core part of development. The age-old adage of “I can code anything if it does not need to work” is still true. What we call programming is much more than coding. But being able to read what code has been changed is a superpower a tester already has.

So here’s a story worth making folklore for the future. We were creating functionality that would list all files of a certain age and delete them. The code to log the list of files to be deleted was implemented correctly. However, reading the code revealed that the few lines under review did not include the actual delete command. Adding the missing line of code was not difficult, but it was also not hard to forget in the first place.

Code reviews are an integral part of programming and can benefit testers - even those who spend very limited time on code. Programming has several layers, and every day we have the opportunity to add a trick or two up our proverbial sleeves.

With this, we wrap up this rather controversial topic and encourage you to think about the stories you tell.

How can the world change if the stories we tell future generations stay the same?

About the Authors Benjamin Bischoff is a Test Automation Engineer within trivago’s core QA team. His focus lies on the development and maintenance of the company’s in-house end-to-end test framework and related build pipelines as well as back-end and API automation. He is an occasional conference speaker and trainer and writes about testing and automation topics on his website https://www.softwaretester.blog/

Maaret Pyhäjärvi works as a principal test engineer at Vaisala. She’s been in various testing roles over the 25 years of her career and has a particular interest in making an impact in software products where quality problems halt development and stop revenue flows. She thinks of herself as a feedback fairy and social learner and is a prolific author of books, blogs, and articles, and a frequent speaker having delivered keynotes and talks in 27 countries. She’s recognized as an influencer in IT in Finland and holds two prestigious global testing awards: MIATPP and EuroSTAR Testing Excellence Award. She blogs at https://visible-quality.blogspot.fi/

Image Credits Diagrams by Maaret Pyhäjärvi Images by Mohamed Hassan

- BrowserStack Home
- Blog
- Software Testing
- Change in the World of Testing - New Misconceptions from Old Folklore
