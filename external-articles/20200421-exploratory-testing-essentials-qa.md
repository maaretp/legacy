---
title: "Exploratory Testing Essentials - Questions and Answers"
publication: "Xray blog"
date: 2020-04-21
url: https://www.getxray.app/blog/exploratory-testing-essentials/
source_retrieved: https://www.getxray.app/blog/exploratory-testing-essentials/
kind: article
language: en
---

# Exploratory Testing Essentials - Questions and Answers

*Xray blog — 2020-04-21*

Source: <https://www.getxray.app/blog/exploratory-testing-essentials/>

> Retrieval note: page text as published.

---
# Exploratory Testing Essentials with Maaret Pyhäjärvi

On April 2nd, TechWell hosted a webinar on Exploratory Testing Essentials with Maaret Pyhäjärvi (F-Secure) and Sergio Freire (Xray).

Maaret talked about how finding the Essentials of Exploratory Testing is going back to its roots as skilled multidisciplinary testing including programming as a tool.

Before we get into the Q&A insights, there are two extra opportunities we’d like to share :

[eBook] Exploratory Testing by Maaret Pyhäjärvi

This book refers to exploratory testing as an approach to thinking and learning while testing. Some might call this skilled testing. Some might say just testing (of good quality). It’s about the special thing professional testers do when they provide great results, so you can learn to do it better too.

[Free App] Xray Exploratory App

At Xray, we know that Exploratory Testing is essential to successful software testing. To support the testing community, we launched the Xray Exploratory App . This app is your go-to companion for Exploratory Testing because it eases the documentation burden by recording videos, making screenshots, taking notes, and sharing your results with your team.

## Convincing managers and people focused on automation

### How do you convince managers that Exploratory Testing is the way forward and explain its value when someone thinks that all testing should be automated?

The longer I have been in the industry, the less I feel that convincing people is a worthwhile cause. My managers rarely go into the details of how I get my testing work done, as long as results are great. I believe in the idea of not asking for permission but forgiveness if needed, finding that it is rarely needed. Radiating intent helps, as well as proposing experiments where we try things in different ways that the current perceived must practice.

If your managers or colleagues push for a certain way of doing testing, having a conversation about their experiences that lead them to this approach and listening may help. In particular, I find one of my earlier career major mistakes was trying to convince people that we should leave space for exploratory testing when the world around me started getting excited about test automation - I could have well-used my energy in helping test automation succeed earlier rather than in protecting space for exploring while not having to pay attention to code.

Nowadays, I model test automation as documentation I leave behind from exploratory testing and a foundation that enables reach beyond my abilities without code. In my experience, we explore when we automate, and it is our choice on how short a leash we use and what results we see as our opportunity to report.  I consider tight roles harmful, and I’m a great fan of pair and mob programming/testing and other forms of a great collaboration.

### You spoke of the idea that opportunity cost is a central concept. Can you explain some more about opportunity cost?

If you seek convincing, opportunity cost may be your way to do it. Opportunity cost is this idea that for every hour you use on something, you have choices on what you use that on . While you do something like create detailed documentation analyzing requirement documents, you are not spending the same time hands-on with the application.

While you write a bug report in the corner, it's important to perfect it so that the developer understands what you saw. You are not collaborating enthusiastically with the same developer, demoing the problem and working together to fix it. While you google to figure out why this test automation script keeps failing in surprising ways, you are not covering new ground in the application where bugs may exist.

We never have an endless amount of time. We always stop testing before we are completely done. We need automation to do some activity that spans over time, environments, data, and functional combinations. It is a worthwhile investment to build something that, when failing, is our invitation to explore. But having one scenario automated out of hundreds is not always better than attending to the application covering tens of others.

Exploratory testing is about looking at the whole, making choices on opportunity cost, and using code to test whenever it makes sense. And with continuous releases, it makes a lot of sense.

### Do you think the time to do Exploratory is the same or is it faster to get quality results?

This depends on what we are comparing it to. Exploratory Testing’s counterpart is scripted testing, which is like playing the game "20 questions" by writing down your questions at the time you know the least.

