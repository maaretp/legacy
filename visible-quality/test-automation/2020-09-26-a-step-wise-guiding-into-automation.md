---
title: "A Step-Wise Guiding into Automation"
date: 2020-09-26
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2020/09/a-step-wise-guiding-into-automation.html
---

# A Step-Wise Guiding into Automation

*Published 2020-09-26*  
*Source: <https://visible-quality.blogspot.com/2020/09/a-step-wise-guiding-into-automation.html>*

---

Looking at a group of testers struggle with automation, I listened to their concerns:

    - Automating was slow. When automating, it would easily take the whole week   
      to get one thing automated.

    - Finding stuff to automate from manual test cases was hard. It was usually a step,   
      not the whole thing that could be automated.

    - It was easy to forget earlier ideas. Writing them down in Jira was encouraged, but   
      Jira was where information goes to die. If it didn't die on its way like often happened.

I'm sure all their concerns and experiences were true and valid. The way the system of work had been set up did not really give them a good perspective of what was done and not, and things were hard.

In my mind, I knew what was expected of the testing they should do. Looking at the testing they had done, it was all good, but not all that was needed. Continuing exactly as before would not introduce a change we needed. So I introduced an experiment.

We would, through the shared test automation codebase, automate all the tests we thought we could document. No separate manual test cases. Only automated. We would split out efforts so that we could see coverage though the codebase adding first versions of all tests that were quick to add and then add actual automation into them a test at a time. Or even, a step of a test at a time if it made sense.

We would refactor our tests so that mapping to manual tests to automated tests was not an issue, as all tests were targeted to become automation.

None of the people in the team had ever heard of an idea that you'd create tests that had only name and a line of log but agreed to play along. Robot Framework, the tool they were already using, made this particularly straightforward.

Since I can't share actual work examples, I will give you the starter I just wrote to illustrate the idea on documenting like this while exploring, using prime from eviltester as a test target.

```
```
*** Settings ***  
Documentation       Who knowns what, just starting to explore  
...                             https://eviltester.github.io/TestingApp/apps/eprimer/eprimer.html  
  
*** Test Cases ***  
Example test having NOTHING to do with what we are testing but it runs!  
    [Tags]      skeleton  
    Log         Yep, 1/1 pass!
```
```

This is already an executable test. All it does is that it logs. The name and log message can convey information on the design. Using a tag shows numbers of these in the reports and logs.

Notice that while the Documentation part of this identifies my test target, there is actually nothing automated against it. It is a form of test case documentation, but this time it is in code, moving to more code, and keeping people together on the system we are implementing to test the system we have.

As I added the first set of skeleton tests and shared them with my team, they already were surprised. The examples showed them what they were responsible for, which was different from their current understanding. And I designed my placeholders already in a way that can be automated. I had placeholders for keywords that I recognized while designing, and I had placeholders for test cases.

Finally, at work, I introduced a four level categorization of "system tests" in automation:

Level 1 is team functionality on real hardware.

Level 2 is combining level 1 features

Level 3 is combining level 1 for user relevant flows

Level 4 is seeing the system of systems around our thing.

The work on this continues at work, and the concreteness of this enables me to introduce abilities to test the team may have assumed they can't have. Also, it enables them to correct me, a complete newbie to their problem domain on any of the misunderstandings I have on what and how we could test.

The experiment is still new, but I am also trying it out with the way I teach exploratory testing. One of the sessions I have been creating recently is on using test automation as documentation and reach. With people who  have never written any automated tests, I imagined browser tests in Robot Framework might do. They do, but then it takes the time from testing to tool learning. Now I will try if the first step of creating skeletons enables a new group to stick with exploration first, and only jump into a detail of automating after.

.
