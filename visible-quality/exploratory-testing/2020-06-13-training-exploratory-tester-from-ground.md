---
title: "Training an Exploratory Tester from the Ground Up"
date: 2020-06-13
updated: 2020-06-15
theme: exploratory-testing
labels: []
source: https://visible-quality.blogspot.com/2020/06/training-exploratory-tester-from-ground.html
---

# Training an Exploratory Tester from the Ground Up

*Published 2020-06-13, updated 2020-06-15*  
*Source: <https://visible-quality.blogspot.com/2020/06/training-exploratory-tester-from-ground.html>*

---

This summer gives me the perfect possibility - a summer intern with experience of work life outside software and I get to train them into being a proper Exploratory Tester.

Instead of making a plan of how to do things, I do things from a vision, and adapt as I learn about what the product team needs (today) and what comes easy for trainee trusted into my guidance.

Currently my vision is that by end of the summer, the trainee will:

- Know how to work effectively in scope of a single team as tester inside that team
- Understand the core a tester would work from and regularly step away from that core to developer and product owner territory
- Know how to see versatile issues and prioritize what issues make sense to report, as each report creates a response in the team
- Know that best bug reports are code but it's ok to learn skills one by one to get to that level of reporting ability - being available is second best thing
- Understand how change impacts testing and guide testing by actual change in code bases in combination of constraints communicated for that change
- Write test automation for WebUI in Jest + Puppeteer and Robot Framework and take part in team choice of going with one or the other
- Operate APIs for controlling data creation and API-based verifications using Java, Python and JavaScript.
- Understand how their testing and test automation sits in the context of environments it runs in: Jenkins, Docker and the environment the app runs in: Docker, Kubernetes and CI-Staging-Prod for complex set of integrated pieces
- Communicate clearly the status of their testing and advocate for important fixes to support 'zero bugs on product backlog' goal in the team
- Control their own balance of time to learning vs. contributing that matches their personal style to not require task management but leading the testing they do on their own
- Have connections outside the company in the community to solve problems in testing that are hard to figure out internally

We got started this week, are are one week into the experience. So far they have:

- Reported multiple issues they recognized are mostly *usability* and *language.* I jumped on the problems with functionality and reported them, demoing those enforced the idea that they are seeing only particular categories now.
- Navigated command line, filesystem, Git, and IDE in paired setting and shown they pick things up from examples they experience, repeating similar moves a day later from learning the concepts.
- Skipped reporting for a *language* bug and fixed it with PR instead.
- Covered release testing with a provided one-liner checklist for the team's first release.
- Provided observations on their mentors (mine) models of how I train them, leading me to an insight that I both work hard to navigate on higher level (telling what they should get done, and only after digging into exactly how to do it if they already don't know that) and respond questions with questions to reinforce they already know some of the stuff.
- Taken selective courses from Test Automation University on keywords they pick up as I explain, as well as reading tool-specific examples and guidelines.
- Explained to me how they currently model unit - service - UI tests and mixed language set the team has.
- Presented a plan of what they will focus on achieving next week with Jest-Puppeteer 1st case with our application.

After the week, I'm particularly happy to see the idea of self-management and \*you leading your own work but radiating intent\* is catching up. Them recognizing they can't see all types of bugs yet is promising as is their approach to learning.

Every step, I prepare them for the world where I won't be there to guide them but they know how to pull in help when they need it - inside the company and outside.
