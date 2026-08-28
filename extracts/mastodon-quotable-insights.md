# Maaret Pyhäjärvi on Mastodon: Quotable Insights

Curated one- and two-line insights pulled from the 3,519 original posts in
`archives/mastodon/20260828_outbox.json` (November 2022 to August 2026). Quotes
are verbatim; dates are the post date in ISO form. Selection favours statements
that stand on their own without the thread around them.

Where the quotable material clusters: testing philosophy and the language we use
for it, the manual/automated false split, test automation as an investment,
feedback and learning, management and visibility, meetings and waste, and — from
2024 onward and heavily in 2026 — AI in testing and work.

## What testing is

- "Testing is not the 'doing the dishes on time' of software development as I saw
  suggested on LinkedIn but it is the 'adding spices' of software development."
  (2023-01-12)
- "When will the world be ready to see that testing is about the problem of
  knowing?" (2023-01-01)
- "Having something 'tested' is not binary, not a yes/no. It is a discussion of
  how much / how well as per possible expected results." (2022-12-01)
- "When your product has performance problems, it is not performance testing you
  lack but performance engineering or performance fixing." (2023-04-04)
- "Bad quality is hard to hide when a tester is in the room. That may be diagnosed
  as the tester being inactive or difficult rather than identifying the root
  cause in quality problems." (2026-04-09)
- "Quality and results don't move out with testers moving out of scope."
  (2025-11-23)
- "It does not help if what I do (exploratory testing) must be called 'quality
  assurance' because someone decided that thinking while testing and talking to
  ones colleagues is not testing so it has to be quality assurance." (2025-06-30)

## Bugs, and the words we use for them

- "How you find a bug ('regression test set') is not the same as the cause of the
  bug ('regression')." (2023-04-06)
- "A common theme on wordplay that has helped many in projects is to replace
  'bugs' with something else. I talk about unfinished work, avoid defect and
  change request, and prefer to frame these as conversations we should be
  having." (2022-12-28)
- "For user a symptom is a bug - 'anything that might bug a user'. For someone
  fixing, they would prefer to prioritise the causes." (2022-11-16)
- "Professional reaction to good / bad news from a tester telling that the system
  is broken in a specific but fairly complicated way: 'That is not only good
  news'." (2023-06-06)
- "Kind of funny how quickly we testers jump to mention that bugs that escaped us
  aren't our responsibility." (2026-02-05)
- "Monday morning, and a tester complains how a system is buggy = not tested [...]
  it again annoys me that even people who professionally test can't tell the
  difference." (2025-08-04)

## Test cases, scripts, and documentation

- "Traditional manual test cases are not about testing, they are about
  documentation." (2023-05-26)
- "The manual testing, that was not about testing but about writing step by step
  documentation in a tool." (2025-11-28)
- "If you coded the thing first and now script test cases for automation before
  automating them, that is not it." (2022-11-09)
- "'AI creates great test cases' may be true, but test cases are not testing."
  (2026-02-10)
- "When your customer asks 'how many tests will you automate for us', that is not
  a literal question for a number or even a percentage. That is a question that
  shows how you approach the question." (2024-08-15)

## Manual versus automated: a false split

- "Like we think we do 'selenium' or 'playwright' or 'robot framework', even if
  there's a lot of ecosystem pieces that drive the experience we have."
  (2023-02-17)
- "I thought I knew what is 'manual testing'. But apparently I did not know that
  it means automated tests that aren't run in pipelines on triggers but
  manually." (2024-08-20)
- "When do we learn that an option to automating is considering if the thing we
  are automating is worth doing in the first place." (2023-11-20)
- "And some bad (wasteful) things aren't bad in the same way when automated."
  (2024-04-17)
- "I wonder if we made the resultful thinking kind of testing less accessible to
  testers by calling it exploratory testing, instead of manual testing."
  (2026-08-05)

## Test automation as an investment

- "Getting some in is not what matters. Sharing every step of the way on
  ownership is what matters." (2022-11-17)
- "Test automation investment that is a series of commits by one person at a time
  significantly cuts the value." (2024-11-15)
