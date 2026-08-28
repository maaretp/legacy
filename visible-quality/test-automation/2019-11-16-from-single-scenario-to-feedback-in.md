---
title: "From Single Scenario to Feedback in Test Automation"
date: 2019-11-16
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2019/11/from-single-scenario-to-feedback-in.html
---

# From Single Scenario to Feedback in Test Automation

*Published 2019-11-16*  
*Source: <https://visible-quality.blogspot.com/2019/11/from-single-scenario-to-feedback-in.html>*

---

Understanding your system and environment is core to designing a strategy of how you balance unattended testing with test automation to attended testing. ¨  
  
Imagine you just build a new feature that really sums up to a single scenario: your user can say "Do a scan on Wednesdays at 10.21 every second week of the month".  
  
To test that basic positive scenario as attended testing, you kick up a Windows machine you will test on. It just happens to be a out-of-the-box-clean US 64-bit Windows 10 with the latest OS patches all in it. You confirm that indeed there is a scan on Wednesday (as it happened to be today) at 10.21 and that it looks like it is supposed to happen again in a month. Having chosen a realistic scenario, one that a user would definitely be likely to set up, you leave the machine waiting and make a note to test again in one month, and verify there were no surprise runs in the meanwhile.  
  
If you know something about exploratory testing, you would probably look at the basic positive scenario as a starting point, and explore a lot more around it:  
  

- Explore Day, Time and Cadence
- Explore type of task, is "Scan" always the same thing, realizing it scans *something* that could be entirely different
- Explore plausible (and less plausible) error scenarios around wrong values, missing values, mixed up values, unintended use
- Explore other things that could happen on the computer simultaneously and could have an impact

It all works. Are you done?

You are not. It works on your machine. Your machine that is just one kind of machine there could be.

And it worked today. With the version you had now. It will change.

This is the thinking that drives us to do test automation, or TA as we seem to lovingly call it.

For every scenario, it gets run on:

- Versions of Windows for Workstations and  Windows for Servers
- 64bit and 32bit - same code, different executables that only can be tested with right bitness.
- Mixes of patch level and "computer cleanliness"

Sometimes, it gets run on more. There's a nice list of [Windows OS versions](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions) that matters in what we are testing.

No human can attend to all that.

For our 550 scenarios, we ended up with 178745 tests run on one day that was busiest last week. A very small percentage of them fail but the failures are usually crash dumps related to timing that are super hard to reveal by human repetition or information on changes an their side effects.

This takes us from 'works on my machines' to ' works on some thousands of our machines'. Yet it does not mean that things work in production in full.

The basic scenario gets tested on "my machine" as I implement the automation. The exploration that must happen to script a scenario qualifies as testing.

The other dimension to attended exploratory testing are relevant. But so is the tooling to enable unattended exploratory testing, one that covers new environments. The tooling that aids us calls us when we need to attend to it.

Yesterday, it was 0.9% of our tests that called us to attend to it. And knowing these dimensions we work, I was very happy with seeing the new telemetry give us the list of priorities of what would make most impact if we attended to it.

And at the same time, I was still doing very traditional exploratory testing to find problems that automation was not the best fit for.
