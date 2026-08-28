---
title: "As a tester, I can represent a user"
date: 2015-02-19
updated: 2016-08-02
theme: public-speaking-and-conferences
labels: []
source: https://visible-quality.blogspot.com/2015/02/as-tester-i-can-represent-user.html
---

# As a tester, I can represent a user

*Published 2015-02-19, updated 2016-08-02*  
*Source: <https://visible-quality.blogspot.com/2015/02/as-tester-i-can-represent-user.html>*

---

I'm writing my second post today based on something tweeted from SAST (Swedish Association for Software Testing) session today - just because explaining context just does not go into a tweet.  
  
Here's my source of inspiration:  
> "We often sloppily hide manual regression testing in the term 'exploratory testing' it doesn't belong there" [@TomasRihaSE](https://twitter.com/TomasRihaSE) [#sastq1](https://twitter.com/hashtag/sastq1?src=hash)  
> — Ulrika Malmgren (@Ulrikama) [February 19, 2015](https://twitter.com/Ulrikama/status/568361111088713728)

I replied this, trying to stick to 140 characters, and got a reply that warrants for more than 140 characters.  
> [@maaretp](https://twitter.com/maaretp) [@Ulrikama](https://twitter.com/Ulrikama) certainly as do users and unexpected events Importance is how fast we fix them, that we dont block the cont flow & learn  
> — Tomas Riha (@TomasRihaSE) [February 19, 2015](https://twitter.com/TomasRihaSE/status/568447102835159040)

  
This just reminds me of so many of the discussions I've had over the last few years, driving my team towards continuous delivery that I need to outline some of my thoughts - still as a testing specialist.  
  

1. **Quality the team is able to produce without manual testing may differ greatly**  
   And when it does, having someone who sees problems (testing specialist) while others don't can be a very useful thing to have. When you use smart and thinking people, you probably will use them for two main purposes: exploratory testing (approach, as opposed to scripting manual cases for regression purposes; combine regression to testing changes in exploratory way) and increasing the level of test automation. I don't want just the latter, I want both.
2. **Breaking things and fixing fast can have business value** And when it does, it still interrupts the flow of new features in the development team to make the fixes available, especially if the fixes require significant effort. You might not want to block the flow to steal away capacity to support things in production you could easily avoid just by including a bit of exploratory testing in the process.  
     
   When I say can have business value, there's a story behind this. I learned with one of the products I'm working with, that fixing bugs quickly make customers like us - since competition is slower but still buggy and customer base is used to waiting for fixes. We just couldn't get as many real valuable features out when bugs from production kept interrupting our development flow. It's just an opportunity cost: time used on fast bug fixes could be time used on value that is many folds the cost of the testing that helps us stay more in the right flow.
3. **Before delivery, there is thinking time embedded in the change task**  
   While we want to deliver the value to production with continuous delivery/deployment, each value item we implement is thought of without pressure to allow thinking time. I wouldn't want to think development teams hack random solutions without thinking them through - that would be unprofessional. Fixing same thing many times isn't the learning intended.  
     
   So, why thinking time for "developer" is perceived as ok but thinking time for pairing two people, "developer+ tester" is perceived as blocking continuous flow and learning, instead of actually amplifying it? When you test a change in an exploratory (skilled) fashion, your thinking will include things that should not have changed. That is the essence of regression testing. But with exploratory approach, it is never *just* regression testing.  
     
   We should not only blindly chance but also think about what changes. Exploratory testing, seeing our change in context of the product seems relevant to me in addition to theoreticizing about the change (designing it to work in collaboration).  
     
   Refer back to point #1. Some teams think great without a testing specialist. Others don't. The ones that don't, learn to think better when they blow up the production in relevant ways many times - if no one has kicked the poor developers into a corner where they just assign blame instead of learning much of anything. Some organisations just need support on the culture that allows for learning, in my experience...
4. **Real users come with an opportunity cost**  
   Users too see problems testers can see. Some users see the problems right after they are created, other users report back the problems six months later when we no longer remember what we changed that broke it. And we value *fast* feedback to learn and to be efficient in the fixes. Users need to be seriously annoyed before they take time to report - the old wisdom of "every 10th user only complains" that you can see all over marketing literature most likely still holds.  
     
   And the real users do not exist to report bugs to us - they have a different purpose to serve. My users try to deliver construction projects with support of our software. When our software does not work, we take them away from the thing our company makes money on to make them our testers. Since there's an opportunity cost again (time to them running into problems and reporting them is time away from something else they could be doing), it's kind of easy to see that we may want to invest on having someone (everyone in the development team for that matter) doing the best we can to make sure they get interrupted as little as possible.  
     
   This one is my pet peeve. For some reason, almost all development teams I've had contact with seem to forget that money from someone else's budget is still money. The business we're in (Facebook on my mind...) may suggest that users cannot just get out and leave when they feel like it. And we may have mechanisms to not annoy same users with everything we break (throttled deployment just to a small portion) that help us mitigate the time we waste on using users as our testers. They may forgive us by the time we do that to them again.
5. **A skilled tester can represent a user - and a few dozen other stakeholders**  
   Many times I hear an implied (or direct) idea that testers are not real users. I'm also very fortunate to hear from my team's developers the surprise on how I can see things that the users will complain about, when they cannot. Skilled testers can represent users. And many other stakeholders too. Numerous times I've addressed things related to business aspects of the product; user flows that would create the optimal value increasing the value users get; legal aspects; how we support the product in production; concerns of future maintainability - just to mention a few.  
     
   You can also learn about some things without involving the users; involving the users when you have done what you can rationally do. Think before you deliver. In collaboration. See point #3.  
     
   People who think testers are not representative of real users and stakeholders may have run into unskilled commodity testers. There's a lot of those around, and they create a bad reputation, most often because their organization's culture drives them into behaving like idiots.

So in the end, I probably agree with the statement that we often sloppily hide manual regression testing in the term 'exploratory testing'. But not seeing exploratory testing as an approach that includes a miss of regression and new feature testing for any chance that we do, with a varying scope in relation to the change we are implementing and automation that exists seems off. The bugs we could find with using the product in a thinking manner in short timeframe are faster feedback we can react on without the cycle of involving users. Outside our automation, we are still interested in the surprising side-effects that we did not intend to design and implement into the system, and there's nothing that beats exploratory testing in finding those issues - and then perhaps automating some more based on what exploration taught us.
