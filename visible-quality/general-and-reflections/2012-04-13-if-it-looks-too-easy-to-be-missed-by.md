---
title: "If it looks too easy to be missed by developers..."
date: 2012-04-13
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2012/04/if-it-looks-too-easy-to-be-missed-by.html
---

# If it looks too easy to be missed by developers...

*Published 2012-04-13*  
*Source: <https://visible-quality.blogspot.com/2012/04/if-it-looks-too-easy-to-be-missed-by.html>*

---

On my first weeks at new job, I've had the pleasure of reporting bugs again. I find this particular result of testing to give me the feeling of achievement. The more relevant the problem, better.   
  
There was one bug I reported on Monday, that just looked too easy to be missed by the developers in my team. As I originally reported it, the problem was that when logging in with one of our three main browsers, there's a highly visible error message. And that this seems to happen only with the recent builds, not in production version.   
  
In the end of the week, I quickly asked in passing the developer whose component was failing, if a fix is available in the next weekly build. He seemed puzzled: what problem, what fix? I checked our Jira, and the issue had not been addressed - which is quite normal. He took a quick look at it, and came back with "I didn't change this for ages" with some details.   
  
I started testing the issue more with the information from him. With fresh eyes, I realized I entered the program from a bookmarked link - something I hadn't mentioned in my original report. I also realized, that I had different addresses bookmarked in the other browsers. So I had missed a relevant bit of info I provided now.   
  
Bottom line: if it looks too easy to be missed by developers, it may be that they didn't test, but in this case, I missed relevant factors that are needed to get the bug visible.  Talking sooner than later to the very busy developers is still a good idea.
