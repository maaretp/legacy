---
title: "Not excited about pull requests"
date: 2017-11-29
updated: 2018-12-26
theme: programming-and-technical
labels: [Agile]
source: https://visible-quality.blogspot.com/2017/11/not-excited-about-pull-requests.html
---

# Not excited about pull requests

*Published 2017-11-29, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2017/11/not-excited-about-pull-requests.html>*

---

There was a new feature that needed to be added. As the company culture goes, Alice volunteered for the job. She read code around the changes to identify the resident local style in the module, knowing how much of an argument there can be over tabs and spaces. She carefully crafted her changes, created unit tests, built the application and saw her additions working well with the product. She had the habit of testing a little more than the company standard required, she cared a lot of what she was building. She even invited the team’s resident tester to look at the feature together with her.

  
All was set except the last step. The Pull Request. It had grown into a bit of a painful thing. Yes, they were always talking about making your change set small to make the review easier, and she felt this was one of the small ones, just as they were targeting. But as soon as her pull request was created, the feedback started.
  
  
If she was lucky, there was just the comments on someone’s preferred style on formatting - over all the codebases they were working on, there still was no commonly agreed style and automatic formatting and linting was only available on some of the projects. But more often than not, every single pull request started a significant thread of discussions of options of how the same thing could be done. 
  
  
Sometimes she would argue for her solution. But most of the time, she would give in, and just change as suggested. Or commanded, she felt. It was either a fight or submission. And the one with the power, reviewing the pull requests, somehow always ended up with their way. 
  
  
After the rewrite to the solution of the people leaving comments, Alice quickly runs unit tests. But that’s it. The version that ends up in production does not get the tester’s eyes before merging, nor the careful testing in the product context Alice put on the first version she created. 
  
  
Another time, her change was just a fix on something that was evidently broken. The pull request rumba started again, with requirements of cleaning up everything that was wrong around the place that had been changed. This time she gave up again - accepting the rejection of the pull request, someone else would get to enjoy the next try of fixing. The “perfect or nothing” attitude won again. 
  
When Alice was free to review Bob’s pull request, she too mimicked the company culture. “This is the way it works”, she thought. She felt that if she said less than others, it would reflect badly on her. So she said as much as she could say. Shared other way of implementing things. And just as Alice would change her code to comments, so would Bob. Knowing the difference of “here’s another way I thought of, for your information” and “I won’t accept without you changing this” had become impossible to differentiate. 
  
  
This story is fictional, and Alice (and Bob) was just the person that got on this fictional project. But the dynamic is very real. It happens to developers with all levels of experience, when the culture around pull requests goes into aiming for perfection instead of good enough. It happens with the culture of delayed feedback with pull requests, with refusal to pair. There’s many ways of implementing the same things, and sometimes arguing about my way / your way AFTER my way was implemented gets overwhelming. 
  
  
Here’s what I’d like to see more:
  

- suggest changes only when that is needed not because you can
- improve the culture created around “acceptance” power dynamic and remove some of the power reviewers hold as guardians of the codebase
- when suggesting extensive changes, go to the person and volunteer to pair.
- volunteer to pair before the work has been done

Writing this reminds me how nice it was to mob on some of the code, when the whole pain and motivation drain related to pull requests was absent.
