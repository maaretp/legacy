---
title: "A Tentative Framework for Managing Software Product Development in Small Companies"
publication: "Hawai'i International Conference on System Sciences (HICSS) Proceedings"
date: 2002
url: https://drive.google.com/open?id=0B07e3JZGe_haX0JyTGtuMDRHczg
source_retrieved: https://drive.google.com/open?id=0B07e3JZGe_haX0JyTGtuMDRHczg
kind: research paper
language: en
---

# A Tentative Framework for Managing Software Product Development in Small Companies

*Hawai'i International Conference on System Sciences (HICSS) Proceedings — 2002*

Source: <https://drive.google.com/open?id=0B07e3JZGe_haX0JyTGtuMDRHczg>

> Retrieval note: text extracted from the author's PDF of the article (the Google Drive copy needs sign-in); layout is approximate.

---

Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

  A Tentative Framework for Managing Software Product Development in Small
                                Companies
     Kristian Rautiainen, Casper Lassenius, Jarno Vähäniitty, Maaret Pyhäjärvi and Jari Vanhanen
                                  Helsinki University of Technology
                             Software Business and Engineering Institute
                               POB 9600, FIN-02015 HUT, FINLAND
                                      firstname.lastname@hut.fi

                        Abstract                                  In this paper we present a tentative framework for
                                                               managing software product development in small
   Deploying an appropriate software process can               companies. By small companies we mean companies with
improve the effectiveness of software engineering. Still,      less than 100 employees and less than 50 developers. The
small companies find it hard to allocate resources to          framework is partly based on our previous research on
software process improvement and tailor existing process       improving the controllability of product development,
models for their needs. In this paper we present a             during which we identified the basic components of a
tentative framework for managing software product              control system for managing product development. To
development in small companies. The framework                  add to this knowledge and to focus on software product
combines business and process management through four          development we have studied different process models
cycles of control: (1) Strategic release management            found in literature. These models provide valuable insight
provides the interface between business management and         and alternatives to managing the software engineering
product development. (2) Release project management            activities of a company. We have also studied the
handles the development of individual product versions.        practices of so-called “agile” processes in order to find
(3) Iteration management deals with the incremental            alternatives that focus on small teams and projects. Also,
development of product functionality within release            the framework is based on interviews, discussions and
projects, and (4) Mini-milestones are used to get an           observations made with the participating companies in
indication of system status during development.                our ongoing research project.
                                                                  In this paper we focus on providing an overall view of
                                                               the framework. The details of the different parts of the
                                                               framework are left for subsequent work. First, we present
1. Introduction                                                the components of a control system for managing product
                                                               development derived from our previous work. Second, we
   It is widely understood that deploying an appropriate       shortly present our research project. Third, we present the
software process can improve the effectiveness and             tentative framework. Finally, we round up with discussion
efficiency of software engineering. However, small             and implications for further work.
companies find it hard to allocate resources for software
process improvement (SPI) and tailor existing process
models for their needs. Many of the well known software
                                                               2. A control system for managing product
process models and reference models, such as the                  development
Capability Maturity Model (CMM) developed by the
Software Engineering Institute (SEI) at Carnegie Mellon           In our previous research project we studied the
University (see e.g. [5]), provide a good basis for SPI, but   controllability of product development and one of the
they also provide excessive overhead if deployed in full.      findings was a set of basic components for a control
Specifically, they do not take the business aspects and the    system for managing product development, shown in
fact that different process models might be needed in          Figure 1. Many organizations face problems in managing
different    situations enough into consideration.             their product development operations. The problems can
Successfully managing software product development             be summarized into four groups: lack of direction,
demands more than having a suitable software process in        competence, motivation, or opportunity.
place – a more holistic view is needed.
Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

                                                                  Lack of opportunity: Even if the direction is clear,
                         Strategy                              people have the necessary competence and are well
                                                               motivated, lack of opportunity to achieve a given target
                                                               can occur. The target may be unrealistic or there may
                                                               simply be too many ongoing projects, too many targets to
      P ortfolio M gmt              Competence Mgmt            try to reach, which causes distraction. This may result
                                                               from, e.g., an inability to prioritize work or unrealistic
                                                               expectations about the existing resources and the effort
                                                               needed. DeMarco and Lister have discussed the subject of
                 P roject Class 1                              productive projects and teams in their classic work [11].
                        P roject Class N                          By thinking in terms of the components in Figure 1,
        Multi-Project          P rocess                        one should be able to create a control system to better
          Mgmt Multi-P roject Mgmt P rocess                    manage the product development efforts of the company
                   Mgmt                  Mgmt                  and improve the ability to control those efforts. A product
                                                               development strategy should provide the overall direction
                  Project Mgmt                                 of the organization, project portfolio management should
                          Project Mgmt                         ensure that the project load is not unreasonable,
                                                               competence management should handle the skill building
                                                               aspects, and good processes and project management
                                                               practices are partly responsible for creating a pleasant
   Figure 1. The basic components of a control
                                                               working environment for increased motivation. The next
   system for managing product development
                                                               sections briefly describe each of these components.
                                                                  Strategy: By strategy we mean the product
    Lack of direction: Getting somewhere demands               development strategy of the company, which should be
