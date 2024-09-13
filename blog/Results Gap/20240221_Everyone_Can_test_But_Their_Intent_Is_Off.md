# Everyone can test but their intent is off

Over my 8 years of ensemble and pair testing as primary means of teaching testers, I have come to a sad conclusion. Many people who are professionally hired as testers don't know how to test. Well, they know how to test but from their testing, there is a gaping results gap. Invisible one. One they don't manage or direct. And the sad part is that they think it is normal.  

If you were hired to do 'testing' and you spent all your days doing 'testing', how dare I show up to say your testing is off?!? I look at results, and the only way to look at results you provide is to test after you. 

My (contemporary) exploratory testing foundations course starts from a premise of giving you a tiny opportunity to assess your own results, because the course comes with the tool of turning invisible ink to visible, that is listing of problems me (and ensembles with me) have found across some hundreds of people. I used to call it 'catch-22' but like usual with results of testing, more work on doing better has grown the list to 26. 

Everyone can test, like everyone can sing. We can do some slice of the work that resembled doing the work. We may not produce good enough results. We may not produce professional results that lead into paying for that work. But we can do something. Doing something is often better than doing nothing. So the bar can be low. 

![Everyone can test](everyone.png)

An experience at work leads me to think that some testers can test but their intent is so far off that it is tempting to say they did not test. But they did test, just the wrong thing. 
Let me explain the example. 

The feature being tested is one of sending pressure measurement values from one subsystem to another, to be displayed there. We used to have a design where the value of the first subsystem that was used on its user interfaces after various processing steps was sent forward to the second subsystem. Then we mangled that value because it followed no modern principles of programmatically processable data so that we could reliably show the value. We wanted to shift the mangling of the data to the source of the data, with information about the data, just in a beautiful modern wrapper of a consistent data model.

Pressure measurement was the first in the line of beautiful modern wrappers. The assignment for the tester was to test this. Full access to conversations with the developer was available. And some days after the developer said "done and tested", the tester also came back with "tested!". I started asking questions. 

I asked if one of the things they tested was to change configurations that impact pressure values so that they can see differences of pressure at sea level (a global comparison point) and at the measurement location. I got an affirmative response. Yet I had a nagging feeling, and built on the yes inviting the whole team to create a demo script for this pressure end to end. Long story short, not only did the tester not know how to test it, it was not working. So whatever they called testing was not what I was calling testing. The ensemble testing session also showed that NO ONE in the team knows the feature end to end. Everyone conveniently looks at a component or at most a subsystem. So we all learned a thing or two. 

Equipped with the information from the ensemble testing experience, the tester said to take more time testing before coming back with "tested!". They did, and today they came back - 7 working days later. I am well aware that this was not the only thing they had on their agenda - even if their agenda is on their full control - and we repeated the dance. I started asking questions. 

They told me they updated the numbers in the model we created for the ensemble testing session. I was confused - what numbers? That model sketched early ideas of how three height parameters would impact the measurements in the end, but it was a quick sketch from an hour of work, not a fill in the ready blanks model. So I asked for demo to understand. 

I was shown how they changed three parameters of height. Restart the subsystem. Basic operations of the subsystem they have been testing for over a year. The interesting conversation was on what did they then test. It turns out they did the exact same moves on the subsystem on a build without the changes and on a build with the changes. They concluded that since the difference they see is in sending the data forward but the data is the same, it must be right. Regression oracle. But very much partial oracle, and partial intent. 

In the next minutes, I pulled up a 3rd party reference and entered the parameters to have comparable values. We learned that they had the parameters wrong, because if the values aren't broken with the latest change, then the change of configuration is likely incorrect. They did not explore values for plausibility, and they were way off. 

I asked to show what values they compared, to learn they chose an internal value. I asked to pull up the first subsystem's user interface for the comparable values. Turns out that the value they compared is likely missing multiple steps of processing to become the right value. 

For junior testers such as this one, I expect I will coach them by having these conversations. I have been delighted with picking up information as new information comes, and I follow the trend of not having to cover same ground all the time. I understand how this blindness to result comes about: in most cases testing a legacy system, the regression oracle keeps them on path. In this case, it leads them to the wrong path. They only took ISTQB course which does not teach you testing. I am their first person to teach this stuff. But it is exhausting. Especially since there are courses like mine or like BBST that they could learn from, and provide the results for the right intent. Learn to control their intent. Learn to *explore*. 

At the same time, I am thinking that all too often juniors to testing - regardless of their years of experience - could learn slightly more before becoming same costs as developers. This level of thinking would not work for a junior developer. 

Testers get by because they can be just without value. Teamwork may make them learn or become negative value. But developers don't get by because the without value of their work gets flagged sooner.  