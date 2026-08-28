---
title: "Confidence playes a role in testing"
date: 2015-10-30
updated: 2016-08-02
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2015/10/confidence-playes-role-in-testing.html
---

# Confidence playes a role in testing

*Published 2015-10-30, updated 2016-08-02*  
*Source: <https://visible-quality.blogspot.com/2015/10/confidence-playes-role-in-testing.html>*

---

It does not take a lot of confidence to say that a typo fix in code (or resource files amongst all the code) is on the smaller risk side of changes. Doing those changes rarely I tend to move slow and review what changed both when changing and when checking in. I build the system, and check the string in it's use. Sometimes I think that's what I could expect developers to do too, and most of the time they do.  
  
But sometimes, when the change feels small and insignificant, we grow overconfident. There's nothing that could break here, surely? Just a typo fix!  
  
I know I have accidentally cut out the ending quotation mark. I have introduced longer strings that don't fit into the screen. I have fixed a text resource from point of view of one location, where it's used in many places and other has issues. I have wanted to fix a "typo" of missing dots on top of a, to learn that it's not a typo, but scandinavian alphabets can't be used here. Also the typo to me could be not a typo for someone else, like US vs. UK English.   
  
So surely, I am aware that nothing is safe. But I would not agree that I cannot myself do the related checks, have the discussions. And if I would work on a high-risk application (which I don't), I would probably still involve someone else with my analysis. I don't look for a one-size fits all solution, I'm against one.   
  
But in my context, it just makes little sense to have everything checked by another person. It somehow boils down to confidence, which reminded me of an insight a friend shared from Lean Kanban Nordic a while ago:   
> Lack of confidence can be an advantage if it gets you to test more, says [@henrikkniberg](https://twitter.com/henrikkniberg) [#fastfeedback](https://twitter.com/hashtag/fastfeedback?src=hash)
>
> — Karoliina Luoto (@totoroki) [October 20, 2015](https://twitter.com/totoroki/status/656369017633030144)

 I'm not very confident when I go fix typos in code. I spend so little time with code. I know what I'm doing, sort of, but I'm also very aware of things that could go wrong. My lack of confidence makes me double-check. But it does not make me include another person just in principle. Then again, I also know that I don't have to ask anyone to look at the code after my change, the version control alerts the developer on my changes and almost certainly someone is looking for a chance to point out if I could learn something from my mistakes.  
  
The discussion also lead to this question:   

  
> [@maaretp](https://twitter.com/maaretp) would you let your devs test their own code (changes)? If yes, why do they still need you? [@michaelbolton](https://twitter.com/michaelbolton) [@dsynadinos](https://twitter.com/dsynadinos)
>
> — Patrick Prill (@TestPappy) [October 30, 2015](https://twitter.com/TestPappy/status/659997609604612096)

Here's where I am confident. I don't think my existence in (this or any other) team is based on the lack of ability to check their own code. I've seen how brilliantly my team's developers test when I sit with them, silently, without making them do better testing with my advice. My presence, my existence and my aura of higher requirements seem to be enough. It's not (just) about skills, it's about habits and differently developed interest profiles.   
  
I regularly let developers (like it would be letting, they always test their own code, there's 10 of them and just one of me) test their own code. Sometimes, I specifically speak out loud about putting their code into production without me testing it, just to assess the risk and remind about our agreement: my effort is something we add on top of all the testing they've already done, it's exploring for new information. And it's best if we can do that together, so that the information of how you do this sticks around when I'm not around.  
  
They don't *need* me. They benefit from having me.  
  
They get faster feedback on complicated things end users might (or might not) report back to them.  
They avoid building some things that aren't going to be valuable because I get heard when I speak business and end-user languages of needs, concepts and value.  
They get to rely on a close colleague on asking questions or pondering about the choices while implementing as they learn more of what is possible. That colleague is available more often than the end users and business people, and knows the product by learning more about it, hands on and all around the various channels developers don't find as fascinating.     
They get regular positive feedback when they excel in creating good things. I *see* *what they really do* and compliment on actions they are doing. They don't have to be perfect now, but they get recognized when they improve.   
They get encouragement to practice, to get better, to share things with me and with each other.   
They get praise of building great software, knowing they would not have built it as well without the deep feedback I helped them gather.   
  
They don't need me. But they tell me that I'm a catalyst, that makes us all better. That I voice out hard things they wish they would know to say. And that together we're just better. I'm just different. I bring other viewpoints to the table. And I'm confident enough to no longer have to measure my value in bugs in Jira or lines of code changes I check.  
  
Too much or too little confidence are both warning signs. With a bit of ping pong in between and a dose of healthy criticism, there's a great opportunity to learn. Sometimes you succeed, sometimes you fail, but you always learn.