understanding where you are (current state) and where          derived from the overall corporate strategy. The business
you want to go (goal or target state). Lack of direction can   environment of the company must be considered, for
be caused, e.g., by an unclear business strategy. In a         instance the speed of change of technology or the
turbulent business environment the target may be moving        markets. An important issue is to understand that there are
so fast that it is elusive. Lack of direction may also         different types of product development projects that need
concern, for instance, process improvement on any              to be staffed and managed in different ways. For example,
organizational level. Measurement and goal setting plays       making a breakthrough product is different from making
an important role in overcoming such a lack of direction.      derivative products to already existing product lines. If
If you can use measures to indicate the present status of      product maintenance is considered as part of product
the process and give target values for the measures for a      development, it is also managed differently. The product
preferred status, you have better chances to control your      development strategy can be summarized as one or
actions towards reaching the goal state.                       multiple roadmaps (product, service, marketing, etc.),
    Lack of competence: Even if you know where you are         where for instance the product roadmap should show the
and where you want to go, you might not know how to            different types of projects and a rough resource allocation.
get there. This is a problem of lack of competence. For        This is then used as an input to project portfolio
example, the company may be moving into previously             management and competence management. E.g. Cooper
unknown markets, or the technology used in a product           talks about these issues in [7] and [8]. Also, these issues
may be so new that the competence has not yet been             have been touched in [18]. For examples of project
acquired. At that point it is very hard to estimate how long   classifications, see [19] and [21].
it takes to reach a sufficient level of competence, which         Portfolio management: By portfolio management we
influences the time to reach the target.                       mean the management of the whole set of projects of the
    Lack of motivation: In processes performed by              product development organization. The input to portfolio
humans, direction and competence are not enough. If            management is the product roadmap, especially the
people are not properly motivated to reaching a given          project type classification and the rough resource
target, any effort may be futile. Even if we know where        allocation. To be successful in portfolio management, one
we want to go and have the necessary competence to get         must also know the existing resources and competences in
there, lack of motivation will slow down or even halt our      the organization. Another input is, of course, the feedback
progress. Lack of motivation can be caused by many             from ongoing projects. The purpose of portfolio
things, which we will not go deeper into in this paper.        management is to specify in more detail the projects
E.g. Wiegers talks about culture builders and killers in his   needed to fulfil the strategic goals of the organization,
work [22].                                                     thus linking projects to strategy and operationalizing the
Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

