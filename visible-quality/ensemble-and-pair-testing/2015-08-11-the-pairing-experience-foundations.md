---
title: "The pairing experience: foundations"
date: 2015-08-11
updated: 2018-12-27
theme: ensemble-and-pair-testing
labels: [Pairing]
source: https://visible-quality.blogspot.com/2015/08/the-pairing-experience-foundations.html
---

# The pairing experience: foundations

*Published 2015-08-11, updated 2018-12-27 · Labels: Pairing*  
*Source: <https://visible-quality.blogspot.com/2015/08/the-pairing-experience-foundations.html>*

---

Back in the days when testing dojos were new, I tried some of them. We would pair up in front of a computer to test, rotate on clock so that everyone around the round table got their share of the computer.  
  
I never particularly liked it. I found that people were really bad at explaining what they were doing and that is the key thing I'd want to learn from - ideas that drive them. The roles of driver and navigator split so that the driver tests and talks out loud, the navigator observes, makes notes and adds stuff felt it was not very engaging. Everyone in the room would have a different idea of what was going on at the computer, deciphering most information from actions as people tend to be bad at talking while testing without significant practice.  
  
As I was teaching testing, I adopted free-form pairing into my courses. I'd have people work in pairs, without assigning them roles and see what comes out. Most often I saw one of the people in the pair be active and the other one trying to contribute something, often quietly watching unless there was a specific discussion on what to do.  
  
Then I learned about **[strong-style pair programming](http://llewellynfalco.blogspot.fi/2014/06/llewellyns-strong-style-pairing.html)**. With strong-style pair programming, the core is that any ideas from one person's head must go through the other person's hands. It relies on the roles of driver and navigator, but changes what each of them is expected to do. Driver is the one who listens and types. Navigator is the one who tells what to do.  
  
In classroom settings, particularly when working in mob (group) format, this style works wonders. You can place the navigator as far as possible from the driver at the keyboard, and everyone can hear what the driver hears. And it guides you to vocalise the core of what we're doing, leaving everyone same experience of navigation as the driver gets.  
  
On way home from Agile 2015,  I collected our ideas about communication in a strong-style pair, in particular as a reaction to many of the issues we see in teaching settings. I've come to realize this isn't programming or testing specific, but it's more about how people work together.  
  
**The Story that Triggers This Post**  

In Agile 2015, I participated a session about unit testing and group learning. The session started with asking for volunteers to join a mob in front of the room, and I was the first to raise my hand as I had promised to model that women could join. Success, we had 50/50 split of genders.  
  
The session was set up with strong-style pairing, with telling driver and navigator their roles. The lady driving first expressed happiness in her role of typist, "I can do that!" and navigator told her what to do word by word, and soon the test was passing. She had just written her first lines of code in her life. With that, the first driver became the second navigator and was soon explaining what the lines of code she was working on would do, just by reading what the English said.  
  
I was third in the queue to become a driver. The third navigator had already been through this before, and he was a programmer, he had already been helping the earlier navigator while he was driving. And when he navigated me, he went to keystrokes telling me what to do. I would have been fine with higher level information, especially since this was not the first time I've seen these Koans.  
  
When I then navigated, I was focused on what level to navigate on, to get the job ("fill in the blanks" as we were doing unit test koans) done fast, as I was feeling slightly annoyed with the idea that I was assumed to need the keystrokes when I was driving.  
  
So the question kept puzzling me: is it better to start your navigation with low-level or high-level? You can say "create a class" or " write 'MyClass VariableName = new MyClass();'". You can say "Copy the text from the file" or go into details of explaining how that happens. And as a woman, I felt particularly sensitive for a level that would be too low. Expressing that idea, I learned I would have been equally uncomfortable with navigation that was too high-level, failing to do what was asked and at worst multiple times in search of the right level.  
  
This and two other posts are about what we learned about Driver-Navigator communication from that trigger.  
  
**Driver-Navigator Pairing in Strong-Style**  
  
For the pair to work well, both parties in the pair need to work well in their roles, and there's specific skills and techniques you can learn to work better from get-go with a new pair in either one of the roles. Techniques, however, are just ideas until you apply them in practice. Only through doing you can learn to pick up the small hints on what would be right thing to do, as you both are equally responsible for your mutual success.  
  
We may think of the driver as an intelligent input device. Intelligence means that while the driver takes orders on what to do and where to go, the driver can also guide to get on the right abstraction level or improvise within the box the navigator gives her.  
  
The navigator is responsible for mining the to-do list and passing the next things to do with instructions on the highest possible abstraction level.  
  
This all builds on trust. The navigator may be just one step ahead of you, and thus unable to give you a clear overview of what you're about to do. The direction the navigator is going to is where the driver goes. When the driver has an idea, the roles can be switched keeping the basic rule in mind: *for an idea to get on the computer, it must go through someone else's hands.*  

Next post up: Things to do as the Driver.
