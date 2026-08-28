---
title: "One Company, Five Testing Archetypes"
date: 2022-01-20
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2022/01/one-company-five-testing-archetypes.html
---

# One Company, Five Testing Archetypes

*Published 2022-01-20*  
*Source: <https://visible-quality.blogspot.com/2022/01/one-company-five-testing-archetypes.html>*

---

In last two years, I have had an exception opportunity to deepen my understanding of the context archetypes, working in a company that encompasses the five. But before we dive into that, let me share an experience.

*Facilitating a workshop on what successful looks like in test automation, I invite pairs of people to compare their experiences and collect insights and related experiences on what made things successful. The room is full of buzz as some of the finest minds in test automation compare what they do, and what they have learned. The pair work time runs out and we summarize things and here's what I learn: test automation is particularly tricky for embedded systems.*

For years, people could silence me by telling me how *embedded systems* are special. And sure they are, like all systems are special. But one thing that is special about working with embedded systems is how convoluted "testing" is. And today I wanted to write down what I have learned of the five types of archetypes of testing that make talking about testing and hiring "testers" very complex even within a single company.

**Software and Systems Testing** is the archetype I mostly exist in. Coming to a problem software first, understanding that software runs on other software, that runs on hardware. That hardware can be built as we build software from components of various abstractions to integrate, or it can be a ready general purpose computer, but it exists and matters to some degree. Like a jenga tower, you will feel shaky on the top layers when the foundation is shaky, and that is usually the difference that embedded systems bring in.  But guess what - that is how you feel about software foundations too and there is a \*remarkable\* resemblance to embedded software development and cloud development in that sense.

With software and systems testing, you are building a product in an assigned scope, overlaying your testing responsibility with the neighboring teams, and a good reminder on this archetype is that for testing, you will always include your neighbors even if you like to leave them out of scope of consideration for development purposes. Your product may have 34 teams contributing to it (I had last year) or it might have a lot simpler flow considering end to end. Frankly, I think the concept of end to end should be immediately retired looking at things from this archetype's perspective.

**Hardware (Unit - in isolation / in integration and Compliance) Testing** is something I have been asking a lot of questions on in the last two years, and I find immensely fascinating specialty. The stuff I loved about calculating needed resistor sizes are the bread and butter in hardware, but making it only about the electronics / mechanics would be an underappreciating way of describing the complexities. Hardware testing is a specializing field with many things worthwhile standardizing and standards compliance makes it such a unique combo. The integrations of two hardware components have its own common sets of problems, and the physical constraints aren't making life simple. Hardware without software is a bit lifeless box, so hardware testing in integration and particularly compliance testing already brings in software and system perspectives, but from a very specific slice perspective.

Really great hardware testers think they don't know software testing yet do well on helping figure out risks of features. I can't begin to appreciate the collaboration hardware designers and hardware testers are offering. The interface there, particularly for test automation success is as close to magic as I have recently experienced.

**Production Testing** is the archetype that surprised me. Where hardware testing looks at design problems with hardware, production testing looks at manufacturing problems with hardware. And again, since hardware without software is a lifeless box, it is testing of each component as well as different scopes of the integrated systems. The way I have come to think of production testing, it is the most automation system design and implementation oriented kind of testing we do. Spending time on each individual piece of hardware translates to manufacturing costs, and the certainty of knowing the piece you ship to the other side of world will be quality controlled before sending is relevant.

Being able to connect our production testing group to great unit testing trainer is one of my connections to learn to appreciate this. Ensembling on their test cases, seeing how they are different, reading their specs. And finally, being on the product side to build test interfaces that enable the production testing work - I had an idea but I did not understand it.

**Product Acceptance Testing** is the archetype of testing I could also just call acceptance testing, and it is associated with promise of a delivery of a *project* not a product. If you need to tailor your product before it becomes the customer's system, you will probably have need of something like this. We call it FIT or FAT (in both cases, it's the integrated system but either in artificial or real physical environments) and the test cases have little in common with the kind of testing I do within Software and Systems Testing. This is demonstrating functionalities with open eyes, ready for surprises and really wishing there were none.

**IT Testing** is the final archetype focused on the business systems that run even software companies. There may well still be companies that don't have software products (even if the transformation is well on its way to make every company a software company), but there are no companies who have no IT. Your IT system may be that self-built excel you use, or a tailored system you acquired, but when it runs \*your business\*, you want to test to see your business can run with it. Not being able to send invoices terminating your timely cash flow has killed companies.

The difference in IT Testing comes from lack of power. The power is in money starting projects. The power is in agreeing more precisely what is included, or agreeing to pay by the hour. Constraints are heavy on the IT systems you are using as foundation, because this is not the thing you sell, this is something that enables you to sell.

> The archetypes matter when we try to discuss *testing*. Because it is all *testing*. It is just not working with the same rules, not even a bit.
