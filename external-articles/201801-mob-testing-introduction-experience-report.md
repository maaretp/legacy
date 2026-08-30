---
title: "Mob Testing - an Introduction and Experience Report"
publication: "Ministry of Testing, The Testing Planet"
date: 2018-01
url: https://dojo.ministryoftesting.com/lessons/mob-testing-an-introduction-experience-report
source_retrieved: https://dojo.ministryoftesting.com/lessons/mob-testing-an-introduction-experience-report
kind: article
language: en
---

# Mob Testing - an Introduction and Experience Report

*Ministry of Testing, The Testing Planet — 2018-01*

Source: <https://dojo.ministryoftesting.com/lessons/mob-testing-an-introduction-experience-report>

> Retrieval note: page text as published.

---
# Mob Testing: An Introduction & Experience Report

Read the latest article from The Testing Planet "Mob Testing: An Introduction & Experience Report" by Maaret Pyhäjärvi

- Copy link
By Maaret Pyhäjärvi

Mob Testin g is about the whole team working on testing on one computer, getting the best of everyone from the work they are doing. This is my story of how I grew to favor Mob Testing and Mob Programming and how you could try it too.

At end of a talk on Exploratory Testing, one of the attendees asked a question:

> ‘With so many years in the industry, how is it you have never learned to program?’

‘With so many years in the industry, how is it you have never learned to program?’

I remember my canned answer well:

> “It has never fascinated me.”

“It has never fascinated me.”

Yet, I’ve spent a few decades actively learning the craft of testing, only to recognize I’ve not even scratched the surface. I had no intention of becoming a programmer. Not for lack of aptitude, but for lack of interest and time. The world is full of more fascinating challenges, and is full of programmers who don’t see enough of the world around programming.

Three years ago I was introduced to Mob Programming; a way of programming on one computer, with the whole team, together. At the time, I was convinced it was time away from things I loved, mostly testing. I told myself I did it only for the purpose of improving teamwork, for both programmer-programmer relations and programmer-tester relations. Little did I know that something no one could convince me of, learning to program and becoming a programmer, would be a reality a year later. Nor could I foresee that a simple mechanism like this could turn programmers into better testers, and improve any testers capabilities. It’s a mechanism I now refer to as Mob Testing.

## The Group Working On The Same Thing

Mobbing (Mob Programming or Mob Testing) starts with the idea of a group of people using a single computer, forcing a true single-piece flow. Each member of the group sits in front of that computer, when it’s their turn, rotating on a timer every few minutes, continuing to work on the same task until completed. Instead of using a round-robin mechanism to taking turns of who works while others watch, mobbing makes everyone work together through strong-style navigation .

This means that whoever is on the keyboard (the driver) is not allowed to decide what happens on the keyboard. The instructions come from the group (the navigators), who guide on the highest possible level of abstraction. The idea is not to get most out of each individual but to get the best idea into the work the team is doing, to avoid having to go back and revisit it, by having everyone’s ideas available in a timely manner.

## Level Of Abstraction, What Is That?

To effectively speak while navigating, it is helpful to think of three levels of abstraction for navigation: Intent , Location , and Details .

- Intent : is the first step, when we explain what we want.
- Location : is used next if intent alone was not enough to make the action happen exactly as we intended, e.g. “use the search with a keyboard shortcut instead of menu”.
- Details : are used as low-level explanations of what to do if we still fail to get movement in the intended direction, e.g. “Type control + F”.

### Examples Of Three Levels Of Abstraction

The group, all together, has the intent of performing a task, for instance, to test the search functionality. Imagine you’re sitting in front of the keyboard, and you’re told to start the application so that the group can test the search functionality. If you’re an application expert, you’re probably fine starting the application without much more detail. This is an example of what is meant by “Intent.” If this is enough, you don’t need to dig deeper into the levels of abstraction.

Starting with the keyboard shortcut instead of the menu bar for search functionality is an example of location; where to start, what to begin with. This is an example of the second level of abstraction, “Location.” The navigator is in control, and makes sure the work gets done the way they intended, giving relevant additional information to the driver to get the work done.

If you’ve never used the application and navigators in the group have, they can guide with as much detail as necessary. This is what is meant by the third level of abstraction, “Details.”

The purpose of the levels are to keep control of the work with the navigators, while sufficiently supporting the driver in front of the keyboard. When speaking with words of intent creates movement towards what the navigators wanted, the lower levels of abstraction are not necessary.

