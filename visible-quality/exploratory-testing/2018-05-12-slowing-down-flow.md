---
title: "Slowing Down the Flow"
date: 2018-05-12
updated: 2018-12-26
theme: exploratory-testing
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2018/05/slowing-down-flow.html
---

# Slowing Down the Flow

*Published 2018-05-12, updated 2018-12-26 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2018/05/slowing-down-flow.html>*

---

This week Craft Conference saw a second edition of my talk "How Would You Test a Text Field?". Regardless of the boringness of the title, I find that this is the type of talk we should have more.

> "How would you test a text field" by [@maaretp](https://twitter.com/maaretp?ref_src=twsrc%5Etfw) was a great display of methodology and added some pretty useful stuff to my development toolbox. Thank you very much! [#Craftconf](https://twitter.com/hashtag/Craftconf?src=hash&ref_src=twsrc%5Etfw)
>
> — Vincent Fahrenholz (@DrearyTown) [May 11, 2018](https://twitter.com/DrearyTown/status/994950711552233478?ref_src=twsrc%5Etfw)

The talk was recorded on video and will be available later in its recorded format.  
  
What I find interesting though is the stuff going through my mind post talk, thinking through all the things I want to do differently.  
  
The talk had five sections to it.   
  

1. Introducing a common model of assessing testers in job interviews: "How would you test a text field?" and one way of judging the responses
2. Testing a text field without functionality
3. Testing a text field in product context through UI & filesystem
4. Testing a text field in code context through API with automation
5. Testing a text field that is more than a text field

As I will not be going to conferences in the upcoming year, I don't have a place to fine-tune the talk to its next generation. Sounds like a great opportunity for doing videos I've been thinking about for a long time!

The things I want to do differently are:

1. When testing a text field without functionality, get people to generate test ideas to the same functionality with GUI present or API present - focus on what functionality is in which layer
2. Visualize test ideas from the group better - use a mindmup. Map them to the four level model of how a tester thinks.
3. Teach the model of testing better: I intentionally create first "phases" of idea collection, idea prioritization, and learning from results before selecting or generating a new idea for the next test in the first exercise. Later exercises I allow for prioritized ideas to action, but force discussion on what the test made us learn. When I test, it all mingles.
4. Force the focus in code context better to just the text field, blur the frame needed to run things out.

I've been teaching the model of testing before with a story of my sister coming back from her first driving lesson many many years ago. She asked our brother to show her the ropes in our own car, as she felt that after her first real drive she was finally ready to pay attention to all those details. On her first driving lesson, the teacher had made her drive around the parking lot a few times and then surprised her by guiding her right amongst traffic. Her experience reminded me of mine: not being able to remember a single thing.

When we are learning to drive a car (or to test in an exploratory fashion), we first need to learn all the individual bits and pieces. In the car, we need to remember the shift, the gear, gas and break, the wheel and all the looking around while maneuvering things we have no routine on. New drivers often forget one of the things. Stopping into a traffic light you see them accidentally trying to go with a gear too high and shutting down their car. As they are slowing and turning the wheel to make a turn, changing the gear at the same time feels difficult. So they make just enough room for themselves to practice. Same applies with testing.

The actions we need to make space for are different for testing. We need to make room for coming up with a test idea and prioritizing the right test idea out of all the ideas we have in our head. We need to make room for properly executing a test that matches that idea. We need to make make room paying attention to the result against both spec and any other ideas of oracles we could use. And we need to make room to reflect and learn about how what we just saw the application do changes our next idea.

Just like when driving a car, the driver controls the pace. Slowing individual activities down is something the driver can and should do. Later, with routine we can combine things. But when we start, we need to pay attention to every individual action.