When you realize some of your questions are off, you can still throw them away and not ask them, but did you really need to create the questions in their final format, or you could have used that time on for example testing the earlier working version without the new changes to get you ready to recognize when things break?

Or could you have just read the specification without creating another kind of specification? Or could the specification you created have been something less effort-intensive and easier to update?

Since exploratory testing is an approach and not a technique where you always do things the same way, comparing it to something else isn’t straightforward. I can say on the comparison though that in cases where we write test cases and send them to an outsourced contractor to run, we could do more valuable work in just a few days than they could in weeks. And by valuable work, I mean finding issues that mattered.

I can explore level 1 (just find a function and see if it could work) or level 10 (function in combination with environments, other functions, data, and whatever other things I figure out that can be connected). Level 10 takes a lot more time , and we don’t always go to level 10. Level 1 exploratory testing is fine too . Regression test automation is often level 1, but we can’t afford to get to level 10 without automating - too much effort and not a smart choice.

## The skilled tester, being and becoming one

### Exploratory testing is based a lot on the experience of the tester, is this correct?

I believe in software development, our success is always based a lot on the experience of the people doing it. The most relevant experience is, though, the experience in learning - in all roles. If we keep having the same skills every day of a year and can deliver 1.00, we are consistently delivering the same 1.00. If we are able to continuously learn, to be 1% better every single day , we deliver 1.01^365 ~ 38 times what we did without the learning . The reason I believe exploratory testing as an approach is so powerful that it centers that learning.

You have more experience tomorrow than today. I've worked with great exploratory testers who just started their first job, and not so great with 20 years of experience of following a script in their head.

Writing documentation isn’t the best way to teach a developer programming, why would it be the best way to teach anyone testing?

### Is exploratory testing also a talent? Are the more observative persons more suitable for these positions?

Good thinking is a talent, but it is a talent we all need to grow. Observing is a talent too, but that is something we can grow in as well. Seeing examples of what kind of information we are looking for and reflecting on the ways we could find that information at the right time is a path to growing.

If there is one thing I look for in someone doing testing, it centers around being brave enough to speak about things they see - sometimes under conditions where it feels like the information isn’t most welcome. Like the Lessons Learned in Software Testing book taught us years ago:

“ A tester who cannot report bugs well is like a refrigerator light that is only on when the door is closed .”

It’s good to remember that bugs are not the only output we expect of testing. We want tools (documentation or automation) to help us do things better in the future, skilled testers of all kinds, and a product that makes sense to test addressing testability as a fundamental concept.

### What do you think about development teams without a tester role, being them the main responsible for the tests? And how do you see the exploratory testing in this scenario?

I don’t see the tester role as a must have, I see testing as a must have. Some of the best testers I know are developers. I am a polyglot programmer too! Yet, some of the other best testers I know don’t write a line of code, but specialize in domain knowledge. Developers (as in application programmers) can be domain experts, great testers and create the application. No one can do much alone, so we need other people around us.

The way I look at it is that a diverse set of ideas produces better software. When you collect ideas for 25 years, you already have some sort of a set, yet you benefit from having colleagues. And if in the software industry we have half of people with less than 5 years of experience, the likelihood of good results is higher when we mix people with different focuses, allowing them to grow to full capability over time as possible.

In one of my previous places of work, I was hired by an organization without any testers - the developers were the ones testing. They were puzzled on the high portion of big visible errors in logs that they could not find. Turns out they could, as soon as they gave up on the test cases a manager had enforced that kept them using time to look at the same, working places whereas they should have looked more around. The manager had good intentions, as they believed no one would ever enjoy testing. With those test cases, that was certainly true.

### So does being a good exploratory tester means that you have to be an expert at Test case writing?

The way I think of it is that generating test ideas is a central skill. Documenting those ideas as test cases is less relevant than being able to execute them. And when documenting those, automation is a viable way of documenting. Unit tests capture so much of our scenarios when we collaborate with application developers!

### Do you feel that Exploratory Testing allows the Tester to "Feel" whether something is not correct rather than just functionally correct?

