---
title: "Increasing Understanding of the Modern Testing Perspective in Software Product Development Projects"
publication: "Hawai'i International Conference on System Sciences (HICSS) Proceedings"
date: 2003
url: https://drive.google.com/file/d/1JONa8kSIuJ7bCfYBp3eQurWMkSeHEGKK/view?usp=sharing
source_retrieved: https://drive.google.com/file/d/1JONa8kSIuJ7bCfYBp3eQurWMkSeHEGKK/view?usp=sharing
kind: research paper
language: en
---

# Increasing Understanding of the Modern Testing Perspective in Software Product Development Projects

*Hawai'i International Conference on System Sciences (HICSS) Proceedings — 2003*

Source: <https://drive.google.com/file/d/1JONa8kSIuJ7bCfYBp3eQurWMkSeHEGKK/view?usp=sharing>

> Retrieval note: text extracted from the Google Drive PDF.

---
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

Increasing Understanding of the Modern Testing Perspective in Software Product
                             Development Projects
               Maaret Pyhäjärvi                                       Kristian Rautiainen and Juha Itkonen
            Conformiq Software Ltd.                                    Helsinki University of Technology
   Stella Terra | Lars Sonckin kaari 16,FIN-                      Software Business and Engineering Institute
            02600 Espoo, FINLAND                                    POB 9600, FIN-02015 HUT, FINLAND
      Maaret.Pyhajarvi@conformiq.com                                       firstname.lastname@hut.fi

                        Abstract                               that the required level of quality is achieved. QA goes
                                                               more easily hand in hand with development as the
   Testing can be difficult to integrate into software         approach in both is constructive. In testing, the mindset
development. Approaches to software testing in relation        used is destructive as the goal of testing is to find errors.
to implementing software are based on the V-model of           It has been argued [15] that the attitude towards seeing
testing. The software process behind the V-model is the        defects is essential for success in finding the defects and it
traditional waterfall model, and as such the traditional       is the core of modern testing approaches. Traditionally,
testing approaches cannot take iterative, incremental and      testing is defined in a narrow sense as “execution of a
agile approaches to developing software into account           program in the intent of finding errors” [15]. The modern
well enough.                                                   definition of testing, more easily adopted by people
   In this paper, we describe the use of a general iterative   viewing themselves as test professionals, defines testing
and incremental framework defined for controlling              as “the process of planning, preparation and measuring
product development—4CC—from a modern testing                  aimed at establishing the characteristics of an information
perspective. The framework provides a common language          system and demonstrating the difference between actual
in which the implementation details and pacing as well as      and required status” [18]. In the wider context testing and
testing details and pacing in software product                 QA activities are converging, QA taking more of a
development projects can be communicated. Viewing              process improvement perspective and testing being part of
testing through a general iterative and incremental            QA. Both QA and testing are seen as activities starting
framework adds to understanding how the testing process        right from the beginning of the project. In this paper, the
should be defined and improved in relation to the              focus is on understanding the testing perspective, since in
software development process. Additionally, best               practice—especially in small organizations—testing as a
practices for testing are identified.                          means of finding defects would be the part to start QA
                                                               related activities from.
1. Introduction                                                   In larger organizations, QA and testing are often
                                                               responsibilities that are organizationally separate from the
                                                               actual development. Testing is organized as a sub-project
    The importance of quality assurance (QA) and
                                                               within the development project. In a small company
software testing is recognized in SME’s as well as in
                                                               testing needs to be more integrated to the development
larger organizations. These activities are an integral part
                                                               process as there is not a separate testing group due to
of the software development and releasing a product to
                                                               limited resources. Testing activities are conducted by the
the market, and should be included in the software
                                                               same people doing all other tasks, with mere change of
development project from the beginning. However, QA
                                                               role. This is not, however, the same as the developers
and testing can be difficult to integrate into the software
                                                               testing their own code; some level of independence in
development. They are easily left to just occur at the end
                                                               testing is also aimed for in a small company.
of the development project, especially if the resources are
                                                                  If development and testing within development are
scarce, and the pressure is on time-to-market and all effort
                                                               separated responsibilities, the project manager would
is focused on implementation.
                                                               choose a development model applicable for the situation
    The essential difference in QA and testing, as
                                                               at hand. The project manager quite often understands that
understood by testing professionals, is the attitude. When
                                                               testing is important and should be included in the project,
assuring quality, you are building in quality and assuring
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