## Use Words: No Touching The Keyboard!

Technologists have a lot of experience translating our ideas to actions through our own hands on the keyboard. Strong-style navigation removes the physical connection, giving us the focus of words.

As a mobbing session begins, it is hard to find the words to say. Someone might not know what to call the thing next to line numbers in our IDE (gutter). We seek words to clearly state what we want to be done. Similarly, some are not used to listening patiently and attempting to follow someone else’s intent. While mobbing allows the driver to speak back and suggest better ways, the power of deciding what to do next is on the navigators.

If the driver starts working on their own, this creates a gap of understanding for different people in the group. It turns the navigators into reviewers attempting to interpret the actions taken by the driver. Keeping everyone connected, and having a mindshare on the task is important. Similarly, the frequent rotation of roles, usually every four minutes enforces the mindshare nature.

To make the beginning easier, the group usually assigns a special practice role for one of the navigators, making them the designated navigator. Like all roles, this rotates and everyone gets their turn being the collective voice of the group directing the driver.

## Bias To Action

The group usually starts with a clear task. For programming activities, a simple refactoring of code is a great thing to do in a mob. Any of the programming Katas or practice exercises can also work. Testing activities could include an automation script or a focused charter for exploratory testing. Whatever we chose, the first challenge is usually communication.

### Two Rules Of Mob Communication

What if the group disagrees on how to do something? What if everyone has a different idea about how to do a particular task?

Two rules usually come in handy for this:

- Yes, and… -rule : The group is working in a mindshare. When something is started, it is finished, but we can add to it.
Yes, and… -rule : The group is working in a mindshare. When something is started, it is finished, but we can add to it.

- Do Both -rule : If given two ways of doing something, list them, and then do both. Start with the one you find less likely, or just random. The goal is to give everyone a voice which is acknowledged.
Do Both -rule : If given two ways of doing something, list them, and then do both. Start with the one you find less likely, or just random. The goal is to give everyone a voice which is acknowledged.

Both of these rules create a bias for action. Go forward. Do. It’s because, as the team does, the work unfolds in ways they did not see before. Well-planned action has not yet started. Deliver the first valuable increment, and make it small enough so that failure is an option, and a welcome learning opportunity.

## Retrospect To Learn

Regardless of how you feel during or after a mobbing session, the mobbing session should end with a retrospective. A typical mob session for beginners is about one to two hours. Leave an additional half an hour for a retrospective. Talk amongst the group about what observations people had on the way the group worked, on the different things the group worked on and what each of the participants of the mob learned. Try not to project your perceptions onto others, but make sure everyone’s experiences are heard. Learn from them, then use them to adjust for future mobbing sessions.

## Getting The Best Out Of Everyone In The Work We Do

The mechanism of mobbing is interesting. In order to get people’s ideas at the right time when they are best consumed, it can feel like there is downtime for some individuals while others are contributing or navigating/driving. Instead of thinking of non-vocal members as not contributing, or taking downtime, we should really think of it as a learning time. An individual should stay as long as they are either learning or contributing.

### Simple Guideline And The Right Size Of A Mobbing Group

The right size of a group where everyone learns or contributes varies. Two are a pair, anything beyond that can be a mob. Like with orchestras, the right sized group depends on what you’re playing.

A necessary guideline to keep in mind is one of kindness, consideration and respect . All members of the mobbing group should be able to hear everyone’s contributions. All members of the mobbing group should be able to contribute. All members of a mobbing group should have their contribution respected, regardless of whether it’s valuable at the time it was suggested.

## My First Experiences Mobbing

My first few times mobbing consisted of various programming activities with my team. Having heard of the mechanism from Woody Zuill at a conference, I wanted a first-hand experience. I was convinced I would not be able to test with my focus only on the code during a mobbing session. I was worried I would slow others down. Even with those worries, I organized the sessions for the purpose of improving the quality of the team’s work.

The first time I sat in the driver seat it was painful. I was told, keystroke by keystroke, what to do with an IDE I had barely ever used. We worked on refactoring our own code, pulling out methods and renaming them. The rotation time was every four minutes and I was relieved when my time at the driver’s seat was over. I realized it would take over 20 minutes before I was again in the driver spot. I used that time to organize my experience and to pay attention to what others were experiencing. The programmers were just as challenged as I was, and I was picking up stuff fast. The second time in the driver’s seat was really nice, and over time it became a place of only moderate discomfort, and then even enjoyment.

