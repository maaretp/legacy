---
title: "My first full day of Mob Programming"
date: 2015-09-09
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Mobbing]
source: https://visible-quality.blogspot.com/2015/09/my-first-full-day-of-mob-programming.html
---

# My first full day of Mob Programming

*Published 2015-09-09, updated 2017-07-22 · Labels: Mobbing*  
*Source: <https://visible-quality.blogspot.com/2015/09/my-first-full-day-of-mob-programming.html>*

---

We've been doing these learning sessions with Mob Programming. We've worked on refactoring, Selenium Webdriver tests on our application, on our unit tests and now on replacing an old component / technology with new. On the last, we spent a full day working as a mob, while the others have been 2 hours of practice on production code.  
  
I'm finding it interesting to see how the group's dynamic changes depending on what type of task we're working on. When we work with something relatively simple (like the first two sessions), our problems of working as a group emerge easily. The driver will not wait for navigators to tell what to do but wants to "show off" or "just get this done quickly". The navigators step away from navigating, leaving it all to two vocal people, so it starts to look more like pair programming with the rest of people watching. From the first two sessions, we agreed to the third we'd go a step back from mob programming (driver - navigators) to Randori (driver - designated navigator - other navigators).  
  
The third session task was completely different. This time, none of us in the mob could actually have done the task all by themselves, so the experience showed a lot more of the idea of bringing the best of everyone into the task. Our task was to replace in one dialog an old grid component with a new Kendo grid. It was the first place in the program where we had to work with subgrids and this brought in the fact that none had knowledge on how exactly that should be done. There were none of our own application examples to look for help.  
  
With this task, Randori did not make sense. Having someone navigate who has no clue of what we're doing, isn't going to help with the navigation skills practice - for that we need something more shared. So we went for group navigation. And it worked much better than before. Partly because one of the developers opted out of the session and complaining about 7 people looking while 1 is working did not interrupt us. Partly because the task at hand required a group to be done effectively. And learning (through retrospecting) could also have it's share in doing better - trying, failing and talking about it probably changes the situation.  
  
We worked as planned for 2 hours before lunch, but as we were not done with the task completely (someone told it was a week of work, no wonder we couldn't do it in two hours...) we discussed how to continue. With my gentle push, I knew that at least two developers would pair up on continuing on it for learning purposes, and the invite to join to mob was open. While there was a mob of 7 in the morning, there was a mob of 4 in the afternoon. The devs invited me into the rotation also in the afternoon.  
  
There were all sorts of events and thoughts I noted during the day:  

- Learning coding steals my focus from thinking "like a tester". I would need to use significant energy into learning what was going on in the code, so that I could contribute with the others. The thoughts of "this should be tested" don't fit into that way of thinking, I felt that for doing what I usually do, I need to take a step back from learning the details. It probably changes over long term for me when the code does not require as much attention continuously.
- I could introduce some things from a tester perspective. Like starting the application while developing in different browsers. Or changing the data or making it more versatile to see problems more clearly and widely. Neither one of these ideas was particularly well received when the focus is on the code and code alone, but I can see that they will humor me with these on the long term, especially after we would do exploratory testing on the mob too.
- There were many things that we should have had a mechanism to park for future that emerged during the session. We were annoyed with the tools and I felt a need to make a note of doing something about it soon, yet later (seems we did, as first individual task of one dev). There were ideas of what we'd like to learn. And things we'd like to get back to to finish them, in particular adding localization as the last task and any strings in the UI in general. But I guess the code might remind us about some of these later.
- We saw many surprises from a technical perspective. We learned together there were two types of icons, and that to get them visible, we needed two different ways of implementing those. We ended up having a discussion about one/many subgrids and changed our implementation idea on the fly as we realized that the embedded assumption of one did not meet the needs of the functionality we were supporting.
- Knowing HTML helps. While it might not be "real code but markup", it helps a lot when you know what the tags do. I felt my years of tweaking html manually were useful in building a connection on my participation in the mob.
- The tooling problems you can't do anything about will annoy you 10 times more in a mob. We had a Visual Studio 2015 application restart problem requiring us to run the app again after changes. The slowness became painful soon. Similarly, Visual Studio 2015 was lagging behind in recognizing some of the changes we did, and waiting for the tool to become responsive again was more painful this way than it usually is.
- Slow feedback with missing unit tests was very painful to me, not sure if others paid much attention to it. I've seen too much of TDD lately to learn to appreciate the fast feedback and knowledge of your old assumptions still being there all together when jumping around to change things. I felt certain I could help the team to share that pain  (and remove it) if we'd just mob more.
- Tens of little mistakes got fixed immediately. Omissions. Typos. Wrong implementation with respect to intent. Bad names. Unnecessary pieces of code. Inappropriate data structure selections. I really enjoyed hearing my devs joke about "that bug would have been a nasty one to try to find debugging later".
- My slowness as a driver was a good thing. It allowed room for clarity of thought. It seemed like having to navigate on a slightly lower level of abstraction made the communication of where we're going and what we're doing clearer. And that slowness improves tremendously already in a day with learning (and relearning) more of the shortcuts.
- The two floors difference when needing one's advice in afternoon who was not joining ended up as worse code than it should have been. We could have called. We could have asked him. But we did not. We did something. I suspect we do that a lot.

I had moments where I would think I'd rather be doing anything else but spend my day with the code. But I loved the social aspect of it, being with my team, having a team instead of people who talk to me once a week and when I initiate a question. And I loved how proud I felt about the people I work with and their skills, abilities and attitudes. We play well together.

It felt appropriate this day of mobbing was the same day when [Llewellyn Falco](http://twitter.com/llewellynfalco) created his little infographic on putting a group of people together. That really sums up how it is: getting the best out of us all. Some of my best is still in front of us, when we actually explore the feature we're creating.

[![](../_images/coxj5rluwaaiqmk-84899299.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoR70t7P72Jcxa9UfwT87rdnX_0WPIpC9RJBIHSN4kmvvK1dTl_MxHHyvY_8k7smQzC8tWizwIboQtdLl1O0inqmIXOCMSgMDiHi3kXJC7rr1qWzaIz1AftYnaWkWtp0HOQLfD4Yv73Q/s1600/COXj5RlUwAAIQmK.mp4)