but as the responsibility of testing details is given to a test   between implementation and testing to successfully
or quality manager, the lack of testing detail in software        control the whole project.
process models is emphasized. The test manager bases his              In the field of software testing, the V-model is the
testing approach on the V-model as it is the state-of-the-        state-of-the-art taught on practically every course on
art in testing. The V-model in its turn is based on the           testing. The V-model—presented in Figure 1—splits the
waterfall model and thus is difficult to use in                   testing process onto levels on which testing is carried out
communicating both the iterative and incremental nature           incrementally in conjunction with system implementation.
of a project as well as the need of rework as defects are         The V-model starts from the smallest pieces possible for
found in an environment where an incremental software             testing and moves on to larger pieces, reflecting the
development lifecycle is used.                                    different viewpoints of testing in different levels of detail.
   In the ongoing SEMS (Software Engineering                          Notice that the flow of abstraction in testing is reverse
Management System) research project we are studying               to the flow in implementation where the custom is to start
software engineering in small companies in the software           from high abstractions and move towards more and more
product business. The need to understand and improve the          concrete details. The reason for starting the testing from
testing process has become evident in the interviews and          individual modules (and not, for instance, from user
case work conducted with our pilot companies. When                requirements) is the organization of labor. It is much
taking the iterative and incremental approach to software         easier to find and fix defects in small units than in large
development and the V-model of testing, we noticed                entities, and the testing of large entities can be carried out
significant difficulties in understanding the details of the      more systematically if it is known that their sub-units
testing perspective in the overall picture without testing-       have already been tested. Planning testing should,
specific expertise. The problems in the use of the V-             however, flow in the same order as implementation. The
model have been recognized in the testing community as            V-model implicitly shows how the testing phase can—
well [9].                                                         and should—be taken into account much before there is
   In this article, we discuss the changes needed so that         some source code to actually be tested.
the modern testing perspective could better be understood
by all roles involved in a software product development
                                                                           Requirements                      Acceptance
project. We do this using the 4CC framework [20], which
provides a structure through which the roles involved can
more easily communicate.
                                                                               Specification                 System

                                                                       BUILD
2. Using the V-model – Why is it Not                                                                                      TE S
                                                                                                                              T
   Enough?                                                                          Design               Integration

   In software process research, many different software
process models have been suggested. Starting with the
                                                                                       Coding             Unit
code-and-fix model, adding structure by splitting the
process to sequential tasks to form the waterfall model
[22], noticing the need and cost of change within a                            Specifications -> Planning -> Testing
development project, resulting in models such as the
spiral model [4] and different other iterative and                                Figure 1 V-model of Testing
incremental models, e.g. [5;8]. Latest ones in the field are         The V-model is an extension of the simple waterfall
so called agile process models [3;7;23], basing their             model, where each process phase concerned with
agility on short increments and intense customer                  implementation has an associated verification and
collaboration.     Software       development        models       validation phase called test level. From a testing point of
acknowledge testing as an integral activity, but cannot           view, testing on each level should be planned and
give testers much detail on how to structure their work.          controlled to avoid overlapping. Traditionally the
   Looking specifically at testing in the perspective of a        individual test plans for the test levels are seen as the
test manager, testing needs a model that is focused on            links between these activities, coordinated with a master
driving the testing-specific efforts. In situations where it      test plan.
is not applicable to have a subproject for testing and a             The V-model is intuitive and easy to explain, even to
separate test manager for the subproject, the project             people who have never heard of a software development
manager needs to consider testing in more detail in               process model. This may be the case when persons with
relation to implementation details. The project manager           specific domain expertise in the use of the system are
needs to understand expectations and dependencies                 needed in testing. The V-model essentially brings forth
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

two important points: testing a smaller part before putting     process model context, the detailed implementation
it into a larger system is a good approach and testing          documentation plays a smaller role but testing still has its
efforts can start with planning as soon as the higher level     place and can take place with the lesser amount of
requirements have been identified. The V-model provides         documents.
a common terminology for testing in the form of test               The V-model tends to emphasize verification (are we
levels.                                                         building the product right?). However—especially for
    The V-model as a basis for testing actitivities has been    product business—emphasis on validation (are we
strongly criticized in [14]. The V-model, just as any           building the right product?) in testing has grown [9;24]
testing model created as an extension to software               and testing needs to assess both perspectives.
development models, ignores the fact that software is              A manager experienced in organizing testing does not
developed in a series of handoffs, where each handoff           organize testing efforts the way that the V-model may
changes the behavior of the previous handoff. The models        suggest if interpreted strictly. However, it has been our
tend to rely on the existence, accuracy, completeness, and      experience that the expertise to avoid the pitfalls may take
timeliness of development documentation. They assert            time to form. Using the V-model as a basis for defining a
that a test is designed from a single document, without         testing process may create an inflexible process to a place
being modified by later or earlier documents, or assert         where agile or incremental approaches would be more
that tests derived from a single document are all executed      appropriate. Testing literature and courses mostly rely on
together. For example, finishing all module testing prior       the V-model and even imply that the waterfall method
to moving to integration testing may be implied in the V-       would be the most current lifecycle model [12]. However,
model steps, but that is not a good approach.                   incremental development is an increasingly popular mode
    The V-model as such looks like a tidy process, but          of development [13] and needs to be addressed also in a
