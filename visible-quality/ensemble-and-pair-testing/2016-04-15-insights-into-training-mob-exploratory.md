---
title: "Insights into training mob exploratory testing"
date: 2016-04-15
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Exploratory Testing, Mobbing]
source: https://visible-quality.blogspot.com/2016/04/insights-into-training-mob-exploratory.html
---

# Insights into training mob exploratory testing

*Published 2016-04-15, updated 2017-07-22 · Labels: Exploratory Testing, Mobbing*  
*Source: <https://visible-quality.blogspot.com/2016/04/insights-into-training-mob-exploratory.html>*

---

I tried it again. Taking my style of mob exploratory testing to unknown, unchartered waters. I delivered a training day where we learn through testing of the client organization's own software. Software I've never seen before we start testing it.  
  
I know I need more practice until the point where I no longer feel afraid of not being able to do it. Moving around with different software takes my quick learning ability out for a stretch, that often feels a little uncomfortable. But it brings such insights for my trainees that any of my discomfort is justified.  
  
I asked the organization to  bring in a laptop with a test environment with their software on it, and select an area out of their documentation we could work on. The documentation is often a test case or a piece of requirements document. We start with identifying an area and exploring it. We extend to using the documentation only a little later, first impressions are built without constraint of a document.   
  
There were a few insightful moments for me that I wanted to make note of:  
  
**Less than 15 minutes to first relevant bug**  
  
We were testing a feature I label here "meters". I quickly learned something that was obvious to everyone else that there's two kinds of meters, and that they are different enough to justify having their own create functionalities. Yet the form opening seemed very much the same, and I still seemed to have options of changing my mind not only between the two types we started with, but a dozen others. The concepts were drawing in front of me, as I could map those to physical entities taken to the software world. I did not agree with the design, but that was nothing to mention in the beginning since more info would be needed.  
  
We created both kinds of meters, and making notes of functionalities we saw within those. As I asked the group to note a particular piece of functionality by giving it a name, the group also tried selecting the options. End result was serendipity: out of the two meter types, we could only be creating one as the other would have a remaining database error message. And it was not even illegal data, just a combination of something legal deeper than the first level.  
  
**Caring for code -discussion**  
  
Later in the day, a discussion took place that kind of surprised me. I shared how I test our daily releases looking at what developer says vs. what code / checkin says to assess risks and to build a per-change strategy. A developer in my training looked puzzled and voiced out his idea: "Is that what testers usually do?".  
  
I explained that I look at the code to build a model of how well we understand the whole. Inconsistencies in what I hear and see lead me to insights on focus areas. Overemphasis of something does the same. I look for patterns that lead me to add things that are missing. And shape of code has proven very useful for me for that.  
  
The puzzled look continues, and we end up asking the audience of 20 people - from management, testing, programming and support if anyone does anything of this sort. None came forward.  
  
This left me wondering if it's something more special than I had given it credit for. Because still when doing that I don't "review code" or "read code". I look at size and shape rather than contents. And I find there often is an idea that the size and shape leads me to that makes the software speak to me to reveal more potential problems.  
  
**"This is not the testing we do here, but should"**  
  
My last note is on a comment I was given from behind the scenes by a friend that brought me in to do the training. As he checked on how we're doing, the comment was that I was teaching testing they don't really do, but should. I suspect they do, but don't talk about it enough.  
  
Talking about how we do intelligent manual exploratory testing happens way too rarely. And sharing more about it with anyone who wants to hear (and some who don't) would make life as testers better.  
  
My takeaway was that a lot of this stuff boils down to learning to talk about it. Communication. Helping people see what I do. And it left me with the idea that mobbing is indeed powerful. It allowed me to show testing in a way people think don't happen.
