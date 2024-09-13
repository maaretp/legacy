# Believing things can be different

27 years testing, and I still think problems with software are fascinating. Running into a problem does not mean it wasn't tested at all, it means I run into a flow that wasn't covered or a problem considered not relevant to fix under whatever constraints the organization has. Sometimes the conditions are fairly general throughout the user base, like with Crowdstrike, and impact all users. Sometimes the conditions are fairly specific, and impact some users. 

There's a story I have told a lot, an illustration of serendipity and the role it plays in testing. Joining a new organization as a tester on my first day, I got access to the system under test, credentials to log in, and logged in barely before I was asked to join whatever inception program the company had in mind. Being pressed with time and not relying on remembering, I bookmarked the address. Not the main page though, I had already clicked onwards a bit, not even paying attention. When I got back to testing, I used the link to find the application and experienced a big visible error screen. Further investigation showed that I was lucky enough to bookmark a single page inside the application with a different implementation pattern resulting in this error. Quite a way to make a tester entrance. 

For some years after that, I was thinking that core of testing seem to be **serendipity** and **perseverance**. Working with a team where developers tested, had tested for 15 years before the first tester ever joined the team, claiming there was no testing done would have been misrepresenting the efforts. But something with the way I tested was different. I got lucky with running into bugs. A lot. Like a more than you can imagine. And this sentiment is something a lot of testers relate to. And I gave the program chances to show how I was lucky, with systematically working through flows and time, and odds, fast forwarding different users year in production time and time again. 

I pulled up two quotes to summarize the insight I had gained: 

> "The more I practice, the luckier I get." - Arnold Palmer (golfer)

> "It's not that I am so lucky, I just stick with the problems longer." - Albert Einstein (scientist)

This kind of luck favors my kind, testers, or at least we frame it as a positive event of luck, to serve as means to remove such luck from those who would not welcome it. But we aren't always working. Work is when you get paid. Most of your time, you are just you, and a user amongst all the others. You'd love for the systems you use to have been built and fixed to work, but things are complicated.

A favorite incident, really showing perseverance with the problem comes from a friend. She was out in an event one evening with her development team, having a good time. She returned home late, crashing in for the night as soon as she could. Next morning she realizes things are a little off at her house. Her scented lamp has fallen and stained her sofa. Going into her kitchen, she discovers a handwritten note. In her absence, police had visited inside her apartment to turn off Alexa, and left a note. A little later in the day, a worried neighbor reaches out and tells about the full blasting volume of music leading to calling the police over, this being so unusual. Turns out Alexa had been throwing an empty house party. 

We were recounting this incident and all the details of interoperability at a conference to realize - later to be confirmed by another colleague working inside AWS, that there was indeed a case where you could have Spotify in a state where you could be far away trying to connect Spotify elsewhere, only to turn up volume on the previous location. A very specific flow. This interoperability bug resulted in an invoice from the apartment company for opening doors to the police late in the evening in owners absence, and a lot of research on whether you could be responsible to pay up for a bug somewhere between Amazon and Spotify. Turns out that spending enough time fighting, you did not have to pay. 

I did not turn this one into a talk and research for quotes, but I did draw a major lesson: 

> Getting lucky costs you time and money that no one is responsible for. 

It's a lesson that is hard to miss as a tester. You are sometimes painfully aware that outside the paid hours where you work for advocating for users in a very particular style, the same characteristic of serendipity is used as free labor sometimes by accident and sometimes by design of the companies. 

When I a few years ago serendipitously run into a Foodora security bug that allowed users to get free food, I did the free labor following through to fix before I disclosed my knowledge. They gave me a discount code of a few euros for hours of investigating with them, which compared to my professional rates are quite a contrast. 

When I last week serendipitously run into another Foodora bug that now impacts users, I came to realize the immense power difference when tables are turned. User advocacy takes even more time. I do user advocacy, because I believe things can be different. 

Things can be different if people share their experiences, and individual experiences sum up to phenomena that speaks to the power. 

Things can be different if people care enough to pick up feedback outside the usual channels. 

Things can be different if people believe there may be a step in the flow where while it works on your machine, it indeed does not work on mine. 

Believing things can be different guides my choices of what I end up doing with my time and effort. I ended up researching legislation to learn where to report and how so that I can loan power a regular user does not have. They would have to investigate with a specific way of asking and report back to me in writing in 14 days. They would have to correct the state of my banking within 1 day. 

I did not imagine that in reporting this I would serendipitously find one more bug: the messaging app fails with error code 500 ("it's our backend") on a specific part of the message I had crafted, even if it seems like regular text with no special features. Reporting the second bug was possible in the messaging app, reporting the first bug required sending over a portion of the text as a screenshot. I did try also talking to a developer who worked at the company and was helpful in explaining how things should work on Foodora, because believing things can be different means I believe people could help when their organizations technical channels fail. 

From this one, I can draw again major lessons: 

> Reporting channels don't always work even if you find them, reducing your chances of solving your issues.

> Testing gives you tools and attitude to work around what blocks you: the text vs. screenshot, the developer inside the organization; the legal references.

A regular user would give up but I am no regular user, even if I am a volunteer on task of user advocacy. When I get the written report on this, it still does no conclude the case even if it hopefully fixes this bug. There's still the work we need to do in the industry to connect the regular users with working feedback systems to get things set right, and the work of setting our systems right. I hope the programmers and testers community does better on quality, and I know it is not easy. I know we try and that we are not done. 

I've been a tester for 27 years because I stick with the problems longer. And I stick with the problems on user advocacy. It's as important as ever when we can't even find a channel to communicate back our troubles to the multinational corporations. Just look at the troubles content creators have social media being kicked out from the foundation their businesses run on, without routes to appeal. 

User advocacy is speaking. It's listening. And the latter is needed even more.  