communicates change poorly. This is due to the built-in         testing context [6;21]. Basing testing on the expectations
waterfall model assumption. A less experienced test             set by the V-model in such a context is difficult. Still, the
manager may assume that the implementation-related              V-model forms the essential basis for any testing
documentation to base testing on is more finalized than it      activities taking place. Therefore the test manager needs
is in practice at time of starting test planning. It may be     experience on different process models and their
insufficiently communicated          which      parts,   e.g.   implications to testing in order to be able to apply the V-
requirements, are more finalized than others. This leads to     model wisely, usually skipping all details except emphasis
focusing the already scarce testing resources based on          on early test planning and the need of test levels. The V-
outdated information to unproductive work. If                   model as development model fits situations in which
implementation documentation has not matured prior to           changes must be managed, for example perhaps with
defining test cases to base test execution on, it may not be    situations in which a fixed cost project is undertaken and
a good approach to write detailed test cases. Due to            any change requests from the customer will carry a price
changes later on during the project, the test cases could       tag.
need considerable rework. It has been suggested that the           Understanding how tests should be grown and how
V-model’s early test planning approach would help               constant regression testing is organized between builds is
programmers to avoid defects by using detailed test cases       a challenge in practice. Communicating all this requires a
testers have written based on first versions of                 more dynamic approach.
documentation [9]. However, reviews and inspections are
likely to be more efficient in order to help correct defects    3. Using the 4CC from a Testing Perspective
early than relying on pre-writing tests that will never be
run [9]. Furthermore, testing is supposed to find defects,         In efforts to understand software product development
and finding a defect may put one back to the requirements       and how to control it, a framework for managing software
definition phase. Defects also need to be verified and          product development was introduced, called 4CC (Four
corrected, and the software tested for regression, still not    Cycles of Control) [20]. With the limitations in the V-
re-executing all test cases, which might take too long a        model as described above, we suggest that the modern
time.                                                           testing perspective can better be communicated through
    Testing activities in the V-model take a document-          the 4CC framework, which emphasizes pacing that sets
driven approach not always feasible in practice. For small,     the basis for all testing activities, and provides a structure
co-located teams with little change in team composition         through which the roles involved can more easily
the need for documentation is smaller than for large and        communicate. The test levels are continuous flows of
distributed teams or teams with high staff turnaround. In       activities that need to be structured through setting up a
all cases, the documentation produced should serve an           rhythm.
actual need and the need should show in keeping the                In ongoing research, we are focusing on small software
documentation up-to-date. Especially in agile software          product companies, and working on understanding the
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

connections of the company’s business model (for more                   As discussed above in section 2, the details of testing
information on business models see [19]) to its software             provided in software process models do not help testers to
product development process. In that context 4CC has                 understand their role in relation to the process. A tester’s
been introduced and it is continuously developed in co-              role is to find and report defects and verify that the
operation with Finnish software companies to better                  reported defects have been resolved, either by a
understand its operational aspects. 4CC is a high-level              programmer fixing them or by management deciding that
iterative and incremental framework, and as such can be              they will not be fixed for some reason. The 4CC
applied in many contexts, but our efforts to bring detail to         framework helps in understanding testing in relation to
it have been focused on the small product company                    other software development activities. It sets four
perspective. The key idea in our research is that different          timeframes on which one needs to address certain issues
software companies produce different kinds of products               in development. The timeframes—depicted as cycles—
for different customer groups, and the approach for                  are presented in Figure 2. The leftmost cycle, named
creating software should fit the company's business                  Strategic Release Management, deals with the release
model, and take into account the influences of product               project portfolio and is the interface between business
perspective and team size. By understanding the                      management and product development deciding on all
possibilities and constraints set on the product                     ongoing major activities requiring attention from product
development process by the business model, software                  development. Release Project Management deals with
process improvement can be focused on the essentials                 issues on the level of individual projects aiming for a
from the business perspective and thus improve product               product release. Increment Management deals with
quality and profitability.                                           managing individual increments producing a part of a
    Testing is one perspective emphasized in our research            release project’s deliverables. Mini-milestones deal with
of small product businesses, as it is viewed as an                   structuring and pacing the daily work for different roles
important area with many challenges in practice by both              participating in the product realization process. Different
the researchers and the pilot companies involved in the              cycles provide different levels of abstraction to facilitate
research. Bringing together development and testing                  control and flexibility.
perspectives in product development in a small company                  The 4CC model adds an important perspective for
context poses challenges, as the traditional approaches of           testing compared to the V-model. The V-model focuses
separate test groups presented in testing literature are not         on a single project and as such, naturally leaves out
applicable as such. We need more thorough understanding              essential co-operation between projects. Projects
of the reasons why the suggestions have been given in                following each other in time could, especially in product
order to scope them to a small company context.                      business, benefit a lot from the results and lessons learned
    We view testing in the broader perspective of                    from previous projects. Projects ongoing simultaneously
