---
title: "Turn up the Good. A Tester Meets Mob Programming"
publication: "Testing Trapeze"
date: 2015-08
url: https://drive.google.com/open?id=0B07e3JZGe_haY1VEdVdQQTdBUWM
source_retrieved: https://drive.google.com/open?id=0B07e3JZGe_haY1VEdVdQQTdBUWM
kind: magazine article
language: en
---

# Turn up the Good. A Tester Meets Mob Programming

*Testing Trapeze — 2015-08*

Source: <https://drive.google.com/open?id=0B07e3JZGe_haY1VEdVdQQTdBUWM>

> Retrieval note: text extracted from the author's PDF of the article (the Google Drive copy needs sign-in); layout is approximate.

---

TURN UP THE GOOD:
       A TESTER MEETS MOB
            PROGRAMMING
        MAARET PYHÄJÄRVI
                                HELSINKI, FINLAND

    LET ME SHARE A JOURNEY OF DISCOVERY                      appreciate mob programming - a group of
    taken on mob programming. I’m a skilled                  people developing software together, on one
    exploratory tester who prefers not to code. When         computer.
    agile started to happen to me, I resisted at first. It
                                                             What is Mob Programming?
    turned out to be the best thing that has
                                                             Mob programming is a whole team approach to
    happened to me in testing. When I learned about
                                                             software development, where coding, designing,
    mob programming, I resisted. Working on my
                                                             testing and working with the customer is all done
    resistance has been a journey into my deep-
                                                             as a team. Woody Zuill, originator of the
    rooted fears. I’ve needed to learn something that
                                                             approach, defines mob programming as “all the
    could again be the next great thing to take us
                                                             brilliant people working at the same time, in the
    forward in software development.
                                                             same space, at the same computer, on the same
    In this article, I take you through a story of how I     thing”. Rather than getting the most from
    rationalize my fears into arguments against a            everybody, we want to get the best of everybody
    method, and how trying things out taught me to           into everything we do.

"   TESTING TRAPEZE | AUGUST 2015                                                                          35
                              Imagine a team working so that they all use only one computer to type
                              the code. They all work on the same thing, together. And they all rotate
                              taking turns on the keyboard typing the code. All day, every day.

    “
                              I learned about mob programming for a conference I organized in
    Treat each other with     Finland, where I invited Woody Zuill to share lessons learned. “Treat
    kindness, consideration   each other with kindness, consideration and respect”, he emphasized.
    and respect               He talked about the positive sides: avoiding wait times when expertise

    ”
                              was right at hand, short feedback cycles, delivering a feature through
                              the pipeline as a steady one-piece flow of value, not collecting half-
                              done work, learning as individuals and as a team, and having many
                              problems vanish.

                              Crazy talk, right?
                              I respectfully dismissed a big part of what Woody Zuill was saying as
                              “will not work here”. My developers and I would not enjoy it, we already
                              had problems working together and more would not be better. It would
                              mess up allocations of time in a way where we’d get less done.

                              A time-lapse video of the mob working day, all working intensively and
                              laughing around a computer made mob programming seem unreal.
                              These people must be special in some way. They did not have testers,
                              they were all “just” programmers. It would be a long way to travel with
                              perspectives as different as developing and testing. With basic
                              knowledge, I saw no examples of bringing the two together, as mobs
                              out there did not have testers like me.

                              In hindsight, I see a big change in my attitude towards mob
                              programming after I started experiencing it. I would rationalize my
                              experience-driven fears into four main arguments of mob programming
                              not working for us:

                                •   Less done with single-piece flow: There must be tasks that
                                    waste effort when the whole team does the work a single person
                                    could do.
                                •   No time for exploring the product: Developers would drive all
                                    effort to code and not be interested in using the application in its
                                    real environment enough.
                                •   Code is boring (to me): Everyone would spend their days on
                                    code, programming. I would have to spend more time on code. I
                                    want to spend time on the system, not code.

"   TESTING TRAPEZE | AUGUST 2015                                                                    36
      •   Failing is public: My rusty programming skills would be
          refreshed in front of people who have issues with women coders.
          Yet another barrier I would prefer not to cross.

    We all have these colleagues we get along with, but would prefer not to
    work too closely with. My worst were people who would tell me “women
    write only comments to code” or who would express that I wasn’t
    welcome for my skills, attributing it to my gender. I was feeling very
    welcome as a tester without mob programming, and I was risking
    losing that respect.

    The things that I do are very valuable in our team as we turn ideas into
    code. I use the product to learn about it and about its use. I’m learning
    how it works, how it should work and what drives value for the end
    users in their use of the product. I regularly help to find the core of what
    we should do next; what would be the smallest possible valuable thing
    from an end user perspective. I look at what we’ve done in context of
    everything else, and help to fit it all together under various scenarios. I
    care for end user experience and business risks, addressing aspects
    of performance and legal considerations just as much as the details of
    what limitations our implementation currently has. The application talks
    to me. It tells me things code never has told me. The application as
    part of a system is a different, more value oriented perspective for
    looking at what our code does. Spending days with code was a threat
    to me spending time with the application.

    I thought being a “driver” in a mob meant being responsible for getting
    the right code written. Taking that responsibility, all by myself, even if for
    a short amount of time, was intimidating. The driver-navigator model
    traditionally describes the driver as the one who has control over where
    we go, and the navigator as the one who oversees the big picture,
    reviewing what gets written.

    I had never heard of strong-style pairing that mob programming uses, a
    specific style of pairing where “for an idea to go from your head into the
    computer, it must go through someone else’s hands” (Llewellyn Falco).
    It turns the expectations of driver and navigator upside down, making
                                                                                                         “
                                                                                       for an idea to go from
                                                                                           your head into the
                                                                                         computer, it must go
    driving the work where you take instructions from the navigator, while           through someone else’s
                                                                                                       hands
    the navigator is responsible for coming up with instructions. And in a
    mob, everyone but the driver holds the navigator role.

                                                                                                         ”
