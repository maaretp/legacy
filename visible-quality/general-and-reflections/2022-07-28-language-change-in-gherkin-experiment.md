---
title: "Language change in Gherkin Experiment"
date: 2022-07-28
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2022/07/language-change-in-gherkin-experiment.html
---

# Language change in Gherkin Experiment

*Published 2022-07-28*  
*Source: <https://visible-quality.blogspot.com/2022/07/language-change-in-gherkin-experiment.html>*

---

I find myself a Gherkin (the language often associated with BDD) sceptic. The idea that makes other people giddy with joy on writing gherkin scenarios instead of manual tests makes me feel despair, as I was never writing the manual tests. The more I think about it and look at it, the more clear it is that the Gherkin examples when done well are examples rather than tests, and some of the test case thinking is causing us trouble.

What we seek with Gherkin and BDD is primarily a conversation of clarity with the customer and business. When different, business-relevant examples illustrate the scenarios our software needs to work through, the language of the user is essential.

In our experiment of concise-but-code tests vs gherkin-on-top tests, I find myself still heavily favouring concise-but-code.

def test\_admin\_can\_delete\_users(

assigned\_user: User, users\_page\_logged\_in\_as\_admin: UsersPage, users\_page: UsersPage

) -> None:

users\_page\_logged\_in\_as\_admin.create\_new\_user(assigned\_user.name, assigned\_user.password)

users\_page.delete\_user(assigned\_user.name)

I'm certain that the current state of fixtures has some cleaning up to do, but I can have a conversation also with this style in user's language. Before implementing, we talk in Friends format *the one where admins can delete all users including themselves* and after implementing, we have the format turned into something where just the name of the test(s) and main steps need to be occasionally looked at together.

It is clear though this is not a format in which the users/business would already be writing our tests for us, and currently I am in a team where we have a product owner who would love nothing more than to be able to do that. There is also a sense of security for external customers if we could share them the specs that we test against that makes considering something like Gherkin worthwhile.

