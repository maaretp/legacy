---
title: "Time to update threat modeling"
date: 2017-09-30
updated: 2018-12-26
theme: agile-teams-and-process
labels: [Agile]
source: https://visible-quality.blogspot.com/2017/09/time-to-update-threat-modeling.html
---

# Time to update threat modeling

*Published 2017-09-30, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2017/09/time-to-update-threat-modeling.html>*

---

Working in a security company, there is an activity we try to routinely do, at least when *anyone* hints on not having done it. That activity is security threat modeling. Getting smart people together, supported by a heuristic (STRIDE) we explore what could possibly go wrong on security with the design we’ve made by now. Purpose of threat modeling is to learn and change when we learn. And for someone trying to drive forward better quality, there’s not a more powerful argument than connecting a bug somehow to security.

  
Heuristics are used to keep the discussion both focused and multifaceted. People easily would focus on one type of problems, and heuristics like STRIDE help with thinking from a few more perspectives. It’s far from complete, but it has been the basic approach for good enough to get started with. The acronym opens up to words Spoofing, Tampering, Repudiation, Information disclosure, Denial of service and Elevation of privilege. 
  
  
Security is about not letting people do bad stuff with systems, hopefully while allowing the right people to do what they were trying to achieve with the use of the system. All of the perspectives easily map to the idea of the users and attackers. 
  
  
But with many modern systems, there is one often dismissed theme I would bundle with security, while I realize that for me as a tester it has long been a separate concern. That is one of **abuse**. I’m exploring extending STRIDE with an A. 
  
  
Abuse vectors are often unique. They are ideas of how we could unintentionally open up ways for targeting misbehaviors against a group with use of the systems. And thinking of the abuse threats is getting increasingly important.
  
  
Let’s explore a few ideas around this.
  
  
A prominent tech woman ended up with targeted abuse with Github. At a time when Github allowed people to be added to projects without their consent someone thought it was a fun thing to add her to projects she would by no means associate with. All those projects then end up being a part of her profile. We would want to make sure our features don’t enable high visibility cyber bullying. 
  
  
A group of people built a learning bot, which turned into a monster in a matter of hours. We would want to make sure that with the learning systems, we can control the quality of the data the system learns from.
  
  
A face recognition software was built, and it did not recognize faces of people of color. The sample set the system was built on did not do a good job at being representative, and the biases of the creators got coded into the functionality. We would want to make sure we don’t make a group of people invisible with systems intended for wide use. 
  
  
A phone had a feature of facial recognition for logging in. It worked perfectly for images of the owner’s face. We would want to make sure that if we use faces as credentials, gaining access to our personal data is not one picture away. 
  
  
Abuse as an attack vector is connected with STRIDE, but different. And we need to start actively thinking of it as we create more sophisticated systems that include our assumptions of privilege and biases.
