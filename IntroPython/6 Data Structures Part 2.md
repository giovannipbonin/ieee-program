# Week 6: Data Structures Part 2
1. Thinking about runtime
1. Runtime of list and dictionary operations
1. Tuples and sets

## Some Updates
1. Check out [Coursera's Python Sequence](https://www.coursera.org/specializations/python)
    - It's great to learn a language from a couple of different perspectives
1. Fun stuff: Go read some of Paul Graham's Essays
    - http://www.paulgraham.com/love.html
1. A [bug](https://github.com/will8211/unimatrix) on my computer

## The Rest of the Semester
We've got 5 classes left. Here are some ideas of what we can cover:
#### The "Musts"
1. Classes and Error Handling
2. Iterators and Generators
3. Functional Python (`map`, `reduce`)

#### The Fun Ones
1. `pandas` - data manipulation and data analysis
2. `matplotlib` - data visualization
3. `flask` - building your own server
4. Intro to Machine Learning in Python
5. Programming challenges / Projects

## Version Control: Git
1. First, it's super practical to run programs on your own computer.
2. `Repl.it` is fantastic, but over the long term, use Python on your computer
3. Saving code matters. Sharing code matters! Use Git.
    - [90% of developers](https://insights.stackoverflow.com/survey/2018/#work-version-control) use Git
4. For now, just use a [GitHub account](github.com/)
5. But at home, definitely [download Git](https://git-scm.com/downloads)

## Thinking about Program Efficiency
- Exact speed is hard to measure
    - Depends on the computer hardware, whatever else is running on the computer, etc
- Instead, we evaluate programs and algorithms based on how fast they are in relationship to the input size
    - If I increase the input by 1, how will the runtime change?
    - If I double the input, how will the runtime change?
- We will use a measure of runtime called _**Big-O**_
    - [Big O Cheat Sheet](http://bigocheatsheet.com/)


#### Some Examples
- `n^2 - 5n + 1000 = O(N^2)`

```python
N = 100
for i in range(N):
  for j in range(N):
    print(i*j)
```

#### Some Useful Names
1. O(1) - constant
1. O(log(n)) - logarithmic
1. O(N) - linear 
1. O(n^2) - quadratic
![](https://cdn-images-1.medium.com/max/1500/1*_nsMVEEkIr1CH8aHjTNbzA.jpeg)

#### Big-O Notation
- Mathematically, if we have a function `f(x)`, we say `O(f(x)) = g(x)` if we can find a number `C` and a number `N` for which all `x > N`
    - Then `|f(x)| ≤ C|g(x)|`
- Intuitively, for a mathematical function, it's the component that will have the biggest impact on the run time
    - Not worrying about constants
- `O(1)` - The algorithm's performance will be the same no matter how big the input is
- `O(N)` -  The algorithm's performance will be directly proportional to the size of the input

### How Lists Work
1. A chunk of memory that is all next to each other
    - The first element is right next to the second element
1. That chunk can grow and shrink

### List Operations and Their Runtime
```python
list.append(x)    # O(1)
list.insert(i, x) # O(N)
del list[i]       # O(N), need to shift all elements after index i over
del list[-1]      # O(1), same as list.pop()
list.index(x)     # O(N), need to search through whole list
list.remove(x)    # O(N), how would you implement with `index` and `delete`
```
- The lookup problem: It is slow to find where a specific element is in our array.
    - How can we do it in `O(1)` time?

### How Dictionaries Work
1. There's a magical function that gives you a unique number for each input
    - AND, if you give that same input to your magical function, you will get the _same_ exact number
2. Based on this unique number, put that number somewhere in your list
    - A simple method is to take that unique number and take the remainder when you divide by the size of the array
    - `MagicNumber % len(DictionaryList)`
3. When you want to look up to see if an input is in your dictionary, give it to your magical function
4. Our lookup problem is now solved in `O(1)` time!
5. In order to get the input never to change, we can't use data structures that can change
    - No lists! We can append to lists, delete from lists, etc. They change!
6. You can still iterate over the keys and values in a dictionary!
    - But _**BEWARE**_: They will not necessarily be in the same order as you added them.
    - Maybe in Python3

### Tuples to the Rescue!
1. Lists of fixed size
    - Easy to make. Easy to break apart
2. They are immutable. You can't change them

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> x, y, z = t
>>> x
12345
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

### Sets
1. The same lookup properties as dictionaries, but with no values
2. Good if you just want to keep track of certain unique items

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> s = set()
>>> s

>>> s.add(5)
>>> s.add(3)
>>> s.add(8)
>>> s
{8, 3, 5}
```


## Python Exercises to Get Things Rolling
1. [Google Python Exercises](https://github.com/2gotgrossman/google-python-exercises)
    - [Original exercises and course](https://developers.google.com/edu/python/exercises/basic)
    - Start with the `basic` folder. Lots of good stuff!
    - Solutions are provided. Try to go as far as you can yourself, but don't be afraid to get help
    - Reading other people's code is super useful.
2. Don't underestimate the importance of grinding through exercises and practice!
    - Coding is a craft. Loving it makes it super easy to do it well
3. Using git, `git clone https://github.com/2gotgrossman/google-python-exercises.git` or `git clone git@github.com:2gotgrossman/google-python-exercises.git`
    

