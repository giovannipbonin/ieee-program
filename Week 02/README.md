## Review of Big-Oh Notation, Stacks, and maybe Python

`from collections import deque`: [Python's built-in library](https://docs.python.org/2/library/collections.html#collections.deque) for fast insertion and deletion on either side of list.

### Python
#### Getting to know some Python


1. Some data structures and basic syntax
    + `list` == `array`
        + `[]` or `list` creates a new empy list
    + `dictionary` == `HashTable`
        + `{}` or `dict()` creates a new empty dictionary
    + `for i in range(10)` == `for(int i = 0; i < 10; i++)`
        + The difference though, is that Python's `for` will only iterate through items
    + Indentation == `{}` in C-like languages and Java
2. Loosely typed system
    + Python knows whether you're dealing with an integer, string, or CSV file
    + BUT BEWARE: It will only catch any errors at runtime
    + This makes writing the first round of code easy, but debugging harder
        + The solution: Testing!
5. `import this`
    + Python tries to make life really easy for you. Just focus on what matters for your problem
6. First class functions!
7. List Comprehensions!!!
    + ![alt text](https://cdn.meme.am/instances/400x/41877559/i-know-list-comprehensions.jpg)
    + How can we iterate through items more simply?
    + https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
8. Starting to touch functional programming:
    + `map`, `filter`, `reduce`
9. Ready to become a Pythonista?
    1. Read the [Python Documentation](https://docs.python.org/2/tutorial/index.html)
    2. Write some code!
    3. Read how Peter Norvig [solved every sudoku puzzle](http://norvig.com/sudoku.html) and [created a spell checker that anyone can implement](http://norvig.com/spell-correct.html)

    









## Queue
- We use queues in our daily lives everywhere, in front of lines in our rollercoaster rides, medical systems, banking, finance, everywhere. And they come in all sorts of forms. The most basic takes only time in consideration, namely the first elements will be the first to be attended.
    - But there are also variations, such as priority queues, which take into consideration a series of factors. For example, in medical organ donation, we might consider the risk of death and urgency for the patient to receive a transplant (very complex system with some simplifications here, and in fact could be optimized with software). 
    - The same applies to computer science, where these queues are useful for designing these systems as well as supporting algorithms such as breadth-first search, and priority queues for A* search.
    
    Breadth-first search basically starts with an element and considers all the elements connected to it, before going to the next level. Whereas A*
    search looks into factors such as the cost of moving to the node and the estimated distance reduction to the goal.
    Video:
    - [ ] [Queue (video)](https://www.coursera.org/learn/data-structures/lecture/EShpq/queue)
    - [ ] [A* Pathfinding Tutorial (video)](https://www.youtube.com/watch?v=KNXfSOx4eEE)
    
## Functional Programming!!

![alt text](https://img.svbtle.com/ygckjhtzktb78w.jpg)


At first, functional programming may seem quite foreign. Some programming languages have a steep learning curve (like Haskell) and are jokingly said to be impractical across all domains. But that cannot be further from the truth. Facebook writes their [spam finder in Haskell](https://code.facebook.com/posts/745068642270222/fighting-spam-with-haskell/) in Haskell. The new release of Java, [Java 8](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html), includes many features from functional programming. Python's first class functions, map/reduce functions, and lambda functions are all functional programming elements. You can write (practically) [functiona JavaScript](https://medium.com/javascript-scene/a-functional-programmers-introduction-to-javascript-composing-software-d670d14ede30). I think I've belabored the point.


### Some neat Functional Programming features:
* *No More Side Effects*: Solving the problem you never knew you had
    + What are the inputs and outputs of a function in C, Java, Python, etc?
    + In other words, what changes in a function in an imperative language?
    + Side effects can act on Memory and/or I/O
    + Without side-effects, parallelization is possible
* First-class and higher-order functions
    + Passing functions around as values
    + [https://www.joelonsoftware.com/2006/08/01/can-your-programming-language-do-this/](https://www.joelonsoftware.com/2006/08/01/can-your-programming-language-do-this/)
* Pure functions
    + Functions with no side effects, just inputs and output(s)
* Recursion and Tail Recursion
    + Iteration is not possible in functional programming languages, but tail recursion is
    + Let me know if you find a good blogpost on it
* Strict versus non-strict evaluation --> Eager vs. lazy evaluation
    + `print length([2+1, 3*2, 1/0, 5-4])`
    + Functional langauges tend to be lazy...in a good way
    + Think about this in an imperative language `if x then y else 1/0` --> If `x==True`, then `z` is never evaluated
* Type Systems
    + Variables have types (int, long, float, String, char, etc)
    + Strongly typed languages (C, Java, Haskell) can remove a lot of Runtime Errors by checking them at compile time
    + [Some are smarter than others](https://softwareengineering.stackexchange.com/questions/279316/what-exactly-makes-the-haskell-type-system-so-revered-vs-say-java)
    + [Diminishing returns of typing](https://blog.merovius.de/2017/09/12/diminishing-returns-of-static-typing.html)
    
### Pair that Functional Programming concept with that Meme!

![alt text](https://camo.githubusercontent.com/8d5b9bbc29baaf9f32dc54a3063ac9cfb3cf06f7/687474703a2f2f696d6775722e636f6d2f304f6c45594e642e706e67)

![alt text](https://cdn-images-1.medium.com/max/1600/1*DzPyfi7TxA6ZS6EsQb5lxg.jpeg)


![alt text](
https://cdn.meme.am/instances/37921079/yo-dawg-i-heard-you-like-functional-programming-so-i-put-functions-in-your-functions-so-you-can-func.jpg)


![alt text](http://s2.quickmeme.com/img/2d/2d71cb0f32d3577dd9d7c79faa988291864660673a9d974edbef9e0549cac9c7.jpg)


### What did I miss?