product roadmap. An important task is to prioritize             management, you can still end up with too many projects
projects and select the order and mix of projects to be         and the project load will then at some point bring matters
executed. The output of portfolio management is an              out of control. Another problem we encountered was that
aggregate project plan or a project roadmap. The plan has       if we did not understand the whole, we could end up with
to be updated at regular intervals to reflect the current       a procedure that was sound in theory, appreciated in
situation. For example, many projects can be interrelated       practice, but failed because of some other practices
and if one project is lagging in its schedule, other projects   already in place.
can be influenced. This may lead to replanning and
reprioritizing the order and mix of projects. For more          3. The SEMS research project
reading, see for example [8], [12] or [18].
    Competence management: The purpose of competence                In the ongoing SEMS (Software Engineering
management is to keep track of the competences -                Management System) research project we are studying
existing and needed - in the organization and plan for          software engineering in small companies in the software
training and recruiting to fulfil those needs. Competence       product business. The project started in the autumn of
management is tightly connected to the product                  2000 and is planned to go on to the end of 2003. Our
development strategy and portfolio management. Also,            main focus is on the software development process and in
competence needs can arise in ongoing projects. One             finding links between the business model(s) the company
approach for obtaining a list of professional competences       has chosen and the software processes and software
can be found in [20].                                           engineering practices needed to support the business
    Multi-project management: The purpose of multi-             model(s). One of the goals is to find a light but high-
project management is to balance and allocate resources         impact way of systematically performing the software
between projects at a regular and short-term basis. Having      engineering practices that are required in developing
people work on multiple projects and moving them                high-quality software products. By light we mean that
around between projects is not easy, though, and can            introducing process or system thinking into the company
cause more harm than gain [4]. Multi-project management         should require as little resources as possible and minimize
is, naturally, closely linked to project portfolio              disruption. Another goal is to determine which the most
management, and could even be considered part thereof.          important practices are and package the lessons learned
    Process management: With process management we              into a software engineering management system for small
mean here managing the product development process.             companies in the software product business.
The process model works as a map for the development                McCormick’s opinion summarizes the ideas brilliantly:
projects providing the stages, milestones, roles, etc. It       “What’s needed is not a single software methodology, but
provides a common vocabulary and the “rules of the              a rich toolkit of process patterns and ‘methodology
game”, i.e., how things are supposed to be done in the          components’ (deliverables, techniques, process flows, and
organization. The process model should also be a tool,          so forth) along with guidelines for how to plug them
providing, e.g., templates and checklists for the projects.     together to customize a methodology for any given
It is important to realize that one process model cannot        project.” ([17], p. 110).
accommodate the needs of all different project types.               We currently cooperate with four companies in a mass-
Therefore some thought has to be put into choosing              market type of business, meaning that customer tailoring
appropriate process models. Some examples of issues             is not a significant part of the business. The products are
affecting the choice of process model are the speed of          not shrink-wrapped and in three of the cases some
change in technology or the markets, the size and length        tailoring has to be made when the product is installed.
of the projects, the size and complexity of the product         One of these companies also has an ASP solution for end
being developed, and the initial uncertainty of the project,    users. Two of the companies are in a fiercely competed,
i.e. how well we know the requirements up front. One            extremely fast-pace business environment, where being
part of process management is collecting data and               first really counts. Being in the software product business,
feedback from projects for process improvement                  the companies make different types of product releases.
purposes.                                                       The way of working is iterative and incremental. The
    Project management: Project management is about             release cycles are short, ranging from one month to a
executing the individual projects in a systematic way,          week, if counting the bug fix releases.
using the guidelines provided from the process models.              As a first step in the project, we have developed a
    One of the main lessons from our previous research          tentative framework for managing software development
project, where we worked with organizations to create a         in such companies, based upon our earlier work in new
control system for product development is that in order to      product development management. This framework is the
improve controllability you have to look at the whole.          subject of the next chapter.
Concentrating only at one part, for instance project
Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

4. Towards a framework for managing                                Bringing a software product release management point
   software product development in small                        of view into the discussion divides our framework into
                                                                two levels: long-term or strategic release management and
   companies                                                    release management in individual release projects.
                                                                Projects are executed in an iterative and incremental
   There are two main issues that have to be addressed in       manner for increased flexibility, using mini-milestones to
order to get from the control system presented in Chapter       gain more controllability. Figure 2 depicts these four
2 to a framework for managing software product                  cycles of control. In relation to Figure 1, the strategic
development in small companies. First, focusing on              release management cycle covers the top three boxes as
software product development, and second, focusing on           well as partly multi-project management, whereas the
small companies. Focusing on software product                   other three cycles present one way of implementing the
development introduces, among other things, the concepts        rest of the general control framework. The radius of a
of software engineering processes and practices. The            cycle symbolizes the time perspective taken. The larger
small company perspective brings constraints, especially        the radius, the longer the time perspective.
concerning resources.                                              The four control cycles, strategic release management,
   Most of the software engineering processes or software       release project management, iteration management, and
