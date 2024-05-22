# Making Releases Routine

*Published: May 23rd 2024*
*Keywords: releases, failure, testing, improvement

Moving organizations from infrequent to frequent releases has been my signature move for a decade. While the successes of moving from 30 days to 30 minutes of release timeframe are things I have learned from, nothing teaches you like a good old failure. After a streak of improvements, last year I faced an interruption to the streak with a four month stabilization phase.

We learned from the failure as a team, and I learned from the failure as an individual. With the odd chance that you could try your own mix of failing instead of repeating ours, let's dissect our experience together. Having just completed the 7th release of year 2024 in the team, I can fairly certainly say we made releases routine, again.

Key takeaways:

- What is the necessary tester brain rewire
- How in practice we turn testing continuous and releases routine
- Importance of conceptual separation of the pipeline and the compliance

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4ll4ddnv694co7dch2l4.png)

In my three decades of working in software projects with a testing emphasis, I have changed jobs a lot. I believe that while practice does not make you perfect, it makes you better, and one of my signature moves I have had plenty of practice with is shortening the release cycles.

I joined this organization 4 years ago, and have been through it here multiple times already. This talk however focuses on the latest product, and my 2,5 years on it, and the deeper lessons I drew from that time.

The first of the three years, we went through the motions. We built a continuous testing capability with increasing amount of test automation, but particularly a pipeline in which we could capture the moves needed. Saying we went from a month of release testing to 30 minutes of release testing is simplification, because we went from not getting releases out to getting them out regularly, and pretty routinely. The routine relied on me as the team's principal test engineer.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eda2f0hp7hgodry0wzr5.png)

Since I had been through this numerous times before, I repeated the basic maneuvers. I taught people that releasing frequently is a game-changer, both for the whole team but particularly from a testing perspective. My go-to story was to talk about how "Pool is not a bigger bathtub". It was not about just doing the same moves faster and more frequently, but we'd have new purposes the new practice enables. You can imagine things like pool party, and swim guard by the pool, but try placing those two to the bath tub and it's more amusing than useful. They are both containers of water, but they enable entirely different purposes. Just like infrequent and frequent releases are both releases, but the entire flow of how teams work gets to change.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yydx06d01elkxn9ak06e.png)

From metaphors, we'd go to sampling some of the practices. Moving testing down in the decomposition chain, more tight collaboration and shared ownership, having to pay attention to purposes of parts in the architecture and hiding things you deploy but want to keep hidden from the customers with feature flags.

Practice made us better. Doing releases was not particularly painful. I was ready to leave again. But this time around instead of leaving, I answered a *what would have to be different for you to stay* question, and became development manager for the team. We made agreements of having no tester in the team. I was confident that would work just fine.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n6qk8u06pcbbqd58hbx1.png)

The 2nd year surprised me. In autumn of 2023, I had to face the reality. Over the timeframe of what was just a few months, we had a version of the product where nothing worked and releases were a pipe dream. We went from frequent releases to struggling with releases, and making one took more than 3 months. It was the most painful release I had experienced in decades.

The first two releases of the year were routine, and I took care of the routine on the side of picking up lots of new work as the manager. The developers did just as well as they had before on keeping release on a short leash. Then I needed to introduce a tester into the team. More of my time went things other than hands-on testing, especially since I needed to make space for the new tester to take up testing work.

With a track record and identity on the signature move, failing with this was not the easiest of experiences. There was no easy and simple explanation. If there was, I would have been able to pass that information to the team I was working with, and a three month stabilization phase would not be what we were experiencing.

Failing is ok though, and failing being ok needs to be modeled. Three months in an organization that wasn't releasing frequently before may be inconvenient to my aspirations, but it lead us to learning.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ckatfii20u0l7q4b8dpq.png)

Mistakes were made, and most definitely by me. Then again, we were not out to find a single culprit, but to understand what was taking us to the entirely different experience.

