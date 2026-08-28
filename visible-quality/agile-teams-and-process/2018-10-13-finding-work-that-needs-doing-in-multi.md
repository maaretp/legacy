---
title: "Finding the work that needs doing in a multi-team testing"
date: 2018-10-13
updated: 2018-12-26
theme: agile-teams-and-process
labels: [Agile]
source: https://visible-quality.blogspot.com/2018/10/finding-work-that-needs-doing-in-multi.html
---

# Finding the work that needs doing in a multi-team testing

*Published 2018-10-13, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2018/10/finding-work-that-needs-doing-in-multi.html>*

---

There's a pattern forming in front of my eyes that I've been trying to see clearly and understand for a good decade. This is a pattern of figuring out how to be a generalist while test specialist in an agile team working on a bigger system, meaning multiple teams work on the same code base. What is it that the team, with you coaching, leading and helping them as test specialist is actually responsible for testing?  
  
The way work is organized around me is that I work with a lovely team of 12 people. Officially, we are two teams but we put ourselves all together to have flexibility to organize for smaller groups around features or goals as we see fit. If there is anything defining where we tend to draw our box that we are not limited by, it is drawn around what we call clients. These clients are C++ components and anything and everything needed to support those clients development.  
  
This is a not a box my lovely 12 occupies alone. There's plenty of others. The clients include a group of service components that have since age of time been updated more like hourly and while I know some people working on those service components, there's just too many of them. And the other components I find us working on, it is not like we'd be the only ones working on them. There's two clear other client product groups in the organization and we happily share code bases with them while making distinct yet similar products out of them. And to not make it too simple, each of the distinct products comprise a system with another product that is obviously different for all three of us, and that system is the system our customers identify our product with.  
  
So we have:  

- service components
- components
- applications
- features
- client products
- system products

When I come in as tester, I come in to be caring for the *system products* from *client products* perspective. That means that to find some of the problems I am seeking, I will need to use something my team isn't developing to find problems that are in the things my team is developing. And as I find something, it really does no longer matter who will end up fixing it.  
  
We also work with a principle of internal open source project. Anyone - including me - in the organization can go do a pull request to any of the codebases. Obviously there's many of them, and they are in a nice variety of languages meaning what I am allowed to do and what I am able to do can end up being very different.  
  
Working with testing of a team that has this kind of responsibility isn't always straightforward. The communication patterns are networked and sometimes finding out what needs doing feels like a puzzle to solve where all pieces are different but look almost identical. To describe this, I went to identify different sources of testing tasks for our responsibilities. We have:  

- Code Guardianship (incl. testing) and Maintenance of a set of client product components. This means we own some C++ and C# code and the idea that it works
- Code Guardianship and Maintenance of a set of support components. This means we own some Python code that keeps us running, a lot of it being system test code.
- Security Guardianship of a client product and all of its components, including ones we don't own.
- Implementing and testing changes to any necessary client product or support components. This means that when a team member in our team goes and changes something others guard, we go as team and ensure our changes are tested. The maintenance stays elsewhere, but all the other things we contribute.
- End to end feature Guardianship and System Testing for a set of features. This means we see in our testing a big chunk of end users experience and drive improvements to it cross-team.
- Test all features for remote manageability. This means for each feature, there a way of using that feature that the other teams won't cover but we will.
- Test other teams features in the context of this product to some extent. This is probably the most fuzzy thing we do.
- All client product maintenance first point of support. If it does not work, we figure out how and who in our ecosystem could get to fixing it.
- Releases. When it's all been already tested, we make the selections of what goes out and when and do all the practicalities around it.
- Monitoring in production. We don't stop testing when we release, but continue with monitoring and identifying improvement needs.

To do my work, I follow my developers RSS feeds in addition to talking with them. But I also follow a good number (60+) components and changes going into those. There is no way anymore Jira could provide me the context of the work we're responsible for, and how that flows forward.

I see others clinging to Jira with the hope that someone else tells them exactly what to do. And in some teams, someone does. That's what I call my "soul sucking place". I would be crushed if my work was defined to do that work identification for others. My good place is where we all know the rules of how to discover the work and volunteer for it. And how to prioritize it, what of it we can skip for low risks related to others already doing some of it.

The worst agile testing I did was when we thought the story was all there is.