development processes in literature concern building large      mini-milestones are described in the following sections.
and complex systems, and therefore can create excessive
overhead for a small company. The CMM (see [5]), for
                                                                4.1. Strategic release management
instance, provides a way to build organizational capability
for performing software engineering. It even provides you
                                                                    The outermost control cycle, strategic release
with a recommended path of improvements to follow. But
                                                                management is the interface between business
the CMM was written to address the process for large,
                                                                management and product development. The main purpose
complex software efforts, something a small company
                                                                of strategic release management is to plan the release
with 3-10 developers probably would not undertake. In
                                                                cycles and the content, role and timing of each individual
[3] Brodman and Johnson showed how small businesses
                                                                release project. This means that the overall strategic
and small organizations viewed the CMM. Especially
                                                                ambitions and goals of the company have to be
some points are interesting to us: the need for the CMM
                                                                considered, together with the availability and
to be more flexible and scalable in order to accommodate
                                                                competences of the people that do the actual work.
different types of projects, and that the attitude of the
                                                                Product line decisions may also be of concern here,
personnel can be a big contributing factor to not applying
                                                                especially when a company grows and diversifies its
the CMM or any other new process approach for that
                                                                product offering. An important task is to elicit, specify
matter. The CMM does not dictate which development
                                                                and prioritize requirements from different stakeholders,
process model one should use, it only tells you to use the
                                                                for instance marketing, customer services and users.
one that suits you best and tailor it for different needs. So
                                                                Requirements engineering also forms the main interface
there actually is flexibility in the CMM, it only gives
                                                                to the individual release projects.
criteria for mature processes, specifically a process must
                                                                    One of the biggest problems in requirements
be: defined, documented, trained, practiced, supported,
                                                                engineering is that the customer does not really know
maintained, controlled, verified, validated, measured, and
                                                                what he wants, or at least cannot express it coherently. In
improvable [5]. CMM also recommends that maturity and
                                                                mass-market products the problem can be that the end
effectiveness of processes should be interpreted in the
                                                                customer is not heard directly, and the requirement
context of the business environment of the company and
                                                                engineers must rely on, e.g., market research data. In fast-
the specific circumstances of the projects. A closer
                                                                pace markets some requirements change during the
explanation of this, however, is left to other sources.
                                                                project. Cusumano and Selby report in [9] that at
Since one of our research goals is to find a link between
                                                                Microsoft a vision statement and outline specification are
the business models companies use and the software
                                                                used to give enough structure to the development effort,
processes that support them, we took the business
                                                                but at the same time accommodate change and flexibility
perspective as a starting point in moving towards a
                                                                during the development process. The specification will
framework for managing software product development.
                                                                then evolve during the development project. Also,
Bays has summarized software release methodologies in
                                                                features are prioritized so that the most important features
his work [1]. He points out some important issues to
                                                                can be implemented first. The development is then done
consider in release management. These, combined with
                                                                in several incremental cycles, between which the
some other issues picked from best practice lists, such as
                                                                requirements can be reprioritized and new requirements
the Airlie Council’s list (cited from [24]) form a basis for
                                                                can be added if necessary.
the tentative framework described in this chapter.
Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

                                    Sales &
                                    Marketing
              Professional
              Services

                                Strategic                      Release
                                                                                   Iteration
                                Release                        Project                             Mini-milestones
           CEO                                                                     Management
                                Management                     Management

                Product
                Development
                                    Customer
                                    Services
                                   Figure 2. The control cycles of the framework
   In eXtreme Programming (XP) software development              abstraction level is more suitable for discussing future
