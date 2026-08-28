---
title: "Trap of Skipping Releases"
date: 2019-05-02
updated: 2020-04-13
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2019/05/trap-of-skipping-release.html
---

# Trap of Skipping Releases

*Published 2019-05-02, updated 2020-04-13*  
*Source: <https://visible-quality.blogspot.com/2019/05/trap-of-skipping-release.html>*

---

It was the third day of making a release, and it felt like everything was going wrong. More like everything was harder than it should be. We had covered plenty of scenarios in our testing efforts, extended the test automation that we can run against the production environment and yet everything felt like an uphill battle.  
  
To top the frustration, just as we were completing the last of the last steps, one of us found a showstopper issue we all immediately agreed on we could not release with.  
  
What happened? The team that so fluently, with moderate effort and no pain was making releases, had regressed into this frustrating pile of individuals that failed at making a release - while succeeding in doing the right thing and caring for the millions our release would impact.  
  
Looking back, we fell into a usual trap we should know to avoid. The trap of not releasing often, and all the time. Instead, we collected 600 pull requests into one release. There was no way of making a release of that size that would be low risk, no matter what we were doing.  
  
The previous release included a design mistake we learned we had as we made the release. Due to the design that was very much intentional even if misinformed, many of the users could not get to the latest version. They weren't particularly bothered, we were. And as an end result, we  stopped releasing until we could figure out a new design on that particular problem.  
  
Making a big release brought out the worst of us:  
  

- We had trouble communicating on who does what and simple things were done many times whereas other things were not done on time
- We run test automation late, as we were struggling to get it to catch up with all the changes the product included.
- Finding a problem, we asked why did the others miss it and turned into a blaming crowd
- We started passing tasks away from our own lists to others, and created assumptions of completion just by assigning it
- We started growing the scope as making it available was taking time. Since it will be tomorrow perhaps we could include this one more thing - all contributing to the frustration.
- Doing the worst in some years is, in many ways, a healthy reminder. It reminds us on what we had with continuous releases, and how important that it. It aligns us on the goal of maintaining continuous releases.

  
And it could be worse. It could be that this wasn't an internal frustration and a reminder, but would reflect poorly on our users. Hoping for the best, fearing for the worst and ready to take on whatever the project life brings us.
