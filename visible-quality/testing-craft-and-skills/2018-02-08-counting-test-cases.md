---
title: "Counting test cases"
date: 2018-02-08
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/02/counting-test-cases.html
---

# Counting test cases

*Published 2018-02-08, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/02/counting-test-cases.html>*

---

Confession: I count test cases. Before you get all riled up, read further. I count test cases for the purpose of understanding how much of something there is. A typical example for my counting is "30 test cases in our test automation" for understanding how many conceptual program pieces there are or "100 lines of functionality added, yet number of unit tests stays the same". Counting things is useful, but it is not all there is.  

On the other hand, it's been at least 8 years since I last counted test cases as in understanding how many there are in a manual test set, how many of them have been passed and how many failed, and how many yet to be discovered for our list through exploring. To be more precise, it's been 8  years since anyone managed to coerce me to write down a test case, or guide anyone close to me to write them down. Instead, I write test cases into automation and free up majority of my time in freeform exploratory testing.

It is also 6 years since I last did session based test management, counting sessions or time in functional areas as a means of progress. And even then, I did it for two weeks to prove a point: I was worth trusting to do good testing without paying extra in time to impose a visibility framework of this sort.

These became irrelevant to me, as I helped my teams move to continuous delivery. When we manage scope of hours or days instead of weeks or months, the numbers no longer matter. Quality of testing we do matters. And we learn about that as we deliver continuously, carefully tuning so that our customers could forget we ever updated their software.

I started this post with an idea of examining my views on counting test cases, if I was asked to do them again. With all the experience I have, would I? When would I? And is there anything I would advise to those who still do?

**Finding the Least Amount of Meaning**

A core principle in testing is one coined by Dijkstra quite a while ago: we can't prove absence of bugs, just show the presence of those. So even if a million test cases passed, the tests that are worthwhile are the ones failing.  
  
Twitter brings me a haha moment:

