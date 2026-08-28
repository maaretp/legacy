---
title: "Four levels of running test automation"
date: 2022-07-14
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2022/07/four-levels-of-running-test-automation.html
---

# Four levels of running test automation

*Published 2022-07-14*  
*Source: <https://visible-quality.blogspot.com/2022/07/four-levels-of-running-test-automation.html>*

---

I work with many teams, and find myself facilitating a growth journey in test automation with regards to how we run it. It is fascinating in the sense that the conversation around coverage remains unchanged when we turn up the speed of feedback. Let's look at this a little more.

**Level 0. Test automation runs on demand**

You have an individual or a subteam implementing test automation for the system at hand, and as they are developing it, they run it. They notice something new is around for testing, they run it. And since their whole work centres around test automation, they run automation many times in a working day.

The feedback of fails comes to the expert creating automation, and majority of the fails is what we consider maintenance - adjusting automation to fit the changed expectations with the product after confirming that this is in the neighbourhood of what we expected.

Sometimes we joke around this saying this is not \*automation\* - there is always, always manual activity for running it. Manual when it fails. Manual when it succeeds. Fast-forwarding some actions in between with automation.

**Level 1. Nightly test automation**

You have a job somewhere that when called, triggers run of automation. Because triggers are complicated for various reasons, you have chosen the simplest trigger possible: time. And since probably your automation is growing from minutes to hours of execution time, it becomes natural that nights are the time when robots are doing some of the testing for you, with regards to whatever batch of changes were introduced during the previous day.

You usually still have an individual or subteam with the purpose of starting their morning on checking all is well after the necessary maintenance, and you may even manage to get to green on most days - at least during the day when the necessary maintenance / corrective action was taken.

When no one changes anything, this is automation. It doesn't fail because there is nothing to note with fails. It runs automatically and succeeds. It baselines your day. Manual when it fails and calls you to explore what changed in the day.

We used to think this is what automation is. But the delay between the change and feedback introduces side effects. We may not understand why it is failing, and the work around figuring things out may grow significantly. And when corrective actions are needed, they are always delayed at least by that one day, causing context switching in the development team.

**Level 2. Test automation on merge to master**

You graduate from time-based trigger to activity-based triggers, and the activity you choose is to test whenever a change is made available for the builds you give - eventually - to customer. This works really well if and when we do continuous small changes to master, and we may even end up turning it to block pipelines on failure so that we never deploy a thing that does not pass all of our tests.

We may not be ready to wait for all the tests, and with failures from each merge, we can pinpoint in time the change that introduced fails, and it may already be helping us with both speed of feedback, granularity of feedback and avoidance of that specialist in team that always keeps an eye on automation when we all can expect our work as developers isn't done without a green pipeline.

However, not all teams do so well on the small changes to master. With pull requests and branches, some teams make significant changes before bringing the changes to master, and end up again with that delayed feedback. Not works than with levels 0 or 1, but still relevant.

**Level 3. Test automation at developer's fingertips**

The state towards we now are aiming for is moving all test automation to a position of being developer's productivity tools. We can't be done without quality in place (for varying degrees of quality), and if there is a subset of relevant feedback, we should have the control of running it and agreements of running it optimised for the developer's use of feedback.

Being able to run test automation on demand in development environment is a part of this. But also, making sure it is run whenever a scope that allows for running it is changed automatically is necessary. We see this usually as per pull request runs of automation, knowing that the coded tests in various scopes pass before we propose to merge.

Over the last two years, I have worked with multiple teams. One level 0 moved to level 1. One level 2 moved to level 3. Most teams on level 1 or level 2, no movement. And one team on level -1 (no automation), moved in last months through 0 to now level 1.
