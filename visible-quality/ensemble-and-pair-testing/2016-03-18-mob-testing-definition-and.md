---
title: "Mob Testing: Definition and Clarifications"
date: 2016-03-18
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Mobbing]
source: https://visible-quality.blogspot.com/2016/03/mob-testing-definition-and.html
---

# Mob Testing: Definition and Clarifications

*Published 2016-03-18, updated 2017-07-22 · Labels: Mobbing*  
*Source: <https://visible-quality.blogspot.com/2016/03/mob-testing-definition-and.html>*

---

I did a webinar on Mob Testing as Ministry of Testing Masterclass this week, which will later be available in [the Dojo](https://dojo.ministryoftesting.com/) if you missed it. My slides are available on [Slideshare](http://www.slideshare.net/maaretp/mob-testing). There were some post-session questions I thought I'd take a moment to respond on in a blog.   
  
**What is this?**  
  
Mob Testing, as I see it, is Mob Programming (Mobbing) applied to any activity we consider testing. I personally love both Mob *Exploratory* Testing and Mob Testing to *create automation artifacts*. And best of all is intertwining testing with programming so that activities become hard to separate, which would then just really be mob programming (with an embedded testing perspective).   
  
So we take any testing activity, put the whole team together to work on that and rotate roles every 4 minutes - that's the start. The group finds a way to test it, building on what is going on, working as one mind on one task. No deciphering of what goes on in the computer, as the things that driver do must come from the navigators in the mob: no thinking at the keyboard.   
  
**Q&A**  
  
Someone working in an Agile project (between the lines definition of agile is Scrum) asks more.  
    
*1.
When does Mob-Testing takes place in project/feature life-cycle? Is it
during the sprint along with User-Story Testing or post-sprint during as
a regression/bug-hunt activity?*  
  
These when-questions are tricky. Let me elaborate.  
  
For a very agile project using mob programming, the whole question of timing would be irrelevant. When the team members come to work in the morning, they start mobbing. They do that throughout the day until they leave. No code gets checked it without the team being there to work on it. Testing is getting intertwined with development. And releases of changes happen typically throughout the day. But this is not the agile you speak of.   
  
Agile I live with does not in-sprint and post-sprint activities. All activities happen in flow, I don't even have sprints. Each feature for me goes to production when it's ready and tested. And that happens daily. But the concepts in the question give me an idea of an organization that splits done to in-sprint and post-sprint activities, as there's work that leaks out of the sprints (and best way to fix that is to get rid of sprints and move to kanban and continuous delivery, but that's another topic of my earlier webinar available on Dojo on Continuous Delivery without Test Automation).    
  
I'd say almost anyone considering mob testing (over mob programming) isn't at a point where we'd mob full days. Then Mob Testing is a learning activity, during which we also contribute. So timing becomes a question of when appropriate activities take place. I personally find a few timings particularly great:  

- Mob Testing (exploring) after feature is "done" to find out what is the real use experience and how the changes sit together with the rest of the product. This is typically for the purpose of learning about a feature / change in the context of the system. Creates a great experience of what a tester would see looking at something that is "done" in the eyes of a developer.
- Mob Testing (exploring) when we're assessing the new feature in the context of it getting implemented. Knowing the state before (and finding problems in the state before) tends to result in shared understanding of what we're building and overall better quality through fixing around while at the change.
- Mob Testing (automating) when there's anything you can automate. It could be shared unit test creation, it could be shared BDD implementation of tests, it could be adding some Selenium.

You have in-sprint and post-sprint testing, and both have different focuses as activity. You can mob on either types of activities. This of it this way: which activity would benefit from having all brilliant minds collaborating around the task the most? Where are special skills of individuals that others would benefit from being exposed to? Where do we most need the fun and motivation that working together on a problem gives us? (boring and challenging are both good answers).   
  
*2.
Is there are multiple Scrum Teams and Testers are assigned to specific
specific team, How does knowledge sharing takes place before getting
together for such activity? Or is it some kind of activity where only
people with prior knowledge will speak and others will attend just to
gain knowledge?*  

I've worked with software I have no prior knowledge on, and as a tester I learn in layers. I don't need all knowledge to be useful. For testing something you don't know, you learn while you test. And you are always free to ask people in the mob (other than the driver) to help out with their knowledge. Typically if there's only one expert available, I tend to not have that expert be the driver at all, but take turns in navigating as designated navigator and mob navigator. I would also ask the expert to only navigate when others get stuck or off the path in a relevant way.   
  
I've noticed that doing something (trying) I don't know creates a focus on knowing more. Passive following creates less of it.  
  
Think of it this way. When I was mob programming with my team for the first time on refactoring, I had no idea of what we'd do. The whole IDE was strange. They would tell me, when I was driving, keystrokes on the first round. But I learned immediately. And when it was my turn to be the designated navigator, the rules of the game were clear. If I see something long, we'll look at breaking that. If I see a bad name, we'll rename. I was not alone, even if I was responsible in a particular role for my 4 minutes.   
  
I tend to choose activities to mob on so that it does the leveling of knowledge. If something is very advanced, I would do that after I've done other mobbing activities leading up to it.    
  
*3. Who all are contributors in the activity, only Testers / Tester+PO / Tester+Dev / Tester+PO+Dev / etc.?*  
  
For mob programming, we're talking of whole team activity. Every skillset present. Non-programmers turn slowly into more of a programmers. And programmers create a lot more empathy for business and real users, when these sit together with us in the team. And the fast answers make a lot of difference in what comes out.   
  
For mob testing, you really need to think of who would you like to share the experience of testing with. It could be just testers like on most of the training courses I deliver. It could be an equal mix of testers and developers, like on the training course I deliver with Llewellyn Falco. It could be one tester amongst a whole team of developers like at my day job. It could be testers and product owners, when focusing  on better business understanding for tests. Any mix of these.   
  
If your group gets bigger, you might want to consider rather having two separate sessions.   
  
*4. What should be the frequency of Mob-testing activity, per-sprint / per-PSI / per-Release / etc.?*  
  
I think I might have answered this in the previous question. It could be that all work - including all testing work - gets done in the mob. Or it could be any amount of time you choose to use on mobbing.   
  
2 hours a week is a great way to exercise mob programming with my team. But we do more than mob testing. All activities are included. The week in between lets people "grow muscle" from the exercise we did, and manages the worries people have in thinking individual contribution will get them to the end goal faster.
