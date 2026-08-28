---
title: "Test Documentation and Mindmaps"
date: 2014-05-10
updated: 2017-07-23
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2014/05/test-documentation-and-mindmaps.html
---

# Test Documentation and Mindmaps

*Published 2014-05-10, updated 2017-07-23 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2014/05/test-documentation-and-mindmaps.html>*

---

I have a thing with documentation - I like it. I like to read books that deliver me new concepts, teach me basics of how to do certain things and make me feel inspired. I read articles, and have a soft spot especially for experience reports that don't tell how things should be done elsewhere but outline how (and perhaps why) they were done in one particular place. I like the fact that people put their ideas on paper - with pictures and text - to open a discussion in software projects. And I really enjoy working to identify the core of information that needs to be written down.  
  
I'm turned into a fun of avoiding *test documentation.* In my main project, I write the end user online help to remember things I might have put in test documentation because it makes the document shared. And it appears people actually do read it. If I have details to write down, I'd prefer to have them written down as comments and implementation into automated tests. And for difficult information on "how was this supposed to work", I regularly volunteer to add stuff on the specifications if the information isn't end-user oriented.  
  
I create test documentation too. I create mindmaps at a point when I know the least. Mindmaps are a cheap form of documenting, they allow me to change my mind as I learn, and they support the learning that happens. When I think I've learned, I transform my mindmaps typically to two documents: a checklist that supports going through the test ideas as the software lives on that usually is in a spreadsheet format. And a short summary document with pictures and text of central concepts I need to quickly remember when I've forgotten all about this area working on another one. And I write reports on issues I notice, and categorize them on their relevance.   
  
As testing is learning, I've noticed over the years that I need to throw away my early documentation structures that I create when I start to test. In the early documents, I put in the stuff that I'm told / read from other sources that exist. Stuff that usually isn't very insightful or complex - the complexity starts to build on top of those. The insights start to happen at times I write bug reports. I learn that things were not as I expected and I log a bug. The insights, if they get collected, get muddled with all the mundane information. And as I come accustomed on my structure of where I write what, I no longer refactor the information for other audiences. The document I started creating works well for this feature / change right now, but in my experience it doesn't serve the needs of those who come later.  
  
Quite a long time ago, I learned to think of test documentation as an output of testing, not input into testing. Test documentation that I'd like to see created serves me when I need to get up to speed with an area other professional tester has tested before me. It delivers some, not all, of the learnings in a condenced format allowing me to get up to speed faster. I can't accept that every tester would start from scratch, there must be ways to accelerate and take the fast lane. Similar documentation I need when I work on an area I haven't had time for in a while - I forget and need a quick reminder when coming back. I believe it's professional to leave things in a better shape than what they were when you entered and care for the one that comes after you, even if no one explicitly tells you so.  
  
This week, I was working on a feature that I realized is similar to something our teams' other tester has worked on. So I needed the summary of the feature and core lessons from that feature already being tested. I digged in for the documentation to find three mindmaps that don't make sense. Surely they list features, but why three? Why they are split this way? Why isn't there just one that I could work with, that would have the up-to-date view. And when I looked at the details of those, there was nothing insightful written down - insightful to me. I also looked into specifications, to notice those do exist, but were out of date. Even if I update specs regularly, I have not emphasized that it could be done by others too. And they were long and boring, with anything insightful that I as a tester could use somewhere between the lines. I know how to read to see things that are not said, but I would love the two page summary instead of the 44 pages.   
  
With this behind me, I tweeted:   
> I'm starting to seriously dislike mindmaps as test documentation. It gives me a feel of 'unable to write to audience' when all is mindmaps.  
> — Maaret Pyhäjärvi (@maaretp) [May 10, 2014](https://twitter.com/maaretp/statuses/465027187075448832)

I'm sure I'm attacking mindmaps just because I'm disappointed in the quality of the ones I looked into in comparison to my expectation at that time. It's hard, if not impossible, to guess the future needs. But in this particular case, looking at the mindmaps again and again, I'm sure the trouble is the mindmaps describe structures from the time we knew the least (before testing) not the time we know the most (when we've tested). I would expect us to have the discipline to spend a moment in the end to make sure that what we leave is - critically looking - the best we can with the latest information and a reasonable amount of effort to balance value / cost.  
  
So I looked around more to realize all documentation, unless I specifically have commanded an other format, is a mindmap. Even the low tech dashboard I've adviced to create is a mindmap. Which gives me the impression - unconfirmed - that there may be a liking of a tool instead of actively thinking of the format in place. Mindmaps are a tool, that brings in a format for the documentation you create with it. I'm not sure if they would work well to capture stories. They seem to work well for listing features and subfeatures, and their relations. And when they have lots of detail, using them to keep track of what you covered just isn't what you could do with a checklist format.  
  
I appreciated what James Bach pointed out:   
> [@vipulkocher](https://twitter.com/vipulkocher) [@maaretp](https://twitter.com/maaretp) The hidden point of the mindmap is often to de-hype bloated traditional docs.  
> — James Marcus Bach (@jamesmarcusbach) [May 10, 2014](https://twitter.com/jamesmarcusbach/statuses/465170450104864768)

I think it should not be a hidden point. In this particular case there never was the bloated traditional documentation. There never was a constraint that stopped us from creating the best imaginable documentation for future - except our imagination. The imagination was lacking in thinking of audiences and times of use, focusing just on what I need and can create right now, while testing. I think a big part of the reason why this happens is that there's an over-reliance on mindmaps. The hidden point being the main point might help with the choices.   
  
In the information I was looking for, in all honesty, I could have used a mindmap. It would have just needed to be a mindmap that structures knowledge from the time after test when you know the most. It would have had different contents. But I could also have used a picture of the process embedded into the feature. No text would suffice. And if I would start testing that area, a checklist would be nice. Mindmaps are a poor format for checklists. A checklist, for me, is something that usually has multiple times to tick it off that I want to keep  track of: builds, environments and such.I would not have used step-by-step instructions on how to test, but the ideas of why and what to test, and how to make sense of it all quickly.   
  
The fact that I can rework all the existing documentation again to learn the basics just isn't good enough. I want a better mix of things.
