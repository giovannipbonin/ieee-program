# Week 4

## Some Updates
1. The link to me: www.tinyurl.com/swe-python4
2. Join our Slack! https://umiami-orgs.slack.com/messages/C98DU69QF/

### Code Online
https://www.google.com/search?q=python3+repl&btnI=

### Review: Functions and Dictionaries
```
def function_name(argument1, argument2):
    # The body of the function
    return some_value
```

```
students = dict()
students['dxm11'] = 'Devin Michaels'
students['dwg11'] = 'David Grossman'

devin = students['dxm11']
print(devin)
```

# Functions

## Default Arguments

1. You can use them if you'd like! But by default, they have a specified value.
2. Don't set `list`s, `dict`s as default values!
```
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

## Miscellaneous Notes
1. Nameyour parameters when you call them! It can make code easier to read
Meh...
```
twitter_search('@obama', False, 20, True)
```
Better!
```
twitter_search('@obama', retweets=False, numtweets=20, popular=True)
```

# Creating simple sequences: Tuples
```
person = 'Raymond', 'Hettinger', 30, 'python@example.com'
fname, lname, age, email = p
print(lname)
```

# Setting up your own Environment
1. First, head to https://www.python.org/downloads/ and download Python 3.6.X
2. We will need to have Python installed locally to do some of the next work
3. I personally prefer writing Python code in PyCharm. [Check it out!] (https://www.jetbrains.com/pycharm/)
4. If you are adventurous, check out [Python Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


# The Command Line
What is "The Command Line"?

## Some command line basics on Unix/Linux systems
1. `ls` - List files
2. `cd` - Change "directory" or folders
3. `cd ~` - Go to your home directory
4. `cd ~/code` - Go to your home directory and then into the folder "code"
5. I would recommend learning `vim` or `emacs` if you're planning to code for a long time. It makes life a lot easier
6. `vim` and `emacs` are ways to edit text files from the command line.

# Reading and writing files

```
file = open("file.txt")
data = file.read()
print(data)
file.close()

```
## Some Useful Functions and Shortcuts
```
# Iterates over each line in the file
for line in file:
  print(line)
```

```
# Returns a list with each line being a line from the file
list_of_lines = file.readlines()
```


```
with open("file.txt") as f:
    data = f.read()
    print(data)
```

# Let's Play with Some Files!
1. Download this file [here]()
2. Or, go for the full sized file [here](https://github.com/dwyl/english-words/blob/master/words_alpha.txt). Note: It is 4MB.

3. What our task is for the rest of the day: Figure out if the user inputs a word, is it in our dictionary.
      - AND: Write our responses to a new file.
4. Some useful functions: "string1 string2".split(" ")

# Something fun
```
import os
os.system('say "your program has finished"')
```

# Some practice for home
1. If you have done the String Compression problem from last week, try compressing `words.txt`. Does it get smaller?
2. If you did the Pig Latin program, try converting every word in `words.txt` into Pig Latin and then write it to file.
3. Do the same as above except for your cipher program!

# Survey
https://docs.google.com/forms/d/e/1FAIpQLScl4sS6iKYGkyBnfTisGtaeuYDfyzpTEVzdxwQIZ1XgPEQ2QQ/viewform?usp=sf_link
