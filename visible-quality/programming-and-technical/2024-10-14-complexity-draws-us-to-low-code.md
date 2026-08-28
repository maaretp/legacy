---
title: "Complexity draws us to low-code solutions"
date: 2024-10-14
theme: programming-and-technical
labels: []
source: https://visible-quality.blogspot.com/2024/10/complexity-draws-us-to-low-code.html
---

# Complexity draws us to low-code solutions

*Published 2024-10-14*  
*Source: <https://visible-quality.blogspot.com/2024/10/complexity-draws-us-to-low-code.html>*

---

If there is one conversation I find myself having ever since I became a test consultant this June, it is the one of clarifying the space of test automation tool options. There are options. Lots of options. And it is not the easiest of all things to make sense into the options.

Even if I simplify the options to free options and browser testing, I face the conversation of the three:

> Selenium, Playwright, or Cypress?

You may guess it, the conversation even with these is less obvious than you'd think. Selenium is driving a standardization effort, which means that while it supports WebDriver Protocol now, it is already supporting WebDriver BiDi on some of the languages. That is, things are changing under the hood in ways many people in browser automation space will want to pay attention to.

[![](../_images/screenshot-2024-10-14-at-18-00-07-01461529.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgINFdSyB652Eu3-jXPVl_yQKFohcuceG9qJbUUkTMu4GvFmQcn2mDeriumABlLRu5u3PDjKDnFucySDSlPLTdDcmZCCJ9gNpbCvMOIwdoWU-fVPPo8vvXknolmaAdPhxe7DY0EnpmQrqPVy7Ov835hpOnK2MrOcEWKMvF0gdxdAqg1hjerLlZ0a5v6A/s1638/Screenshot%202024-10-14%20at%2018.00.07.png)

Watching things within the Playwright repo going on in pull requests, it looks like Webdriver BiDi is finding its way into Playwright too. And when that happens, it is an essential change on the overall landscape.

For now with using CDP, there is the definite need of regularly emphasizing that Chromium is not Chrome nor Edge. Webkit is not Safari. Playwright and Cypress, running on CDP don't do real cross-browser testing. The approximation may be sufficient. Single browser testing may be sufficient. But for now, you would need something based on WebDriver Protocol (like Selenium) if you wanted to automate for the browsers your users are using.

[![](../_images/screenshot-2024-10-14-at-8-58-19-0226313c.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZZ6JOHtBS0qsuMQ13aUnjvjJ6g53fAAI6TchOxxo-teJTZOvmh82-v9R8QXBsP-2rS3KIyuYBE6W_ydqJYNNbYgfxJ2xSX1loNuXmaedyPImrKfGXDccqGKh-6TyJBctVvGOk3WFRNS7_mHGIVTCP2Trdg7Pa3U_tAffRLVGvBJgH21SSNN39BGCjlw/s948/Screenshot%202024-10-14%20at%208.58.19.png)

To make matters more complicated, the three are not the only options. In the Selenium ecosystem for **testing** purposes, the recommendation is to use one of the frameworks built on top of it like Nightwatch or SeleniumBase or frameworks using WebDriver Protocol without using Selenium like WebdriverIO. Then again, using Selenium as the driver for any and many commercial tools is also an option, and you might not even know what powers the framework under the hood. There's layers.

[![](../_images/screenshot-2024-10-14-at-8-58-58-948c678b.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgarvZyhQH0iia2U1vwRZ89tShsfuGScXMDOfqTGDjMhxCSKRosz1Y2smMLUZmERTnc12mVoYYhLsn9MsGFTUKa88ixeFSIAnjCmu5DIncr1fa8LQGgdP8ZJGT-ghHIZ1UTEytAFECcCJYYcPRVs3GKsB4u0A5AgSzVToOov4SjHC7WT9U461EphjekbQ/s924/Screenshot%202024-10-14%20at%208.58.58.png)

  

And features.

[![](../_images/screenshot-2024-10-14-at-17-51-30-5876afb3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYFFzYGZXeM9sF9-SZppricsy-Tew7CQcqbfSA1kwsnrfI_sWJZfDrRhyetdRqKCf0d9KKbxlDRgz4Qa04MoqV7iSaCZi9Yz7cfZQNcGENh-Q2whi3dFkx73_I3adZYlZUrgBF8UA-bYMo-kDPWtSCwy3Us0vWD-5bAHcERxPdMrqnx0s0ejfZKi1Jkg/s1176/Screenshot%202024-10-14%20at%2017.51.30.png)

However, when we talk about these tools, we don't talk about the layers or features. We talk about naming the tools, leaving it for the reader to figure this all out.

[![](../_images/screenshot-2024-10-14-at-18-29-13-50aebfc9.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9Rw9VGFKkH6yXsfuwj7m3e45vQLAViWmuJNKKa2EkEfz0ZdUfFJnXMEkoEEcdKCc2CPEwBeU4TyJGdCRvvWdspSMUrgiH7xRwj6uFLrKpGlinfGmgVkxQmmZc9KWhjgWUgZEnKjmLvfKGRxHcqio6HJfKUtnSB3-RxeoFjYmnXpAlsSgQ7fz4xNKrVQ/s1198/Screenshot%202024-10-14%20at%2018.29.13.png)

The main benefit I find from low code platforms is their closed nature. You don't have to care what is outside the box and you have no control what is inside the box. It probably boxes in things you need to do testing. It simplifies the world. Instead of reading and making sense of all this and all the change to this, you can focus on the work of testing.

Sometimes we argue about the tools so much that focus gets lost. We live with our choices long, and keeping things open has, in my perspective, more value than the simplification.
