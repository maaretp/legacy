---
title: "Theories of Error"
date: 2017-02-24
updated: 2017-07-23
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2017/02/theories-of-error.html
---

# Theories of Error

*Published 2017-02-24, updated 2017-07-23 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2017/02/theories-of-error.html>*

---

Some days it bothers me that I feel testers focus more on actions while testing than thinking about the underlying motivations of why  they test the way they do. Since I was thinking about this all of my way to office, I need to write about a few examples.  
  
In a conference few weeks ago, I was following a session where some testing happened on stage, and the presenter had a great connection speaking back and forth with the audience on ideas. The software tested was a basic tasks tool, running on a local machine saving stuff into what ever internal format the thing had. And while discussing ideas with the audience, someone from the audience suggested testing SQL injection types of inputs.  
  
The idea of injection is to enter code through input fields to see if the inputs are cleaned up or if whatever you give goes through as such. SQL in particular would be relevant if there was a database in the application, and is a popular quick attack among testers.  
  
However, this application wasn't built on a database. Doing a particular action wouldn't connect with making sense of testing this way unless there was a bit more of a story around it. As the discussion between the audience member and the presenter remained puzzled, I volunteered an idea of connecting that together with an export functionality, if there was one and assessing the possible error from that perspective. A theory of error was needed for the idea to make sense.  
  
Another example I keep coming back to is automation running a basic test again and again. There has been the habit of running the same basic test on schedule (frequently) because identifying all the triggers of change in a complex environment is a complex task. But again, there should be a theory of error.  
  
I've been volunteered a number of rationale for running automation this way:  

- The basic thing is basic functionality and we just want to see it always stays in action
- If the other things around it wouldn't cause as much false alarms in this test, it would actually be cheap to run it and I wouldn't have to care that it does not really provide information most of the time
- When run enough times, timing-related issues get revealed and with repetition, we get out the 1/10000 crash dump that enables us to fix crashes

I sort of appreciate the last one, as it has an actual theory of error. The first two sound most of the time like sloppy explanations.  
  
So I keep thinking: how often can we articulate why we are testing the way we are? Do we have an underlying theory of error we can share and if we articulated it better, would that change the way we test?