- "The real work is done by people, perhaps implementing that automation."
  (2023-12-07)
- "Design your test code for when it fails." (2024-05-09)
- "Code alone is already a liability, but code without code that builds it and
  tests it (pipeline), that is a whole other level of liability. If you add 5000
  manual test cases to the mix, that isn't helping it." (2024-07-01)
- "Test system is more complicated that system under test. Because you have all
  that test ware around the thing." (2025-05-27)
- "Granularity. That's what we seek for feedback. Isolating changes and getting
  feedback on each separately rather than the tangled mess of nightly runs and
  end to end tests." (2024-09-22)

## Exploratory testing

- "There Is nothing in definition of exploratory testing saying you can't have
  specs. It's funny how many insist that their idea of using it when spec is
  unavailable is the key defining factor." (2025-02-09)
- "I don't care what it is. I care about the fact that I have an application with
  a lot of insight that I would like people to be able to generate, and they
  aren't able to. I want to find the teachable skills so that they are."
  (2026-01-03)
- "Agency - not separating the things that inherently should belong together -
  has been a driving force for how I facilitate testing." (2023-08-17)
- "I have been watching people who do a flavor of exploratory programming. The
  difference between whether that is good or bad is in how they judge success of
  a step. Works in one scenario or works in necessary scenarios." (2024-03-17)

## AI and LLMs

- "Theory of the day. When AI is in the organization structure, it's not in the
  organization." (2025-12-18)
- "I find it fascinating that we would rather pay 1€ to AI than the same 1€ to a
  human. The ongoing conversation is not about cost savings, it's about replacing
  a dependency with one with different features." (2025-12-18)
- "Applying AI in testing to do test practices that are already wasteful to do
  wasteful things faster is not my goal." (2024-09-26)
- "For a lot of issues in testing, we have good answers that are not AI."
  (2024-09-26)
- "The 'AI agent' is hardly the new user. The programmatic proxy is not the user,
  the user is whoever is behind the proxy, with an actual need." (2026-07-17)
- "Does prompting really happen in the problem domain? I tend to see people
  prompting mostly in solutions domain." (2025-12-11)
- "The genAI you need to run your tests means that the cost of use repeats over
  time. If you expect your tests to live 10 years (conservative), that can make a
  lot of paid API calls. Design the use a bit please." (2024-08-23)
- "When the value of stack is delegated to an AI model, people aren't as willing
  to pay whatever is built on top of it." (2026-01-30)
- "'Did you create this summary with AI' (implying it was incorrect, which it
  was) is the new repellent of work I could be doing." (2026-08-20)

## Feedback

- "More feedback is not always better. Dealing with that feedback is time away
  from something else." (2025-03-04)
- "Seeing week after week that people aren't into talking about my topics on lean
  coffee is feedback." (2023-12-22)
- "People confuse an attempt to establish a boundary before escalating behavior
  as 'feedback' and spiral into reciprocating 'feedback' instead of hearing and
  confirming the boundary." (2022-11-15)
- "Every time I find myself wondering why it's always me with corrective
  feedback. Some things are just too important to be left as you found them."
  (2025-04-05)
- "All emotions are welcome, all behaviors are not." (2024-09-28)

## Learning and skill

- "Learning isn't rework. Learning and thoughtfully reacting to learning leads to
  change, but framing that as rework misses the mark by so much that I can't even
  begin to express it." (2024-02-02)
- "When someone can't do something, it is not a *quality of the person* problem,
  it is a *quantity of skills in a person*." (2024-09-09)
- "The people who can't learn on the side of work can't learn when full time
  learning either. Time was not the blocker for learning, it turns out to be
  excuse." (2026-01-20)
- "People who say they learn badly with self-study also tend to learn badly in
  teacher-lead." (2025-07-04)
- "Expressing intent and reviewing intent are not skills people have out of the
  box (box being schools)." (2023-11-20)
- "There is time to understand and learn details of how something works, and
  there is time to treat it as black box providing a service that enables you to
  provide value in your work. You can't open all the boxes." (2022-11-28)
