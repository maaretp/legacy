---
title: "The Foundation Moves - Even in Robot Framework with Selenium"
date: 2020-05-18
theme: test-automation
labels: []
source: https://visible-quality.blogspot.com/2020/05/the-foundation-moves-even-in-robot.html
---

# The Foundation Moves - Even in Robot Framework with Selenium

*Published 2020-05-18*  
*Source: <https://visible-quality.blogspot.com/2020/05/the-foundation-moves-even-in-robot.html>*

---

As my work as tester shifts with a new organization, so do things I am watching over. One of the things the shift made me watch over more carefully is the Robot Framework community. While I watch that with eyes of a new person joining, I also watch it with eyes of someone with enough experience to see patterns and draw parallels.  
  
The first challenge I pick on is quite a good one to have around: old versions out there and people not moving forward from those. It's a good one because it shows the tool and its user community has history. It did not emerge out of the blue yesterday. But history comes with its set of challenges.  
  
Given a tool with old versions out there that the main maintainers do their best deprecating, the maintainers have little power over the people in the ecosystem:  
  

- Course providers create their materials with a version, and for free and open courses, may not update them. Google remembers the versions with outdated information.
- People in companies working with automating tests may have learned the tricks of their trade with a particular version, and  they might not have realized that we need to keep following the versions and the changes, and maintaining tests isn't just keeping them running in our organization but proactively moving them to latest versions.

Robot Framework has a great, popular example of this: the Robot Framework Selenium Library. Having had the privilege of working side by side in my previous place with the maintainer [Tatu Aalto](https://twitter.com/AaltoTatu), I have utmost respect for the work he does.

The Robot Selenium Library is built on top of Selenium. Selenium has moved a lot in recent years, first to the Selenium WebDriver over the Selenium RC, and then later to versions 3 and 4 of the Selenium WebDriver to move Selenium towards a browser controlling standard integrated quite impressively with the browsers. As something built on top, it can abstract a lot of this change for its users, for both good and bad.

The good is, the users can rely on someone else's work (your contributions welcome, I hear!)  to keep looking at how Selenium is moving. As a user, you can get the benefits of changes by updating to the newer version.

The bad is, there might be many changes that allow you to not move forward, and it is common to find versions you would expect to be deprecated in code created recently.

Having the routine of following your dependencies is an important one. Patterns of recognizing that you are not following your dependencies are sometimes easy to spot.

With Robot Framework, let me suggest a rule:

> If your Robot Framework code introduces a library called Selenium2Library, it is time for you to think about removing the 2 in the middle and learning how you can create yourself a cadence of updating to latest regularly.

Sometimes it is just as easy as allowing for new releases (small steps help with that!). Sometimes it requires you join information channels and follow up on what goes on.

In the last years, we have said goodbye to Python 2 (I know, not all - get to that now, it is already gone) and Selenium has taken leaps forward. Understanding your ecosystem and being connected with the community isn't good thing to abstract away.

In case you did not know, Robot Framework has a [nice slack group](https://robotframework-slack-invite.herokuapp.com/) - say hi to me in case you're there!
