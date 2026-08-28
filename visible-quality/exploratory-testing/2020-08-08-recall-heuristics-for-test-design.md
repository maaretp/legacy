---
title: "Recall Heuristics for Test Design"
date: 2020-08-08
theme: exploratory-testing
labels: []
source: https://visible-quality.blogspot.com/2020/08/recall-heuristics-for-test-design.html
---

# Recall Heuristics for Test Design

*Published 2020-08-08*  
*Source: <https://visible-quality.blogspot.com/2020/08/recall-heuristics-for-test-design.html>*

---

Good exploratory testing balances our choices what to do *now* so that whenever we are out of time, we've done the best job testing we could in the time we were given, and are capable of having a conversation about our ideas of risks we have not assessed. To balance choices, we need to know there are choices and recently I have observed that the amount of choices some testers make is limited. A lot of what we call test design nowadays is recalling information to make informed selections. Just like they say:

    If the only tool you know is a hammer, everything starts to look like a nail. 

We could add an exploratory testing disillusionment corollary: 

    It's not just that everything starts to look like a nail, we are only capable of noticing nails. 

The most common nail of testers that I see is the error handling cases of any functionality. This balances the idea that most common nail programmers see is the sunny day scenario of any functionality, and with the two roles working together, we already have a little better coverage over functionality in general.

To avoid the one ingredient recipe, we need awareness of all kinds of ingredients. We need to know a wide selection of options for how to document our testing from writing instructional test cases, to making freeform notes to making structural notes on individual level to making structural notes on group level to documenting tests as automation as we are doing it.  We need to know a selection of coverage perspectives. We need to know that while we are creating programs in code, they are made for people and a wide variety of people and societal disciplines from social sciences to economics to legal apply. We need to know relevant ways things have failed before, being well versed in both generally available bug folklore as well as local bug folklore, and to consider both not failing the same way, but also not allowing our past failures to limit our future potential and drive testing by risk, not fear.

This all comes down to the moment you sit in a team meeting, and you do backlog refinement over the new functionality your team is about to work on. What are the tasks you ensure the list includes so that testing gets done?

In that moment, what I find useful being put on the spot is *recall heuristics*. Something that helps me remember and explain my thoughts in a team setting. **We can't make a decision in the moment, without knowing our options**.

I find I use three different levels of recall heuristics to explore what I need to recall my options in a moment. Each level explores at a different level of abstraction:

- **change**: starting from a baseline where the code worked, a lot of times what I get to test is on a level of code commit to trunk (or about to head to trunk).
- **story**: starting from a supposingly vertical slice of a feature, a user story. In my experience though people are really bad at story-based development in teams, and this abstraction is available rarely even if it is often presented as the go-to level for agile teams.
- **feature**: starting from value collection in the hands of customers where we all can buy into the idea of enabling new functionality.

For a story level recall heuristic, I really like what [Anne-Marie Charrett has offered in her post here](https://mavericktester.com/2019/12/31/heuristics-sfdipot/). Simultaneously, I am in a position of not seeing much of *story-based development* but backlogs around me tend to be on value items (features and capabilities) and the story format not considered essential.

**Recall on level of change**

The trigger for this level of recall is a chance in code. Not a Jira ticket, but seeing lines of code change with a comment that describes the programmer intent for the change.

Sometimes this happens in a situation of pairing, on the programmer's computer, the two of you working together on a change.

Sometimes this happens on a pull request, someone having made a change and asking for approval to merge it to trunk.

Sometimes this happens on seeing a pull request merged and thus available in the test environment.

This moment of recall happens many times a day, and you thinking quickly on your feet under unknown change is a difference in fast feedback and delayed feedback.

How I recall here:

- (I) **intent**: What is supposed to be different?
- (S) **scope**: How much code changed? Focused or dispersed?
- (F) **fingerprint**: Whose change, what track record?
- (O) **on it**: How do I see it work?
- (A) **around it**: How do I see other potentially connected things still work?

**Recall on level of feature**

The trigger for this level of recall is need of test planning on a scale of feature to facilitate programmers carrying their share of testing but also to make space for testing.

Sometimes this happens in a backlog refinement meeting, the whole team brainstorming how we would test a feature.

Sometimes this happens in a pair, coming up with ideas of what we'd want to see tested.

Sometimes this happens alone, thinking through the work that needs doing for a new feature when the work list is formed by process implying "testing" happens on every story ticket and epic ticket level without agreeing what it specifically would mean.

- (L) **Learning**: Where can we get more information about this: documents, domain understanding, customer contacts.
- (A) **Architecture**: What building it means for us, what changes and what new comes in, what stays.
- (F) **Functionality**: What does it do and where's the value? How do we see value in monitoring?
- (P) **Parafunctional**: Not just that it works, but how: usability, accessibility, security, reliability, performance...
- (D) **Data**: What information gets saved temporarily, retained, and where. How do we create what we need in terms of data?
- (E) **Environment**: What does it rely on? How we get to see it in growing pieces, and where?
- (S) **Stakeholders**: People we hold space for. Not just users/customers but also our support, our documentation, our business management.
- (L) **Lifecycle**: Features connect to processes, in time. Not just once but many times.
- (I) **Integrations**: Other folks things we rely on.

Recalling helps make choices as we are aware of our choices. It helps call in help in making those choices.
