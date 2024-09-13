# Did you make notes of what you learned on the CrowdStrike case?

It was hard to miss a few weeks back: CrowdStrike's inputs off-by-one bug bluescreened a number of computers relevant enough to impact how business of all sorts run globally. I'm still not sure what is the top sentiment of this for me:

* *Sucks to have been the cause of this*. Sociotechnical systems fail and you never know when you're part of the system that causes this.

* *Scale of who were impacted surprised me*. Managing to deliver visibly broken to this scale in an hour feels rushed.

* *Costs of this across industry must be everyone's responsibility*. Having people manually fix this on business computers globally must have cost a fortune, and the bill of this must end up being split instead of finding its way to source.

Everyone in this tech bubble followed this. Everyone had an opinion. There's a case of failure now, something other than Therac-25 we still talk to this day as an example even if that happened 1987.

## An Outsider's Recount of What Happened

Revealing the details of the issue reached us in two waves:

* First wave of reporting focused on "it's the test system that did not catch it".

* Second wave of reporting focused on why and changes resulting from it

I learned more from the second wave of reporting.

I learned the problem was an off-by-one number of inputs of specific kind between two components. One component produced input of 21 input parameters with the extra input parameter including specific kind of input. The other component received 20 input parameter and did not work well with the extra input parameter with specific kind of input.

The time-based distribution of why this leaked was particularly interesting.

The capability to produce templates with 21 inputs was introduced in February and taken to production. The use of the capability with incompatible input happened in July, resulting in the blue screen.

Process-wise, the bug was missed in February. It may have been introduced by another developer. The latter developer, in July would have found the bug if they tested previous developer's work again. Testing of it, as it appears, would have required two things that take effort away from the development environment:

* Production like environment. If Windows blue screens, a Windows would have been needed. Nothing in the materials discusses if developers could test this on their development machines, or if it would require connecting to a virtual environment or remote environment.

* Looking at result from outside in. As last step of making a change, someone could look at the change working at least on one Windows machine. The reporting, however, does not make it completely clear if there really was no third conditions like having to run the system for more than 5 minutes. These kind of faults could take time for the computer to do the work to come crashing down.

**This could have happened in many of the organizations I have been at**. Developer teams shortcut production like environments and looking at the result from outside in. Even when automated, end-to-end tests like this take longer to run. It is often considered a risk worth taking that we make software available for users without zero pair of eyes on it. I tend to prefer two pairs of eyes on a change, because no one - no one - should be left alone with responsibility of potentially breaking some millions of computers globally. It is always a fail of the sociotechnical system when pushing bugs to production, in scale, happens.

The changes outlined were interesting: Items 1-4 are missing behaviors (features) of the code. Item 5 says they will test in changes now in integration instead of in isolation. Item 6 says they will throttle delivery to destroy a select group rather than everyone. Items 5&6 are generally considered good practices.

## Recounting Personal History

I used to work with security software with risks exactly like this - possibility of taking down millions of Windows machines. This whole incident reminds me we too, decade(s) ago had problem like this that test coverage missed. But we had a few other mechanisms that protected us:
Delay-based distribution: the group who would get things first was small but reactive, and rendering a board member's computer useless without manual intervention did a lot of good for investments in ensuring the lessons were learned without impacting customers
Eating own dogfood in company: we learned to distribute internally continuously, and segment distributions. The whole environment for testing was built to provide HUMAN interventions because test systems fail.
Throttling, autorevert, secondary update channels: we built a number of features that would enable us to fix things without showing up face to face
Architectural rewrites: isolating risks like this, because not all software causes blue screens.
And then there was the continuous investment on test coverage. I would have remained disappointed if the conclusion in the end is that test coverage is what they missed, when they have a wealth of investments their board members would happily sponsor to never see this happen to them again.

## Moving on

The sociotechnical system designed and put in place did not account for a risk that realized. And that leaves me thinking of this.
"Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."

--Norm Kerth, Project Retrospectives: A Handbook for Team Review
This is our chance as industry to remember: Production-like environment and looking at result from outside in. In some teams developers do that. And in many teams still, it's considered so important that the teams invest in a team member with a testing emphasis. Some teams call that person a developer, but others may use the familiar term 'tester'.
