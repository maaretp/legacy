---
title: "A New Experiential Exploratory Testing Exercise on focusing feedback to own application"
date: 2021-05-28
theme: exploratory-testing
labels: []
source: https://visible-quality.blogspot.com/2021/05/a-new-experiential-exploratory-testing.html
---

# A New Experiential Exploratory Testing Exercise on focusing feedback to own application

*Published 2021-05-28*  
*Source: <https://visible-quality.blogspot.com/2021/05/a-new-experiential-exploratory-testing.html>*

---

Over the years of first me learning testing and then me teaching testing to strengthen what I have learned, I have come to appreciate an experiential style of learning. Instead of me lecturing how testing is like detective work where we are supposed to find all the information others around us are missing about quality, I prefer us doing testing to learn this.

For this purpose, I have created many starting points for us experiencing testing together. I find that the selection of the application we will test will guide the lessons we are able to pull out. Every single application has something in common, but also forced thinking that is different in some relevant way. Today I wanted to talk about one of these experiential exercises, to give you an example of a favorite. 

  

Then again, what makes a favorite? Some of the exercises I have been adding most recently get my attention. This week I added an exercise on targeting our testing on our application when there’s our part and a 3rd party API. 

  

I tested solo on Saturday. I paired with Irja Straus from Croatia on Monday. And I paired with Hamid Riad from Sweden on Wednesday. And as always with new targets, while I had a rough idea of what I would want to teach, hands-on exploratory testing taught me things that surprised me. 

  

When I tested solo, I set up the application. Like with most open source applications, the setup wasn’t straightforward, and before I could run it on my machine with a good conscience, I had to update many javascript dependencies to get to a comfortable state without critical security warnings. Similarly, I set up the mocks I needed for the exercise, and solved issues around CORS. CORS is a browser security function that is supposed to protect us a bit from bad implementations, apparently introduced since the application had been created. 

  

From what I thought would be a solo exploratory testing session, I soon discovered it would become a session to update documentation, fix dependencies and the project in general to get to running it. I finished my tests by playing barely enough to know the API had some intelligence and was not just a REST frontend to a database. Interesting 3rd party API promises good for my exercise on focus for the exploratory tester \*away\* from the interesting API, into our application. 

  

When I paired with Irja, we got to the focus on our application very easily. From a simple demo, we got to using the mocks to test and really left the API alone for most of the session except for some comparison results and a deep focus into the promises of functionality the API specification had to offer. We learned about value dependencies, what worked and what didn’t. We ended up reading code to know what ‘works as implemented’ means for this application - including calling the API with a typo that reimplements logic that API would encapsulate in the application. Starting from not knowing anything about the application, I learned about the data we would need to take control over as we explored the API forcing our front-end to show us functionality that matched data. We would find domain concepts that weren’t implemented, problems with what was implemented and report our discoveries. 

  

When I paired with Hamid, we first fell into the lure of the interesting API, playing with values from the user interface and testing the 3rd party API more than our own application. Even though I first thought that was not what I wanted out of this exploratory testing exercise, I soon learned it was exactly what I wanted. Each of us in the pair building on the ideas of the other, we learned about how the API deals with mistaken inputs and what input validation our application should have. The time we spent on the 3rd party API paid back when then turning our focus on our application. While the previous session gave me the experience on the API specification and set my expectations on that, this session found interesting but different problems. We also fixed some bugs while at it. 

  

I’m planning to test the exercise as I now envision it at Socrates UK Digital open space conference next week. This time I would run it as an ensemble testing exercise, and see where the group goes with the constraint and facilitation, and like in the end of every experiential session, pull out the lessons the group can share. 

  

I have other exercises that teach other things. I used two full training days facilitating people through various exercises this week as I was teaching my exploratory testing work course. I’m a big fan of experiential learning, and that in general we learn testing by doing testing. We can inspire and motivate, make sense and clarify models with the material around the exercises. Yet, discovering your lessons - my intended core lessons and some surprises - is immensely valuable. 

  

It’s the kind of teaching I want to figure out how to scale. I can scale talks of theory and experiences. But I am yet to find out how to scale experiential teaching of the lessons I have created.
