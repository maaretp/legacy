---
title: "Test Automation Process Improvement in a DevOps Team: Experience Report"
publication: "NEXTA 2020 (ICSE workshop)"
date: 2020
url: https://drive.google.com/open?id=1soKIBGN5cunqVFoiBtSEB4pVwNJfD8TZ
source_retrieved: https://drive.google.com/open?id=1soKIBGN5cunqVFoiBtSEB4pVwNJfD8TZ
kind: research paper
language: en
---

# Test Automation Process Improvement in a DevOps Team: Experience Report

*NEXTA 2020 (ICSE workshop) — 2020*

Source: <https://drive.google.com/open?id=1soKIBGN5cunqVFoiBtSEB4pVwNJfD8TZ>

> Retrieval note: text extracted from the Google Drive PDF.

---
Test Automation Process Improvement in a DevOps
            Team: Experience Report

               1st Yuqing Wang1∗                     2nd Maaret Pyhäjärvi1∗                   3rd Mika V. Mäntylä
    M3S research unit, University of Oulu                   F-Secure                    M3S research unit, University of Oulu
               Oulu, Finland                             Helsinki, Finland                        Oulu, Finland
            yuqing.wang@oulu.fi                   maaret.pyhajarvi@f-secure.com                mika.mantyla@oulu.fi

   Abstract—How to successfully conduct test automation process      be seen as “process for iterative software development and is
improvement (TAPI) for continuous development, consisting of         an umbrella over several other processes including continuous
iterative software development, continuous testing, and delivery,    integration, continuous testing, continuous delivery and contin-
is the challenge faced by many software organizations. In this
paper, we present an experience report on TAPI in one DevOps         uous deployment” [7]. However, based on many sources [8]–
team in F-Secure (a Finnish software company). The team builds       [10], despite the effort, not all software organizations are able
Windows application software and exists in F-Secure’s TAPI           to meet the purpose of TAPI, usually caused by inadequate
culture. The team self-reports high satisfaction and maturity in     implementation.
test automation for continuous development. To study their TAPI,        Several researchers have stated the importance of TAPI re-
we reviewed a collection of experience notes, team reflection
reports and telemetry result reports. Then several meetings          search to increase the likelihood of succeeding with TAPI [11],
were held to discuss the details. We found that based on             [12]. Since TAPI is a new trend in recent years, little empirical
the understanding of the team, test automation maturity for          research has been conducted on observing software organiza-
continuous development is defined as a set of indicators, e.g.,      tions that have been successfully carrying out TAPI and gain-
the increasing speed to release, improving the productivity of the   ing test automation maturity for continuous development [13],
team, high test efficiency. Second, the team indicated that a set
of critical success factors have a major impact on successfully      [14].
carrying out its TAPI, e.g., incremental approach, the whole            The purpose of this paper is to present an experience report
team effort, test tool choice and architecture, telemetry. Third,    on TAPI in one DevOps team at F-Secure (a Finnish software
we compare the TAPI practices in the observed team with the          company). The team builds Windows application software and
practices described in prior literature. The team believes that      exists in F-Secure’s TAPI culture. The team self-reports high
the existing test automation maturity approaches should include
the identified practices like the whole team effort to build a
                                                                     satisfaction and maturity in test automation for continuous
more comprehensive test automation improvement model for the         development. This paper aims to answer the research question:
software industry.                                                      • RQ1 - Perceived success factors: What makes TAPI
   Index Terms—Software, test automation, success factor, pro-             successful in the DevOps team at F-Secure?
cess, improvement, maturity, experience report
                                                                        The second author of this paper is an engineering manager
                          I. I NTRODUCTION                           who monitored TAPI in the observed team at F-Secure. She
                                                                     provided a collection of experience notes, team reflection
   Nowadays, software organizations bear the pressure to get         reports, and telemetry result reports. To answer the research
their products to the market quickly and deploy them fre-            question, we reviewed those materials and hold several meet-
quently [1]. Test automation has been widely applied to ensure       ings to discuss the details. The first author conducted thematic
consistent product quality in the frequent release cycles. How-      analysis to identify critical factors that make TAPI successful
ever, many organizations still have immature test automation         in the team on the available materials. Those factors were
processes with process-related issues such as inefficiency of        verified and revised by the second author to ensure the
test activities, heavy maintenance effort, slow feedback to the      accuracy and correctness. The detailed study results can be
development work [2], [3].                                           found in the remainder of the paper.
   According to the state of testing report 2019 [4], the               This paper is structured as follows. Section II introduces
software industry has been more and more concerned about             the background and related work that indicate the reason
test automation process improvement (TAPI). Many software            for our research. Section III introduces the research method
organizations are conducting TAPI aimed at achieving for             and process. Section IV presents the study results. Section V
continuous development [5], [6]. Continuous development can          discusses the implications to study results and threats to
  1 Contribute equally to this study                                 validity. Section VI concludes the study and illustrates the
  ∗ Corresponding author                                             future work.
                      II. BACKGROUND                                shared with all co-authors. Experience notes describe the
  This section reviews the concept of software test automation      evolution of TAPI practices from 2005 to 2019. They were
