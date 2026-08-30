---
title: "Maaret Pyhäjärvi on Testing in the Modern Age"
show: "Semaphore podcast"
date: 2024-03-12
url: https://semaphoreci.com/blog/maaret-pyhajarvi
source_retrieved: https://semaphoreci.com/blog/maaret-pyhajarvi
kind: podcast episode
language: en
---

# Maaret Pyhäjärvi on Testing in the Modern Age

*Semaphore podcast — 2024-03-12*

Source: <https://semaphoreci.com/blog/maaret-pyhajarvi>

> Retrieval note: page text as published.

---
Testing safeguards the quality and reliability of products. And while there might be occasional misunderstandings, as in any collaborative environment, developers and testers are not inherently at odds. On this subject, veteran tester Maaret Pyhäjärvi believes in delivering feedback constructively.  In this episode, she will share her thoughts on the role of testers, how they can provide “the right kind of feedback” to developers, and how to navigate the nuances of different architectures and documentation practices.

## Edited transcription

A seasoned tester with over 25 years of experience in various testing and quality roles, Maaret Pyhäjärvi summarizes her role under the playful title of “feedback fairy.” “I come with the gift of feedback, with a smile on my face, with actual care on how people will receive the news,” she says. Knowing that feedback encompasses both positive and negative insights for improving organizations and products, Maaret clarifies that feedback “is not just about pointing out flaws, but also celebrating progress and potential”; and adds, “ It’s not only the bad news that your baby is ugly, it’s also the great news that it looks like things are improving, things are better today .”

## Testing and producing the right kind of feedback

Since getting feedback is the job of testers, they should have a certain skill set for providing the “right kind of feedback” to developers. First off, programming skills are a non-negotiable, as they allow testers to understand code, which is critical for grasping a product’s functionality. As Maaret puts it, if “ you can’t read code, you can’t get the information. ”

Secondly,  Maaret emphasizes the importance of testers understanding the domain, since this is what allows them to “recognize the gap between what the users want and expect.” The role of testers is to understand customer needs and ensure their expectations are met through the product, which can only be achieved by knowledge of the domain.

Lastly, testers have to thrive on collaboration, “being able to talk about this stuff with people who probably have a different background than you do yourself.” Testers should take initiative, speak up, and be comfortable with uncertainty.

Aside from the testers’ skill, Maaret emphasizes that the “right kind of feedback” goes beyond identifying issues, but uncovering the root causes behind these errors, and consequently, preventing them in the future. This requires a deeper understanding of the system and the user experience. Besides, the “right kind” of feedback, she suggests, should be integrated earlier in the process, potentially through unit testing, instead of through error messages that pop up to users. In this way, the “right kind” of feedback should be actionable and provide clear insights and suggestions that guide developers toward fixing problems and ultimately improve code quality.

## Holistic testing

Maaret strongly advocates for a holistic approach to testing, which she terms “contemporary exploratory testing.” What distinguishes “contemporary” testing from traditional, she explains, is its adaptability to modern practices, including automation: “ It would be silly to say that exploratory testing is somehow manual and doesn’t take into account the realistic CI, CD pipeline-based work that we have in pretty much any of the teams that are successful these days. ”

Secondly, contemporary testing is defined by collaboration and shared ownership within the team, using test environments and ensemble testing to collectively identify and resolve issues instead of prioritizing formal bug reports.

## Deployment types and times

The size of the user base significantly impacts the testing approach. As Maaret explains, with a smaller user base, there’s a higher chance of catching and fixing issues before they affect a large number of users, “but if you have a few million users, probably 50% of them will suffer before you notice your mistake.” Consequently, even in faster release cycles, there’s a need for rigorous testing to prevent critical problems from reaching the production environment.

But the notion that slower releases equate to higher quality might be flawed. For starters, due to security considerations, modern technologies require frequent updates: “Modern JavaScript isn’t really something that you don’t update frequently. You do have to.” Besides, Maaret argues that frequent, smaller updates based on a stable baseline allow faster issue identification and rollbacks: “I think there’s this weird idea that somehow people think that if we deliver less frequently, it’s somehow giving us the rigorousness like we have the time to do rigorousness. But actually, we have time to take more risks. […] So if you made a mistake, even if 50% of those millions will see that mistake if you can revert in five minutes, it’s a short thing that happened.”

## Testing monolith applications and microservices

Testing approaches differ between monolith applications and microservices. What matters in grasping this difference is adapting and understanding the nuances of each architecture. Testers, Maaret says, “have to understand APIs and be able to work with smaller pieces with an API;” besides, microservices’ granularity can benefit testing by facilitating understanding of potential impacts of changes and “makes it somewhat easier when you’re not trying to guess on an end-to-end level what might be the impacts.” Newer testers, she adds, are more likely to start with microservices “and then understand how that sits in a bigger picture.”

Similarly, having dedicated testing groups, where testers collaborate primarily with their kind, can potentially disconnect them from developers. In turn, breaking down testing groups, Maaret believes, fosters closer collaboration with developers.

While she recognizes that “product owners and development managers or engineering managers can hurt the testing culture a lot”, she believes “they can also promote the testing culture a lot,” acting as a bridge between testers and developers.

## Rethinking software documentation and customer feedback

Maaret recognizes several issues when putting together software documentation. starting by its size: “We write too much, which means there’s a cost of reading, all of that”. Hence, she believes it should focus on essential information that justifies its creation and maintenance cost.

Likewise, Maaret questions the value of documenting too early, when understanding is still limited and “we know less than what we would know by the time we have developed things.” To solve this issue, Maaret proposes documenting later when the most knowledge is available.

Maaret advocates for “paying attention to who’s reading stuff,” and only documenting what is truly useful, focusing on user needs. In this regard, it is possible to provide documentation, tailored to specific situations, within the context of the user interface. However, Maaret expresses concern about overwhelming users with too much information within the UI.

What’s more, potential improvements to documentation could address some of the customer support workload. Maaret identifies difficulty finding or understanding documentation as a recurring theme in customer inquiries:  “ ‘I don’t even know where to get started’, that type of question.”

However, Maaret also expresses reservations about the value of customer feedback. First, concerning its “high noise-to-information ratio,” the volume of irrelevant information with only occasional valuable insights. There’s also the issue of the lack of knowledge about what development teams can do. Maaret points out that “the distance between the development team and the support team often means that the support team doesn’t know when the development team would be having the power of actually changing the user’s experience.” As such, to review customer support, Maaret emphasizes the need for collaboration between development and support teams, “to build these bridges where we read that stuff together and pick up the important things.”

## The bottom line

Maaret actively shares her work on various platforms, offering different levels of detail and engagement:

- For the latest insights and unfiltered thoughts, follow her on Mastodon, @maaret@tivia.social .
- For in-depth articles and blog posts, visit her webpage, maaretp.com , and on DEV Community, dev.to/maaretp ; you can also search for her talks on YouTube.
- For curated content and professional connections Connect with her on LinkedIn: linkedin.com/in/maaret .

## Listen on your favorite podcast app
