---
title: "Optimising start of your exploratory testing"
date: 2022-07-23
theme: exploratory-testing
labels: []
source: https://visible-quality.blogspot.com/2022/07/optimising-start-of-your-exploratory.html
---

# Optimising start of your exploratory testing

*Published 2022-07-23*  
*Source: <https://visible-quality.blogspot.com/2022/07/optimising-start-of-your-exploratory.html>*

---

Whenever I teach people exploratory testing, we start the teaching experience with an application they don't yet know. Let's face it: exploring something you have no knowledge of, and exploring something you have baseline knowledge on are different activities. Unless we take a longer course or the context of the application you work with, we really start with something we don't know.

I have two favourite targets of testing I use now. Both of them are small, and thus learning them and completing the activity of testing them is possible. In addition, I teach with targets that are too large to complete testing on, for the variety they offer.

The first one is a web application that presents input fields and produces outputs on a user interface. The second one is code that gets written as we are exploring the problem we should have an implementation for.

With both test targets, I have had the pleasure of observing tens of testers work with me on the testing problem, and thus would like to mention a few things people stereotypically may do that aren't great choices.

**1. Start with input filtering tests**

Someone somewhere taught a lot of testers that they should be doing *negative testing*. This means that when they see an input field, be it UI or API level, they start with the things they should not be able to input. It is relevant test, but only if you first:

- Know what positive cases with the application look like
- Know that there is an attempt of implementing error handling
- Specifically want to test input filtering after it exists

With the code-oriented activity, we can see that input filtering exists only when we have expressed the intent of having input filtering and error handling. With both activities, we can't properly understand and appreciate what is incorrect input before we know a baseline of what is a correct input.

A lot of testers skip the baseline of how this might work and why would anyone care. Don't.

**2. Only one sunny day**

Like testers were taught about negative tests, they were also taught about sunny day scenarios. In action, it appears many testers hold the false belief that there is one sunny day scenario, when in fact there's many, and a lot of variation in all of them. We have plenty to explore without trying incorrect inputs. We can vary the order of things. We can vary what we type. We can vary times between our actions. We can vary how we observe.

There are plenty of positive variations for our sunny day scenario and we need to start with searching for them. When problems happen in sunny day scenarios, they are more important to address.

Imagining one sunny day leads also to people stopping exploring prematurely, before they have the results the stakeholders asking for testing have the information, the results they'd expect.

**3. Start with complex and long**

To ground exploring to something relevant, many people come up with a scenario that is complex or long, trying to capture all-in-one story of the application. As an anchor for learning it's a great way of exploring, but it becomes two things that aren't that great:

- Scenario we must go through, even if that means blind sighting for what is reality of the application
- Scenario we think we got through no matter what we ended up doing

I find that people are better at tracking small things to see variation than they are tracking large things to see variation. Thus an idea of a scenario is great, but making notes and naming things that are smaller tend to yield better results.

Also, setting up a complex thing that takes long to get through means delay to finding basic information. I've watched again and again people doing something really complex and slow to learn about problems later they could have shown and had fixed early if they did small before large, and quick before slow.

The question with this one is though - does speed of feedback matter? In the sense of having to repeat it all after the fix, it should matter to whoever was testing, and knowing of a problem sooner tends to allow motivation to fix it without forgetting what introduced the problem.  Yet better later than never.

**4. Focus on the thing that isn't yours**

Many people seem to think exploratory testing should not care for team limits but the customers overall experience. Anything and everything that peaks the tester's curiosity is fair game. I've watched people test javascript random function. I've watched people test browser functionalities. I've watched people test the things that aren't theirs so much that they forget to test what is theirs.

This is usually a symptom of not thinking at all in terms of what is yours - architecture wise. When you find something does not work, who will be able to address it? Your team can address how they use 3rd party services and change to a different one. Just because you can test the things that you rely on, does not mean you always should.

I find that if we think in terms of feedback we want to react on and can react on, we can find more sense to information we provide for our teams. Yes, it all needs to work together, but if we are aware of who is providing certain functionalities, we can have conversations of reacting to feedback we otherwise miss.

**5. Overemphasis on usability**

Usability is important and since you are learning a new domain and application while exploring, you probably have ideas on it. Sometimes we push these ideas to the center so early that we don't get to the other kinds of things expected as results.

This usually for me is a symptom of the "even a broken clock is right twice a day" syndrome, where any results of testing are considered good, instead of looking at the purpose of testing as a whole. It feels great to be able to say that I found 10 bugs, and it sometimes makes us forget if those 10 bugs had the ones that exist that people care the most for.

Delaying reporting of some types of bugs and particularly usability bugs is often a good approach. It allows for you, the tester, to consider if with 4 hours of experience you still see the same problems the same way, and why is learning the application changing your feedback.

**6. Explicit requirements only**

Finally, my pet peeve of giving up control of requirements to an external source. Exploratory testing, in fact, is discovering theories of requirements and having conversations on these discovered requirements. Limiting to explicit requirements is a loss of results.

There's a whole category of important problems exploratory testing is able to uncover - bugs of omission. The things that we reasonably should expect to be there and be true, but aren't. While we try to think of these in advance to the best of our abilities, we are at extra creative with the application as our external imagination, letting us think in terms of what we may be missing.

With the code-oriented exploratory testing target, I have two dimensions of things the PO holds true and assumes the others would know, yet the others will come with completely different set of assumptions.

I'll leave this today with the action call for exploratory testing:

> Go find (some of) what the other's have missed!

The recipe is open, but some ingredients make it less likely to do with great results.
