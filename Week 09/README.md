# PYTHON!!!

## Why use Python
1. A quick scripting language
2. Back-End development
3. Data Science and Machine Learning
4. Internet of Things

## The Zen of Python
``` import this ```

## Environment Setup
1. PyCharm
2. Anaconda
3. Or choose your own IDE 

## Python 2.7 or Python 3.6 ??
If you're just starting, head for the world of Python3.

## Basic Types
1. `int`s
2. `float`s
3. `string`s
4. `list`s
5. `dict`s
6. Objects
7. `tuple`s
8. `set`s

## Slicing and Dicing
1. `[i]`
2. `[:i]`
3. `[-i]`

## Basic Control
1. `for` loops
2. Iterators
3. `while` loops
4. `if`, `else`, `elif`
5. `break`
6. `continue`
7. `else`

## Basic functions
1. For lists: `append`, `del`
2. `len`, `id`, `hash`

## Functions 101
```
def func(param1, param2):
   do_something(param1)
   value = do_another_thing(param2)
   return value
```

1. keyword arguments
2. `*arguments`, `**keywords`

## module mania
```
from god import universe as uni

uni.create_life()
uni.create_python()

assert uni.is_perfect() == True
```

1. pandas, numpy, and scipy
2. requests
3. sys
4. math, random, statistics
5. timeit
6. matplotlib.pyplot as plt
7. collections - cool data structures
8. There are modules for threading and multi-processing
9. https://docs.python.org/3/tutorial/stdlib.html

## Looping techniques: for loops and beyond
1. `map` and `filter`
2. List comprehensions
3. Dictionary Comprehensions
4. Set comprehensions

## Tuple Packing and unpacking
1. `a, b = b, a`

## Classes
https://docs.python.org/3/tutorial/classes.html
```
class MyClass(SuperClass):
   static_var = 5

   __init__(self, my_name):
      self.name = my_name
```

What do you do when there's no private variables?

## Functions as first-class data
```
def a_plus_b(a, b):
   return a + b

def apply_function_to_list_of_pairs(list_of_pairs, function):
   new_list = []
   for (a, b) in list_of_pairs:
      new_list.append( function(a, b) ) 
   return new_list

l = zip( range(5,10), range(15,25, 2) )
new_list = apply_function_to_list_of_pairs(l, a_plus_b)

print(new_list)
```
   
## Scope in Python
https://www.python-course.eu/python3_global_vs_local_variables.php

