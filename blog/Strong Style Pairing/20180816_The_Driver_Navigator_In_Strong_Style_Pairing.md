# The Driver-Navigator in Strong-Style Pairing

There’s no better way of learning programming or testing than working together with people, building on one another’s insights. Well, it does not always feel like the best way if the power dynamics are off and the skills and understanding of how to work well in a pair are not in place. Let’s talk about the two roles a bit.

In a pair, we have a *driver* and a *navigator*. Think of these roles as they are in driving rally. The driver is hands on the wheel, and in control of paying attention to the immediate task at hand. They are busy looking at the road ahead, optimizing the drive and not checking the map. Checking the map would be a distraction. That is where the navigator jumps in. Keeping track of goals on a larger scale, paying attention to other level of details they can help significantly in getting to better results. Navigator takes care of directions and instructions, and feeding them to the driver as needed.

This same distribution of tasks is what is the core of strong-style pairing. Instead of making the navigator decipher what is going on in the drivers head, the control is placed with the navigator. For strong-style pairing, we say:

> “I have an idea, you take the keyboard”.

For traditional pairing, we’d say: “I have an idea, give me the keyboard”.

## Getting Set Up For Pairing

For the pair to work well, both parties in the pair need to work well in their roles, and there’s specific skills and techniques you can learn to work better from get-go with a new pair in either one of the roles. Techniques, however, are just ideas until you apply them in practice. Only through doing you can learn to pick up the small hints on what would be right thing to do, as you both are equally responsible for your mutual success.

We may think of the driver as an intelligent input device. Intelligence means that while the driver takes orders on what to do and where to go, the driver can also guide to get on the right abstraction level or improvise within the box the navigator gives them.
The navigator is responsible for mining the to-do list and passing the next things to do with instructions on the highest possible abstraction level the driver can consume.

This all builds on trust. The navigator may be just one step ahead of you, and thus unable to give you a clear overview of what you’re about to do. The direction the navigator is going to is where the driver goes. When the driver has an idea, the roles can be switched keeping a basic rule in mind: *for an idea to get on the computer, it must go through someone else’s hands*.

## Who Should Drive and Who Should Navigate?

You have a pair of people. You are different people, with different ideas and experiences. The two of you are stronger together because you build on each other, and also because each of you have unique qualities. Sometimes the qualities are more of a foundational or long-lasting kind, like experience that does not build up over night or transfer in a few days of pairing. Sometimes the qualities are more of temporary, like one having a rough day just today.

One of you will take the role of the Driver — the intelligent input device. One of you will be the Navigator, working out the direction you’re about to head to together. Which of the two of you should be which?

The first rule on being the navigator would be that whoever has the idea toget on the computer, should navigate. Remember: for an idea to get on the computer, it must go through someone else’s hands in strong-style pairing. This brings quickly the idea that perhaps the more experienced one should navigate. At least first. At least until it’s time to switch. You learn very different things in being a driver and being a navigator.
The dynamic of newcomer and a seasoned professional is interesting. Having the newcomer just drive is already a relevant service for the navigator, freeing you from typing to think on a bit higher level. The information for the newcomer sticks in a completely different way from doing it, hands on the keyboard, than watching what someone else is doing.

Whoever had the idea of what to do will navigate. When I started pairing on exploratory testing with a developer, I was the Navigator. When I started pairing on unit tests with a developer, I was the Driver. Over time with both tasks, I will take both roles. And I will grow towards navigating so that the first idea that I have that I could navigate us through, I volunteer to do.

There’s three trigger options on change of roles:

* On time: you can just change roles on a regular interval. Start with shorter times and grow the time as you grow to work as a pair.

* On task: you can change roles when some task is completed. Like a typical ping-pong style pairing, you change so that one creates a unit test and other implements, and both get to do both types of tasks.

* On idea: you just change when the driver feels there’s a direction he’d like to navigate to. It’s like saying “hey, I have an idea, you take the keyboard now”.

Regardless of the role you’re in, the pair of you should remember to take breaks. Pairing can be very intensive work and outside getting the work done in a pair, you’re also responsible for building forward your pairing experience. And that usually works best by inviting for feedback, like taking a small walk around and retrospecting your most recent pairing experience together.

## Driver: Things to Do

You are the intelligent input device. What is expected of you except for typing as you’re told?

* **Push back**. Express that you need to modify the way the navigator is navigating you. You may want to change the box in which you work, make it bigger to give you more freedom or make it smaller to be clearer on what to do. You may realise you need to try something else, and express that in questions. Key is to be active even when driving.

* **Improvise**. The navigator gives you a box within which you operate. You have choices on how you can do things. You choose what you believe to be best for context at hand, and driver gives you more detail if they disagree with your choices. Improvising is about adding your intelligence to the collaboration.

