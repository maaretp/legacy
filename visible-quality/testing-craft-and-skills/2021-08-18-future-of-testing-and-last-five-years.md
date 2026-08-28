---
title: "Future of Testing and Last Five Years?"
date: 2021-08-18
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2021/08/future-of-testing-and-last-five-years.html
---

# Future of Testing and Last Five Years?

*Published 2021-08-18*  
*Source: <https://visible-quality.blogspot.com/2021/08/future-of-testing-and-last-five-years.html>*

---

This morning opened up with Aleksis Tulonen reminding a group of people that he asked us five years ago a question on the future of testing in five years.

> Five years ago, people made predictions on how our approaches in software development will change in the following years. They also considered how the changes would impact testing approaches. <https://t.co/nGFyOmUhh6>
>
> — Aleksis Tulonen (@al3ksis) [August 18, 2021](https://twitter.com/al3ksis/status/1427936555583279111?ref_src=twsrc%5Etfw)

I had no idea what I might have said five years ago, but comparing to what I am willing to say today, the likelihood of saying something safe is high.

**So, what changed in five years?**

- **Modern Agile**. I had not done things like No product owner, No estimates and No projects at the last checkpoint. I have done them now. And I have worked in organizations with scale. These rebel ideas have been in scale of the team I work in with relevant business around us.
- **Frequent Releases**. It may be that I learned to make that happen, but it is happening. I've gone through three organizations and five teams, and moved us to better testing through more frequently baselining quality in production with a release. And these are not all web applications with a server, but globally distributed personal computers and IoT devices are in my mix.
- **Integrated engineering teams without a separate testing group**. Testers are in teams with developers. They are still different but get along. Co-exist. Separate testing groups exist in fewer places than before. Developers at least help with testing and care on unit testing. You can expect unit testing.
- ****Exploratory includes automation**. Profile of great testers changed into a combo of figuring out what to test and creating code that helps test that. The practice of "you can't automate without exploring. You can't explore (well) without automating." became day to day practice in my projects.**
- **BDD talk. BDD became a common storyline and I managed to avoid all practical good uses. I tried different parts of it but didn't get it to stick. But we stopped using the other words as commonly - specification by example and acceptance test driven development lost the battles.**
- **Ensemble Testing and Programming**. It moved from something done at Hunter to something done in many but still rare places. I made it core to my teaching and facilitating exploratory testing in scale at organizations I work at. And it got renamed after all the arguments on how awful 'mobbing' sounds. The term isn't yet won over completely but it has traction.
- **Testing Skill Atrophy**. Finding people 'like me' is next to impossible. Senior people don't want to do testing, only coach and lead testing or create automation. Senior testers have become product owners or developers or quality coaches but rarely stay in hands-on testing. We are more siloed within testing than we were before. And finding "a tester" can mean so many things that recruiting is much harder these days.
- **Developers as Exploratory Testers**. Developers started testing and in addition to small increments - test after cycles taking us to good level of unit testing without TDD, developers started driving and contributing in exploratory testing on different scopes of the system. They were given the permission to do 'overlapping' work and run further than testers got in the same timeframe.
- **Test Automation University**. Test automation became the go-to source for new testers to learn stuff around. Test Automation University, headmastered by Angie Jones and sponsored by Applitools, became a bazaar for materials on many different tools.
- **Open-Source to Fame**. Everyone has their own tool or framework or library. Everyone thinks they are better than others. Very few really know the competition, and marketing and community building is more likely to lead to fame. Starting something became more important than contributing to something.
- **Browser Driver Polite Wars**. Options to Selenium emerged. Selenium became standard and even more options emerged. People did a lot of browser testing and Cypress made it to JS-world radar for real. Playwright started but is in the early buzz. Despite options that are impossible to grasp to so many people in development efforts (there's other stuff to focus on too!) people mostly remained respectful.
- **Dabbles of ML**. First dabbles into machine learning in testing space emerged. This space is dominated by commercial, not open source. And programming was "automated" with Github Copilot that translates well-formulated intentions as comments into code machine learned from someone else. Applications with machine learning became fairly commonly available and bug fixing for those systems became different.
- **Diversified information**. There are more sources for information than ever before, but it is also harder to find. Dev.to and self-hosted blogs are the new go-to, in addition to written content video and voice content has become widely available. Difficult part is to figure out what content makes sense to give time to and we've seen the rise of newsletter aggregators in testing field.
- **One Community is No More**. Some communities have become commercial and in many ways, resemble now tool vendors. Come to our site, buy our thing - paywalls are a thing of the day. At the same time, new sources have emerged. There is no "testing community", there are tens of testing communities. Developer communities have become open to testing and choosing to hang out with people in the language you work in has become something testers opt in for more.
- **Twitter Blocks Afoot**! While visible communication is more civil and less argumentative than before, people block people with a light touch. If blocking someone five years ago was an insult, now it is considered less of an insult and more of a statement of curating the things you end up reacting to in the world.
- **Women in Testing**. The unofficial slack community grew and became a globally connected group of professionals. Safe space with people like me enabled me to start paying attention to contents of men again and saved many people from feeling alone and isolated in challenging situations. The community shows up at conferences as group photos.
- **DevOps**. It is everywhere. The tools of it. The culture of it. The idea that we pay attention to 'testing' in production (synthetic tests and telemetry). 'Agile' became the facilitator wasteland and developers of different specialties grouped their agile here.
- **Cloud**. Products went to cloud first. Supporting tools followed in suite. And the world became cloud-native for many corners of the software development world.
- **Mobile & API**. These became the norm. REST APIs (or gRPC) in the IDE is the new UI testing. Mobile has separate language implementations for presentation layers and forced us to split time on Web / Mobile.
- **Crowdsourcing**. It remains but did not commoditize testing a lot. I find it almost surprising, and find this to be a hope for a better future where testing is not paying user to hang out with our applications to pay them peanuts for time and bigger peanuts if they were lucky to see a bug.

I most likely forgot a trend I should have named, but the list of reflections is already long. But back to what **I** predicted.

> I don’t think much will change yet in 1, 3 or 5 years, other than that our approaches continue to diversify: some companies will embrace the devops-style development and continuous testing, while others figure ways for releasing in small batches that get tested, and others do larger and larger batches. Esp. in the bespoke software sector, the forces of how to make money are so much in favor of waterfall that it takes decades for that to change.
>
> But if there is a trend I’d like to see in testing, it’s towards the assumption of skill in testing. Kind of like this:
>
> - black-hat hackers are people who learn to exploit software for malice.
>
> - white-hat hackers are double agents who exploit software for malice and then give their information to the companies for good
>
> - exploratory testers are white-hat hackers that exploit software for any reason and give that information for companies. From compromise to more dimensions like “hard to use”, “doesn’t work as intended”, “annoys users”.
>
> - because exploratory testers are more generalized version of hackers, exploratory testing will go away at the same time as software hackers go away. You get AI that write programs, but will need exploratory testers to figure out if programs that are produced are what you want.

I don't think I see my hope of "assumption of skill in testing". I see better programmers who can test and a few good testers. Being a developer with testing specialty is one of the entry level roles and everyone is expected to pick up some programming. Acceptance testing by non-programmers remains, is lower paid and has different time use profile - as much time, but in small deliveries and better quality to begin with.

My bets on AI will come for the programmer jobs barely fit the 5-year window, but from where we got now, I wouldn't say I am wrong on it. Then again, testers became programmers and we started understanding that programmers don't write code 7.5 hours a day.

Next five years? Will see how that goes.