is seen as “an evolving dialog between the possible and          releases and products. USDP also suggests business or
the desirable”. A practice called “the Planning Game”            domain models to be used, which can add width to the
brings together the two players: Development and                 information on top of the vision statement. In a very small
Business. Requirements are collected on story cards,             company a single person most likely acts in multiple roles
where Business writes the story and Development                  and strategic release management is done by as few as 3-4
estimates how long the story will take to implement. The         people. Even when the company grows the group should
stories can be split into more stories if necessary. Then        be kept fairly small for the meetings to be effective.
the stories are sorted and Business chooses the scope and
date of the next release.[2] The point here is that there        4.2. Release project management
should always be an effort estimation attached to the
requirements or features, otherwise you cannot consider             The next control cycle, release project management, is
the resource implications to the release projects.               concerned with individual release projects developing the
   The important thing to remember in requirements               actual product versions. In a small company there should
engineering is that the requirements should depict what          not be many concurrent projects, simply because there are
the system is supposed to do for the user, not the structure     not enough developers. This does not mean that there
of the system. The point is to fulfil a business need, which     would not be many different types of projects in the
the requirements should reflect. That way design                 company. The same developers can be, e.g., working on
decisions and decisions to add or drop features are easier       improving the product platform, developing new features
to make during development.                                      to an existing product, installing the product at the
   Figure 2 gives an example of some of the possible             customer’s site, maintaining the product (fixing defects),
stakeholders or stakeholder representatives that might be        or developing an entirely new product. The implication of
involved in strategic release management. The variety of         different types of projects is that they should be managed
stakeholders and their different areas of expertise propose      and controlled differently.
a challenge: the requirements or the features to match the          Two main project types are functionality driven and
requirements that are discussed should be presented in a         schedule driven. A new operating system is an example of
way that everyone understands. The Unified Software              a product that requires a functionality-driven project.
Development Process (USDP) suggests use cases for                Certain functionalities have to be in place for a system to
capturing the requirements and communicating them to             be able to work as an operating system. This means that
the customer and the designers [14]. This approach is            the schedule is allowed to slip so that the development
probably too detailed for this level of discussion. The          team can build the required functionality. Microsoft
vision statement used at Microsoft is a better way to            Office is an example of a product (or product family) that
communicate the purpose of the product. That way the             is developed in schedule-driven projects. The release
Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

deadline is set in advance and the product is released on       4.3. Iteration management
schedule. It is impossible to say beforehand what the final
configuration of features in the product is, because the            In each iteration a set of use cases or features are
features are decided upon as the project progresses.            identified, specified in detail, designed, implemented and
Features are dropped if they cannot be finished in time for     tested. This way there should be a working product at the
the release. For this to work, the features have to be          end of each iteration, which can be delivered to users to
prioritized.                                                    get early feedback on further development. At the end of
    What this means in relation to Figure 2 is that the         each iteration strategic release management is revisited to
release project management has to consider the length,          check the market situation and possible new or changed
content and number of iteration cycles in a project. The        requirements, so that the next development cycle can
task is to plan and specify the release project according to    focus on the relevant features. This approach has been
the priorities specified in strategic release management. In    found good for developing high-quality products in an
this paper the details of project planning are left out. In     environment with high uncertainty and rapidly changing
one of the companies we have studied, experience has            requirements [16], which is the environment of the
shown that a maximum controllable iteration cycle length        companies we have worked with.
for a new product or larger new features to an existing             An example of this approach is Microsoft, where large
product is three months. In the beginning the company           projects are divided into multiple incremental cycles at
tried longer cycles, but it always led to the projects going    the end of which a shipment of the product is made to
out of control. If there is only one iteration cycle, the       stabilize the product (Figure 3). That way Microsoft can
process followed resembles the traditional waterfall            fall back on the previous shipment if the next cycle fails.
model. When a product matures and there is experience           The individual engineers synchronize their work by doing
from multiple product generations, the changes to the           daily builds, which are also tested daily. The process has
product, e.g., adding new features can probably be done         been accordingly named Synchronize-and-Stabilize.[10]
with less effort and in shorter cycles, given that there are
no changes in the personnel developing the product. This          Product vision
should be a consideration in iteration planning. As a rule
of thumb, the length of a release project should lie                    Functional specification
between three and twelve months.
    USDP suggest an architecture-first approach in
