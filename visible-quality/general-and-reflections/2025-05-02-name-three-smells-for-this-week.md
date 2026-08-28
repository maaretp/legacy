---
title: "Name Three Smells for This Week"
date: 2025-05-02
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2025/05/name-three-smells-for-this-week.html
---

# Name Three Smells for This Week

*Published 2025-05-02*  
*Source: <https://visible-quality.blogspot.com/2025/05/name-three-smells-for-this-week.html>*

---

The world of testing is not ready and done. We are testing, sure, yet there is so much work on doing better we would need. I wanted to share the three stories that blow my mind this week. Remember, while I see a lot of projects that my company works with, I also see a lot of projects my company does not work with but community at large works with.

These are my smells of the week.

**1. Manual automated testing**

Testers have been automating testing for some years, and have some hundreds of test cases automated. Sounds great. But something feels a little off - for quite some time now, no new tests have been added; effort of testing stays on a high level as the reason quoted is *maintenance.*

With a discussion, we dig in a little deeper. Tests are not reliably green, which then means they are run with an isolated pipeline step that is executed manually.

Asking another, there isn't even a pipeline. The automated tests are executed manually on a testers computer, on demand.

*Necessary cleanup: quarantine for unreliable as route to move your tests to actual pipelines that run on change.*

**2. Leaky regression testing**

A new release went to production, a month of regression testing was done before it, and yet, 20+ problems reported within days post-production. Maybe a month is not sufficient?

With a discussion, we dig in a little deeper. We learn that *regression testing* in this case means that we don't look at the changes that were done, but we protect basic business scenarios by repeating the same tests we did every time. The trouble is, changes are different every time, and they tend to not break on the basic business scenarios but on where ever the changes were made. Yet we insist on more blind regression testing over opening our eyes to try and follow the changes.

*Necessary cleanup: stop pretending regression tests without change-based analysis are the solution. Implement everything as code, follow the changes and you are likely to do better.*

**3. Test case obsession**

A new senior tester joins a product team with a history of high automation and success with continuous integration and deployment. The tester concludes that not having a *manual tests repository* is a problem, and works to transform, *manually,*automated tests to test cases because they have always seen test cases in Jira Xray or equivalent as core of what good testing is to them.

*Necessary cleanup: understand that code is documentation too. Be careful with the kind of experiences you recruit for.*
