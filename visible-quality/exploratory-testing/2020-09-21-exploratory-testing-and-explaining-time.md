---
title: "Exploratory Testing and Explaining Time"
date: 2020-09-21
theme: exploratory-testing
labels: []
source: https://visible-quality.blogspot.com/2020/09/exploratory-testing-and-explaining-time.html
---

# Exploratory Testing and Explaining Time

*Published 2020-09-21*  
*Source: <https://visible-quality.blogspot.com/2020/09/exploratory-testing-and-explaining-time.html>*

---

If you've looked into exploratory testing, chances are you've run into two models of explaining time.

The first one is around the observation that there are four broad categories of "work" when you do exploratory testing, and only one of them is actually taking your testing forward, and thus visualizing the portion of this may be useful. In that model, we split our time to setup, test, bug and off-charter. Setup is anything we do to get ready to test. Test is anything we do to amp up coverage from just starting to getting close to completion. Bug is when we get interrupted by reporting and collaboration on results of testing. And off-charter is when we don't get to do testing but to exist in the organization that contains the testing we do.

The broad categories of work model has been very helpful for me explaining testing time to people over the years. It really boils down to a simple statement: Getting to coverage takes focused time, and if we report the time on it, you may have an idea of testing progressing. Let's not measure test cases or test ideas, but let's measure time that gives us a fighting chance of getting testing done.

The three other categories of time use outside "test" are set up as the possible enemy. Setup takes time - it's away from testing! Finding many bugs - not only away from testing, but requiring to repeat all testing done so far! Off-charter - you're having me sit in meetings! They can also be set up as questions to facilitate a positive impact on the "test", as in investing in setup that makes test time be sufficient, or investing in pairing on bugs that make future bugs less frequent.

The second model making rounds includes a more fine-grained split of activities happening within exploratory testing sessions, that people could even use to explain their sessions for things like daily meetings. Instead of saying you are doing "testing" day after day for that big login feature, you could explain your focus with words like intake (asking around for information and expectations), survey (using the software to map, but not really test), setup (infra and data specifically), analysis (creating a coverage outline), deep coverage (get serious testing done), closure (retesting and reporting).

If we map these activities to the four categories, there's a lot of explanation for setup here: intake, survey, setup, analysis and closure are all mostly setup - they don't really build up coverage, but are necessary parts of doing testing properly.

While the first model has been valuable for me in years of use, I would replace the latter model by finding the words that help you communicate with your team. If these words help, great. If these words silence your team members and create a distance of them not understanding your work, not so great.

The words I find myself using to explain how I progress through a change / feature related exploratory testing are:

- what am I *investing* in: in the now, or for later; getting the job done quick vs. enabling myself and others in the future
- what kind of *outputs* I'm generating: story of my testing, bug reports, mindmap, executable specifications
- what kind of *output mindset* my work has: generative or completion-oriented; some work generates more work, some gets stuff done
- whether you see *movement*: working vs. introspecting; some work looks like hands on keyboard, other look like staring at a whiteboard

For me it is important to add more words to "test" too: mapping, acquiring coverage, completing as well as for "bugs": isolating, documenting, demonstrating.

Looking at the way I work, I explain very little of testing in daily meetings and don't write a report of any kind. Documentation I leave behind is automation. For transferring deeper knowledge, I pair with people, and to get new people started, I write a one page playbook of testing that sets the stage. The people I explain testing to are ones I pair with for either automation or for doing particular testing.

The real question of explaining your time is: Why are you doing it? Do you grow others with it? Do you explain yourself to people who hired you for them to trust you? Or maybe you explain it to yourself  as introspection, to figure out how things could be different for you tomorrow.
