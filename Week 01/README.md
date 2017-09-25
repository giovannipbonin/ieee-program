### Hash Tables
 - Hash Tables are beautiful things and extremely useful in a very large and diverse domain of applications. If you have seen them before, and you are under the impression that they are complicated, just forget anything you know about them. They are quite straightforward:
      - Starting with the easy part, "table", we have a data structure that represents a table mapping a value generally represented as a string, to another value of any type. That's what a table is, and if hash tables were just the running time to find a value in the table would be O(n), and it wouldn't be very useful.
       -> That's the power of "hashing", where we take the key which is the value that maps to another, and process it with a function (for example adding the ascii characters modulo the number of entries in the table, which works but we will later see can be optimized substantially), and finds where in the table it belongs
       - Know how hash tables are implemented, but more importantly know how to use them to build new systems.
       
Videos:
-  [Core Hash Tables (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/m7UuP/core-hash-tables)
- [Dealing with Collisions] (https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/ozYZh/core-collisions-in-hash-tables)
-  [Phone Book Problem (video)](https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-problem)


-  [Video Lectures on Hash Tables](https://www.coursera.org/learn/data-structures/home/week/3)
- [On Designing a Fast Hash Table] (http://www.ilikebigbits.com/blog/2016/8/28/designing-a-fast-hash-table)

![alt text](http://slideplayer.com/slide/1649208/7/images/32/Double+Hashing+h(+k,+i+)+=+(+h1(k)+++i+*+h2(k)+)+mod+m.jpg)
       
       
### String Builders
- In java, how many Strings are created in this line of code?
```
String s = "h" + "e" + "l" + "l" + "o"
```
- With StringBuilder, use `append(String)`
- [StringBuilder Example Use](https://docs.oracle.com/javase/tutorial/java/data/buffers.html)
- What's the meta-point? --> Implementation matters.


### Linked List
- If we use a list however, which is a series of items (call them nodes) connected by links, all we have to do is make the new element point to the first element of the array. If we want to insert elsewhere, it's similar, we just need to get the preceeding element and have its link point to the new element, and have the new element point to the one after the original element. And it follows that this takes O(1), whereas retrieving the Nth element takes O(N)

Video: 
- [Singly Linked Lists (video)](https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists)
- [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/rjBs9/core-linked-lists-vs-arrays)
- [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays)



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
 

### Home Reading:
- [Neural Networks for Machine Learning](https://www.coursera.org/learn/neural-networks)
- [How Google Is Remaking Itself As A Machine Learning First Company](https://backchannel.com/how-google-is-remaking-itself-as-a-machine-learning-first-company-ada63defcb70)
- [Large-Scale Deep Learning for Intelligent Computer Systems (video)](https://www.youtube.com/watch?v=QSaZGT4-6EY)
- Deep Learning and Understandability versus Software Engineering and Verification by Peter Norvig](https://www.youtube.com/watch?v=X769cyzBNVw)
- [Google's Cloud Machine learning tools (video)](https://www.youtube.com/watch?v=Ja2hxBAwG_0)
- [Google Developers' Machine Learning Recipes (Scikit Learn & Tensorflow) (video)](https://www.youtube.com/playlist?list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal)
- [Tensorflow (video)](https://www.youtube.com/watch?v=oZikw5k_2FM)
- [Tensorflow Tutorials](https://www.tensorflow.org/versions/r0.11/tutorials/index.html)
- [Practical Guide to implementing Neural Networks in Python (using Theano)](http://www.analyticsvidhya.com/blog/2016/04/neural-networks-python-theano/)