and related work conducted on TAPI research.                        created by the second author of this paper for purposes of
                                                                    this research. Software production snapshot data from 2019
A. Software test automation                                         was collected for sharing telemetry statistics, release and test
   Test automation is the use of tools (normally referred as        automation change log excerpts. The first and third authors of
test tools) to automatically test the applications in software      this paper studied those materials to familiarize with the case
development [15]. Similar to general purpose of software            and identify data answering research questions.
development, test automation follows a lifecycle which de-             In the second step, six online meetings among co-authors
termines how it begins, evolves, and ends [15], [16]. Test          were conducted via Skype. The duration was 55-67 minutes.
automation covers the entire software test process and consists     Before a meeting, a meeting guide was prepared to outline the
of the variety of testing activities, e.g., test case design,       discussion topics including, for example, when, why, and how
test scripting, test execution, test evaluation, to test-result     they do particular TAPI practices (recorded on the materials),
reporting [17].                                                     and what effect those TAPI practices have. During a meeting,
                                                                    we carried out the discussion around those topics. The second
B. Related work
                                                                    author took responsibility to explain the contents on company
   TAPI related topics have been studied by software engi-          experience materials and complement with details. Open ques-
neering (SE) practitioners and researchers for many years.          tions were asked for answering our research question. The
Many practitioners have published their TAPI related articles       notes were written down at a meeting. All meetings were audio
in blogs, magazines, SE related websites. For example, there        recorded. The audio records of meetings were transcribed
are such articles explain why and how TAPI should be carried        verbatim into text files.
out for continuous development [18]. Other studies (e.g., [19],
[20]) that summarize the benefits, challenges, general steps,       C. Data analysis
success factors of TAPI also exist.
                                                                       The text files that record the transcription verbatim of
   For TAPI research, based on our review on related work,
                                                                    meetings, meeting notes, as well as experience notes were
there are survey studies (e.g., [8], [21]) exploring the state of
                                                                    imported into NVivo (a qualitative data analysis software) [24].
art of test automaton in the industry, and indicates the need for
                                                                    We identified critical success factors from those materials
TAPI for many organizations, especially for those who are far
                                                                    by performing inductive coding [25]. Inductive coding is an
from being mature. Several empirical studies (e.g., [22], [23])
                                                                    thematic analysis technique. It uses a iterative approach to
have been explored the steps and practices of conducting TAPI
                                                                    extract data from sources and then build the common themes
in software organizations. Additionally, there is the number of
                                                                    to classify them. Our inductive coding process was performed
recent studies conducted test automation maturity models for
                                                                    in three steps, as shown in Fig. 1.
providing the guidelines for TAPI, for example, Eldh et al. [5]
develops the TAIM model and Furtado et al. [6] develops
MPTA.BR.
   However, despite many TAPI topics have been examined by
prior work, we failed to identify empirical research conducted
on observing software organizations that are carrying TAPI in
practices.
                  III. R ESEARCH METHOD
   We studied several industrial experience reports conducted
in software engineering field. We conducted our study in three
                                                                       Fig. 1. Data thematic analysis process (modified according to [25])
stages: (1) a study plan, (2) data collection, (3) data analysis.
Each stage is described in the following sub-sections.
                                                                       First, the initial reading was performed to identify rele-
A. A study plan                                                     vant texts (that describe relevant critical success factors) on
  We defined a study plan to set data collection and analysis       available materials. Second, we coded the segment of relevant
process for presenting an experience report. This plan was          texts in NVivo. The memos were written throughout the
agreed by all authors.                                              coding process. Third, by reviewing the codes and memos,
                                                                    we establish themes to describe the critical success factors.
B. Data collection                                                     We reviewed the trustworthiness of our list of success
   The second author was responsible for facilitating the access    factors mapped into categories, when necessary, the original
to the required data from the team of F-Secure for this study.      texts were examined.
The data collection was carried out in two steps.                      Based on the thematic analysis, the first author summarized
   In the first step, a collection of experience notes, team        study results to answer the research question in this paper.
reflection reports, software production snapshot data were          The second author reviewed the study results and proposed
the changes: (1) revise inappropriate contents, (2) complement      maintenance from running created a few particular issues.
more examples and details, (3) add new contents considered          The coverage of test automation was limited, running it and
to be important. The final modification were made in the            analyzing results was manual work, skills for maintenance
discussion among co-authors. The final results was reported         unavailable in feature teams and selected market leader tool
by the first author and the second author by the paired-            evolved out of its market position and was left behind better
simultaneous writing. The third author reviewed that.               tools.
                                                                       The current generation of test automation efforts with Epics
                         IV. R ESULTS                               are founded on a Windows endpoint protection platform,
  To present the study results, we first provide an overview        multi-team effort started in 2009 for consumer products and
of case description. Next, the research question is answered.       built from whole-team responsibility with open source tools.
                                                                    Both the new product architecture and the test automation
A. The company and team description
                                                                    system were created as a pair to support one another. Epics
   F-Secure Oyj is a cyber security company with headquarters       joined in 2016 to develop corporate products with the same
