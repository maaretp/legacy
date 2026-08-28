---
title: "Timing is essential!"
date: 2011-03-05
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2011/03/timing-is-essential.html
---

# Timing is essential!

*Published 2011-03-05*  
*Source: <https://visible-quality.blogspot.com/2011/03/timing-is-essential.html>*

---

In recent projects, I've had the pleasure of working with an organized frame for testing. The frame includes very traditional elements: first you design your tests, write them out for experts in the matter to review, to receive comments that as per your documentation they are not sure if what you do is enough and how you could improve. After ignoring most of the comments for various reasons, starts test execution phase, in which you're supposed to report which tests now pass and which fail, and which have you even tried out.   
  
I work within an organization that provides contents to this frame of testing. We have testers, who supposingly could do the testing blind-folded, or with the help of other subject-matter experts. The frame is just for showing if we've done what we were supposed to, and if the schedule can hold up to its promises.   
  
I'm having a small-scale rebellion within the frame.   
  
For a particular area to test, I just did not manage to motivate myself into writing the tests as requested in the planning phase. It was a prioritization decision with too many things to do, to drop out something that would most likely be of little value. For testing in a different way, I have significant organizational support within my organization. The organization guiding the testing work is external, but my good fortune is that the somewhat-of-an-expert-in-test-positioning allows me more flexibility than others.   
  
We skipped the "test planning phase". When "test execution phase" started, I trusted the 3 month timeframe would be enough for what we had thought and discussed on a very high level, checking a sample of production data, some hundreds of items. I assumed the people I work with knew how this particular thing is supposed to work, at least in some scale as they had participated in defining what we'd want.   
  
We started executing tests as the version became available. We run tests on a selected sample of production data, selected against a business-oriented criteria of commonality and essential differences that we'd run into. We had selected a corner to start from, so this was just the first step - we were not sure what other steps would be required, but there was an idea that perhaps about 4 different rounds of attacking the software would be needed. The first round included 61 samples of data - 61 SOAP messages where the input data was the only variable.   
  
Half of the response messages included wrong answers. We digged in deeper in our analysis, and identified 13 separate issues we reported. Same problems would happen in a lot of our samples, at least that was our assumption. Now, about a month later, I know that 5 out of our 13 issues have resulted in a code change to get the result we expected. One is in the queue. Others were due to us setting up some of our data incorrectly - a typical problem in our domain, looking for the stuff in the wrong   
environment. With every step of our testing, we learned together, and adapted what we'd want our next steps to be. This was possible and easy, as we had not yet written the test specification that would fix the contents of our tests.   
  
However, as was expected, the organized frame would make its comeback. I received polite reminders of delivering our test specification, up until the point I felt the "last responsible moment" had arrived. I reviewed examples of what the test spec should be like, and made the decision of not taking the advice from examples, which would have required me to write 61 test cases of the first round we did - documentation that no-one really needs. Instead, I wrote four test cases and no-one can argue those are not test cases. One just happens to handle multiple data samples.   
  
At this point, we know from running the first round, that there's another round just like this one with a tweak of one of the most essential variables in addition to data. And we're safer to assume, knowing our skills and understanding the application better, that four samples of different changes to variables would cover the ground that we need to cover for us to be safe with the most significant risks. Thus, four tests cases.   
  
Yesterday evening, two days after having delivered the test specification for review, I run the second batch of test. There's other people to do some more detailed analyses, but already as I was running them, I looked at all the results in a matrix to spot trends and increase my understanding of what this would take to test as far as we want to go. I realized, that if I had run my tests one-by-one as management wish was for reporting purposes, there would have been problems I could   
not have spotted. They were obvious in a larger sample, but would have not been noted in single samples.   
  
As I assumed, I also received the "how do we put these test into our reporting" -question, with kind request of writing tests as they had thought out for reporting purposes. I suggested two options:   
  
1) four test cases, where one has been started but state is fail until bugs are fixed (which hides our progress, but serves as a rough way of seeing our progress)   
  
2) add categorizing numbers to the test cases after we've run them, as we don't exactly know the contents before we're running them. They'd metrics-wise be the same as others, after the test have been run but not before. We just don't want to do extra work that does not create value, and them being able to follow our progress in detail provides little value if any.   
  
Looking forward to how this turns out, and will write a better experience report later. I need these to change the status quo and allow good people do do good testing in our segment. There should be more consideration on timing when to do what and interleaving test design / execution. To allow my colleagues to work efficiently with better results than before, I need to help in creating a better frame. Time is right for that.