maximizing customer satisfaction and providing feedback              could be managed together for more efficient use of
for process refinement, in addition to just detecting and            testing resources. It is important to see testing related
getting defects corrected in the software. The testing               activities in projects as a portfolio from which all ongoing
process needs to be examined together with the overall               projects can benefit from through reuse and experiences.
project and product management processes of the firm.                   In the testing community, a so called multiple V-model
Testing activities include planning, management,                     has been applied by consultants in an iterative and
implementation and support needed from a tester’s                    incremental context, showing that for testing the number
perspective. Information flow and pacing are important               of deliverables to base testing on increases. Using the
for testing activities. Testing by executing a program               multiple V-model one draws a V for each iteration and
needs the program to be implemented to some extent. Test             shows time as the horizontal axis. The added detail
case design relies on having information on the features to          depicts writing the documents that testing is based on in
be implemented.                                                      smaller pieces, but resulting in a presentation that is
                                                                     difficult to communicate and understand and shares the
                                                                     limitations of the V-model.
                                                                        On the project level, the test lifecycle depicted by a test
                                                                     level is too simplistic to provide support for actual work
       Strategic          Release
       Release            Project
                                       Increment   Mini-milestones   that is based on small handoffs. The test levels in the V-
                                       Mgmt
       Management         Management                                 model depicts in iterative and incremental context a
                                                                     testing effort that start in the beginning of the project with
                                                                     planning and proceed to execution as soon as a part has
                                                                     been implemented. The need for managing all testing
                                                                     levels separately depends on the process used. In extreme
            Figure 2 The 4CC Framework                               programming, two testing levels are applied: unit testing
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

and acceptance testing, with the first combining goals of           ACCEPTANCE TESTING                                  E
the two lower levels and latter combining goals of the two                                                              D
higher levels. In systems with challenging integration the
                                                                                                        C               C
integration level may be managed separately.
                                                                                            B           B               B
    Figure 3 describes how testing work is split in iterative
                                                                                            A           A               A
and incremental development to various testing levels.
The figure depicts relationships between modules A-E                SYSTEM TESTING                                  E
and how these are collected together for higher testing
                                                                                                                    D
levels. Test execution starts as soon as the first modules
                                                                                                C                   C
are implemented. New handoffs which correspond to
                                                                                       B        B                   B
mini-milestone cycles of the 4CC model trigger new
                                                                                       A        A                   A
testing activities. Modules A and B are unit tested prior to
integrating them together. In integration testing, the focus        INTEGRATION TESTING                     D
                                                                                                                E
is on verifying that the added module works together with                                   C               C
                                                                                                                C
the current version of the whole system. In system testing,
                                                                                  B         B               B
the whole system is verified to planned extent, with focus                                                      B
                                                                                  A         A               A
on the whole system, not just the latest addition.                                                              A

    There are few points that need to be stressed in Figure          UNIT TESTING
3. Implementation and testing of modules D and E are                  A       B         C           D
depicted to be separate but partly overlapping. In
                                                                                                        E
integration testing, these are presented to be integrated to
the latest available baseline that was completed at the
                                                                                                                            Time
time of starting the module. In system testing, the
                                                                 Figure 3 Test Levels in Iterative and Incremental
modules D and E are not brought to the system separately,
                                                                                     Development
but as a group. A typical situation would be that the two
                                                                   Understanding the modern testing perspective of test
modules are created by separate developers individually.
                                                                levels depicted in Figure 3 results in noting that the
Acceptance testing level is typically the final level of
                                                                system to be tested grows all the time. Very soon in the
tests, but it essentially is also an ongoing activity. The
                                                                development, it becomes impossible to re-execute all
different levels need to be managed as a whole to avoid
                                                                defined tests on one build, but the tests need to be split on
unnecessary rework—each level focuses on testing
                                                                various builds over time. As the pile in the figure grows,
different aspects as described with the V-model.
                                                                managing the testing effort focuses on creation of test
Typically, the different levels in testing would apply
                                                                suites—collections of test cases—and prioritizing them,
different test environments. Rework due to regression
                                                                as controlling individual tests would result in detail that
testing takes place on the test levels. Change in the tested
                                                                may distract the overall view on control.
modules results in need of retesting through the whole
                                                                   Testing     is   essentially about        feedback      to
pipe effectively.
                                                                implementation. Testing needs to be managed based on
    The test levels just as the V-model defining the levels
                                                                small handoffs, building a larger whole. Testing should be
have their roots in the project business. In project business
                                                                reactive to handoffs. Thus many testing details are best
the acceptance test level is emphasized as it is the
                                                                communicated on the mini-milestone level as the daily
customer’s perspective in verifying that the software
                                                                reaction options. These reactions need to be synchronized
developed fulfills the customer’s needs. The essence of
                                                                to the organization’s pacing as well as the developers’
acceptance testing is that it is the final testing prior to
                                                                pacing. Managing testing in a project needs to build the
accepting the software and it should be characterized by
                                                                proper relationship between control and flexibity. How
relatively small number of defects. The focus on
                                                                this rhythm has been included in the Microsoft’s synch-
acceptance test level is on fulfilling the customer needs
                                                                and-stabilize model is discussed in the following section
and found defects should be related to that. Essentially at
                                                                by describing synch-and-stabilize in 4CC.
the end of acceptance test, the test is the final check
before moving the system into production. In product
business the role of acceptance test level is two-fold. First   4. Modern Testing Best-Practices and Synch-
of all, it stresses the user perspective, both usability and       and-Stabilize Testing
applicability, throughout the development. Secondly, it is
the final checks that are made for releases.                       Understanding the pacing of development is essential
                                                                for successful testing. To better understand the modern
                                                                testing perspective and its implications in managing
                                                                testing in projects, we have identified the best practices in
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

