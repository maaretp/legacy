# Practice Makes Better - 5x to Continuous Releases

*Published: Jun 23rd 2021*
*Keywords: continuousdelivery, release, improvement

I've had my share of practice as a software tester. My career consists of streaks of 3 years at a job before moving on to try something different. Yet I find, just looking back five last teams I have joined, that my quest for different has given me the same assignment, and I recognized that only in hindsight! In this talk, I want to distill some of my lessons from this practice of showing up in places and turning up the release pace. I come at this as "just a tester" with the notion that *no one is *just* anything*. We come to things with our human traits and interests, and it is up to us to team up with others and make the best out of whatever we're given.

![Future is Already Here](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w4fzi43mll68zu4ysmdw.PNG)

For years, I looked around at conferences and heard some brilliant, amazing talks. For continuous delivery, I was inspired by Facebook and Amazon in learning about the machinery they built to release to production many times a day. As I looked around and talked to my friends in the industry, I learned that while we do great things, we have a tendency of including bits of wishful thinking in the experiences we share. The stories we tell at conferences are usually our best stories. These stories have power. I urge you all to believe that here, talking about future, the future is already present. It most definitely isn't known to me, and I have a lot of energy and other people's support on my side to pay attention. The future we are building is amongst us, it is very much not evenly divided. I believe I see one part of that future though, for all types of applications. And that part of future is one where continuous delivery transforms our software delivery capabilities regardless of technologies.

![My Work in Last Year](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kn96pfj4ea9kwzsl5pje.PNG)

I work as just a tester, with a fancy title: they labeled me a principal test engineer. What I do is improve testing from within, doing testing and sharing the work of testing with everyone. I test across teams, across the entire organization, with other system testers, developers, hardware testers, product owners and product managers. I get to talk to about 60 people a month as part of the work, I am the single person with end to end accesses to a major product we've been building because I've asked to get to test them. And the work I have done in a year can be shown in this series of numbers.

For a particular team when I retrospected with them on testing for the first time a year ago, it took them 32 days of making a release, and they were expecting to see one every six months. We worked together, turned releases into smaller, got rehearsing through six releases with most recent one taking us 2 days from feature complete commit to having the version running in production.

![Tempo Metric](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eatrgig56hhreh0ejy6k.PNG)

The most recent system I applied frequent releases at is not one that makes mobile applications. But we made a lot of the same arguments I hear people on mobile applications teams make: customers don't want frequent chance; this works only on web applications; it is impossible; the overhead of releasing is too much.

We have more work ahead of us to up the frequency, but I already see a team with improved collaboration, testing practice that can cope with the change that fits in their head, and aspirations to go further than where we are now, not just in the team but in the organization.

![Deployments/Releases](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g63dce73djc2y3m8rmyj.PNG)

We don't really separate deployment and releases conceptually, and the core of the change is added frequency. There's an old agile wisdom going around suggesting things get better with practice, so doing things that we avoid because they feel painful get better with the increased visibility.

There's two things that I think are quite magical on releases.

* The way release-making unifies a team of individuals and subgroups around a common goal.

* The way requirements discussions turn into real customer feedback and we stop the uncertainty buildup.

Releases frame a lot of the work we do. Not tasks. Not features. Releases. Making value available for customers.

![5x Continuous Releases](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h3v56qx6nu284q839bw1.PNG)

We talked about my last year, which I did not intend to become a year of moving teams to frequent releases. While my last year included several teams on a similar journey, my last five places of work, in hindsight, are a repeat story with similarities but also differences. I have come to appreciate that this is not a recipe I apply on places I work at, but it is more like a guardrail to introduce experimentation in.

Experimentation allows us to take the pieces of future we are building from where they are, adapt them and try how they fit for us.  Experimentation is how we bring teams from the past to the future - and beyond.

From my first team of frequent, weekly releases to thousands, the journey has taken me to monthly releases to millions where a release is not about updating a server but personal computers and devices across the world.

Every single one of the five has told me that what we did was impossible. Impossible is just something we have not yet figured out. And looking into the future that is already around us, we can pick up advice on the steps we could try to find our way around that impossible.

I can't today take the time to share you each individual journey. Instead, we look at some highlights that might prove useful on your way of making changes happen around you.

![Airing out stale practices](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2cqg5cjx3euzyux1z23w.PNG)

Being new to a team often, I have come to appreciate that a new person joining can be a disruptive event. The local culture is very infectious, and especially during trial periods, many of us, me included, are careful on how much we dare to rock the boat.

Coming into teams who have collected years of practices that have worked for them, I can be quite a whirlwind. Suggesting things like "no product owner", "no jira", "self-destructing product backlog", "no gatekeepers, pair over PR" and "everyone tests" are not easy ones to take in. And we usually already have system in place that keeps us functioning.

I remind myself that the way teams worked before I joined got them the job done and changing a little all the time is better than revamping anyone's practices. Continuous releases and turning up release frequency is an easier change that brings everyone on board, and enables sneaking in other changes.

![Release frequency changes practices](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6zqb6sp0nf3wgypra759.PNG)

When you move from a release every year to a release every month, you just can't keep all the old practices. As release frequency changes, you see testing looking different, shared for the whole team and steps towards build and test automation creating a shared experience in the team.  The architecture starts to turn something everyone understands and scope of releases move from systems to subsystems, and to components and even files. The organization around shows a different kind of concern, changing the tone of conversation from project management to tracking delivered scope running in production.

Most likely code review and branching practices change. And testing definitely looks at change as files and components changing in making risk assessments of what needs to be verified.

![Indirect change](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rv313r51jssuqcotomuh.PNG)

