---
title: "Seeing what is there, away from the eyes"
date: 2015-09-26
updated: 2016-08-02
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2015/09/seeing-what-is-there-away-from-eyes.html
---

# Seeing what is there, away from the eyes

*Published 2015-09-26, updated 2016-08-02 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2015/09/seeing-what-is-there-away-from-eyes.html>*

---

We made significant changes on how our product handles logins, and I was feeling like it was a whole new feature and approached testing of it that way. You know all the usual stuff of valid and invalid passwords with various contents, looking through allowed character sets and seeing what happens then. And then there's the usual extensions to what you can see, like locking an account after enough trials and scenarios related to that.  
  
As I was testing the login, I got particularly intrigued with the idea of locking / unlocking one's password, and with a little back and forth, I learned that our application counts the failed attempts also while in unlocking mode, and thus one wrong entry gets your password locked after you turn on the locking. Not quite what we meant.  
  
I had a discussion with the developer on this, to learn that this was not new. It was just something neither one of us had felt the urge to test before. I was puzzled on what lead me to it now. Looking into my feelings, it was the risk of being bored. Wanting to see that things could be different than before.  
  
With that idea, I stared at the user interface a while, and let my mind wonder. I realized that when running group testing sessions, people often miss things that are connected, but not visible. And I realized yet another hidden thing I had not paid attention to: audit logs. Kind of obvious thing, something I definitely should be aware of but something that did not remind about its existence visibly.  
  
Software has so much connections that are there, that you need to see even if they were not visible. I'd be really badly off as a tester if I expected to get that kind of information from specs, it's the stuff that I tend to bring to the table thinking about other systems and scenarios in which things can be connected.  
  
I updated my little pictures and checklists, to keep the core insights available for those who come after me. I'm looking forward to someone telling me all the perspectives I'm still missing.
