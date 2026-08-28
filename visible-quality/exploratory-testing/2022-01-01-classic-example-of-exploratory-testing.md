---
title: "Classic Example of Exploratory Testing"
date: 2022-01-01
theme: exploratory-testing
labels: []
source: https://visible-quality.blogspot.com/2022/01/classic-example-of-exploratory-testing.html
---

# Classic Example of Exploratory Testing

*Published 2022-01-01*  
*Source: <https://visible-quality.blogspot.com/2022/01/classic-example-of-exploratory-testing.html>*

---

As I listened to Lee Hawkins and Simon Tomes conversation calling for "classic example of exploratory testing" and discussing "respecting current norms" when joining projects while still wanting to bring in the "rigorous practice that is deliberate" and "increases product knowledge" and "is valuable beyond added bug reports", I just feel like I need to sort my head my writing about the most recent testing effort I have been thrown at.

A month ago, I started making my transition from one project to another. I'm still figuring out what is the right approach for me as I am joining as a consulting tester with a lot of freedom on choosing what I do (and commanding others on doing things differently). But I have already learned a thing or two:

- There is a release coming up, and a release behind the team a few months ago. The delta between the releases show that testing of the previous release wasn't particularly huge success because the scope is bug fixes that the customer is requesting. And while I believe we will miss some bugs, the full list does not fit my idea of what good results from testing and fixing would look like.
- There is an impressive set of automated tests on unit, integration and UI levels fully administered by the developers. The developers even create a listing in English on what things are in the automation so that a non-programming tester can make sense of it.
- There is a tester in the team and the tester isn't testing. I have little idea what they do but nothing that resembles testing. Developers test. Developers test and automate. Product owner writes specifications and answers all questions. It takes a better than average tester when you have developers who do well on basic testing and I'm concluding that we may not all be motivated for that task.

Bad results. Good automation and appearance of testing. Lost tester.

My first act as a second tester in this team had been to address a communication problem in a style I consider almost a signature move for me. On product owner wanting to reprioritize a fix as "not important", I take up the fixing myself without asking for permission. The whole conversation on "not interesting problem" makes me understand what might have lead to the lost tester I am watching now. The fixing on a completely new codebase takes me a few hours as I find the right place for the simple fix and follow through the pipeline seeing the fix and possible side effects on the final product.

I dig in a little deeper, into documentation and learn there is two generations of test cases.

The first generation of test cases follows the format of "System administrator shall be able to view users", with detailed step by step instructions on  how to go about one way of seeing this is true. There's 66 of these tests, and reading them all through takes me 2 hours. No useful information except for one point: some of these test cases describe features that aren't available yet. Someone scoped out functionality, but tests don't reflect that. There is no evidence of anyone ever running these tests, but if it took me hours to read, it has taken someone weeks to write. I recognize I see 4800 more of these styles of tests required from a sister product with a subcontracting company and know I will have a few more hours of work ahead of me.

I also find a factory acceptance testing procedure that is separate from the development time test cases. Same stuff. No useful information. Another hour of reading through the detailed instructions I could already do deducing from the purpose of the application and user interface.

The second generation of test cases shows the team had made an effort moving away from the stepwise tests. I find 52 test cases, this time in bullet point list in version control, with markings on which of these tests are (A)utomated and (M)anual. An example test from the list reads as "Protected pages redirect to login page". Again zero information value to me, but at least this generation of documentation isn't trying to tell me to set value 2 and then 5, and leave me already frustrated with the idea that 2—>5 is a completely different scenario than 5—>2 and that NOTHING in any of the documentation hints to this crucial information I had already learned by exploring the application.

To describe a starting point for the testing I'm about to do, I describe 13 test cases. I can summarize the reminders of all other documentation to 3 test cases, and add the other 10 on perspectives that I was thinking are relevant with the exploratory testing I have done by now. One of the tests reads as "[Feature] Users, roles and logins" and it is all that I write down knowing I can do a 15 minute and 15 hour version of that based on how I perceive the risks.

I create my usual structures to document my exploratory testing in Jira. Using zephyr and those 13 test cases, I place them into a test plan I title "Pre-release Feature Testing". I know that as I continue exploring, I may change the tests, add more and I know my personal goal for this is to now finally build up the listing of the testing that should be happening, and then do some of it in the schedule available.

I also create another plan I title "RC1 Release Testing", with a single test case: "[Release] Time on Customer Configuration" and decide I will invest 4 hours of my time after we think all other work is done, on exactly what the customer will experience.

I start my exploratory testing work from outlining a test report, writing down first what changes with this release and how that leads to my assessment of risks. I collect metrics of jira tickets and code commits, and analyze changes that might come from outside.

I then choose the areas from my listing that I need to learn in order of risks related to changes. I figure out how to control incoming data, and how to access outgoing data in 3rd party systems. I learn how to access every server, every configuration and every log I can find.

As I test and find problems, I make proposals on \*not fixing\* the problems by comparing them to what I am learning that matters to the user and what is already in the version the customer has vs. what are newly introduced problems. I know we are on a schedule to finish, and knowing quality is more important than getting quality right now.

I see catastrophic symptoms of possible regression the good automation is completely missing out on, but instead of just reporting the problem, I investigate the problem by comparing versions identifying the environmental conditions that are true to me now that make the problem visible in both versions.

I note there is a huge body of requirements and specifications I have not yet read, and note to go back to using that as a checklist of things I may not have considered *after* I first address what the application itself is telling me about possibilities of variables and scenarios.

I drive all my actions to me learning the application, the application domain, the architecture, the interfaces, and information we may be missing about the quality in ways that would be actionable with the team.

This is exploratory testing. It is not ad hoc random time on application seeing if it fails, but it is deliberate, purposeful and investigative. It starts off with light documentation, and it ends with better documentation. And it takes skills to get it done to a good level of results.

And with results I mean:

- knowing more of the problems and limitations in action for the application
- fixing the bugs that matter and deciding on the bugs that don't matter, together
- scoping the project to schedule success
- documentation and test automation that we'll benefit next time around
- tester knowledgable on the problem domain and team context enabling better collaboration

There's as many stories of how things are done and what of the application leads to insights that provide the right results, and we may need to start telling more of them.
