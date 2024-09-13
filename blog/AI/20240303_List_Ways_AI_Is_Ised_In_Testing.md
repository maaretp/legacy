# List Ways in Which AI is Used In Testing

I have now been through 3 out of 30 days of AI in Testing by Ministry of Testing. I was awarded my fifth Anniversary Badge, meaning that I have not shown up in that community for a while. 

![MoT Anniversary announcement](anniversary.png)

The first day was introduction. Second day was to read an introductory article. Third day asked to list ways AI is used in testing. As with blogging, I filled the paper and wanted to leave the notes from personal experience behind as a blog post. 

Practical applications, personal reflection rather than research:

**Explaining code**. Especially on particularly tired day while being aware that I cannot share secrets, I like to ask chatGPT to explain to me what changes with code in some pull request so that I would understand what to test. Answers vary from useful to hilarious, and overly extensive.

**Test ideas for a feature**. Whenever I have completed an analysis of a feature to brainstorm my ideas, I tend to ask how chatGPT would recommend me to test it. Works nicely on domain concepts that are not this company only, and I have a lot of that with standards and weather phenomena.

**Manipulating statistics**. I seem to be bad at remembering excel formulas, but I use a lot of cross-referencing test generated results in excels. ChatGPT has been most helpful in formulas to manipulate masses of data in excel.

**Generating input/output data**. Especially with Co-pilot, I get data values for parameterized tests. Same test, multiple inputs and outputs generated. More effort into reviewing if I like them and find them useful.

**Generating (manual) test cases**. I have seen multiple tools do this, and I hate hate hate it. I always turn off steps from test cases and write down only core insights I would want the future me to remember in 3 months.

**Generating programmatic tests**. Copilot does well on these on unit testing level, but I am not sure I would want all that stuff available. Sometimes helps in capturing intent. But I prefer approvals of inputs and outputs over handcrafted scripts anyway for unit level exploratory testing.

**Generating tests based on models**. Has nothing to do with AI, but is a pre-AI practice of avoiding writing scripts and working with more maintainable state-based models. Love this, especially for long running reliability testing.

**Generating database full of test data**. Liked tools of this. I think they are not AI though, even though they often claim they are. The problem of having realistic pattern but not real people’s data is a thing.

**Refactoring test code**. Works fine at least for robot framework and python tests as long as we first open the code we want to move things from. Trust things to be pre-aware and suffer the duplication. We’ve been measuring this a bit, and copilot seems to encourage duplication for us.

Wrote down few, will revisit when time is right. 