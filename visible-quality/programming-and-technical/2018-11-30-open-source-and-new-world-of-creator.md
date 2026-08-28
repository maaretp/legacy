---
title: "Open Source and the New World of Creator Responsibility"
date: 2018-11-30
updated: 2018-12-26
theme: programming-and-technical
labels: [Programming]
source: https://visible-quality.blogspot.com/2018/11/open-source-and-new-world-of-creator.html
---

# Open Source and the New World of Creator Responsibility

*Published 2018-11-30, updated 2018-12-26 · Labels: Programming*  
*Source: <https://visible-quality.blogspot.com/2018/11/open-source-and-new-world-of-creator.html>*

---

As I'm minding my own business, doing some testing and enjoying myself, I get brutally interrupted by an incoming message. Someone somewhere has a problem. With the product I work with. I know that I care a lot, deep down, but the timing of the message is just so inconvenient. Reluctantly I offload from the work I was doing, preparing myself mentally to dig into the intrusion.  
  
As I read the message and related bug report, I feel the frustration in me growing. The steps to reproduce the problem are missing. The description of the problem is vague. It feel like the reporter did not even understand what they were doing, let alone knowing what  the product was doing. Reading the text again and again, I come to the conclusion they have an actual problem, but their report, all without the right details and logs does not help me to do anything with it.  
  
The tester that I am, I start testing the situation myself. Sure enough, it is not like I have tested our product together with Google Ads management interface. As I set up the environment, I realize I have to have an actual campaign set up so that I could even reproduce the problem. I toy between the "going to ask for company credit card" and "use my own credit card, here's the opportunity I always wanted to try ads for my own stuff" and go for the easy route and build a little campaign to advertise my conference. I confirm the bug, test more to figure out exact steps to isolate it to know what is the minimal impact workaround I can suggest, collect the logs and attach all of my investigation into the records I started with.  
  
The fix is ready in 10 minutes. The release of the fix takes a little longer.  
  
All of this happened in a project where I get paid for my time. Yet I am frustrated. But what about when we find ourselves working on our pet projects, sharing them as open source?  
  
First of all, the code, whether closed or open source does what its creators make it do.   
> Two reminders in one tweet:  
> 1. Algorithms never make conscious decisions, they do what they’re told  
> 2. You’re responsible for what the code you write does, both socially and technically, including higher-order effects. <https://t.co/jRLHuGOXIk>
>
> — Pete Holiday (@toomuchpete) [November 24, 2018](https://twitter.com/toomuchpete/status/1066334159478693888?ref_src=twsrc%5Etfw)

  
This means there is always creator responsibility of what can be done with the software you created.  
  
With software, it's not just about being a creator as in writing some lines of code, but it is also being an owner of what you started creating. You can be responsible for the code you wrote to an extent, but when you move in open source projects to the idea of being responsible for code others created on a codebase you started, we're piling a lot of work and responsibilities on someone who did not really opt into it.  
  
There was a great example of that this week.

> Holy hell, Node. A package with 2 million downloads a week and the maintainer hands over control to a rando stranger? And now it's mining cryptocurrency. Wow.<https://t.co/V2mQ8fS2PZ> [pic.twitter.com/MkqhHzjic1](https://t.co/MkqhHzjic1)
>
> — Kenn White (@kennwhite) [November 26, 2018](https://twitter.com/kennwhite/status/1067133581435305984?ref_src=twsrc%5Etfw)

It wasn't \*mining\* it was \*stealing\* as many pointed out. But the really peculiar thing to look at was the formation of camps in assuming different responsibility for the owner as original contributor.   
  
Finally posting this was motivated by a good friend of mine running a relevant open source test automation tool project tweeting this:   
> As an author of an open source test automation tool, I'm surprised how bad bug reports we often get from testers. I don't expect many users to be able to provide code contributions, but reporting issues ought to be one of their core skills. </rant>

> — Pekka Klärck (@pekkaklarck) [November 29, 2018](https://twitter.com/pekkaklarck/status/1068092194060406784?ref_src=twsrc%5Etfw)

 Going back to my story to start this blog post, you can't really always expect that your users - that is what they are even if your project is free and open source - would take the time to isolate and report problems. And when you make it so, at worst you are like another open source maintainer who goes around bragging on quality of their code when reality is that their users just don't bother reporting but take the choice of just walking away.  
     
I know how to write good bug reports yet I rarely do. I only do it when I get paid for it, or as a result of it I get something I need. I want to optimize the time I spend and a quick report on problems is the smallest possible contribution I can choose to take.   
  
Information is valuable for a project that wishes for wider scale adoption. While there may not be direct money coming in from an free open source project, I find that many of the relevant creators have found a way of turning their thing into some income flow.  
  
Say thank you for making you \*aware\* you have work you can think about doing, and stop blaming anyone who works free. I know it is hard to do, even when you have a paying customer.