planning and performing the iterations. The purpose is to              Development          Development     Development
find and develop a baseline architecture that will facilitate           subcycle              subcycle        subcycle
implementing features now and in the future.
MacCormack’s findings support that investments in                       Buffer time          Buffer time     Buffer time
architectural design are associated with better performing
projects, with good performance indicated by product                                                           Feature
                                                                       Alpha release        Beta release      complete
quality as perceived by the user [16]. Another
consideration is perceived risk. The greater the perceived                                                  Beta release
risk impact, the earlier the feature should be implemented.                                                   UI freeze
This way there is enough time to react to the possibly                                                     Code complete
realized risk and gain better control of the project.                                                      • Final test
    We have observed that when projects begin, planning                                                    • Final debug
quality assurance is often poorly done. Quality does not                                                   • Stabilize
just appear into the product – we have to think about it                                                    Final release
right from the start. We have seen organizations that have
left testing “to the last weekend” before the release, and      Figure 3. The Synchronize-and-Stabilize process
the consequences have been less than impressive. A                             (redrawn from [10])
difficult decision in testing is how much and exactly what          XP approaches incremental development by doing the
to test with limited resources. Prioritizing test cases and     development in short iterations, lasting 1-3 weeks.
parts of the system is the key. Also, understanding what        Highsmith talks about time-boxing projects as a
“good enough” quality means in each case is important.          mechanism for managers to force periodic convergence of
The testing process should be planned in parallel with the      a system [13]. All this implies that a certain amount of
development project, so that testing is considered at every     freedom can be given to the developers during the
stage.                                                          iteration cycle, as long as the system is stabilized at the
                                                                end, thus adding controllability by showing the exact
                                                                status of the system at that point in time.
Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

   An incremental development process makes regression          someone else’s revised code in time. This could have
testing especially important, as does a daily build practice.   been avoided if common rules for the source code control
Inspections or peer reviews could be seen as a part of the      had been established.
testing process, since one main point is trying to detect,          To avoid leaving all system testing “to the last
identify and track the defects as early as possible. This       weekend” also requires that a version of the system can be
can give an indication of defect levels in the final product    moved to a testing environment at will. When defects are
and eliminating defects early is less costly [24]. Tracking     found they must be identified with the exact version of the
defects is almost as important as finding them in the first     system that is under test. Especially in the case of
place. Without tracking, the same defect might be “found”       common ownership of code, writing proper change notes
over and over again, and a simple defect count would be         to the source code control system is important. It can save
misleading. Tracking should also facilitate learning about      time in forming an understanding of how the changes
the testing process for improvement purposes.                   might have influenced other parts of the system.

4.4. Mini-milestones                                            4.5. Summary and lessons learned

   In order to have a better indication of the status of            The tentative framework for managing software
development and thus better control the development             product development in small companies combines
effort, mini-milestones are used, for example in the form       business and process management for developing high-
of daily builds, as in the case of Microsoft. At Microsoft      quality software products that fulfil market requirements.
the daily build - daily test cycle makes early detection of     Strategic release management is the interface between
defects possible. If something breaks the system, the           business management and product development taking a
defect must have been introduced the same day, which            long-term view to release management. This means
makes finding the defect easier.                                processing the available market information and making
   In XP the idea of “test first” is introduced. The idea is    decisions about the content, role and timing of each
to write a unit test for every production method that could     individual release project.
possibly break. The tests should be written before the              The products are developed in release projects in an
code is written, serving at the same time as a specification    iterative and incremental fashion. The basic idea of an
or explanation for the methods and features. The unit tests     iterative and incremental development process is to
are then supposed to be running at 100 % all the time. If       deliver early to get user feedback on the system. At the
something breaks the system, a test is written that will        same time technical feedback on system performance or
detect the defect before it is fixed. Automated testing         other non-functional aspects can be made available. The
gives confidence to refactoring, since the tests should pick    feedback is used in planning the subsequent development
up any defect introduced to the system. Another                 cycle(s). Frequent integration of the system, or mini-
interesting practice in XP is pair programming, where two       milestones, such as daily or weekly builds, is used to get a
persons sit at the same computer. One person writes the         better indication of system status during development.
code and the other person watches, in principal doing           This way project management finds early warning signs
inspection online. This should result in better quality code    and can take proper controlling actions.
[23].                                                               Change management concerns the entire development
   Source code control or configuration management              effort, starting from requirements and going down to the
