---
title: "Run the code samples in docs"
date: 2017-10-12
updated: 2018-12-26
theme: programming-and-technical
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2017/10/run-code-samples-in-docs.html
---

# Run the code samples in docs

*Published 2017-10-12, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2017/10/run-code-samples-in-docs.html>*

---

I was preparing for a session on exploratory testing in a conference, wanting to make a point of how testing an API is just like testing a text field. Even the IDE you use just gives you keyword recognition based on just a few letters, and whatever values you pass in are a guided activity. The thinking around those fields is what matters. And as I was preparing, I went to my favorite test API and was delighted to notice that since the public testing sessions pain, there was now some basic getting started documentation with examples.  
  
I copypasted an example around approving arrays into the IDE, and things did not go as I would have expected. Compiler was giving me errors, and I could extend my energy barely to see what the error message was about. There were simple errors:  

- a line of code was missing semicolon
- a variable a was introduced, yet when it was used it got renamed to x

As a proper tester, I was more happy than sad with the lack of quality in the documentation, and caused a bit of pain to the poor developer asking not to fix in for a few hours so that I could have other testers also see how easy finding problems in a system is because documentation is part of your system. I think the example worked nicely around encouraging anyone to explore an API with its documentation.  
  
The cause of the problem I saw was that the code sample was never really executed. And over time even if it was executed once, it could break with changes as it wasn't always executed with the code.  
  
A lot of times, we think of (unit) tests as executable documentation. They stay true to functionality if we keep on making them pass as we change the software. Tests work well to document drivers. But for documenting frameworks, you need examples of how it calls you. It makes sense to do the examples so that you can run them - whether they are tests or other form of documentation.  
  
Documentation is part of your API. Most of us like to start with an example. And most of us choose something else if possible if your documentation isn't helpful. Keep it running.
