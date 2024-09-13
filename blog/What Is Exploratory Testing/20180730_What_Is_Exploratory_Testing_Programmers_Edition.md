# What is Exploratory Testing — the Programmer Edition

It has been 34 years since Cem Kaner coined the term to describe a style of skilled multidisciplinary testing common in Silicon Valley. In the new software world regime where programmers find themselves taking a lot more responsibility of testing, we need to understand what exploratory testing is as it extends what most programmer’s find their tests covering, and causes us talk past each other in understanding what testing.

![Girl on computer](./girloncomputer.webp)

## What Testing Gives You?

As a programmer, you know what you’re implementing. When you don’t know, you’ll learn. You explore the problem to figure out a solution.
Back in the days some bad organizations told you that they’ve hired a group of testers. They might even say that since they pay other people for testing, you shouldn’t be bothering yourself with that.

But you know you want to test. Because testing has direct value to you as a programmer. It gives you four things:

* Specification

* Feedback

* Regression

* Granularity

Specification means that tests you write can be concrete examples of what the program you’re about to write is supposed to do. No more fancy words around high level concepts — give me an example and what is supposed to happen with it. And when moving on, you have the specification of what was agreed. This is what we made the software do, change is fine but this was the specification you were aware of at time of implementation.

**Feedback** means that as the tests are around and we run the tests — they are automated, of course — the tests give us feedback of what is working and what not. The feedback, especially when we work with modern agile technical practices like test-driven development, gives us a concrete goal of what we need to make work and if it is working. They help us anchor our intent so that given the interruptions, we still can stay on the right path. And we can figure out if the path was wrong. This is the test that passes, yet you say it isn’t right. What are we not seeing?

**Regression** means that tests don’t only help us when we’re building something for the first time, but they also help us in changes. And software that does not change is dead, because users using and loving it will come back with loads of new ideas and requirements. We want to make sure that when we change something, we make only changes we intended. And regression is the perspective of doing more than we intended, without tests without us knowing.

**Granularity** comes to play when our test fail for a reason. Granularity is about knowing exactly what is wrong and not having to spend a lot of time figuring it out. We know that small tests pinpoint problems better. We know that automation pinpoints problems better than people. And we know that we can ask people to be very precise on their feedback when they complain something doesn’t work. Not having to waste time on figuring out what is wrong is valuable.

This is not exploratory testing. Exploratory testing often guides this type of testing, but this is testing as artifact creation. Exploratory testing focuses on testing as performance — like improvisational theatre — in a multidisciplinary way beyond computer science.

## Exploratory Testing, eh?

I get all of this good stuff from testing as I know it, unit tests and test automation. What is this exploratory testing stuff then?
Exploratory testing is basically saying that spending time thinking with your application, your APIs, your environments as an external imagination, you will find things you did not realize you were missing. And time thinking with something you’ve implemented is real, empirical. Not just something you wish was true like most of our designs.

Exploratory testing is multidisciplinary, basically saying that it is not enough for you to take orders from whoever gives you requirements, but you have to think critically on why they are asking what they are asking and its practical implications. If someone asks you to do something that is illegal, you need to point it out. If you don’t know if it is illegal, you need to spend time figuring out what is and isn’t illegal, and how that would show up in the application you are creating. GDPR is a great example of this: not caring for privacy can cost your organization a lot. And it is not just law you need to care for. You need to care for business, users, environments your software runs in, ethics, psychology — and many more. You want to do no harm, and be conscious about what you are doing. Intentional, not accidental.

With the way you look at testing as programmer, what more is there that exploratory testing promises to give you? It’s an approach that focuses on learning while evaluating what you know and don’t know, giving yourself chances of learning the things you don’t know you don’t know but can see while using the application like your users would.

It gives you four things:

* Guidance
* Understanding
* Models
* Serendipity

**Guidance** is not just about the specification, but general directions of what is better and what is not. Some of it you don’t know to place in yes/no boxes, but have to clarify with your stakeholders to turn them into something that can be a specification.

**Understanding** means that we know more about the place of our application in the overall world of things, why people would find it valuable, how other’s design decisions can cause us trouble and how what should be true if things were right always are not. It helps us put the details we’re asked to code into a bigger picture — one that is sociotechnical and extending beyond our own organization and powers.

**Models** are ways of encoding knowledge, so that we can make informed decisions, understand things deeper and learn faster next time or with next people joining our teams.

**Serendipity** is the lucky accidents, running into information you did not expect to find. The lucky accidents of new information about how things could and do go wrong when using your application emerge given enough time and variety to use of your application. And knowing helps you not get the escalations waking you up to critical maintenance tasks because who else would fix all of this than the programmers?

## An Approach To Testing

Exploratory testing is a approach to testing. It says whoever tests needs to be learning. Learning needs to change what you are doing. You can’t separate designing of tests and executing them without losing learning that influences your next tests. It is an approach that frames how we do testing in a skilled way.

We don’t do just what is asked, but we carefully consider perspectives we may miss.

We don’t look at just what we are building, but the dependencies too, intentional and accidental.

Unsurprisingly, great programmer teams are doing exploratory testing too. Creating great automation relies on exploratory testing to figure out all the things you want to go check. While with exploratory testing we believe that premature writing of instructions hinders intellectual processes, we also know that writing that stuff as code that can be changed as our understanding grows, this frees our mental capacity to think of other things. The executable test artifacts give us that peace of mind.

Programmer teams are also doing what I would consider low quality exploratory testing with limited ideas of what might make a difference in new information being revealed. And that is where testers often come in — mindspace free of some of the programmer burdens, they focus their energies elsewhere, raising the overall quality of work coming out of teams.

Finally, I want to leave you with this idea — bad testing is still testing. It just does not give much of any of the benefits you could get with any testing. Exploratory testing and learning actively transforms bad testing to better.
