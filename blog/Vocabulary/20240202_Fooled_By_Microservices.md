# Fooled by Microservices, APIs and Common Components

These days writing software is not the problem. Reading software is the problem. And reading is a big part of the real problem, which is owning software. Last two years has been a particularly challenging experience in owning software, and navigating changes in owning software. I have not cracked it, I am not sure if I will crack it but I have learned a lot.

To set the stage of my experience. Imagine coming to a company with a product created over a period of 20 years. There's a lot of documentation, none of it particularly useful except code. While the shape of the existing product is invisible, you join a team dedicated to modernisation. And the team has already chosen a rewrite approach.

For the first year, the invisible is not a priority. After all, it will be replaced, and figuring out the new thing is enough work as is with a new product. With what feels like heroic effort, you complete the goal of the year with managed compromises. Instead of full rewrite, it's full rewrite of selected pieces. The release is called "Proof of Concept" and it does not survive the first customer contact.

Second year has goals set, to add more functionality on top of the first year. The customer feedback derails goals leading to an entire redesign of the user interface, addressing  9/19 individually listed pieces of feedback. Again what feels like heroic effort, you complete the goal of the year with managed compromises, but now an upwards rather than downwards trend.

The second year starts to give a bit of shape to the existing invisible product, with deliberate actions. You learn you own something with 852k lines of code. It has 6.2% duplication, and 16,4% unit test code coverage. The new thing you've been focusing on has grow into 34k lines of code, with 5% duplication and unit test code coverage of 70%, and great set of programmatic tests that don't hit the unit test coverage numbers.

Meanwhile, you start seeing other trends:

* Management around you casually drops expectations of microservices, APIs that allow easily building other products than this one, and common components with expectations of organizational reuse.

* You and your team are struggling with explaining that the compromises you took really may not have changed it all to what some people now seem to be expecting,

* You realize that what you now live with is four different generations of technological choices no one told the invisible mass would bring you - time adds to your understanding

In one particularly difficult discussion, someone throws microservices at you as the key thing, and you realize that the two sides of the table aren't talking about the same thing.

One party is describing Scripts with flat file integration:

* Promised by shadow R&D without promises of support, usually done in scale of days

* Automate a specific task

* Deployment is file drop on filesystem, and not available if not dropped

* Can break with product changes

* Output: file or database, usually a file

* Expected to not have dependencies

* Needs monitoring extended separately

* Using files comes with inherent synchronisation problems

* Needs improving if scale in insufficient

* Can be modified by a user

* Batch work, will not be real time

* File based processing steps quickly increase complexity

The other party is describing microservices with API integration:

* Promised by R&D assuming it will drive product perspective forward, usually in scale of months when deployment risks are addressed

* Develop apps that scale

* Deployment is with product and feature can be on or off

* Protected by design as product capability with product changes

* Output: well defined API

* Deployed independently / separately with dependencies - API, DB, logic, UI

* Follows a pattern that allows for common monitoring

* Uses http and message queues as communication protocol

* Can be scaled independently

* Can't be modified by a user

* Can be close to real time data synchronization

* Plug in extra processing steps

One party thinks micro is "fast additions of features" and other thinks it is a way of creating common designs.

You start paying more attention of what people are saying and expecting, and realize the pattern is everywhere. Living with so many generations of expectations and lessons makes owning software particularly tricky.

We're often coming to organizations at a time. We're learning as we are moving along. And if we are lucky, we learn sooner rather than later. Meanwhile, we are fooled by the unknown unknowns, and confused by the promises of the future in relation to realities of today.

The best you can do is ground conversations to what there is now, and manage to better from there.