"   TESTING TRAPEZE | AUGUST 2015                                                                         37
                            Leaning in on Mob Programming
                            While I’m a tester on my team, I push my team and myself beyond what
                            I personally want to do, for the best of our company. Mob programming
                            would not be a default choice for anyone in my team without seeing a
                            bigger picture over individual preferences and fears. I needed to
                            investigate more on my negative thoughts on mob programming, give it
                            a chance, and see how it works.

                            Listening later to a Mob Programming talk by Woody Zuill from Oredev
                            2014, I recognized a trigger that started my leaning in to mob
                            programming. “If you’re ever in San Diego, contact me and come mob
                            with us”, Woody said. I joined them for a day in early 2015.

                            Instead of seeing Mob Programming in action, it turned out I
                            experienced it in action. The mob added me to the rotation as if it was
                            the most natural thing to do, even with someone who might not code
                            and had no knowledge of what they were developing. I learned through
                            experience that sitting in front of the keyboard was actually the least
                            scary part, as everyone else would be helping me through. They would
                            explain what I should write, and as they noticed I got the hang of
                            something, they would change the level of abstraction to fit my current
                            level of knowledge. I saw them stumbling and making mistakes. And
                            none of them displayed any of the attitudes towards women or newbies
                            that I was expecting. In particular, I remember Jason Kerney, a member
                            of the Hunter mob, telling me later that years of mobbing had made him
                            kinder.

    “
    The day was a mind-
    changing experience.
    With that experience,
                            The day was a mind-changing experience. With that experience, what
                            was impossible before, was now possible. But I was still left with some
                            of my concerns, in particular the ones related to what I enjoy (not code)
    what was impossible     and how exploratory testing would work in a mob. I had spent a day on
    before, was now         a product I had never seen before, learned more about it in a day than
    possible                what I could usually expect to learn in a week and to what was done

    ”                       during that day.

                            Facing My Team and My Fears
                            I decided to give mob programming a chance. I invited Llewellyn
                            Falco, a technical agile coach, to run a session of group refactoring
                            with my team. He never told my team we would be doing mob
                            programming, we would just be working together.

"   TESTING TRAPEZE | AUGUST 2015                                                                 38
    During the session, I learned about fears my developers had towards
    checking in code. I saw how great the dynamics were when we needed
    to decide what we’d call a particular method. And I survived my
    biggest fear, taking my turn on the computer in front of some people
    with interesting attitudes towards women who code.

    The final touch was when the developer who objected most towards
    pairing and collaboration, volunteered more pairing and grouped work
    in his retrospective observations. My team has started on a path of
    change towards more collaboration.

    I have continued gathering experiences in mob programming. I taught
    exploratory testing in mob format. I participated in several learning to
    code sessions in mob format. I learned that since exploratory testing is
    a performance (as opposed to artifact creation that unit testing
    represents) the audience matters, and for the better. Being different is
    actually an asset in a mob when the mob remembers to treat others
    with kindness and respect.

                                                                                                    “
    Mob programming found its way to my work and office because of our
    struggles on unit testing. These sessions added to my ideas of how a         people build on top of
    tester can be part of the mob. I saw how people build on top of each            each other, needing
    other, needing triggers for memory to come to the best ideas they have.      triggers for memory to
    I could see how my product knowledge and ideas of where things               come to the best ideas
    could go wrong turned into useful activities right away. When we were                      they have

                                                                                                    ”
    frustrated with a blocking excel file when running tests, as a mob we
    turned that experience into changed code that was unblocking.
    Frustration we experienced as a group was more pressing than the
    issue would have been to any of us individually.

    More Mob Programming Ahead
    I still have my concerns on mobbing, but with the experiences I’ve had,
    we’ve come to a point where my team will work in mob programming
    style.

    In particular, there are challenges related to individual’s skills that we
    have trouble finding constructive approaches for, other than mob
    programming. I remember hearing that pair programming is what
    developers do when they like each other, otherwise the same activity is
    called code review. Mob programming softens the blow, exposing
    everyone equally. Like Woody Zuill says, “We’re stuck with what we got,

"   TESTING TRAPEZE | AUGUST 2015                                                                    39
                                 so we need to find ways of getting those individuals to work well with
                                 the other individuals”.

                                 I deeply care for how much value we provide as a team for our
                                 company. I’ve already seen good examples of avoiding rework by
                                 getting the best (as opposed to most) out of the individuals. And I know
                                 that at this point of my career and experience, I’m strong enough to

    “
    Providing value and
    gaining value
    (learning) in a mob are
                                 lead my team into mob exploratory testing whenever that is needed. My
                                 skills and interests as an exploratory tester will continue to develop, not
                                 atrophy.

    equally important. Mob       I look forward to learning more about how my testing changes with
    programming is about         being in a mob. The change is for the better, even if it heavily stretches
    learning to work well        me out of my personal comfort zone. Providing value and gaining value
    together                     (learning) in a mob are equally important. Mob programming is about

    ”                            learning to work well together.

    Maaret Pyhäjärvi is a tester extraordinaire from Finland specializing in breaking illusions about
    software through means of exploratory testing. She is a software specialist with soft spots for hands-
    on testing, helping teams grow and building successful products and businesses. She tweets as
    @maaretp and blogs regularly.

"   TESTING TRAPEZE | AUGUST 2015                                                                        40
