---
title: "Exploratory Testing an API"
date: 2016-03-07
updated: 2016-08-02
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2016/03/exploratory-testing-api.html
---

# Exploratory Testing an API

*Published 2016-03-07, updated 2016-08-02 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2016/03/exploratory-testing-api.html>*

---

This week Thursday, I'm running a workshop at Booster Conference on Exploratory Testing an API. I decided to go for ApprovalTests as the test target because it's something I've been meaning to learn, and what is a better way to learn than to test. Also, having the creator close by seemed like it could be an advantage.  
  
Before my prep of me testing it, I knew there was extensive unit tests. ApprovalTests are tested with ApprovalTests, and a lot of them. So my main interest is not on the stuff that is already being tested, but on stuff that tends to slip through the cracks when unit testing.  
  
With a bit of personal brainstorming, I came up with three approaches to focus on.  
  

1. Usability and Consistency of the API and functionalities
2. Environment
3. Inputs and outputs

It's been quite a ride for preparations.

First I noted cosmetic bugs - typos in the interface. Within 5 minutes, those were gone, fixed. I may still be snarky on the backwards compatibility for the poor users who rely on the mistyped but these were in the interfaces that are not intended for external users, regardless of being visible.

Then I pointed out a specific difficulty for the users of the API. ApprovalTests uses the concept of Reporters, that get introduced with something of this format:

```
    [UseReporter(typeof(DiffReporter))]
```

And there's a lot of reporters! But they are all over the IDE-provided list, as they have no means of grouping them together. And honestly, the idea of a user going to check what is available in reporters in the open source project just seems a little more than most users I can imagine will do. Although I'm first to admit that I might be even more on the lazy side on this stuff.

End result: change request to rename all reporters to start with Report. And while at it, clarifying the names otherwise too. Some of the reporters have the purpose of running silently with the builds, while others pop up the best tools for analysis.

I built up a nice list of purposes that the Approvals and Reporters serve, that will make a great foundation for further exploration with my workshop participant. And mapping those out through learning about the consistency (and inconsistency) might be helpful as documentation also later on, so I'll share that later.

I concluded my prep with a research on inputs and outputs in the unit tests. The innocent request of "please run them" revealed that they had not been run with the last change and had tests breaking. Software & tests got fixed - and I got my confirmation that my hunch on environments being still troublesome is worth going for with line breaks in the files. We sampled different types of tests, and found groups of tests that had been accidentally excluded from the solution. Added some of them back too.

I'm going to have so much fun with the people at the workshop revealing problems with this. The best of all of it: I don't need to waste my time on trivialities of simple bugs, because there's been a significant effort into the unit tests. They are pretty impressive, but showing those isn't what this is about: it's about learning things you don't learn with the unit tester glasses: flaws of your design logic, inconsiderations of your environment and things that just slipped through the programmer's eyes.