> Hahaha, I found this picture I created for a presentation I did many years ago... [@NicolaO55](https://twitter.com/NicolaO55?ref_src=twsrc%5Etfw) [@RymdKratta](https://twitter.com/RymdKratta?ref_src=twsrc%5Etfw) [pic.twitter.com/XUu6L7233k](https://t.co/XUu6L7233k)
>
> — Maria Kedemo (@mariakedemo) [February 7, 2018](https://twitter.com/mariakedemo/status/961296070390272000?ref_src=twsrc%5Etfw)

The image with texts coins the least amount of meaning in counting test cases: counting the ones passed. Counting the ones that did not find bugs. Counting only the ones that pass. Forgetting that each change for the bugs found invalidates the ones already passed introducing a new test target.  
  
**Adding More Meaning**  
  
Thinking back 8 years for the time I last counted test cases, I remember a futile battle turning into a productive negotiation. I started off with the premise that the way things had always been done - counting passes and failed tests - was a way to take us to bad testing and bad relationship with management. I was faced with the fact that with a 30-days acceptance testing project after multi-year delivery project, no one was comfortable without a way to see how testing was progressing. I couldn't go full on session-based test management. I find that it was a poor choice to replace what was in place with the amount of work needed to ramp up skills of business specialist in the methodology.  
  
I approached the problem at hand with experimentation. Experiments are a way of asking to try something different, just this time without commitment to doing it again because it may go bad too. We started off where the organization was before me: writing test cases in advance, and following pass/fail numbers throughout the 30 days.  
  
In the first 30-day acceptance testing, I started stretching with what I perceived as the biggest risk of using test cases as measure in a traditional way: **quality of testing that gets performed**. With pre-designed test cases, you create the ideas of what to test when you know the least. You have no software in your hands just the promiseware of requirements. The way test cases were created was looking at an old version of the product, imagining how the promises change that and making those scenarios that walk us through to see the changes in action.  
  
With my lead, we introduced two kinds of test cases. The first batch was just like it had always been. Details of where to go, what to look for. The second batch was different. We used HP toolset to create  template test case, an idea of reusable steps for test cases. The template test case steps were a high level of the process the system was supporting us through, no details. The actual test cases were test data: people whose data we could use to walk through the process, in different ways. We split the time available so that we first tested with the traditional type of tests for half the time available, and the other half was left for what was essentially exploratory testing.  
  
All the bugs we found - and we did find quite a few - were found with the latter type of tests. We learned the mix was really good for us at that point of time. Jumping directly to freedom would have made people nervous. Mix of the old and the new allowed us to do great, stretching people not too far away from their current skills and comfort zones. We reported tests planned, passed, failed, and started-yet-not-finished across both types of test cases.  
  
In the second 30-day acceptance testing I lead for a different product, we stretched further into exploratory testing. The system we were testing had a complex processing logic with one step reaching to a third party system including manual processing. We again created test data as test cases and template test cases as reusable steps, and step 7 in the 12 step process was the information the 3rd party system needed to pass us. The group testing was seasoned in the business process, and had never used test cases before and this was a perfect fit for them.  
  
Results in what testing found before going live were equally great. The test numbers showed us that a big portion of tests were in started-yet-not-finished state, and helped us encourage the 3rd party system in tracking whether our requests of info arrived on both ends.  
  
The third 30-day acceptance testing I lead experimented in the secondary risk of using test cases as measure of progress: **conveying the nature of testing as activity**. In the first two efforts, I was aware of the illusion tests marked passed or failed were creating. As we found a problem, a new version of the system was introduced. When we found a critical cross-system change-introducing bug when 80% of tests were passed, the remaining 20% wasn't really enough. The idea of the metric was not only founded on guidance that lowered the quality of testing that could happen, but also encouraged lying on the coverage assuming there was no change.  
  
We still used test case counts, but we changed our graphs and communication to a metaphor of a Progress Bar. We all know how progress bars are. Time waited for something to update and the number shown on the screen have often some connection, but it is not predictable and reliable. It's something to just say 'hold on, wait, be patient - working on something'.  With the progress bar, we introduced a 30% "invisible tests" number, showing the allocation we expected for repeating tests or introducing tests while testing. By the time we were at old 100% of tests passed, we really needed the extra 30% to run tests again for change and we avoided the old stupid ways of non-testing managers deciding that we were done when things planned were done once.  
  
**Why Would a Project Need Test Case Counts?**  
  
I'm not for test case counts. However, when I have to deal with them, I've learned the core of playing them for the goals of doing a good job testing:  

- Free the "test case". It's just any placeholder of things to do. It could be an exploratory testing charter. They don't need to be the same size. Trying to make them same size is just foolish.
- Communicate 'best before' idea for results. A test passed today can be not executed tomorrow. And how quickly the 'best before' date hits you, depends a lot on the organization.

The projects need test case counts if they have no other measure of progress and are not ready to place trust in getting a spoken reliable measure of progress without a forced test case counting methodology.

When I started looking at testing as time investment and reporting against time, things got more straightforward for me. Given a week, I can always say that on 4 days used, I have only one left. While exploring, I can explain what I've discovered in that time, and what I would use the next week on. I can do that, teams of exploratory testers can do that, but not all business specialists temporarily assigned as testers can do that.

I know counting test cases is meaningless. I know the same test case done early on can take more time because I can't stop myself from exploring around whatever I was given. I know the same test case done again later can find a problem that was there in the first place, but I was just not in a state with my learning that enabled me to see it.   Constraining on test cases when the process is about learning makes absolutely no sense.

But I accept that sometimes I have to do things that make little sense to me, because they help others. I also know that I can experiment and offer alternatives that slowly take people towards where I am with understanding the dynamics around testing. Sometimes, asking people to trust me on my perceptions of status is enough. I've learned to be away enough to build ways of working that don't crumble on my absence.

A great option to take people towards is more frequent deliveries. When meeting an organization that counts test cases, that is now my default change I would go about introducing.
