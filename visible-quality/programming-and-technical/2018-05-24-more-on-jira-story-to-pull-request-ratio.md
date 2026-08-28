---
title: "More on Jira story to pull request ratio"
date: 2018-05-24
updated: 2018-12-26
theme: programming-and-technical
labels: [Agile]
source: https://visible-quality.blogspot.com/2018/05/more-on-jira-story-to-pull-request-ratio.html
---

# More on Jira story to pull request ratio

*Published 2018-05-24, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2018/05/more-on-jira-story-to-pull-request-ratio.html>*

---

Today, just as I was blogging away my previous post, one of my team members send me a quick message: "Would you accept my pull request?"  
  
I don't get many of those. There's so many of us working on the shared 'internal open source codebase' that mostly other people get there before me. I've been given rights just as everyone else even if I don't use them exactly as everyone else.  
  
So I follow the link to the pull request, check the repo name and wonder a little, and check the diff to realize it is a one line change. For a small moment, I stop to appreciate how nice the tooling is, showing me exactly what is changing. I appreciated the description giving me context of why the one line was changing. So I pressed the Approve-button.  
  
A minute later, I get a second ping. "Can you merge the pull request? My rights don't seem to be high enough.". I go back, see that my rights are high enough, stop to think about the ridiculousness that someone has again introduced different rights and assigned them this way, and click on the Merge-button.  
  
A minute later, I get a third ping. "I checked downstream things, all worked out well".  
  
Between each minute, I was testing already the exactly same thing the change would have impact on. After all, we were working together, on the same thing, as a team.  
  
This was so painless. So easy. And then I thought about what another team wanted to require of our processes.  
  
For each pull request, there must be a matching Jira ticket "for documentation purposes", because "support needs to read it". The change we just introduced was part of a bigger things we were building, and the bigger thing would require changes to at least 10 different repositories - meaning 10 different pull requests. And the pull request had already all the relevant info. A one-liner of it would end up in the detailed release notes in case someone wasn't into hunting down the info across repositories.  
  
I sighed and thought about stupidity of processes, and decided to write this down.  
  
Don't come telling me that this is needed for a bigger company. This is particularly detrimental for a bigger company. Know more options.  
  
There's a great way of learning about options: listening. There are so many awesome people who speak about this stuff. Pay attention. I try to.