* **Switch level of abstraction**. If you feel the abstraction level of navigating could be higher or lower, talk back to the navigator. If the navigator is using too low level, you can give them the higher level. “You can just tell me to run it”, when navigator is telling you shortcut in keystrokes. If the navigator is using too high level, you can ask “Tell me what to type?” or “Where’s that located?”. Change the level of abstraction and enable a common experience of learning to work together better.

* **Ask questions**. If you feel something isn’t right, ask about it. You can simply go for “Are you sure?” to stop the navigator to think about what is going on. Keep your questions specific so that the answers can be short. You can try validating questions to clarify what is going on right now, “It seems we’re using zip-add-object to regulate temperatures, is that correct?”. You can check if the thing you did was correct against your understanding: “I thought the database only accepted one connection at a time. Why did we do two?”. You can suggest where to go, without deciding for the navigator: “Shouldn’t we do this first?”. Avoid general why-questions and work to prevent long explanations.

* **Initiate role switch on an idea**. When you realise what should be done and think you could navigate this task better, initiate a role switch. You can switch roles on idea, without waiting for the timer. Or you could never use a timer and switch on tasks.

It’s good to remember that you as the driver are helping the navigator to navigate. Sometimes navigators will try a general avoidance technique of declaring tasks mundane, and great driver will volunteer to be around even for that task. Sometimes you are just literally trying to go against the excuse. Sometimes the two of you just need to get through the bad stuff together to get to the fun stuff together, to build the long-term relationship.

Underneath what we actually do as driver, there’s a bunch of attitudes to consider:

* **Trust your navigator**. Stay in the moment. Be ready to work with partial knowledge. Your navigator is probably only one step ahead of you.

* **Just try it**. You can always do it both ways and end up with a third that builds on top of both. Learn by doing. Learning while doing is just as important as getting the end result out of the process.

* **Constant self-reflection**. Investigate what is going through you. Focus on learning. When following your navigator, you’re reverse-engineering. Navigator keeps telling you stuff. You get a very thin, narrow view into the system. You can start putting things together a lot and this gives you a chance to reflect on what you’re learning individually as driver with your pair.

* **Patience**. Give the relationship time. It’s good on both sides, but it’s extra useful on the driver side who works with incomplete knowledge.

There’s two main pitfalls to being a driver.

* **Thinking**. You think within the box or change the box. Thinking too far as the driver takes the navigator’s focus on bringing you back to the task at hand.

* **Silence**. It’s not an open box to do anything you think of. If you want to take the lead, switch roles, but try not to run your own way with the silence.

## Navigator: Things to Do

As navigator, you are in responsible for caring for your driver. If the driver is the intelligent input device, for them to operate properly, you need to care for the conditions of work. Being the navigator, you need to pay attention to your driver, to constantly know where they are going. And you need to enable them to go as fast as possible.

As a navigator, you have three main tasks you’re paying attention to:

* **Feed driver the next thing to do**. You’re creating the driver the box they work in on as high abstraction level as your driver can handle.

* **Mine the to-do-list**. Create an idea on where to go next. You might be just one step ahead, but being that one step ahead is important. Where to go to get your thing done?

* **Observe your driver**. See where they are and where they are going, and correct if the direction does not match what you had in mind. Pay attention on how they are doing, and help them whenever they need it.

Three main tasks might sound simple, but there’s a bundle of advice to do them slightly better.

### Programming style matters

The style of programming matters. Pair programming would seem to work a lot more fluently if the *programming style is consume-first*. With this the idea is that you start with an end result at first and then one by one build the things you wish you had in order to have the end result. Consume-first enables the navigator to go immediately, coming up with things to do while figuring things out themselves. And the end result and it’s division keep a visible checklist of what there is to do to get to the end result.

Some navigators prefer to work with bottom-up programming style. They build the image of the end result in their head, and feed the smallest possible pieces to the driver, one at a time. In this style, the navigator has a lot more of the information about what we’re trying to achieve, leaving the driver to interpret more of why the navigator is having them do things.

The third style is hardest, when there’s no ability to work in small pieces. If the navigator has to figure out the whole thing before feeding driver work, most of the time the driver is paused or participating in design discussions over taking the implementation forward. As a navigator, you’re supposed to care for your driver, not just having them type for you. Keeping driver waiting while navigator figures things out by themselves isn’t exactly the optimal way of caring. Working with partial information is essential.

### The abstraction level dilemma

As the navigator feeding the driver the next thing to do, finding the right abstraction level to communicate with them is relevant, even key to making progress. For driver to go forward, you need to find the right level on which to talk. If you are using an abstraction level too high, you will see nothing happening at the keyboard. If you are using an abstraction level too low, you’re not harnessing the powers of your driver by keeping them on too short a leash.

