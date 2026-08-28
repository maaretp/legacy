---
title: "Natural laziness and 'It works on my machine'"
date: 2015-09-28
updated: 2018-12-26
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2015/09/natural-laziness-and-it-works-on-my.html
---

# Natural laziness and "It works on my machine"

*Published 2015-09-28, updated 2018-12-26*  
*Source: <https://visible-quality.blogspot.com/2015/09/natural-laziness-and-it-works-on-my.html>*

---

When teaching programming to kids, a first "rule of programming" sinks in well. Telling the kids *programmers are lazy*, and that you should never write more than a few letters of whatever method you are about to call. Let tools do the work for you when you can.   
  
My personal experience of people in the software industry is though that most of us are far from lazy. Programmers automate the tedium, identifying repetitive (and even potentially repetitive) tasks and turn them into code. That level of effort shows qualities where laziness isn't the first word that comes to mind.  
  
But there's things where programmers are lazy in ways I find sometimes hard to comprehend. The laziness coins to a way of thinking that her own computer is the center of the universe, resulting in the infamous "it works on my machine" phrase.  
  
At work, I was testing a few minor changes to the user interface. I had reported that there was a bit too much of indentation in one particular dialog. I had reported a choice of color in certain places was a bit to gray, making it appear disabled. Simple things. Simple things that stayed in our queue quite a while. So when they finally came through, I was happy with the idea that we'd now have two items less and we could be one step closer to our targeted "stop-and-fix" ideal, that we struggle with as a team on some areas more than others.  
  
So I tested the changes. I opened the two distinct places that had been broken and rightly so, they were now changes. But the first thing I observe is that the thing that used to be grey but was properly indented was now incorrectly indented while black. And looking around a little more, to it seemed like to fix one specific thing, *every other place in the program had been broken*.  
  
I reminded myself to breath while I was going through what I perceived as the obvious: the developer could not have tested this at all. With a few breaths in and out, I rephrased it in my head: the developer could not have tested this in a production-like environment. That's where the laziness in testing shows. My developers always keep hoping that their development environment is like production. And regularly they learn (from me) that this is not the case.  
  
It turned out that our minified styles were included in version control where they were not supposed to be, overriding old stuff of top of the new. Developers were happy to find a root cause that enforces the idea that they still don't need to go outside their own environments. *If it only stays this way,* says a little voice in my head. So we have a discussion, resulting in changes to our TFS configuration.  
  
The core problem remains. The developer environment is not the same as the end user environment, even in a ridiculously tiny product development like ours, and more so on anything bigger I've had a chance to work on. If I cannot overcome the natural laziness of the developers on this like my friends keep suggesting, there's another way to solve the problem. Turning the problem into a programming problem of test automation over various environments.  
  
Meanwhile, I'm practicing breathing and encouraging use of other test environments at least for particular types of changes. It had been a while since I had to hear "It works on my machine".