in Finland and over 1600 employees globally. F-Secure’s             platform, followed by a second corporate team with different
products protect enterprises and consumers against a wide           product responsibility in 2018.
variety of security threats. Windows endpoint security products        Fig. 2 shows the current test automation system shared
(incl. features such as antivirus) form a product line sharing      among teams (including Epics) for Windows endpoint prod-
code assets and practices. F-Secure has multiple DevOps teams       ucts. The whole system consists of seven areas: Tools Root,
attending to different customer segment’s needs, creating dif-      Scripts, TestLab infra, WinOS image, Environment virtualiza-
ferent Windows endpoint security products from a common             tion service, Jenkins, Radiator and TA telemetry. CI to build
product line.                                                       test automation system exists and it pulls latest from code
   With 30 years of history in testing Windows endpoint             repositories for test automation to run test automation in CI
security products, the start of serious test automation efforts     environment on product change.
date back to 1999 with a training by Mark Fewster. Efforts
lead to tool selection and implementation in place in 2005,
following best practices of the time. Since then, the TAPI
initiative was started.
   Nowadays, test automation is an integral part of fast-
paced development giving developers feedback at F-Secure
for Windows endpoint security products. TAPI is embedded
in the culture for continuous development. The goal of TAPI
is to enhance the ability to produce and maintain the quality of
products in agile and continuous integration (CI) environment.
TAPI practices may be different from team to team, but each
team shares the TAPI culture at F-Secure.
   The DevOps team observed in this paper is Epics, with
currently 11 engineers. Epics is responsible for developing and
operating Windows endpoint security products that integrate
with cloud-based Protection Service for Businesses manage-
ment system for corporate customers. Epics was created in                              Fig. 2. Test automation system
2016 to build on an existing consumer product and further de-
velop it for corporate customers. Epics product responsibility         At the time of writing this paper, Epics self-reports high
has grown from original 1 product to currently 14 products it       satisfaction and maturity in test automation for continuous
releases versions on with a monthly schedule. Products Epics        development, which is demonstrated by the set of indicators:
operate count their users in millions. Epics shares F-Secure’s        •   The increasing speed to release: Epics has the ability
culture of TAPI and leads efforts in speeding up Windows                  to make continuous release decisions based on test au-
endpoint security product’s release cadence.                              tomation results. While regular release cycle has been 1-
   Looking back to 2005, test automation in the similar team              2 major, 2 minor releases a year for each product team,
operating for Windows endpoint security products looks dif-               Epics had 9 releases of its products in 2019 shown in
ferent. While application development was responsibility of               Table I. Each release contained hundreds of changes on
several feature teams, test automation was responsibility of              product and test automation. Time from release decision
two test automation developers in a separate team providing               to release at first customer machines has improved from
reusable test libraries as a service for those feature teams. Us-         5 days (2018) to 4 hours (2019) and the team makes
ing a commercial Capture and playback tool as programming                 progress towards two week cadence typical for web
platform, the two test automation developers created a library            applications for a Windows application with distributed
of tests feature teams would run. Separating the creation and             deployment.
  • Improving productivity of the team: Epics with 11                                         TABLE II
    people was capable splitting their effort to test automa-                        P ERCEIVED S UCCESS FACTORS
    tion, customer valuable features, maintaining, monitoring,       Dimension         Factor
    and operating for a large, significantly growing, user           Human             Whole team effort
    base. Epics contributed 2917 code changes (including test                          Expert team members
                                                                                       Self-motivated team members
    automation) to Windows endpoint security platform to             Organizing        Allow time for learning curve
    take forward products they are responsible for.                                    Internal open source community mindset
  • Shared platform work efficiency: Quality of the Win-             Technical         Test tool choice and architecture
                                                                                       Testlab infrastructure
    dows endpoint security platform remained high showing                              Product testability
    up in low number of maintenance issues, while it was                               Telemetry
    developed actively in multi-team multi-site independent          Process           Incremental approach
                                                                                       Process observation and optimization
    teams. Test automation showed what part of the system
    in CI is unavailable and when it returns to availability.
  • Sustainable test automation maintenance effort: Test
    automation stayed up to speed with changes while team         from other development work. Maintenance was hindered by
    had bandwidth to other work. Every team member con-           lack of test automation skills in feature teams, which were
    tributed to test automation, sharing the load.                trying to use the created automation.
  • Finding relevant issues: Test automation helped add a            In 2009, when product architecture was completely re-
    set of Server products in a few days finding operating        vamped and new test automation created side by side to it, test
    system specific issues, identified large number of crashes    automation became a developer specialty creating individual
    and pinpointed relevant problems.                             Python developers building test automation systems from
  • The high satisfaction of customers: Epics addressed 167       within the team.
    support issues from customer base counted in millions            In 2016, when Epics started working, their practices and
    and worked on one support escalation for their products.      tooling for test automation came with the Endpoint protection
  • High test efficiency: Run a maximum of 213 708 tests          platform. New hires included a test automation specialist (a
    on single working day to cover the changes of that day.       new Python developer). Allowing growing to learn Python
  • Reasonable investment for TAPI: No visible investment         on the job with continuous progress in TAPI gradually took
    on improving test automation process as it is part of         the team towards supporting continuous testing and frequent
    normal work.                                                  releases.
                                                                     In 2018, the team moved organically to a ‘whole team effort
                            TABLE I                               model’- everyone working toward the same goals to build
                 R ELEASE INFORMATION IN 2019                     software products - while serving growing user base and more
 Release     # of commits on   # of commits on   Availability     frequent releases. The goal was to release more often, which
            product            test automation                    required removing possible bottlenecks in test automation.
 19.1       655                398               23.01.2019       In this model, everyone was encouraged to conduct test
 19.2       689                298               05.03.2019
 19.3       519                349               03.05.2019       automation. Establishing the release practice and seeing each
 19.4       517                255               06.06.2019       member contributes to test automation activities took a year.
 19.5       304                184               27.06.2019          At the time of writing this paper, the team is cross-functional
 19.6       285                195               12.08.2019
 19.7       290                137               05.09.2019       and carry out agile and CI practices. There are two dedicated
 19.8       530                311               28.10.2019       specialists in the area of test automation. All team members
 19.9       304                365               19.11.2019       perform test automation tasks. The team takes care of feature
                                                                  and test automation discovery, development and maintenance,
                                                                  and operate and monitor the production environment. Each
