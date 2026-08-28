---
title: "Starter Project Overload - just tell me the steps"
date: 2020-07-14
theme: general-and-reflections
labels: []
source: https://visible-quality.blogspot.com/2020/07/starter-project-overload-just-tell-me.html
---

# Starter Project Overload - just tell me the steps

*Published 2020-07-14*  
*Source: <https://visible-quality.blogspot.com/2020/07/starter-project-overload-just-tell-me.html>*

---

Today, I ended up spending a few hours setting up a javascript - jest - puppeteer environment, to enable comparison of the tests we do on a third framework (we did this before with record-playback within Datadog and Robot Framework). The two others served as stepping stones to understanding what you can and can't test and what maintenance of the scripts feel like, and continuing with either of the two in our team would mean that these tests belong to the tester alone. So Javascript is a definite priority for sharing with the rest of the team.

Googling around did not make getting set up easy and fluent. There is too much instruction, unsurprisingly. The question from the intern is well warranted: "How the hell are you supposed to know which of these articles are worthwhile sources?"

My blog does not match the criteria of worthwhile sources I explained them: seek material as close to the original open source project as possible. But I thought I'd still write down for fun and benefit how simple it turned out to be.

To get the jest - puppeteer environment running to a point where you can start writing your own tests, here is what to do.

1. Install yarn (=> google "install yarn" and install as instructed)  
   Yarn is a package manager. It pulls down packages someone else made available.   
   NPM is another package manager. You could use that too, the commands are just different then.   
   And yes, package manager is something you need on your development machine. The packages it brings down to your project are different in the sense that they are dependencies for what you build. The steps to install dependencies with package manager are setup, and you don't want all those files to be same for every single programming project you do on your computer.
2. Create a folder for your programming project to reside in and open the folder in VS Code  
   This step is for familiarity and control. Having nothing and being in the empty folder when working with a new tool gives sense of control.
3. Run Terminal (from Terminal | New Terminal in VSCode) and install dependencies  
   You will want to run   

   ```
   yarn add jest  
   yarn add puppeteer  
   yarn add jest-puppeteer
   ```

   that will create you a bunch of files under your empty folder under node\_modules folder.
4. Add jest to your path so that you can run it from command line  

   ```
   yarn global add jest
   ```
5. Initialize jest to create the configuration file  

   ```
   jest --init
   ```

   This creates jest.config.js file.
6. Test that jest alone works for you  
     
   Create a file sum.js  

   function sum(a, b) {

   return a + b;

   }

   module.exports = sum;

     
   Create a file sum.test.js  

   const sum = require('./sum');

     

   test('adds 1 + 2 to equal 3', () => {

   expect(sum(1, 2)).toBe(3);

   });

     
   Straight out of Jest Getting Started!   
     
   Run the tests  

   ```
   jest
   ```
7. Add jest-puppeteer to jest.config.js file  

   ```
   "preset": "jest-puppeteer"
   ```

   While at it, comment out   

   ```
   testEnvironment: "node",
   ```
> This step was the one that I was hunting for an hour! For everyone's benefit, I could have used the energy I use on this post to help correct the original jest documentation but I ended up adding to newbie confusion.

8. Test that jest puppeteer works for you  
     
   create a file google.spec.js   
   (NOTE! spec, not test or it worn't work - the second thing that was causing me pain in this flow)   
     

   describe('Google', () => {

   beforeAll(async () => {

   await page.goto('https://google.com');

   });

   it('should be titled "Google"', async () => {

   await expect(page.title()).resolves.toMatch('Google');

   });

   });
9. Replace all tests/specs with whatever you want to work on.

Next up is putting these in a container without using a container project starter. But that must be another blog post for my future reference.