The core of going as fast as possible is navigating on the highest level of abstraction. Talking in keystrokes when talking in concepts would suffice can feel insulting. So pay attention to raising the level of abstration.

* **Intent**. What is the thing we want to accomplish now?

* **Location**. Where does doing that start? Is the cursor in the right place or moving to the right place so that what we want done could be done?

* **Details**. What exactly to do or type so that the intent is fulfilled, allowing for the drivers contribution while avoiding mistakes?
You notice if the level of abstraction is too high with the puzzled look on their face and the lack of action you expect to see. Drill in if needed.

I was particularly puzzled with the idea of using highest abstraction level possible, until I realised finding the level is really a listening and observation exercise. If you give instructions and following them is hard, you’re probably working on a too high abstraction level. Drilling down can be instant, just be more specific. If you’re not noticing the need to change level, you’re perhaps risking an experience of failing with tasks that lowers motivation in pairing, so it’s good to keep your eyes and ears open. If you start from a very low abstraction level, the driver can always correct you by telling you the level they are comfortable with. But if they have not yet learned how to, they might get a feeling of being talked down. And I found I am particularly sensitive to that, being the only woman and paying attention to being treated differently.

### Mining the to-do-list

There needs to be an idea of where we’re heading. But the road ahead might be only clear for the next few steps, instead of all the way. An important thing for a driver is keeping track of the work ahead. There’s three main things to consider on this:

* **Timing**: Find the right time to use an item on the list. What should be done first, what would make a coherent shared story in your pairing. What choices would enable you as the navigator to care for your driver in the best possible way?

* **Backlog**: what is there on the list of things to do? Your backlog is best if it can somehow be part of the code and become a shared view — with consume-first style. But you can also make notes by scribbling on a piece of paper of a whiteboard. Whatever you need to keep track of things. Notes are disposable, code (including test code) is what remains when you’re done.

* **Prioritisation**: Deciding what comes next and in what order to do things. It’s not just about the right time in long term, but the right thing right now. And it keeps changing as you learn.

### Express a in-a-nutshell idea of what you’re doing

As a navigator in strong-style, you are not supposed to have to justify all your chosen actions to your driver. Sometimes the driver has little clue on where you’re about to be heading, and a great practice in these cases seems is to *invite temporary trust* saying you’d like to just go to this direction for like 10 minutes, and if they are still unsure about doing this, you can change then. The argument of what is right thing to do takes easily more time than that. And nothing stops the pair of you implementing both of your ideas and then deciding that a third, completely different option is what you should go for. With programming in particular, there’s a lot of uncertainty that unfolds only through implementation and experimentation.

If you need to express what you’re doing, you should learn to express that in a very concise format. Instead of all the rationale, pick only the part of the message that is absolutely relevant to care for your driver.

### Immediate feedback

When you navigate, keep an eye on your driver. Double-check with questions what the driver does. And if the driver does something you consider a problem, help them correct it right away. Feedback belongs with the action the feedback relates to.

## Closure Activities

### Recognizing time to switch

Either one in the pair can suggest a switch of roles. But as a navigator, you are usually in a controlling position, so your position gives you a bit of extra responsibility to pay attention to when the driver would have ideas that she should navigate on. You want, in the long term, to build a pair where both can contribute. Switching pairs gives a chance to try out the other role, and only practice helps you get better.

### Step back and think about what you’re doing

Sometimes you may feel you get bogged down into the details of implementation, and you might want to take a step back and think if you are spending your efforts in the right area. You may not notice without intentional step back to look at the bigger picture, because you’re going fast with support of your pair (and usually a nice bunch of unit tests too).

### Retrospectives

Looking at your collaboration and how the two of you feel about it on regular intervals is also necessary. Not just looking at what you implemented and stepping back on that, but talking about what you learned and what you like and dislike about your collaboration, in a constructive tone.

## Ending this with a word of warning

I’ve started to really enjoy looking into the dynamics of this style of pairing. But there’s a story I learned, that I also find very specific to this style.

Two programmers were pairing in strong-style and had the time of their life. There was a lot of talk, as all ideas must go verbally for two people to share. Sometimes the discussions were very enthusiastic and to an outsider they might have appeared even heated.
While the pair was enjoying, the environment that did not recognise the different pairing style was betting on which one of the two in the pair would quit first.

Don’t care just for your pair, care also for your environment. Verbalising your thoughts makes them available for more people than just the two of you. Take it as an opportunity to build relationships outside your immediate pair.
And it is not always that the pair is enjoying. Your pair not opting to work with you again is feedback that the way you’re connecting isn’t appropriate. A pair is two people, where both need to feel comfortable.
