# Do Thee TDD

Sampling many customer organizations, I can't help but to note a customer theme we aren't answering well. The question is if we are doing test-driven development.

A lot of us know what it is. We usually have learned to recognize it as possibly two different patterns: 

1. TDD while programming. Super-small loops (inside out,  'Chicago school'). Or small loops with mocks at play (outside in, 'London school'). 
2. ATDD (BDD, SBE - lots of names for similar idea) where examples characterize the feature before adding it. 

For a lot of the customers through, I realize these two are more intertwined. And the conversation very often gets derailed to defining if the test *really happened before*, and how often did it make sense for each of the developers to write the test first ('isolating a bug is great test first') or write it as part of the few hours-few days feature they are on ('easier to capture intent in the same pull request when I first figured out how to get it done'). In a scale the customer looks at, you can't really tell if it was before or after. In scale of the developer learning techniques to better control and describe the intent and not miss relevant bits with short-loop-after, learning the test-driven development techniques, both Chicago and London styles to mix them up probably does a whole world of good. 

The customers concern is not always whether the test came first. But it is if it came before (ATDD style) and if it came with the change itself (included in PR). 

I find myself characterizing the answers to this team with slightly more granularity: 

* Level -1. Test after with tester tests and bug reports. This happens a lot too. The 'nightly run' where analyzing the failures takes a week. We've all been there. Lets hope for a generation of developers who will look puzzled at that statement. 

* Level 0. No Sign of TDD. When code is merged with pull request, significant effort of testing follows in subsequent pull requests. There could be test changes with the original pull request, but their intent tends to be to get old tests to pass. 

* Level 1. Short-Loop-After. When code is merged, so are tests. Same pull request. Thus in same repo, going into the pipeline. Little care if it was a mix of before and after writing the implementation because the loop is short enough. This more driven and continuous than we ever used to have and we should celebrate. 

* Level 1b. Disciplined TDD. When code is merged, so are tests. Mixing outside in and inside out, with and without mocks, but the developers consistently write tests first. 

* Level 2. Acceptance criteria with examples. Examples from customers, illustrating core things that are different after the change, and introduction of the new behavior.  Just having the examples around help developers with a clearer definition of done, and less looping back to new information to learn. Things aren't obvious to everyone in the same way. 

* Level 3. BDD automation before implementation. Examples passing one by one drive the idea of are we done with the change. 

The three first teams I think of are on levels -1, 0 and 1. They all aspire to level 2. 

Smaller steps may make it more manageable as a change. Where are you, and where are you heading? 