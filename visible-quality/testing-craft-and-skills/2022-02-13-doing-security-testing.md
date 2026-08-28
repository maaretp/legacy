---
title: "Doing Security Testing"
date: 2022-02-13
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2022/02/doing-security-testing.html
---

# Doing Security Testing

*Published 2022-02-13*  
*Source: <https://visible-quality.blogspot.com/2022/02/doing-security-testing.html>*

---

This week Wednesday, as we were kicking off BrowserStack Champions program with a meeting of program participants around a fireside chat, something in the conversation in relation to all things going on at work pushed an invisible button in me. We were talking about security testing, as if it was something separate and new. At work, we have a separate responsibility for security, and I have come to experience over the years that a lot of people assume and expect that testers know little of security. Those who are testers, love to box security testing separate from functional testing and when asked for security testing, only think in terms of penetration testing. Those who are not testers, love to make space for security by hiring specialists in that space and by the Shirky Principle, the specialists will preserve the problem to which they are a solution.

Security is important. But like with other aspects of quality, it is too important for specialists. And the ways we talk about it under one term "security" or "security testing", are in my experience harmful for our intentions of doing better in this space.

Like with all testing, with security we work with \*risks\*. With all testing, what we have at stake when we take risk can differ. Saying we risk money is too straightforward. We risk:

- other people's discretionary money, until we take corrective action.
- our own discretionary money, until we take corrective action.
- money, lives, and human suffering where corrective actions don't exist

We live with the appalling software quality in production, because a lot of the problems we imagine we have are about the first, and may escalate to the second but while losing one customer is sad, we imagine others in scale. When we hear RISK, we hear REWARD in taking a risk, and this math works fine while corrective actions exist. Also, connecting testing with the bad decisions we do in this space feels like a way of the world, assuming that bug advocacy as part of testing would lead to companies doing the right things knowing the problems. Speaking with 25 years of watching this unfold, the bad problems we see out there weren't result of insufficient testing, but us choosing the RISK in hopes of REWARD. Because risk is not certain, we could still win.

The third category of problems is unique. While I know of efforts to assign a financial number to a human life or suffering, those don't sit well with me. The 100 euros of compensation for the victims of cybercriminals stealing psychotherapy patient data is laughable. The existence of the company limiting liability to company going bankrupt is unsettling. The amount of money police uses investigating is out of our control. The fear of having your most private ideas out there will never start to spark joy.

Not all security issues are in the third category, and what upsets me about the overemphasis of security testing is that we should be adding emphasis to all problems in the third category.

A few years ago I stepped as far away as I possibly can from anyone associating with "security" after feeling attacked on a Finnish security podcast. Back then, I wrote a post discussing the irony of my loss / company's loss categories proposing that my losses should be the company's losses by sending them a professional level services bill, but a select group of security folks decided that me running into a problem where it was a company's loss, ridiculing my professionalism was a worthwhile platform. While I did report this for slander (crime) and learned it wasn't, the rift remains. Me losing money for bug: testing problem. The company losing money for bug: security problem. I care for both.

As much as I can, I don't think in terms of security testing. But I have a very practical way of including the functional considerations of undesired actors.

We test for having **security controls***.* And since testing is not about explicit requirements but also ensuring we haven't omitted any, I find myself leading conversations about timing of implementing security controls in incremental development from perspective of risks. We need security controls - named functionalities to avoid, detect, counteract and minimize impacts of undesired actors.

We test for **software update mechanism.** It connects with security tightly, with the idea that in a software world riddled with dependencies to 3rd party libraries, our efforts alone without the connected ecosystem are in vain. We all have late discoveries despite our best efforts but we can have the power of reacting, if only we are always able to update. Continuous delivery is necessary to protect customers from the problems we dropped at their doorstep, along with out lovely own functionalities.

We test for secure design and implementation. **Threat modeling** still remains an activity that brings together security considerations and exploratory testing for the assumptions we rely our threat modeling decisions on as a superb pair. Secure programming - avoiding typical errors for a particular language - shows up as teams sharing lists of examples. Addressing something tangible - in readable code - is a lot more straightforward than trying to hold all ideas in head all the time. Thus we need both. And security is just one of the many perspectives where we have opportunities to explore patterns out of the body of code.

We integrate **toolsinto pipelines**. Security scanners for static and dynamic perspectives exist, and some scanners you can use in the scale of the organization, not just a team.

We **interpret standards**for proposals of controls and practices that the whole might entail. This alone, by the way, can be work of a full time person. So we make choices on standards, we make choices of detail of interpretation.

We **coordinate reactions**to new emerging information, including both external and internal communication.

We **monitor the ecosystem** to know that a reaction from us is needed.

We **understand legal implications as well as reasons**for privacy as its own consideration, as it includes a high risk in the third category: irreversible impacts.

And finally, we may do some **penetration testing**. Usually for the purpose of it is less of finding problems, but to say we tried. In addition, we may organize for a marketplace for legally hunting our bugs and selling our bugs with high implications to us over the undesired actors, through a **bug bounty** program.

So you see, talking about security testing isn't helpful. We need more words rather than less. And we need to remove the convolution of assuming all security problems are important just as much as we need to remove the convolution of assuming all functional problems aren't.
