---
title: "Stop Expecting Rules"
date: 2023-04-26
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2023/04/stop-expecting-rules.html
---

# Stop Expecting Rules

*Published 2023-04-26*  
*Source: <https://visible-quality.blogspot.com/2023/04/stop-expecting-rules.html>*

---

Imagine having a web application with a logout functionality. The logout button is on the top LEFT corner. That's a problem, even if your requirements did not state that users would look for logout functionality on the top RIGHT corner. This is a good example of requirements (being able to logout) and implicit requirements (we expect to find it on the right). There are a lot of things like this where we don't say all the rules out loud.

At work, we implemented a new feature on sftp. When sftp changes, I would have tested ftp. And it turns out that whoever was testing that did not have a \*test case\* that said to test ftp. Ftp was broken in a fairly visible way that was not really about changing sftp, but about recompiling C++ code to make a latent bug of 2009 now visible. Now we fixed ftp, and while whoever was testing that now had a test case saying to testing sftp and ftp as a pair, I was again unhappy. With the size of the change to ftp, I would not waste my time testing sftp. Instead, I had a list of exactly 22 places where we had the sonar tool identify problems exactly as this used-to-be-latent one, and I would have sampled some of those in components we had changed recently.

Search of really simple rules fails you. If you combine two things for your decision, the number of parameters is still small.

In the latter case, the rules are applied for a purpose of optimising opportunity cost. To understand how I make my decisions - essentially exploratory testing - would require balancing the cost of waiting another day for the release, the risks I perceive in the changes going with the release, the functional and structural connections in a few different layers. The structural connection in this case had both size and type of the change driving my decisions on how we would optimize opportunity cost.

I find myself often explaining people that there are no rules. In this case, it would hurt timelines for maybe a few hours to tests ftp even when those few hours would be better used elsewhere. The concern is not so much on the two hours wasted, but on not considering the options of how that two hours could be invested - on faster delivery or on better choice of testing that supports our end goal of having an acceptable delivery on the third try.

A similar vagueness of rules exist with greeting people. When two people meet, who says hello first? There are so many rules, and rules on what rules apply, that trying to model it all would be next to impossible. We can probably say that in a Finnish military context, the rank plays to the rules of who starts and punishment of not considering the rules during rookie season is teaching you rule following. Yet the amount of interpretations we can make on other's intentions when passing someone at the office without them (or us) saying hello - kind of interesting sometimes.

We're navigating a complex world. Stop expecting rules. And when you don't expect rules, your test cases you always run will make much less sense than you think they do.
