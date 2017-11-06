## Math Logic and Puzzles

### Combinatorics (n choose k) & Probability
- [ ] [Math Skills: How to find Factorial, Permutation and Combination (Choose) (video)](https://www.youtube.com/watch?v=8RRo6Ti9d0U)
- Bayes theorem: https://www.youtube.com/watch?v=2Df1sDAyRvQ 
- Expected value: https://www.youtube.com/watch?v=q27iV8y4fdM

### Probability:
- [ ] [Basic Theoretical Probability](https://www.khanacademy.org/math/probability/probability-and-combinatorics-topic)  
- [ ] [Probability Explained (video)](https://www.youtube.com/watch?v=uzkc-qNVoOk&list=PLC58778F28211FA19)
- [ ] MIT **Probability** (mathy, and go slowly, which is good for mathy things) (videos)
- [ ] [MIT 6.042J - Probability Introduction](https://www.youtube.com/watch?v=SmFwFdESMHI&index=18&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Conditional Probability](https://www.youtube.com/watch?v=E6FbvM-FGZ8&index=19&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Independence](https://www.youtube.com/watch?v=l1BCv3qqW4A&index=20&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Random Variables](https://www.youtube.com/watch?v=MOfhhFaQdjw&list=PLB7540DEDD482705B&index=21)
- [ ] [MIT 6.042J - Expectation I](https://www.youtube.com/watch?v=gGlMSe7uEkA&index=22&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Expectation II](https://www.youtube.com/watch?v=oI9fMUqgfxY&index=23&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Large Deviations](https://www.youtube.com/watch?v=q4mwO2qS2z4&index=24&list=PLB7540DEDD482705B)
- [ ] [MIT 6.042J - Random Walks](https://www.youtube.com/watch?v=56iFMY8QW2k&list=PLB7540DEDD482705B&index=25)

- [Mathematics for Topcoders](https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/)

![alt text](https://camo.githubusercontent.com/e45e39c36eebcc4c66e1aecd4e4145112d8e88e3/687474703a2f2f692e696d6775722e636f6d2f6a6a3341354e382e706e67)

# System Design and Scalability: A soft intro

##### _Why systems matter_
We expect things to happen quickly when we interact with the internet. When designing large systems, speed really matters.
1. Fact: A 100-millisecond delay in load time can hurt conversion rates by up to 7%
2. Fact: A 2-second delay in load time can hurt bounce rates by up to 103%
3. Fact: At scale, a 1 second delay can be the difference between life and death.

### Performance vs scalability
* A service is scalable if it results in increased performance in a manner proportional to resources added. Generally, increasing performance means serving more units of work, but it can also be to handle larger units of work, such as when datasets grow.
* If you have a performance problem, your system is slow for a single user.
* If you have a scalability problem, your system is fast for a single user but slow under heavy load.

### Latency vs throughput
* Latency is the time to perform some action or to produce some result.
* Throughput is the number of such actions or results per unit of time.
* Generally, you should aim for maximal throughput with acceptable latency.

### Availability vs consistency
* CAP Theorem

### Horizontal vs. Vertical Scaling
* Vertical Scaling is easier, but limited
* Map-Reduce

### Load Balancers
[Peecture](https://camo.githubusercontent.com/21caea3d7f67f451630012f657ae59a56709365c/687474703a2f2f692e696d6775722e636f6d2f6838316e39694b2e706e67)

### Design for failure: Redundancy
1. Databases that have multiple replicas
2. Master / Master vs. Master / Slave

### There is no perfect system. Everything depends on *your* system
1. Read-heavy vs. Write-heavy tasks
2. Ensure your design works if scale changes by 10X or 20X, but the right solution for X often not optimal for 100X.

[Numbers everyone should know](https://everythingisdata.wordpress.com/2009/10/17/numbers-everyone-should-know/)'

[The System Design Primer](https://github.com/donnemartin/system-design-primer)


