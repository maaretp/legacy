---
title: "Life after GDPR"
date: 2018-07-23
updated: 2018-12-26
theme: agile-teams-and-process
labels: [Agile]
source: https://visible-quality.blogspot.com/2018/07/life-after-gdpr.html
---

# Life after GDPR

*Published 2018-07-23, updated 2018-12-26 · Labels: Agile*  
*Source: <https://visible-quality.blogspot.com/2018/07/life-after-gdpr.html>*

---

In the last year, offices around the world have been like mine, buzzing with the words GDPR. The European Global Data Protection Regulation became active and enforceable in May.  
  
It's not like *privacy* of our users did not matter before. Of course it did. But GDPR introduced concepts to talk around this in more detail.  
  
It assigned a monetary value of not caring that should scare all of us. An organization could be penalized with a fine of 4% of the companies global annual turnover or 20 million euros, which ever is greater.  
  
It introduced six requirements:  

- Breach Notification - if sensitive data gets leaked, companies can't keep this a secret. And to know that there was a breach, you need to know who has been accessing the personal data.
- Access to Your Data - if anyone has data of you, asking should give it to you, without a cost.
- Getting Forgotten - if the original purpose you consented changes or you withdraw your consent, your data needs to be removed.
- Moving Your Data - if you want to give your data elsewhere, they should provide it in a machine readable format.
- Privacy by Design - if there's personal data involved, it needs to be carefully considered and collecting private data in case isn't a thing you can do.
- Name Someone Responsible - and make sure they know what they're doing.

Getting ready for all of this has required significant changes around organizations. There's been needs of revising architectural decisions like "no data should ever be really deleted". There's been refining what *personal* really means, and adding new considerations on the real need of any data belonging into that category.

In a world where we build services with better, integrated user experience, knowing our users perhaps with decades of knowing their personal patterns and attributes, we are now explicitly told we need to care.

So as a tester, looking at a new feature coming in for implementation, this should be one of your considerations. What data is the feature collecting, combining to, and what is the nature of that data? Do you really need it, and have you asked for consent for this use? Did you cover the scenarios of asking for the data, moving the data or actually getting the data deleted on request?

For us testers, the same considerations apply when we copy production data. The practices that were commonplace in insurance companies like "protected data" are now not just for the colleagues data, but we need to limit access and scramble more. I suspect the test environment have been one of the last considerations we addressed with the GDPR projects in general, already being schedule challenged just to get minimally ready.

We should have cared before, but we should in particular care now. It's just life after GDPR came to action. And GDPR is a way of decoding some rules around agency of individual people in the software connected world.