B. RQ1 - Perceived success factors                                member worked with more responsibility to create and en-
   To answer ‘RQ1 - Perceived success factors’, we identified     hance the value of automated tests.
critical factors that determine the success of TAPI in the           2) Expert team members: One important factor determining
DevOps team at F-Secure. Those factors were classified into       success of TAPI is in the mix of people in Epics. From first
several dimensions, see Table II. In next sub-sections, we        senior test automation developer who had never written Python
elaborate the details about what test automation practices are    to senior test strategist, to senior developers experienced with
performed around those factors and what impacts each factor       test automation, to a junior aged 15 when starting with the
has.                                                              team, they provided a mix of perspectives and forced deliberate
   1) Whole team effort: The whole team effort is considered      learning as part of the work. Test automation expertise was
as a critical factor for the success of TAPI in Epics.            not test automation developer specialty, but something every
   In 2005, when the two-person in the separate team are          team member had perspectives to contribute on. Signicant
creating a library of automated tests for the feature teams for   contributions to better test automation came from a continued
Windows endpoint products, the test automation was isolated       series of insights implemented in code, e.g., a team interaction
leading a Python developer implement the telemetry plugin.            Nowadays, the team co-owns a tailored tool set that contains
   3) Self-motivated team members: Self-motivated team             more than 10 different test tools, see Fig 2. Each tool is
members was understood as one major factor. When moving to         used for a purpose in the present test automation system.
‘the whole team effort’ model in Epics, the goal of TAPI was       There is many kinds of code created for test automation,
modeled through some members actions to other members.             for example: Nose Plugins for reusable functionalities like
All members in the team were allowed to take test automation       telemetry sending, Jenkins DSLs for job definitions in test
tasks and learn while doing them. Team members voluntarily         automation, Wrappers for C++ to Python bindings, Libraries
distributed each responsibility among themselves depending         and tools for observing security incidents, and crash analyzer
on their preference and experience level. They became more         for post-processing analysis, scripts for specific actions and
self-motivated to increase their involvement in test automation    verification. Test runs and change orchestration and continuous
by, e.g., actively using existing test tools, fetching useful      integration related tasks are performed with Jenkins.
results for their needs, growing ideas that may add value for         Individual tools are interchangeable and got replaced when
the team, and sharing the expertise with others. It was noted      better options come along. Test tools were selected to serve
that test automation can be performed in a better way, when        current ideas, and changed as new insight emerged. Team
test professionals was not over-burdened with assigned tasks.      members were allowed to identify the needs for suitable
                                                                   test tools. The final test tool selection decisions were made
   4) Allow time for learning curve: Allowing time for learn-
                                                                   through approving a change into the system, discussing at
ing is a factor that determines the success of TAPI at F-
                                                                   least between two people. Each test tool was selected with
Secure as well as Epics. Because of technology changes (e.g.,
                                                                   experimentation mindset, to see if that it is useful and main-
test tools, product architecture, test infrastructure) and the
                                                                   tainable. Benefits were discovered through experimenting with
discovery of new knowledge, people were expected to learn
                                                                   the test automation continuously running to support software
new things. Since Epics started, a learning-by-doing strategy
                                                                   production. Integrating the variety of test tools into the same
has been applied. In the ‘the whole team effort model’, all team
                                                                   system was not a straightforward task but includes discovery.
members were encouraged to improve their test automation
                                                                   Lots of changes to the test automation system were done to
expertise and skills by performing test automation tasks. They
                                                                   combine the strengths of test tools. In the current system,
were allowed to fail with test automation in a safe way.
                                                                   test automation is based on a general purpose programming
Experiences are discussed without scheduled meetings, sharing
                                                                   language Python that supports and integrates with the C++-
