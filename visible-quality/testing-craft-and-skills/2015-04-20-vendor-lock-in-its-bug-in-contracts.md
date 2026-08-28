---
title: "Vendor lock-in: It's a bug in contracts"
date: 2015-04-20
updated: 2016-08-02
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2015/04/vendor-lock-in-its-bug-in-contracts.html
---

# Vendor lock-in: It's a bug in contracts

*Published 2015-04-20, updated 2016-08-02*  
*Source: <https://visible-quality.blogspot.com/2015/04/vendor-lock-in-its-bug-in-contracts.html>*

---

For years, the Finnish software and testing community has remembered a public failure in product quality. VR (the Finnish railways) had significant problems with a new system after go-live and VR together with their contractor Accenture was all over news on the problems.  
  
The talk of today is that the story has another turn: Accenture owns a core part of the source code this system is built on, effectively ensuring that no other contractor can deliver changes VR will need for the system. And the sum mentioned in press is 3 million euros.  
  
This is an example of vendor-lock in. There's something in contracts and the way the development has been set up that ensures the customer will have no other choice but to buy more services from the original vendor.  
  
In a Agile CxO open space within Agile Finland about half a year ago, I noticed that a common value companies discussing in the realm of agile contracting was to serve customers without creating a vendor lock-in. It came out so strongly, that it could almost be described a common value - believing no vendor lock-in is in the best interest of the customer. Software in agile is built with a change in mind.  
  
Over the years, I've experienced many examples of vendor lock-in:  

- No code comments: in a project delivered, code was uncommented. No one had *required* it needs to be commented.
- Undescriptive variable names: sure, calling variable with one letter alphabets is concise but not helpful trying to figure out what the code does.
- Choosing end-of-life open source component: in a project, the contractor drove a decision to use "tried-in-production" version where a newer was available, without mentioning that the newer existed as the old architecture wouldn't allow for changes needed - also for this customer.
- End-user pseudocode in specifying: having customer organization specify things in detail and translating that directly to code without code reuse by smart structures.

Vendor lock-in is a big bug in contracts between customers and contractors. It's a bug I've needed to report many times as a tester. It's a bug that I've been invited to remove before the contract is made, not only a bug with consequences to mitigate in acceptance testing phase. It can be a really expensive bug.    
  
Specifying in detail what is expected in contracts isn't helping. We need a change in mindsets: instead of the big contractors who repeatedly create intentional vendor lock-in, how about going for the smaller agile contracting companies.  
  
If you want to find out who those are in Finland, ask which companies were part of Agile Finland Agile CxO discussions. Get involved in that group as a customer. You might also learn ways of acquiring your software so that you get value in production earlier, more effectively and efficiently and not only right now in this project but actually designed with a change in mind: continuously.
