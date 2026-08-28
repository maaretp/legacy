---
title: "A learning journey with unit tests just starting"
date: 2015-01-14
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2015/01/a-learning-journey-with-unit-tests-just.html
---

# A learning journey with unit tests just starting

*Published 2015-01-14*  
*Source: <https://visible-quality.blogspot.com/2015/01/a-learning-journey-with-unit-tests-just.html>*

---

I know I'm privileged. I have work that allows me to craft my work into whatever I personally want it to be. I can share details of my work other people could not share. I have friends and colleagues that are willing to help me with whatever I'm ready to accept help on. The privileges with a new year brings me to a new thing I'm just starting to work on: unit tests.   
  
My team does *some* unit tests but the scale is small and all of it is test-after. The tools and approaches we've chosen come from books and articles, and the level of fluency we have on the whole idea of unit tests is low. I've kept my distance to unit tests, occasionally looking through what there is, but I never took the time to get my environment to a point where I could even run them. Looking through them happens mostly in secret, all by myself, but occasionally I might also ask a developer to show me around, just to make them talk of what they've been up to.  
  
I have had a feeling that due to lack of fluency in the practice, we're really not getting the hang of it.  The lack of fluency is also driving us heavily towards Selenium tests, where the feedback cycle is long as we run those tests only with nightly builds. And even there now that we've added more tests, we're seeing symptoms of brittleness that lowers the information value our Selenium tests provide.   
  
I feel I'd like to help. I can help by bringing in coaches and
consultants, and that is how we ever even got started. But someone
visiting with examples that are not your code tends to be quite
different from the actual work. A day tends to be different than longer term. And my company tends to not be ready to pay for longer term help. So I asked help as in a personal favor for me to learn unit testing from a friend with much better knowledge on the topic than anyone in my team. This starts my journey into total discomfort, as he volunteers to personally coach me and pair with me to help me learn things I know I could and should, but not always want to. The step from theory of code and reading of code into writing it, even with a great developer to pair up with, is going to be causing me some growing pains.  
  
With our first session, I came in with the idea that we could look at some tests the team's architect - the best unit tester as far as my perceptions would be right - had just added. I wanted to see what is there, and if that would help me make some sense into the whole thing in my head. We randomly sampled one.  
  

  
Just looking at it left me confused.  

- I had no idea what the "comparator" the test is testing is
- Naming into "method\_scenario\_result" is probably consistent with a good practice from a book, but it doesn't exactly help reading the test
- I could just not make sense of what the test was and was already ready to give up

All by myself, I would probably have given up. But with a friend with me, I was asked to give him seven minutes of a time box to work on the test with me, and we'd see then if it starts making more sense.  
  
He said there would be some work we could do on readability of the test, and we started from creating the same test idea in a bit different format, where everything we worked on focused on readability. The tests would be named more simply to read as English, the concepts would be pulled out and grouped both on level of tests and variables within the tests, and the test data we would use would try to emphasize the fact that we're testing case sensitivity. With test data he was advising me to create, I found connections to stuff I do when I test - being able to follow the data, like entering text into a text field that tells me where that particular piece of data had been entered.  
  
Seven minutes passed, and I had started to feel there was hope after all. With another seven minutes with him explaining changes step by step with me on the keyboard asking whenever I needed to clarify things, we ended up with the new, extended version of the same test and found inconsistencies in null/empty value handling that could be a bug. We also changed the code the test was testing to handle nulls.  
  

With the short time of changing the code with readability in mind, I feel a lot happened. Some of the information in the original tests was not relevant to what the test was about (the content of the URLs did not matter), and as it got removed, it made understanding what was there simpler. Instead of every test being an individual check, we'd group checks so that each test checks things that belong together. It would end up as something I can read.  
  
It would be foolish of me to claim I now could do all of this by myself. I feel the main outcome of the first test was a positive feeling that this could eventually make sense, and that I would not need to run away and hide even though I was feeling way out of my comfort zone.