modern testing to characterize how testing could be              willing to use. Testing does not necessarily need to be
included in the product development lifecycle within the         document-driven, the need for documents as a basis for
4CC framework. As a tangible example of the ability to           testing depends on the context.
add testing detail in 4CC we have dissected Microsoft’s              Pacing test activities is important in order to be able to
testing approach in the Synch-and-Stabilize process as           understand and control testing activities on very short
defined in [5]. A growing trend in the field of testing is a     cycles. Testing activities are highly dependent on other
so-called context-driven school of testing, asserting that       project activities and thus the need for agility is high.
there are only good practices in context, but no best            Testing efforts need to be split over time and on different
practices [9]. However, the practices presented here are         builds, as execution of all test cases on a certain build is
starting points to tailor the approach for test management       not applicable [2]. The number of test cases is likely to be
in a specific context instead of directly applying               large and all test cases take significant time to execute.
assertations in the V-model.                                     Found defects need to be fixed concurrently with test
   The modern testing perspective can be characterized           execution proceeding and corrections released to re-
by its best practices. We have identified five main best         testing. The risk of many corrections integrated into a
practice areas, each with several details, from recent           build after having waited for test round on a previous
testing literature [10] and mirrored these to the                build to finish increases the risk of noticing side effects of
operational test management approaches in case                   defect corrections late. The test environment should exist
companies[9;11;12;16-18]. The best practices selected are        separately from the developers environment and should
based on the case work conducted at pilot companies.             change only in the agreed pace. Daily rhythm through
They represent common ways of integrating testing into a         knowing the rules of the game as dependencies and
software project. Basing testing on product and business         deadlines facilitates efficient testing.
risk is a main driver behind test efforts. Testing should be         Traceability and maintainability includes ways of
based on product and business risks, as exhaustive testing       connecting testing to requirements as well as
is not feasible as the number of combinations to verify in       considerations on the ability to maintain and grow the
a non-trivial program is very high. Testing needs to take        tests. Test cases should be grouped into test suites of
into account the changing risks as technology and market         different priorities, different functionalities and different
matures, and needs agility planned in the testing process        uses (e.g. smoke test, regression test) to facilitate control.
so that adjusting is possible. The most important risks for      A traceability matrix between the test cases and
the product from the user’s perspective should be                requirements should be kept up-to-date in order to know
addressed first. This should be visible both in prioritizing     if tests need to be updated, as well as what tests need to be
test cases and executing them so that high-priority tests        updated, to the changing requirements. A light-weight
will be run first, as well as in prioritizing different          approach to defining test cases is needed. Test case
hardware and software platform combinations testing will         definition should focus on requirements that have matured
be conducted on, as all combinations are not possible to         to the level that they will actually be implemented. The
test.                                                            number of test cases needs to be minimized and focus of
   Destructive attitude drives the testing effort as the         tests addressed. Quality of testing determines the quality
main goal of testing is to find defects as early as possible     of evaluation on product quality and needs to be assessed
to facilitate timely release with aimed quality level. In        continuously. Test reporting should be done on a regular
order to include the destructive attitude, there is a need for   basis but carry only the necessary overhead. The number
independence in testing, as one tends to be unable to see        of test environments is increasing. Testing important user
one’s own mistakes. As defects are fixed, new rounds of          environments is spread over the course of the project and
previously executed tests need to be executed to find            should be focused on selected environments based on
defects that have been caused by defect fixes, which             environment risk-based priorities. It is important to be
happens easily as the complexity of the code makes it            able to connect the testing performed, the time the testing
difficult to anticipate all dependencies.                        was performed and the environments testing was
   Early involvement of all test levels is important. Each       performed on, if e.g. the customer base changes and thus
developed feature needs to be tested on all levels from          the priorities of environment change.
unit to acceptance and the different levels exist                    Looking at Synch-and-Stabilize as defined and detailed
concurrently and continuously throughout the project.            in [5], an emphasis on testing in the product development
Reviews and inspections are a part of testing as they help       process is evident. Redefinition of Microsoft’s
in noticing the defects early. Testing needs to have an          development process resulting in definition of synch-and-
emphasis on validation in addition to verification as            stabilize started with a “zero-defects memo”, pointing out
creation of defect-free software that no one will use is not     the costs of defects to Microsoft’s customers. In synch-
worth the effort—the software needs to be validated that         and-stabilize, testing exists as a separate function with
the features it provides are the ones that the users are         dedicated testers, integrated into the everyday product
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

implementation, paced by daily builds. The aim is to find                                                                   reports to highest level management and related projects.
defects as early as possible.                                                                                               Program reviews are conducted quarterly for each project.
   The goal of early test involvement included in the V-                                                                       The Release Project Management cycle is structured to
