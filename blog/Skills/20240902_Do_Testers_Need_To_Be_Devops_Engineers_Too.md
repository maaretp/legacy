# Do testers need to be devops engineers too?

At a point of my testing career, I specialized in understanding test environments. It started off with seeing connections between subsystems, and recognizing compatible data. Well, there was no other choice to test effectively in insurance industry, where a new IBM mainframe test environment (I got one of those too!) took 1 million and 1 year. I can't remember if it was time when we still had Finnish mark as unit of money, or if it was already euro time, I just remember the overwhelming sense of responsibility for enabling  project with a million spending. That time of my career added awareness to any environment I would test in since, and categorizing workstations and servers and versions became a routine. 

When cloud later landed on my world, the categorization and foundation of test environments was particularly useful. Recognizing locations for storage, compute and specialized services and setting up connections and dependencies between all these geographically distributed and provisioned as needed with controls we have and controls that we recognize but don't have helped a lot in figuring out what it was that I was testing. 

It was easy to grasp that the new project that I just started with will have better working test environment early in the week, and we could expect troubles as the week advances. I could see what symptoms are likely to be about having provisioned a smaller test environment, what are likely to be results of data and memory, and I can design the way I test particular things around that weekly and daily cadence that I recognize going on for the test environment. 

I was thinking about his today, as I saw someone asking if testers need to understand CI/CD, and what of it, and what specific skills are we supposed to have in that space? 

Many of my colleagues extending in test automation space go CI/CD pipelines route after they realize that programmatic tests that run on their machine manually won't be much in the way of automation. There is a significantly higher value if tests are run right after a change that could break things is done and that requires designing the tests into a CI/CD pipeline. Many of those colleagues find barely a day a week for doing testing, when after running the tests nightly turns into optimized sets in the pipelines, and environments turn into dockerized orchestrated platforms where nothing changes in the infra without changing lines of code (Infrastructure as Code). 

I still work with testers who understand environments on the level I used to - recognizing that there is a different address for two different yet same test environments, with heuristics on what to pay attention to each. They, like me before I integrated a lot of this CI/CD pipelines stuff into my thinking, use environments with specific timing patterns to control the version they are experiencing in testing. They may design environments on the level of not allowing change, because installing means often unavailable or out of control we understand. These testers need to understand CI/CD as mechanism of publishing and scheduling, but go no further. 

Increasingly, I work with testers who design and enhance pipelines. While they don't need to do all the changes themselves, they need to read pipelines to see what goes on. Red has a reason, and drives their days of working to see where red is coming from. Majority of people in this group configure new jobs within the same realm of examples, and don't really take things further. Only some bring in new tools. But the new tools part, that is something people seem to love doing.

Then there are people who live in pipelines. Tests are placeholders and boxes, but they rarely have time to go and think about their coverage themselves. Working for the pipelines is the work. Making them run on better infra. Adding new tools. Upgrading the existing tools. Building all the machinery that could support the teams. These people, even with testing background, tend to call themselves devops engineers, to emphasize their attention to infrastructure and pipelines. 

When hiring for a tester, you may expect any of these levels of knowledge. A lot of people search for the middle ground. More and more, we expect people to come with the knowledge of what control pipelines give to your test environments and options of testing. 

And more and more, finding a balance where people know enough yet still manage to test not only build pipelines is what we seek.