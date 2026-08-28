---
title: "Traditional pairing on adding some Selenium tests"
date: 2015-08-28
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Pairing]
source: https://visible-quality.blogspot.com/2015/08/traditional-pairing-as-comparison-point.html
---

# Traditional pairing on adding some Selenium tests

*Published 2015-08-28, updated 2017-07-22 · Labels: Pairing*  
*Source: <https://visible-quality.blogspot.com/2015/08/traditional-pairing-as-comparison-point.html>*

---

Since my team isn't big on pairing, when I get them to pair, I tend to let things happen as they happen without insisting on mechanisms. Strong-style pairing does not happen naturally.  
  
Today I paired with our summer intern, who's been spending some of his summer getting around our Selenium Webdriver -tests. Pairing meant joining him on his work of today with whatever I could bring into it. And the reason we paired is that I'm an expert in what features there are and how we might know if they work, and he was "out of scenarios to automate".  
  
His computer, his tools and technology, and I was sitting by him fighting sleep. He was very helpful speaking about what he was doing, which is something I've learned not to take for granted. Even though I'm familiar enough with our structure, keeping myself up to date on where he clicked and where he ended up, reading the filenames from the tabs and interrupting him whenever things did not make sense was hard. I was continuously feeling it was too exhausting, that I was not learning as much as I'd like and that I was there just to remind of the scenario we were automating. This was very much traditional style pairing. I could review whatever he was doing. I could contribute and did. I fixed typos and corrected the test naming. I required concepts relevant to the test to be visible in the test and not hidden in the underlying structures to improve readability of the test. I observed the application to realize which wait from our utilities would be appropriate. And I was in control of the test scenario, what happens first and what verifications should be in place. I wasn't useless, but I wasn't as engaged as I tend to be when driving / navigating in the Strong-style.  
  
This however left me thinking: if a non-coder pairs up with a developer, it's easy to imagine they might at first prefer this style. Even if they are asleep most of the time on the details, they are not challenged to actually get into the code. If they drive in strong-style, they will learn to code little by little. The work proceeds slower, as there's more learning going on. If they navigate in strong-style, there's a bit of a confusion on what part is navigating on an abstract level and what part is sharing the navigation with the driver.  
  
So there might be a balancing thing here: how much time are you willing to invest in knowledge transfer in the pairing? Strong-style transfers more knowledge. Traditional style allows two experts of very different fields co-exists and collaborate.  
  
I had enough time to let my mind wonder: for a test that I do manually in 20 seconds, we spent 1,5 hours building the test. And most of the stuff we used was pre-implemented. A big chunk went into finding out what to wait on to avoid Sleeps. I wonder if I will ever see this work worthy of my time within my interests. It bears little to no resemblance to what I know as testing.   
  
*Added:*  
*Hmm, the smell in traditional pairing might be: "I did not have to put in much of my effort and this was not a good use of my time".*
