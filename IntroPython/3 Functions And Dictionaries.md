# Week 2

## Some Updates
1. The link to me: www.tinyurl.com/swe-python1
2. Join our Slack! https://umiami-orgs.slack.com/messages/C98DU69QF/
3. HackerRank is a great resource
      - [30 Days of Code](https://www.hackerrank.com/challenges/30-hello-world/problem)


### Code Online
https://www.google.com/search?q=python3+repl&btnI=

### Review: Ifs and Loops
```
my_number = 42
for i in range(5, 100):
  if 500 % my_number == 0:
    print(i)
  elif my_number % i == 0:
    print(i)
    break
  
  print("My number is divisible by....")
```

# Functions
1. Mathematical Functions
2. Breaking up your code into smaller parts.
      - Programmers are lazy. Don't repeat what you write

```
def function_name(argument1, argument2):
    # The body of the function
    return some_value
```

### Square
```
def square(x):
    return x*x
```


### The Happy Birthday Problem
```
def happyBirthdayEmily():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")

def happyBirthdayAndre():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Andre.")
    print("Happy Birthday to you!")

def main():
    happyBirthdayEmily()
    happyBirthdayAndre()
```

Example: [The Staircase Problem](https://www.hackerrank.com/challenges/staircase/problem)

# Dictionaries!!!
1. What are dictionaries? Maps, key-value pairs, hash tables (???)
2. Creating a dictionary: `dict()` or `{}`
3. Adding elements: `my_dict[new_key] = new_value`
4. Checking to see if a key is in your dictionary `key in my_dict`
5. Iterating over items in a dictionary: THE POWER OF ITERATION!


```
city_population = { "New York City":8550405, 
                    "Los Angeles":3971883, 
                    "Toronto":2731571, 
                    "Chicago":2720546, 
                    "Houston":2296224, 
                    "Montreal":1704694, 
                    "Calgary":1239220, 
                    "Vancouver":631486, 
                    "Boston":667137
                    }
```

If interested, take a look at `from collections import defaultdict`. 

# Functions are values...??? And lambda functions
1. `lambda x : x*x`
2. `cube_me = lambda x : x * x * x`
    - This is equivalent to the following:
``` 
def cube_me2(x):
      cube = x**3
      return cube
```

# Reading and writing files
```
with open("file.txt", "wb") as f:
    print(f.read())
```

# Ciphers and Encodings
Add a shift to each letter in a message
'abc' + 1 = 'bcd'
'aaa' + 2 = 'ccc'

# Some practice for home
1. https://www.hackerrank.com/challenges/python-lists/problem
2. String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string `aabcccccaaa` becomes `a2b1c5a3`. Bonus: If the string would not become smaller than the original string, then you should return the original string.
3. If I give you a file that contains all the words in the English langauge, can you tell me if a text file has only English words?
4. Implement a function to determine if a string has all unique characters. So given "hello", you should return False. And given "you are", you should return True.
