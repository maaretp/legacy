# Dealing with In-Development Bugs

## Principles

Principle 1: Bug is anything that might bug a stakeholder. It includes non-conformance to explicit requirements but also 
proposals of being below a great level. It’s not just users but all stakeholders, including our future selves. 

Principle 2: Zero Bugs Policy. We fix them all or we decide that something below a great level is currently required. 
This means some bugs are closed without fixing. We never keep things hanging around for future. Closed ones can be brought 
back in future without the mental cost of keeping them on open tracked lists. Agreed limitations are documented on 
the NO list for acceptance by release time because people forget agreements.

Principle 3: Fix and forget. We fix root causes not symptoms and while fixing, we document improved developer intent 
with programmatic tests. Having bugs means we had new information to process. 

## Practice 

While Testing:

* Team adds one-liner descriptions for any bugs that are not fixed within the same day as discovered on the releases page
* Team uses conversational approach to make people aware of incomplete work by discussing bugs after daily meetings to support fixes flowing through quickly
* Team writes more than one-liner if more text is needed. Comments are not used to communicate. Comments indicate wrong choice of tool and failure of conversational approach the practice relies on.

While Prioritizing:

* Team clarifies unclear priorities in in-scope/not-in-scope level with a conversational approach
* Team actively proposes things that don’t jeopardise quality but can be scoped out

While Refining:

* Team members call one another to create understanding to make the right fixes

While Fixing:

* Team uses release page to remember to fix all identified bugs
* Team’s target is to make this list empty, and strikethrough is used to indicate need of second pair of eyes on the fix
* Anyone other than the fixer can be second pair of eyes for a fix and delete the item from the page to indicate its confirmed gone

## Practice (needed when stabilization became a need)

While Testing:

* Team reports bugs and links them to tests selected into test execution so that they show up in traceability matrix
* Team uses metric of visible vs. invisible inked to estimate things on list not yet made visible by sufficient testing against explicit requirements and implicit stakeholder expectations

While Prioritizing:

* Named Responsible prioritizes all issues assigned to them and indicates prioritisation by removing themselves from assigned to field
* Named Responsible prioritizes with both priority (group) and rank (absolute order). Team only uses priority as rank is insignificant while epics are already in development.  
* Named Responsible links bugs to epics for purposes of their own tracking. The bugs are already linked to tests and visible with traceability matrix.

While Refining:

* Team hold weekly meeting on Mondays to clarify what bugs are ready for team to pick (prioritized) and clear enough

While Fixing:

* Team picks issues first in highest priority from https://vaisala.atlassian.net/issues/?filter=11522&jql=project+%3D+AMS+AND+issuetype+%3D+Bug+AND+status+not+in+(Done%2C+Closed)+ORDER+BY+priority+DESC&atlOrigin=eyJpIjoiNjgzMzNhYjhlOGM1NDAxNmJhNWYyOTFlMWM0ODVlYzAiLCJwIjoiaiJ9
* Team’s target is to make this list empty
* Team doesn’t assign them to people but recognise some may require multiple people and we want to keep only the ongoing work visible with possible assignment to avoid any personal queues
* Team makes list empty by carefully considering implications of proposed changes, not by patching symptoms described
* Team updates developer intent in programmatic tests in addition to fixing, applying a fix-and-forget (because automation remembers) principle
* Team moves issues to In verification status to indicate the problem has been addressed
* Anyone other than the fixed can be second pair of eyes for a fix and close the item as Done.
* Refining, Ready for development, In development and Ready for verification statuses are not used, only Open, In verification and Closed. 