I think the “feel” comes from many directions. Obviously reading the functional specification is one of those directions. Nothing in exploratory testing says we should be foolish and not care about the agreements made. We just don’t need to stick to that box when we are assessing possible information about quality. Even if we agreed it works this way, if we have seen other,  better ways of doing it, that is valid. If we are confused and have no idea how it would be better, that feeling is a valid way of reporting concerns on quality too.

### It sounds like exploratory testing is more like a mindset and motivation. You mentioned that your goal was to enable the rest of the team to become ETs. How can I push people in the right direction to become ETs?

I think of it as an approach to testing that anyone could have. I like to think of developers becoming better at exploratory testing just as much as I like to think of specialists in testing and know how to think better while testing. My current whole team of application developers, automation specialists and exploratory testers can do exploratory testing. Our rule is that whoever makes changes pulls others to help and everything that we deliver has at least two pairs of eyes on it . The developer's eyes - in a frame of exploring with their growing ability - is central.

To move more to exploratory, introduce introspection and reflection. Pair and mob. Try dropping things you’ve always done. Try adding things you’ve not yet had. With every change, learn. And learn about what goes out into production, listening to your customer feedback (with telemetry - no one should trust people to have energy to complain these days).

## Doing and reporting on Exploratory Testing - in Agile projects

### How can we include exploratory testing as needed in every sprint in Agile Project? How many hours do we allocate for exploratory testing?

Since exploratory testing (to me) is an approach, it is not an activity. It is the frame in which all my testing activities happen . What this question seems to be asking though is that when we have done all the other kinds of testing, should we still reserve time to just spend with the application using and testing it? Or, when we do nothing else but this, how much time do we need for testing in the end?

If it takes a whole sprint to code (and test) something, we can make a wide variety of choices on how much time we add on top of that. I find myself being around just about the same time as the creating the feature takes, and the time that I need for testing varies in how connected the feature is to others and how well I can trust the rest of the testing happening before me.

Exploratory testing takes my whole sprints. I do occasionally have time to fix bugs, I often have time to talk to my colleagues and point out how we could work better, and I have time to analyze what comes out of production as part of my plans for exploring now. I plan per feature what I want to see done before it goes out, and after it is out. Not testing something does not mean it could not work. It just means we did not see it working.

### Any advice for how best to report your testing status in scrum context? How do you provide exploratory testing metrics? For example, with a manager/director that wants testing coverage metrics?

I officially report (as to managers/management) very little. I discuss testing a lot with my team, and I do take notes. Whiteboards are full of little plans of what is needed and how we share that work.

I have reported earlier when we did not release this often. Continuous delivery removed the traditional test reporting need and moved us to report as a whole team. When I reported testing only, I usually looked at the number of open bug reports (which makes no sense now as there are no open bug reports) and testing progress. Testing progress I reported with a thumb vote turned to numbers on quality, coverage and expected change. Sometimes I would also report where time went - either setup, test or bugs with coverage only growing with test time.

### Is there a way to quantify exploratory efforts, especially to overlay it with Test coverage - especially if some sort of progress indicators are required by particular stakeholders and c-level management?

I work with products, and if our c-level was concerned with test metrics instead of business metrics, I would be concerned. They care about quality deeply, but as per our arrangement, they don’t need a metric on that, our teams maintain and improve the level of quality.

The way to get away from these metrics was to start releasing continuously. I do remember still, a time when we had projects, and managers cared about project endgame through testing. I just don’t miss those times.

For coverage reporting, it used to be relevant for me to have a coverage outline - no test cases though. Now I use that effort and focus - true to opportunity cost - into improving our test automation to be the coverage outline that then either is blue or not.

## Regulations

### How to integrate exploratory testing in the Regulated software industry?

The regulated industries are regulated because they handle risks around human life or significant economic impact. The way I look at it, those industries have been doing exploratory testing as rounds of rehearsal to their scripted, documented testing that the regulars require. They split testing into different stages. While they build the products, exploratory testing and quite insightful approaches to assess risks are their bread and butter. The final validation often needs to be done in a more scripted manner, but automation is also providing great scripted proof of these testing stages.

### How does regulated software adopt ET? Regulators still require script based evidence in their auditing.

I would like to suggest that this evidence is a small part of all things testing going on. There are people better than me to address specifics of how this works. I have not gone against a regulator but if I did, I would approach it with:

