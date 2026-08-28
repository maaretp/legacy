---
title: "Machine Learning knows it better: I’m a 29-year old man"
date: 2017-10-01
updated: 2018-12-26
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2017/10/machine-learning-knows-it-better-im-29.html
---

# Machine Learning knows it better: I’m a 29-year old man

*Published 2017-10-01, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2017/10/machine-learning-knows-it-better-im-29.html>*

---

Machine Learning (ML) and Artificial Intelligence (AI) are the hit theme in testing conferences now. And there’s no entry criteria on who gets to speak on how awful or great that is for the future of testing, existence of testers and the test automation we are about to create. I’m no different. I have absolutely no credentials other than fascination to speak on it.  
  
The better talks (to me - always the relative rule) are ones where we look into how to decompose testing problems around these systems. If the input to the algorithm making decisions changes over time, the ideas we have on deterministic testing for same inputs just won’t make sense unless we control the input data. And if we do, we are crippling what the system could have learned, and allowing it to provide worse results. So we have a moving target on the system level.
  
  
My fascination to these systems has lead me to play with some available. 
  
  
I spent a few hours on Microsoft Azure cognitive services API for sentiment analysis inspired by a talk. As usual, I had people work with me on the problem of testing, and was fascinated on how different people modeled the problem. I had programmers who pretty much refused to spend time testing without getting a spec of the algorithm they could test against. I had testers who quickly built models of independent and dependent variables in input and output, and dug in deeper to see if their hypotheses would hold, designing a test after another to understand the system. Seeing people work to figure out if the teaching data set is fixed or growing through use was fascinating. And I had testers who couldn’t care less on how it was built but focused on whether it would be useful and valuable given different data. 
  
  
I also invested a moment of my time to learn that I’m a 29-year old man based on my twitter feed. This result was from University of Cambridge Psychometric Centre’s service http://applymagicsauce.com. The result is obviously off, and just a reminder on the idea that “6 million volunteers” isn’t enough to provide an unbiased data set a system like this would learn from. And 45 peer-reviewed scientific articles add only the “how interesting” to the reliability of the results. 
  
My concern on ML/AI isn’t on whether it will replace testers. Just for the arguments sake, I believe it will. Since I started mob testing with groups, my perspective into how well testers actually perform in the large has taken a steep dip, and I base my hope for the testers future usefulness in their interests to learn, not on what they perform today. The “higher function thinking” in testing exists, but is more rare than the official propaganda suggests. And the basic things won’t be that impossible to automate. 
  
My concern on ML/AI is that people suck. With this I mean that people do bad things given the opportunities. And with ML/AI systems, as the data learned over time changes the system, we can corrupt it both in the creation of the original model and in using it while it is learning. We need to fix people first.
  
  
The people with time and skills use their time sometimes on awful problem domains. There must be a great idea other than “we could do this” to create a system that quite reliably guesses people’s sexual orientation from pictures, opening a huge abuse vector. 
  
  
The people who get to feed data into the learning systems take joy in making the systems misbehave, and not in the ways we would think testing does. Given a learning chat bot, people first teach it to swear, spout out racist and sexist slurs and force the creators to shut them down. 
  
Even is the data feeding was openly available for manipulation, these systems tend to multiply our invisible biases. The problems I find fascinating are focused around how we in the tech industry will first learn about the biases (creating systems in diverse groups, hint hint), fix them in ourselves to a reasonable extent and then turn the learnings into systems that are actually useful without significant abuse vectors.  
  
So if there is a reason why the tester role remains is that figuring out these problems requires brain capacity. We could start by figuring out minorities and representation, kindness and consideration without ML/AI. That will make us better equipped for the problems the new systems introduce.
