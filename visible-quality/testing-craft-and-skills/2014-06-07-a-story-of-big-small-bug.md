---
title: "A story of a big small bug"
date: 2014-06-07
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2014/06/a-story-of-big-small-bug.html
---

# A story of a big small bug

*Published 2014-06-07*  
*Source: <https://visible-quality.blogspot.com/2014/06/a-story-of-big-small-bug.html>*

---

This week, after a day at conference and a day home with a sick kid, I got back at the office to test. As I opened Jira and got reminded of recent fixes, I chose an area that I found relevant to start from. The changes were quite extensive as the developer had spent several days puzzled with them.

I opened the application and clicked though the shortest possible sunny day scenario and the application froze. I could't believe it, so I restarted and it was true. I felt upset. I felt disappointed. I felt that with all the efforts to improve on team responsibility, it just gets worse. I was thinking that perhaps the best way to help my team mates feel responsible would be just to remove me as the safety net - except that did not work either. So I talked with the devs to let them know it doesn't work and blocks me, logged it on Jira and steamed out the worst of frustration in a tweet.

Then I tested some more, to learn that the first feature I was testing was just a tip of the iceberg. Out of the features I tried, there was one that worked and many that didn't. I realized the problem wasn't with the changes to area I was testing at first, but with common dialog component. As we're a tight team, I realized the issue would belong to another developer, the one with the faulty change. So I reassigned the jira issue.

At this point, I was even more upset. There was a problem making our application freeze on all actions but the one the change was done for. Not only had the developer making the change skipped testing any other places when changing our dialog component, but he had done the change paired up with another who did the same. And none of the six had used the app in over two days to notice.

Soon after, there was a quick and dirty fix - by the words of the developer. The final fix would take a little longer. But I was told they're both small fixes, and wouldn't need much testing after. A little later I also learned that a developer had seen the problem, but forgot to mention it to others. At least there was hope, as the whole team wasn't completely hands off the application. Mistakes happen.

This incident reminded me again about the difference in how I think as a tester and how developers think. When I see a problem, I look into its severity and implications to users. When developers see the  same problem, they look at how interesting or complicated it is to fix. And size of symptoms may be completely unrelated with the size of the fix.

With the discussions on smallness of the fix, I was left feeling unappreciated. It was a small fix, small effort for the developer. But it wasted a day of my time. How about including my time in sizing up the implications in the team? It would have kept small if there was at least a bit of own testing by the developer before the feature showed up in the common build. Or after. But before it blocked all of my other testing.

Also, the fix wasn't small to me as I was going through all features in the program for other surprising impacts. While knowing the fix it was unlikely, it was still a possibility. Again some hours of work the developers refuse to take ownership of as it shouldn't have an impact.

So, negotiating on more test automation ahead. Even if the developers dislike maintaining it.
