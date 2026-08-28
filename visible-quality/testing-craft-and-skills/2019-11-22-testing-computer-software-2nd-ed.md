---
title: "Testing Computer Software, 2nd ed"
date: 2019-11-22
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2019/11/testing-computer-software-2nd-ed.html
---

# Testing Computer Software, 2nd ed

*Published 2019-11-22*  
*Source: <https://visible-quality.blogspot.com/2019/11/testing-computer-software-2nd-ed.html>*

---

I'm collecting some of the history of Exploratory Testing and for that, going into selected references that brought the idea to me. The first book I read on testing (I'm a newbie, only 22 years in the industry :D ) was  
> Cem Kaner et al. Testing Computer Software, 2nd ed. published: 1999

For research purposes, I have had my hands on the 1st edition too, which is from 1988 but it's been a while.  
  
For the second edition, I go for index and look for exploratory testing.  
  
exploratory testing  
   - generally 6, 7-11, 215  
   - boundary conditions 7-11  
   - discover the program's limits 215, 241  
  
Page 6 is a chapter "The first cycle of testing" and Step 4: Do some testing "on the fly". Here the book speaks on running out of formally planned test cases. It emphasizes that regardless, you can keep testing. It encourages to think of new things without spending much time preparing or explaining the tests. It encourages trusting instincts and trying anything that feels promising.  
  
It introduced the example in question as something where you switched from formal to informal very early on as the program crashed. And then it introduces the concept:  
> "Rather than gambling away the planning time, try some exploratory tests - what ever comes in mind."

It then pulls a core concept out:  
> "Always write down what you do and what happens when you run exploratory tests."

It moves to give examples about how surprising problems you did not anticipate for when planning your formal test series are now useless on figuring out what the problems with software are.  
  
Page 7-11 goes into Step 5: Summarize what you know about the program and its problems. It introduces with a table "Further exploratory tests". It then discusses a possible way of implementing as a reason for problems testing is finding with explaining ascii character codes and linking boundaries to them. Finally, it describes a second cycle of testing after fixes and reminds there will be multiple cycles and that you want to select tests for each cycle based on what the programmer said she changed. The book emphasizes that it is not a mere act of selecting but you need to come up with new tests too.  
  
Of total of 16 pages on the first sequence of testing, the book discusses exploratory tests for 5 pages at a time the rest of the world was still speaking only of scripted tests.  
  
Page 215 talks about Initial development of test materials. It talks of parallel work on testing  and the test plan saying "you never let one get far ahead of the other". It moves to talk about the first prompts you should consider: testing against documentation, starting to create a function list and analyzing limits. It never mentions exploratory testing, but describes how a plan is created as per "our approach" which reads as exploratory.  
  
Page 241 is on components of test planning documents and specifically three kinds of matrices: environment matrix, input combination matrix and error message and keyboard matrix. For input combination matrix, it elaborates:  
> "Our approach is more experiential. We learn a lot about input combinations as we test. We learn about natural combinations of these variables, and about variables that seem totally independent. We also go to the programmers with the list of variables and ask which ones are supposed to be totally independent."

The book was a collaboration between Cem Kaner, Jack Falk and Hung Quoc Nguyen and as such it does not outline if exploratory testing was coined by one or all of them but it being published under their names says the was some level of agreement to allow such concept in the book.  
  
While these are the specific parts marked for "Exploratory testing", the way I read it, the whole book is a description of exploratory testing as it was known then - the smart way of testing with care but attention to costs and nature of testing in product companies that lived or died with wasteful practices.
