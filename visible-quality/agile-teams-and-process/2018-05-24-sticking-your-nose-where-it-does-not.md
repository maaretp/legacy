---
title: "Sticking Your Nose Where It Does Not Belong"
date: 2018-05-24
updated: 2018-12-26
theme: agile-teams-and-process
labels: [Agile]
source: https://visible-quality.blogspot.com/2018/05/sticking-your-nose-where-it-does-not.html
---

# Sticking Your Nose Where It Does Not Belong

*Published 2018-05-24, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2018/05/sticking-your-nose-where-it-does-not.html>*

---

There's the things I'm responsible for, and then there's things I choose to insert myself into, without an invite. I have numerous examples, and many experiences on how at some point of my career this became ok and even expected behavior. In the famous words of Grace Hopper paraphrased: Don't ask for permission, apologize if needed. It's been powerful and I can only hope I learned it sooner.  
  
  
Today, I wanted to share a little story of one of those times I was sticking my nose where it does not belong: another team, another team's choices of how to run their "agile process".  
  
It all started from seeing a written piece defining, as testers, what are the tester requirements for a story to be accepted for testing. This whole vocabulary is so strange to me. As a tester, I am not a gatekeeper. I don't define \*my\* requirements. Teams negotiate whatever requirements they may have across roles when they are any good. And I would do a lot of things to avoid building the "development" and "testing" phases, even within a change - including mob programming. But the contents of the list were what ticked me on a trajectory this time.  
  
The contents, paraphrased again, were saying that there must be code review, unit tests, functional tests, parafunctional tests, static analysis, documentation in general and in Jira story tickets in particular. But the idea that this was a requirement for being "ready for QA" seemed so off I did not even know where to start.  
  
So I started simple - with a question.   
> I wanted to ask how you think of this a little more. Some context: here
> we do continuous integration through pull requests, meaning that a
> typical Jira ticket could have anything from 1 - 100 pull requests
> associated with it. We also do releases continuously, meaning that what
> goes out (and needs testing) is a pull request content not a Jira
> ticket. Is there something relevantly different in how you work in this
> case?

Asking this, I learned that \*obviously\* there must be a Jira ticket for every pull request. It was so obvious that I was cringing because it wasn't. So while I think there are a ton of things wrong with that idea from looking at how developer work flows naturally and incrementally when feature toggles are available, I had one thing I felt the urge of saying out of all the things I was thinking.   
> If writing a ticket takes 2 minutes, and reading it by various
> stakeholders takes 10 minutes, I might argue that you could actively
> think of opportunity cost. The time you use on those tickets is time
> away from somewhere. Where is the value on documenting on that level?
> Many teams here have come to the conclusion that it isn't there.

I should have realized to just step out at this point, because I was in for a teaching of how I don't know software development.   
> Maybe it is not obvious, but things like 'developer checklist' could
> help to deliver high quality code.. which means less bugs and less cost.
> If someone would like to discuss about this, let's show him/her "How
> much do bugs cost to fix during each phase" graph.

 And it continued:  

- Writing documentation - in Jira tickets of pull request size - is essential because R&D is not alone but there are other parts of organization AND we get blamed if we don't deliver as ordered.

At this point, I realize there are fundamental differences not worth going into. There is no interest in hearing opposing views. They are optimizing for a customer - contractor relationship while I'm optimizing for working as a single product company. I've lived years of blameless life that enables me to focus on actually delivering value, they are afraid where I am not.    
  
Good thing my manager knows that I can stir up some trouble. I may step out, but I never ever give up. The best way to show this is to focus on how awesome my team is at delivering. Nose back where it belongs, until another dig.
