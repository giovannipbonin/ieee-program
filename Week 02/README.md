## Review of Big-Oh Notation, Stacks, and maybe Python

`from collections import deque`: [Python's built-in library](https://docs.python.org/2/library/collections.html#collections.deque) for fast insertion and deletion on either side of list.

### Python
#### Getting to know some Python
1. `list` == `array`
2. `dictionary` == `HashTable`
    + `{}` or `dict()` Creates a new empty dictionary
3. `for i in range(10)` == `for(int i = 0; i < 10; i++)`
    + The difference though, is that Python's `for` will only iterate through items
4. Indentation == `{}`
5. `import this`
    + Python tries to make life really easy for you. Just focus on what matters for your problem
6. First class functions!
7. List Comprehensions!!!
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
    
### Functional Programming!!

![alt text](https://img.svbtle.com/ygckjhtzktb78w.jpg)
