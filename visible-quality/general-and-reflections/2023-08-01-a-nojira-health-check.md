---
title: "A NoJira Health Check"
date: 2023-08-01
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2023/08/a-nojira-health-check.html
---

# A NoJira Health Check

*Published 2023-08-01*  
*Source: <https://visible-quality.blogspot.com/2023/08/a-nojira-health-check.html>*

---

One of my favorite transformation moves these days is around the habits we have gathered around Jira, and I call the move I pull NoJira experiment. We are in one, and have been for a while. What is fascinating though is that there is a lifecycle of it that I am observing, live, and wanted to report some observations on.

October 5th, 2022 we had a conversation on NoJira experiment. We had scheduled a training on Jira for the whole team a few days later, that with the team deciding on this one then promptly cancelled. The observation leading to the experiment was that I, then this team's tester, knew well what we worked on and what was about to be deployed with merging of pull requests, but the Jira tasks were never up to date. I found myself cleaning them up to reflect status and the number of clicks to move tasks through steps was driving me out of my mind.

Negotiating a change this major, and against the stream, I booked a conversation with product ownership, manager of the team and director responsible for the product area. I listened to concerns and wrote down what the group thought.

> - Uncontrolled, uncoordinated work
> - Slower progress, confusion with priorities and requirements
> - Business case value get forgotten

We have not been using Jira since. Not quite a year for this project, but approaching.

First things got better. Now they are kind of messy and not better. So what changed?

First of all, I stopped being the teams' tester and became the team's manager, allocating another tester. And I learned I have ideas of "common sense" that is not so common without having good conversations to change the well-trained ideas of "just assign me my ticket to work on".

The first idea that I did not know how to emphasize is that *communication happens in 1:1 conversations*. I have a learned habit of calling people to demo a problem and stretching to fix within the call. For quality topics, I held together a network of addressing these things, and writing a small note on "errors on console" was mostly enough for people to know who would fix it without assigning it further. It's not that I wrote bug reports on a confluence page instead of Jira. I did not just report the bugs, I collaborated on getting them fixed by knowing who to talk to and figuring out how we could talk less in big coordinating meetings.

The second idea that I did not know to emphasize enough is that *we work with zero bugs policy* and we stop the line when we collect a few bugs. So we finish the change including the unfinished work (my preferred term to bugs) and we rely on fix and forget - with test automation being improved while fixing identified problems.

The third idea I missed in elaborating is that *information prioritisation is as important as discovery*. If you find 10 things to fix, even with a zero bug policy, you have a gazillion heuristics of what conversations to have first over throwing a pile of information suffocating your poor developer colleagues. It matters what you get fixed and how much waste that creates.

The fourth idea I missed is that *product owners expectations of scope need to be anchored*. If we don't have a baseline of what was in scope and what not, we are up for disappointments on how little we got done compared to what wishes may be. We cannot neglect making the abstract backlog item on product owners external communications list into a more concretely scoped listing.

The fifth idea to conclude my listing in reflection is that *you have to understand PULL*. Pull is a principle, and if it is a principle you never really worked on, it is kind of hard. Tester can pull fixes towards a better quality. Before we pull new work, we must finish current work. I underestimated the amount of built habit in thinking pull means taking tasks someone else built for your imagined silo, over together figuring out how we move the work effectively through our system.

For first six months, we were doing ok on these ideas. But it is clear that doubling the size of the team without good and solid approach of rebuilding or even communicating the culture the past practice and success of it is built on does not provide the best of results. And I might be more comfortable applying my "common sense" when the results don't look right to me in the testing space than those coming after me.

The original concerns are still not true - the work is coordinated, and progresses. It is just that nothing is done and now we have some bugs to fix that we buried in confluence page we started to use like Jira - as assigning / conversing / reprosteps listing, over sticking with the ideas of truly working together, not just side by side.
