---
title: "A story on requirement traceability"
date: 2010-09-28
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2010/09/inspired-with-thread-on-software.html
---

# A story on requirement traceability

*Published 2010-09-28*  
*Source: <https://visible-quality.blogspot.com/2010/09/inspired-with-thread-on-software.html>*

---

Inspired with a thread on software-testing list, I shared a story I'll also post here.   
  
Not very long ago, I was working in a project, contractor side, with responsibility on testing the changes with a team of testers. The change was adding a common new feature to a number of applications, built with various technologies.   
As typical in the sector (insurance / pension), we had lots of documentation: requirements / functional specifications / technical specification for each application, going to the detail where there was not much room for interpretation. We also had the Way-Testing-Must-Be-Done, including traceability to detailed test cases. Since someone had thought of requirements being different, they came up with the concept of test requirements, where you'd create yet another level of documentation as part of the specification project that puts all others together in point of view of testing.   
  
The test requirements were created per application. They detailed what should be tested - whatever the specification maker had come up with. As the Way-Testing-Must-Be-Done stated, we carefully linked each test case to requirement, and for a lot of the requirements, there were several test cases. Huge effort.   
  
On the side, we did a little exercise regrouping the requirements on a list that was formatted towards the overall change and risks related to that in particular ways. Just for fun, we traced our tests to this list too. Previously we had 100 % coverage as the Way-Testing-Must-Be-Done required us. From this point of view, the coverage measure was 13 %. We did not add more test cases.   
  
Eventually, we tested. We run out of schedule with less than half of planned tests executed, and had to pass on the software anyway. It was tested by yet another group, with very little problems to note. No complaints in production (they still might not know it's not working...) The unfortunate part was that our group wasn't doing too well results-wise in our testing, we found only a handful of problems.   
  
I've written down some metrics during the project. The size of the overall effort was about 5 man-years, and 16,7 % of it was reserved for testing. We logged 5 bugs. A big part of the testing was talking to people, 75 people listed if you wanted to talk to all that were significantly involved in making it happen.   
  
In my past projects on a completely different sector (software products), this testing would have been considered quite much of a failure. Documentation was expensive, it did not help us in the future, and it did not help us finding problems (there weren't much) and making sure we would have tested before passing it on in the chain.   
  
Lessons I actively took from this:  
- I will not compromise my beliefs in what makes good testing for the Way-Testing-Must-Be-Done without a good discussion again  
- Requiring and managing traceability isn't providing much value this way - we can use the requirements (some of them at least) as session charters instead of creating more useless documentation. I knew it before, now I know how much it took in effort with little value provided.   
- The traceability concept we were using missed an essential part: the level of quality committed developers could produce without support from a traditional testing group in testing of their own and ways of building the software to avoid some of the problems.   
  
In my current projects, I guide contractors from customer side. Traceability is the magical proof that the contractor did what the customer required, and that sending extra invoice on anything unclear is allowed. I'd prefer cheaper ways of doing that, and getting a system to production that serves at least a significant part of the expectations that were included in setting up the project. I don't want full coverage. It's way too expensive. And when the cost is needed, I'd prefer responsible ways of covering risks instead of the requirements.
