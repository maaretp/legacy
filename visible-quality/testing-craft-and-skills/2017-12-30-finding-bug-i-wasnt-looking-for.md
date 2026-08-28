---
title: "Finding a Bug I wasn't looking for"
date: 2017-12-30
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2017/12/finding-bug-i-wasnt-looking-for.html
---

# Finding a Bug I wasn't looking for

*Published 2017-12-30, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2017/12/finding-bug-i-wasnt-looking-for.html>*

---

Some years ago, I was working as a test manager on a project where I was considered "too valuable to test". So I tested in secret, to be able to guide the people that were not as "valuable" as I was, to make them truly valuable.  
  
We were an acceptance testing group on customer side, and the thing we were building would take years and years before there was all the end to end layers to use it like an end user would. A lot of the testing got postponed as there was no GUI - leaving us thin on resourcing early on. There were multiple contractors building the different layers, and a lot of self-inflicted complexity.  
  
The core of the system was a calculation engine, a set of web services sitting somewhere. With the little effort and weird constraints on my time, I still managed to set up up to test something while it had no UI.  
  
We used SoapUI to send and receive messages. The freebie version back then did not have a nice "fill in the blanks" approach like the pro one, and it scared the hell out of some of my then colleagues. So we practiced in layers, putting values in excel sheets and then filling the values back into the messages. As my  group learned to recognize that amongst all the extra technical cruft was values they cared deeply for and concepts they could understand better than any of the developers, we moved to working with the raw messages.  
  
In particular, I remember one of my early days of trying to figure out the system of thousands of pages of specification with using it. I could figure out that there were three fields that needed filling as compulsory, the other stuff was all sorts of overrides. So I took a listing of a set of those three things in some thousands, and parametrized to send thousands of messages, saving responses on my hard drive.  
  
I did not really know what I would be looking for, but I was curious of the output. I opened one in Notepad++, and skimmed through thousands of lines of response. There was no way I would know if this was right or wrong. I got caught up seeing error codes, and made little post-it notes categorizing what I was seeing. I repeated this with another message, and felt desperate. So out of a whim, I opened all the messages I had and started searching codes I had on my notes across all the messages.  
  
The first code I was searching for was something that I conceptually understood that it shouldn't be that common. Yet, 90 % of the messages I had included that code. I checked with a business expert, and indeed my layman understanding was correct - the system was broken in a significant way if this code was this common. It meant lots of manual work for a system that was intended to automate decisions in the millions.  
  
By playing around to understand when told not to, I found a bug I wasn't looking for. But one that was a no go in a system like that.  
  
My greatest regret is that I spent time in the management layers, fighting in their terms. With the skills I have as a tester, I would have won out the fight for my organization if I just tested. Even when told not to. I was too valuable not to test.  
  
This experience made sure I would again find places to work that did not consider the most expensive tester someone who wasn't allowed to test. And I've been in right kind of organizations, making a difference ever since.