1) Some set of test as evidence;

2) Automation as evidence;

3) Classifying video sessions as evidence.

Even without regulators, in customer-contractor cases where customers are often suspicious on how testing hours end up used, evidence of some sort is often requested. Dig into the reason why they ask for evidence and find a time-considerate way of doing the evidence absolutely required. That evidence has less to do with testing and more to do with the relationship maintenance.

## Comparing to other methodologies

### A person asked me what percentage of bugs can be found while doing Exploratory Testing, compared with Scripted Testing. What do you say?

It really depends on the project. Or maybe more, it depends on the system under test . When there are a lot of bugs, it does not matter what mechanism we use to approach the testing, we can’t use the system without seeing issues. The problem is not with testing. The difference starts to show when code reviews and unit testing and considerate developers turn base quality around and bugs are hard to find. In one major project I was leading customer acceptance testing. We did scripted tests for one week, freeform exploratory for three. We found a total of three bugs in four weeks, and all of them with exploratory testing. But we paid a LOT for the contractor who did their testing in a scripted manner, worried about our tightened contracts.

It’s not about the percentage of bugs, it is about how much we are willing to pay for getting the same (excellent) software.

### What dangers do you see with Software that is already written, as we can fall into testing software that is already written and may miss bugs?

For me, exploratory testing is done continuously, so not only after writing software. I have an older version of our software that I can use as my external imagination while we are designing the change and find problems before we write a single line of change. For me, black box testing means we approach testing, exploratory or scripted without looking at all the nitty gritty internal details.

Testing is full of dangers and peril, and potential of wrong choices and missing relevant information. That is what makes it hard and interesting. It’s a continuous balancing act on risks and relevant information. The exploratory approach encourages us to learn and reflect continuously, rather than believe that what we carefully crafted at time we can by design know the least would have to remain as the guiding material.

### What in exploratory testing is like Ad hoc testing and what is different from Ad hoc?

I wonder if there is a practical difference. Back in the days I was a new tester, I had to report the type of testing I was doing. The bug reporting database had options ad hoc (directed) and ad hoc (undirected). I used to think that the ad hoc (directed) was exploratory testing, deciding on my intent and focusing on covering something specific. But later I learned that ad hoc (undirected) is just another form of exploratory testing. Usually when we say ad hoc, we mean there is no structure expected or given, whereas with exploratory testing, I would expect some. But I feel this all is more of wordplay than practical differences.

### Is risk-based testing part of Exploratory?

Risk-based testing is an idea of testing through sampling based on risk, rather than comprehensively trying to cover all aspects. We can analyze risks just as much for scripted and exploratory testing. Given the same amount of time, exploratory testing gives me more time with application while scripted takes away some of my time on creating the scripts. Assessing and labeling risks is a good practice.

## Other questions and topics

### Can any of the outlined principles be applied to end user database upgrades or UAT?

Yes. I’ve transformed multiple database migration projects and user acceptance testing projects from specifics of designing and writing test cases in advance to designing data and learning requirements in advance, while doing exploratory testing. In my experience it let us out of a box to consider what feedback was relevant, and it would have been foolish of us to not collect the data while preparing.

### Do you suggest creating test matrices for exploratory testing?

I sometimes use a matrix of some sort, most typically features x environments.  Whatever documentation helps you think, track and change as you learn more - I suggest going for that. Interested in trying Exploratory Testing? Download the Xray Exploratory App and start testing your systems.

### About the Author

Maaret Pyhäjärvi

Maaret Pyhäjärvi is an exploratory tester extraordinaire with a day-job at F-Secure as Lead Quality Engineer. She is a tester, (polyglot) programmer, speaker, author, conference designer and a community facilitator.

## Related Blog Articles

### Exploratory Testing

## Contemporary Exploratory Testing with Maaret Pyhäjärvi

### Exploratory Testing

## Uncover product risks with Exploratory Testing

### Exploratory Testing

## How to measure the success of exploratory testing?

## Ready to use Xray?

Get started with a trial for your business

## Subscribe our Newsletter

Receive the best articles, latest news, premium content and events information.
