---
title: "Faking testing and getting caught"
date: 2021-02-13
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2021/02/faking-testing-and-getting-caught.html
---

# Faking testing and getting caught

*Published 2021-02-13*  
*Source: <https://visible-quality.blogspot.com/2021/02/faking-testing-and-getting-caught.html>*

---

A lot of my work is about making sense into the testing we do, and figuring out the quality of testing. The management challenge with testing is that after they come to terms in investing in it, it isn't obvious if the investment is worth it. Surely, the teams do testing. But do they do it so that it provides the results we expect? Faking testing isn't particularly hard, and the worst part is that a lot of the existing processes encourage faking testing over testing that provides results. With an important launch, or an important group of customers we're building a business with, we don't want to be surprised in scale or type of issues we have never even discussed before.

I find myself in hunt of two aspects of quality in testing: effectiveness and efficiency.

Effectiveness is the idea that no matter what the testing we do is, does it give us the layers we need to not be caught red-handed with our customers? To be effective at testing, we have two main approaches:

- Build well - bad testing won't make quality worse
- Test well -  when issues emerge, finding them would be good

A good way to be effective at testing is to bring in more eyes at the problem. Don't ask only the developer-developer pair to test, add a third person you believe will take testing to heart and prioritize it. But why settle for three people if you could have ten, or 10 000. Grow the group. From unit testing to system testing, to end-to-end testing of systems, to pilot customers to beta customers, to real customers in production with continuous releases. That will tell you of effectiveness of earlier stages, and make you effective overall.

This effectiveness consideration is the most important work I do, and sometimes - I would even say often, I catch people in this activity on faking testing. Most often people don't even realize they are faking testing, and they approach testing with wrong skills and focus, not providing the result that would be reasonable to expect for investing into that layer.

Faking testing, no matter how unintentional, looks like we do a lot and we do, but we get nothing out. And we notice only when there is a need of testing well, because building well did not alone give us sufficient results. The later stages, hopefully designed into the overall testing in times close to the faked testing rather than discovering quality of testing at the delivery, reveal bugs in scales and types that we would reasonably expect to be found if we did the stages well.

While effectiveness is the key, after effectiveness is in place I look at efficiency. There is only so much we should have to invest in testing on various layers, testing should increase our productivity and not slow us down, and we might be investing in a box of testing thinking it cover more boxes than it should for the return the investment gives us.

These puzzles often fill my days, and I try to help people learn exploratory testing to get away from faking testing. They don't want to fake it, they just do what they think they should.
