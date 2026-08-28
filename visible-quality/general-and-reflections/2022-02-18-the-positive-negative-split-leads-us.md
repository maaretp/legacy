---
title: "The Positive Negative Split Leads Us Astray"
date: 2022-02-18
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2022/02/the-positive-negative-split-leads-us.html
---

# The Positive Negative Split Leads Us Astray

*Published 2022-02-18*  
*Source: <https://visible-quality.blogspot.com/2022/02/the-positive-negative-split-leads-us.html>*

---

As I teach testing to various groups in ensemble and pair formats, I have unique insight into what people do when they are asked to test. As I watch any of my students, I know already what I would do, and how many of my other students have done things. Noticing students miss out on something, I get to have those conversations:

"You did not test with realistic data at all. Why do you think you ended up with that?"

"You focused on all the wrong things you can write into a number input, but very little on the numbers you could write. Why do you think you ended up with that?"

"You tested the slow and long scenario first, that then fails so you need to do it again. Why do you think you ended up with that?"

As responses, I get to hear the resident theory of why - either why they did not yet but would if there was more time, or more often, why they don't need to do that, and how they think there are no options to what they do as if they followed an invisible book of rules for proper testing. Most popular theory is that **developers test the positive flows so testers must focus only on negative tests***,* often without consulting the developers on what they focus on.

I typically ask this question knowing that the tester I am asking is missing a bug. A relevant bug. Or doing testing in a way that will make them less efficient overall, delaying feedback of the bug that they may or may not see.

I have watched this scenario unfold in so many sessions that today I am ready to call out a pattern: *ISTQB Test Design oversimplification of equivalence classes and boundary values hurts our industry*.

Let me give you a recent example, from my work.

My team had just implemented a new user interface that shows a particular identifier of an airport called ICAO code. We had created a settings API making this information available from the backends, and a settings file in which this code is defined in.

Looking at the user interface, this code was the only airport information we were asked to display for now. Looking at the settings API and the settings file, there was other information related to the airport in question like it's location in latitude and longitude values. Two numbers, each showing a value 50.9 that someone had typed in. How would you test this?

I showed it around for people asking this.

One person focused on the idea of random values you can place in automation, ones that would be different every run time and mentioned the concept of valid and invalid values. They explained that the selection of values is an *acceptance tester's* job, even if the project does not have such separation in product development.

One person focused on the idea that you would try valid and invalid values, and identified that there are positive and negative values, and that the coordinates can have more than one decimal place. We tested together for a while, and they chose a few positive scenarios with negative value combined with decimal places before calling it done.

I had started with asking myself what kind of real locations and coordinates are there, and how I could choose a representative sample of real airport locations. I googled for ICAO codes to find a list of three examples, and without any real reason, chose third on the list that happened to be an airport in Chicago. I can't reproduce the exact google search that inspired me to pick that one, but it was one where the little info box of the page on google already showed me a few combos of codes and coordinates, where I chose 41.978611, -87.904724. I also learned googling that latitudes may range from 0 to 90 and longitudes range from 0 to 180.

It turned out that it did not work at all. Lucky accident brought me with my first choice to discover a combination of four things that needed to be put together to reveal a bug.

- The second number had to be negative
- The second number had to be with more than four digits
- The second number had to be less than 90
- The first number had to be positive

Serendipity took me to a bug that was high priority: a real use case that fails. Every effort in analyzing with the simple ISTQB style equivalence classes and boundary values failed, you needed BBST style idea of risk-based equivalence and combination testing to identify this. The random numbers may have found it, but I am not sure if it would have been motivated to immediate fix like the fact that a real airport location for a functionality that describes airports does not work.

Our time is limited, and ISQTB style equivalence classes overfocus us on the negative tests. When the positive tests fail, your team jumps. When the negative tests fail, they remember to add error handling, if nothing more important is ongoing.

After I had already made up my mind on the feature, I showed it to two more testers. One started with coordinates of their home - real locations, and I am sure they would have explored their way to the other 3/4 of the globe Finnish coordinates would not cover. The other, being put on the spot fell into the negative tests trap, disconnected with the represented information but when pointing this out, found **additional** scenarios of locations that are relevantly different, and now I know some airports are below sea level - the third value to define that I had not personally properly focused on.

Put the five of us together and we have the resultful testing I call for with contemporary exploratory testing. But first, unlearn the oversimplistic positive / negative split and overfocus on the negative. The power of testing well lies in your hands when you test.
