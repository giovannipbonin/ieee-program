# The Internet-Taught Software Engineer - A Student-to-Student Class and Experiment

### Note
Class Author: Giovanni Pascotto Bonin
- I am more than willing, and would be happy to mentor anyone - who is highly motivated - in any stage and give advice based on my experiences. I am also just in the start of my career, but I've had to overcome all kinds of obstacles and there is plenty of advice I can give for people looking for jobs in the Bay Area. Feel free to email me: pbonin.giovanni@gmail.com

- I decided to create this class to teach while I am the president of IEEE at the University of Miami to supplement the school's curriculum, open doors for students to engage in discussions and interactions on the subject, as well as create a foundational framework for our organization on campus for future semesters. 

- If someone else decides to run something similar to this on their campus, I am also running guest speakers (in addition to each of these sessions), and that's a really good way to engage professional experience in your organization, as well as have experienced engineers potentially help you with the program. 

#### Acknowledgements:
- There are many other sources I have used to create this guide and I am very thankful for all the people that have put them together. I have heavily used resources and structure from @jwasham's Google Interview University guide. 


### Communication
I was initially going to use a Slack channel for this, but then I realized that most people don't have their Slack account open all the time, and realistically most won't download the app and have notifications on. So we will be using the IEEE Facebook group chat, to take advantage of the sad fact that people are on Facebook all the time and thus will receive the notifications. Send me an email or let me know in class that you want to be added to the group. We will also send announcements on orgsync, so if you don't have fb it's ok.

