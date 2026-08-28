---
title: "Access to code: denied?"
date: 2015-09-11
updated: 2016-08-02
theme: programming-and-technical
labels: []
source: https://visible-quality.blogspot.com/2015/09/access-to-code-denied.html
---

# Access to code: denied?

*Published 2015-09-11, updated 2016-08-02*  
*Source: <https://visible-quality.blogspot.com/2015/09/access-to-code-denied.html>*

---

I started in a new company three years ago, as the first tester in the teams. There was a lot to test. There were a lot of problems to be found and reported. I easily spent my time on the applications without ever getting it all done anyway.  
  
I remember my manager asking me if I needed Visual Studio (license) back then, with a premise that I don't. I had not had access to code before (except that I would ask developers to show me stuff), so I wasn't thinking I would need it now.  
  
There were these occasional struggles, when there would be changes I did not know of as no one told me. I could have seen the checkins, if I had the tools. I was also struggling with typos that people did not feel like fixing, that would take a significant portion of my energy as I just cannot pass them without slowing down just a bit. Easy fixes that I got tired of waiting for.  
  
I started looking into my options several months into the job. At this point, it was established that developers would have Visual Studio but I wouldn't. So I installed the free version, looked up a few blog posts on how to get things set up and got myself access to the code repository. That was simple, just ask as the access was controlled in our teams. Developers were more than happy to reorganize the way we did things to whatever I found I wanted to volunteer for.  
  
I quickly learned the places to go to to fix the typos, and haven't reported one since as I fix them faster. I learned to start the builds whenever I needed to. I created a habit of spying on commits, mostly on level of comments attached to them, but also into the code that was actually changed. I started reading code that was created, just because I could.  
  
Again time passed, and we realized that I wouldn't actually be allowed to use TFS with my free version of Visual Studio. While it can be done, it's not what you're allowed to do as per license agreements. And I got "promoted" into the real tools of the trade. They didn't just give me Visual Studio Professional, but I got also ReSharper. Toolwise, I was where the developers were.  
  
Months passed, and I used the paid version just as I had used the free version. Our builds changed from on-demand (which I would just run whenever there was a change, why would I waste time on testing something old that wouldn't go to production anyway) to continuous. And our monthly releases changed to daily, whenever there was something that was ready doing features one by one. I would deal with a lot of the merges and keeping track of what is in the versions.  
  
Then I wanted to work on unit tests. And you really can't work on unit tests without refactoring the application while adding the tests. I needed to build the application. It did not build in my environment, there was a significant struggle to understand from errors I was getting that something wasn't installed. But I got there.  
  
I had forgotten many of these steps, as things changed a little by little until I was reminded that the case still often is that access to code for testers is denied and that many of us still hunt for the information about the changes that we should know of. Having the access creates opportunities for better testing to happen. Why shouldn't we have that door open?
