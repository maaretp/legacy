---
title: "All of us have a test environment"
date: 2018-07-14
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/07/all-of-us-have-test-environment.html
---

# All of us have a test environment

*Published 2018-07-14, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/07/all-of-us-have-test-environment.html>*

---

This post is inspired by a text I saw fly by as I was reading stuff in the last hours: All of us have a test environment, but some of us are lucky enough to have a production environment too.  
  
Test environments have been somewhat of a specialty of mine for the 25 years I've spent in testing, yet I rarely talk about them. So to celebrate that, I wanted to take a trip down memory lane.  
  
**Lesson One: Make it Clean**  
  
I started as a localization tester for Windows applications. After a few decades, I still remember the routines I was taught early on. As I was starting to test a new build (we got them twice a week back then), I would first need to clean my environment. It meant disk imaging software and resetting the whole of Windows operating system to a state close to factory settings. Back then it wasn't a problem that after doing something like this, you'd spend the next hours in receiving updates. We just routinely took ourselves to what we considered a clean state.  
  
As you'd find a problem, the first thing people always would ask you was if it was tested on a clean machine. I can still remember how I felt with those questions, and the need of making sure I would never fail that check.  
  
**Lesson Two: You Don't Have to Make it Clean**  
  
Eventually, I changed jobs and obviously took with the a lot of the unspoken attitudes and ideas my first job had trained me in. I believed I knew what a test case looked like (numbered steps, y'all!) to an extent that I taught university students what I knew ruining some of them for a while.  
  
I worked on another Windows application, in a company with less of a routine on cleanliness of the test environments, and learned a lot about the fact that when environments are realistic as opposed to clean, there's a whole category of problems of relevance that we are finding. It might have made sense to leave those out as long as we were focusing on localization testing, but it definitely did not make any sense now that I was doing functional testing.  
  
I realized that we were not just testing our code, but our code in an environment. And that environment has a gazillion variables I could play with. Clean meant less variables in play and was useful for a purpose. But it definitely was not all there was.  
  
**Lesson Three: The Environment is Not My Machine but It's Also My Machine**  
  
Time moved forward, and application types I was testing became more varied. I ended up working with something I'd label as client - server and later on web. The Client - Server application environments no longer were as much under my personal control as the Windows applications I started off with. There was my machine with the client on it, but a huge dependency to a Server somewhere, often out of my reach. What version was where mattered. What I configured the Client to talk to mattered. And I learned of the concept of different test environments that would be under fairly regular new deliveries.  
  
We had integration test environment, meaning the Server environment where we'd deliver new versions fairly often and that was usually a mess. We had system test environment, where we'd deliver selected versions as they were deemed good enough from whatever was done with the Integration test environment. And we had an environment that was copy of Production, as most realistic but also not a place where we could bring in versions.  
  
For most people, these different environments were a list of addresses handed to them, but that was never my approach. I often ended up introducing new environments, rationalizing existing ones with rules, and knowing exactly what purpose each of them could give me with regards to how it impacted the flow of my testing.  
  
**Lesson Four: Sometimes They Cost a Million**  
  
Getting a new environment wasn't always straightforward, it was usually a few months of making a business case for it and then shopping some rack servers we could hide in our server lab. I remember standing in front of one of these racks, listening to the humming both from it and the air conditioning needed to run that much hardware and being fascinated. Even if it took a few months arguing and a few more months delivering, it was still something that could be done.  
  
But then I started working with Mainframes and a cost of a new environment went from some thousands to a million. It took me two years to get in a new environment while in this environment.  
  
Being aware of the cost (not just hardware but the work to configure), I learned the environments we were working on in even more detail. I would know what data (which day's production copy scrambled) would reside where. I would know which projects would do what testing that would cause the data to change. In a long chain of backend environments, I knew which environments belonged together.  
  
In particular, I knew how the environments were different from the production environment to the extent that I still think of a proud moment in my career when we were taking a multi-million project into production as big bang, and I had scheduled a test to happen in production as the first thing to do, one that we couldn't do elsewhere as the same kind of duplication and network topology wasn't available. And the test succeeded, meaning the application failed. It was one of those big problems and my proudness was centered around the fact that we managed to pinpoint and fix it within the 4 hour maintenance windows because we were prepared for it.  
  
**Lesson Five: It Shouldn't be Such a Specialty**  
  
Knowing the environments the way I did, I ended up being a go to person for people to check of which of the addresses to use. I felt frustrated that other people - in same kinds of positions that I was holding - did not seem to care enough to figure it out themselves. I was being more successful than others in my testing for knowing exactly what I was testing, and what pieces it consisted of. My tests were more relevant. I had less of "oops, wrong environment, wasn't supposed to work there".  
  
So think about your environments and your attitude towards the environments? Are they in your control or are you in their control?