a team room and a discussion chat.
                                                                   based products by its design.
   5) Internal open source community mindset: Internal open           7) Test lab infrastructure: “Let us create a tool that would
source community mindset is considered critical for the suc-       really enable fast provisioning of different test environments,”
cess of TAPI to gain test automation maturity for continuous       said by a developer at F-Secure about ten years ago. From
development. Since 2009, F-Secure has worked with internal         the insight of what could be built, with support from peers
open source community model meaning all code is visible            enthusiasm, they implemented a tool that framed the internal
and changeable to anyone internally. Running code served as        managed test lab infrastructure plus the images for the provi-
documentation that different teams contribute on. Before 2009,     sioning of various test environment. Because of the positive
projects worked on isolated branches and bringing changes          results of this first attempt, since that, this tool was put in
together was difficult.                                            use for a long time in product teams that are responsible for
   In 2016, when Epics started, product code (including the        Windows endpoint security products. The provisioning system
test automation part) was shared in the internal open source       was able to start a new working test environment in 5 seconds
community with other development teams, who build prod-            and played a significant role in test automation progress.
ucts from same Windows Endpoint Protection platform. Test             Some years after, the developer who implemented the tool
automation assets were first created separately for Epics,         left F-Secure. Future maintenance and operation was split be-
and in 2018 combined with other teams on the platform              tween R&D and IT departments - maintenance and operations
into a shared repository, even if different folders. Over time,    with R&D, providing infrastructure to run on from IT. With
sharing assets (creating reusable methods in test automation)      new cloud-based cost allocation, provisioning and security
increased while there is still a per team separation visible in    models, wishes to have these with the tooling emerged. In
the folder structure. Shared repository with cross-team review     2018, it was seen that current test lab infrastructure was under-
responsibilities enabled co-creation of shared assets for test     resourced (needing more machines it got), and poorly managed
automation beyond individual team’s capabilities.                  (hard to find a quick fix in case of problems). Operational
   6) Test tool choice and architecture: For Epics, the use        problems with current system were fixed in 2019 and a future
of test tools is necessary and critical for its test automation.   replacement is under consideration.
Without the current test tools, the success of TAPI seems             8) Product testability: The 2005 lessons on test automation
impossible. In 2005, the tool in use was commercial tool           lead to an insight on importance of product making test au-
allowing capture and replay, used as a scripting platform. Since   tomation possible - testability, e.g., products requiring reboot
then, the closed languages in commercial tools were deemed         are harder to automate, so new architecture does not require
limiting.                                                          reboots. Testability was a major architectural change, not
minor coordination from an outside team and test automation        The change steps were carried out through experiments to
testers in the separate team made significant effort living with   allow learning, even though some succeeded and some failed.
the architecture rather than changing it to testable.              The incremental changes affected daily work of the team, both
   In 2009, with a change in business focus and need of solv-      positively and negatively. The positive results became part of
ing product performance issues, the product architecture was       TAPI.
completely revamped. With this change, automation testability         11) Process observation and optimization: The capability
features were designed into the products and team practices,       to continuously explore useful information for optimizing test
in efforts lead by developers to ensure the feedback they need     automation process is critical for Epics. There was a model to
from the test automation. From intertwined functionality, the      specify which aspects (e.g., maintenance costs, test execution
design moved towards isolated functionality in components.         times) should be addressed for optimizing the test automation
Information reliable automation needed was made available          process. However, the actual optimization was done reacting
with C++ to Python wrappers every functionality now comes          to the current ideas. A principle of “appreciate what you have
with.                                                              and make it better” was regularly applied. Especially after
   Complete redesign of product architecture enabled asking        ‘the whole team effort‘ model was introduced, everybody was
for visibility and control for test automation purposes, and       allowed to bring or implement process optimization related
getting it - or doing the necessary change yourself. Under this    ideas in the team.
architecture, services and components are more independent.
Testing a single part independently became less complex, and                               V. D ISCUSSION
the effort to do it was deducted.                                     In this section we carry out the discussion on our research
   9) Telemetry: Telemetry is process of automatically record-     question, explain the TAPI culture in F-Secure, and outline the
ing and transmitting the collection of data for monitoring [26].   threats to validity.
Product telemetry use in scale for Epics started in 2017,
                                                                   A. RQ1 - Perceived success factors
and expanded from product telemetry in test environments to
test automation telemetry in 2019. Test automation telemetry          In this study, we present a set of key success factors of
solved two perceived problems: radiator snapshots were im-         TAPI in one DevOps team of F-Secure. We compared our
mediately outdated due to numbers of builds to test, and each      results with the results of other studies in this research scope
failure required reading logs to know who the feedback was         and found the similarities and differences.
targeted for while being hard to collate to find trends.              Many success factors (identified in this study) have been
   In November 2019, a Python developer in Epics imple-            examined in existing literature. For example, test tool choice
