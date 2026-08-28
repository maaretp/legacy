---
title: "Getting started with mob programming for User Interface Styles"
date: 2015-11-25
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Mobbing]
source: https://visible-quality.blogspot.com/2015/11/getting-started-with-mob-programming.html
---

# Getting started with mob programming for User Interface Styles

*Published 2015-11-25, updated 2017-07-22 · Labels: Mobbing*  
*Source: <https://visible-quality.blogspot.com/2015/11/getting-started-with-mob-programming.html>*

---

While we've had some opportunities to try mob programming with my team, there's now an actual theme over a longer term a subgroup of my team will work on. It turns out that the subgroup consists of people who have not tried this way of working before AND that we need to do all of this in a remote setting. I'm looking forward to learning about how it works for us.  
  
We've selected a theme: styles and the UI. There's a few reasons for this becoming a selection:  

- There's a new user interface designer in our team that has not worked with major projects on styles before. So we know there's a significant skills ramp-up needed, and I don't know of a better way to do that than hands-on with a pair/group.
- The current user interface programmer has not been strong on discipline. When sensing urgency in schedule, it's just easy to take a shortcut. And those shortcuts pile up. The style code looks messy and it's my personal testing nightmare: fix one thing, and many surprising places break. Cleanliness of style code would help us so much, whereas testing of styles in the extent they've been creeping to is just failure demand. So, I will test while bringing my idea of discipline to the group.
- No programmer other than the user interface programmer currently touches the style code. It is too complicated to understand. We want to also transfer back some knowledge of how everyone in the team could work with it and clean it up as they go, and inviting them into the mob seems to be a good starting point for that encouragement.
- I want to try mobbing over long term and get more experiences in being the non-programmer (turning into a programmer) in a mob. And the others don't resist (at least yet), since the learning / sharing / improving the maintainability just makes sense.

Our styles, while they were CSS, used to be as clean as the rest of the code. Then we hired a user interface programmer who brought in LESS, changed all styles alone so that no others were involved and alianated everyone else by accident. It's not hard to see that touching something as wide and complicated, people do follow the instinct to flee (and leave the work for the specialized individual), even if that negatively affects our flow. I'm just glad testing isn't in this position in my team, it could be. *Lesson: work together and share the work not to get there*.   
  
We had a "show-and-tell" session for the style code newbies of the team last week. We looked at our logic of structuring styles and I had two thoughts in my head: 1) now would be a great time to get that test-driven CSS lesson [Llewellyn Falco](http://twitter.com/LlewellynFalco) could do with Agile Finland 2) reading code is separate from writing code - I know when I see a mess, while creating that mess myself would take a more focused learning effort. I made notes of four things to pay attention to:  

- Use variables instead of the magic numbers. We really would want to keep things together better to follow what goes on.
- Simplify the overwriting chain. Minimal design over everything we could do. Less is better. And chaining makes up a mess of unpredictability.
- Scope with views. We have mechanisms to scope the styles, but we mostly keep things global. No wonder I see side effects of changes.
- No Important! -keyword unless absolutely have to. Use of these in chains have escalated in use of these almost everywhere, to make sure the last in chain will end up being applied. Discipline.

Today we had our first scheduled mobbing session. It did not go quite as we'd hope. We started with 2 hours timebox and two goals in mind. We would use the new user interface designer's computer and first goal was that we would set things up that were needed for her to do the work. Second goal was styling of a tiny feature with minimalistic styles that would still fit both designer's ideas of beautiful UI (and the team's idea of maintainability, only valuable stuff added).  
  
We only got work done on the first goal. We got the basics tried quickly, sharing voice over Skype and control of the computer over join.me, rotating on four minutes with the idea that our "expert" would skip his driving turn if we were in middle of something where we'd just be stuck without him navigating. With Visual Studio, we soon learned the computer in question had not been set up for the solution we needed to work on. With a few clicks, that was done. So we went to find the branch with the new feature to be styled and run into our first problem. The branch was not visible on the computer in question. We tried connections, no luck. We installed git bash and gui, thinking we could perhaps bring the branches in from the command line. First time installation gave us git bash that kept crashing every time we'd start it, and after rebooting (no effect) we reinstalled. But looking at things from command line did not take us much further. We pinged in more senior developers, still no clue. So we changed computer.  
  
The starting setup on the second computer was faster, and we got to a point of Visual Studio and starting the application at about 40 minutes into our session. We started feeling the frustration of sharing the remote computer, as the feedback sluggishness of mouse movement made doing simple clicks harder than we're used to. We stopped the running application, synched the branch and went to run the application, only to see it crash at start. With theory of join.me and security settings, we turned off the sharing, no effect. So we decided to reboot the second computer too.  
  
While waiting for reboot (it takes quite a while on Windows...) I asked my local colleague whose computer we tried using first if we could try one more thing - something I had suggested quite early on into the problem, something that should not be connected that was dismissed when I suggested it by the expert. We pulled latest of our integration branch and all of a sudden, the information of existing branches was available too. So by the time of reboot and reconnect, we had a working local environment.  
  
  
Just before our remote expert could rejoin, we tried running the application, with the crash. We tried changing solution configurations between Development and Debug, and got a little further: login screen. But same error at login. The group was getting very amused with the luck we were having, and concluded that at least it was much nicer to be in this together than alone.  
  
We called in yet another senior, to confirm our theory: the new feature relied on database changes that were available only in the developer's personal database. At 1,5 hours, we decided to call this session done and leave the second goal for next session, by which time we'd get the database changes in a common environment too.  
  
A few observations of this session:  

- The first goal turned out to be more complicated than we expected. No one, be it "code newbie", "style expert" or "senior developer / architect" had an immediate answer. Trying and googling were key.
- If we would have tried the unlikely idea when it was presented instead of dismissing it, we would have saved 20 minutes. As a "code newbie", sometimes getting heard can be difficult.
- Getting stuck and unstuck together seemed more efficient. Alone we would have just left it waiting for the "senior developer / architect" to hunt down an answer he did not have when we invited him - research needed. Together, we worked through the first problem and even managed to solve it. Surely, we could have done something else in the meanwhile. Like read the news.
- Minimizing the remoteness so that the one that must be remote is but the rest rotate locally seems a good idea with the connection sluggishness.
- We could improve from  here: the one test that fails the continuous delivery when the application doesn't start would be great for things like this.
- Nothing I would pinpoint to my great tester abilities today. Perhaps next time. Next time is next week Monday. So experiment continues and everyone is still with me.
