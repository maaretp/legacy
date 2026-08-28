---
title: "A Regular Expression Drive-By"
date: 2017-03-27
updated: 2017-07-23
theme: test-automation
labels: [Test Automation]
source: https://visible-quality.blogspot.com/2017/03/a-regular-expression-drive-by.html
---

# A Regular Expression Drive-By

*Published 2017-03-27, updated 2017-07-23 · Labels: Test Automation*  
*Source: <https://visible-quality.blogspot.com/2017/03/a-regular-expression-drive-by.html>*

---

I was working in strong-style pair on my team's test automation code last week, to assess candidates to help us as consultants for a short timeframe of ramping up our new product capabilities. The mechanisms of "an idea from your head to the computer must go through someone else's hands" lends itself well for assessing both skills and collaboration. At first, I would navigate on the task I had selected - cleaning up some test automation code. But soon, I would hand the navigation over to my pair and be the hands writing the changes.  
  
There was this one particular line of code that in both sessions caught my eye and was emphasized by the reaction of my pairs: "This should have a code comments on it", "Ehh, what does this do, I have no idea!". It was a regular expression verifying if a message should be parsed to passed or failed but the selection of what the sought for keyword was was by no means obvious.  
  
I mentioned this out loud a few days later, just to seek for confirmation that instead of the proposed code comment, it should really just be captured in a convenience method that would have a helpful name. But as we talked on the specific example, we also realized that it would make sense to add a unit test on that regular expression to explain the logic just a bit more.  
  
The unit test would start failing if for any reason the messages we used to decide on pass/fail would no longer be available, and would be more granular way of identifying where the problem was than reading the logs of the system test.  
  
A regular expression drive-by made me realize we should unit test our system tests more.
