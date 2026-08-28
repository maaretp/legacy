---
title: "Our Three Ways to Beta"
date: 2019-10-25
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2019/10/our-three-ways-to-beta.html
---

# Our Three Ways to Beta

*Published 2019-10-25*  
*Source: <https://visible-quality.blogspot.com/2019/10/our-three-ways-to-beta.html>*

---

Working in a product company, the term "beta testing" we pass around in testing certifications actually has meaning and relevance to us. But while you can find a vocabulary definition to it, the real life with what it means is much more interesting and versatile. So let's look at three products and their three ways to do beta.  Each product version when fully taken to use means installation to computers counted in millions so set your eyes away from that one server and think about building something where distributing and installing is a major effort split between the user ("acceptance testing") and the product ("all testing") organizations.   
  
**Product A**  
  
Product A is targeted for big organizations and whether it is true or not, the day to day is filled with change avoidance, change control and unwillingness to take new versions into use. Product A version the customers have today is *good enough* as in not causing trouble, and there is no pull to move forward. Every move forward is work that includes acceptance testing of a new version of product A in whatever specifics each customer has around that ensuring standards around disallowing untested (by the customer organization separately) software to sneak into production.  
  
Because releases are work and hard and to be avoided, the product A works with a very traditional release cycle. You can expect to see an annual cycle of planning to be set around the idea that there are two major releases and 2 minor releases. The customers recognize that a version with x.00 is always the major one and as it introduces new major features and changes, you should avoid it employing a conservative strategy. The minor releases, x.01 customers recognize for having what x had, but fixes from the first brave customers, with history showing that the conservative strategy is worth the wait.  
  
With only a few releases a year, each release introduces thousands of changes even if the list of visible new things is only a few items per release. The risk accrued on not releasing is a realistic threat that the customers of the product experience because as hard and well as the product A team tests, the real operational environment is always more versatile and use cases more surprising that a test lab can simulate.  
  
When product A does beta, it is *a schedule milestone* and *warning of uncertain / low quality for customers*, a release on top of the four releases. When you add two the two major versions a beta each, you have total of 6 releases a year! And if anyone takes a look at the beta version finding out it does not work in customer environments (again, product team tests hard in test lab before!) the features available for that release could already be somewhat improved for by time of the major release being "RTM" (release to manufacturing). Time between beta and RTM is not for bug fixing though, it is for the second batch of features that never see a beta. Sometimes when the stars align, testing and fixing work happens during this beta instead of running with the next batch of features.  
  
The beta exists to enable a user organization to start their acceptance testing early but no one would expect it to end up in wide production use. That's what the major and minor versions are for.  
  
**Product B**  
  
Product B is targeted for big organizations too, but the big organizations serve a more individualistic user base. Major and minor releases work very similarly, with annual planning cycle seeing two of each but their size on effort allocated is different. They are not projects where one follows the other, but usually a new major release starts as previous goes out, and a minor release happens on the side. A significant difference comes with size of minor releases, that product
B minimizes. Most of fixes are seen within major releases and going out only in the next major release, and doing a
minor release is an effort to minimize the scope whereas product A sees
it more as a maximizing the scope to get anyone to move to a new
release.  
  
The customer sentiment around what a major and minor release means is very much the same as with product A but there is slow yet significant pull to get the major releases out for real users to use. There is some avoiding of change as it is still a project, but it is considered a little less arduous.  And then there is some of exact symmetry of how product A customers would behave, but that is in the minority.  There's rules in place on how many versions are supported, which supports the slow pull.   
  
When product B does beta, it's a *pulse release* assessing quality continuously, every two weeks. Whatever can be used internally, can be used externally for a selected group of thousands of users. Beta is more of a way of paying for product by telling if it fails, and it very rarely fails in ways users see. Meanwhile it is possible to see ways of failing users don't see through telemetry.  
  
When a release is made available, every single feature it includes has been out in beta. People have been asked specifically about those changes. Some things have been in beta for 6 months, others two weeks. A RTM schedule depends on key features (major risks) having enough time in beta to assess feedback and RTM quality is solid enough so that major releases are regularly considered for use.    
  
**Product C**  
  
Product C is targeted for medium sized organizations but lives in a service space where continuous changing of software is already more acceptable practice for customers. Since it is a service, moving from a version to another is in theory invisible to the user organizations, and they've been stripped from possibility to control it. New stuff comes with a cadence that does not show up even as a need to reboot. There are no major and minor releases, just releases every 2-4 weeks.  
  
When product C does beta, it's a *time to cancel wider distribution*. It's not called beta really, but "early access" (external customers) and "pilot" (internal customers). The time for beta is one week before full availability, and as with product B, things run more on telemetry and seeing failure than hearing back from a real user seeing problems.  
  
**Do the differences matter?**  
  
The differences cause some confusion as one product's beta is not another product's beta, and the rules around how to schedule are very essentially different. As a tester, I would never want to go back to product A style of working and from my experiences in continuous delivery as transformative practice, both B and C have a lot of similarities.  
  
It's now been 12 years since I moved product B to the pulse style continuous beta. I've played a central role in defining product C taking the practices further, ensuring the best software we have created is running as a service on the customers machines.  
  
I work from the idea that in the security business of *defence*, we need to move fast because the *offense* definitely is. The end users may not understand all the details of what we defend them against, but working with those details day in and day out, I know in my heart the speed matters. Even more in the future than today.
