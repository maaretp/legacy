---
title: "Testing on THEIR production"
date: 2022-07-01
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2022/07/testing-on-their-production.html
---

# Testing on THEIR production

*Published 2022-07-01*  
*Source: <https://visible-quality.blogspot.com/2022/07/testing-on-their-production.html>*

---

Many years ago, a candidate was seeking employment as software tester for a team I was interviewing for. The candidate had done prep work and tested the company's web site looking for functional, performance and security problems. They had caused relevant load (preventing other's from using the site), found functionalities that did not match their expectations and had ideas of possible vulnerabilities. They were, however, completely oblivious to the idea that other organisations production environments are available for \*fair use\* as per \*intended purposes\* and testing is not an intended purpose of production environments. They had caused multiple denial of service attacks to a site that was not built to resist those and considered it a success. We did not. We considered it unethical, borderlining illegal, and did not hire.

For years to come, I have been teaching on every single course that we as testers need to be aware of not only what we test, but where we test too. THEIR production isn't our test environment.

When I discovered a security bug in Foodora that allowed me to get food without paying, I did my very best on not hitting that bug because I did not want to spend time on reporting it. THEIR production was not my test environment. Inability to avoid it lead to some folks in the security community speak poorly of me as I was unwilling to do the work but mentioned (without details) that such a problem existed, after I had done the work I did not want to do on helping them fix it. They considered that since I knew how to test (and was more aware of how the bug could be reproduced), my responsibilities were higher than a user's. I considered requiring free use of my professional skills unfair.

What should be clear though:

> Other organisations' production is not your test environment. That is just not how we should roll in this industry.

When I teach testing, I teach on other people's software deployed to my own test environment. When I test in production, I do so because my own company asks and consents to it. When I test on other people's production, I do that to provide a service they have asked for and consented to.

There are some parallels here to web scraping which isn't illegal. The legal system is still figuring out "good bots" and "bad bots", requiring us to adhere to fair use and explicitly agreed terms of use to protect data ownership.

Building your scrapers and testing web sites are yet a different use case to running scrapers. When building and testing, we have unintentional side effects. When testing in particular, we look for things that are broken and can be made more broken by specific use patterns.

Testing on someone else's production isn't ethically what we should do even if legally it may be grey area. We can and should test on environments that are for that purpose.

Regularly I still come across companies recruiting with a take-home assignment of automating against someone else's production. Asking a newer tester to show their skills by potentially causing denial of service impacts without consent of the company whose site is being tested is not recommended. Would these people have the standing to say no - most likely not.

So today I sent two email. One to a testing contractor company using a big popular web shop as their test target letting them know that they should have permission to make their candidates test on other people's production. Another to the big popular web shop to let them know which company is risking their production for their test recruiting purposes.

The more we know, the more we can avoid unintentional side effects but even then - THEIR production isn't your test environment. Stick to fair use and start your learning / teaching on sites with consent for such pattern.