We realized we had simultaneously let go of two essential key ingredients to frequent releases. We tested continuously, but we also accrued a results gap in testing continuously, as we didn't complete things before there was more to test. We got more to test since whenever product owner would ask about capacity, a free developer would pick up new work over fixing bugs.

In a few short months, we accrued uncertainty in scale that made testing difficult, and sharing fixing work broke down completely. A lot of this breakdown was related to practices I had as a tester, that I had not taught the new tester, as some intricate ways of testing and communicating is invisible to a seasoned tester, and a more structured approach is needed to support someone learning the finesse.

I have often quoted Cem Kaner on "Tester that does not report bugs well is like a refrigerator light that is only on when the door is closed". My established conversational style of feeding requests for fixes without prioritizing them through a product owner wasn't possible for others. I had levels of status, already when I was not a manager - after all I was the only principal tester in the organization. And I had not realized how much uncertainty we accrued before I put my hands in the software.

I should add, there was also a new kind of testing (performance) that injected while we were still in the fixing cycles. It turned out to reveal a bug where we experience 1:160 performance degradations where root cause was hardware. Limit WIP, also from adding new testing capabilities point of view.

We dug ourselves out of the self-made hole by very traditional bug reporting and fixing cycle.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zeglag241yhq61ygbs3k.png)

We were barely out of the hole, and had retrospective conversations with the team. There were many reasons and the conversation was not an easy one due to the systemic nature of the problem, but the core output of the retro was a common commitment: "Make Releases Routine". We decided that routine required that when a month was over, a release would happen. Month would be the minimum, we would prefer 2 weeks. We would not let ourselves go on a longer leash anymore.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dnimjuozwl34xikgpn8j.png)

Energized by the failure and learning, we modeled the tasks that were involved in making a release. Our particular flavor had 18 tasks. Team members paired with me on those tasks. And we learned that many - most - of those tasks were things only I knew how to do.

We grouped the work to see patterns in the tasks, and minimized the team's tester's focus on continuous system testing rather than everything I had done for the releases.

Developers set out to automate more into the pipeline. We improved capability and reliability of the pipelines significantly.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vvr6cg6135e71qp6bg5u.png)

With more rounds of practice, we realized we needed to solidify and establish continuous testing capability. We did this by detailed coaching for the tester to make good selections on priorities and need of collaboration.

We pulled out to separate cadence all things that did not need to be bundled with release. All things compliance tend to be this.

We looked at the tasks we were doing critically, and started dropping things intentionally. What we ended up with looking at the emergent structure, is a pipeline producing a release candidate, and a set of compliance work.

Latest of the releases took 30 minutes.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ilrm93s0r5n27u5mn2bb.png)

There was a lot of work under continuous system testing that was a relic of the old ways of testing, from time when we had less test automation we could lean on. Building that capability in test automation allowed for compliance-related need of testing to move fully to the principle of seeing green and packaging programmatic tests with the release as evidence. I have been looking at a growing trend in numbers and code coverage, as well as the trend of things found that automation misses.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9pkay0fyygist505eh2z.png)

Over three calendar years, we had quite big differences. New people in the team. New base knowledge. I would like to think that having failed and learned solidifies the practice. Time forward with me away from the team will show if we established a way that scales.

From this experience, I went back to thinking about what I wish I would have explained better.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/iokj1ahpg8vnie0skesl.png)

I still keep hearing that releases are overhead. Many teams push against frequent releases. They are still stuck in that bathtub and don't even recognize the party they could have if they had a pool.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ee5xww80quyh8pnti6p0.png)

What is this work then?

First of all, it's somewhat of an investment to build and maintain a pipeline that does builds and releases. But when that exists, it does a lot of heavy lifting for the team.

Second, there is process - requirements on how things must be done, and people with power of blocking reviews. Sending an email and waiting for a response can be surprisingly much work, and especially calendar time.