becomes crucial when we use practices like Microsoft’s          test cases and source code. Depending on what details the
daily build - daily test. Also, the more often we make          changes concern, the practices differ. If requirements
releases, the better we have to be able to manage the           change, they may influence anything from the architecture
source code. One would think this all seems very                of the system to just a part of a module. Other changes,
straightforward and clear, but we have observed that in         like code changes, seem to be of less impact and
practice source code control is not properly done, at least     importance, but they should also be documented in a
in many small companies. The main reason seems to be            commonly agreed way.
that although everyone uses tools like CVS, the practices           One might assume that managing change gets easier
have not been agreed upon, which leads to almost as             the smaller the development team is. That is partly true,
many different practices as there are developers. We            since the team is very often co-located, which improves
noticed one instance of this in a company that was              communication between the members of the team. But
confident about their source code control. When they            there will always be a need to write down the changes,
started doing more rigorous defect tracking, they suddenly      because leaving the details to memory only is very risky.
noticed that the already fixed defects repeatedly popped            The organization should establish commonly agreed
back into the system. This happened because some of the         upon rules and guidelines to align the efforts of
developers did not check in their code or update to             individuals and teams. Each rule should have a tolerance
Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

level attached to it, so as to show how strictly it must be       picking one may require picking a bunch of others for
followed and how much freedom each person has in                  consistency. That is why the idea of families of practices
applying that rule. For example, coding conventions may           or methodologies for different situations is appealing.
be very strict to facilitate easy maintenance of the                 An interesting question for further work is the
software, whereas more freedom can be given on, e.g.,             scalability of the framework. Cockburn’s ideas of
choosing the code-writing tool.                                   methodology families are appealing and we want to look
   One of the main lessons we have learned so far is that         into what it might mean in terms of our framework. This
establishing a common language is one of the most                 might also solve the issue of prioritizing and sorting the
valuable and tangible results of applying “process                details.
thinking” in an organization. We thought that in a small             Currently we are working on developing and
company people communicate and interact with each                 implementing a product roadmapping process for strategic
other more frequently thus almost automatically creating          release management into two of the companies we work
a common language, but we were proven wrong. For                  with. We are also looking closely on testing and defect
example, when we started developing the product                   tracking.
roadmapping process for strategic release management,
we observed that different people were using different            References
terms for the product parts, even within the product
development team. Creating a conceptual model of the              [1]   Bays, M.E., Software Release Methodology, Prentice Hall,
product that all people could agree upon and understand,                Upper Saddle River, 1999.
facilitated more meaningful discussions and decision-
making concerning the product and its future releases.            [2]   Beck, K., eXtreme Programming eXplained, Addison-
The same has applied to, e.g., quality assurance.                       Wesley, Boston, 2000.

                                                                  [3]   Brodman, J.G. and D.L. Johnson, “What Small
5. Discussion and further work                                          Businesses and Small Organizations Say About the
                                                                        CMM”, In Proceedings of ICSE-16, 1994.
    In this paper we have presented work in progress in
                                                                  [4]   Brooks, F.P. Jr., The Mythical Man-Month: Essays on
our research project where we are developing a
                                                                        Software Engineering, 20th anniv. ed., Addison-Wesley,
framework for managing software product development                     Reading, 1995.
in small companies. The framework is still tentative, and
some issues that we know are important have been left out         [5]   Carnegie Mellon University / Software Engineering
so far. As an example, measurement is not discussed at                  Institute, The Capability Maturity Model: Guidelines for
all. On that front we have been working for a longer time               Improving the Software Process, II. Series, Addison-
on a tool set for the creation, management and use of a                 Wesley, 1995.
measurement system. We plan to continue and integrate
                                                                  [6]   Cockburn, A., “Designing a light methodology”,
our earlier work on measurement into this framework.                    Presentation 1998, http://members.aol.com/humansandt/
    We also plan on adding more detail to the framework                 crystal/tutorial/methodology2.ppt, Cited 17.3.2001.
