---
title: "Stop paying users, start paying testers"
date: 2020-11-23
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2020/11/stop-paying-users-start-paying-testers.html
---

# Stop paying users, start paying testers

*Published 2020-11-23*  
*Source: <https://visible-quality.blogspot.com/2020/11/stop-paying-users-start-paying-testers.html>*

---

At work when I find a bug, I'm lucky. I follow through during my work hours, help with fixing it, address side effects, all the works. That's work.

When I'm off work, I use software. I guess it is hard not to these days. And a lot of the software recently makes my life miserable in the sense that I'm already busy doing interesting things in life, and yet it has the audacity of blocking me from my good intentions of minding my business.

Last Friday, I was enjoying the afterglow of of winning a major award, bringing people to my profile and my book, only to learn that my books had vanished from LeanPub. One the very day I was more likely to reach new audiences, LeanPub had taken them down!

After a full excruciating day of thinking what was it that I did wrong to have my account suspended for authorship, LeanPub in Canada woke up to tell me that I had, unfortunately, run into a "rare bug". Next day I had my books back, and a more detailed explanation of the conditions of the bug.

If I felt like wasting more of my time, I guess I could go about trying to make a case for financial losses.

- It took time of my busy day to figure out how to report the bug (not making it easy...)
- It caused significant emotional distress with the history of one book taken down in a dispute the claimant was not willing to take to court
- It most likely resulted in lost sales

But overall, I call my losses, and turn it into a sharable story. Issues with software are something to pay attention to, and I can buy into the idea of this being rare in the sense that it was probably hard to catch and they were quick to react on it.

Next day, I decide its time to buy a new domain name, and I go to Hover, where all my services are hosted in a nice bundle. I own a dozen domains. That is how I start new projects. Sometimes, the annual process of deciding if I want to still pay for a domain is my best way to manage hobby projects.

I try to log in. And I fail with a 404 error. Like a good user, I refresh, and continue my day without reporting. I don't want to spend time on this, I just want to get things done without all these hiccups.

These two issues are functional bugs, meaning bugs that inconvenience the user, one more significantly than the other. They have very little impact on the company, and the better companies are like LeanPub, making the bug go away fast when it is actually blocking.

There is a third functional bug that I stumbled upon, in the very same way as all these other functional bugs. But this functional bug is what they call "exploitable". That basically means that it can hurt the company, not just the user. Sometimes exploitable bugs are about money, like this one was. Sometimes exploitable bugs are about secrets, like Vastaamo problem was. Exploitable bugs are of special interest to folks in security, and they are bugs with a particular priority to folks in software testing.

Just like with the two other bugs, I was minding my own business, not testing in anyone's production. I wanted to buy food delivered, and I used the Foodora app.

First time I saw this bug, the symptoms were subtle to me. I received two confirmation emails. I received a phone call from the pizzeria I ordered from asking if I ordered two meals. I had a pleasant conversation with the pizzeria guy about this happening often that orders were duplicated, as pleasant as a conversation I don't want to be in can be. And I received one meal, just what I ordered. Because while I was a user, I'm also a tester and a particularly observant one, I knew what I had done to trigger the condition. I was not planning on doing it again. So I tweeted a wide characterization with no repro steps to vent my frustration on software getting in my way.

Ordering takeaway food as much as I do, it was only a matter of time before it happened again. This time I had my whole extended family over, and it was a fairly large order. Yet this different restaurant apparently did not know the issue, and delivered two full sets of food at my doorstep. With yet another inconvenient discussion with someone I did not want to meet at my doorstep, the driver took the other set of food away with him. I was inconvenienced, more than the previous time. I tweeted about Foodora needing to fix their bug, and searched their web page to contact with no luck. So I let it be. Someone asked me for steps to repro, alerting me to the idea that I might have to waste my time on this eventually.

Third time was the charm. I still don't want to reproduce this bug, and despite my best efforts, it happened AGAIN. Already upset at the idea of having to have the conversation of what I ordered and didn't, I just took the food they delivered and complained they delivered me two sets of my order billing only one. With the proof of order numbers and payments, I assumed they could track it and get it fixed. Their loss, they should care. I mentioned that if they did see my feedback and needed help, I would be happy to tell tell them exactly what causes it. I didn't feel like writing long step-wise instructions into the void. I spent more of my energy in establishing credibility in knowing that this is a bug than on anything else. Because, that is what testers find they need to do when they report. Dismissing feedback is regular.

Weeks passed, they contacted me. I wrote them the steps. Weeks passed, they contacted me. They said thank you, that they had the issue addressed with their tech folks, and gave me, the user, 10 euros.

I write a shorter version of the story on my LinkedIn wall, only to learn how the cyber community (some outskirts of it, at least), misrepresents what I say:

- Someone claimed I was "testing in production" because through my profession, I couldn't be a user.
- Someone claimed I was "testing without consent" because I wasn't part of a bug bounty in finding this
- Someone claimed that I was breaking the law using the software with a vulnerability hitting the bug
- Someone claimed I was blackmailing Foodora on the bug I had already reported, for free, expressing to them I was not doing this for money in our communication
- Someone claimed I was criminally getting financial benefit of the bug
- Someone claimed the company could sue me, their user, for libel in telling they had a bug
- Someone claimed I was upset they did not pay me more, not on the fact they didn't pay a competent tester in the first place (I know how to get to the bug, I would have found it working for them - exploratory testers couldn't avoid it, automation only strategy or test cases could)
- Someone claimed I was eating on the company's expense, when I was reporting on 200 euros of losses (for food they had thrown away)

You may already sense that I think these claims are poppycock. But these types of claims are very typical for anyone with a larger follower base - I'm great platform for both security marketing effort but apparently also restaurants telling me they still want me as their customer.

Today I listened to Turvakäräjät podcast, only to learn I made appearance as a "reputable tester" on this security podcast in Finnish. They really got their alternative facts straight: eating on others' expense (not that I had to pay for every order I made, there was no free meal ever, only duplicate to go to waste) and being upset over 10 euros bounty.

Let's reiterate this one more time.

There is no money in the world that I would be willing to sell my free time on to test their software with a zero sum contract that only pays when I find problems. I think bug bounty programs and crowdsourcing are unethical, and would not take part in results-only payment models. I struggle with ethics of companies like Foodora that don't treat their drivers as employees, but I use them because I have nothing better in times I don't want to leave home for food. My ethics are important to me.

There is no money in the world that would compensate stealing my time on bugs, exploitable or not. The bugs are not the users responsibility, even if sometimes users hands are tied, and waiting or leaving are not real options.

There is no ethical obligation for me to report even exploitable bugs as a user. The ethical obligation I take on me is not to share a vulnerability further. Knowing impact does not mean knowing the mechanism. And I write about the impact vaguely to protect the buggy party. I delay big visible posts to times when they won't have extra harm on my account.

I say don't pay the user, paying users 10 euros is an insult to the users. Hire a professional, and note that the professionals don't work for peanuts.
