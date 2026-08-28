---
title: "Serendipity in testing"
date: 2015-02-03
updated: 2016-08-02
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2015/02/examples-of-serendipity-in-testing.html
---

# Serendipity in testing

*Published 2015-02-03, updated 2016-08-02 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2015/02/examples-of-serendipity-in-testing.html>*

---

Two years ago in a bus somewhere in Ireland, I had a chat with Rikard Edgen that taught me something relevant I thought I should share today. I was talking about tester luck: not being able to use pretty much any software without seeing it fail in various ways, sometimes even without intention. Rikard pointed out that there is an actual word and concept for it that he discusses in his book [Little Black Book on Test Design](http://thetesteye.com/blog/2011/09/the-little-black-book-on-test-design/): ***Serendipity***. I needed to know more.  
  
Rikard pointed out that if we as testers talk about luck on something as core to testing as serendipity is, we're not helping non-testers - people who do not have the same experience of serendipity - understand and value what is special in testers. There is a reason why regularly, consistently, my team members ask out loud "How did you find that, really?".  
  
Serendipity is a "lucky accident", but in testing, it entails more than just an accident. Those of us testers experiencing serendipity tend to do something to push their luck. Luck favors the one who intentionally varies their actions, understands how things that seem the same can be different and relentlessly keeps doing things differently.  And the more I test, the more ideas of what could make things different I seem to experience.   
> "The more I practice, the luckier I get" - Arnold Palmer

Here's some of my examples of serendipity in action. Regardless of knowing the theory of error after the issue was found, I cannot claim I actively thought of things like that while testing, at least not that particular moment I run into the issue. These are just four ones that I particularly remember, serendipity at play happens all the time.   

- **Getting HTTP 500 instead of HTTP 404, resulting in a program error**  
  This issue is what inspired me to write this post. I was testing a new feature today on a new application we are working on. We had just introduced authorization feature, indicating that the users should not get to see pages on the application they were not authorized for. It has been tested, quite thoroughly by the pair of developers implementing the feature, and I was not intending to do a deep test on that, just as we had agreed in  the team.  
    
  I created a few users with different levels of rights, and made notes of pages the higher rights level had and the lower rights should not have. And while doing the notes of positive cases, I decided to try a few addresses without any preparation on my part. I was about to change the end part of the address to point to a non-existing page, and with the idea of writing some garbled text, I first tried just removing a final "s" from "users". Unexpectedly, the very first test I did ended up showing me a program error, a case we did not handle for the users. A case that I thought was specifically mentioned in the Jira issue about this change.  
    
  I tried the garbled text, the real pages and all there seemed to work to the extent I was testing them.  
    
  The surprise from the developers was clear: how did I find that? Detailed analysis of the problem shows there are 2 pages that in this application give a HTTP 500 response instead of HTTP 404 as the feature was designed to handle, for a reason of having controllers of those names on a different level, causing the application to crash - a technology specific problem.  
    
  The reason I tried that was that a small chance to the name of the page seemed to make different sense than a bigger change. And trying a few that appear in any way different for me just makes my life much more fun - with or without the problem.
- **Galumphing around, resulting in a program error**  
  This issue happened just less than a week ago. I was testing a feature I had tested hundreds of times before, and feeling a little impatient. Impatience changes how I use the product, I started clicking around the user interface, pressing buttons, inserting and removing text - a lot of inert actions that should have no impact.  
    
  I double-clicked on one out of the many radio buttons, and was presented with a program error dialog, much to my surprise. I isolated the steps to repro to just a double click in a specific location, and did some research around the product if similar behavior would appear elsewhere, without running into such cases.  
    
  Again, the developers were asking how did I find that. And again, I have no better explanation than saying that I vary my actions. It sounds great to be able to refer to galumphing, a technique coined by James Bach. I could immediately recognize that in use after I saw the problem, but while I was testing, I was just after variation to push my luck to never feel bored.
- **Sampling places and technologies after configurable product name change, resulting a broken old feature**  
  This issue is a little older, but I remember it particularly well because of the team discussions it caused us to have. We had been implementing a feature to make our product name configurable. The developer pointed out there were 57 instances where he had chanced it, and that he had tested the changes himself. I was about to look at it with another pair of eyes.  
    
  Knowing the product from perspective of features and technologies and user scenarios. I implicitly, without consulting anyone, decided to check a few places - there was no way I would repeat going through the 57 instances he had already tested, our product just isn't worth that level of investment for this feature, not with other things in the queue. Testing more of this would result in testing less of other more important things.   
    
  I opened the first dialog I had in mind where the configurable product name should be visible. The first one on my selections was a feature as deep in the application as I could imagine. And to my surprise, the feature did not work at all, as the dialog I was trying to open would not open.  
    
  After the surprise of me running into that as the first thing when testing this, the developer came back with the results of analysis. Out of the 57 places, I had run into the only one that did not work, and the reason was that this was with implemented with another technology. I can claim after the fact that I knew that (I did), but that did not really drive my decision.
- **Bookmarking a page, resulting in program error**  
  This issue is the first issue I started with at my new place of work at Granlund. On day 1 of new job, I was going through the introductory motions just as anyone else. I was shown the application and as I was about to head to a meeting that would introduce me to the ways of working, I quickly bookmarked the page I was shown to get back to it later, knowing I had no way of remembering things without notes as I was getting so much info. As I came back from the meeting, I was about to start testing. I went to my bookmark to log into the application, only to see a program error that blogged me from logging in.  
    
  After analysis, I know that on a huge application with a lot of different areas and pages, I had been lucky enough to bookmark the only page that could not handle a direct link. This idea of a test is on my list of things I do, but I did not try doing that on day 1 of new job. But serendipity had been a sure way of making an impression.

My current project reminds me that a lot of testing is serendipity and perseverance. Vary to push your luck, be open to possibilities, explore the limits of done. Keep trying more when you think you've tried all that is relevant - it is never too late.  
> It's not that I'm so smart, it's just that I stay with
> problems longer. – Albert Einstein

Sounds right to me.