## Table of Contents
- [Week 0](#week-0)
- [Week 1](#week-1)
     1. About Silicon Valley, Google, Facebook, and Startups - Motivation
     2. Interview Process & General Interview Prep
         * Emacs and vi(m)
         * Unix and Command Line Tools 
- [Week 2](#week-2)
     1. Algorithmic complexity / Big-O / Asymptotic analysis
     2. An Overview of Data Structures and Algorithms
- [Week 3](#week-3)
     2. Basic Algorithms: Binary Search and Sorting
     3. Recursion 
- [Week 4](#week-4)
     1. Machine Learning - Supervised Learning
     2. Machine Learning - Unsupervised Learning
- [Week 5](#week-5)
     1. Heaps and Balanced Trees
     2. Dynamic Programming
- [Week 6](#week-6)
     1 & 2: Graphs and Search
- [Week 7](#week-7)
     1. Knapsack problem and More Dynamic Programming
     2. Shortest Paths Revisited, NP-Complete Problems and What To Do About Them
- [Week 8](#week-8)
     1. Bitwise operations, Discrete Mathematics, and NP Completeness and Computability
     2. Caches, Processes and Threads, and other topics
- [Week 9](#week-9)
     1. Testing and System Design
     2. Putting it all together and Review
- [Week 10](#week-10)
     1. Practice




# Week 0

## Session 1 

First meeting and announcement:

Here the plan is to announce the program to the general body meeting, get input from the students on final things they might be interested in learning on top of the program, as well as finding out times that will work for most people.


## Session 2

Guest Speaker (CEO of Kairos Analytics): Feb 23rd 6:30 pm at MEA 202

# Week 1 

## Session 1 - About Silicon Valley, Google, Facebook, and Startups - Motivation

## Talk


#### Major interview tip 

Before anything else: 
- Few people would reference professional athletes when talking about software engineering tips, but by having an attitude toward your career similar to that of an athlete toward his, there is a lot I've learned. One of my favorite athletes, Muhammad Ali, was asked how many sit-ups he would do and his reply was: "I don't count my sit-ups, I only count when it starts hurting, because that's when it really counts."

There is nothing like working your hardest in the road to achieving your dreams. This lecture series is just a compilation of advice both from various amazing people I have met, and some I observed on my own. I am passing this advice along, but keep in mind the only way for you to be able to solve new problems is to develop the foundation through discovery yourself. Practicing to solve these problems on your own is the only way to create those neural pathways. 

I actually learned a lot about learning in this Coursera class I took in my last semester in college: 

- https://www.coursera.org/learn/learning-how-to-learn

To practice, get one of the recommended books with a list of exercises and hammer through it! Do all these problems, do one per day, or do two, or three, depending on how much time you have. There's no excuse to not do at least one of them a day until you feel comfortable enough to go to an interview feeling that you will make it. 

Success leads to confidence (conversely from what people believe), so the more you successfully solve problems the more confident you will be. Start small, build your skills, and you will make it. It's hard to properly emphasize just how helpful these books are.

- [Programming Interviews Exposed: Secrets to Landing Your Next Job, 2nd Edition](http://www.wiley.com/WileyCDA/WileyTitle/productCd-047012167X.html)
- [Cracking the Coding Interview, 6th Edition](http://www.amazon.com/Cracking-Coding-Interview-6th-Programming/dp/0984782850/)
- [Elements of Programming Interviews](https://www.amazon.com/Elements-Programming-Interviews-Insiders-Guide/dp/1479274836)
 
#### What Silicon Valley looks like
![Silicon Valley](https://sethsphd.files.wordpress.com/2014/03/in-the-heart-of-silicon-valley.jpg)


#### It also look a lot like this
![Coding at the whiteboard - from HBO's Silicon Valley](https://dng5l3qzreal6.cloudfront.net/2016/Aug/coding_board_small-1470866369118.jpg)

### The Purpose of This Guide - Everything I'd wish I was taught earlier on

This program will help you understand computer systems, algorithm efficiency, data structure performance, 
low-level languages, and how it all works together. These subjects are extremely important, and the hiring process for Google (and Silicon Valley companies in
general) places a huge importance on them. There is no shortage of studying, the more you know about these subjects, the better.

Before I started college I started learning computer science on my own, although I'd wish I had started even earlier given I was already 17. But due to
some obstacles in my career choices I didn't dive in until that point, but when I did I committed as if I was born to do this. Before college, I had a gap year.
During that period, when I found websites such as Coursera, MIT OpenCourseware, and a multitude of other content on the internet such
as free textbooks and all that, I realized there is nothing short of motivation that can stop any of us from becoming one of the best at any field we want to excel in.

When I started college, I realized that I could actually learn better on my own than I could learn in class, so if that's the case for you, embrace it and pursue your passion
in the way you know works best. The goal of this is to be a list of resources that can be followed and give you a good coverage on what's important, specifically filling in the gaps left by a typical computer science or software engineering curriculum.
It turned out for me that by the end of my college career I wanted to work for a startup, as that way I can have a bigger impact in something that is
in its early stages and really needs to be pushed forward. These experiences with learning told me to go work for a startup fixing education with 
technology.

This is a long plan, and some interviewers will even tell you that some of this stuff is more advanced than you need. In fact, I found this guide
after accepting my full-time offer with my favorite startup in the world (Coursera), and I am going through it now (for fun) since practice is never too much,
and some of this stuff I haven't had time to cover before, but it is well worth it to be good at what we do.

So yes, it might be true that some of these things don't often show up in an interview. But that's until it does, and you
start thinking to yourself DAMN this is my favorite company, I should really have spent that weekend learning about this, now I have to wait a year to reapply.

This is not the SAT or MCAT. The reason why software companies want us to know these subjects is because it is important
for our jobs, and the more we know about it the more we can build, the faster we can create, and innovate. Although you might not be designing algorithms
on a daily basis as a software engineer (although some engineers do exactly that), becoming good at this will develop the right way of thinking that you need
to solve problems of all sorts in systematic and efficient ways.

### Logistics

I remodeled the guide as a curriculum to be conducted on a weekly basis, as well as adding a lot to it. Again, it's a work in progress that I am doing in my free time,
and I plan on properly breaking down the outline so that it evenly fits across weeks. We will try to meet twice a week and have extra content for
the ambitious who want to do more at home, but the idea is that during the sessions we will cover one or two pieces of content for each subject and
have extra to be done at home.

For those wanting to track their progress at home, just fork the repo and mark an [x] on the items you have done, commit and push it.

Instructions: not familiar with git yet? No worries http://rogerdudler.github.io/git-guide/ 
Or, if you are a University of Miami student, you have a free subcription to Lynda.com and you can take this quick start Git and GitHub course: https://www.lynda.com/Git-tutorials/Up-Running-Git-GitHub/409275-2.html


### It's All About Discipline
- People put too much emphasis on IQ as opposed to emotional intelligence. After a certain level of IQ what really matters is dedication, passion,
and good discipline toward your work. Most of the famous genius engineers that we all know and heard of struggled with these topics too at one point,
but with the right discipline and passion they became really good at it by sticking to it. So never be discouraged!

- Check the home assigned readings and videos for "The Myth of the Genius Programmer" 


### Silicon Valley

#### History and the Future
todo
#### The Personality, Values, and Culture of Silicon Valley
todo
#### It's not about Silicon Valley as a Location, it's about the values it has inspired
todo


Play in lecture:
- [ ] [The Evolution of Search (video)](https://www.youtube.com/watch?v=mTBShTwCnD4)
- [ ] [How Search Works - Matt Cutts (video)](https://www.youtube.com/watch?v=BNHR6IQJGZs)
- [ ] [How Google makes improvements to its search algorithm (video)](https://www.youtube.com/watch?v=J5RZOU6vK4Q)
- [ ] [How to Work at Google: Prepare for an Engineering Interview (video)](https://www.youtube.com/watch?v=ko-KkSmp-Lk)
- [ ] [How to Work at Google - Candidate Coaching Session (video)](https://www.youtube.com/watch?v=oWbUtlUhwa8&feature=youtu.be)
- [ ] [Google Recruiters Share Technical Interview Tips (video)](https://www.youtube.com/watch?v=qc1owf2-220&feature=youtu.be)
- [ ] [How to Work at Google: Tech Resume Preparation (video)](https://www.youtube.com/watch?v=8npJLXkcmu8)

## Resources that helped my career
- Code2040: a wonderful fellowship program for Latinos and African-American students who want to work in Silicon Valley.
  It made a huge impact in my career by exposing me to the industry, and I spent a whole 
  summer meeting extremely talented people working in companies across Silicon Valley 
  who are also motivated to fix the world's greatest problems:  www.code2040.org
- Google: Seriously, use it. If you have a question, instead of beating your head against the wall, just Google it, 
  unless you are doing an exercise and you are not supposed to Google the answer. But no one is supposed to 
  know what a Turing Machine is without first learning it. So if you feel discouraged, just remember that it's never 
  too late to pick up on something. There are so many resources out there for free.
- Coursera (www.coursera.org): With the above in mind, Coursera made a huge impact in my career. 
  When I realized I could learn anything I wanted from the best professors in the world, and for free. And that if I wanted to impress recruiters
  I could also get a certificate from Stanford. It really pays off to show you are investing in your skills.
  Disclaimer: the favorite startup in the world I mentioned I will be joining is Coursera, 
  but that's the reason why I will be joining them, because it made a huge impact in my life. www.coursera.org
- Pramp: I used this a couple times, it's a cool platform where you can schedule mock interviews with strangers

Reading at home:

- [ ] A list of resources that was created by Google: [Google Careers: Technical Development Guide](https://www.google.com/about/careers/students/guide-to-technical-development.html)
- [ ] Conference, you should definitely watch this [Made by Google announcement - Oct 2016 (video)](https://www.youtube.com/watch?v=q4y0KOeXViI)
- [ ] [How Search Works - the story](https://www.google.com/insidesearch/howsearchworks/thestory/)
- [ ] [Phone Screen Questions](http://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions)
- [ ] [How Search Works](https://www.google.com/insidesearch/howsearchworks/)
- [ ] [Get That Job at Google](http://steve-yegge.blogspot.com/2008/03/get-that-job-at-google.html)
- [ ] [How Google Search Dealt With Mobile](https://backchannel.com/how-google-search-dealt-with-mobile-33bc09852dc9)
- [ ] [Google's Secret Study To Find Out Our Needs](https://backchannel.com/googles-secret-study-to-find-out-our-needs-eba8700263bf)
- [ ] [Google Search Will Be Your Next Brain](https://backchannel.com/google-search-will-be-your-next-brain-5207c26e4523)
- [ ] [The Deep Mind Of Demis Hassabis](https://backchannel.com/the-deep-mind-of-demis-hassabis-156112890d8a)
- [ ] The myth of the Genius Programmer](https://www.youtube.com/watch?v=0SARbwvhupQ)

[ ] Start reading 20 minutes a day (or whatever fits your learning style/routine): 
[Book: How Google Works](https://www.amazon.com/How-Google-Works-Eric-Schmidt/dp/1455582344)


## Session 2 - Interview Process & General Interview Prep

Talk points: 

### Interview Confidence

 - Be confident, but not arrogant

### Talk while you think, and code, explain everything that might be ambiguous


### If running out of time and need shortcuts, explain how you would not do the shortcut in a real scenario

### The interviewer is there because they want to hire someone, they are your friend not your enemy
- If they give you a hint, take it, don't be cocky

- Discuss last session's coverage, and home readings. Very encouraged for students to share their insights with each other and motivations (20 minutes of discussion)

- [ ] [Gayle L McDowell - Cracking The Coding Interview (video)](https://www.youtube.com/watch?v=rEJzOhC5ZtQ)
- [ ] [Cracking the Coding Interview with Author Gayle Laakmann McDowell (video)](https://www.youtube.com/watch?v=aClxtDcdpsQ)
- [ ] ['How to Get a Job at the Big 4 - Amazon, Facebook, Google & Microsoft' (video)](https://www.youtube.com/watch?v=YJZCUhxNCv8)
- [ ] [How does CPU execute program (video)](https://www.youtube.com/watch?v=42KTvGYQYnA)
- [ ] [Machine Code Instructions (video)](https://www.youtube.com/watch?v=Mv2XQgpbTNE)

Reading at home:
- [ ] [ABC: Always Be Coding](https://medium.com/always-be-coding/abc-always-be-coding-d5f8051afce2#.4heg8zvm4)
- [ ] [Four Steps To Google Without A Degree](https://medium.com/always-be-coding/four-steps-to-google-without-a-degree-8f381aa6bd5e#.asalo1vfx)
- [ ] [Whiteboarding](https://medium.com/@dpup/whiteboarding-4df873dbba2e#.hf6jn45g1)
- [ ] [How Google Thinks About Hiring, Management And Culture](http://www.kpcb.com/blog/lessons-learned-how-google-thinks-about-hiring-management-and-culture)
- [ ] [Effective Whiteboarding during Programming Interviews](http://www.coderust.com/blog/2014/04/10/effective-whiteboarding-during-programming-interviews/)
- [ ] [Failing at Google Interviews](http://alexbowe.com/failing-at-google-interviews/)
- [_] http://www.byte-by-byte.com/choose-the-right-language-for-your-coding-interview/
- [ ] http://blog.codingforinterviews.com/best-programming-language-jobs/
- [ ] https://www.quora.com/What-is-the-best-language-to-program-in-for-an-in-person-Google-interview
[See language resources here](programming-language-resources.md)


### Talk points -  Important advice: Pick One Language for the Interview

1:
You can use a language you are comfortable in to do the coding part of the interview, but for Google, these are solid choices:

- C++
- Java
- Python

You need to be very comfortable in the language, and be knowledgeable, so pick one, and do all the practice problems in that language. The more you practice
the more natural it will look like you feel at developing with the language, and that's important even though knowing the syntax itself isn't. But there
is a subconscious feeling we get by looking at the flow of someone working with something, and it's important to give interviewers that feeling




2. You won't remember it all
As the author of the original guide said:
    "I watched hours of videos and took copious notes, and months later there was much I didn't remember. I spent 3 days going
    through my notes and making flashcards so I could review.

    Read please so you won't make my mistakes:

    [Retaining Computer Science Knowledge](https://googleyasheck.com/retaining-computer-science-knowledge/)"



 2. Review, review, review

Again, though interviewers say they don't care about you memorizing details, they do want to see that you're really good at what you do, 
so if you easily recall the details, you will look much better. 


 4. Focus

One of my struggles was trying to do too much at the same time. I not only wanted to get a job at my favorite companies, despite not going to a school where those companies would recruit, I also wanted to take a bunch of online classes on things that wouldn't help me with the interview or school, but would benefit my personal learning goals and career (such as machine learning and even stuff like philosophy and history and business). It is indeed 
possible to be good at all these things, but you can't do them all at once. ****Forget multi-tasking. ***** just schedule time in your calendar and focus on
one thing at each time.  If you can dedicate 2 hours of focused time to this guide every day, you will go a long way.


3. Studying strategy:

For each subject covered, read and watch the content covering it, and then **implement** it. Please, don't skip the implementation part, this is the most
important one. Do not look at AVL trees and think "Oh we covered that in my algorithms class", the interviewer will never care what your class covered, 
he or she will ask you to implement it.

Also, write tests to make sure the code works. Most interviewers also ask you to do that. (Or at least run through test cases, but run them on paper, not 
simply by plugging the input in, because on the whiteboard they want to see if you can think through the code you just wrote.

So basically the process is: 
- understand an algorithm or subject
- implement it on paper (preferably whiteboard while talking through it as an interview)
- test it by running through examples by hand and thinking through it
- Implement on a computer and test with real inputs

Note: you should use standard libraries of python when practicing. Unless, for example, the question is sorting an array, then you should ask the interviewer
whether he expects you to use the standard library or implement it yourself. When in doubt, always ask for clarification! Don't make assumptions, and don't be afraid to ask questions, it's a good thing.


### Starting with basics

- ### Emacs and vi(m)
    - suggested by Yegge, from an old Amazon recruiting post: Familiarize yourself with a unix-based code editor
    - vi(m):
        - [Editing With vim 01 - Installation, Setup, and The Modes (video)](https://www.youtube.com/watch?v=5givLEMcINQ&index=1&list=PL13bz4SHGmRxlZVmWQ9DvXo1fEg4UdGkr)
        - [VIM Adventures](http://vim-adventures.com/)
        - set of 4 videos:
            - [The vi/vim editor - Lesson 1](https://www.youtube.com/watch?v=SI8TeVMX8pk)
            - [The vi/vim editor - Lesson 2](https://www.youtube.com/watch?v=F3OO7ZIOaJE)
            - [The vi/vim editor - Lesson 3](https://www.youtube.com/watch?v=ZYEccA_nMaI)
            - [The vi/vim editor - Lesson 4](https://www.youtube.com/watch?v=1lYD5gwgZIA)
        - [Using Vi Instead of Emacs](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Using_Vi_instead_of_Emacs)
    - emacs:
        - [Basics Emacs Tutorial (video)](https://www.youtube.com/watch?v=hbmV1bnQ-i0)
        - set of 3 (videos):
            - [Emacs Tutorial (Beginners) -Part 1- File commands, cut/copy/paste, cursor commands](https://www.youtube.com/watch?v=ujODL7MD04Q)
            - [Emacs Tutorial (Beginners) -Part 2- Buffer management, search, M-x grep and rgrep modes](https://www.youtube.com/watch?v=XWpsRupJ4II)
            - [Emacs Tutorial (Beginners) -Part 3- Expressions, Statements, ~/.emacs file and packages](https://www.youtube.com/watch?v=paSgzPso-yc)
        - [Evil Mode: Or, How I Learned to Stop Worrying and Love Emacs (video)](https://www.youtube.com/watch?v=JWD1Fpdd4Pc)
        - [Writing C Programs With Emacs](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Writing_C_programs_with_Emacs)
        - [(maybe) Org Mode In Depth: Managing Structure (video)](https://www.youtube.com/watch?v=nsGYet02bEk)

- ### Unix command line tools
    - suggested by Yegge, from an old Amazon recruiting post. I filled in the list below from good tools.
    - [ ] bash
    - [ ] cat
    - [ ] grep
    - [ ] sed
    - [ ] awk
    - [ ] curl or wget
    - [ ] sort
    - [ ] tr
    - [ ] uniq
    - [ ] [strace](https://en.wikipedia.org/wiki/Strace)
    - [ ] [tcpdump](https://danielmiessler.com/study/tcpdump/)





# Week 2

## Session 1 -  Algorithmic complexity / Big-O / Asymptotic analysis


### Talk points:

- You should be so comfortable (afte preparing and going through this) with algorithm complexity and Big-O notation that it is a natural process for you.
- You should be able to look at algorithms and spit out what the algorithm complexity is, and as the name might suggest otherwise, it is not complex at all. In fact it is a method for quickly managing complexity while getting a good evaluation on how the algorithm will run for large-scale applications.
- Imagine if you could do math, and simply get rid of all constants and lower order terms, and just say how the given function grows as the input grows, this is basically it.

- [ ] [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- [ ] [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=V6mKVRU1evU)
- [ ] [Big O Notation (and Omega and Theta) - best mathematical explanation (video)](https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [ ] Skiena: [video](https://www.youtube.com/watch?v=gSyDMtdPNpU&index=2&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
- [ ] [A Gentle Introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
- [ ] [Orders of Growth (video)](https://class.coursera.org/algorithmicthink1-004/lecture/59)
- [ ] [Asymptotics (video)](https://class.coursera.org/algorithmicthink1-004/lecture/61)
- [ ] [UC Berkeley Big O (video)](https://youtu.be/VIS4YDpuP98)
- [ ] [UC Berkeley Big Omega (video)](https://youtu.be/ca3e7UVmeUc)
- [ ] [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [ ] [Illustrating "Big O" (video)](https://class.coursera.org/algorithmicthink1-004/lecture/63)


Home reading:
- [ ] TopCoder (includes recurrence relations and master theorem):
- [Computational Complexity: Section 1](https://www.topcoder.com/community/data-science/data-science-tutorials/computational-complexity-section-1/)
- [Computational Complexity: Section 2](https://www.topcoder.com/community/data-science/data-science-tutorials/computational-complexity-section-2/)
- [ ] [Cheat sheet](http://bigocheatsheet.com/)

## Session 2 - An Overview of Data Structures and Algorithms

### Talk points - Data structures
   - Here I will give a lecture on how data structures and algorithms relate to Big-O, why choosing the appropriate data structures and algorithms
   - can have a significant impact on asymptoptic complexity (Big-O). Furthermore I will make a clear distinction between algorithms and data structures, 
   - and show that at the same time they work together, and that efficient algorithms make use of efficient data structures to boost performance. 

  - I will focus on the big picture, giving an overview of popular and extremely useful data structures and algorithms, and in the future sessions we  will dive into understanding the list of algorithms and data structures that students are expected to know.
    

### What is a data structure - With Examples
   - A data structure is exactly what it sounds like: a structure in a computer used to store and organize data in a form that will be useful.
    - As you begin to think about them, you can draw on a paper to come up with a picture of how the data is organized. When doing this, don't worry about the lower levels of how computer might handle memory, or physically store it, just worry about how the data is organized. For example: an array is a data structure, and you could represent it as [3, 2, 3, 4, 5], or (4, 5, 1, 2), it doesn't matter. As you progress in computer science, you will learn that we use notations such as [] to represent data structure of certain behaviors and () for another, but when the notation is introduced then you learn about it.
    - We have data structures in the real world, a bookshelf is a data structure, except that the data are books. A line in front of your favorite Disney ride is a queue, where the data is people. Queues are useful to preserve the order in which the elements arrived, in computing that's a very useful concept, for many systems, ranging from simple design of systems where users might be placed on a queue to chat with an agent, or even search algorithms which we will cover later, such as breadth-first search.

### Arrays
- So why do we need anything beyond arrays? Well, if you simply want to access or update an element in the array, they are very efficient for the job and it takes constant time to do so. But imagine if you wanted to insert an element in the beginning of the array. It would take O(n) operations to do so, since we have to shift all the elements to the end by one.
Video
- [Arrays (video)](https://www.coursera.org/learn/data-structures/lecture/OsBSF/arrays)


### List
- If we use a list however, which is a series of items (call them nodes) connected by links, all we have to do is make the new element point to the first element of the array. If we want to insert elsewhere, it's similar, we just need to get the preceeding element and have its link point to the new element, and have the new element point to the one after the original element. And it follows that this takes O(1), whereas retrieving the Nth element takes O(N)

Video: 
- [Singly Linked Lists (video)](https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists)
- [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/rjBs9/core-linked-lists-vs-arrays)
- [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays)
- [why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)

### Queue
- We use queues in our daily lives everywhere, in front of lines in our rollercoaster rides, medical systems, banking, finance, everywhere. And they come in all sorts of forms. The most basic takes only time in consideration, namely the first elements will be the first to be attended.
    - But there are also variations, such as priority queues, which take into consideration a series of factors. For example, in medical organ donation, we might consider the risk of death and urgency for the patient to receive a transplant (very complex system with some simplifications here, and in fact could be optimized with software). 
    - The same applies to computer science, where these queues are useful for designing these systems as well as supporting algorithms such as breadth-first search, and priority queues for A* search.
    
    Breadth-first search basically starts with an element and considers all the elements connected to it, before going to the next level. Whereas A*
    search looks into factors such as the cost of moving to the node and the estimated distance reduction to the goal.
    Video:
    - [ ] [Queue (video)](https://www.coursera.org/learn/data-structures/lecture/EShpq/queue)
    - [ ] [Priority Queues (video)](https://www.lynda.com/Developer-Programming-Foundations-tutorials/Priority-queues-deques/149042/177123-4.html)
    - [MIT (video)](https://www.youtube.com/watch?v=s-CYnVz-uh4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=13)
    - [ ] [A* Pathfinding Tutorial (video)](https://www.youtube.com/watch?v=KNXfSOx4eEE)
    
### Hash Tables
 - Hash Tables are beautiful things and extremely useful in a very large and diverse domain of applications. If you have seen them before, and you are under the impression that they are complicated, just forget anything you know about them. They are quite straightforward:
      - Starting with the easy part, "table", we have a data structure that represents a table mapping a value generally represented as a string, to another value of any type. That's what a table is, and if hash tables were just the running time to find a value in the table would be O(n), and it wouldn't be very useful.
       -> That's the power of "hashing", where we take the key which is the value that maps to another, and process it with a function (for example adding the ascii characters modulo the number of entries in the table, which works but we will later see can be optimized substantially), and finds where in the table it belongs
       - Know how hash tables are implemented, but more importantly know how to use them to build new systems.
       
       
       Videos:
        - [ ] [Core Hash Tables (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/m7UuP/core-hash-tables)
        - [ ] [Data Structures (video)](https://www.coursera.org/learn/data-structures/home/week/3)
        - [ ] [Phone Book Problem (video)](https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-problem
       
### Trees
 - Trees are again just another form of organizing data in a way that provides benefits for certain applications. It is called a Tree because it has branches, like real life trees do. Most think of it as an upside down tree.  For example:
    3
   / \
  5  1
 / \
0   2
    - Trees come in all sorts and forms, depending on the application we are desigining them for there are advantages in choosing one type from another, and we will look at each of those indidually as well as examine the trade-offs in future sessions. But it is easy to understand the great advantage of trees at all by talking about binary search trees (BSTs). Their one rule is that:
    - For every node, its left child contains a value smaller than or equal to itself, and its right child is larger. E.g:
    4
   / \
  2   5
 / \
1   3

We can see that finding an element here only takes O(log(n)) time for a generally balanced tree. We will also looking at the problem of unbalenced trees later (where most the height of one of the children is much larger than the other, and worst case run time is O(n), to solve this we have balancing algorithms)


Videos:
- [ ] [Series: Core Trees (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/ovovP/core-trees)
- [ ] [Series: Trees (video)](https://www.coursera.org/learn/data-structures/lecture/95qda/trees)
- [ ] [Series (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/p82sw/core-introduction-to-binary-search-trees)
- [ ] [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
- [ ] [MIT (video)](https://www.youtube.com/watch?v=9Jry5-82I68)    
Overview video: 
- [ ] [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
    
    
### Graphs
   - Graphs, just like trees, are another way to represent data. A tree is actually just a specific form of a graph. Graphs are very important when we want to model items that have a relationship with one another, like trees. Every tree is a graph, but not every graph is a tree because some graphs can contain cycles (loops) and trees cannot. 
 
 Videos: 
 - [ ] [CSE373 2012 - Lecture 11 - Graph Data Structures (video)](https://www.youtube.com/watch?v=OiXxhDrFruw&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=11)
 - [ ] [CSE373 2012 - Lecture 12 - Breadth-First Search (video)](https://www.youtube.com/watch?v=g5vF8jscteo&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=12)
 

## Week 3



### Session 1 - Recursion 


Concept:
- https://www.coursera.org/learn/principles-of-computing-2/lecture/CVJBS/the-importance-of-recursion
- https://www.coursera.org/learn/principles-of-computing-2/lecture/ccrwD/recursion
- https://www.coursera.org/learn/principles-of-computing-2/lecture/pubjS/visualizing-recursion
- https://www.coursera.org/learn/principles-of-computing-2/lecture/ylfQH/recurrences



Example Application:

Binary search
https://www.coursera.org/learn/object-oriented-java/lecture/Zmla4/core-binary-search

Counting inversions
- https://www.coursera.org/learn/algorithms-divide-conquer/lecture/GFmmJ/o-n-log-n-algorithm-for-counting-inversions-i
- https://www.coursera.org/learn/algorithms-divide-conquer/lecture/IUiUk/o-n-log-n-algorithm-for-counting-inversions-ii
   
Quicksort
- https://www.coursera.org/learn/algorithms-divide-conquer/lecture/Zt0Ti/quicksort-overview
- https://www.coursera.org/learn/algorithms-divide-conquer/lecture/xUd8B/partitioning-around-a-pivot
- https://www.coursera.org/learn/algorithms-divide-conquer/lecture/QCLVL/choosing-a-good-pivot

More:
- https://www.coursera.org/learn/algorithms-divide-conquer/lecture/KMyzr/correctness-of-quicksort-review-optional


### Session 2 - Basic Algorithms examples

Talk points: Here we will see the importance of algorithms in designing efficient applications, and how we can benefit from using the advantages of efficient data structures and algorithms together to create very powerful systems.

### Applications of Sorting

  One of the most basic algorithms is sorting. Everyone is familiar with sorting. In real life we might have a bookshelf sorted by alphabetical order, which is useful for retrieving and finding the correct book at a later time.
  
There are many problems where sorting first will help to solve the problem more efficiently.

- Use these slides
  http://www3.cs.stonybrook.edu/~algorith/video-lectures/1997/lecture8.pdf
  



### Applications of Hash tables 


- Use these slides
http://www3.cs.stonybrook.edu/~algorith/video-lectures/2007/lecture6.pdf

   

Home Videos: 
- https://www.coursera.org/learn/algorithms-on-strings
- https://www.youtube.com/watch?v=CLHDr1tqaFQ
- [ ] [CS 61B Lecture 29: Sorting I (video)](https://www.youtube.com/watch?v=EiUvYS2DT6I&list=PL4BBB74C7D2A1049C&index=29)
- [ ] [CS 61B Lecture 30: Sorting II (video)](https://www.youtube.com/watch?v=2hTY3t80Qsk&list=PL4BBB74C7D2A1049C&index=30)
- [ ] [CS 61B Lecture 32: Sorting III (video)](https://www.youtube.com/watch?v=Y6LOLpxg6Dc&index=32&list=PL4BBB74C7D2A1049C)
- [ ] [CS 61B Lecture 33: Sorting V (video)](https://www.youtube.com/watch?v=qNMQ4ly43p4&index=33&list=PL4BBB74C7D2A1049C)
- [ ] [1. Quicksort](https://www.youtube.com/watch?v=5M5A7qPWk84&index=1&list=PLe-ggMe31CTeE3x2-nF1-toca1QpuXwE1)
- [ ] [2. Selection](https://www.youtube.com/watch?v=CgVYfSyct_M&index=2&list=PLe-ggMe31CTeE3x2-nF1-toca1QpuXwE1)
- [ ] [3. Duplicate Keys](https://www.youtube.com/watch?v=WBFzOYJ5ybM&index=3&list=PLe-ggMe31CTeE3x2-nF1-toca1QpuXwE1)
- [ ] [4. System Sorts](https://www.youtube.com/watch?v=rejpZ2htBjE&index=4&list=PLe-ggMe31CTeE3x2-nF1-toca1QpuXwE1) 
- [ ] [Analyzing Bubble Sort (video)](https://www.youtube.com/watch?v=ni_zk257Nqo&index=7&list=PL89B61F78B552C1AB)
- [ ] [Insertion Sort (video)](https://www.youtube.com/watch?v=c4BRHC7kTaQ&index=2&list=PL89B61F78B552C1AB)
- [ ] [Selection Sort (video)](https://www.youtube.com/watch?v=6nDMgr0-Yyo&index=8&list=PL89B61F78B552C1AB)

# Week 4 


### Session 1 - Machine Learning - Supervised Learning
Intro:
- https://www.coursera.org/learn/machine-learning/lecture/RKFpn/welcome
 - https://www.coursera.org/learn/machine-learning/lecture/1VkCb/supervised-learning
Regression:
 - https://www.coursera.org/learn/machine-learning/lecture/db3jS/model-representation
 - https://www.coursera.org/learn/machine-learning/lecture/rkTp3/cost-function
 - https://www.coursera.org/learn/machine-learning/lecture/N09c6/cost-function-intuition-i
 
Classification:
- https://www.coursera.org/learn/machine-learning/lecture/wlPeP/classification
 - https://www.coursera.org/learn/machine-learning/lecture/RJXfB/hypothesis-representation
 - https://www.coursera.org/learn/machine-learning/lecture/OAOhO/non-linear-hypotheses
 - https://www.coursera.org/learn/machine-learning/lecture/4h5X4/prioritizing-what-to-work-on

### Session 2 - Machine Learning - Unsupervised Learning
Intro:
 - https://www.coursera.org/learn/machine-learning/lecture/olRZo/unsupervised-learning
 - https://www.coursera.org/learn/machine-learning/lecture/czmip/unsupervised-learning-introduction

K-Means:
 - https://www.coursera.org/learn/machine-learning/lecture/93VPG/k-means-algorithm
 - https://www.coursera.org/learn/machine-learning/lecture/G6QWt/optimization-objective
 
Applications:
 - https://www.coursera.org/learn/machine-learning/lecture/0EJ6A/motivation-i-data-compression
 - https://www.coursera.org/learn/machine-learning/lecture/t6pYD/motivation-ii-visualization
 - https://www.coursera.org/learn/machine-learning/lecture/Rhg6r/problem-formulation
 - https://www.coursera.org/learn/machine-learning/lecture/uG59z/content-based-recommendations
 - https://www.coursera.org/learn/machine-learning/lecture/2WoBV/collaborative-filtering
 

More:
- [Neural Networks for Machine Learning](https://www.coursera.org/learn/neural-networks)
- [How Google Is Remaking Itself As A Machine Learning First Company](https://backchannel.com/how-google-is-remaking-itself-as-a-machine-learning-first-company-ada63defcb70)
- [Large-Scale Deep Learning for Intelligent Computer Systems (video)](https://www.youtube.com/watch?v=QSaZGT4-6EY)
- Deep Learning and Understandability versus Software Engineering and Verification by Peter Norvig](https://www.youtube.com/watch?v=X769cyzBNVw)
- [Google's Cloud Machine learning tools (video)](https://www.youtube.com/watch?v=Ja2hxBAwG_0)
- [Google Developers' Machine Learning Recipes (Scikit Learn & Tensorflow) (video)](https://www.youtube.com/playlist?list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal)
- [Tensorflow (video)](https://www.youtube.com/watch?v=oZikw5k_2FM)
- [Tensorflow Tutorials](https://www.tensorflow.org/versions/r0.11/tutorials/index.html)
- [Practical Guide to implementing Neural Networks in Python (using Theano)](http://www.analyticsvidhya.com/blog/2016/04/neural-networks-python-theano/)

 


 
# Week 5


## Session 1 - Trees and Tries



- ### Trees - Notes & Background
    - [ ] [Series: Core Trees (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/ovovP/core-trees)
    - [ ] [Series: Trees (video)](https://www.coursera.org/learn/data-structures/lecture/95qda/trees)
    - basic tree construction
    - traversal
    - manipulation algorithms

- ### Binary search trees: BSTs
    - [ ] [Binary Search Tree Review (video)](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
    - [ ] [Series (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/p82sw/core-introduction-to-binary-search-trees)
        - starts with symbol table and goes through BST applications
    - [ ] [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
    - [ ] [MIT (video)](https://www.youtube.com/watch?v=9Jry5-82I68)
    

- ### Tries
    - Note there are different kinds of tries. Some have prefixes, some don't, and some use string instead of bits
        to track the path.
    - I read through code, but will not implement.
    - [ ] [Sedgewick - Tries (3 videos)](https://www.youtube.com/playlist?list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ)
        - [ ] [1. R Way Tries](https://www.youtube.com/watch?v=buq2bn8x3Vo&index=3&list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ)
        - [ ] [2. Ternary Search Tries](https://www.youtube.com/watch?v=LelV-kkYMIg&index=2&list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ)
        - [ ] [3. Character Based Operations](https://www.youtube.com/watch?v=00YaFPcC65g&list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ&index=1)
    - [ ] [Notes on Data Structures and Programming Techniques](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Tries)
    - [ ] Short course videos:
        - [ ] [Introduction To Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/08Xyf/core-introduction-to-tries)
        - [ ] [Performance Of Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/PvlZW/core-performance-of-tries)
        - [ ] [Implementing A Trie (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/DFvd3/core-implementing-a-trie)
    - [ ] [The Trie: A Neglected Data Structure](https://www.toptal.com/java/the-trie-a-neglected-data-structure)
    - [ ] [TopCoder - Using Tries](https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/)
    - [ ] [Stanford Lecture (real world use case) (video)](https://www.youtube.com/watch?v=TJ8SkcUSdbU)


## Session 2 - Heaps and Balanced Trees
https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/WHOPA/



- ### Heap / Priority Queue / Binary Heap
    - visualized as a tree, but is usually linear in storage (array, linked list)
    - [ ] [Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))
    - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/iIzo8/heaps-operations-and-applications
    - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/KKqlm/heaps-implementation-details-advanced-optional
    - [ ] [Naive Implementations (video)](https://www.coursera.org/learn/data-structures/lecture/z3l9N/naive-implementations)
    - [ ] [Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees)
    - [ ] [Basic Operations (video)](https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations)
    - [ ] [Complete Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees)
    - [ ] [Pseudocode (video)](https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode)
    - [ ] [Heap Sort - jumps to start (video)](https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291)
    - [ ] [Heap Sort (video)](https://www.coursera.org/learn/data-structures/lecture/hSzMO/heap-sort)
    - [ ] [Building a heap (video)](https://www.coursera.org/learn/data-structures/lecture/dwrOS/building-a-heap)
    - [ ] [CS 61B Lecture 24: Priority Queues (video)](https://www.youtube.com/watch?v=yIUFT6AKBGE&index=24&list=PL4BBB74C7D2A1049C)
    - [ ] [Linear Time BuildHeap (max-heap)](https://www.youtube.com/watch?v=MiyLo8adrWw)
    - [ ] Implement a max-heap:
        - [ ] insert
        - [ ] sift_up - needed for insert
        - [ ] get_max - returns the max item, without removing it
        - [ ] get_size() - return number of elements stored
        - [ ] is_empty() - returns true if heap contains no elements
        - [ ] extract_max - returns the max item, removing it
        - [ ] sift_down - needed for extract_max
        - [ ] remove(i) - removes item at index x
        - [ ] heapify - create a heap from an array of elements, needed for heap_sort
        - [ ] heap_sort() - take an unsorted array and turn it into a sorted array in-place using a max heap
            - note: using a min heap instead would save operations, but double the space needed (cannot do in-place).
            
            

- ### Balanced search trees
    - Know least one type of balanced binary tree (and know how it's implemented):
    - "Among balanced search trees, AVL and 2/3 trees are now passé, and red-black trees seem to be more popular.
        A particularly interesting self-organizing data structure is the splay tree, which uses rotations
        to move any accessed key to the root." - Skiena
    - Of these, I chose to implement a splay tree. From what I've read, you won't implement a
        balanced search tree in your interview. But I wanted exposure to coding one up
        and let's face it, splay trees are the bee's knees. I did read a lot of red-black tree code.
        - splay tree: insert, search, delete functions
        If you end up implementing red/black tree try just these:
        - search and insertion functions, skipping delete
    - I want to learn more about B-Tree since it's used so widely with very large data sets.
    - [ ] [Self-balancing binary search tree](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)

    - [ ] **AVL trees**
        - In practice:
            From what I can tell, these aren't used much in practice, but I could see where they would be:
            The AVL tree is another structure supporting O(log n) search, insertion, and removal. It is more rigidly
            balanced than red–black trees, leading to slower insertion and removal but faster retrieval. This makes it
            attractive for data structures that may be built once and loaded without reconstruction, such as language
            dictionaries (or program dictionaries, such as the opcodes of an assembler or interpreter).
        - [ ] [MIT AVL Trees / AVL Sort (video)](https://www.youtube.com/watch?v=FNeL18KsWPc&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=6)
        - [ ] [AVL Trees (video)](https://www.coursera.org/learn/data-structures/lecture/Qq5E0/avl-trees)
        - [ ] [AVL Tree Implementation (video)](https://www.coursera.org/learn/data-structures/lecture/PKEBC/avl-tree-implementation)
        - [ ] [Split And Merge](https://www.coursera.org/learn/data-structures/lecture/22BgE/split-and-merge)
        
        
 - [ ] **2-3 search trees**
        - In practice:
            2-3 trees have faster inserts at the expense of slower searches (since height is more compared to AVL trees).
        - You would use 2-3 tree very rarely because its implementation involves different types of nodes. Instead, people use Red Black trees.
        - [ ] [23-Tree Intuition and Definition (video)](https://www.youtube.com/watch?v=C3SsdUqasD4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=2)
        - [ ] [Binary View of 23-Tree](https://www.youtube.com/watch?v=iYvBtGKsqSg&index=3&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [ ] [2-3 Trees (student recitation) (video)](https://www.youtube.com/watch?v=TOb1tuEZ2X4&index=5&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)

 - [ ] **Red/black trees**
        - In practice:
            Red–black trees offer worst-case guarantees for insertion time, deletion time, and search time.
            Not only does this make them valuable in time-sensitive applications such as real-time applications,
            but it makes them valuable building blocks in other data structures which provide worst-case guarantees;
            for example, many data structures used in computational geometry can be based on red–black trees, and
            the Completely Fair Scheduler used in current Linux kernels uses red–black trees. In the version 8 of Java,
            the Collection HashMap has been modified such that instead of using a LinkedList to store identical elements with poor
            hashcodes, a Red-Black tree is used.
        - [ ] [Aduni - Algorithms - Lecture 4 (link jumps to starting point) (video)](https://youtu.be/1W3x0f_RmUo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3871)
        - [ ] [Aduni - Algorithms - Lecture 5 (video)](https://www.youtube.com/watch?v=hm2GHwyKF1o&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=5)
        - [ ] [Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
        - [ ] [An Introduction To Binary Search And Red Black Tree](https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-binary-search-and-red-black-trees/)
        - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/8acpe/red-black-trees
        - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/JV7KI/rotations-advanced-optional
        - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/jPL2x/insertion-in-a-red-black-tree-advanced

Home:
    - [ ] **Splay trees**
        - In practice:
            Splay trees are typically used in the implementation of caches, memory allocators, routers, garbage collectors,
            data compression, ropes (replacement of string used for long text strings), in Windows NT (in the virtual memory,
            networking, and file system code) etc.
        - [ ] [CS 61B: Splay Trees (video)](https://www.youtube.com/watch?v=Najzh1rYQTo&index=23&list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd
        
        - [ ] MIT Lecture: Splay Trees:
            - Gets very mathy, but watch the last 10 minutes for sure.
            - [Video](https://www.youtube.com/watch?v=QnPl_Y6EqMo)

 
    - [ ] **2-3-4 Trees (aka 2-4 trees)**
        - In practice:
            For every 2-4 tree, there are corresponding red–black trees with data elements in the same order. The insertion and deletion
            operations on 2-4 trees are also equivalent to color-flipping and rotations in red–black trees. This makes 2-4 trees an
            important tool for understanding the logic behind red–black trees, and this is why many introductory algorithm texts introduce
            2-4 trees just before red–black trees, even though **2-4 trees are not often used in practice**.
        - [ ] [CS 61B Lecture 26: Balanced Search Trees (video)](https://www.youtube.com/watch?v=zqrqYXkth6Q&index=26&list=PL4BBB74C7D2A1049C)
        - [ ] [Bottom Up 234-Trees (video)](https://www.youtube.com/watch?v=DQdMYevEyE4&index=4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [ ] [Top Down 234-Trees (video)](https://www.youtube.com/watch?v=2679VQ26Fp4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=5)

    - [ ] **B-Trees**
        - fun fact: it's a mystery, but the B could stand for Boeing, Balanced, or Bayer (co-inventor)
        - In Practice:
            B-Trees are widely used in databases. Most modern filesystems use B-trees (or Variants). In addition to
            its use in databases, the B-tree is also used in filesystems to allow quick random access to an arbitrary
            block in a particular file. The basic problem is turning the file block i address into a disk block
            (or perhaps to a cylinder-head-sector) address.
        - [ ] [B-Tree](https://en.wikipedia.org/wiki/B-tree)
        - [ ] [Introduction to B-Trees (video)](https://www.youtube.com/watch?v=I22wEC1tTGo&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=6)
        - [ ] [B-Tree Definition and Insertion (video)](https://www.youtube.com/watch?v=s3bCdZGrgpA&index=7&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [ ] [B-Tree Deletion (video)](https://www.youtube.com/watch?v=svfnVhJOfMc&index=8&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [ ] [MIT 6.851 - Memory Hierarchy Models (video)](https://www.youtube.com/watch?v=V3omVLzI0WE&index=7&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf)
                - covers cache-oblivious B-Trees, very interesting data structures
                - the first 37 minutes are very technical, may be skipped (B is block size, cache line size)


- ### N-ary (K-ary, M-ary) trees
    - note: the N or K is the branching factor (max branches)
        - binary trees are a 2-ary tree, with branching factor = 2
        - 2-3 trees are 3-ary
    - [ ] [K-Ary Tree](https://en.wikipedia.org/wiki/K-ary_tree)
 

     - C/C++:
             - [ ] [Binary search tree - Implementation in C/C++ (video)](https://www.youtube.com/watch?v=COZK7NATh4k&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=28)
             - [ ] [BST implementation - memory allocation in stack and heap (video)](https://www.youtube.com/watch?v=hWokyBoo0aI&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=29)
             - [ ] [Find min and max element in a binary search tree (video)](https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
             - [ ] [Find height of a binary tree (video)](https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31)
             - [ ] [Binary tree traversal - breadth-first and depth-first strategies (video)](https://www.youtube.com/watch?v=9RHO6jU--GU&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=32)
             - [ ] [Binary tree: Level Order Traversal (video)](https://www.youtube.com/watch?v=86g8jAQug04&index=33&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
             - [ ] [Binary tree traversal: Preorder, Inorder, Postorder (video)](https://www.youtube.com/watch?v=gm8DUJJhmY4&index=34&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
             - [ ] [Check if a binary tree is binary search tree or not (video)](https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
             - [ ] [Delete a node from Binary Search Tree (video)](https://www.youtube.com/watch?v=gcULXE7ViZw&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=36)
             - [ ] [Inorder Successor in a binary search tree (video)](https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
             
             - [ ] [MIT, Advanced Data Structures, Strings](https://www.youtube.com/watch?v=NinWEPPrkDQ&index=16&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf)
             
             - [MIT (video)](https://www.youtube.com/watch?v=s-CYnVz-uh4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=13)
             - [MIT (video)](https://www.youtube.com/watch?v=AfSk24UTFS8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=14)

              - [ ] [Tree Height Remark (video)](https://www.coursera.org/learn/data-structures/supplement/S5xxz/tree-height-remark)
              - [ ] [MIT: Heaps and Heap Sort (video)](https://www.youtube.com/watch?v=B7hVxCmfPtM&index=4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)


- ### Treap
    - Combination of a binary search tree and a heap
    - [ ] [Treap](https://en.wikipedia.org/wiki/Treap)
    - [ ] [Data Structures: Treaps explained (video)](https://www.youtube.com/watch?v=6podLUYinH8)
    - [ ] [Applications in set operations](https://www.cs.cmu.edu/~scandal/papers/treaps-spaa98.pdf)
        

# Week 6
Todo: 1) organize this section, clean up unecessary stuff, and maybe add more stuff 
      2) write my talk


## Session 1 - Graph Properties and Graph Search


- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/NX0BI/graph-search-overview
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/JZRXz/breadth-first-search-bfs-the-basics
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/ZAaJA/bfs-and-shortest-paths
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/BTVWn/bfs-and-undirected-connectivity
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/pKr0Y/depth-first-search-dfs-the-basics
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/yeKm7/topological-sort
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/rng2S/computing-strong-components-the-algorithm
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/f11at/structure-of-the-web-optional


Dijkstra Graph Search Algorihtm
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/rxrPa/dijkstras-shortest-path-algorithm
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/Jfvmn/dijkstras-algorithm-examples
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/VCHYw/correctness-of-dijkstras-algorithm
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/Pbpp9/dijkstras-algorithm-implementation-and-running-time


### Session 2 - Solving Problems Using Graphs

todo - get skiena content slides, and here https://www.coursera.org/learn/algorithms-on-graphs

Home: 


Graphs are a huge subject in computer science, there are many applications in which they are powerful. From modeling the relationships between people in social networks, to representing connections of genomic data in trying to understand patterns of diseases, they are very useful. There are many ways to represent them and we will understand them below: 


- [ ] **Union-Find**
    - [ ] [Overview](https://www.coursera.org/learn/data-structures/lecture/JssSY/overview)
    - [ ] [Naive Implementation](https://www.coursera.org/learn/data-structures/lecture/EM5D0/naive-implementations)
    - [ ] [Trees](https://www.coursera.org/learn/data-structures/lecture/Mxu0w/trees)
    - [ ] [Union By Rank](https://www.coursera.org/learn/data-structures/lecture/qb4c2/union-by-rank)
    - [ ] [Path Compression](https://www.coursera.org/learn/data-structures/lecture/Q9CVI/path-compression)
    - [ ] [Analysis Options](https://www.coursera.org/learn/data-structures/lecture/GQQLN/analysis-optional)
    - [ ] [Sedgewick Algorithms - Union-Find (6 videos)](https://www.youtube.com/watch?v=8mYfZeHtdNc&list=PLe-ggMe31CTexoNYnMhbHaWhQ0dvcy43t)


- [ ] **Advanced Graph Processing** (videos)
    - [ ] [Synchronous Distributed Algorithms: Symmetry-Breaking. Shortest-Paths Spanning Trees](https://www.youtube.com/watch?v=mUBmcbbJNf4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=27)
    - [ ] [Asynchronous Distributed Algorithms: Shortest-Paths Spanning Trees](https://www.youtube.com/watch?v=kQ-UQAzcnzA&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=28)



- use resources from here https://www.coursera.org/learn/algorithms-on-graphs (edit necessary)
https://www.coursera.org/learn/algorithms-graphs-data-structures
 



# Week 7

### Session 1 - Dynamic Programming 


     Todo: 1) organize this section, clean up unecessary stuff, and maybe add more stuff 
           2) write my talk


Todo: 1) organize this section, clean up unecessary stuff, and maybe add more stuff  
      2) write my talk

- https://www.coursera.org/learn/algorithms-greedy/lecture/LIgLJ/the-knapsack-problem
- https://www.coursera.org/learn/algorithms-greedy/lecture/0n68L/a-dynamic-programming-algorithm
- https://www.coursera.org/learn/algorithms-greedy/lecture/LADQc/example-review-optional
     
- https://www.coursera.org/learn/algorithms-greedy/lecture/QJkyp/optimal-substructure
- https://www.coursera.org/learn/algorithms-greedy/lecture/tNmae/a-dynamic-programming-algorithm 
     
- https://www.coursera.org/learn/algorithms-greedy/lecture/GKCeN/problem-definition
- https://www.coursera.org/learn/algorithms-greedy/lecture/rUDLu/optimal-substructure
- https://www.coursera.org/learn/algorithms-greedy/lecture/0qjbs/proof-of-optimal-substructure
- https://www.coursera.org/learn/algorithms-greedy/lecture/3wrTN/a-dynamic-programming-algorithm-i
- https://www.coursera.org/learn/algorithms-greedy/lecture/5ERYG/a-dynamic-programming-algorithm-ii

- https://www.coursera.org/learn/algorithms-greedy/lecture/WENc1/introduction-weighted-independent-sets-in-path-graphs
- https://www.coursera.org/learn/algorithms-greedy/lecture/t9XAF/wis-in-path-graphs-optimal-substructure
- https://www.coursera.org/learn/algorithms-greedy/lecture/w040v/wis-in-path-graphs-a-linear-time-algorithm
- https://www.coursera.org/learn/algorithms-greedy/lecture/TZgJM/wis-in-path-graphs-a-reconstruction-algorithm
- https://www.coursera.org/learn/algorithms-greedy/lecture/VEc7L/principles-of-dynamic-programming

More: 
  Dynamic programming is quite simple. It takes advantages of two things seen previously: data structures and recursion.
    - [ ] Videos:
- [ ] List of individual DP problems (each is short): [Dynamic Programming (video)](https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr)
- [ ] [The RNA secondary structure problem (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/80RrW/the-rna-secondary-structure-problem)
- [ ] [A dynamic programming algorithm (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/PSonq/a-dynamic-programming-algorithm)
- [ ] [Illustrating the DP algorithm (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/oUEK2/illustrating-the-dp-algorithm)
- [ ] [Running time of the DP algorithm (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/nfK2r/running-time-of-the-dp-algorithm)
- [ ] [DP vs. recursive implementation (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/M999a/dp-vs-recursive-implementation)
- [ ] [Global pairwise sequence alignment (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/UZ7o6/global-pairwise-sequence-alignment)
- [ ] [Local pairwise sequence alignment (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/WnNau/local-pairwise-sequence-alignment)


        
- [ ] **More Dynamic Programming** (videos)
    - [ ] [6.006: Dynamic Programming I: Fibonacci, Shortest Paths](https://www.youtube.com/watch?v=OQ5jsbhAv_M&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=19)
    - [ ] [6.006: Dynamic Programming II: Text Justification, Blackjack](https://www.youtube.com/watch?v=ENyox7kNKeY&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=20)Du
    - [ ] [6.006: DP III: Parenthesization, Edit Distance, Knapsack](https://www.youtube.com/watch?v=ocZMDMZwhCY&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=21)
    - [ ] [6.006: DP IV: Guitar Fingering, Tetris, Super Mario Bros.](https://www.youtube.com/watch?v=tp4_UXaVyx8&index=22&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [ ] [6.046: Dynamic Programming & Advanced DP](https://www.youtube.com/watch?v=Tw1k46ywN6E&index=14&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [ ] [6.046: Dynamic Programming: All-Pairs Shortest Paths](https://www.youtube.com/watch?v=NzgFUwOaoIw&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=15)
    - [ ] [6.046: Dynamic Programming (student recitation)](https://www.youtube.com/watch?v=krZI60lKPek&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=12)


     
## Session 2 - Solving Problems with Dynamic Programming 

See from skiena's slides, and within the extra content here in the guide and: 

https://www.coursera.org/learn/dna-sequencing/lecture/ZDDOH/practical-implementing-dynamic-programming-for-edit-distance
https://www.coursera.org/learn/advanced-algorithms-and-complexity/lecture/71PHI/tsp-dynamic-programming
https://www.coursera.org/learn/algorithms-npcomplete/lecture/gXaGS/a-dynamic-programming-heuristic-for-knapsack
https://www.coursera.org/learn/algorithms-npcomplete/lecture/qtdIZ/knapsack-via-dynamic-programming-revisited
https://www.coursera.org/learn/algorithms-npcomplete/lecture/ApF82/ananysis-of-dynamic-programming-heuristic
https://www.coursera.org/learn/comparing-genomes/lecture/TDKlW/dynamic-programming-and-backtracking-pointers
https://www.coursera.org/learn/algorithms-greedy


 

# Week 8
 
## Session 1 - Bitwise operations, Discrete Mathematics, and NP Completeness and Computability

Todo: 1) organize this section, clean up unecessary stuff, and maybe add more stuff 
      2) write my talk

### Combinatorics (n choose k) & Probability
- [ ] [Math Skills: How to find Factorial, Permutation and Combination (Choose) (video)](https://www.youtube.com/watch?v=8RRo6Ti9d0U)
- [ ] [Make School: Probability (video)](https://www.youtube.com/watch?v=sZkAAk9Wwa4)
- [ ] [Make School: More Probability and Markov Chains (video)](https://www.youtube.com/watch?v=dNaJg-mLobQ)
- [ ] [Basic Theoretical Probability](https://www.khanacademy.org/math/probability/probability-and-combinatorics-topic)  
- [ ] [Probability Explained (video)](https://www.youtube.com/watch?v=uzkc-qNVoOk&list=PLC58778F28211FA19)
- [ ] MIT **Probability** (mathy, and go slowly, which is good for mathy things) (videos):
- [ ] [MIT 6.042J - Probability Introduction](https://www.youtube.com/watch?v=SmFwFdESMHI&index=18&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Conditional Probability](https://www.youtube.com/watch?v=E6FbvM-FGZ8&index=19&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Independence](https://www.youtube.com/watch?v=l1BCv3qqW4A&index=20&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Random Variables](https://www.youtube.com/watch?v=MOfhhFaQdjw&list=PLB7540DEDD482705B&index=21)
- [ ] [MIT 6.042J - Expectation I](https://www.youtube.com/watch?v=gGlMSe7uEkA&index=22&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Expectation II](https://www.youtube.com/watch?v=oI9fMUqgfxY&index=23&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Large Deviations](https://www.youtube.com/watch?v=q4mwO2qS2z4&index=24&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Random Walks](https://www.youtube.com/watch?v=56iFMY8QW2k&list=PLB7540DEDD482705B&index=25)
    
### Shortest Paths and NP, NP-Complete, and Approximation Algorithms

- https://www.coursera.org/learn/algorithms-npcomplete/lecture/8HT5O/polynomial-time-solvable-problems
- https://www.coursera.org/learn/algorithms-npcomplete/lecture/o1CGE/reductions-and-completeness
- https://www.coursera.org/learn/algorithms-npcomplete/lecture/vZ9Bc/definition-and-interpretation-of-np-completeness-i
- https://www.coursera.org/learn/algorithms-npcomplete/lecture/3JqiX/definition-and-interpretation-of-np-completeness-ii
- https://www.coursera.org/learn/algorithms-npcomplete/lecture/VZY2Z/the-p-vs-np-question
- https://www.coursera.org/learn/algorithms-npcomplete/lecture/jugfP/algorithmic-approaches-to-np-complete-problems
      
- Know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem,
        and be able to recognize them when an interviewer asks you them in disguise.
- Know what NP-complete means.
- [ ] [Computational Complexity (video)](https://www.youtube.com/watch?v=moPtwq_cVH8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=23)
- [ ] Simonson:
- [ ] [Greedy Algs. II & Intro to NP Completeness (video)](https://youtu.be/qcGnJ47Smlo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=2939)
- [ ] [NP Completeness II & Reductions (video)](https://www.youtube.com/watch?v=e0tGC6ZQdQE&index=16&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
- [ ] [NP Completeness III (Video)](https://www.youtube.com/watch?v=fCX1BGT3wjE&index=17&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
- [ ] [NP Completeness IV (video)](https://www.youtube.com/watch?v=NKLDp3Rch3M&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=18)
- [ ] Skiena:
- [ ] [CSE373 2012 - Lecture 23 - Introduction to NP-Completeness (video)](https://youtu.be/KiK5TVgXbFg?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=1508)
- [ ] [CSE373 2012 - Lecture 24 - NP-Completeness Proofs (video)](https://www.youtube.com/watch?v=27Al52X3hd4&index=24&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
- [ ] [CSE373 2012 - Lecture 25 - NP-Completeness Challenge (video)](https://www.youtube.com/watch?v=xCPH4gwIIXM&index=25&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
- [ ] [Complexity: P, NP, NP-completeness, Reductions (video)](https://www.youtube.com/watch?v=eHZifpgyH_4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=22)
- [ ] [Complexity: Approximation Algorithms (video)](https://www.youtube.com/watch?v=MEz1J9wY2iM&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=24)
- [ ] [Complexity: Fixed-Parameter Algorithms (video)](https://www.youtube.com/watch?v=4q-jmGrmxKs&index=25&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
- Peter Norvik discusses near-optimal solutions to traveling salesman problem:
- [Jupyter Notebook](http://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb)
- Pages 1048 - 1140 in CLRS if you have it.


More: 


- ### Bloom Filter
    - Given a Bloom filter with m bits and k hashing functions, both insertion and membership testing are O(k)
    - [Bloom Filters](https://www.youtube.com/watch?v=-SuTGoFYjZs)
    - [Bloom Filters | Mining of Massive Datasets | Stanford University](https://www.youtube.com/watch?v=qBTdukbzc78)
    - [Tutorial](http://billmill.org/bloomfilter-tutorial/)
    - [How To Write A Bloom Filter App](http://blog.michaelschmatz.com/2016/04/11/how-to-write-a-bloom-filter-cpp/)


- ### Cryptography
    - also see videos below
    - make sure to watch information theory videos first
    - [ ] [Khan Academy Series](https://www.khanacademy.org/computing/computer-science/cryptography)
    - [ ] [Cryptography: Hash Functions](https://www.youtube.com/watch?v=KqqOXndnvic&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=30)
    - [ ] [Cryptography: Encryption](https://www.youtube.com/watch?v=9TNI2wHmaeI&index=31&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
- ### Linear Programming (videos)
    - [ ] [Linear Programming](https://www.youtube.com/watch?v=M4K6HYLHREQ)
    - [ ] [Finding minimum cost](https://www.youtube.com/watch?v=2ACJ9ewUC6U)
    - [ ] [Finding maximum value](https://www.youtube.com/watch?v=8AA_81xI3ik)
    - [ ] [Solve Linear Equations with Python - Simplex Algorithm](https://www.youtube.com/watch?v=44pAWI7v5Zk)
- ### Math for Fast Processing
    - [ ] [Integer Arithmetic, Karatsuba Multiplication (video)](https://www.youtube.com/watch?v=eCaXlAaN2uE&index=11&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [ ] [The Chinese Remainder Theorem (used in cryptography) (video)](https://www.youtube.com/watch?v=ru7mWZJlRQg)
    

  
## Session 2 - Caches, Processes and Threads, and other topics (edit)
 Todo: 1) organize this section, clean up unecessary stuff, and maybe add more stuff 
      2) write my talk
 
 
  ### Bitwise operations
 
 [Bit Manipulation (video)](https://www.youtube.com/watch?v=7jkIUgLC29I)
 [C Programming Tutorial 2-10: Bitwise Operators (video)](https://www.youtube.com/watch?v=d0AwjSpNXR0)
 [Binary: Plusses & Minuses (Why We Use Two's Complement) (video)](https://www.youtube.com/watch?v=lKTsv6iVxV4)
 [4 ways to count bits in a byte (video)](https://youtu.be/Hzuzo9NJrlc)
 [Count Bits](https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan)
 
 - ### Compilers
    - [ ] [How a Compiler Works in ~1 minute (video)](https://www.youtube.com/watch?v=IhC7sdYe-Jg)
    - [ ] [Harvard CS50 - Compilers (video)](https://www.youtube.com/watch?v=CSZLNYF4Klo)
    - [ ] [C++ (video)](https://www.youtube.com/watch?v=twodd1KFfGk)
    - [ ] [Understanding Compiler Optimization (C++) (video)](https://www.youtube.com/watch?v=FnGCDLhaxKU)

- ### Floating Point Numbers
    - [ ] simple 8-bit: [Representation of Floating Point Numbers - 1 (video - there is an error in calculations - see video description)](https://www.youtube.com/watch?v=ji3SfClm8TU)
    - [ ] 32 bit: [IEEE754 32-bit floating point binary (video)](https://www.youtube.com/watch?v=50ZYcZebIec)

- ### Unicode
    - [ ] [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets]( http://www.joelonsoftware.com/articles/Unicode.html)
    - [ ] [What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text](http://kunststube.net/encoding/)

- ### Endianness
    - [ ] [Big And Little Endian](https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Data/endian.html)
    - [ ] [Big Endian Vs Little Endian (video)](https://www.youtube.com/watch?v=JrNF0KRAlyo)
    - [ ] [Big And Little Endian Inside/Out (video)](https://www.youtube.com/watch?v=oBSuXP-1Tc0)
        - Very technical talk for kernel devs. Don't worry if most is over your head.
        - The first half is enough.


 ### Caches
    - [ ] LRU cache:
        - [ ] [The Magic of LRU Cache (100 Days of Google Dev) (video)](https://www.youtube.com/watch?v=R5ON3iwx78M)
        - [ ] [Implementing LRU (video)](https://www.youtube.com/watch?v=bq6N7Ym81iI)
        - [ ] [LeetCode - 146 LRU Cache (C++) (video)](https://www.youtube.com/watch?v=8-FZRAjR7qU)
    - [ ] CPU cache:
        - [ ] [MIT 6.004 L15: The Memory Hierarchy (video)](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
        - [ ] [MIT 6.004 L16: Cache Issues (video)](https://www.youtube.com/watch?v=ajgC3-pyGlk&index=25&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-)

### Processes and Threads
   - [ ] Computer Science 162 - Operating Systems (25 videos):
        - for processes and threads see videos 1-11
        - [Operating Systems and System Programming (video)](https://www.youtube.com/playlist?list=PL-XXv-cvA_iBDyz-ba4yDskqMDY6A1w_c)
    - [What Is The Difference Between A Process And A Thread?](https://www.quora.com/What-is-the-difference-between-a-process-and-a-thread)
    - Covers:
        - Processes, Threads, Concurrency issues
            - difference between processes and threads
            - processes
            - threads
            - locks
            - mutexes
            - semaphores
            - monitors
            - how they work
            - deadlock
            - livelock
        - CPU activity, interrupts, context switching
        - Modern concurrency constructs with multicore processors
        - Process resource needs (memory: code, static storage, stack, heap, and also file descriptors, i/o)
        - Thread resource needs (shares above (minus stack) with other threads in same process but each has its own pc, stack counter, registers and stack)
        - Forking is really copy on write (read-only) until the new process writes to memory, then it does a full copy.
        - Context switching
            - How context switching is initiated by the operating system and underlying hardware
    - [ ] [threads in C++ (series - 10 videos)](https://www.youtube.com/playlist?list=PL5jc9xFGsL8E12so1wlMS0r0hTQoJL74M)
    - [ ] concurrency in Python (videos):
        - [ ] [Short series on threads](https://www.youtube.com/playlist?list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1)
        - [ ] [Python Threads](https://www.youtube.com/watch?v=Bs7vPNbB9JM)
        - [ ] [Understanding the Python GIL (2010)](https://www.youtube.com/watch?v=Obt-vMVdM8s)
            - [reference](http://www.dabeaz.com/GIL)
        - [ ] [David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon 2015](https://www.youtube.com/watch?v=MCs5OvhV9S4)
        - [ ] [Keynote David Beazley - Topics of Interest (Python Asyncio)](https://www.youtube.com/watch?v=ZzfHjytDceU)
        - [ ] [Mutex in Python](https://www.youtube.com/watch?v=0zaPs8OtyKY)


    Scalability and System Design are very large topics with many topics and resources, since there is a lot to consider
    when designing a software/hardware system that can scale. Expect to spend quite a bit of time on this.

More: 



- ### Computer Security
    - [MIT (23 videos)](https://www.youtube.com/playlist?list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Introduction, Threat Models](https://www.youtube.com/watch?v=GqmQg-cszw4&index=1&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Control Hijacking Attacks](https://www.youtube.com/watch?v=6bwzNg5qQ0o&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=2)
        - [ ] [Buffer Overflow Exploits and Defenses](https://www.youtube.com/watch?v=drQyrzRoRiA&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=3)
        - [ ] [Privilege Separation](https://www.youtube.com/watch?v=6SIJmoE9L9g&index=4&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Capabilities](https://www.youtube.com/watch?v=8VqTSY-11F4&index=5&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Sandboxing Native Code](https://www.youtube.com/watch?v=VEV74hwASeU&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=6)
        - [ ] [Web Security Model](https://www.youtube.com/watch?v=chkFBigodIw&index=7&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Securing Web Applications](https://www.youtube.com/watch?v=EBQIGy1ROLY&index=8&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Symbolic Execution](https://www.youtube.com/watch?v=yRVZPvHYHzw&index=9&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Network Security](https://www.youtube.com/watch?v=SIEVvk3NVuk&index=11&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Network Protocols](https://www.youtube.com/watch?v=QOtA76ga_fY&index=12&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Side-Channel Attacks](https://www.youtube.com/watch?v=PuVMkSEcPiI&index=15&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)

- ### Parallel Programming
    - [ ] [Coursera (Scala)](https://www.coursera.org/learn/parprog1/home/week/1)
    - [ ] [Efficient Python for High Performance Parallel Computing (video)](https://www.youtube.com/watch?v=uY85GkaYzBk)


- ### Networking (videos)
    - [ ] [Khan Academy](https://www.khanacademy.org/computing/computer-science/internet-intro)
    - [ ] [UDP and TCP: Comparison of Transport Protocols](https://www.youtube.com/watch?v=Vdc8TCESIg8)
    - [ ] [TCP/IP and the OSI Model Explained!](https://www.youtube.com/watch?v=e5DEVa9eSN0)
    - [ ] [Packet Transmission across the Internet. Networking & TCP/IP tutorial.](https://www.youtube.com/watch?v=nomyRJehhnM)
    - [ ] [HTTP](https://www.youtube.com/watch?v=WGJrLqtX7As)
    - [ ] [SSL and HTTPS](https://www.youtube.com/watch?v=S2iBR2ZlZf0)
    - [ ] [SSL/TLS](https://www.youtube.com/watch?v=Rp3iZUvXWlM)
    - [ ] [HTTP 2.0](https://www.youtube.com/watch?v=E9FxNzv1Tr8)
    - [ ] [Video Series (21 videos)](https://www.youtube.com/playlist?list=PLEbnTDJUr_IegfoqO4iPnPYQui46QqT0j)
    - [ ] [Subnetting Demystified - Part 5 CIDR Notation](https://www.youtube.com/watch?v=t5xYI0jzOf4)


# Week 9

## Session 1 - Testing and System Design 

Todo: 1) organize this section, clean up unecessary stuff, and maybe add more stuff 
      2) write my talk



  Talk points:
        - how unit testing works
        - what are mock objects
        - what is integration testing
        - what is dependency injection
       
    - [ ] [Agile Software Testing with James Bach (video)](https://www.youtube.com/watch?v=SAhJf36_u5U)
    - [ ] [Open Lecture by James Bach on Software Testing (video)](https://www.youtube.com/watch?v=ILkT_HV9DVU)
    - [ ] [Steve Freeman - Test-Driven Development (that’s not what we meant) (video)](https://vimeo.com/83960706)
        - [slides](http://gotocon.com/dl/goto-berlin-2013/slides/SteveFreeman_TestDrivenDevelopmentThatsNotWhatWeMeant.pdf)
    - [ ] [TDD is dead. Long live testing.](http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html)
    - [ ] [Is TDD dead? (video)](https://www.youtube.com/watch?v=z9quxZsLcfo)
    - [ ] [Video series (152 videos) - not all are needed (video)](https://www.youtube.com/watch?v=nzJapzxH_rE&list=PLAwxTw4SYaPkWVHeC_8aSIbSxE_NXI76g)
    - [ ] [Test-Driven Web Development with Python](http://www.obeythetestinggoat.com/pages/book.html#toc)
    - [ ] Dependency injection:
        - [ ] [video](https://www.youtube.com/watch?v=IKD2-MAkXyQ)
        - [ ] [Tao Of Testing](http://jasonpolites.github.io/tao-of-testing/ch3-1.1.html)
    - [ ] [How to write tests](http://jasonpolites.github.io/tao-of-testing/ch4-1.1.html)


- ### Implement system routines
    - understand what lies beneath the programming APIs you use
    - can you implement them?

- ### String searching & manipulations
    - [ ] [Sedgewick - Suffix Arrays (video)](https://www.youtube.com/watch?v=HKPrVm5FWvg)
    - [ ] [Sedgewick - Substring Search (videos)](https://www.youtube.com/watch?v=2LvvVFCEIv8&list=PLe-ggMe31CTdAdjXB3lIuf2maubzo9t66&index=5)
        - [ ] [1. Introduction to Substring Search](https://www.youtube.com/watch?v=2LvvVFCEIv8&list=PLe-ggMe31CTdAdjXB3lIuf2maubzo9t66&index=5)
        - [ ] [2. Brute-Force Substring Search](https://www.youtube.com/watch?v=CcDXwIGEXYU&list=PLe-ggMe31CTdAdjXB3lIuf2maubzo9t66&index=4)
        - [ ] [3. Knuth-Morris Pratt](https://www.youtube.com/watch?v=n-7n-FDEWzc&index=3&list=PLe-ggMe31CTdAdjXB3lIuf2maubzo9t66)
        - [ ] [4. Boyer-Moore](https://www.youtube.com/watch?v=fI7Ch6pZXfM&list=PLe-ggMe31CTdAdjXB3lIuf2maubzo9t66&index=2)
        - [ ] [5. Rabin-Karp](https://www.youtube.com/watch?v=QzI0p6zDjK4&index=1&list=PLe-ggMe31CTdAdjXB3lIuf2maubzo9t66)
    - [ ] [Search pattern in text (video)](https://www.coursera.org/learn/data-structures/lecture/tAfHI/search-pattern-in-text)
    
    If you need more detail on this subject, see "String Matching" section in [Additional Detail on Some Subjects](#additional-detail-on-some-subjects)

------ TOdo: work on below content




- ### Design patterns
    - [ ] [Quick UML review (video)](https://www.youtube.com/watch?v=3cmzqZzwNDM&list=PLGLfVvz_LVvQ5G-LdJ8RLqe-ndo7QITYc&index=3)
    - [ ] Learn these patterns:
        - [ ] strategy
        - [ ] singleton
        - [ ] adapter
        - [ ] prototype
        - [ ] decorator
        - [ ] visitor
        - [ ] factory, abstract factory
        - [ ] facade
        - [ ] observer
        - [ ] proxy
        - [ ] delegate
        - [ ] command
        - [ ] state
        - [ ] memento
        - [ ] iterator
        - [ ] composite
        - [ ] flyweight
    - [ ] [Chapter 6 (Part 1) - Patterns (video)](https://youtu.be/LAP2A80Ajrg?list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO&t=3344)
    - [ ] [Chapter 6 (Part 2) - Abstraction-Occurrence, General Hierarchy, Player-Role, Singleton, Observer, Delegation (video)](https://www.youtube.com/watch?v=U8-PGsjvZc4&index=12&list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO)
    - [ ] [Chapter 6 (Part 3) - Adapter, Facade, Immutable, Read-Only Interface, Proxy (video)](https://www.youtube.com/watch?v=7sduBHuex4c&index=13&list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO)
    - [ ] [Series of videos (27 videos)](https://www.youtube.com/playlist?list=PLF206E906175C7E07)
    - [ ] [Head First Design Patterns](https://www.amazon.com/Head-First-Design-Patterns-Freeman/dp/0596007124)
        - I know the canonical book is "Design Patterns: Elements of Reusable Object-Oriented Software", but Head First is great for beginners to OO.
    - [ ] [Handy reference: 101 Design Patterns & Tips for Developers](https://sourcemaking.com/design-patterns-and-tips)

- ### Messaging, Serialization, and Queueing Systems
    - [ ] [Thrift](https://thrift.apache.org/)
        - [Tutorial](http://thrift-tutorial.readthedocs.io/en/latest/intro.html)
    - [ ] [Protocol Buffers](https://developers.google.com/protocol-buffers/)
        - [Tutorials](https://developers.google.com/protocol-buffers/docs/tutorials)
    - [ ] [gRPC](http://www.grpc.io/)
        - [gRPC 101 for Java Developers (video)](https://www.youtube.com/watch?v=5tmPvSe7xXQ&list=PLcTqM9n_dieN0k1nSeN36Z_ppKnvMJoly&index=1)
    - [ ] [Redis](http://redis.io/)
        - [Tutorial](http://try.redis.io/)
    - [ ] [Amazon SQS (queue)](https://aws.amazon.com/sqs/)
    - [ ] [Amazon SNS (pub-sub)](https://aws.amazon.com/sns/)
    - [ ] [RabbitMQ](https://www.rabbitmq.com/)
        - [Get Startet](https://www.rabbitmq.com/getstarted.html)
    - [ ] [Celery](http://www.celeryproject.org/)
        - [First Steps With Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
    - [ ] [ZeroMQ](http://zeromq.org/)
        - [Intro - Read The Manual](http://zeromq.org/intro:read-the-manual)
    - [ ] [ActiveMQ](http://activemq.apache.org/)
    - [ ] [Kafka](http://kafka.apache.org/documentation.html#introduction)
    - [ ] [MessagePack](http://msgpack.org/index.html)
    - [ ] [Avro](https://avro.apache.org/)
    
    
- [ ] [Simonson: Approximation Algorithms (video)](https://www.youtube.com/watch?v=oDniZCmNmNw&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=19)



## Session 2 - Putting it all together and Review

  This section will have shorter videos that can you watch pretty quickly to review most of the important concepts.
  It's nice if you want a refresher often.

- [ ] Series of 2-3 minutes short subject videos (23 videos)
    - [Videos](https://www.youtube.com/watch?v=r4r1DZcx1cM&list=PLmVb1OknmNJuC5POdcDv5oCS7_OUkDgpj&index=22)
- [ ] Series of 2-5 minutes short subject videos - Michael Sambol (18 videos):
    - [Videos](https://www.youtube.com/channel/UCzDJwLWoYCUQowF_nG3m5OQ)
- [ ] [Sedgewick Videos - Algorithms I](https://www.youtube.com/user/algorithmscourses/playlists?shelf_id=2&view=50&sort=dd)
    - [ ] [01. Union-Find](https://www.youtube.com/watch?v=8mYfZeHtdNc&list=PLe-ggMe31CTexoNYnMhbHaWhQ0dvcy43t)
    - [ ] [02. Analysis of Algorithms](https://www.youtube.com/watch?v=ZN-nFW0mEpg&list=PLe-ggMe31CTf0_bkOhh7sa5uqeppp3Sr0)
    - [ ] [03. Stacks and Queues](https://www.youtube.com/watch?v=TIC1gappbP8&list=PLe-ggMe31CTe-9jhnj3P_3mmrCh0A7iHh)
    - [ ] [04. Elementary Sorts](https://www.youtube.com/watch?v=CD2AL6VO0ak&list=PLe-ggMe31CTe_5WhGV0F--7CK8MoRUqBd)
    - [ ] [05. Mergesort](https://www.youtube.com/watch?v=4nKwesx_c8E&list=PLe-ggMe31CTeunC6GZHFBmQx7EKtjbGf9)
    - [ ] [06. Quicksort](https://www.youtube.com/watch?v=5M5A7qPWk84&list=PLe-ggMe31CTeE3x2-nF1-toca1QpuXwE1)
    - [ ] [07. Priority Queues](https://www.youtube.com/watch?v=G9TMe0KC0w0&list=PLe-ggMe31CTducy9LDiGVkdSv0NfiRwn5)
    - [ ] [08. Elementary Symbol Tables](https://www.youtube.com/watch?v=up_nlilw3ac&list=PLe-ggMe31CTc3a8nKRDxFZZrWrBvkc9SG)
    - [ ] [09. Balanced Search Trees](https://www.youtube.com/watch?v=qC1BLLPK_5w&list=PLe-ggMe31CTf7jHH_mFT50kayjCEA6Rhu)
    - [ ] [10. Geometric Applications of BST](https://www.youtube.com/watch?v=Wl30aGAp6TY&list=PLe-ggMe31CTdBsRIw0hXln0hilRs-DqAx)
    - [ ] [11. Hash Tables](https://www.youtube.com/watch?v=QA8fJGO-i9o&list=PLe-ggMe31CTcKxIRGqqThMts2eHtSrf11)
- [ ] [Sedgewick Videos - Algorithms II](https://www.youtube.com/user/algorithmscourses/playlists?flow=list&shelf_id=3&view=50)
    - [ ] [01. Undirected Graphs](https://www.youtube.com/watch?v=GmVhD-mmMBg&list=PLe-ggMe31CTc0zDzANxl4I2MhMoRVlbRM)
    - [ ] [02. Directed Graphs](https://www.youtube.com/watch?v=_z-JsVaUS40&list=PLe-ggMe31CTcEwaU8a1P1Gd95A77HV85K)
    - [ ] [03. Minimum Spanning Trees](https://www.youtube.com/watch?v=t8fNk9tfVYY&list=PLe-ggMe31CTceUZxDesGfHGLE7kcSafqj)
    - [ ] [04. Shortest Paths](https://www.youtube.com/watch?v=HoGSiB7tSeI&list=PLe-ggMe31CTePpG3jbeOTsnGUGZDKxgZD)
    - [ ] [05. Maximum Flow](https://www.youtube.com/watch?v=rYIKlFstBqE&list=PLe-ggMe31CTduQ68XQ-sVj32wYJIspTma)
    - [ ] [06. Radix Sorts](https://www.youtube.com/watch?v=HKPrVm5FWvg&list=PLe-ggMe31CTcNvUX9E3tQeM6ntrdR8e53)
    - [ ] [07. Tries](https://www.youtube.com/watch?v=00YaFPcC65g&list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ)
    - [ ] [08. Substring Search](https://www.youtube.com/watch?v=QzI0p6zDjK4&list=PLe-ggMe31CTdAdjXB3lIuf2maubzo9t66)
    - [ ] [09. Regular Expressions](https://www.youtube.com/watch?v=TQWNQsJSPnk&list=PLe-ggMe31CTetTlJWouM42fyttyKPgSDh)
    - [ ] [10. Data Compression](https://www.youtube.com/watch?v=at9tjpxcBh8&list=PLe-ggMe31CTciifRRo6yY0Yt0mzgIXXVZ)
    - [ ] [11. Reductions](https://www.youtube.com/watch?v=Ow5x-ooMGv8&list=PLe-ggMe31CTe_yliW5vc3yO-dj1LSSDyF)
    - [ ] [12. Linear Programming](https://www.youtube.com/watch?v=rWhcLyiLZLA&list=PLe-ggMe31CTdy6dKzMgkWFuTTN1H8B-E1)
    - [ ] [13. Intractability](https://www.youtube.com/watch?v=6qcaaDp4cdQ&list=PLe-ggMe31CTcZCjluBHw53e_ek2k9Kn-S)

---

## Week 10 - Practice

- [ ] **String Matching**
    - [ ] Rabin-Karp (videos):
        - [Rabin Karps Algorithm](https://www.coursera.org/learn/data-structures/lecture/c0Qkw/rabin-karps-algorithm)
        - [Precomputing](https://www.coursera.org/learn/data-structures/lecture/nYrc8/optimization-precomputation)
        - [Optimization: Implementation and Analysis](https://www.coursera.org/learn/data-structures/lecture/h4ZLc/optimization-implementation-and-analysis)
        - [Table Doubling, Karp-Rabin](https://www.youtube.com/watch?v=BRO7mVIFt08&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=9)
        - [Rolling Hashes, Amortized Analysis](https://www.youtube.com/watch?v=w6nuXg0BISo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=32)
    - [ ] Knuth-Morris-Pratt (KMP):
        - [TThe Knuth-Morris-Pratt (KMP) String Matching Algorithm](https://www.youtube.com/watch?v=5i7oKodCRJo)
    - [ ] Boyer–Moore string search algorithm
        - [Boyer-Moore String Search Algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm)
        - [Advanced String Searching Boyer-Moore-Horspool Algorithms (video)](https://www.youtube.com/watch?v=QDZpzctPf10)
    - [ ] [Coursera: Algorithms on Strings](https://www.coursera.org/learn/algorithms-on-strings/home/week/1)
        - starts off great, but by the time it gets past KMP it gets more complicated than it needs to be
        - nice explanation of tries
        - can be skipped



## Coding exercises/challenges

Once you've learned your brains out, put those brains to work.
Take coding challenges every day, as many as you can.

- [ ] [How to Find a Solution](https://www.topcoder.com/community/data-science/data-science-tutorials/how-to-find-a-solution/)
- [ ] [How to Dissect a Topcoder Problem Statement](https://www.topcoder.com/community/data-science/data-science-tutorials/how-to-dissect-a-topcoder-problem-statement/)

Challenge sites:
- [LeetCode](https://leetcode.com/)
- [TopCoder](https://www.topcoder.com/)
- [Project Euler (math-focused)](https://projecteuler.net/index.php?section=problems)
- [Codewars](http://www.codewars.com)
- [HackerRank](https://www.hackerrank.com/)
- [Codility](https://codility.com/programmers/)
- [InterviewCake](https://www.interviewcake.com/)
- [InterviewBit](https://www.interviewbit.com/invite/icjf)

Maybe:
- [Mock interviewers from big companies](http://www.gainlo.co/)

## Once you're closer to the interview

- [ ] Cracking The Coding Interview Set 2 (videos):
    - [Cracking The Code Interview](https://www.youtube.com/watch?v=4NIb9l3imAo)
    - [Cracking the Coding Interview - Fullstack Speaker Series](https://www.youtube.com/watch?v=Eg5-tdAwclo)
    - [Ask Me Anything: Gayle Laakmann McDowell (author of Cracking the Coding Interview)](https://www.youtube.com/watch?v=1fqxMuPmGak)




## General Tips


### Resume Tips

- [Ten Tips for a (Slightly) Less Awful Resume](http://steve-yegge.blogspot.co.uk/2007_09_01_archive.html)
- See Resume prep items in Cracking The Coding Interview and back of Programming Interviews Exposed

## Interview Tips


### Coding Question Practice

Now that you know all the computer science topics above, it's time to practice answering coding problems.

**Coding question practice is not about memorizing answers to programming problems.**

Why you need to practice doing programming problems:
- problem recognition, and where the right data structures and algorithms fit in
- gathering requirements for the problem
- talking your way through the problem like you will in the interview
- coding on a whiteboard or paper, not a computer
- coming up with time and space complexity for your solutions
- testing your solutions

There is a great intro for methodical, communicative problem solving in an interview. You'll get this from the programming
interview books, too, but I found this outstanding:
- [ ] [Algorithm design canvas](http://www.hiredintech.com/algorithm-design/)

No whiteboard at home? That's fine, buy one. Or don't if that's really an issue, but just practice on paper and practice whiteboarding skills at school or something. You should really practice on whiteboard though, to mimick the real interview setting. But the main thing you want to practice is to practice under stress, there's nothing like coding in front of a guy who is going to decide whether you get a job or not, and then you're as nervous as you've never been before. 

The solution? Practice that. How? Every interview you get the opportunity in doing, do it. Even if it's a company you don't care much about, you will still be practicing coding while someone else is looking at you and your subconscious mind constantly fighting you by making you afraid of being embarassed. Trust me, I had the biggest issues with this, the only way to get over it was to interview dozens and dozens of times, just like speaking in public or anything of the sort. The more you do it, the more you realize the worst case scenario is not nearly as big of a deal as your pessimistic-self anticipates, and in that process you will become less and less nervous each time you attempt something similar.

Supplemental:

- [Mathematics for Topcoders](https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/)
- [Dynamic Programming – From Novice to Advanced](https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/)
- [MIT Interview Materials](https://web.archive.org/web/20160906124824/http://courses.csail.mit.edu/iap/interview/materials.php)
- [Exercises for getting better at a given language](http://exercism.io/languages)
   


#### Interview Questions

Think of about 20 interview questions you'll get, along the lines of the items below. Have 2-3 answers for each.
Have a story, not just data, about something you accomplished.

- Why do you want this job?
- What's a tough problem you've solved?
- Biggest challenges faced?
- Best/worst designs seen?
- Ideas for improving an existing Google product.
- How do you work best, as an individual and as part of a team?
- Which of your skills or experiences would be assets in the role and why?
- What did you most enjoy at [job x / project y]?
- What was the biggest challenge you faced at [job x / project y]?
- What was the hardest bug you faced at [job x / project y]?
- What did you learn at [job x / project y]?
- What would you have done better at [job x / project y]?

#### Questions for the interviewer

- How large is your team?
- What does your dev cycle look like? Do you do waterfall/sprints/agile?
- Are rushes to deadlines common? Or is there flexibility?
- How are decisions made in your team?
- How many meetings do you have per week?
- Do you feel your work environment helps you concentrate?
- What are you working on?
- What do you like about it?
- What is the work life like?

#### Once You've Got The Job

- [10 things I wish I knew on my first day at Google](https://medium.com/@moonstorming/10-things-i-wish-i-knew-on-my-first-day-at-google-107581d87286#.livxn7clw)



## Books (if you are thirsty for success please be thirsty for knowledge, reading, and learning).
- [Programming Pearls](http://www.amazon.com/Programming-Pearls-2nd-Jon-Bentley/dp/0201657880)
- [Grokking Algorithms](https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230)
- [Write Great Code: Volume 1: Understanding the Machine](https://www.amazon.com/Write-Great-Code-Understanding-Machine/dp/1593270038)
- [Elements of Programming Interviews](https://www.amazon.com/Elements-Programming-Interviews-Insiders-Guide/dp/1479274836)
- [Introduction to Algorithms](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844)
- [Algorithm Design Manual](http://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202) (Skiena)
- [The Unix Programming Environment](http://product.half.ebay.com/The-UNIX-Programming-Environment-by-Brian-W-Kernighan-and-Rob-Pike-1983-Other/54385&tg=info)
- [The Linux Command Line: A Complete Introduction](https://www.amazon.com/dp/1593273894/)
- [TCP/IP Illustrated Series](https://en.wikipedia.org/wiki/TCP/IP_Illustrated)
- [Head First Design Patterns](https://www.amazon.com/gp/product/0596007124/)
- [Design Patterns: Elements of Reusable Object-Oriente​d Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)
- [Site Reliability Engineering](https://landing.google.com/sre/book.html)
- [UNIX and Linux System Administration Handbook, 4th Edition](https://www.amazon.com/UNIX-Linux-System-Administration-Handbook/dp/0131480057/)
- - [Programming Interviews Exposed: Secrets to Landing Your Next Job, 2nd Edition](http://www.wiley.com/WileyCDA/WileyTitle/productCd-047012167X.html)
- [Cracking the Coding Interview, 6th Edition](http://www.amazon.com/Cracking-Coding-Interview-6th-Programming/dp/0984782850/)
- [Elements of Programming Interviews](https://www.amazon.com/Elements-Programming-Interviews-Insiders-Guide/dp/1479274836)
- [Python Machine Learning](https://www.amazon.com/Python-Machine-Learning-Sebastian-Raschka/dp/1783555130/)
- [Data Science from Scratch: First Principles with Python](https://www.amazon.com/Data-Science-Scratch-Principles-Python/dp/149190142X)
- [Introduction to Machine Learning with Python](https://www.amazon.com/Introduction-Machine-Learning-Python-Scientists/dp/1449369413/)
- [Machine Learning for Software Engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)
      