model is realized well as testing is integrated to software                                                                 three themes or phases. The project begins with planning,
implementation from the beginning and participates as its                                                                   is continued by 3-4 development subcycles and finished
own function in planning and scheduling the work.                                                                           with a stabilization phase. On the Increment Management
Different levels of testing are also applied, all taking place                                                              cycle each of the project phases have different kinds of
concurrently and continuously, feature by feature. Unit                                                                     tasks. Planning focuses on setting a project vision, a
testing is not formalized and is seen as the testing                                                                        skeletal functional specification that sets areas and
conducted by the programmer. However, developer                                                                             subareas for features and thus facilitate early
testing responsibilities include testing their own features                                                                 identification of test suites, and a master schedule,
running automated tests created by the testers frequently,                                                                  including testing activities estimated by people
usually on a daily basis. Programmers are paired with so                                                                    conducting the actual work later on. Next 3-4 increments
called “buddy testers”, and these testers do integration                                                                    each build and test a selected prioritized set of
testing with the help of the programmer on the feature on                                                                   functionalities of the product. The final increment’s theme
a private release before the feature is released to system                                                                  is stabilization, which includes testing the product as a
testing. Buddy testers form a testing organization for the                                                                  whole, and finding and fixing defects. The stabilization
project, coordinated by test leads and test managers that                                                                   phase goes hand in hand with beta testing, if one is
are responsible for system testing iteratively and                                                                          employed. Increments at Microsoft employ so called
incrementally. System testing examines the product from                                                                     buffer time for unexpected delays. The Increment
six perspectives, namely user perspective, international                                                                    Management cycle is also structured to three phases. The
perspective,      hardware       compatibility,       software                                                              development phase is concerned with the teams
compatibility, specification compliance and product                                                                         developing the deliverables for the increment. At the end,
stability. Acceptance testing at Microsoft includes                                                                         the increment is stabilized to required quality and buffer
usability testing to verify each feature, and beta releases                                                                 time is reserved as a contingency for unanticipated
that are employed to better understand dependencies of                                                                      problems.
different customer hardware and software platforms and                                                                         On a mini-milestone level, a tester chooses his task
defects manifesting only in some of these platform                                                                          based on the dependent activities in implementation.
combinations. Testing on different levels is not document-                                                                  When preparing for new testing, testers do general
driven as the V-model might suggest. The product is                                                                         reviews on previous project’s postmortem reports and
outlined in a product vision, its features are written down                                                                 reports from other testing groups, talk with product
in a functional specification as the project goes on and                                                                    support personnel and customers, review media
technical details are documented in the code using                                                                          evaluations, devise special tools or code routines to help
comments and a common style of coding.                                                                                      them test, study competitor products for new features,
                                                                                                                            develop testing strategy by identifying high-risk areas,
                                                                                                                            and review each other’s plans and scripts for
                                                         St
                                                           ab
                                                                ili z
                                                                                                                            completeness. Developers find more of their own defects
                                                                     a   tio
                                                                             n   Development                                than testers do, and only developers can prevent errors
                             Development
         Strategic Release                 Release Project                         Inc rement
                                                                                                          Mini-milestones
                                                                                                                            from happening in the first place. Code that is assumed
           Management                       Management                            Management

                                                                                                 Bu
                                                                                                     r
                                                                                                   ff e
                                                                                                                            difficult and code that is produced by new people is
                                                         Pla
                                                            nn
                                                              ing                Stabilization
                                                                                                                            reviewed by senior developers. If new functionality has
                                                                                                                            been coded and is to be integrated to the public release,
                                                                                                                            the tester focuses on testing the private release of the
                                                                                                                            “buddy developer”. After code has been integrated in the
  Figure 4 The 4CC Framework with Synch-and-                                                                                public release, testers execute tests and track defects
                 stabilize Details                                                                                          found in the test release and characterize them by feature
   All test levels are concurrent and continuous activities,                                                                area and severity. If coding is ongoing, the tester may
                                                                                                                            focus on defining tests for the functionality as well as
and can be better understood by looking at the project on
several levels through the 4CC framework presented in                                                                       automating tests. Online user documentation is tested just
Figure 4. On the Strategic Release Management cycle,                                                                        as the program itself. If the coding activity is defect-
Microsoft has twice a year highest level scheduling of                                                                      fixing, the tester focuses on verifying fixes as they
rolling out new products and setting their budget. Once a                                                                   become available in daily builds. On a weekly basis, a
year Microsoft updates its three-year product plans and                                                                     subset of tests is executed on a debug build with
their interdependencies. They use monthly project status                                                                    testability features helping defect location. System tests
                                                                                                                            go on continuously on daily builds. Pacing of testers
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

activities is dependent on the programmer’s activities. On      ratio, which is not feasible for a small company.
the other hand, rules apply to the other direction as well.     However, the software a small company is developing is
For some products, a rule on having 10 critical open bugs       probably not the size of Microsoft’s products either and
means interrupting development of new features until the        the size and complexity are issues to consider for different
critical bugs have been resolved to a level below the           instantiations of the best practices.
agreed limit.
   The number of testers Microsoft uses is significantly
                                                                      Table 1 Modern Testing Best Practices
