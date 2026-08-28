---
title: "You don't need a different person to test what you did"
date: 2015-10-29
updated: 2016-08-02
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2015/10/you-dont-need-different-person-to-test.html
---

# You don't need a different person to test what you did

*Published 2015-10-29, updated 2016-08-02*  
*Source: <https://visible-quality.blogspot.com/2015/10/you-dont-need-different-person-to-test.html>*

---

If it is unclear to anyone reading my blog, I'm very much a tester. Nothing I do outside the domain of what testers usually do changes the fact that I love testing, I care for testing and I want to learn about testing. There might be days when I'm the product manager. There might be days when I'm the programmer. And the more people tell me that there's things testers don't do, the more I go and break the wall that is just imaginary.  
  
On the other hand, I've been a tester for 20 years. I work long, intensive days learning my craft. I pay attention to how I test. I pay attention to where my ideas come from, collect perspectives and ways of getting me into perspectives that everyone else in my team misses. And I'm getting pretty good at that, and yet there is so much more to learn about how to test in a world of unknown unknowns, too much information and myriad of connections. It's the best thing ever. And it's hard work.  
  
It's hard work that haven't given me time to do manual regression testing, because I keep coming up with new perspectives (and I think manual regression testing can also be done by developers, increasing the likelihood of it turning into automation). It's hard work that haven't given me enough time to learn to be as excellent in programming as I could be if I had chosen differently. But testing is my superpower, it helps my team do awesome stuff together. It helps our product manager come thank my team about delivering consistently working software, and it lets me be proud of my developers who invite my contribution (even if still way too slowly) and actively act on the feedback they can get from me.  
  
You become great at testing by choosing your focus like a tester chooses. Practicing testing. Programming is fun, but it's different. It creates different thought patterns that the focus on bugs, value, business and systems. To build great software, we need both thought patterns, preferably in close collaboration.  
  
I was again tweeting today about the stupidity of my own thoughts in hindsight, realizing how much effort I've wasted (without creating any additional value) by logging bugs into bug database about user message typos, over the option of skipping the logging and just going in and fixing them. I've discussed my way through the layers of resistance to get access to the source code only fairly recently, still causing regular stress to developers who see I've changed a file they consider *their own* to fix typos in strings. But that takes us forward. It's time-saving for us all, that I approach different problems differently. The risk of changing a string to be printed to two letters shorter has implications, but just as developers are able to check their changes, I check mine. The tester in me is strong, it has no problems overpowering the programmer me.  
  
But when I tweet about things like this, my colleagues in testing remind me of how much my mind has changed. This is a great example:  
> [@maaretp](https://twitter.com/maaretp) After you play the role of dev & fix a typo, does another, different person play the role of tester & check your work?
>
> — dsynadinos (@dsynadinos) [October 29, 2015](https://twitter.com/dsynadinos/status/659702351662587904)

I too used to think the relevant bit was having two people, a programmer and a tester. I used to think there was things a tester should do (and nothing would stop a programmer from taking role of a tester, except skills)  the check your work part.  
  
What I've learned, looking at things in more detail and with less abstractions, is that the changes we do into code are not all the same. For non-programming testers (one of which I still consider myself to be most of the time) the changes in software to make it work can appear more magical than they are. And stopping the mysticism that surrounds software is very much necessary. When I know from hundreds of samples the impact on our system - rehearsing again and again, delivering continuously to production - that user string fixes are often safe, I don't need to go ask some different person to play the role of tester for me. I know I'm biased about my own work, but not everything needs to be treated the same. That's one reason why I love the idea of context-driven.  
  
Find your rules. Learn about the weaknesses of them. Sometimes (more often than not), explore around them. But always, always be aware that in whole team of us developing, time used on one thing is time away from something else. Handoff from one person to another is more work than handoff from the programmer in me to the tester in me. The choices we make are supposed to be intellectual. The best the bright people can make together.  
  
You don't need a different person to test what you did. But someone should test the change. Just like I don't test every change from developers, they don't need to test every change from me. We can ask for help when help is needed.