In this post, I want to look at the [user/business collaboration created Gherkin](https://gist.github.com/maaretp/2e789f210d553b4542b238f3990d4321) for this feature in our project compared to the [result that is running in our pipeline](https://gist.github.com/maaretp/34b7fff26560f73c6f2aac2f5839f6f1) today. Luckily, the feature we are experimenting is so commonplace that we reveal absolutely nothing of our system by sharing the examples.

[![](../_images/screenshot-2022-07-28-at-15-39-20-35e80c80.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglNGOR7X77Ju05wSbjEca8OkJNvVxHzWGjVJ8yZV_n19oWbA4wKUQ5P47Il6ohLjJZVHL4900jawW0RPbd0rbp9lWPV_-B3wq7NhwHpEa0w_nWdANjzDRar83EDaXnRaOBdfiwoo4rFYKCXsAGCR6sEcVyoWLtoor-I-7e8HgoQLdU2NvEKMBNzLE/s1278/Screenshot%202022-07-28%20at%2015.39.20.png)

The user/business collaboration generated examples started with two on creating new users:   

[![](../_images/screenshot-2022-07-28-at-15-45-41-e808ea5b.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinjQ67iAoxNfDek03c3vUC1UVCtlEcgDSFHS6kg68qNjnVVkjxX1Ch44EZ9I8YimNsFCFBTULNr-Mpm3qxoD3yb1NAD-FcF5n7wQgM3aRWmiOaPH3habCLXHUc-nc4Q2I_gOZ-8hmYe-53N9KzKT49lo4ja6yq9DtbrAB1wvtaQnVrfJc-32f8Tkw/s1034/Screenshot%202022-07-28%20at%2015.45.41.png)

**From: old**

These turned to three by now.

[![](../_images/screenshot-2022-07-28-at-15-47-44-76d631fe.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEir9LOzQvMW2PP0T8MvovpdYtJ9CUcZeIdkN7SkfxcJjZbflqaIe3ydB6g8XAQOmU-eoBhpkbNva2-4SUw9rGQyPC9YG7JrI6hQA-voWeXxa39Xk5arrGz3z6MkZrOWDjYBrUwUVTOtnRg1Os0Fy-7397uobF8UI6f2eAeUz518jRfVLFztyL_eT3Q/s984/Screenshot%202022-07-28%20at%2015.47.44.png)

[![](../_images/screenshot-2022-07-28-at-15-48-03-f0818394.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBP5ijpVaHPmm6NdqgBaQvp1ecYv-G_0Wbd6JrvfxkthAw5Xxnf3AvypocWyyDNRvVkjhp2N65bHIoZ0jnhXeg8uRTLtR5ngjOLYk6nmqsBQNawTKvMZFcS0GJQ_j_wm2KvvMg0t5laYVDw0_hfxJdSgPuDVWBF71QF8jbwk6fKGVuEntHsqnFv1E/s1088/Screenshot%202022-07-28%20at%2015.48.03.png)

**From: new**

  

You can see a difference in language. Earlier we talked about users, where some of them get admin rights and others don't. Now, the language emphasis is on having admin and user. Also the new language isn't yet consistent on these, having admin and admin user used interchangeably in the steps. The new language also reveals a concept of default admin, which just happens to be one user's information on the database when it starts - clearly something where we should have a better conversation than the one I was around to document with the user/business collaboration session.

The second one of the new also threw me off now that I compare it. I first reacted on admin's not being able to create users without admin rights - there is no admin without rights, those are the same thing. But then I realized that the it is trying to say *Admin can create users that are not admins.*

Another thing that this sampling makes obvious is that two scenarios turned to three, and the split to creating admins and users makes sense more for a testing point of view than business point of view. Again, admin is just a user with admin rights. Any user could be an admin, permanently or temporarily.

Similarly, it turned longer. Extra steps - deleting in particular - was introduced as step to each. Clearly a testing step made visible, and adding most likely not the essential part of the example for user/business.

And it also turned shorter. Changing password, the essential functionality originally described vanished and found a new home, simplifying this scenario as it was also separately described in the original.

[![](../_images/screenshot-2022-07-28-at-16-07-15-401036d6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwxYEjGvwiETT5DfVZb0ZJsYcDj5SPN-5hhqZWcCRo3Rb8UdlJmcJHG9_lqjBv_LhpPMsm3gkzT004wmceAPBgd0KMzmp1iYaYF5ZoZ0seKXN6lgb-RgYALjeIeA3GFYKNPAmN2jPYBkGQ-IqSCMKBSx66r30JAGv-AqaoDHgLO4SOZsblhv9OJOs/s1200/Screenshot%202022-07-28%20at%2016.07.15.png)

**From: new**

[![](../_images/screenshot-2022-07-28-at-16-14-24-c9a7d321.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbhzBze-cJmNuuj_3eTSqBx5ICAMNlYUcpg5oBt-FC4e_KHWyRz7m_UBUT09sHNGG3uN5pLPN0EQ5cbfMWFY55jgQhacSKL9yVp9wNLQt9s9_8wmCwuhNQuzWXMt84TkDkS1wdxRQvqtIGDmBbu5878S5gwbQHS58nXQf3DKKj36JokfJJ77mBRgI/s842/Screenshot%202022-07-28%20at%2016.14.24.png)

**From: old**

With this one, steps exist for testing purpose only. They now describe the implementation. A common pitfall, and one we most definitely fell into: not illustrating the requirement as concisely as we could, but illustrating operating of the system as test steps.

Interestingly, after the first example and mapping the original and the new, we have six things that originate with user/business, and only one that remains in the implemented side.

[![](../_images/screenshot-2022-07-28-at-16-09-58-f74e5e65.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9TKux41vIx8UoqIN3IY0BZ6Myayja4RM3XPTdlKa1Dm1DS748cY43gNguP5P0c581un3BSzlbB4uGSw9rb8Si334hIbd2P4Ay_VjIyZISztBagP0d7NmnOGJb0HuXbG0CaSzswByioc1wS91x58oa24ztSnGnhDDTSr5Mv41wUr9UDPfD4BKPK5M/s986/Screenshot%202022-07-28%20at%2016.09.58.png)

**From: new**

  

We can find the match from the originals to this one.

[![](../_images/screenshot-2022-07-28-at-16-12-35-5ad04868.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge6_oQD0ILkUuLRIdB3ftU-Zm71XVB-hophaDRaK_P_PeK6hOfFpNCTrjvSo2lCiFfEdw-wL8RUiom9VF_fknCxLs-2GGL7zOEsm_nNPcGORIS3iHIbHtnZUDBLObbUuwl_rz4tAeQmPsBYMM-Tt9q2QPLb76_Xunkj6yIDxrnU3Dbi-OYSliEClY/s664/Screenshot%202022-07-28%20at%2016.12.35.png)

From: new

  

So what else got lost in translation? These three.

[![](../_images/screenshot-2022-07-28-at-16-16-32-87c924f4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMVUS1io7cwIvVBicfw7K1t6ZinhQU-jrtr18ggmzRAKHdXAHexdNYGZR7Tibfh5qS6zMEcpNoGdMp-MKxctr36vXAxay5RhBG9dLh5Zu5FHbrfG686heZq2J0D43z_5cJgtg0LyUV9K2pkudC7poQ7sTA1aeHuHuTvJf6jOdE8i5ZNFJs4bjU1qw/s1232/Screenshot%202022-07-28%20at%2016.16.32.png)

  

[![](../_images/screenshot-2022-07-28-at-16-16-48-59450056.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinN-etQqF91JTfcCAB50HIjP-Hy5zBvVs7o1xzPFMEEsDMLIc5dXm-AS5aTPR4WImJRJlYNIAmjBOdNSBc-VjIUQjpSkE6-_dNGndV9tQfWiAQHk1LxQKgKLmWK7n3ZPhh-mWamChqLpiqFk3s9zeMJJmGi54NsO4qBAxheJbEM1sT9GZAjdEfmIA/s814/Screenshot%202022-07-28%20at%2016.16.48.png)

From: new

The first two are the real reason why such functionality exists in the first place, and it is telling that those are missing. They require testing two applications together, a "system test" so to speak.

The last one missing is also interesting. It's one that we can only do manually editing the database after no admin access, again a "system test".

Having looked at these, my takeaways are:

1. Gherkin fooled us in losing business information while feeling like it was "easier" and "more straightforward". The value of reading the end result is not same as value of reading the business input.
2. Tests will be created on testing terms and creating an appearance of connection with business isn't yet a connection
3. The conversation mattered, the automated examples didn't.
