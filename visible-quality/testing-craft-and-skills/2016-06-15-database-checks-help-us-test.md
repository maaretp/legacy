---
title: "Database checks help us test"
date: 2016-06-15
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2016/06/database-checks-help-us-test.html
---

# Database checks help us test

*Published 2016-06-15*  
*Source: <https://visible-quality.blogspot.com/2016/06/database-checks-help-us-test.html>*

---

Reading around what people write on testing and test automation, I get the feeling that there are these two big camps of information. There's a lot of stuff on unit test automation, and there's a lot of stuff about system test automation, in particular things like Selenium. It could just be what catches my eye, but I wanted to dedicate a small piece of writing to my one current favorite of test code we run: database checks.  
  
  
Four years ago, as we were starting our efforts with automation, we focused heavily on unit tests to fail with them in various ways. We could use a lot of time creating them, but with lack of skill we ended up doing tests that lock implementation not behavior, and a maintenance nightmare. In addition, the tests never failed for anything useful. So they vanished.  
  
Two years ago, we then focused on Selenium. The tests found relevant things, and covered ground that developers found somewhat boring to cover. But as the amount of these tests grew, so did the troubles with brittleness. We then identified the subset of tests that would run so that we'd be able to rely on their results.  
  
Less than a year ago, we moved our unit tests from Asserts testing more towards Approval testing. It ended up helping us check complex objects without a lot of maintenance work, and encouraged the team to look for better interfaces to test through.  
  
I don't even remember exactly when the idea of database checks came up. There was just this recurring theme with stuff I'd find that revealed some of our functionalities broke the data. It was painful to test that, because you would only see the brokenness through other functionalities or over a longer time. So we started adding the rules of what the data should be, and made it automatic so that it would alert when I used features that messed up the data, or similarly, when users used features in production that messed up the data.  
  
The tests weren't particularly granular. We could tell who used application in a way that triggered the database checks, but not what they were doing. We could tell the problem happened in last 24 hours, but in production there was always a delay.  
  
Running checks in test environment with what the team was doing was more granular. But even the detective work needed to figure out what needed addressing wasn't impossible - since we knew the work existed with the checks.  
  
Out of all the things we've done for automation, these have helped us the most. The little extensions to what a person has the energy to continuously observe on a database level finds relevant problems.  
  
  
There is just one big challenge: discipline. Keeping up with the idea of considering detective work a priority, to address causes over symptoms. We're still working in untriggered volunteering of this work to share with the team.