more than what is traditionally the tester-developer ratio.
Especially it is more than what is possible in the small        Best Practice Area       Details
company context. At Microsoft, this has been a                  Basing testing on        Gaining understanding of
compromise in being able to change direction based on           product and business     changing product and business
market inputs as needed. The number of testers could be         risk                     risks
reduced if more upfront planning was introduced—more                                     Prioritizing test cases
time on architectural planning and detailed design work—                                 Prioritizing test environments
or if developers would be made to review their own code                                  Testing in order of priority
more. Reducing the number of testers would reduce the           Destructive attitude     Goal of finding defects
amount of flexibility in evolving features or components                                 Need of independence
incrementally. Testers are deemed relatively inexpensive        Early involvement        Reviews and inspections as a
compared to the cost of recalling and replacing products        of all test levels       means of finding defects early
because of major defects.                                                                Emphasis of both verification and
                                                                                         validation
5. Managerial Implications                                                               All test levels take place
                                                                                         concurrently and continuously
    A classic problem in testing is the difficulty of                                    Need of document-driven testing
communicating with the project manager when you are                                      needs to be assessed
taking the role of a test manager [1]. Expectations differ      Pacing test activities   Dependence on other activities
in used process model, produced documentation and                                        Rework due to defect corrections
readiness level of the documentation at a point in time.                                 Splitting test cases to builds over
This is, at least to some extent, due to the different models                            time
applied by the two perspectives. Another reason                                          Identifying daily tester tasks
suggested has been the project manager’s lack of                                         Controlled test environment with
knowledge in testing details [10].                                                       releases to testing
    In this paper, we have described the use of a general       Traceability and         Grouping tests into test suites
iterative and incremental framework defined for                 maintainability          Use of a traceability matrix
controlling product development—4CC—from a modern                                        Light-weight just-in-time
testing perspective. The framework provides a common                                     approach to writing test cases
language in which the implementation details and pacing                                  Test reporting on defined internal
as well as the testing details and pacing can be presented.                              releases
Based on our experience with our pilot companies,                                        Scheduling test suites to different
viewing both implementation and testing activities in the                                environments
4CC framework helps in understanding dependencies
between activities and the scope of time the activity is           The framework described has been created keeping the
related to.                                                     product development context in mind. However, the three
    Our research focus is small companies and within that       lower cycles describe pacing of a project and could be
context, we have identified best practices for testing. The     applied in understanding pacing of projects in project
best practices are summarized in Table 1. The best              business as well. Lately, the 4CC model has been applied
practices have been selected from testing literature based      to structure testing in companies other than small as well
on our case experience on what kind of approaches are           as other than those in product business. The 4CC
possible in the small product company context. However,         framework helps in structuring the complex testing effort
the same best practices can be seen in Microsoft’s Synch-       on several levels of abstraction, reminding of the
and-Stabilize development model and its testing details.        connection between these levels. It sets a common
Essential in synch-and-stabilize is the pacing set for          vocabulary in the pacing of the development efforts and
development, facilitating communication and co-                 helps in communicating different kinds of handoffs and
operation between implementation and testing.                   their rhythm. Especially in definition and communication
Microsoft’s approach employs a 1:1 tester-developer             of a test strategy 4CC has been effective. Understanding
Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
6 – 9, 2003, Big Island, Hawaii.

the forms in which the test strategy presents itself on          -     Explicitly encourage the use of sources of
different levels has helped in defining it.                            information other than project documentation during
    4CC is a framework for controlling work. It helps in               test design.
describing logistics in a project for testing as well as other   -     Allow the test effort to be degraded by poor or late
development-related work. The Test Management                          project documentation, but prevent it from being
Approach (TMap) model [18] describes testing in four                   blocked entirely.
dimensions: lifecycle, organization, techniques and              -     Allow individual tests to be designed using
infrastructure. It has a weakness in its lifecycle as the              information combined from various sources.
lifecycle assumes waterfall-like approach. Our                   -     Allow tests to be redesigned as new sources of
experiences point out that the added detail in the pacing in           information appear.
4CC that is critical for success enables communicating the       -     Include feedback loops so that test design takes into
modern testing perspective better. The other cornerstones,             account what’s learned by running tests.
namely organization, techniques and infrastructure,              -     Allow testers to consider the possible savings of
include important testing specific details that are placed             deferring test execution.
on the lifecycle.                                                -     Allow tests of a component to be executed before
    Pacing testing in relation to implementation is                    the component is fully assembled
important. Even though it may seem that there is a lot of            These are also important things for managers to
change to manage, a word of warning on an approach we            consider when tailoring the best practices in Table 1 to a
have seen in practice. In some cases there has been a daily      project-specific or company-specific instantiation.
build cycle but testers use biweekly builds to be able to            Test improvement models such as TPI (Test Process
execute all tests on one build. However, the                     Improvement) are attempting to phase test improvement.
implementation proceeds meanwhile and even though the            These models have their roots in CMM and base their
full round of tests have been executed, the latest build has     testing approach in the V-model, which we argue is not
changed significantly and would need to be tested for            sufficient. Viewing testing through a general iterative and
regression. This is one manifestation of interpreting the        incremental framework adds to understanding how the
V-model’s levels strictly.                                       testing process should be defined and improved in relation
    The V-model supports individual projects. With 4CC           to the software process. We are basing the test process on
