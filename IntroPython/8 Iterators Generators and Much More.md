# Week 8: Iterators and Generators
1. 
1. Thinking about creating new _types_
1. Dealing with what happens when your code goes bad
    - Errors and what to do about them

# Sensentia Talk on Semantic Networks
1. Natural Language Processing, AI, etc
1. Tomorrow at 7pm in MEA 202

## Some Updates
1. Python Practice
    - [Google Python Exercises](https://github.com/2gotgrossman/google-python-exercises)
1. Google Code Jam! 
    - [Good Practice Problems](https://codejam.withgoogle.com/2018/challenges)

## The Rest of the Semester
We've got 3 classes left. We will be covering the following:
1. Intro to Machine Learning in Python
1. Programming challenges / Projects

## Last Week
1. Object Oriented Programming
    - How to create your own data structures
1. Classes and Objects are the way!
1. Error Handling and Exceptions
    - When things go wrong, how can you let the user know?
    - Or how can you make sure things keep on going

## Iterators!
1. Super essential part of Python 3
    - The biggest difference between Python 2 and Python 3
1. An iterator is an object that allows you to traverse a data structure
    - Not all data structurs are traversable (How would you traverse a Car object?)
1. In Python, any class that implements the `__iter__` function is an iterator
1. Common iterators you've seen already:
    - `list`, `dict`, `set`, `tuple`, `range`, `str`
    - We call these things "containers"
    - Let's try out some examples!
1. You iterate over containers all the time!
    - `for i in range(10):`
    - A `for`-loop creates an iterator out of the container you get it
        - Challenge: Implement a function called `for` that takes as paramaters (1) a container and (2) a function

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

## How Do Iterators Work?
1. Iterators implement a function called `next`
    - It either returns the next value of the thing it's iterating over
    - Or it returns a `StopIteration` Error

## Iterator Examples
```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# Super Powerful: We can now deal with infinity as a data structure
class InfiniteRange:
    def __init__(self):
        curr_val = 0
    def __iter__(self):
        return self

    def __next__(self):
        curr_val += 1
        return curr_val
```


## Generators: The Easy Way to Roll Your Own Iterators
- Let's dive right into an example
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for c in reverse("Yo, what's good?"):
    print(c)
```
- Every time `next()` is called on our generator, the code is executed up to `yield`
- We return the `yield` value
- When `next()` is called the next time, we resume the function from where we left off

## The Powerful Concepts
### 1. A Concept to Apply to Many Data Structures
1. The idea of traversing or iterating over data structures is a common one. 
1. Even with the data structures we know thus far, it is pretty powerful

### 2. Saving Memory By Being Lazy
1. We only create a new value when we have to
    - `reverse` returns values on the fly. It doesn't create the whole reversed list and then return the whole list
1. Exercise: Go implement your own `range` function using iterators
    - [Documentation](https://docs.python.org/3/library/functions.html#func-range)

## Taking Iterators to the Next Level
1. Let's talk about some powerful functions that take advantage of iterators
1. These are part of the built in Python

### `zip`
1. What if you want to iterate in a `for` loop over pairs of items?
```python
cities = ['NYC', 'MIA', 'SFO']
states = ['NY', 'FL', 'CA']
for city, state in zip(cities, states):
  print(city + ", " + state)
```

### `enumerate`
1. iterate over a container but give each on a number in order
1. For lists, `enumerate` will give you the index of the element along with the element itself

```python
fishies = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
for i, fish in enumerate(fishies):
    print(fish, "has index", i)
```
1. Exercise: Implement your own `enumerate` using `range` and `zip`

### `map`
1. Super common pattern: Apply a function to elements in an iterator (oftentimes a list) and get a new list back

```python
initial_list = list(range(20))
new_list = []
for i in initial_list:
    new_list.append(i ** 2)

# Do something else on the list
# Example: sum(new_list)
```

1. Why could this actually be a bad thing?
1. There's an Iterator for that!

```python
def map(function, iterator):
    for val in iterator:
        yield function(val)

initial_list = list(range(20))
new_values = map(lambda x: x ** 2, initial_list)
```
1. You can `map` a `map` object

### Exercises
1. Implement on your own the following functions
    - `filter`: `filter` takes in a function and an iterator.
        - for each value of the iterator, if applying the function of the value returns `True`, `yield` that value
        - Otherwise, continue to the next element
    - `accumulate`: The running sum of elements
        - `accumulate([1,2,3,4,5]) --> 1 3 6 10 15`
1. Great library to play with: `itertools`
    - https://docs.python.org/3/library/itertools.html

