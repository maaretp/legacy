---
title: "Three routes to fixing problems test cases hide"
date: 2021-02-14
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2021/02/three-routes-to-fixing-problems-test.html
---

# Three routes to fixing problems test cases hide

*Published 2021-02-14*  
*Source: <https://visible-quality.blogspot.com/2021/02/three-routes-to-fixing-problems-test.html>*

---

I'm a big fan of exploratory testing, which often means I have reservations about test cases or at least ideas of how to interpret test cases in a way that does not require such an intensive investment into writing things down, that help us write things down that are needed and how to not think of test cases - or any documentation for that matter - to represent all the testing we are doing.

Today I wanted to share three experiences from my career from three different organizations on how we tweaked our test cases to fix a problem all three organizations shared: using a lot of time for testing, but leaking significant bugs we believed we should be able to find.

**Organization 1: Business Acceptance Testing**

The first example is from an organization where I managed business acceptance testing. I was working with two different projects, moving the business acceptance testing phase from months after months endeavor to something that would fit 30-days. One of my projects had a history of writing detailed test cases, the other had a history of not really using test cases. In getting the timeframe condensed, understanding what we had in mind to do and being able to reprioritize was essential.

For both projects, we used Quality Center (HPs ALM solution was called that back then). Both projects started with test data in mind, and that is what we used as a starting point for our tests. We selected our test data to a set of criteria, wrote the criteria down on the test case title summarizing the business need for that particular data type. And as test steps, we used Quality Center's concept of test templates - a reusable set of steps that described the processes the two teams were running on a high level, same for every single test case.

Thus our test cases were titles, with template test checklists to help us analyze and reprioritize our work. Same looking tests on first week could take a day, and later in the cycle, we could spend 15 minutes. The test case looked same, but we used it different, to explore.

On one of the two projects, they had a history of writing test cases where steps also described the detail, and were concerned that giving those up may mean they forget to cover something as the information of changes isn't easy to pass around for a whole group doing acceptance testing. So we split out weeks into two first where we used the "old style" detailed tests and two latter where we used the new style. We found all problems during the latter two weeks, but in general, the software contractor had done a really great job with regards to their testing and the numbers of bugs we had to deal with were record low.

**Organization 2: Product testing with Reluctant Developers**

The second example is from an organization I joined as their first and only test specialist. With their project manager's leadership, they had figured out writing test cases into word documents, one for each major area of the product. Tracking that the test cases were completed was central to the way they tested amongst the group of developers. Automation, on unit or system level, was not a thing yet for them.

As I joined, the project manager wanted me to start creating test case documents like they had, improving them, and had ideas of how many test cases they would expect me to complete every day.

Sampling one of the existing test specifications, it had 39 pages, 46 test cases, and 3 pieces of relevant information I could not figure out without reading the text based on commonly available knowledge.

I made a deal with the project manager to write down structured notes while I tested, and we got to a place where I was trusted with testing, reluctant developers were trusted to test with me, and the test cases went away. Instead we used checklists of features to remind us what could be checked to design tests in the moment with regards to what the changes to the system were.

**Organization 3: Product testing with certification requirements**

The third example is from an organization with a history of writing test cases that are traced back to requirements. Test cases are stepwise instructions.

The change I introduced was to have two kinds of test cases: [Scenario] and [Feature]. Scenarios are what we use to test with and leave a lot of room for what exactly needs to be verified. Same test could be a week or an hour. For Scenarios, the steps are features as checklist - what features are part of that user journey. When we feel we need a reminder of how-to see a basic, sunny day scenario of a feature to remember what testing starts from, that is where Feature tests come in. The guideline was to write down only what wasn't obvious and keep instructions concise. There can be a feature test, without any steps at all. Steps are optional.

Clearly, the test cases don't describe all the testing that takes place. But they describe seeing that what we promised that would be there, is there, and help us remember and pass on the information of how to see a feature in action.

**The Problems Test Cases Hide**

Test cases can lead people into thinking that when they've done what they designed to do - the test cases - they are done testing. But testing does not work that way. The ways software can fail are versatile and surprising. And we care about results - information and bugs - over the documentation.

Too much openness does not suite most of us. But too much prescription suites us even worse. And if prescription is something we want to invest in, automation is a great way of documenting in a prescribed manner.
