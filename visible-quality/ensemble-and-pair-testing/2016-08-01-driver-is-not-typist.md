---
title: "Driver is not a typist"
date: 2016-08-01
updated: 2017-07-22
theme: ensemble-and-pair-testing
labels: [Mobbing]
source: https://visible-quality.blogspot.com/2016/08/driver-is-not-typist.html
---

# Driver is not a typist

*Published 2016-08-01, updated 2017-07-22 · Labels: Mobbing*  
*Source: <https://visible-quality.blogspot.com/2016/08/driver-is-not-typist.html>*

---

I listened to a talk today on [How Agile and OO have lost their way](https://www.youtube.com/watch?v=DOyNfmqwR98&app=desktop) by James Coplien. At around 48 minutes into the video, James introduces Mob Programming.  
  
"One of the very exciting things I've seen emerge recently is Mob Programming ... Kind of like pair programming, except it's the entire team. *You have one person at the keyboard, they may not think, they may not talk*. They only type. You have a facilitator, and the rest of the team writes the code and tells the typist what to write. Then you swap roles every few minutes."  
  
We (myself & Llewellyn Falco) teach strong-style pair programming, especially in mob programming with the phrase "no thinking on the keyboard" that I've considered dangerous. I've recently observed many misunderstandings from this, and softened the expression to "no decisions on the keyboard". Thinking is allowed, encouraged even. Talking back to the navigators is allowed, encouraged even.  
  
Seeing how James frames Mob Programming driver role as "they may not think, they may not talk", I feel the need to thinking about how to communicate this better.  
  
Woody Zuill talks about a dumb input device (the keyboard) and the smart input device (the driver). The smart input device is not a typist, but a translation. The person on the keyboard primarily translates intent like "we'll need an invoice class" or "there should be a method for creating new employees" into implementation. The driver is navigated on the highest abstraction level possible, and has a lot of power in the order and details of implementation. If the navigators disagree on the choices, a discussion emerges through the continuous review. And if the driver is a beginner as programmer, the navigators drill down in the navigation instructions to the level the driver needs.  
  
Within just a few hours, you see a newbie move from "type var" into "we'll need a variable to store the employee info" in the instructions. Details and typist-level instructions are momentary, and the option we revert to when the driver needs it and we move beyond typing quickly.