mented telemetry plugin into the test automation system for        and integration, expert team members, and self-motivated team
monitoring automated tests. Every automated tests automati-        members were mentioned by Mark Fewster and Dorothy
cally reported itself as it runs with telemetry. For example,      Graham in the book ‘Software test automation-effective use
it can be seen that how many automated tests are failed,           of test execution tools’, which was published in 1999 [27]. In
passed, and skipped, how long they take. This made all             other case studies (e.g., [3], [28], [29]) which were published
of such relevant information on automated tests in scale of        several years ago, product testability related factors were
200 000 tests a day visible and collated in real time. It is       recognized on test automation maturity studies in particular
more straightforward than before to track and control of test      software organizations. Our results complement the research
automation process for continuous improvement.                     of existing studies by showing that those factors are still valid
   10) Incremental approach: An emphasis was put on the            for TAPI practices in the current industry. Nevertheless, we
incremental approach to improve test automation and its            explore and explain new success factors, e.g., the whole team
process for those 15 years in F-Secure for Windows endpoint        effort, incremental approach, and agile-oriented process related
security platform and products. From the old teams to Epics,       factors, which were rarely observed in other studies. We claim
an incremental approach was used with the point of continuous      those factors should receive enough attention in future TAPI
learning. Since the initial phase of TAPI, there was no doc-       research.
umented test automation strategy specifying what should be            On the other hand, our study results are in conflict with
improved for determining the mature test automation process.       some observations of TAPI of the prior research:
Indeed, the strategy was discovered step by step in practices.        • Defining an explicit test automation strategy at start
Epics continuously explored their needs and possibilities for           can guide organizations to do TAPI in general. Test au-
test automation. The direction of TAPI was discussed in the             tomation strategy related topics are discussed in many test
groups of internal stakeholders - usually in informal settings,         maturity models like TMap [30] and TestSPICE 3.0 [31].
peer to peer. Accordingly, the actionable steps were took to            Also, prior studies (e.g., [8], [32]) surveying practitioners
make the meaningful changes.                                            about the TAPI in practices confirmed that developing a
   Rather than totally changing the whole test automation pro-          test automation strategy with right concerns may con-
cess, the changes were always added incrementally piece by              tribute to the success of TAPI in Agile development
piece into the existing test automation process. Some changes           environment. However, based on the observation, having
occurred naturally as problems arise and needed to be fixed.            a test automation strategy at the initial phase seems is
     not that critical for the success of TAPI in the DevOps         C. Threats to validity
     team at F-Secure. As described in Section IV-B10, there            In this section, the threats to the validity of the study in
     was no documented test automation strategy. With the            this paper and approaches taken to minimize their impacts
     incremental approach, there was the broad understanding         are explored, according to a standard checklist in software
     about what they have now and what they want to add on           engineering from Wohlin [34].
     the basis of existing test automation process. The goals           Construct validity refers to the extent to which the study
     and action plans were allowed to be discovered at any           can represent the theory behind it [34]. We reviewed prior
     time.                                                           literature about the concept of TAPI and related work before
  • Selecting test tools to fit the current needs and future         conducting the case. The study protocol was defined before-
     development. Lots of SE researchers and practitioners           hand. We carried out several meetings to further verify the
     have highlighted that selecting right test tools to fit the     content of experience reports and complement the details. At
     current needs and future development is critical to test        the end, our observations and study results were reviewed and
     automation success [33]. However, in the observed team          verified with the representatives (who involved in TAPI in
     in this study, test tools are treated as interchangeable Lego   Epics) to avoid false interpretations and ensure the reliability.
     bricks. They could be selected to serve the instant ideas,         External validity is concerned with how the study results
     and changed as new insight emerged.                             can be generalized [34]. The study setting of this paper
  • Measuring the quality of performance of test automa-             may threaten the external validity. Our findings are strongly
     tion is important. Based on the study [11], the quality         bounded by the context of this team at F-Secure, and they may
     of performance of test automation must be measured              not be representative for TAPI of all software organizations. To
     to reflect how the goals of TAPI are achieved. In our           address this threat, we attempted to describe the company and
     case, the measurements are shown, i.e., in the dashboard        the team in as much detail as possible, but since the time span
     or telemetry. Rather than the quantitative measures, the        of their TAPI is large it is hard to acquire detailed information
     qualitative investigation and discussions were conducted        about the context of F-Secure conducting TAPI in very early
     to regular examine the changes in their TAPI.                   years. This makes it more challenge to relate the case in this
  • The TAPI must follow the guidelines, as described in             paper to other similar TAPI cases in the industry. Individual
     prior literature [6]. With the incremental approach, the        differences are suggested to be considered when generalizing
     observed team in this study has tailored its own test           the study results.
     automation process depending on its requirements.                  Conclusion validity refers to whether the correct con-
  The above differences may point out the gap between the            clusions are made through observations of the study [34].
academia and industry, though more research is needed to             In our study, the conclusions were made according to the
confirm this.                                                        thematic analysis on raw data. We performed the data analysis
                                                                     with NVivo in where all qualitative codes were stored. The
B. Test automation process improvement culture in F-Secure
                                                                     conclusions were verified among co-authors.
   Experience report on TAPI culture with Epics reports on a            Internal validity focus on how the study causes the out-
