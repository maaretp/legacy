# Evidence of Testing

# Principles

Principle 1: Our primary evidence is green run of test automation on four levels: unit, component, subsystem-e2e and system-e2e. This evidence is version controlled and packed with every build from main as scripts that can be run against the build.

Principle 2: Secondary evidence exists to critique reliability of primary evidence. It takes form of exploratory feature and release testing tracked with Jira tests and test executions and green marks on acceptance criteria.

Principle 3: Everything team thinks ends up in code. Displaying this thinking with written acceptance criteria reviewed / demoed increases likelihood of noticing expectations don’t match.  

# Practice

While Planning:

* Team adds one-liner [Feature] and [Explore] and [Release] tests to repository to support selecting delivered features for secondary regression testing to address the risk of changing claims while changing automation for false green status
* Team selects tests into per-release Feature and Release Testing test execution
* Team collects preliminary claims for acceptance criteria and the NO lis
* Team builds up programmatic tests on unit, component, subsystem-e2e and system-e2e levels with principle of always increasing coverage and value of tests as executable specification of developer intent
* Team reviews the acceptance criteria and proposes enhancements and clarifications

While Testing:

* Team gets green pipeline to merge to master and monitors percentage of green pipelines to master
* Team get green scheduled pipeline on system-e2e tests twice a day and monitors percentage of green scheduled pipelines
* Team marks the items on Feature and Release Testing test execution green to indicate their best current assessment of sufficient testing
* Team updates claims for acceptance criteria and the NO list to match tested and delivered scope
* Team does not link found bugs to tests in test executions even if they reported the bugs in writing

While Releasing:

* Team presents the plan exists and that all items on test execution are green and that items have acceptance criteria marked :check_mark: to indicate verification.
* Team accepts release after reviewing the evidence with competence managers (technical quality and system testing are owned by different competences)
