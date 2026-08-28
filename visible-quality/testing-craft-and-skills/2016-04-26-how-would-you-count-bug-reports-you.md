---
title: "How would you count bug reports you never get?"
date: 2016-04-26
updated: 2016-08-02
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/04/how-would-you-count-bug-reports-you.html
---

# How would you count bug reports you never get?

*Published 2016-04-26, updated 2016-08-02*  
*Source: <https://visible-quality.blogspot.com/2016/04/how-would-you-count-bug-reports-you.html>*

---

There's recently been a significant transformation on a piece of software we work on with my team. In the last month, we've done more releases of that piece than we managed to do in the year before it. There's a clear feeling of progress. And the progress has included the amount of code for the piece dropping to a quarter of where we started off with the transformation. The final frontier of siloed development has joined team ownership and our drive to clean up things to be understood.  
  
Looking at this piece of software, I'm observing an interesting aura of mysticism on how users approach it. It's like I'm moving into the past where I four years ago surprised our product manager with the idea that *software can work when he tries it out*- something that should be close to obvious in my books.  
  
I started to think about this seeing a tweet:  
> "We only had one or two bugs in production in 4 years of mob programming." [@WoodyZuill](https://twitter.com/WoodyZuill). <https://t.co/sKrEsC1VI3>
>
> — Cucumber (@cucumberbdd) [April 26, 2016](https://twitter.com/cucumberbdd/status/725018361197920256)

The worst piece of code my team delivered probably had also just one or two bugs in production over the last year. But for us, the reason was that the users would seek workarounds rather than ask for fixes, or that the bugs just did not bug the users enough for them to speak up.  
  
Since we moved the piece of software into the frequent release cycles, we've fixed a LOT of bugs users never complained about. A lot that users had not even run into. Looking at the  bugs we've fixed, I find it nearly impossible to believe that they could have been using the software all this time. But they did, they found their ways around everything that bugs us (and slows them down).  
  
When you get little to none in bug reports from production, do you assume all is well? My sample says I shouldn't. Even asking the users directly might not give you a realistic picture.  
  
And on the other areas where feedback is more frequent: if it bugs a user, it's a bug. And we have loads of things that bug the user, that we rather frame as feature requests, some of which we have no intention of acting upon. Counting them seems more of counterproductive. We could count how often we get interrupted with a quick request to change something in production that reorders our immediate priorities? But most of those wouldn't count as bugs in any traditional sense.