company following a relaxed, verbally communicated strategy          comes [34]. In our study, threats to internal validity may
without strict rules and processes relying on developers vol-        lie in the data collection. Our data were mainly collected
untary participation. We consider this an unusual success with       from a collection of experience notes, team reflection re-
TAPI resulting in high maturity of test automation as well as        ports, and telemetry result reports. Materials were provided
continuously improving it.                                           by one person (the second author of this paper) in Epics
   TAPI culture with Epics relied on the idea that a running         at F-Secure. They were filtered through models available
test automation system documents itself and people working in        in literature practitioners suggest may provide an outdated
teams and across teams in networked manner co-create contin-         perspective to maturity. Viewpoints on the material as well
uous strategy of experimenting and improving. Appreciating           as selecting aspects to highlight from the material might have
what the team had, and continuously adding to it to make it          some subjective viewpoints. We tried to overcome this type
better resulted in shifting the team to a place where they are       of threat by acquiring more quantitative data to explain the
happy with their automation.                                         results. However, because of the personnel and technology
   Test Automation had been team-driven to serve teams and           changes in passed years, collecting and comparing quantitative
developers as opposed to manager reporting or return on              data beyond what was accessible at first was outside scope of
investment calculations. Architectural layering of test automa-      this work.
tion architecture blocks, ”interchangeable Lego bricks” each
provide a service small enough to replace with better ideas and                            VI. C ONCLUSION
implementations. Customer value and TAPI value had been                 This paper presents an experience report on TAPI in one
prioritized as equal candidates from same team effort budget.        DevOps team at F-Secure. For the study purpose, we reviewed
   Finally, internal open source applied at F-Secure includes a      a collection of experience notes, team reflection reports, and
developer-friendly sense of ownership and lack of bureaucracy        telemetry result reports. Several meetings were held to discuss
to make changes towards one company’s needs and goals.               the details. As the study results, first, we reported that,
the team defined its test automation maturity for continuous                    [10] ISTQB, “Worldwide software testing practices survey 2017-18,” Tech.
development by a set of indicators, see Section IV-A. Second,                        Rep., 2018.
                                                                                [11] Y. Wang, M. Mäntylä, S. Eldh, J. Markkula, K. Wiklund, T. Kairi,
it is noted that, to successfully conduct TAPI, the team has                         P. Raulamo-Jurvanen, and A. Haukinen, “A self-assessment instrument
performed main practices around a set of factors mapped into                         for assessing test automation maturity,” in Proceedings of the Evaluation
different dimensions, see Table II. Third, under the further                         and Assessment on Software Engineering. ACM, 2019, pp. 145–154.
                                                                                [12] Y. Wang, “Test automation maturity assessment,” in 2018 IEEE 11th In-
investigation, we found that the team has the tailored test                          ternational Conference on Software Testing, Verification and Validation
automation process for continuous development, which may                             (ICST). IEEE, 2018, pp. 424–425.
have the similarities or differences with the ones defined in                   [13] V. Garousi, M. Felderer, and T. Hacaloğlu, “Software test maturity as-
                                                                                     sessment and test process improvement: A multivocal literature review,”
prior literature.                                                                    Information and Software Technology, vol. 85, pp. 16–42, 2017.
   This study has three main contributions. First, from the                     [14] K. Hrabovská, B. Rossi, and T. Pitner, “Software testing process models
industry perspective, it introduces the industrial case of suc-                      benefits & drawbacks: a systematic literature review,” arXiv preprint
                                                                                     arXiv:1901.01450, 2019.
cessfully carrying out TAPI in a DevOps team. Second, from                      [15] P. Pocatilu, “Automated software testing process,” Economy Informatics,
the academia perspective, this study connects to the prior                           vol. 1, pp. 97–99, 2002.
studies and makes novel contribution. For example, the success                  [16] V. Garousi and F. Elberzhager, “Test automation: not just for test
                                                                                     execution,” IEEE Software, vol. 34, no. 2, pp. 90–96, 2017.
factors of TAPI frequently mentioned in prior studies are                       [17] V. Garousi and M. V. Mäntylä, “When and what to automate in software
explained with empirical evidence. Also, we identified new                           testing? a multi-vocal literature review,” Information and Software
factors such as the whole team effort, incremental approach,                         Technology, vol. 76, pp. 92–117, 2016.
                                                                                [18] T. Kairi. (2019) Why and how to self-assess test automation
and telemetry. Third, as an empirical research, this study                           maturity. [Online]. Available: https://www.eficode.com/blog/self-assess-
narrows the gap between academia and industry.                                       test-automation-maturity
   In the future, we plan to assess the level of test automation                [19] W. automation testing. (2019) 5 major steps to test automation
                                                                                     assessment. [Online]. Available: https://www.testbytes.net/blog/test-
maturity in the same DevOps team at F-Secure. Based on the                           automation-assessment/
assessment results, we could investigate the specific impact of                 [20] P. Merrill. (2019) 13 questions that determine test automation success.
critical success factors on the maturity level and the short-term                    [Online]. Available: 13 questions that determine test automation success
                                                                                [21] K. Karhu, T. Repo, O. Taipale, and K. Smolander, “Empirical observa-