we depict that it is important to also manage a portfolio of     iterative and incremental as well as agile software
projects. The software product lifecycle outlasts                development processes but also the waterfall model
boundaries of projects and when planning for testing, it is      would be applicable as a special case of a project with
important to consider if there would be synergies between        only one increment. We have conducted a benchmark of
the separate testing activities in projects.                     15 Finnish software development organizations’ testing
                                                                 with the TPI model and within this benchmark, reflected
6. Discussion and Further Research                               the results to the 4CC. The results of this benchmarking
                                                                 are currently under processing.
   We have presented the use of a framework for                      To help with business-focused process improvement
managing software product development in small                   and practice selection, we are working on evaluating
companies to increase understanding of the modern                software development processes from the perspective of
testing perspective in software product development              business fit and a business-dependent path for software
projects. The framework and its details are still tentative      process improvement from the basics. We are also
and our ongoing research both adds detail to it and              collecting a set of tools to support the instantiation of the
collects empirical data in using the described details in        framework in companies.
piloting companies. Test process definition and                      The details in 4CC are focused on small product
improvement research work continues and the best                 companies. However, the overall idea of pacing within
practices identified are further tested in companies. To         any project (3 lower cycles) applies just as well. The
better support testing, 4CC needs to be instantiated to          applicability has been tried in practice at Conformiq
detail in our case companies. The goals of the testing           Software Ltd.
model needed include [14]:
-     Force a testing reaction to every code handoff in the      References
      project.
-     Require the test planner to take explicit, accountable     [1] Bach, J., "James Bach on Explaining Testing to Them.
      action in response to dropped handoffs, new                    Helping Non-testers Understand and Support Your Work,"
      handoffs, and changes to the contents of handoffs.             Software Testing & QUality Engineering, vol. 3, no. 6,
                                                                     2001.
 Copyright 2003 IEEE. Published in the Proceedings of the Hawai'i International Conference on System Sciences, January
 6 – 9, 2003, Big Island, Hawaii.

 [2] Bays, M., Software Release Methodology, Prentice-Hall        [19] Rajala, R., Rossi, M., Tuunainen, V., and Korri, S.,
     PTR, 1999.                                                        Software Business Models: A Framework for Analysing
                                                                       Software Industry, Tekes, Technology Review 108/2001,
 [3] Beck, K., Extreme Programming Explained, Addison-                 2001.
     Wesley, 2000.
                                                                  [20] Rautiainen, K., Lassenius, C., and Sulonen, R., "4CC: A
 [4] Boehm, B., "A Spiral Model of Software Development and            Framework for Managing Software Product Development,"
     Enhancement," IEEE Computer, vol. 21, no. 5, 1988, pp.            Engineering Management Journal, vol. 14, no. 2, 2002, pp.
     61-72.                                                            27-32.

 [5] Cusumano, M. A. and Selby, R. W., Microsoft Secrets:         [21] Redmill, F., Software projects: Evolutionary Vs. Big-Bang
     How the World's Most Powerful Software Company                    Delivery, John Wiley & Sons, New York, 1997.
     Creates Technology, Shapes Markets, and Manages
     People, Simon & Schuster Inc, 1998.                          [22] Royce, W. W., "Managing the Development of Large
                                                                       Software Systems," Proceedings of Wescon, 1970, pp. 1-9.
 [6] Cusumano, M. A. and Yoffie, D. B., "Software
     Development on Internet Time," IEEE Computer, vol. 32,       [23] Schwaber, K. and Beedle, M., Agile Software Development
     no. 10, 1999, pp. 60-69.                                          with Scrum, Prentice Hall, 2002.

 [7] Highsmith, I. J., Adaptive Software Development: A           [24] Weinberg, G. M., The Psychology of Computer
     Collaborative Approach to Managing Complex Systems,               Programming, Van Nostrand Reinhold, New York, 1971.
     Dorset House Publishing, 2000.

 [8] Jacobson, I., Booch, G., and Rumbaugh, J., The Unified
     Software Development Process, Addison Wesley Longman,
     Inc., 1999.

 [9] Kaner, C., Bach, J., and Pettichord, B., Lesson Learned in
     Software Testing - A Context-driven Approach, Wiley
     Computer Publishing, 2002.

 [10] Kaner, C., Falk, J., and Nguyen, H. Q., Testing Computer
      Software, 2 ed., John Wiley & Sons Inc., 1999.

 [11] Kit, E., Software Testing in the Real World, Addison-
      Wesley, 1995.

 [12] Koomen, T. and Pol, M., Test Process Improvement: A
      Practical Step-by-step Guide to Structured Testing, ACM
      Press, 1999.

 [13] Marco, I. and MacCormack, A., "Developing Products on
      Internet Time," Harvard Business Review, vol. 75, no. 5,
      1997.

 [14] Marick, Brian, "New Models for Test Development,"
      Proceedings of Quality Week 1999, 1999)

 [15] Myers, G., The Art of Software Testing, John Wiley &
      Sons, New York, 1979.

 [16] Patton.R., Software Testing, Sams Publishing, 2001.

 [17] Perry, W., Effective Methods for Software Testing, Wiley,
      1995.

 [18] Pol, M., Teunissen, R., and van Veenendaal, E., Software
      Testing - A guide to the TMAP Approach, Addison-Wesley,
      2002.

View publication stats
