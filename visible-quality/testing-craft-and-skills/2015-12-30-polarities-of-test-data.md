---
title: "Polarities of test data"
date: 2015-12-30
updated: 2016-08-02
theme: testing-craft-and-skills
labels: [Exploratory Testing]
source: https://visible-quality.blogspot.com/2015/12/polarities-of-test-data.html
---

# Polarities of test data

*Published 2015-12-30, updated 2016-08-02 · Labels: Exploratory Testing*  
*Source: <https://visible-quality.blogspot.com/2015/12/polarities-of-test-data.html>*

---

I've recently been testing a complete redo of our reporting functionalities, and all in all surprised in how is it possible for a pair of developers to think it works when it does not. Even when there is a clear oracle in form of an existing previous implementation you can test against.  
  
Testing this redo as if it is new functionality but with a simpler oracle has lead me to create simpler test data. I first handle just individual pieces and then move on further into combinations. The main principle guiding me is control: me in control of the data, understanding the basic before going into the complex and complicated.  
  
My testing of the reporting functionalities was interrupted by a release with just a few little updates. All the updates were related to upgrading components, both 3rd party and our apps shared components. These usually cause specific types of problems, so I run a set of explorations around basic scenarios but this time, did not pay attention to data much. I used the data I had created for the reports, simple and controllable.  
  
And a bug escaped us: there's a grid component that we for purposes of one view overloaded for height calculation, ending up with a problem that in other places, scrolling would fail. A classical (for us) mistake of one developer working with the component in one place tweaking it to be for that purpose, and it having trouble then when used elsewhere.  
  
For me the interesting lesson was on data. If I had been on my typical data, I could not have avoided to see the bug. But since I was in a narrow and limited, controllable set of data, it hid the problem.  
  
With continuous delivery though, the problem was shortlived. But it lead me to create two specific sets of data to reuse as part of my checklists. There's never one, but I can try doing smart selections of what I keep available.
