---
title: "A Bunnycode Case Study for AI in Testing"
date: 2024-03-05
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2024/03/a-bunnycode-case-study-for-ai-in-testing.html
---

# A Bunnycode Case Study for AI in Testing

*Published 2024-03-05*  
*Source: <https://visible-quality.blogspot.com/2024/03/a-bunnycode-case-study-for-ai-in-testing.html>*

---

It's day 5 of 30 days of AI testing, and they ask for reading a case study or sharing your experience. I did sharing experience already on an earlier day, and in the whim of a moment, set up a teaching example.

I google for obfuscated code in python to find <https://pyobfusc.com/>. I'm drawn to *most reproducible**,* authored by [mindiell](https://pyobfusc.com/submissions2023/4158721484/) and when I see the code, I'm sold. How would you test this?

[![](../_images/screenshot-2024-03-05-at-11-35-52-ae732232.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidxirwRam59ewTN-7mRXCkwadFdPlAlRxI6co6dwxxrMGIvEGft1hZHyMudWFPs5l2xoYGhmYzrhDGyujgHkUAAoH6fK0TrG9oa_eZPQNUGpe18Qs3Vab40TE4yGpx2QM17OQuxnuxTbDOB3mQyF8GeH7NGg2cCrLHemZnhyphenhyphen_FZRiVPzTQpD7qGhsD2w/s722/Screenshot%202024-03-05%20at%2011.35.52.png)

Pretty little rabbit, right? Reminds me of reading some code at work, work is just less intentional with obfuscation. And really do not have the time or energy to read that. I could test it as black box, learning that given a parameter of a number, it gives me a number:

[![](../_images/screenshot-2024-03-05-at-21-24-59-c0430580.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMBq_aA2AUMZ-pvMEAnFcXU3ljNE_9whHkpATHr2lNX0gjnA1Qmlk4NvWtkZvV5YJoYB1Ozg7mMgqYuZav16zKVNs-qfuMxd4-7OWLjrF2BllMUIctGuDX8LfmfxqbKYuBgpj93DGolrdDw4KV-EgAA_GRujR4L3LV6RyGyG1zjRijHAPJPwljduRJ7A/s439/Screenshot%202024-03-05%20at%2021.24.59.png)

As if I didn’t know what the rabbit implements or recognize the pattern in the output, I was thinking of just asking ChatGPT about it. However, I did not get that far.

Instead, I wrote **def function():** on my IDE while GitHub copilot is on, thinking I would have wrapped the program into a function. It reformatted it to something a bit more readable.

[![](../_images/screenshot-2024-03-05-at-21-31-17-26d4d439.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgL_RBJUBmudv8JI-ycLM0wf9FbQthbKRtd0vTnqskW33gQp5GxbGHO0fRO_B_wNoUcJnZ2om-EZwX7zqdkXchyvn3PmgZDFzNam65e_yU8cRQ6uxTwYTdTooKavMb8f-Cre1gOiAw9esTLvUWmMQidW-WfZ1L4Dc2P4L7g6cgFbj1SOU4iHx-xhnsvyA/s1069/Screenshot%202024-03-05%20at%2021.31.17.png)

  
Prompting some more in the context of code.

Comment line “#This function” proposes “is obfuscated”. Duh.

Comment line “#This function imp” proposes "lements the Fibonacci sequence using Binet’s formula.

At this point, I ask chatGPT how to test a function that implements the Fibonacci sequence using Binet’s formula. I get long text saying try values I already tried, but in code, and a hint to consider edge cases and performance. I try a few formats to ask for a value that would make a good performance benchmark, and lose patience.

I google for performance benchmark to learn that this Binet’s formula is much faster than the recursive algorithm, and find performance benchmarks comparing the two.

I think of finalizing my work today with inserting the bunny code into chatGPT and asking “what algorithm does this use” to get second language model generate likely answer as the Binet’s formula. Given the risk and importance of this testing at this time, I conclude it’s time to close my case.

There are so many uses to figure out what it is I am testing (while being aware of what I can share with tool vendors when giving access to code) and this serves as a simulation of idea that you could ask about the pull request. This was the case I wanted to add to the world today.

I should write a real case study. After all, that was one of the accommodations we agreed with multiple levels above me in management when my team at work started GitHub Copilot tryouts some 6 months ago. I should publish this in action, with a real time. As soon as something generates me some time.
