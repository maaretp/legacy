---
title: "A theory of risk - when sample size is relevant"
date: 2016-07-12
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2016/07/a-theory-of-risk-when-sample-size-is.html
---

# A theory of risk - when sample size is relevant

*Published 2016-07-12*  
*Source: <https://visible-quality.blogspot.com/2016/07/a-theory-of-risk-when-sample-size-is.html>*

---

I've been having these discussions about how words may be very different but interests very similar between programmer and tester communities. One of my favorite examples of that is that the testing community talks of [oracles, heuristic oracles and partial oracles](http://kaner.com/?p=190). It includes two main ideas: how would I recognize a problem and how I could create a program that recognizes problems? The same thing with focus on creating programs in programmer communities seems to go under the names of theory testing or property-based testing.

I feel a part of the reason we're not making enough progress in the field of smarter testing is that our worlds of solutions and ideas don't meet enough. We too rarely make the effort to understand what people mean, and in particular, we too often work with abstractions: concepts and discussions, instead of pairing up and doing stuff, and learning from that.

Looking through [Cem Kaner's oracle post](http://kaner.com/?p=190) with a programmer today made me think back to an interesting experience, and the programmer to find interest into working in a common kata so that all unit tests would be theories.

One of the very cool tests I performed in one organization came out of a consideration of risks. We were replacing an existing system with a new one, and of course while replacing, we were also changing things. We could compare some stuff between the old and the new system (and did), but that was not very straightforward. The system was generating decisions ending up in letters, and a lot of time the letters were barely if at all reviewed by a person.

I remember one of my big insights about the old system from having sat with users using the system that while the new system was fully automatic in sending the letters, the old system included a minor person interaction. With a lot of tacit knowledge, people using the old system would review the decision for rough correctness and interestingly, could change any inputs if they'd spot problems. The insight was that with the old system, the problems that would leak out of the organization were things were decisions were off only by a little, so that the person applying her knowledge would have hard time spotting them. That would not be the case with the new system, that targeted to still lighten the load of people involved in the process.

Speaking with various people, I came to the realization that one of my main concerns was that with the old system, the organization had over decades turned a fully manual handling process to a mostly automated process. There were very few people using the system. We were expecting to need less people with the new system. Anything that would increase need of manual work would be bad.

As I could state my theory of risk of increasing need of manual work, I could start working on how I could test that. So asking around, I figured that the new system would have specific error codes automatically moving the letters from automatic generation and mailing to manual processing - one perspective of the thing I was concerned about.

I set up a little script to take names and identifiers from an excel file with thousands of pairs of info, and generated messages into the decision engine and captured the return messages as files in a folder. I could very easily just search the files and count the number of instances of the error code I was looking for.

Within a short amount of time, I went from the contractor telling that the system was ready to production very soon, to understanding that this system in production would require us to manually work on more than half of the decisions we'd be using it for. The expectation was a small percentage and empirical evidence of a relevant dataset showed that it was not the case.

It was just one test amongst many others, but it had a lot of power as it revealed information in a wider scale. From a theory of risk of manual processing, one test took me to understanding how much processing could be expected.  Individual data points could have hinted on the same, but it would never have been as powerful as the wider sample set.

Kaner's post mentions business models as partial oracles. We all probably have our stories and experiences on how we figure out stuff like this. Are we sharing that so that others could learn from it?
