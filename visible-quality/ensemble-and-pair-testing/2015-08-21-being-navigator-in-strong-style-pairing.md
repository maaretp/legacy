---
title: "Being a navigator in Strong-style Pairing"
date: 2015-08-21
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Pairing]
source: https://visible-quality.blogspot.com/2015/08/being-navigator-in-strong-style-pairing.html
---

# Being a navigator in Strong-style Pairing

*Published 2015-08-21, updated 2017-07-22 · Labels: Pairing*  
*Source: <https://visible-quality.blogspot.com/2015/08/being-navigator-in-strong-style-pairing.html>*

---

...this post continues where I left off with [describing the Driver role in Strong-style pairing](http://visible-quality.blogspot.fi/2015/08/being-driver-in-strong-style-pairing.html).  
  
**A step back: who should drive and who should navigate?**  

You have a pair of people. You are different people, with different ideas and experiences. The two of you are stronger together because you build on each other, and also because each of you have unique qualities. Sometimes the qualities are more of a foundational or long-lasting kind, like experience that does not build up over night or transfer in a few days of pairing. Sometimes the qualities are more of temporary, like one having a rough day just today.

One of you will take the role of the Driver - the intelligent input device. One of you will be the Navigator, working out the direction you're about to head to together. Which of the two of you should be which?

The first rule on being the navigator would be that whoever has the idea to get on the computer, should navigate. Remember: for an idea to get on the computer, it must go through someone else's hands in Strong-style pairing. This brings quickly the idea that perhaps the more experienced one should navigate. At least first. At least until it's time to switch. You learn very different things in being a driver and being a navigator.

The dynamic of newcomer and a seasoned professional is interesting. Having the newcomer just drive is already a relevant service for the navigator, freeing you from typing to think on a bit higher level. The information for the newcomer sticks in a completely different way from doing it, hands on the keyboard, than watching what someone else is doing.

Here's a story that stuck with me about powers of pairing with newcomers from Agile 2015. Someone was teaching his daughter to code by having her pair with him with one rule: ask "is there a test for that?". The daughter would sit and ask that every now and then would ask the question at the right time. Looking at what's going on, information catches on and the questions expand. This style is more of the traditional pairing. Having the newcomer type for you gives a whole other level of learning in strong-style pairing.

Whoever had the idea of what to do will navigate. When I started pairing on exploratory testing with a developer, I was the Navigator. When I started pairing on unit tests with a developer, I was the Driver. Over time with both tasks, I will take both roles. And I will grow towards navigating so that the first idea that I have that I could navigate us through, I volunteer to do.

There's three trigger options on change of roles:

- **On time**: you can just change roles on a regular interval. Start with shorter times and grow the time as you grow to work as a pair.
- **On task**: you can change roles when some task is completed. Like a typical ping-pong style pairing, you change so that one creates a unit test and other implements, and both get to do both types of tasks.
- **On idea**: you just change when the driver feels there's a direction he'd like to navigate to. It's like saying "hey, I have an idea, you take the keyboard now".

Regardless of the role you're in, the pair of you should remember to take breaks. Pairing can be very intensive work and outside getting the work done in a pair, you're also responsible for building forward your pairing experience. And that usually works best by inviting for feedback, like taking a small walk around and retrospecting your most recent pairing experience together.

**Navigator: Things to Do**  
  
As navigator, you are in responsible for caring for your driver. If the driver is the intelligent input device, for her to operate properly, you need to care for the conditions of work. Being the navigator, you need to pay attention to your driver, to constantly know where she is going. And you need to enable her to go as fast as possible.  
  
As a navigator, you have three main tasks you're paying attention to:  
  

- **Feed driver the next thing to do**. You're creating the driver the box she works in on as high abstraction level as your driver can handle. We'll talk about abstraction level a little more later.
- **Mine the to-do-list**. Create an idea on where to go next. You might be just one step ahead, but being that one step ahead is important. Where to go to get your thing done?
- **Observe your driver**. See where she is and where she is going, and correct if the direction does not match what you had in mind. Pay attention on how she is doing, and help her whenever she needs it.

Three main tasks might sound simple, but there's a bundle of advice to do them slightly better.

*Programming style matters*

The style of programming matters. Pair programming would seem to work a lot more fluently if the **programming style is consume-first**. With this the idea is that you start with an end result at first and then one by one build the things you wish you had in order to have the end result. Consume-first enables the navigator to go immediately, coming up with things to do while figuring things out herself. And the end result and it's division keep a visible checklist of what there is to do to get to the end result.

Some navigators prefer to work with bottom-up programming style. They build the image of the end result in their head, and feed the smallest possible pieces to the driver, one at a time. In this style, the navigator has a lot more of the information about what we're trying to achieve, leaving the driver to interpret more of why the navigator is having her do things.

The third style is hardest, when there's no ability to work in small pieces. If the navigator has to figure out the whole thing before feeding driver work, most of the time the driver is paused or participating in design discussions over taking the implementation forward. As a navigator, you're supposed to care for your driver, not just having her type for you. Keeping driver waiting while navigator figures things out by herself isn't exactly the optimal way of caring. Working with partial information is essential.

*The abstraction level dilemma*  
  
As the navigator feeding the driver the next thing to do, finding the right abstraction level to communicate with her is relevant, even key to making progress. For driver to go forward, you need to find the right level on which to talk. If you are using an abstraction level too high, you will see puzzled expressions and nothing happening at the keyboard. If you are using an abstraction level too low, you're not harnessing the powers of your driver by keeping her on too short a leash.  
  
I was particularly puzzled with the idea of using highest abstraction level possible, until I realised finding the level is really a listening and observation exercise. If you give instructions and following them is hard, you're probably working on a too high abstraction level. Drilling down can be instant, just be more specific. If you're not noticing the need to change level, you're perhaps risking an experience of failing with tasks that lowers motivation in pairing, so it's good to keep your eyes and ears open. If you start from a very low abstraction level, the driver can always correct you by telling you the level she is comfortable with. But if she has not yet learned how to, she might get a feeling of being talked down. And I found I am particularly sensitive to that, being the only woman and paying attention to being treated differently.  
  
*Mining the to-do-list*  
  
There needs to be an idea of where we're heading. But the road ahead might be only clear for the next few steps, instead of all the way. An important thing for a driver is keeping track of the work ahead. There's three main things to consider on this:  
  

- **Timing**: Find the right time to use an item on the list. What should be done first, what would make a coherent shared story in your pairing. What choices would enable you as the navigator to care for your driver in the best possible way?
- **Backlog**: what is there on the list of things to do? Your backlog is best if it can somehow be part of the code and become a shared view - with consume-first style. But you can also make notes by scribbling on a piece of paper of a whiteboard. Whatever you need to keep track of things. Notes are disposable, code (including test code) is what remains when you're done.
- **Prioritisation**: Deciding what comes next and in what order to do things. It's not just about the right time in long term, but the right thing right now. And it keeps changing as you learn.

  
*Express a in-a-nutshell idea of what you're doing*  
  
As a navigator in strong-style, you are not supposed to have to justify all your chosen actions to your driver. Sometimes the driver has little clue on where you're about to be heading, and a great practice in these cases seems to have been to **invite temporary trust**saying you'd like to just go to this direction for like 10 minutes, and if she is still unsure about doing this, you can change then. The argument of what is right thing to do takes easily more time than that. And nothing stops the pair of you implementing both of your ideas and then deciding that a third, completely different option is what you should go for. With programming in particular, there's a lot of uncertainty that unfolds only through implementation and experimentation.  
  
If you need to express what you're doing, you should learn to express that in a very concise format. Instead of all the rationale, pick only the part of the message that is absolutely relevant to care for your driver.  
  
*Immediate feedback*  

When you navigate, keep an eye on your driver. Double-check with questions what the driver does. And if the driver does something you consider a problem, help her correct it right away. Feedback belongs with the action the feedback relates to.  

*Recognizing time to switch*  
  
Either one in the pair can suggest a switch of roles. But as a navigator, you are usually in a controlling position, so your position gives you a bit of extra responsibility to pay attention to when the driver would have ideas that she should navigate on. You want, in the long term, to build a pair where both can contribute. Switching pairs gives a chance to try out the other role, and only practice helps you get better.  

*Step back and think about what you're doing*  
  
Sometimes you may feel you get bogged down into the details of implementation, and you might want to take a step back and think if you are spending your efforts in the right area. You may not notice without intentional step back to look at the bigger picture, because you're going fast with support of your pair (and usually a nice bunch of unit tests too).  
  
*Retrospectives*  
  
Looking at your collaboration and how the two of you feel about it on regular intervals is also necessary. Not just looking at what you implemented and stepping back on that, but talking about what you learned and what you like and dislike about your collaboration, in a constructive tone.  
  
**Ending this with a word of warning**  
  
I've started to really enjoy looking into the dynamics of this style of pairing. But there's a story I learned, that I also find very specific to this style.  
  
Two programmers were pairing in strong-style and had the time of their life. There was a lot of talk, as all ideas must go verbally for two people to share. Sometimes the discussions were very enthusiastic and to an outsider they might have appeared even heated.  
  
While the pair was enjoying, the environment that did not recognise the different pairing style was betting on which one of the two in the pair would quit first.  
  
Don't care just for your pair, care also for your environment. Verbalising your thoughts makes them available for more people than just the two of you. Take it as an opportunity to build relationships outside your immediate pair.