- "The realization that I can know more of our old legacy system in a day than
  anyone in the team [...] All these ways to learn were always available and they
  did not take those. Agency is really the key." (2024-02-24)

## Teaching, mentoring, paying it forward

- "2nd generation tester (someone I hired and trained) was recruiting. Instead of
  bringing in one junior, her org now brings in two. Network effect of paying it
  forward FTW." (2025-03-12)
- "I teach by doing, by the learner. It's a strong-style navigated demo where the
  person who knows less is on the keyboard." (2026-06-18)
- "When I direct work, assess knowledge and skills, and teach things I know as I
  figure out I know something you don't know, I am not coaching you." (2023-10-25)
- "Sharing in the open is not away from them, it is serendipitous opportunities
  for learning for me." (2024-01-09)
- "It turns out that since I quit public speaking, my colleagues think I will not
  teach them stuff I know." (2023-08-05)
- "The realisation of learning to appreciate how much of the work is *holding
  space* over doing the work hit me again." (2023-01-04)

## Management and leadership

- "You don't fix management / meeting heavy approach with management / meetings."
  (2025-11-04)
- "The reason 'management' does not know how to 'lead' testing is that many of
  them have never experienced good and before they do, they operate on hearsay.
  It's not a leadership problem (alone), it is a visibility / explainability
  problem." (2024-11-28)
- "When you have 5 leaders to 5 teams each with 5 developers, the best I can do
  for quality is get these leadership folks (me included) out of the way creating
  helpful frames of direction." (2022-11-08)
- "If the only way to communicate is through manager supervision, a lot of
  necessary things will remain unsaid." (2023-05-09)
- "So managers asking 'me to write notes as memo' are not just moving my private
  to public, they remove the way I learn." (2022-12-20)
- "Explain me the box I work in, don't prioritise for me. Especially task level."
  (2023-11-22)
- "The higher up we are in management, the more we need to learn to control
  reactions to emotions." (2023-07-28)
- "Failing to step up to consider your impact, value and preferences is not a
  problem of your manager, it is yours." (2023-11-28)
- "The observation was, again, that same good work is allowed and expected when
  you don't change work or person, but change the person's title." (2024-06-11)

## Trust, agency, and self-organisation

- "The thing is, when I say I'm not trusted, it means you trust *yourself* over
  me." (2024-01-05)
- "Being the second pair of eyes means you have to be able to add to the first
  pair." (2023-08-14)
- "Me watching you read and think out loud is not 'collaboration'. Really."
  (2025-10-24)
- "It is kind of insulting to not let team of six with 200 years of experience
  self-organize. People outside have too much time on their hands." (2026-02-27)
- "Almost every time when you feel you need more people, the opposite is true."
  (2024-09-19)

## Meetings, queues, and waste

- "Meetings are queues. Holding on to a thing you'd need to know of until daily
  just because there is daily isn't optimizing the value creation." (2022-12-28)
- "It's not the planning that happens in that meeting, it's the planning that
  happens leading to that meeting." (2022-11-15)
- "There are queues to wait in that describe the process design, and ones that
  assign blame. Being able to tell the difference between the two is kind of
  relevant. They get tangled up so easily." (2024-09-11)
- "Seeing waste as in things we do for 'process' that isn't even really a process
  but inability to access past agreements in useful ways with courage to change."
  (2023-11-06)
- "You interrupt a colleague at office, and they report hours on the thing you
  interrupted. Same but remote, and it's admin. Reporting hours is such a
  collaboration killer." (2024-10-30)
- "I measure pull requests. Not because I would think they represent some form of
  efficiency but because nothing changes when you change nothing. It is an
  indicator of blocked progress." (2023-01-08)

## Estimation, deadlines, and decisions

- "It is not about sticking to the deadline, it is to understand that before your
  final deadline, there may be other deadlines that cause work for others."
  (2025-06-03)
- "Not making a decision when a decision is needed is making a decision."
  (2023-03-27)
- "Recognize that all decisions aren't irreversible and move your decision to a
  scope that isn't. Seek the path." (2025-03-19)
