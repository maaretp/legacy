---
title: "Let down by the Realworld app"
date: 2021-05-07
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2021/05/let-down-by-realworld-app.html
---

# Let down by the Realworld app

*Published 2021-05-07*  
*Source: <https://visible-quality.blogspot.com/2021/05/let-down-by-realworld-app.html>*

---

This week, I finally got to making space in my calendar to pair up with Hamid Riaz on start of creating a new exploratory testing course centered around yet another test target: [the Realworld App](http://realworld.io/). Drawn in by the promise of "mother of all demo apps" and the lovely appearance of a programmer community who had contributed examples for the demo app frontends and backends in so many sets of technology, I had high expectations. I wanted to create a course that would teach the parts of exploratory testing that are *hard* and we only get to *in good agile teams that have their quality game in shape*.

Instead, I was reminded again that demo apps without the active agile team, no matter how good the original developer may have been, never get to the point of having their quality game in shape.

The first example implementation I picked up from the list was a end-to-end testing demo setup, only to learn it had been years since it was last updated (sigh), and the most basic of the instructions on how to get it running relied on half-docker (good), half local OS, and local OS was expected to be anything but what I had - Windows. While I have worked my way through of setting all too many projects that expect mac / linux to build on my work Windows, I did not feel up for the task today. So next option.

Next I picked up a nodejs implementation, no dockerizing involved but I could add that to make it more isolated for anyone testing after me on the course. At this point Hamid joined me.

Without too much effort, we got through installing Mongo, and all the dependencies needed. We installed postman, imported the tests and eventually also the environment variables provided, and run the tests only to note that some of the functionality that was supposed to be there, was no longer there - the years between the last changes and the latest of MongoDB seemed to do the trick of making the application fail, and we were not told of the version the code expected.

After the pairing, I summed up on twitter:

> When the last commit is "Jan 1st, 2018" and npm install results in "found 91 vulnerabilities (35 low, 17 moderate, 38 high, 1 critical)", is that enough to test to know to run away from it?
>
> — Maaret Pyhäjärvi (@maaretp) [May 5, 2021](https://twitter.com/maaretp/status/1390002180258680834?ref_src=twsrc%5Etfw)

I should have known then. Software that is not maintained is not worthwhile target for realworld testing.

When office work the next day added to inspiration of forgetting that results of testing don't stay valid for long even when you don't change anything let alone when you do, I concluded:

> If it is a software feature and we tested it six months ago, you \*must\* understand by now that the results from back then are not quite valid today?
>
> — Maaret Pyhäjärvi (@maaretp) [May 6, 2021](https://twitter.com/maaretp/status/1390326281477271554?ref_src=twsrc%5Etfw)

My search for a worthwhile test target to teach testing that does not just succeed for the mere sloppiness of the org that created them still continues.