Third, a lot of teams still pile up many kinds of testing activities to the concept of the release. It may be exploratory testing sessions by the whole team. It may be manual regression testing. It may be daily test automation with failure analysis activity. What it shows up as though is a gap in testing results and the larger the scope, the larger the uncertainty.

It's not a static listing, but all of these are probably areas where your aspired capability and your current capability are not quite on par.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1b1czitppujdrrexz7ad.png)

The sense of overwhelm with release work, for us at least, did not get easier by looking at the details. We minimized our themes checklist to 8, containing the 22 required high level checks the process asked for, with the 3579 tickets for specific compliance checks. And yes, I have actually read these through.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/il5xjrq42ppd4pt4zxm2.png)

The results gap of testing is the most devious one though. It's like an empty paper of results where magic ink turns the text visible. And the magic ink is not available to us all. It is still common that next groups in line (acceptance) have information and understanding that your immediate team may lack.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9uz1zumvtkavqpv4wnpj.png)

This boils down to a question:

**What must be different to shorten release testing from 30 days to 30 minutes?** Think about it for a moment.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/trqmf06oqjhqmavfzyuf.png)

It's not the automation alone that must be different. Having automation is important. More important than test automation though is build automation. I have successfully done daily releases without any test automation for an earlier project. We overemphasize test automation.

You won't have automation that does the same work that you'd do in a month in 30 minutes. You're designing relevant parts of the work. It's a redesign of tasks.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/iaoa8n9cpqc1b3kdmial.png)

A core part to redesign is that you don't test as much as you used to in what you call release testing. You do more before release testing. You ask developers to do more. You trust developers having done more, and let them fail and learn. Hard thing to do, I know. They can test. Really they can. They often don't because they like you to have work and imagine you wouldn't if they didn't leave you some. Talk about it.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7c41doe6rnxccr79kt80.png)

What also must change is bugs found at this stage. Those should be a special case. And only certain kinds of bugs -- new ones -- should matter. You will learn as you test same product. Apply that learning outside release testing, you have continuous work. Let bugs get on the next train.

The amount of testers I have offended saying we release today whether you tested or not is not small.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4h73ir6kq1vfrgyffyc5.png)

You make changes and deploy. You call that feature testing.

You decide it's time to deploy elsewhere. You call that release testing. You don't repeat testing you did on the first for the latter. And you might use ways of hiding the changes until your organization is ready to show them. Feature flags are a way of limiting visibility to unfinished work from a customer perspective.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/am7gkcfrpsoyllz9zdu5.png)

To top this off, I have three guidelines for you.

Make everything as code. When code changes, you see the change. Follow the change. Learn to understand what the change you see is. Have conversations with developers around that change. Teach your developer colleagues to write what they just learned about the thing they implemented when they know the most, which is at time of pull request / commit. Plans and tasks are outdated and inaccurate at that time.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rwwbrnnhovkjtec43ark.png)

Learn to pace testing to continuous. Start off-sync testing activities as capability building activities to turn them in-sync. Build test automation, not because it finds you bugs but because it tells you about changes you did not understand were happening. When they fail, learn about what you did not know.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/b34t5ze25sl2i9gs2ell.png)

Build that pipeline, and grow it. Make it do more of the work that needs doing for every pull request. Routine really comes with repetition. Capture that knowledge in code.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6crf79v172isyyvejtqu.png)

To conclude, I am quoting myself. I may come to this from a tester - a manager - a programmer perspective, but "Making releases routine is the heartbeat of a good team, creating a bubble of productive serenity". You may need that bubble in the organization your team works in.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vrqb6u7kd9bc1zmjhlp9.png)

I enjoy connecting with people, and love a good conversation. You may notice I like my work. I also like talking about themes related to my work. I started speaking to get people to talk to me. I talk back, and I invite you all on a journey to figure out how we explore our way into a better place for software creators and consumers.

I’m happy to connect on LinkedIn, and write my notes publicly on Twitter.
