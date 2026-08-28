---
title: "Testing the same old but with a new implementation"
date: 2016-02-22
updated: 2016-08-02
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2016/02/testing-same-old-but-with-new.html
---

# Testing the same old but with a new implementation

*Published 2016-02-22, updated 2016-08-02 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2016/02/testing-same-old-but-with-new.html>*

---

Many of us testers run into these occasionally: there was a feature that was done and tested a while ago. Then new information emerged and a complete rewrite in order. More often that not, there's a new understanding of requirements driving the change. There's often something new that needs to be implemented, that would be hard to extend on the old implementation.  
  
Me and my team are in the final rounds of one of these changes. We had 3 reports (which are basically the main output for the users using our software) and we needed 3 new ones, which needed to be essentially different. And while discussing these 3, we realized that what we actually need is a report configuration engine, as the each of the new organizations coming into this is likely to have their own configuration needs even if the information would be same or similar.  
  
With this rewrite, one of the shining stars in the team took the problem and turned from someone who could deliver incrementally into a protective person, focused on the technical structures. In hindsight, he was doing a lot of research on components he could use but it all appeared one big chunk. And digging him out the hole he dug was quite an effort.  
  
At some point, all the 6 reports were all intertwined and needed to be released together. A discussion by discussion we untangled them, and delivered the 3 new first (already months ago) to learn what they would be in real use. We learned just few weeks ago they are missing an essential feature, so a second round of work on them is in order. And the 3 old ones, we found ways of delivering them one by one. After 3+1 out, we decided on changing the layout in relevant ways, and again agreed on the steps to deliver this further.  
  
As we're now on final rounds, there's two reports left to test. I was feeling the testing was particularly straightforward in the pattern:  
  

- search for customer feedback on the old reports
- pick any special data mentioned in the reports
- generate a new and old report, and compare

I found many problems with the approach today. I learned that for a particular set of data and options, the report wouldn't generate at all. I learned that there was extra information and that some of our conciseness goals were nicely achieved. Over the day, I felt as if I was surrounded by a warm blanket: there was the old version, the version that worked "right". And it was so rare to have that that I realized I almost had forgotten how much that helps.

Feeling too comfy, I decided to try something different, and cover combinations of options in more detail again. I made a list on paper of what I wanted to try, and to my surprise found more relevant problems of how things would misbehave.

At the end of the day, I was reflecting back what I had done. How close it was that I called it done when I did what I had in mind test design wise. And how relevant it was to find the other way of approaching to learn what did not work.

All it takes is finding the next stretch. But I love having the old system as an oracle. Why did I ever settle in not keeping the old installation available when I was newer to this? Can't imagine.