and long-term benefits and effects of test automation. Addi-                         tions on software testing automation,” in 2009 International Conference
tionally, the set of key success factors presented in this paper                     on Software Testing Verification and Validation. IEEE, 2009, pp. 201–
may be only a part of possible solutions to some software                            209.
                                                                                [22] B. Pettichord, “Seven steps to test automation success,” Star West,
organizations. We also could widen the research by carrying                          November, 1999.
out a case study surveying more software organizations.                         [23] D. Graham and M. Fewster, Experiences of test automation: case studies
                                                                                     of software test automation. Addison-Wesley Professional, 2012.
                         ACKNOWLEDGMENT                                         [24] Q. P. Ltd. (2019). [Online]. Available: https://www.qsrinternational.com/
                                                                                [25] D. S. Cruzes and T. Dyba, “Recommended steps for thematic synthesis
  The first and third author of this study are supported by                          in software engineering,” in 2011 International Symposium on Empirical
TESTOMAT Project (ITEA3 ID number 16032), funded by                                  Software Engineering and Measurement. IEEE, 2011, pp. 275–284.
                                                                                [26] M. Kechagia, D. Mitropoulos, and D. Spinellis, “Charting the api mine-
Business Finland under Grant Decision ID 3192/31/2017.                               field using software telemetry data,” Empirical Software Engineering,
                                                                                     vol. 20, no. 6, pp. 1785–1830, 2015.
                             R EFERENCES                                        [27] M. Fewster and D. Graham, Software test automation. Addison-Wesley
 [1] J. Kroll, I. Richardson, R. Prikladnicki, and J. L. Audy, “Empirical            Reading, 1999.
     evidence in follow the sun software development: A systematic mapping      [28] C. Persson and N. Yilmazturk, “Establishment of automated regression
     study,” Information and Software Technology, vol. 93, pp. 30–44, 2018.          testing at abb: industrial experience report on’avoiding the pitfalls’,” in
 [2] D. M. Rafi, K. R. K. Moses, K. Petersen, and M. V. Mäntylä, “Benefits         Proceedings of the 19th IEEE international conference on Automated
     and limitations of automated software testing: Systematic literature            software engineering. IEEE Computer Society, 2004, pp. 112–121.
     review and practitioner survey,” in Proceedings of the 7th International   [29] M. Grindal, J. Offutt, and J. Mellin, “On the testing maturity of software
     Workshop on Automation of Software Test. IEEE Press, 2012, pp. 36–              producing organizations,” in Testing: Academic & Industrial Conference-
     42.                                                                             Practice And Research Techniques (TAIC PART’06). IEEE, 2006, pp.
 [3] K. Wiklund, S. Eldh, D. Sundmark, and K. Lundqvist, “Technical debt             171–180.
     in test automation,” in 2012 IEEE Fifth International Conference on        [30] T. Koomen, B. Broekman, L. van der Aalst, and M. Vroon, TMap next:
     Software Testing, Verification and Validation. IEEE, 2012, pp. 887–             for result-driven testing. Uitgeverij kleine Uil, 2013.
     892.                                                                       [31] S. TestSPICE. (2014, OCT 10,) Testspice 3.0. [Online]. Available:
 [4] PractiTest, “State of testing survey 2019,” Tech. Rep., 2019.                   http://www.intacs.info/index.php/testspice
 [5] S. Eldh, K. Andersson, A. Ermedahl, and K. Wiklund, “Towards a test        [32] E. Collins, A. Dias-Neto, and V. F. de Lucena Jr, “Strategies for
     automation improvement model (taim),” in 2014 IEEE Seventh Inter-               agile software testing automation: An industrial experience,” in 2012
     national Conference on Software Testing, Verification and Validation            IEEE 36th Annual Computer Software and Applications Conference
     Workshops. IEEE, 2014, pp. 337–342.                                             Workshops. IEEE, 2012, pp. 440–445.
 [6] A. Furtado, S. Meira, and M. Gomes, “Towards a maturity model in           [33] P. Raulamo-Jurvanen, M. Mäntylä, and V. Garousi, “Choosing the right
     software testing automation,” in The Ninth International Conference on          test automation tool: a grey literature review of practitioner sources,”
     Software Engineering Advances, 2014, pp. 282–285.                               in Proceedings of the 21st International Conference on Evaluation and
 [7] Hohnanna. (2018) Continuous development: How iterative                          Assessment in Software Engineering. ACM, 2017, pp. 21–30.
     processes     can    improve     your    code.    [Online].   Available:   [34] C. Wohlin, P. Runeson, M. Höst, M. C. Ohlsson, B. Regnell, and
     https://deploybot.com/blog/continuous-development                               A. Wesslén, Experimentation in software engineering. Springer Science
 [8] J. Kasurinen, O. Taipale, and K. Smolander, “Software test automation           & Business Media, 2012.
     in practice: empirical observations,” Advances in Software Engineering,
     vol. 2010, 2010.
 [9] Capgemini, Sogeti, and Microfocus, “World quality report 2018-19,”
     Tech. Rep., 2018.