While the change is about release frequency, it changes many other things too. Everything is interconnected. Getting reluctant people to join in releasing more frequently helps rewrite their perceptions of what is possible. For us people there is this idea of cognitive dissonance, saying we are uncomfortable when our beliefs and actions are not congruent. So by making us do actions that don't match out beliefs is a more likely way of changing beliefs than conversations about those beliefs.

I did not know about cognitive dissonance until I was psychologically profiled for a leadership position I never accepted. The psychologist pointed out that what I was doing to make change happen had a name.

We have ideas of change we want to see, but another change may create the space for the change we hoped for. Everything is connected.

![Continuous releases without test automation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zqgfuavp7zy7969ma4nk.PNG)

A more surprising lesson over these five transformations has been one about test automation. I used to believe that test automation was crucial to more frequent releases. But then I worked with an organization where we had no unit tests or other level test automation. We built a release pipeline without a single test, where we could promote our system at will on press of a button.

We might not have gotten to the super-fast releases, but we did release daily, sometimes multiple times a day. We sorted out risks by testing in branches and hiding new functionality until we felt ready to show it.

Going through this on repeat, increasing release frequency sets a measurable goal of increasing our level of automation. But also, we can release a version without testing it and sometimes, in some of these organizations, the tests we were running were very close to closing our eyes at release time - to no harm in production. I've worked with some pretty amazing groups of developers.

But let's still emphasize this: build automation - reliable, repeatable, trustworthy, tested with every change - is non-negotiable.

![It's a Feature](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zslkjjk5zy2ju6ypy5g4.PNG)

This lesson  of considering features needed bit me again in the last week, so I'm reiterating it for myself just as much as sharing it for you. Moving to more frequent releases is more than just repeating the same faster. If you have something that at release time renders your customers system less valuable for 24 hours, you can't do that daily. You can't even do that monthly. But accepting that isn't necessary.

In efforts to find more frequent releases, we've introduced new product features like silent installs that never bring the system down, feature flag frameworks that allows us to hide changes until we want to see a group of changes revealed, upgrades that diff to a level of files that need changing and treating everything as code thus being able to assume that we can see changes we make.

![Crossing Roles and Tasks](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ct6bq8pl8bo8mwk6whik.PNG)

Moving through this change so many times has added to my understanding of importance of job crafting - the idea that we can take a job we're given and make it the job we want. There is almost always a little more flexibility than we give ourselves credit for, and conversations over cups of (virtual) coffee can do wonders. Building those bridges and relationships across roles helps in becoming more valuable for our organizations as we learn to connect things in insightful ways.

![Software Must Change](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bf1ewtgeq8nxq0zvo7e6.PNG)

We've talked about how frequent releases change testing and software development, but the change we see in our future is larger than our development teams. Our customers are increasingly expecting to see change, and choosing the applications they use and download based not only on features and quality, but the belief that software that does not change indicates the business behind it is not doing well, and the software is dying.

Looking at my phone where I don't turn on automatic updates, the feelings with large numbers of updates is three-fold. The annoyance of always having to update, the blind trust in it working because it did almost every other time I got to rehearse it - tinted with tester fear of new problems, and the appreciation of what apps are still worthwhile my time.

![Summarize to Milk](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qhzv61gb2ej0u0cxumi2.PNG)

Finally, I am inviting appreciation of how important change is by revealing how I find myself talking about milk at office.

Yes, milk. The white substance we in Finland consume one of the highest amounts per capita in the world. It's not the fact that an average Finn consumes 130 liters per year, but it may contribute to the fact that I have become painfully aware how quickly milk goes bad.

I find myself talking about milk with regards to test results, when my product management colleagues want to reuse results from six months ago (last release) in making a new release with limited testing now. The test results are like milk, if we infrequently release, we don't end up replenishing them regularly, and the old results are like old milk and we shouldn't trust them. So let's release frequently and keep our test results worthwhile.

I find myself telling my colleagues the same on practices. In places where I have worked, we tend to learn from our past mistakes and for everything that went significantly wrong, we add a new rule or practice. Sometimes we add new practices to a level where the practices prevent movement, and recently I have been having these conversations about pull requests, our go-to practice in protecting quality in the product. We really should have, like milk has, a best before date printed on every single practice. We shouldn't automatically assume all the great agreements from times before I even joined the team should still be valid today. Throwing old out makes room for new and fresh. So let's create space that moves us from our local optimum to finding something that works even better.

I also find myself thinking back to old experiences of importance of the second batch that is more fresh, enabling fixing something the previous batches introduced. When we invited an older lady from next apartment over for coffee in our student apartment and the first milk poured into her coffee made a plopping sound of sourness, it was great having a new fresh cup of coffee and a recently acquired milk to fix the mistake that had just happened. So let's make sure we have the possibility to fix errors without leaving our customers waiting for long. That requires new releases.

I also often go back to talking to business people how software is not like milk. When you go buy milk, it is cheaper if you buy as much of it as you think you can consume - larger portions of it are relatively cheaper. Software is exactly he opposite. The smaller portions include less risk, enable control of schedules and scopes. We want to keep asking how we could buy even smaller batches to improve our development efforts. So let's make sure we purchase and deliver software in smaller cartons, with features we can hold in our heads and supporting structures that help us hold the old promises with test automation.

I invite you to find the stories you repeat, and share them further. The future is already here, while not evenly divided. The stories of others inspire us on our journeys, and give ideas of things we could try. We're on a journey to future of our industry together. I believe the future is built in small incremental changes and social settings - together.

![Get in Touch](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1wss5a5hopq03a2v1s43.PNG)

I enjoy connecting with people, and love a good conversation. You may notice I like my work. I also like talking about themes related to my work. I started speaking to get people to talk to me. I talk back, and I invite you all on a journey to figure out how we explore our way into a better place for software creators and consumers.
