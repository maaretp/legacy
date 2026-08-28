---
title: "Focus on some, be blind to some - need faster learning"
date: 2014-12-18
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2014/12/focus-on-some-be-blind-to-some-need.html
---

# Focus on some, be blind to some - need faster learning

*Published 2014-12-18*  
*Source: <https://visible-quality.blogspot.com/2014/12/focus-on-some-be-blind-to-some-need.html>*

---

I'm trying to think why true incremental development and co-designing features seems to be so hard. The reason I think of this is that just when I thought we managed to do something better, the empirical evidence suggests that we failed. Now the question is if we will learn of this.  
  
We did earlier several features so that someone (our project manager) created a specification in collaboration with business representatives, turning their needs basically into paper prototype of user interface sketches. The developers would look at that, ask what ever and draw their conclusions on what to implement. I would look at that as a tester, see different things and when seeing the features in action, notice things that wouldn't work - either  because the user need and the design were out of synch or because the design was insufficient in relation to product context or because there were still minor issues developers had not noticed on the implementation. It was awful: at worst, we would do three rounds of redesign, as the feedback I would provide would trigger very good discussions with the business representatives, and we would learn that what we had specified was nowhere in the neighborhood of what we would actually need.  
  
To make things less awful, we changed so that we all sat together to do the designs, discuss the needs and guiding ideas for the latest feature. As we discussed, the designs changed - almost completely. That is positive, we are much closer to what we would need with the collaboration. But as discussions tend to go, the vocal people tend to get too much attention. If we would note problems we had previously of not understanding availability of functionalities in different states of the program, it would hog our attention. If we would talk about the labels and button locations on the user interface (like the business people wanted, it would hog our attention. So with all the discussion, in retrospect, we lost focus.  
  
There's major concepts within our program that guide all functionalities. They are like a frame that never goes away. We failed to talk about those. In retrospect, it was obvious to me. It was one of the things where we always fail, seeing features in relation to other features, especially system features. And yet, now that I'm testing the feature, it's obvious that we failed to deliver working software from a very central angle. There's a whole bunch of small fixes we don't need to do now, but adjusting things on the level of basic concepts might be quite much harder.  
  
There's really one big mistake we keep running into over and over again. Not having all the information at once is not the mistake. Not being able to pass information we might in retrospect think we had is not the mistake. Our mistake is that we build things in too big chunks, and accept delayed feedback.  
  
With two days before Christmas vacation and less than a week of work effort before a major demo, it's not exactly a fun thing to tell people that we added something that appears to work to the extent we need to demo it, but the old stuff we had is quite much broken. And that the new stuff only works in simple settings, if placed in realistic production scenarios, it fails in very relevant ways.  
  
We have a nice demo user interface with nice demo functionality. But is that what the system is about - hardly. We need to learn new ways of working together and learning together. Perhaps 2015 with mob programming could take us closer. A new years wish, perhaps?