as we deepen our understanding of the challenges of
managing software product development, as well as find            [7]   Cooper, R.G., Winning at New Products, 2nd ed, Addison-
workable solutions. The details will be prioritized and                 Wesley, Reading, 1993.
most likely sorted in some kind of hierarchy for different
                                                                  [8]   Cooper, R.G., S.J. Edgett and E.J. Kleinschmidt, Portfolio
situations and needs.                                                   Management for New Products, Addison-Wesley,
    Alistair Cockburn has developed the Crystal family of               Reading, 1998.
methodologies [6], where he uses three dimensions for
methodology selection: the number of people involved in           [9]   Cusumano, M.A. and R.W. Selby, Microsoft Secrets, The
the project, the criticality of errors, and where the priority          Free Press, New York, 1995.
of the project lies (e.g. productivity, legal liability, etc.).
                                                                  [10] Cusumano, M.A. and D.B. Yoffie, “Software
The more people are involved in a project, the more
                                                                       Development on Internet Time”, IEEE Computer, Vol.
formal the communication to coordinate efforts has to be.              32, No. 10, 1999, pp. 60-69.
If a system is life-critical, verification and validation
practices must be extensive and rigid, and so on.                 [11] DeMarco, T. and T. Lister, Peopleware: Productive
    These are views we are looking to incorporate into our             Projects and Teams, 2nd ed, Dorset House Publishing,
framework in the future. One early temptation has been to              New York, 1999.
create a list of best practices from different sources. The
list would then be used as a source to pick practices when
needed. Unfortunately, practices are often interrelated and
Copyright 2002 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
7 – 10, 2002, Big Island, Hawaii.

[12] Englund, R.L. and R.J. Graham, “From Experience:           [19] Shenhar, A.J., “From Theory to Practice: Toward a
     Linking Projects to Strategy”, Journal of Product               Typology of Project-Management Styles”, IEEE
     Innovation Management, Vol. 13, No. 1, 1999, pp. 52-64.         Transactions on Engineering Management, Vol. 45, No.
                                                                     1, 1998, pp. 33-48.
[13] Highsmith, J.A. III, Adaptive Software Development: A
     Collaborative Approach to Managing Complex Systems,        [20] Spenser, L.M., S.M. Spenser, Competence at Work:
     Dorset House Publishing, New York, 2000.                        Models for Superior Performance, John Wiley & Sons,
                                                                     New York, 1993.
[14] Jacobson, I., G. Booch and J. Rumbaugh, The Unified
     Software Development Process, Addison-Wesley,              [21] Wheelwright, S.C. and K.B. Clark, Revolutionizing
     Reading, 1999.                                                  Product Development, The Free Press, New York, 1992.

[15] Kerssens-van Drongelen, I.C. and A. Cook, “Design          [22] Wiegers, K.E., Creating a Software Engineering Culture,
     Principles for the Development of Measurement Systems           Dorset House Publishing, New York, 1996.
     for Research and Development Processes”, R&D
     Management, Vol. 27, No. 4, 1997, pp. 345-357.             [23] Williams, L., R.R. Kessler, W. Cunningham and R.
                                                                     Jeffries, “Strengthening the Case for Pair Programming”,
[16] MacCormack, A., R. Verganti and M. Iansiti,                     IEEE Software, Vol. 17, No. 4, 2000, pp. 19-25.
     “Developing Products on ‘Internet Time’: The Anatomy
     of a Flexible Development Process”, IEEE Engineering       [24] Yourdon, E., Death March: The Complete Software
     Management Review, Vol. 29, No. 2, 2001, pp. 90-104.            Developer’s Guide to Surviving “Mission Impossible”
                                                                     Projects, Prentice Hall, Upper Saddle River, 1999.
[17] McCormick,     M.,     “Programming     Extremism”,
     Communications of the ACM, Vol. 44, No. 6, 2001, pp.
     109-111.

[18] Rautiainen, K., M. Nissinen and C. Lassenius, “Improving
     Multi-Project Management in Two Product Development
     Organizations”, In Proceedings of HICSS-33, 2000.