- "The thing that we estimated 1...2 days has taken 40 days." (2023-05-22)
- "People conflate categorization and prioritization a lot. When you classify
  items to P1, P2 and P3, that is categorization. Prioritization says item 1 is
  more important than item 2." (2026-01-14, quoting a colleague)

## Scope, requirements, and value

- "Specs are not handed over to us, they are created by us." (2022-12-11)
- "The things I expect are not requirements as they are negotiable and more a
  visualisation than a specification." (2023-05-17)
- "Our problem is not distance from customers, it's prioritizing the changes."
  (2024-02-02)
- "The best of teams have customer so much at heart that you can proxy and
  listen, not follow requirements or negotiate scope." (2023-02-10)
- "Caring for schedule in the projects I work with is more often caring for
  scope. Not as fast as possible." (2023-08-06)
- "When you have the wrong system, you have the wrong system no matter what tech
  magic you put around it." (2024-11-15)
- "Risk is an event with uncertainty. Leaking confidential data by posting it to
  a third party API that collects it is not a risk. Them changing their mind
  about using it is." (2025-02-08)

## Change and organisations

- "Waterfall is waterfall, even if you choose to draw it as loop." (2024-10-11)
- "What drives change is not cost of ownership but new features." (2024-04-07)
- "I think I am doing better for testing in scale of the company now that my
  responsibility is not to make testing better in scale of the company."
  (2023-08-25)
- "When they say they need 'enterprise scale', it means being done by masses of
  commoditized workers. It's bringing the skill level down rather than up."
  (2025-02-07)
- "Creating an IT ticketing system that is so hard to use that you can't report
  the trouble you have is a great way of saving in the visible IT costs. However,
  the true cost is in productivity of the tasks IT is supposed to support."
  (2026-01-14)

## Consulting, hiring, and career

- "Noticing a pattern with clients: paying for advice and expertise is hard if it
  is not directly bundled with execution. The platform of expertise has been
  quite an investment, yet it's expected to be available for free." (2026-01-14)
- "I never realized that having a CV that is not 'company confidential' since I
  have been learning so actively in public could be a benefit. But turns out it
  is." (2025-07-02)
- "Consulting is fascinating on the feedback you get on continuous job
  interviews. Learn to ask 'what you look for' and 'how do I match'. The worst
  thing is 'I don't have any questions'." (2025-12-02)
- "Having a tester who is trustworthy - invaluable. Also emphasised having
  testers who are not trustworthy and the extra load they add." (2023-05-30)
- "Having one team member with testing emphasis (tester) tends to mean that
  testing is not an entry level position. With teams of testers, there were
  *some* entry level positions for testing and now they are rare." (2025-05-07)

## Speaking and writing

- "Choosing to speak / teach based on writing is not about best, it's about
  chances." (2022-11-22)
- "But the hard part is writing worth reading, and finding worthwhile reading in
  all of the writing." (2024-06-26)
- "Four blog posts in four days. Clearly I don't write so that people would read
  but so that I can offload." (2024-06-24)
- "Some people think public speaking means invite to 'debate' and no need for
  kindness." (2023-09-20)
- "The inclusive approach cannot pretend the speakers aren't setting the tone,
  also on their behavior outside the event." (2024-01-25)
- "There are stories I have waited for 5 years and two employers to tell. Not
  because I would have to pay 5M if I told, but because time dilutes the
  connection and leaves the lesson." (2024-05-30)
- "To change the world, I need to move what is grey to the academically
  acceptable." (2026-01-03)

## Voice and stance

- "I see much of the world as models, and I work through problems making through
  creating a visual representation of them [...] I value people who draw
  together, because it's the process not the result that matters." (2022-11-11)
- "At some point of your life you talk more about things that have happened over
  the things that could still happen. When the balance twists to past, you are
  old." (2025-06-25)
- "The things that happen in our heads may have a connection with reality and yet
  not be real. We choose our actions and live with the consequences." (2025-03-22)
- "Sometimes I am leading things that aren't mine to lead." (2026-05-29)
- "Two years ago I was the only woman in our leadership group. Now I'm one of
  three. Just realized it's enough that I no longer feel like I stick out for
  it." (2026-08-07)