The group continued to work as a mob on various types of programming tasks. We refactored. We changed GUI components. We added unit tests. We worked on Selenium test scripts. We started new, major features. Outside of work, I organized community meetups to work on TDD, and legacy code refactoring, and unit testing, in mob format to take my experiences further.

### Cognitive Dissonance Experience

I found myself a valuable addition in a mob. A year later, after many mobbing experiences, I realized something had changed. I no longer spoke about programming as something I did not like, or did not do. I did not set out to be a programmer, quite the opposite. I found that when my beliefs and actions were out of synch long enough, my beliefs had changed. This is often referred to as cognitive dissonance , and it turns out to be a great way of changing a person’s beliefs. Instead of trying to rationalize something you already understand, give them experiences that may transform them and inform their own understanding of an issue, problem, or belief.

### Extending Into Mob Testing

As mob programming turned out to be a great way to learn, I found myself curious about how it would work on testing activities. My chances of convincing my whole team of programmers to regularly explore with me were limited. I enhanced my work experiences with community experiences. I did sessions in Open Space conferences where anyone could set up sessions, and realized the power of sharing our thoughts while doing it. As a senior hands-on tester, I found people were often missing some good habits, ideas, or tools, and learned to inject it into the work with

> “let me navigate for a while.”

“let me navigate for a while.”

#### Learning As A Facilitator

I learned to speak in questions as a facilitator, encouraging the group to bring the best of them into the work we were doing. Personally, I learned tons from other testers that would approach a problem differently, use different tools, or insist on different priorities for doing things. These learnings, which were insightful and crucial to me, were sometimes considered a “common sense” approach by the person who taught it. It was not something they would have thought to teach to a new colleague.

#### Stealth Mob Testing

The more the team tested in a mob format, the more I realized that someone with a strong tester background brought unique perspectives and behaviors into a mob programming group. A tester in a mob, doing stealth mob testing, could clarify the requirements just in time, find problems when there was no ego at play, guide the group into testing with different environments, suggest data and scenarios while building, then ensured it was documented as automated tests. Even the slowness I worried about turned out to be a strength, making the team more deliberate and considerate in their communication and identifying better solutions. Instead of building technical debt, we found ourselves building and using technical assets which we could reuse and extend.

I knew something beautiful had happened when developers started looking at me saying:

> “You’d want me to click here. You’d want me to try a different browser. You’d want me to use some other data in my testing.”

“You’d want me to click here. You’d want me to try a different browser. You’d want me to use some other data in my testing.”

I could quietly let them do great testing that they knew how to perform. It wasn’t only me who gained new skills and became a programmer, they also became testers.

Programming is like writing. Getting started is easy, but it takes a lifetime to get good at it. Testing is the same. Learning with others in a mob format is both a powerful learning experience and a great way of working with results which reflect the best of everyone.

## Getting Started With Mob Testing

You could try mobbing as a group activity at your work or meetup. With complex tasks, a group of smart people get the job done. With simple tasks, the group innovates for efficiency. Choose any task, and get a group together.

Take with you two guiding principles:

- Kindness, consideration and respect - this is how you work closely with others.
- Get the best out of everyone from the work - hear everyone’s voices actively.
Consider the core dynamics:

- Working on one computer
- Frequent rotation
- Strong-style navigation
- Navigating on highest level of abstraction (Intent)
- No decisions while in front of the keyboard (Driving)
- Retrospect after a session
Use two rules while working:

- Yes, and…
- Do both
(Optional) Use a facilitator to support the experience:

- Assign a designated navigator to practice
- Speak in questions to clarify intent
- Track dynamics
- Step in to navigate to set an example
All you need is a group of people sharing a computer; all looking at one screen working on a shared task. The possibilities of serendipitous learning are endless.

## References

Woody Zuill: Mob Programming - a Whole Team Approach

Llewellyn’s Strong Style Pairing

## Author Bio

Maaret Pyhäjärvi is feedback fairy with a day job at F-Secure, where they call her a Lead Quality Engineer. She identifies as an empirical technologist, tester and programmer, catalyst for improvement, author and speaker, and community facilitator and conference organizer. Her day job is working with a software product development team as a hands-on testing specialist with a focus on exploratory testing. She was awarded as Most Influential Agile Testing Professional Person 2016. She blogs regularly and is the author of two LeanPub books.

- Copy link
